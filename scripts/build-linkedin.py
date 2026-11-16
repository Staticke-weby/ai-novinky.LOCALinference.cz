#!/usr/bin/env python3
"""Vygeneruje příspěvek na LinkedIn z publikovaných denních přehledů.

Styl je pevná šablona (opakovatelná): jedna úvodní věta, pak témata s prefixem
zdroje (`RD:` / `HN:`) a nakonec odkazy na Docs MD.

Témata se vybírají jako **nejlepší podle skóre** (z tabulky v `00-index.md`),
střídavě mezi zdroji. Odkazy bere z `logs/publish.json`. Bez argumentů použije
poslední publikovaný den pro každý zdroj; lze předat i konkrétní složky.

Příspěvek vypíše na stdout a zároveň uloží do `logs/linkedin.txt` (poslední
vygenerovaný), aby ho orchestrující agent mohl vložit do chatu.

Použití:
    python3 scripts/build-linkedin.py
    python3 scripts/build-linkedin.py --den 2026-10-26
    python3 scripts/build-linkedin.py rd/2026-10-02 hn/2026-10-04

`--den` bere sloučený denní přehled (`dny/<datum>/prehled.md` a `temata.json`)
a dá do příspěvku **jeden odkaz** na celý den; stejná témata z Redditu a HN
jsou v něm už sloučená.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "build_prehled", Path(__file__).resolve().parent / "build-prehled.py"
)
build_prehled = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_prehled)

# Sloučený den se od 15. 11. 2026 publikuje na vlastní web (GitHub Pages),
# takže odkaz na `dny/<datum>` je trvalý a nebere se z logs/publish.json.
_site_spec = importlib.util.spec_from_file_location(
    "build_site", Path(__file__).resolve().parent / "build-site.py"
)
build_site = importlib.util.module_from_spec(_site_spec)
_site_spec.loader.exec_module(build_site)

PROJECT = Path(__file__).resolve().parent.parent
LOG = PROJECT / "logs" / "publish.json"
# Poslední vygenerovaný příspěvek (orchestrující agent ho odsud vloží do chatu).
OUT = PROJECT / "logs" / "linkedin.txt"
MAX_HIGHLIGHTS = 10
SOURCE_NAMES = {"rd": "Reddit", "hn": "Hacker News"}
SOURCE_ABBR = {"rd": "RD", "hn": "HN"}
# Buňka tabulky s titulkem má dvě podoby:
#   1) markdown odkaz `[titulek](soubor.md)` (starší indexy; u sloučených postů
#      navíc ` <br>(sloučeno: ID)`),
#   2) prostý text (novější indexy), kde hranaté závorky patří k titulku
#      (`[Smutné] …`, `[AKTUALIZACE] …`) a odkaz na soubor je v samostatném sloupci.
# U podoby 2 se úvodní `[` nesmí odstranit – je součástí titulku. Proto titulní
# buňku bereme jako odkaz jen tehdy, když jí skutečně je (celá sedí na `[…] (….md)`).
LINK_CELL_RE = re.compile(r"^\[(?P<label>.*?)\]\((?P<target>[^()]*\.md)\)(?P<rest>.*)$", re.DOTALL)
MERGED_NOTE_RE = re.compile(r"\s*<br>\s*\(sloučeno:[^)]*\)")


def cell_title(cell):
    """Vytáhne čistý titulek z buňky tabulky (bez odkazu a poznámky o sloučení)."""
    cell = MERGED_NOTE_RE.sub("", cell).strip()
    m = LINK_CELL_RE.match(cell)
    if m:
        return (m.group("label") + m.group("rest")).strip()
    # Není to odkaz – buňka je holý titulek, případné závorky v něm necháme.
    return cell.strip()

INTRO = "Denní přehled AI novinek z {sources}."
SOURCE_INTRO = {"rd": "Redditu", "hn": "Hacker News"}


def load_published():
    try:
        return json.loads(LOG.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return []


def latest_days():
    """Poslední publikovaný den pro každý zdroj (rd, hn)."""
    latest = {}
    for rec in load_published():
        if rec.get("service") == "docs-md":
            latest[rec.get("day", "").split("/", 1)[0]] = rec.get("day")
    return [latest[s] for s in ("rd", "hn") if s in latest]


def url_for(day):
    if day.startswith("dny/"):
        date = day.split("/", 1)[1]
        # odkaz dávej jen když je den opravdu vygenerovaný do docs/
        if (PROJECT / "dny" / date / "prehled.md").is_file():
            return build_site.site_url(date)
        return None
    for rec in reversed(load_published()):
        if rec.get("service") == "docs-md" and rec.get("day") == day:
            return rec.get("url")
    return None


def pretty_date(day):
    _, date = day.split("/", 1)
    year, month, daynum = date.split("-")
    return f"{int(daynum)}. {int(month)}. {year}"


def scored_articles(day):
    """Články z tabulky v indexu jako (skóre, titulek), seřazené od nejvyššího."""
    text = (PROJECT / day / "00-index.md").read_text(encoding="utf-8")
    header, rows, in_table = None, [], False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_table = stripped.lower().startswith("## články")
            header = None
            continue
        if not in_table or not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        # Sloupec s titulkem: Reddit píše „Titulek“, HN někdy „Článek“ — ber obojí.
        title_i = next(
            (
                i
                for i, c in enumerate(header)
                if "titulek" in c.lower() or "článek" in c.lower() or "clanek" in c.lower()
            ),
            None,
        )
        score_i = next(
            (i for i, c in enumerate(header) if "skóre" in c.lower() or "body" in c.lower()),
            None,
        )
        if title_i is None or score_i is None or max(title_i, score_i) >= len(cells):
            continue
        title = cell_title(cells[title_i])
        score = re.search(r"\d+", cells[score_i])
        if title and score:
            rows.append((int(score.group()), title))
    rows.sort(key=lambda r: -r[0])
    return rows


def highlights(days):
    """Nejlepší témata podle skóre, střídavě mezi zdroji (max MAX_HIGHLIGHTS)."""
    per_day = []
    for day in days:
        abbr = SOURCE_ABBR.get(day.split("/", 1)[0], day.split("/", 1)[0].upper())
        per_day.append([(abbr, title) for _, title in scored_articles(day)])
    out, i = [], 0
    while len(out) < MAX_HIGHLIGHTS and any(i < len(t) for t in per_day):
        for t in per_day:
            if i < len(t) and len(out) < MAX_HIGHLIGHTS:
                out.append(t[i])
        i += 1
    return out


def intro(days):
    """Úvodní věta podle zdrojů, které příspěvek obsahuje."""
    sources = [s for s in ("rd", "hn") if any(d.startswith(s + "/") for d in days)]
    joined = " a ".join(SOURCE_INTRO.get(s, s) for s in sources) or "Redditu a Hacker News"
    return INTRO.format(sources=joined)


def build(days):
    lines = [f"{intro(days)} Co se řešilo:"]
    lines += [f"• {abbr}: {title}" for abbr, title in highlights(days)]
    lines += ["", "Celé přehledy:"]
    for day in days:
        source = SOURCE_NAMES.get(day.split("/", 1)[0], day)
        count = len(scored_articles(day))
        url = url_for(day) or "(nepublikováno)"
        lines.append(f"{source}, {pretty_date(day)} – {count} článků: {url}")
    return "\n".join(lines)


def den_data(date):
    """Sloučená témata dne z `dny/<date>/temata.json` (pokud existují)."""
    path = PROJECT / "dny" / date / "temata.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return None


def build_den(date):
    """Jeden příspěvek na den: témata ze sloučeného přehledu a jeden odkaz."""
    days = [
        d
        for d in (f"rd/{date}", f"hn/{date}")
        if (PROJECT / d / "00-index.md").is_file()
    ]
    if not days:
        raise SystemExit(f"pro {date} chybí rd/ i hn/")
    data = den_data(date)
    lines = [f"{intro(days)} Co se řešilo:"]
    if data and data.get("temata"):
        for topic in data["temata"][:MAX_HIGHLIGHTS]:
            abbr = "+".join(SOURCE_ABBR.get(s, s.upper()) for s in topic["sources"])
            lines.append(f"• {abbr}: {topic['title']}")
        themes = len(data["temata"])
        articles = data.get("clanky") or sum(len(scored_articles(d)) for d in days)
    else:
        lines += [f"• {abbr}: {title}" for abbr, title in highlights(days)]
        articles = sum(len(scored_articles(d)) for d in days)
        themes = articles
    url = url_for(f"dny/{date}") or "(nepublikováno)"
    lines += [
        "",
        "Celý denní přehled:",
        f"Reddit + Hacker News, {pretty_date('dny/' + date)} – {themes} témat z {articles} článků: {url}",
    ]
    return "\n".join(lines)


def main(argv):
    if argv and argv[0] == "--den":
        if len(argv) != 2:
            raise SystemExit("použití: build-linkedin.py --den YYYY-MM-DD")
        text = build_den(argv[1])
    else:
        published = load_published()
        if not argv and published and str(published[-1].get("day", "")).startswith("dny/"):
            date = published[-1]["day"].split("/", 1)[1]
            text = build_den(date)
        else:
            days = argv or latest_days()
            if not days:
                raise SystemExit("žádné publikované dny (logs/publish.json) — zadej složky ručně")
            text = build(days)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
