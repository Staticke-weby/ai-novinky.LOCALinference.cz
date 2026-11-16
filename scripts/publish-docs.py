#!/usr/bin/env python3
"""Publikuje `prehled.md` dne na docs-md.com přes MCP server.

Docs MD vykresluje Markdown korektně (čeština v pořádku) a má limit 120 000
znaků na dokument; den má ~35–90 tisíc. Používá se místo yeet.md, jehož webový
font láme českou diakritiku.

**Od 13. 11. 2026** Docs MD zrušil REST API (`POST/PATCH /api/share` vrací 410)
a publikuje se jen přes MCP server `https://docs-md.com/mcp`: jednou
`register_agent` (klíč se ukládá do `logs/docs-md-agent.json`, gitignored),
pak `share_markdown` / `update_share` s tímto `agent_key`.

Dokumenty vytvořené před 13. 11. 2026 nemají vlastníka, ale jejich `edit_token`
(`logs/publish.json`) pořád funguje pro `update_share` — opakovaná publikace
téhož dne tedy aktualizuje stejnou URL.

Čerstvě registrovaný agent má trust `new`: dokumenty žijí max. 30 dní a odkazy
v nich jsou neklikatelné (plain text). Trvalé (`expiry: never`) a klikatelné
odkazy dostane, až bude `established` (14 dní + 5 dokumentů ve 3 dnech), takže
skript bere expiraci z `whoami.limits.max_expiry`.

Nejprve slepí den (`build_prehled.build`), umí ale publikovat i hotový soubor,
typicky sloučený denní přehled `dny/<datum>/prehled.md` z `build-denni.py`
(pozná složku bez `00-index.md`).

Použití:
    python3 scripts/publish-docs.py rd/2026-10-02
    python3 scripts/publish-docs.py hn/2026-10-04
    python3 scripts/publish-docs.py dny/2026-10-26
    python3 scripts/publish-docs.py --dry-run dny/2026-10-26
"""

import importlib.util
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "build_prehled", Path(__file__).resolve().parent / "build-prehled.py"
)
build_prehled = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_prehled)

PROJECT = Path(__file__).resolve().parent.parent
MCP = "https://docs-md.com/mcp"
LOG = PROJECT / "logs" / "publish.json"
AGENT_FILE = PROJECT / "logs" / "docs-md-agent.json"
AGENT_NAME = "reddit-ai-denni-prehled"
AGENT_DESC = (
    "Denní AI přehled z Redditu a Hacker News pro petrbaloun/reddit-clanky-ai"
)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
MAX_CHARS = 120000


def mcp_call(name, arguments, timeout=120):
    """Zavolá jeden MCP nástroj. Vrací structuredContent, u odmítnutí vyhodí SystemExit."""
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
        }
    ).encode("utf-8")
    req = urllib.request.Request(MCP, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json, text/event-stream")
    req.add_header("User-Agent", UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise SystemExit(f"docs-md.com MCP vrátil HTTP {exc.code}: {detail}") from exc

    # Odpověď je jeden server-sent event ("data: {…}"), případně rovnou JSON.
    payload = None
    for line in raw.splitlines():
        if line.startswith("data:"):
            payload = json.loads(line[5:].strip())
            break
    if payload is None:
        payload = json.loads(raw)
    if "error" in payload:
        raise SystemExit(f"docs-md.com MCP chyba: {payload['error']}")
    result = payload.get("result") or {}
    if result.get("isError"):
        text = (result.get("content") or [{}])[0].get("text", "neznámá chyba")
        raise SystemExit(f"docs-md.com odmítl {name}: {text}")
    return result.get("structuredContent") or {}


def agent_key(register=True):
    """Klíč agenta z logs/docs-md-agent.json; při prvním běhu ho zaregistruje."""
    try:
        data = json.loads(AGENT_FILE.read_text(encoding="utf-8"))
        if data.get("agent_key"):
            return data["agent_key"]
    except (FileNotFoundError, ValueError):
        pass
    if not register:
        return None
    result = mcp_call(
        "register_agent",
        {"name": AGENT_NAME, "description": AGENT_DESC, "client": "opencode"},
    )
    AGENT_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENT_FILE.write_text(
        json.dumps(
            {
                "agent_id": result.get("agent_id"),
                "name": result.get("name") or AGENT_NAME,
                "trust": result.get("trust"),
                "created_at": result.get("created_at"),
                "agent_key": result.get("agent_key"),
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    AGENT_FILE.chmod(0o600)
    print(
        f"registrován agent {result.get('name')} "
        f"({result.get('trust')}), klíč uložen do {AGENT_FILE.relative_to(PROJECT)}"
    )
    return result.get("agent_key")


def max_expiry():
    """Nejdelsi expirace, kterou trust level agenta dovolí ('30d', 'never', …)."""
    key = agent_key(register=False)
    if not key:
        return "30d"
    try:
        limits = mcp_call("whoami", {"agent_key": key}).get("limits") or {}
    except SystemExit:
        return "30d"
    return limits.get("max_expiry") or "30d"


def publish(markdown, filename):
    expiry = max_expiry()
    arguments = {
        "agent_key": agent_key(),
        "content": markdown,
        "filename": filename,
        "kind": "report",
        "audience": "čtenáři denního AI přehledu",
        "expiry": expiry,
    }
    try:
        return mcp_call("share_markdown", arguments)
    except SystemExit as exc:
        # Trust se mohl změnit mezi whoami a zápisem — zkus bezpečnou 30d.
        if expiry == "30d" or "expiry" not in str(exc):
            raise
        arguments["expiry"] = "30d"
        return mcp_call("share_markdown", arguments)


def load_log():
    try:
        return json.loads(LOG.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return []


def find_existing(day):
    for rec in reversed(load_log()):
        if rec.get("service") == "docs-md" and rec.get("day") == day:
            return rec
    return None


def update(record, markdown, filename):
    arguments = {"id": record.get("id") or record["url"], "content": markdown}
    if filename:
        arguments["filename"] = filename
    if record.get("editToken"):
        # dokument z doby před 13. 11. 2026 — nemá vlastníka, jen edit token
        arguments["edit_token"] = record["editToken"]
    else:
        arguments["agent_key"] = agent_key()
    return mcp_call("update_share", arguments)


def record(day, result, edit_token=None):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    history = [
        r
        for r in load_log()
        if not (r.get("service") == "docs-md" and r.get("day") == day)
    ]
    entry = {
        "service": "docs-md",
        "day": day,
        "url": result.get("url"),
        "id": result.get("id"),
        "published": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    if edit_token:
        entry["editToken"] = edit_token
    for key in ("expiry", "expires_at", "trust", "links_clickable"):
        if result.get(key) is not None:
            entry[key] = result[key]
    history.append(entry)
    LOG.write_text(json.dumps(history, ensure_ascii=False, indent=1), encoding="utf-8")


def czech_date(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    return f"{d.day}. {d.month}. {d.year}"


def display_name(day):
    """Lidský název pro hlavičku share a og:title na LinkedIn."""
    parts = day.split("/", 1)
    if len(parts) == 2 and re.match(r"^\d{4}-\d{2}-\d{2}$", parts[1]):
        src, date_str = parts
        date = czech_date(date_str)
        if src == "dny":
            return f"Denní AI přehled – {date}.md"
        if src == "rd":
            return f"Reddit AI přehled – {date}.md"
        if src == "hn":
            return f"Hacker News AI přehled – {date}.md"
    return day.replace("/", "-") + ".md"


def prebuilt_count(markdown):
    heads = re.findall(r"^##\s+(.+)$", markdown, re.M)
    return sum(1 for h in heads if h.strip().lower() != "obsah")


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if a != "--dry-run"]
    if len(args) != 1:
        raise SystemExit(
            "použití: publish-docs.py [--dry-run] <složka dne | hotový .md | dny/2026-10-26>"
        )
    target = Path(args[0])
    if target.suffix == ".md":
        out = target
        day = str(out.parent.relative_to(PROJECT)) if out.is_relative_to(PROJECT) else out.parent.name
        markdown = out.read_text(encoding="utf-8")
        n = prebuilt_count(markdown)
    elif (target / "prehled.md").is_file() and not (target / "00-index.md").is_file():
        out = target / "prehled.md"
        day = str(target)
        markdown = out.read_text(encoding="utf-8")
        n = prebuilt_count(markdown)
    else:
        day = args[0]
        out, n = build_prehled.build(day)
        markdown = out.read_text(encoding="utf-8")
    if len(markdown) > MAX_CHARS:
        raise SystemExit(f"{out} má {len(markdown)} znaků (limit Docs MD je {MAX_CHARS})")
    kind = "témat" if day.startswith("dny/") else "článků"
    if dry:
        print(f"[dry-run] {out}: {len(markdown)} znaků, {n} {kind}, klíč {day}")
        return 0
    filename = display_name(day)
    existing = find_existing(day)
    if existing and (existing.get("editToken") or existing.get("id")):
        result = update(existing, markdown, filename)
        record(
            day,
            {**existing, **result, "url": existing.get("url") or result.get("url")},
            existing.get("editToken"),
        )
        print(f"aktualizováno: {existing['url']}  ({n} {kind})")
    else:
        result = publish(markdown, filename)
        record(day, result)
        print(
            f"publikováno: {result.get('url')}  ({n} {kind}, "
            f"expiry {result.get('expiry')}, trust {result.get('trust')})"
        )
    for notice in result.get("notices") or []:
        print(f"  poznámka: {notice}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
