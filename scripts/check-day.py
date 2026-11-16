#!/usr/bin/env python3
"""Kontrola denního souhrnu (rd/<datum> nebo hn/<datum>) před commitem.

Ověří, že každý článek (`<id>_<slug>.md`) má správný prvního řádek `# <id>`,
tučný titulek, řádek metadat a aspoň 3 odstavce prózy, a že odkazy v indexu
a soubory sedí obousměrně. Robustní vůči uvozovkám a diakritice v titulcích
(na rozdíl od inline Pythonu v promptu).

Použití: python3 scripts/check-day.py rd/2026-10-09
Návrat: 0 ok, 1 chyby, 2 špatné argumenty.
"""
import re
import sys
from pathlib import Path

SKIP = {"00-index.md", "prehled.md"}
LINK = re.compile(r"\]\(([^)]+\.md)\)")


def main(argv):
    if len(argv) != 1:
        raise SystemExit("použití: check-day.py <složka dne, např. rd/2026-10-09>")
    base = Path(argv[0])
    idx = base / "00-index.md"
    if not idx.exists():
        raise SystemExit(f"chybí {idx}")

    errs = []
    files = sorted(p.name for p in base.glob("*.md") if p.name not in SKIP)
    for name in files:
        rid = name.split("_", 1)[0]
        lines = (base / name).read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != f"# {rid}":
            errs.append(f"{name}: první řádek není '# {rid}'")
        if len(lines) < 3 or not (lines[1].startswith("**") and lines[1].rstrip().endswith("**")):
            errs.append(f"{name}: chybí tučný titulek na 2. řádku")
        blocks = [b.strip() for b in re.split(r"\n\s*\n", "\n".join(lines[2:])) if b.strip()]
        prose = [b for b in blocks if not b.startswith(("#", "**")) and "·" not in b.split("\n", 1)[0]]
        if len(prose) < 3:
            errs.append(f"{name}: {len(prose)} odstavců prózy (<3)")

    links = LINK.findall(idx.read_text(encoding="utf-8"))
    for link in links:
        if not (base / link).exists():
            errs.append(f"index odkaz neexistuje: {link}")
    for name in files:
        if name not in links:
            errs.append(f"index neodkazuje na {name}")

    print(f"článků: {len(files)}  odkazů v indexu: {len(links)}")
    if errs:
        print("CHYBY:")
        for e in errs:
            print(" -", e)
        return 1
    print("KONTROLA OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
