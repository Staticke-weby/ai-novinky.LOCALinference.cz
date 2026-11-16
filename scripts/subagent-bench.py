#!/usr/bin/env python3
"""Změří rychlost subagentů z OpenCode session databáze.

OpenCode ukládá sessions do SQLite: `session_v2` (řádek na session, včetně dětí
spuštěných nástrojem `subagent`) a `session_message` (JSON s modelem, časy a usage).
Skript z nich spočítá wall-clock běhu, dobu generování a dekódovací tok/s podle modelu.

Použití:
    scripts/subagent-bench.py                    # sessions aktuálního projektu
    scripts/subagent-bench.py <adresář>          # sessions v daném adresáři
    scripts/subagent-bench.py --all              # všechny sessions v DB
    scripts/subagent-bench.py --model opencode-go/muse-spark-1.3-contributor
    scripts/subagent-bench.py --db <cesta>       # jiná DB (výchozí ~/.local/share/opencode/opencode.db)
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DEFAULT_DB = Path.home() / ".local/share/opencode/opencode.db"


def db_path(arg: str | None) -> Path:
    value = arg or os.environ.get("OPENCODE_DB")
    if not value:
        return DEFAULT_DB
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = DEFAULT_DB.parent / path  # relativní override se řeší pod datovým adresářem
    return path


def parse_args(argv: list[str]) -> tuple[Path | None, str | None, bool, Path | None]:
    target: Path | None = None
    only: str | None = None
    everything = False
    db: Path | None = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--all":
            everything = True
        elif arg == "--model":
            i += 1
            only = argv[i]
        elif arg.startswith("--model="):
            only = arg.split("=", 1)[1]
        elif arg == "--db":
            i += 1
            db = db_path(argv[i])
        elif arg.startswith("--db="):
            db = db_path(arg.split("=", 1)[1])
        elif arg in ("-h", "--help"):
            print(__doc__)
            raise SystemExit(0)
        elif arg.startswith("-"):
            raise SystemExit(f"neznámý argument: {arg}")
        else:
            target = Path(arg).expanduser()
        i += 1
    return target, only, everything, db


def session_model(raw: str | None) -> str:
    if not raw:
        return "?"
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    provider, ident = data.get("providerID"), data.get("id")
    if provider and ident:
        return f"{provider}/{ident}"
    return ident or raw


def collect(db: Path, directory: Path | None, only: str | None) -> dict[str, dict]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row

    query = (
        "select id, parent_id, agent, model, directory, time_created, time_updated "
        "from session_v2"
    )
    params: list[str] = []
    if directory is not None:
        query += " where directory = ?"
        params.append(str(directory))

    per_model: dict[str, dict] = defaultdict(
        lambda: {"sessions": set(), "reqs": 0, "gen_ms": 0.0, "stream_ms": 0.0,
                 "out": 0, "in": 0, "cache": 0, "cost": 0.0, "wall": []}
    )
    for session in conn.execute(query, params):
        sid = session["id"]
        wall = ((session["time_updated"] or 0) - (session["time_created"] or 0)) / 1000.0
        fallback = session_model(session["model"])
        for (raw,) in conn.execute(
            "select data from session_message where session_id = ? and type = 'assistant'", (sid,)
        ):
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue
            model = msg.get("model") or {}
            name = f"{model.get('providerID')}/{model.get('id')}" if model.get("id") else fallback
            if only and only not in name:
                continue
            rec = per_model[name]
            if sid not in rec["sessions"]:
                rec["sessions"].add(sid)
                if wall > 0:
                    rec["wall"].append(wall)
            rec["reqs"] += 1
            times = msg.get("time") or {}
            created = times.get("created") or 0
            streamed = times.get("streamed") or times.get("completed") or created
            completed = times.get("completed") or streamed
            rec["gen_ms"] += max(completed - created, 0)
            rec["stream_ms"] += max(streamed - created, 0)
            tokens = msg.get("tokens") or {}
            rec["out"] += int(tokens.get("output") or 0)
            rec["in"] += int(tokens.get("input") or 0)
            rec["cache"] += int((tokens.get("cache") or {}).get("read") or 0)
            rec["cost"] += float(msg.get("cost") or 0)
    conn.close()
    return per_model


def fmt(model: str, r: dict) -> str:
    sessions = len(r["sessions"])
    reqs = r["reqs"]
    out = r["out"]
    stream_s = max(r["stream_ms"], 1.0) / 1000.0
    wall = sorted(r["wall"])
    median_wall = wall[len(wall) // 2] if wall else 0.0
    return (
        f"{model}\n"
        f"  sessions (subagent/souborů): {sessions}   requestů: {reqs}\n"
        f"  výstupních tokenů:   {out}  (vstup {r['in']}, cache-read {r['cache']})\n"
        f"  generování celkem:   {r['gen_ms'] / 1000:.1f} s   stream okno: {stream_s:.1f} s\n"
        f"  output/request:      {out / max(reqs, 1):.0f} tokenů\n"
        f"  dekódování:          {out / stream_s:.1f} tok/s (stream okno, včetně TTFT)\n"
        f"  wall-clock/session:  medián {median_wall:.1f} s, max {wall[-1] if wall else 0:.1f} s, min {wall[0] if wall else 0:.1f} s\n"
        f"  cena:                ${r['cost']:.4f}"
    )


def main() -> int:
    target, only, everything, db = parse_args(sys.argv[1:])
    path = db or DEFAULT_DB
    if not path.exists():
        print(f"nenalezena OpenCode DB: {path}", file=sys.stderr)
        return 1
    directory = None if everything else (target or PROJECT)
    per_model = collect(path, directory, only)
    if not per_model:
        scope = "všech sessions" if everything else f"sessions v {directory}"
        print(f"žádné assistant zprávy v {scope} ({path})")
        return 1
    scope = "vše" if everything else str(directory)
    print(f"# {scope}  ({path})\n")
    for model, r in sorted(per_model.items(), key=lambda kv: -kv[1]["out"]):
        if not r["reqs"]:
            continue
        print(fmt(model, r) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
