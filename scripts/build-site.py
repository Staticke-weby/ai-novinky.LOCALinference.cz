#!/usr/bin/env python3
"""Vygeneruje statický web (GitHub Pages) ze sloučených denních přehledů.

Vstup je `dny/<datum>/prehled.md` (z `build-denni.py`), výstup je `docs/`:
`<datum>.html` pro každý den, `index.html` s archivem, `feed.xml`, `style.css`,
`.nojekyll` a `CNAME`. Web se servíruje z větve `main`, složky `/docs`.

Markdown se neRenderuje obecně — zpracovává se jen to, co `build-denni.py`
skutečně produkuje (H1/H2, odrážky, `**tučně**`, odkazy, `---`). Záměrně
**nepodporuje** `__tučně__`, protože v textech jsou redditová jména typu
`u/__ThrowAway__123`, která by se rozbila.

Kotvy nadpisů se berou z odkazů v sekci `## Obsah`, takže klikací obsah sedí
i tam, kde by se `slugify()` rozešel s původním generátorem.

Použití:
    python3 scripts/build-site.py              # všechny dny z dny/
    python3 scripts/build-site.py 2026-11-14   # jen jeden den
"""

import hashlib
import html
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "build_prehled", Path(__file__).resolve().parent / "build-prehled.py"
)
build_prehled = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_prehled)

PROJECT = Path(__file__).resolve().parent.parent
DNY = PROJECT / "dny"
OUT = PROJECT / "docs"

# Adresa webu (bez koncového lomítka). Web jedou GitHub Pages z tohohle repa
# (main /docs) pod vlastní doménou; `docs/CNAME` se generuje z SITE_DOMAIN.
SITE_BASE = "https://ai-novinky.localinference.cz"
SITE_DOMAIN = "ai-novinky.localinference.cz"
SITE_NAME = "Denní AI přehled"
SITE_DESC = "Denní souhrny AI novinek z Redditu a Hacker News v češtině."

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CSS_URL = "style.css"  # doplní main() podle obsahu CSS
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.*)$")
H2_RE = re.compile(r"^##\s+(.*)$")
BULLET_RE = re.compile(r"^[-*]\s+(.*)$")
ANCHOR_BULLET_RE = re.compile(r"^[-*]\s+\[[^\]]+\]\(#([^)]+)\)\s*$")


def site_url(date):
    """Trvalý odkaz na denní přehled (pro LinkedIn a feed)."""
    return f"{SITE_BASE}/{date}.html"


def inline(text):
    """Escapuje a převede odkazy a **tučné** na HTML."""
    text = html.escape(text, quote=False)
    text = LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', text)
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    return text


def strip_inline(text):
    """Čistý text z řádku s markdownem (pro popis a og:description)."""
    text = LINK_RE.sub(lambda m: m.group(1), text)
    text = BOLD_RE.sub(r"\1", text)
    return text.strip()


def render_markdown(md):
    """Převede `prehled.md` na HTML. Vrací (titulek, html, popis)."""
    lines = md.splitlines()
    title = ""
    description = ""

    # kotvy z obsahu: `- [titulek](#kotva)` v sekci `## Obsah`
    anchors = [
        m.group(1)
        for m in (ANCHOR_BULLET_RE.match(line.strip()) for line in lines)
        if m
    ]

    out = []
    anchor_i = 0
    in_obsah = False
    in_list = False
    para = []

    def flush_para():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for raw in lines:
        stripped = raw.strip()

        if not stripped:
            flush_para()
            close_list()
            continue

        if stripped == "---":
            flush_para()
            close_list()
            out.append("<hr>")
            continue

        m = H1_RE.match(stripped)
        if m:
            flush_para()
            close_list()
            title = strip_inline(m.group(1))
            out.append(f"<h1>{inline(m.group(1))}</h1>")
            continue

        m = H2_RE.match(stripped)
        if m:
            flush_para()
            close_list()
            heading = m.group(1)
            in_obsah = strip_inline(heading).lower() == "obsah"
            if in_obsah:
                out.append(f'<h2 id="obsah">{inline(heading)}</h2>')
                continue
            if anchor_i < len(anchors):
                anchor = anchors[anchor_i]
                anchor_i += 1
            else:
                anchor = build_prehled.slugify(strip_inline(heading)) or "tema"
            out.append(
                f'<h2 id="{html.escape(anchor, quote=True)}">{inline(heading)}</h2>'
            )
            continue

        m = BULLET_RE.match(stripped)
        if m:
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            continue

        if not description:
            description = strip_inline(stripped)
        para.append(stripped)

    flush_para()
    close_list()
    return title, "\n".join(out), description


PAGE = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{site}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{css}">
<link rel="alternate" type="application/rss+xml" title="{site}" href="{feed}">
</head>
<body>
<header class="site"><a href="{home}">{site}</a><span class="sep">·</span><a href="{feed}">RSS</a></header>
<main>
{body}
</main>
<footer class="site">{footer}</footer>
</body>
</html>
"""


def page(title, description, url, body, css, home, feed, footer):
    return PAGE.format(
        title=html.escape(title, quote=True),
        description=html.escape(description, quote=True),
        url=html.escape(url, quote=True),
        site=html.escape(SITE_NAME),
        css=css,
        home=home,
        feed=feed,
        body=body,
        footer=footer,
    )


def pretty_date(date):
    d = datetime.strptime(date, "%Y-%m-%d")
    return f"{d.day}. {d.month}. {d.year}"


def load_temata(date):
    path = DNY / date / "temata.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return None


def day_meta(date):
    """Souhrnné údaje dne pro archiv a feed."""
    data = load_temata(date) or {}
    temata = data.get("temata") or []
    sources = sorted({s for t in temata for s in t.get("sources", [])})
    return {
        "date": date,
        "pretty": pretty_date(date),
        "url": site_url(date),
        "themes": len(temata),
        "articles": data.get("clanky") or len(temata),
        "sources": sources,
    }


def days():
    return sorted(
        (p.parent.name for p in DNY.glob("*/prehled.md") if DATE_RE.match(p.parent.name)),
        reverse=True,
    )


CSS = """:root {
  --bg: #fdfdfc;
  --fg: #1c1b19;
  --muted: #6b6760;
  --line: #e3e0d9;
  --accent: #b4451f;
  --card: #f6f4ef;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #16151a;
    --fg: #e8e6e1;
    --muted: #9b968c;
    --line: #2e2c33;
    --accent: #ff9166;
    --card: #1e1d23;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font: 1.05rem/1.7 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
        "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-feature-settings: "kern";
  text-rendering: optimizeLegibility;
}
header.site, footer.site {
  max-width: 46rem;
  margin: 0 auto;
  padding: 1rem 1.25rem;
  font-size: .9rem;
  color: var(--muted);
}
header.site { display: flex; gap: .5rem; align-items: baseline; padding-top: 1.5rem; }
header.site a { color: var(--muted); text-decoration: none; }
header.site a:hover { color: var(--accent); }
header.site .sep { color: var(--line); }
main { max-width: 46rem; margin: 0 auto; padding: 0 1.25rem 3rem; }
h1 { font-size: 1.85rem; line-height: 1.25; margin: 1.5rem 0 .75rem; letter-spacing: -.01em; }
h2 { font-size: 1.2rem; line-height: 1.35; margin: 2.25rem 0 .5rem; }
h2 + p { margin-top: .25rem; }
p { margin: .75rem 0; }
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }
a:hover { text-decoration-thickness: 2px; }
ul { margin: .75rem 0; padding-left: 1.2rem; }
li { margin: .35rem 0; }
hr { border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }
strong { font-weight: 650; }
h2#obsah + ul, h2#obsah + ul li { font-size: .97rem; }
/* odkazy v obsahu: ať je vidět, že to jsou odkazy (podtržení až při hoveru,
   aby 36 položek nepodtržením nezmizelo a zároveň nebylo přeplácané) */
h2#obsah + ul a { color: var(--accent); text-decoration: none; }
h2#obsah + ul a:hover { text-decoration: underline; }
h2 { scroll-margin-top: 1.5rem; }
footer.site { border-top: 1px solid var(--line); margin-top: 1rem; }
/* archiv */
.archive { list-style: none; padding: 0; margin: 1.5rem 0; }
.archive li {
  display: flex;
  flex-wrap: wrap;
  gap: .25rem .75rem;
  align-items: baseline;
  padding: .7rem .9rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--card);
  margin: .5rem 0;
}
.archive .date { font-variant-numeric: tabular-nums; color: var(--muted); font-size: .9rem; min-width: 7.5rem; }
.archive a { font-weight: 600; text-decoration: none; }
.archive .meta { color: var(--muted); font-size: .85rem; margin-left: auto; }
.lead { color: var(--muted); }
"""


def write_day(date):
    md = (DNY / date / "prehled.md").read_text(encoding="utf-8")
    title, body, description = render_markdown(md)
    meta = day_meta(date)
    full_title = title or f"{SITE_NAME} – {meta['pretty']}"
    doc = page(
        title=full_title,
        description=description or SITE_DESC,
        url=meta["url"],
        body=body,
        css=CSS_URL,
        home="index.html",
        feed="feed.xml",
        footer=f'<a href="index.html">Archiv</a> · {html.escape(SITE_NAME)}',
    )
    (OUT / f"{date}.html").write_text(doc, encoding="utf-8")
    return meta, full_title, description


def write_index(entries):
    items = []
    for meta in entries:
        src = " + ".join(
            {"rd": "Reddit", "hn": "HN"}.get(s, s.upper()) for s in meta["sources"]
        )
        items.append(
            f'<li><span class="date">{meta["pretty"]}</span>'
            f'<a href="{meta["date"]}.html">{meta["themes"]} témat z {meta["articles"]} článků</a>'
            f'<span class="meta">{src}</span></li>'
        )
    body = (
        "<h1>Denní AI přehled</h1>"
        f'<p class="lead">{html.escape(SITE_DESC)}</p>'
        f'<ul class="archive">{"".join(items)}</ul>'
    )
    doc = page(
        title=SITE_NAME,
        description=SITE_DESC,
        url=f"{SITE_BASE}/",
        body=body,
        css=CSS_URL,
        home="index.html",
        feed="feed.xml",
        footer=f'{len(entries)} dní · <a href="feed.xml">RSS</a>',
    )
    (OUT / "index.html").write_text(doc, encoding="utf-8")


def write_feed(entries, titles):
    items = []
    for meta in entries[:30]:
        date = meta["date"]
        dt = datetime.strptime(date, "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc)
        title = titles.get(date) or f"{SITE_NAME} – {meta['pretty']}"
        desc = f'{meta["themes"]} témat z {meta["articles"]} článků (Reddit + Hacker News).'
        items.append(
            "  <item>\n"
            f"    <title>{html.escape(title)}</title>\n"
            f"    <link>{meta['url']}</link>\n"
            f"    <guid>{meta['url']}</guid>\n"
            f"    <pubDate>{format_datetime(dt)}</pubDate>\n"
            f"    <description>{html.escape(desc)}</description>\n"
            "  </item>"
        )
    newest = entries[0]["date"] if entries else datetime.now().strftime("%Y-%m-%d")
    dt = datetime.strptime(newest, "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc)
    feed = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<rss version="2.0">\n<channel>\n'
        f"  <title>{html.escape(SITE_NAME)}</title>\n"
        f"  <link>{SITE_BASE}/</link>\n"
        f"  <description>{html.escape(SITE_DESC)}</description>\n"
        "  <language>cs</language>\n"
        f"  <lastBuildDate>{format_datetime(dt)}</lastBuildDate>\n"
        + "\n".join(items)
        + "\n</channel>\n</rss>\n"
    )
    (OUT / "feed.xml").write_text(feed, encoding="utf-8")


def main(argv):
    global CSS_URL
    CSS_URL = f"style.css?v={hashlib.md5(CSS.encode('utf-8')).hexdigest()[:8]}"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "CNAME").write_text(SITE_DOMAIN + "\n", encoding="utf-8")

    wanted = [a for a in argv if DATE_RE.match(a)]
    if argv and not wanted:
        raise SystemExit("použití: build-site.py [RRRR-MM-DD …]")

    entries, titles = [], {}
    for date in days():
        meta, title, _ = write_day(date)
        entries.append(meta)
        titles[date] = title
        print(f"{date}: {meta['themes']} témat -> docs/{date}.html")

    if wanted:
        # jen kontrola, že požadované dny existují
        missing = [d for d in wanted if d not in titles]
        if missing:
            raise SystemExit(f"chybí dny: {', '.join(missing)}")
    if not entries:
        raise SystemExit("v dny/ není žádný prehled.md")

    write_index(entries)
    write_feed(entries, titles)
    print(f"hotovo -> {OUT.relative_to(PROJECT)}  ({len(entries)} dní, index + feed)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
