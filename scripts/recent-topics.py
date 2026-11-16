#!/usr/bin/env python3
"""Seznam témat, která už vyšla, pro plánování dalšího dne.

Plánovač dostane tento seznam jako podklad a **přísně** vynechá témata
z posledních 3 dnů (Reddit i HN). U HN navíc dostane dnešní Reddit, aby
stejné téma zpracoval jako navazující článek (`souvisi_s`) a ve sloučeném
denním přehledu se spojilo do jedné sekce.

Použití:
    python3 scripts/recent-topics.py 2026-10-27 --source rd
    python3 scripts/recent-topics.py 2026-10-27 --source hn
    python3 scripts/recent-topics.py 2026-10-27 --source rd --check
"""

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

PROJECT = Path(__file__).resolve().parent.parent
LOOKBACK = 3
SKIP_HOSTS = ("reddit.com", "redd.it", "news.ycombinator.com")
STOP = set(
    """a an the to of in on for and or with at by from is are was were be been being
    this that these those it its as into about after before over under more most less
    new says say said how why what who when where will would can could may might not no
    than then them they their our your his her we you i he she but if so just also only
    via using use used gets get make makes made much many one two three first last next
    own same other some such very out up down off again here there all any both each few
    nor too s t don now d ll m o re ve y ain aren couldn didn doesn hadn hasn haven isn
    ma mightn mustn needn shan shouldn wasn weren won wouldn
    a v ve na se si z ze do pro k o u i ze že je to ten ta ty od po při jak co který
    která které už ale nebo než aby když pak ještě jen také jako mezi před za nad pod
    bez přes""".split()
)


def norm_url(url):
    try:
        p = urlparse(url or "")
    except ValueError:
        return ""
    host = (p.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    if not host or any(host == h or host.endswith("." + h) for h in SKIP_HOSTS):
        return ""
    return host + (p.path or "").rstrip("/")


def toks(text):
    text = re.sub(r"[^0-9a-zá-ž]+", " ", (text or "").lower())
    return {w for w in text.split() if len(w) > 2 and w not in STOP}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def load_day(src, day):
    folder = PROJECT / src / day
    plan_path = folder / "_data" / "plan-clanku.json"
    cand_path = folder / "_data" / "candidates.json"
    if not plan_path.is_file() or not cand_path.is_file():
        return []
    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        cand = {c.get("id"): c for c in json.loads(cand_path.read_text(encoding="utf-8"))}
    except (ValueError, OSError):
        return []
    out = []
    for item in plan:
        cid = item.get("id", "")
        c = cand.get(cid, {})
        url = c.get("url") or ""
        bundle = folder / "_data" / "bundles" / f"{cid}.md"
        if bundle.is_file():
            m = re.search(r"^- url:\s*(\S+)", bundle.read_text(encoding="utf-8", errors="replace"), re.M)
            if m:
                url = m.group(1).strip()
        out.append(
            {
                "id": cid,
                "title": item.get("titulek") or c.get("title") or "",
                "original": c.get("title") or "",
                "url": url,
                "merged": item.get("dalsi_ids") or [],
            }
        )
    return out


def pretty_day(day):
    y, m, d = day.split("-")
    return f"{int(d)}. {int(m)}. {y}"


def render_source(src, day, label):
    items = load_day(src, day)
    if not items:
        return []
    lines = [f"#### {label} ({len(items)} článků)"]
    for it in items:
        bits = [f"- **{it['title']}**"]
        if it["original"] and it["original"].strip().lower() != it["title"].strip().lower():
            bits.append(f"původně: {it['original']}")
        if it["url"]:
            bits.append(it["url"])
        bits.append(f"id: {it['id']}")
        lines.append(" — ".join(bits))
    lines.append("")
    return lines


def render(day, source):
    d = date.fromisoformat(day)
    lines = [
        f"# Co už vyšlo – podklad pro plán článků ({pretty_day(day)})",
        "",
        "Témata níže se už objevila. Pravidla jsou u jednotlivých sekcí.",
        "",
    ]
    had = False
    if source == "hn":
        same = render_source("rd", day, "Reddit")
        if same:
            lines += [
                f"## Dnes na Redditu ({pretty_day(day)}) – stejné téma sloučit, nevynechat",
                "",
                "Když kandidát odpovídá některému z těchto témat, zpracuj ho a v plánu uveď "
                "`souvisi_s: <reddit_id>`. Ve sloučeném denním přehledu se spojí do jedné sekce.",
                "",
                *same,
            ]
    lines += [f"## Poslední {LOOKBACK} dny – přísně vynechat", ""]
    for i in range(1, LOOKBACK + 1):
        prev = (d - timedelta(days=i)).isoformat()
        block = []
        block += render_source("rd", prev, "Reddit")
        block += render_source("hn", prev, "Hacker News")
        if block:
            had = True
            lines += [f"### {pretty_day(prev)}", "", *block]
    if not had:
        lines += ["(žádná předchozí témata k dispozici)", ""]
    return "\n".join(lines).rstrip() + "\n"


def check(day, source):
    """Zkontroluje, že den neobsahuje témata z předchozích dnů (přesná URL / titulek)."""
    d = date.fromisoformat(day)
    current = load_day(source, day)
    if not current:
        print(f"{source}/{day}: chybí plán, kontrolu nelze provést")
        return 0
    previous = []
    for i in range(1, LOOKBACK + 1):
        prev = (d - timedelta(days=i)).isoformat()
        previous += load_day("rd", prev)
        previous += load_day("hn", prev)
    hits = 0
    for cur in current:
        cu = norm_url(cur["url"])
        ct = toks(cur["title"])
        for old in previous:
            same_url = bool(cu) and cu == norm_url(old["url"])
            same_title = jaccard(ct, toks(old["title"])) >= 0.7
            if same_url or same_title:
                print(
                    f"OPAKOVÁNÍ: {cur['id']} „{cur['title']}“ × {old['id']} „{old['title']}“"
                )
                hits += 1
                break
    if hits:
        print(f"{source}/{day}: {hits} témat z posledních {LOOKBACK} dnů zůstalo v přehledu")
        return 1
    print(f"{source}/{day}: bez opakování z posledních {LOOKBACK} dnů")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--source", choices=("rd", "hn"), required=True)
    ap.add_argument("--check", action="store_true", help="zkontrolovat hotový den")
    args = ap.parse_args(argv)
    date.fromisoformat(args.date)
    if args.check:
        return check(args.date, args.source)
    sys.stdout.write(render(args.date, args.source))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
