#!/usr/bin/env python3
"""Vygeneruje statický web (GitHub Pages) ze sloučených denních přehledů.

Vstup je `dny/<datum>/prehled.md` (z `build-denni.py`), výstup je `docs/`:
`<datum>.html` pro každý den, `index.html` s archivem, `feed.xml`, `sitemap.xml`,
`robots.txt`, `style.css`, `.nojekyll`, `CNAME` a `sw.js`. Web se servíruje
z větve `main`, složky `/docs`.

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

_spec_denni = importlib.util.spec_from_file_location(
    "build_denni", Path(__file__).resolve().parent / "build-denni.py"
)
build_denni = importlib.util.module_from_spec(_spec_denni)
_spec_denni.loader.exec_module(build_denni)

PROJECT = Path(__file__).resolve().parent.parent
DNY = PROJECT / "dny"
OUT = PROJECT / "docs"

# Adresa webu (bez koncového lomítka). Web jedou GitHub Pages z tohohle repa
# (main /docs) pod vlastní doménou; `docs/CNAME` se generuje z SITE_DOMAIN.
SITE_BASE = "https://ai-novinky.localinference.cz"
SITE_DOMAIN = "ai-novinky.localinference.cz"

# Náhled pro sdílení odkazu (og:image). Kreslí ho Pillow ve stejném vzhledu
# jako web: `og.png` pro archiv a `og/<datum>.png` pro jednotlivé dny.
# Bez Pillow se obrázky jen vynechají a meta značky se nevygenerují.
OG_SIZE = (1200, 630)
OG_FONTS = {
    "bold": ("Inter-Bold.ttf", "DejaVuSans-Bold.ttf"),
    "regular": ("Inter-Regular.ttf", "DejaVuSans.ttf"),
}
OG_FONT_DIRS = (
    "/usr/share/fonts/truetype/inter-zorin-os",
    "/usr/share/fonts/truetype/inter",
    "/usr/share/fonts/truetype/dejavu",
)
OG_BG = "#ffffff"
OG_FG = "#23262f"
OG_MUTED = "#555962"
OG_LINE = "#edeef3"
OG_ACCENT = "#187a63"

# Service worker: GitHub Pages nejde nastavit hlavičky (posílá max-age=600
# na všechno), takže web po nasazení může 10 minut ukazovat starou verzi.
# SW proto jede network-first: vždy si vyžádá čerstvou stránku (cache: no-store,
# tedy i mimo HTTP cache) a do Cache API ukládá jen kopii pro offline režim.
# Cache se pojmenovává podle buildu, takže nové nasazení starou cache zahodí.
SW_JS = """// Generuje scripts/build-site.py — needituj ručně.
// Web se vždy načítá ze sítě, aby se změny projevily hned; cache slouží
// jen jako záložka, když síť není.
const CACHE = "__CACHE__";

self.addEventListener("install", () => self.skipWaiting());

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)))
      )
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return; // Umami, cizí odkazy

  event.respondWith(
    fetch(request, { cache: "no-store" })
      .then((response) => {
        if (response.ok) {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
        }
        return response;
      })
      .catch(() =>
        caches.match(request).then((hit) => hit || caches.match("index.html"))
      )
  );
});
"""
SITE_NAME = "Denní AI přehled"
SITE_BRAND = "AI novinky"  # jméno v hlavičce (odkaz na úvod)
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


def render_markdown(md, extras=None):
    """Převede `prehled.md` na HTML. Vrací (titulek, html, popis).

    Obsah (`## Obsah`) se schová do rozbalovacího `<details>`, aby nepřekážel.
    `extras` je seznam HTML bloků v pořadí témat (rozbalovací plný text);
    každý se přidá na konec své sekce.
    """
    lines = md.splitlines()
    title = ""
    description = ""

    # kotvy z obsahu: `- [titulek](#kotva)` v sekci `## Obsah`
    stripped_lines = [line.strip() for line in lines]
    anchors = [
        m.group(1)
        for m in (ANCHOR_BULLET_RE.match(line) for line in stripped_lines)
        if m
    ]
    extras = list(extras or [])

    out = []
    anchor_i = 0
    topic_i = -1
    extra_done = 0
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

    def close_obsah():
        nonlocal in_obsah
        if in_obsah:
            out.append("</details>")
            in_obsah = False

    def append_extra():
        nonlocal extra_done
        if topic_i >= 0 and extra_done <= topic_i < len(extras):
            if extras[topic_i]:
                out.append(extras[topic_i])
            extra_done = topic_i + 1

    for raw in lines:
        stripped = raw.strip()

        if not stripped:
            flush_para()
            close_list()
            continue

        if stripped == "---":
            flush_para()
            close_list()
            append_extra()
            close_obsah()
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
            append_extra()
            heading = m.group(1)
            if strip_inline(heading).lower() == "obsah":
                n = len(anchors)
                out.append(
                    '<details class="obsah" id="obsah">'
                    "<summary>Obsah"
                    f'<span class="n">{n} {plural_cs(n, "téma", "témata", "témat")}</span>'
                    "</summary>"
                )
                in_obsah = True
                continue
            close_obsah()
            if anchor_i < len(anchors):
                anchor = anchors[anchor_i]
                anchor_i += 1
            else:
                anchor = build_prehled.slugify(strip_inline(heading)) or "tema"
            out.append(
                f'<h2 id="{html.escape(anchor, quote=True)}">{inline(heading)}</h2>'
            )
            topic_i += 1
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
    append_extra()
    close_obsah()
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
<link rel="stylesheet" href="{css}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="favicon-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#187a63">
<link rel="alternate" type="application/rss+xml" title="{site}" href="{feed}">
<link rel="sitemap" type="application/xml" title="Sitemap" href="sitemap.xml">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="{image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{image}">
<script defer src="https://navstevnost.pikapod.net/script.js" data-website-id="c7f4fc4d-e002-4d3f-aad1-9f2020cf83ea"></script>
</head>
<body>
<header class="site">{back}<a class="brand" href="{home}">{brand}</a><span class="sep">·</span><a href="{feed}">RSS</a><a class="parent" href="https://www.localinference.cz">LOCALinference.cz ↗</a></header>
<main>
{body}
</main>
<footer class="site">{footer}</footer>
{sw_register}
</body>
</html>
"""


SW_REGISTER = (
    '<script>if ("serviceWorker" in navigator) { window.addEventListener("load", '
    'function () { navigator.serviceWorker.register("sw.js", '
    '{ updateViaCache: "none" }); }); }</script>'
)


def page(title, description, url, body, css, home, feed, footer, image=None, image_alt=None, back=""):
    image = f"{SITE_BASE}/{image}" if image else f"{SITE_BASE}/og.png"
    return PAGE.format(
        title=html.escape(title, quote=True),
        description=html.escape(description, quote=True),
        url=html.escape(url, quote=True),
        site=html.escape(SITE_NAME),
        brand=html.escape(SITE_BRAND),
        css=css,
        home=home,
        feed=feed,
        body=body,
        footer=footer,
        image=html.escape(image, quote=True),
        image_alt=html.escape(image_alt or f"{SITE_NAME} – náhled", quote=True),
        back=back,
        sw_register=SW_REGISTER,
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


CSS = """/* Geist (SIL OFL 1.1, viz assets/fonts/OFL.txt) — stejné písmo jako docs-md,
   čte se líp než systémové; latin + latin-ext kvůli české diakritice. */
@font-face {
  font-family: "Geist";
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url("fonts/geist-latin-ext.woff2") format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C4, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
@font-face {
  font-family: "Geist";
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url("fonts/geist-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
:root {
  /* barvy z www.localinference.cz (Starlight: zelený akcent, neutrální šedé) */
  --bg: #ffffff;
  --fg: #23262f;
  --muted: #555962;
  --line: #edeef3;
  --accent: #187a63;
  --card: #f6f7f9;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #17181c;
    --fg: #edeef3;
    --muted: #888c96;
    --line: #353841;
    --accent: #35b48f;
    --card: #23262f;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font: 1.05rem/1.7 Geist, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
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
header.site { display: flex; flex-wrap: wrap; gap: .5rem; align-items: baseline; padding-top: 1.5rem; }
header.site a { color: var(--muted); text-decoration: none; }
header.site a:hover { color: var(--accent); text-decoration: underline; }
header.site .brand { color: var(--accent); font-weight: 650; }
header.site .parent { margin-left: auto; }
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
/* obsah je sbalený do <details>, rozbalí si ho jen kdo potřebuje */
details.obsah {
  margin: 1.5rem 0 1.75rem;
  padding: .15rem 1rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--card);
}
details.obsah > summary {
  display: flex;
  align-items: baseline;
  gap: .55rem;
  padding: .75rem .1rem;
  font-weight: 600;
  color: var(--accent);
  cursor: pointer;
  list-style: none;
}
details.obsah > summary::-webkit-details-marker { display: none; }
details.obsah > summary::marker { content: ""; }
details.obsah > summary::before { content: "+"; font-weight: 700; }
details.obsah[open] > summary { border-bottom: 1px solid var(--line); }
details.obsah[open] > summary::before { content: "−"; }
details.obsah > summary .n { font-size: .85rem; font-weight: 400; color: var(--muted); }
details.obsah ul { margin: .6rem 0 .9rem; padding-left: 1.1rem; }
details.obsah li { font-size: .97rem; margin: .3rem 0; }
details.obsah a { color: var(--accent); text-decoration: none; }
details.obsah a:hover { text-decoration: underline; }

/* plný článek pod anotací — rozbalovací „+ Číst dál" (bez oddělovací linky,
   anotace a odkaz na plný text patří k sobě) */
details.full { margin: .5rem 0 0; }
details.full > summary {
  display: flex;
  align-items: baseline;
  gap: .5rem;
  font-size: .93rem;
  font-weight: 600;
  color: var(--accent);
  cursor: pointer;
  list-style: none;
}
details.full > summary::-webkit-details-marker { display: none; }
details.full > summary::marker { content: ""; }
details.full > summary::before { content: "+"; font-weight: 700; min-width: .8rem; }
details.full[open] > summary::before { content: "−"; }
details.full .full-body { margin: .4rem 0 0; font-size: 1rem; }
details.full .full-body p { margin: .85rem 0; }
h2 { scroll-margin-top: 1.5rem; }
footer.site { border-top: 1px solid var(--line); margin-top: 1rem; }
/* archiv: dny po měsících, v kartě je hlavní datum, počet novinek druhotný */
.months { margin: 2rem 0 0; }
.month h2 {
  display: flex;
  align-items: baseline;
  gap: .6rem;
  margin: 2.25rem 0 .7rem;
  font-size: .82rem;
  font-weight: 650;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}
.month h2 .mcount {
  font-size: .74rem;
  font-weight: 400;
  letter-spacing: 0;
  text-transform: none;
  color: var(--muted);
  opacity: .75;
}
.days {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(7.25rem, 1fr));
  gap: .5rem;
}
.day {
  display: flex;
  flex-direction: column;
  gap: .15rem;
  padding: .65rem .8rem .7rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--card);
  color: var(--fg);
  text-decoration: none;
}
.day:hover { border-color: var(--accent); }
.day .dnum {
  font-size: 1.25rem;
  font-weight: 650;
  line-height: 1.15;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
  white-space: nowrap;
  color: var(--accent);
}
.day .dmeta { font-size: .78rem; line-height: 1.3; color: var(--muted); }
.lead { color: var(--muted); }
"""


def _og_font(weight, size):
    from PIL import ImageFont

    for directory in OG_FONT_DIRS:
        for name in OG_FONTS[weight]:
            path = Path(directory) / name
            if path.is_file():
                return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size)


def _og_wrap(draw, text, font, max_width, max_lines):
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if not current or draw.textlength(candidate, font=font) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while draw.textlength(f"{last}…", font=font) > max_width and " " in last:
            last = last.rsplit(" ", 1)[0]
        lines[-1] = f"{last}…"
    return lines


def _og_one_line(draw, text, font, max_width):
    text = " ".join(text.split())
    if draw.textlength(text, font=font) <= max_width:
        return text
    while text and draw.textlength(f"{text}…", font=font) > max_width:
        text = text[:-1].rstrip()
    return f"{text}…"


def og_card(path, kicker, title, subtitle, note, items=()):
    """Nakreslí 1200×630 náhled pro sdílení. False, když chybí Pillow."""
    try:
        from PIL import Image, ImageDraw, ImageFilter
    except ImportError:
        return False

    width, height = OG_SIZE
    img = Image.new("RGB", (width, height), OG_BG)
    # jemný akcentní přeliv v pravém horním rohu (overlay + rozostření, ať nemá
    # tvrdou hranu)
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(overlay).ellipse(
        (width - 330, -280, width + 280, 330), fill=(24, 122, 99, 40)
    )
    overlay = overlay.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    margin = 80
    f_kicker = _og_font("bold", 30)
    f_title = _og_font("bold", 62)
    f_sub = _og_font("regular", 34)
    f_note = _og_font("regular", 26)

    draw.ellipse((margin, 84, margin + 14, 98), fill=OG_ACCENT)
    draw.text((margin + 28, 74), kicker, font=f_kicker, fill=OG_ACCENT)

    y = 176
    for line in _og_wrap(draw, title, f_title, width - 2 * margin, 2):
        draw.text((margin, y), line, font=f_title, fill=OG_FG)
        y += 76
    y += 20
    for line in _og_wrap(draw, subtitle, f_sub, width - 2 * margin, 2):
        draw.text((margin, y), line, font=f_sub, fill=OG_MUTED)
        y += 46

    if items:
        f_item = _og_font("regular", 31)
        y += 34
        for item in items[:3]:
            draw.ellipse((margin + 2, y + 15, margin + 10, y + 23), fill=OG_ACCENT)
            draw.text(
                (margin + 26, y),
                _og_one_line(draw, item, f_item, width - 2 * margin - 26),
                font=f_item,
                fill=OG_FG,
            )
            y += 47

    draw.line((margin, height - 118, width - margin, height - 118), fill=OG_LINE, width=2)
    draw.text((margin, height - 88), SITE_DOMAIN, font=f_note, fill=OG_MUTED)
    draw.text(
        (width - margin - draw.textlength(note, font=f_note), height - 88),
        note,
        font=f_note,
        fill=OG_MUTED,
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    return True


def topic_annotations(md):
    """Text anotace pro každé téma v pořadí sekcí (bez meta odrážek)."""
    sections = []
    current = None
    for raw in md.splitlines():
        s = raw.strip()
        if s.startswith("## "):
            if strip_inline(s[3:]).lower() == "obsah":
                current = None
                continue
            current = []
            sections.append(current)
            continue
        if current is None or not s or s == "---":
            continue
        if BULLET_RE.match(s) or s.startswith("#"):
            continue
        current.append(s)
    return [" ".join(" ".join(parts).split()) for parts in sections]


def topic_full_texts(date, temata, annotations=()):
    """Rozbalovací plný text našeho článku pro každé téma (v pořadí témat).

    Bere se z `rd/<datum>/<id>_*.md` a `hn/<datum>/<id>_*.md`; když téma sloučilo
    oba zdroje, má vlastní `<details>` každý z nich. Odstavce, které už jsou
    v anotaci, se na začátku přeskočí, aby se text neopakoval.
    """
    blocks = []
    for index, tema in enumerate(temata):
        annotation = annotations[index] if index < len(annotations) else ""
        ids = tema.get("ids") or {}
        parts = []
        for src, cid in ids.items():
            folder = PROJECT / src / date
            paths = sorted(folder.glob(f"{cid}_*.md")) if folder.is_dir() else []
            if not paths:
                continue
            rec = build_denni.parse_article(paths[0], src, date)
            paras = [
                re.sub(r"^#{1,6}\s*", "", p).strip()
                for p in (rec.get("paragraphs") or [])
                if p.strip()
            ]
            if not paras:
                continue
            shown = [
                p
                for p in paras
                if not (annotation and " ".join(p.split())[:120] in annotation)
            ] or paras
            label = {"rd": "Reddit", "hn": "Hacker News"}.get(src, src.upper())
            summary = "Číst dál" if len(ids) == 1 else f"Číst dál – {label}"
            body = "".join(f"<p>{inline(p)}</p>" for p in shown)
            parts.append(
                f'<details class="full"><summary>{summary}</summary>'
                f'<div class="full-body">{body}</div></details>'
            )
        blocks.append("".join(parts))
    return blocks


def write_icons():
    """Favicon ve stejné zelené jako web: SVG + PNG + .ico (bez fontu, „A" je
    kreslené tahy, aby vypadalo stejně ve všech velikostech)."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#187a63"/>'
        '<g stroke="#fff" stroke-linecap="round" stroke-linejoin="round" fill="none">'
        '<path d="M32 18 18 47" stroke-width="7"/>'
        '<path d="M32 18 46 47" stroke-width="7"/>'
        '<path d="M24 37h16" stroke-width="6"/>'
        "</g></svg>"
    )
    (OUT / "favicon.svg").write_text(svg, encoding="utf-8")

    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return

    def icon(size, rounded=True):
        scale = 4  # kreslit větší a zmenšit = hladké hrany
        px = size * scale
        unit = px / 64
        img = Image.new("RGBA", (px, px), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        if rounded:
            draw.rounded_rectangle(
                (0, 0, px - 1, px - 1), radius=int(14 * unit), fill=OG_ACCENT
            )
        else:  # apple-touch-icon si masku dělá sám, takže celá plocha
            draw.rectangle((0, 0, px, px), fill=OG_ACCENT)

        # v 16 px je tah 7 jednotek moc tlustý, „A" se slije
        thin = 1.0 if size >= 32 else 0.72

        def stroke(a, b, width):
            width_px = max(1, int(width * thin * unit))
            draw.line((a[0] * unit, a[1] * unit, b[0] * unit, b[1] * unit),
                      fill="#ffffff", width=width_px)
            r = width_px / 2
            for point in (a, b):
                x, y = point[0] * unit, point[1] * unit
                draw.ellipse((x - r, y - r, x + r, y + r), fill="#ffffff")

        stroke((32, 18), (18, 47), 7)
        stroke((32, 18), (46, 47), 7)
        stroke((24, 37), (40, 37), 6)
        return img.resize((size, size), Image.LANCZOS)

    for size, name in (
        (192, "icon-192.png"),
        (32, "favicon-32.png"),
        (16, "favicon-16.png"),
    ):
        icon(size).save(OUT / name)
    icon(180, rounded=False).save(OUT / "apple-touch-icon.png")
    icon(64).save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    manifest = {
        "name": SITE_BRAND,
        "short_name": SITE_BRAND,
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": OG_ACCENT,
        "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}],
    }
    (OUT / "site.webmanifest").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def write_day(date):
    md = (DNY / date / "prehled.md").read_text(encoding="utf-8")
    temata = (load_temata(date) or {}).get("temata") or []
    title, body, description = render_markdown(
        md, topic_full_texts(date, temata, topic_annotations(md))
    )
    meta = day_meta(date)
    full_title = title or f"{SITE_NAME} – {meta['pretty']}"
    og = f"og/{date}.png"
    if not og_card(
        OUT / og,
        "Reddit + Hacker News",
        full_title,
        f"{meta['themes']} témat · anotace s odkazy na diskusi",
        SITE_NAME,
        items=[t.get("title", "") for t in temata[:3]],
    ):
        og = None
    doc = page(
        title=full_title,
        description=description or SITE_DESC,
        url=meta["url"],
        body=body,
        css=CSS_URL,
        home="index.html",
        feed="feed.xml",
        footer=f'<a href="index.html">Archiv</a> · {html.escape(SITE_NAME)}',
        image=og,
        image_alt=full_title,
        back='<a href="index.html">← Archiv</a><span class="sep">·</span>',
    )
    (OUT / f"{date}.html").write_text(doc, encoding="utf-8")
    return meta, full_title, description


MONTHS_CS = (
    "Leden", "Únor", "Březen", "Duben", "Květen", "Červen",
    "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec",
)
WEEKDAYS_CS = ("po", "út", "st", "čt", "pá", "so", "ne")


def plural_cs(n, one, few, many):
    """1 novinka / 2 novinky / 5 novinek."""
    if n == 1:
        return one
    if 2 <= n % 100 <= 4:
        return few
    return many


def write_index(entries):
    # Dny se seskupí po měsících; v kartě je důležité datum, počet novinek
    # je pod ním druhotný.
    months = {}
    for meta in entries:
        d = datetime.strptime(meta["date"], "%Y-%m-%d")
        months.setdefault((d.year, d.month), []).append((d, meta))

    sections = []
    for year, month in sorted(months, reverse=True):
        days = months[(year, month)]
        cards = []
        for d, meta in days:
            n = meta["themes"]
            cards.append(
                f'<a class="day" href="{meta["date"]}.html">'
                f'<span class="dnum">{d.day}. {d.month}.</span>'
                f'<span class="dmeta">{WEEKDAYS_CS[d.weekday()]} · '
                f'{n} {plural_cs(n, "novinka", "novinky", "novinek")}</span>'
                "</a>"
            )
        sections.append(
            '<section class="month">'
            f"<h2>{MONTHS_CS[month - 1]} {year}"
            f'<span class="mcount">{len(days)} {plural_cs(len(days), "den", "dny", "dní")}</span>'
            "</h2>"
            f'<div class="days">{"".join(cards)}</div>'
            "</section>"
        )

    og = "og.png"
    if not og_card(
        OUT / og,
        "Reddit + Hacker News",
        SITE_NAME,
        SITE_DESC,
        f"Archiv {len(entries)} dní",
        items=[
            f"{meta['pretty']} · {meta['themes']} "
            f"{plural_cs(meta['themes'], 'novinka', 'novinky', 'novinek')}"
            for meta in entries[:3]
        ],
    ):
        og = None
    body = (
        "<h1>Denní AI přehled</h1>"
        f'<p class="lead">{html.escape(SITE_DESC)}</p>'
        f'<div class="months">{"".join(sections)}</div>'
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
        image=og,
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


def _w3c(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")


def write_sitemap(entries):
    """Sitemap z archivu: úvod + každý den. Drží se sám v souladu s `dny/`."""
    newest = entries[0]["date"] if entries else datetime.now().strftime("%Y-%m-%d")
    index_dt = datetime.strptime(newest, "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc)
    urls = [
        "  <url>\n"
        f"    <loc>{html.escape(SITE_BASE)}/</loc>\n"
        f"    <lastmod>{_w3c(index_dt)}</lastmod>\n"
        "    <changefreq>daily</changefreq>\n"
        "    <priority>1.0</priority>\n"
        "  </url>"
    ]
    for meta in entries:
        dt = datetime.strptime(meta["date"], "%Y-%m-%d").replace(hour=8, tzinfo=timezone.utc)
        urls.append(
            "  <url>\n"
            f"    <loc>{html.escape(meta['url'])}</loc>\n"
            f"    <lastmod>{_w3c(dt)}</lastmod>\n"
            "    <priority>0.8</priority>\n"
            "  </url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def write_robots():
    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE_BASE}/sitemap.xml\n"
    )
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")


def main(argv):
    global CSS_URL
    CSS_URL = f"style.css?v={hashlib.md5(CSS.encode('utf-8')).hexdigest()[:8]}"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    fonts = PROJECT / "assets" / "fonts"
    if fonts.is_dir():
        (OUT / "fonts").mkdir(parents=True, exist_ok=True)
        for font in sorted(fonts.glob("*.woff2")):
            (OUT / "fonts" / font.name).write_bytes(font.read_bytes())
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    cache_name = f"ai-novinky-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    (OUT / "sw.js").write_text(SW_JS.replace("__CACHE__", cache_name), encoding="utf-8")
    (OUT / "CNAME").write_text(SITE_DOMAIN + "\n", encoding="utf-8")
    write_icons()

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
    write_sitemap(entries)
    write_robots()
    print(
        f"hotovo -> {OUT.relative_to(PROJECT)}  "
        f"({len(entries)} dní, index + feed + sitemap + robots)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
