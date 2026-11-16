#!/usr/bin/env python3
"""Slepí články jednoho dne do jednoho souboru `prehled.md` pro publikaci.

Vezme složku dne (např. `rd/2026-10-02` nebo `hn/2026-10-04`), přečte `00-index.md`
(kvůli titulku a pořadí článků) a všechny články sloučí do `<složka>/prehled.md`:
titulek přehledu, krátký úvod, obsah a jednotlivé články jako sekce `##`.

Přílohu ani metodiku nepřidává – publikuje se jen skutečný přehled článků.

Použití:
    python3 scripts/build-prehled.py rd/2026-10-02
    python3 scripts/build-prehled.py hn/2026-10-04
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)\s]+\.md)\)")
SKIP = {"00-index.md", "prehled.md"}


def slugify(title):
    """Kotva nadpisu tak, jak ji generuje Docs MD (malá písmena, bez interpunkce,
    mezery na pomlčky, diakritika zůstává)."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    return slug.replace(" ", "-")


def read(path):
    return path.read_text(encoding="utf-8")


def ordered_articles(day_dir):
    """Články v pořadí, v jakém je uvádí index; zbytek dozadu podle názvu."""
    index = day_dir / "00-index.md"
    order = []
    if index.is_file():
        for target in LINK_RE.findall(read(index)):
            path = day_dir / target
            if path.is_file() and path.name not in SKIP and path not in order:
                order.append(path)
    for path in sorted(day_dir.glob("*.md")):
        if path.name not in SKIP and path not in order:
            order.append(path)
    return order


def title_of(day_dir):
    index = day_dir / "00-index.md"
    if index.is_file():
        for line in read(index).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return day_dir.name


def article_title_and_body(path):
    lines = read(path).splitlines()
    # Zahodit první řádek `# <id>`.
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    # Druhý neprázdný řádek bývá tučný titulek -> použijeme jako nadpis sekce.
    title = path.stem
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped:
            match = re.match(r"^\*\*(.+?)\*\*\s*$", stripped)
            if match:
                title = match.group(1).strip()
                lines = lines[:i] + lines[i + 1:]
            break
    body = "\n".join(lines).strip()
    return title, body


def build(day_dir):
    day_dir = Path(day_dir)
    if not day_dir.is_dir():
        raise SystemExit(f"chybí složka: {day_dir}")
    articles = ordered_articles(day_dir)
    if not articles:
        raise SystemExit(f"ve {day_dir} nejsou žádné články")

    date = day_dir.name
    parts = [f"# {title_of(day_dir)}", ""]
    parts.append(f"Denní přehled – **{len(articles)}** článků. Každá sekce je jeden článek v plném znění.")
    parts += ["", "## Obsah", ""]

    parsed = []
    for path in articles:
        title, body = article_title_and_body(path)
        parsed.append((title, body))
        parts.append(f"- [{title}](#{slugify(title)})")
    parts.append("")

    for title, body in parsed:
        parts += ["---", "", f"## {title}", "", body, ""]

    out = day_dir / "prehled.md"
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return out, len(articles)


def main(argv):
    if len(argv) != 1:
        raise SystemExit("použití: build-prehled.py <složka dne, např. rd/2026-10-02>")
    out, n = build(argv[0])
    size = out.stat().st_size
    print(f"{out} ({n} článků, {size} B)")


if __name__ == "__main__":
    main(sys.argv[1:])
