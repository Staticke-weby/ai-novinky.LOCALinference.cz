#!/usr/bin/env python3
"""Posbírá Hacker News příspěvky za den a připraví podklady pro souhrn.

Výstup do `hn/<YYYY-MM-DD>/_data/`:
    dataset.json     – všechny story v okně (pro filtr AI/tech a přílohu)
    appendix.json    – story s >= 10 komentáři (kandidáti do přílohy)
    candidates.json  – kandidáti na články (nejvyšší skóre)
    bundles/<id>.md  – balíček pro pisatele (metadata, selftext, externí článek, komentáře)

Používá veřejné HN API (Algolia) – bez prohlížeče a bez blokování.
HN nezveřejňuje skóre komentářů, proto je v balíčcích místo skóre `-`
a pořadí komentářů odpovídá řazení HN.

Použití: python3 scripts/hn-collect.py 2026-10-04
"""

import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Prague")
API = "https://hn.algolia.com/api/v1"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"
PER_PAGE = 100
MAX_PAGES = 12            # 1200 story je na den s rezervou
MIN_POINTS = 20           # do balíčků jde od tohoto skóre
MIN_COMMENTS = 10         # a od tohoto počtu komentářů
MAX_CANDIDATES = 45       # kolik balíčků stavět
MAX_COMMENTS = 30         # kolik komentářů do balíčku
COMMENT_DEPTH = 1
COMMENT_CHARS = 1200
ARTICLE_CHARS = 20000
PAGES = re.compile(r"<[^>]+>")

# Termíny pro preferenci AI/tech příspěvků (jen zvýhodnění, ne tvrdý filtr).
AI_TERMS = [
    "ai", "artificial intelligence", "machine learning", "deep learning", "neural",
    "llm", "llms", "gpt", "chatgpt", "openai", "anthropic", "claude", "gemini",
    "deepmind", "deepseek", "llama", "mistral", "qwen", "kimi", "grok", "copilot",
    "hugging face", "transformer", "diffusion", "stable diffusion", "agent", "agents",
    "rag", "embedding", "embeddings", "inference", "fine-tune", "finetune", "training",
    "dataset", "benchmark", "robot", "robotics", "autonomous", "self-driving", "gpu",
    "cuda", "nvidia", "tpu", "chip", "chips", "semiconductor", "datacenter",
    "data center", "pytorch", "tensorflow", "langchain", "prompt", "hallucination",
    "alignment", "agi", "singularity", "ml",
]
AI_RE = re.compile(r"\b(" + "|".join(re.escape(t) for t in AI_TERMS) + r")\b", re.I)


def ai_score(story):
    """Počet AI/tech termínů v titulku a URL (jen pro řazení kandidátů)."""
    hay = f"{story.get('title', '')} {story.get('url', '')}"
    return len(set(m.group(0).lower() for m in AI_RE.finditer(hay)))


def get_json(url, params=None, timeout=30, retries=2):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            last = exc
            if attempt < retries:
                time.sleep(2)
    print(f"  ! request selhal: {url} ({last})", file=sys.stderr)
    return None


def html_to_text(raw):
    """Z HTML udělá čitelný text (odkazy jako 'text (url)', odstavce zachované)."""
    if not raw:
        return ""
    raw = re.sub(r"(?is)<(script|style|noscript|head|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<(br|/p|/div|/li|/h[1-6])\s*/?>", "\n", raw)
    raw = re.sub(
        r'(?is)<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        lambda m: f"{PAGES.sub('', m.group(2)).strip()} ({m.group(1)})",
        raw,
    )
    raw = PAGES.sub("", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    raw = re.sub(r"\n\s*\n\s*\n+", "\n\n", raw)
    return raw.strip()


def window(date):
    start = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=TZ)
    end = start + timedelta(days=1)
    return int(start.timestamp()), int(end.timestamp())


def fetch_stories(w0, w1):
    stories, seen = [], set()
    page = 0
    while page < MAX_PAGES:
        data = get_json(
            f"{API}/search_by_date",
            {
                "tags": "story",
                "numericFilters": f"created_at_i>{w0},created_at_i<{w1}",
                "hitsPerPage": PER_PAGE,
                "page": page,
            },
        )
        if not data:
            break
        hits = data.get("hits", []) or []
        for h in hits:
            oid = h.get("objectID")
            if not oid or oid in seen:
                continue
            seen.add(oid)
            hn_url = f"https://news.ycombinator.com/item?id={oid}"
            stories.append(
                {
                    "id": oid,
                    "title": (h.get("title") or "").strip(),
                    "url": h.get("url") or hn_url,
                    "permalink": hn_url,
                    "author": h.get("author") or "",
                    "points": h.get("points") or 0,
                    "num_comments": h.get("num_comments") or 0,
                    "created_at_i": h.get("created_at_i") or 0,
                    "story_text": html_to_text(h.get("story_text") or ""),
                }
            )
        if page + 1 >= (data.get("nbPages") or 1):
            break
        page += 1
        time.sleep(0.3)
    return stories


def walk_comments(children, depth, out):
    for c in children or []:
        if len(out) >= MAX_COMMENTS:
            return
        text = html_to_text(c.get("text") or "")
        if text:
            out.append({"author": c.get("author") or "?", "depth": depth, "text": text[:COMMENT_CHARS]})
        if depth < COMMENT_DEPTH:
            walk_comments(c.get("children"), depth + 1, out)


def fetch_comments(story_id):
    data = get_json(f"{API}/items/{story_id}")
    if not data:
        return []
    out = []
    walk_comments(data.get("children"), 0, out)
    return out


def extract_main_html(raw):
    """Vytáhne hlavní obsah stránky, ať text netáhne navigaci a patičku."""
    for tag in ("article", "main"):
        match = re.search(rf"(?is)<{tag}\b[^>]*>(.*?)</{tag}>", raw)
        if match and len(match.group(1)) > 500:
            raw = match.group(1)
            break
    else:
        match = re.search(r"(?is)<body\b[^>]*>(.*?)</body>", raw)
        if match:
            raw = match.group(1)
    return re.sub(r"(?is)<(nav|header|footer|aside|form|dialog)\b[^>]*>.*?</\1>", " ", raw)


def fetch_article(url):
    if not url or "news.ycombinator.com" in url:
        return "(bez externího článku – vlastní text nebo diskuse)"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            ctype = (resp.headers.get("Content-Type") or "").lower()
            if "html" not in ctype and "text" not in ctype:
                return f"(externí obsah typu {ctype.split(';')[0] or 'neznámý'} – nestahuji)"
            raw = resp.read(4 * 1024 * 1024).decode(resp.headers.get_content_charset() or "utf-8", "replace")
    except Exception as exc:  # noqa: BLE001 – u článků stačí vědět, že to nešlo
        return f"(externí článek se nepodařilo načíst: {exc})"
    text = html_to_text(extract_main_html(raw))
    text = re.sub(r"\n{3,}", "\n\n", text)[:ARTICLE_CHARS]
    if len(text) < 1500:
        return "(externí článek se načetl jen částečně – pravděpodobně paywall)\n\n" + text
    return text


def fmt_time(ts):
    return datetime.fromtimestamp(ts, TZ).strftime("%-d. %-m. %Y, %H:%M") + " (Europe/Prague)"


def render_bundle(story, comments, article):
    lines = [
        f"# {story['id']}",
        "",
        "## Metadata",
        "- subreddit: Hacker News",
        f"- autor: {story['author']}",
        f"- čas: {fmt_time(story['created_at_i'])}",
        f"- skóre: {story['points']}",
        f"- komentářů: {story['num_comments']}",
        f"- url: {story['url']}",
        f"- permalink: {story['permalink']}",
        "",
        "## Selftext",
        story["story_text"] or "(žádný vlastní text)",
        "",
        "## Externí článek",
        article,
        "",
        "## Komentáře ([skóre | hloubka | autor] text)",
    ]
    if comments:
        for c in comments:
            lines.append(f"[- | {c['depth']} | {c['author']}] {c['text']}")
    else:
        lines.append("(žádné komentáře)")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", argv[0]):
        raise SystemExit("použití: hn-collect.py <YYYY-MM-DD>")
    date = argv[0]
    out_dir = Path(__file__).resolve().parent.parent / "hn" / date
    data_dir = out_dir / "_data"
    (data_dir / "bundles").mkdir(parents=True, exist_ok=True)

    w0, w1 = window(date)
    print(f"sběr HN {date} (okno {w0}..{w1})")
    stories = fetch_stories(w0, w1)
    print(f"  story celkem: {len(stories)}")
    if not stories:
        raise SystemExit("HN nevrátilo žádné story – končím")

    for story in stories:
        story["ai"] = ai_score(story)
    stories.sort(key=lambda s: (-s["ai"], -s["points"], -s["num_comments"]))
    (data_dir / "dataset.json").write_text(
        json.dumps(stories, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    appendix = sorted(
        (s for s in stories if s["num_comments"] >= MIN_COMMENTS),
        key=lambda s: (-s["ai"], -s["points"]),
    )
    (data_dir / "appendix.json").write_text(
        json.dumps(appendix, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    candidates = sorted(
        (s for s in stories if s["points"] >= MIN_POINTS and s["num_comments"] >= MIN_COMMENTS),
        key=lambda s: (-s["ai"], -s["points"], -s["num_comments"]),
    )[:MAX_CANDIDATES]
    print(
        f"  kandidáti na články: {len(candidates)} (z {len(appendix)} v příloze, "
        f"{sum(1 for s in candidates if s['ai'])} s AI/tech termínem)"
    )

    def build(story):
        comments = fetch_comments(story["id"])
        article = fetch_article(story["url"])
        bundle = render_bundle(story, comments, article)
        (data_dir / "bundles" / f"{story['id']}.md").write_text(bundle, encoding="utf-8")
        return story["id"], len(comments)

    with ThreadPoolExecutor(max_workers=8) as pool:
        done = list(pool.map(build, candidates))
    print(f"  balíčků hotovo: {len(done)}")

    (data_dir / "candidates.json").write_text(
        json.dumps(
            [
                {
                    "id": s["id"],
                    "title": s["title"],
                    "url": s["url"],
                    "points": s["points"],
                    "num_comments": s["num_comments"],
                    "bundle": f"hn/{date}/_data/bundles/{s['id']}.md",
                }
                for s in candidates
            ],
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    print(f"hotovo -> {out_dir}")


if __name__ == "__main__":
    main(sys.argv[1:])
