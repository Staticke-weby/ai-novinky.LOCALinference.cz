#!/usr/bin/env python3
"""Posbírá Reddit příspěvky za den přes Arctic Shift a připraví podklady.

Nahrazuje prohlížečový sběr: veřejné API, bez 403 a bez prohlížeče (~30 s/den).
Spouští ho `daily.sh` před agentem.

Výstup do `rd/<YYYY-MM-DD>/_data/` (stejný tvar, jaký čeká souhrn-writer):
    dataset.json     – všechny posty v okně
    appendix.json    – posty s >= 10 komentáři
    candidates.json  – kandidáti na články (nejvyšší skóre)
    bundles/<id>.md  – metadata, selftext, externí článek, komentáře

Pozn.: Arctic Shift doplňuje skóre a počty komentářů až ~36 h po publikaci
(do té doby mohou být 1/0). Pro historická data (starší než ~2 dny) je přesný.

Použití: python3 scripts/rd-collect.py 2026-10-01
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
BASE = "https://arctic-shift.photon-reddit.com"
UA = "reddit-ai-souhrn/1.0 (collector)"
SUBREDDITS = [
    "artificial", "ArtificialInteligence", "MachineLearning", "deeplearning",
    "LocalLLaMA", "LocalLLM", "OpenAI", "ChatGPT", "ClaudeAI", "singularity",
    "agi", "StableDiffusion", "comfyui", "LLMDevs", "GeminiAI", "Bard",
    "OpenAIDev", "AIAssisted", "LLM",
]
POST_FIELDS = (
    "id,author,title,selftext,url,score,num_comments,created_utc,subreddit,"
    "link_flair_text,over_18,retrieved_on"
)
MIN_COMMENTS = 10
MIN_POSTS = 5
MAX_CANDIDATES = 40
MAX_COMMENTS = 25
COMMENT_DEPTH = 1
COMMENT_CHARS = 1200
ARTICLE_CHARS = 20000
PAGES = re.compile(r"<[^>]+>")


def get_json(url, params=None, timeout=60, retries=2):
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
                time.sleep(3)
    print(f"  ! request selhal: {url} ({last})", file=sys.stderr)
    return None


def health_check():
    """Rychlý test, zda Arctic Shift odpovídá.

    Při výpadku (522/523/000) se tak nečeká na 19 subredditů × 3 pokusy a den
    se rovnou přeskočí.
    """
    data = get_json(
        f"{BASE}/api/posts/search",
        {"subreddit": SUBREDDITS[0], "limit": 1, "fields": "id"},
        timeout=15,
        retries=0,
    )
    return data is not None


def html_to_text(raw):
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
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", raw).strip()


def extract_main_html(raw):
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
    if not url or "reddit.com" in url or url.startswith("/"):
        return "(bez externího článku – vlastní text nebo diskuse)"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            ctype = (resp.headers.get("Content-Type") or "").lower()
            if "html" not in ctype and "text" not in ctype:
                return f"(externí obsah typu {ctype.split(';')[0] or 'neznámý'} – nestahuji)"
            raw = resp.read(4 * 1024 * 1024).decode(resp.headers.get_content_charset() or "utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return f"(externí článek se nepodařilo načíst: {exc})"
    text = html_to_text(extract_main_html(raw))[:ARTICLE_CHARS]
    if len(text) < 1500:
        return "(externí článek se načetl jen částečně – pravděpodobně paywall)\n\n" + text
    return text


def window(date):
    start = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=TZ)
    return int(start.timestamp()), int((start + timedelta(days=1)).timestamp())


def fetch_subreddit(sub, w0, w1):
    # `auto` vrátí 100–1000; na některé subreddity občas vrátí 422 (přetížení),
    # proto fallback na pevné limity.
    for limit in ("auto", 100, 25):
        data = get_json(
            f"{BASE}/api/posts/search",
            {
                "subreddit": sub,
                "after": w0,
                "before": w1,
                "limit": limit,
                "sort": "desc",
                "fields": POST_FIELDS,
            },
        )
        if data is not None:
            return data.get("data", []) or []
    return []


def fetch_comments(post_id):
    data = get_json(f"{BASE}/api/comments/tree", {"link_id": f"t3_{post_id}", "limit": 300})
    tree = (data or {}).get("data", []) or []
    out = []

    def walk(nodes, depth):
        for node in nodes:
            if node.get("kind") == "more":
                continue
            d = node.get("data", {})
            body = (d.get("body") or "").strip()
            if body:
                out.append(
                    {
                        "score": d.get("score") or 0,
                        "depth": depth,
                        "author": d.get("author") or "?",
                        "body": body[:COMMENT_CHARS],
                    }
                )
            replies = d.get("replies")
            if depth < COMMENT_DEPTH and isinstance(replies, dict):
                walk(replies.get("data", {}).get("children", []), depth + 1)

    walk(tree, 0)
    out.sort(key=lambda c: -c["score"])
    return out[:MAX_COMMENTS]


def fmt_time(ts):
    return datetime.fromtimestamp(ts, TZ).strftime("%-d. %-m. %Y, %H:%M") + " (Europe/Prague)"


def render_bundle(post, comments, article):
    permalink = f"https://www.reddit.com/r/{post['subreddit']}/comments/{post['id']}/"
    lines = [
        f"# {post['id']}",
        "",
        "## Metadata",
        f"- subreddit: r/{post['subreddit']}",
        f"- autor: u/{post.get('author') or '[deleted]'}",
        f"- čas: {fmt_time(post['created_utc'])}",
        f"- skóre: {post.get('score') or 0}",
        f"- komentářů: {post.get('num_comments') or 0}",
        f"- url: {post.get('url') or permalink}",
        f"- permalink: {permalink}",
    ]
    if post.get("link_flair_text"):
        lines.append(f"- flair: {post['link_flair_text']}")
    lines += [
        "",
        "## Selftext",
        (post.get("selftext") or "").strip() or "(žádný vlastní text)",
        "",
        "## Externí článek",
        article,
        "",
        "## Komentáře ([skóre | hloubka | autor] text)",
    ]
    if comments:
        for c in comments:
            lines.append(f"[{c['score']} | {c['depth']} | u/{c['author']}] {c['body']}")
    else:
        lines.append("(žádné komentáře)")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", argv[0]):
        raise SystemExit("použití: rd-collect.py <YYYY-MM-DD>")
    date = argv[0]
    out_dir = Path(__file__).resolve().parent.parent / "rd" / date
    data_dir = out_dir / "_data"
    (data_dir / "bundles").mkdir(parents=True, exist_ok=True)

    w0, w1 = window(date)
    t0 = time.time()
    if not health_check():
        print("Arctic Shift neodpovídá (health-check) — sběr přeskočen", file=sys.stderr)
        return 1
    print(f"sběr Reddit {date} (okno {w0}..{w1}, {len(SUBREDDITS)} subredditů)")

    with ThreadPoolExecutor(max_workers=5) as pool:
        per_sub = list(pool.map(lambda s: fetch_subreddit(s, w0, w1), SUBREDDITS))
    t_posts = time.time()
    seen, posts = set(), []
    for sub, found in zip(SUBREDDITS, per_sub):
        for p in found:
            if p.get("id") and p["id"] not in seen:
                seen.add(p["id"])
                posts.append(p)
    print(f"  postů celkem: {len(posts)}  (posty: {t_posts - t0:.1f}s)")
    if len(posts) < MIN_POSTS:
        print(
            f"  nasbíráno jen {len(posts)} postů (< {MIN_POSTS}) — sběr přeskočen",
            file=sys.stderr,
        )
        return 1

    posts.sort(key=lambda p: (-(p.get("score") or 0), -(p.get("num_comments") or 0)))
    (data_dir / "dataset.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
    appendix = [p for p in posts if (p.get("num_comments") or 0) >= MIN_COMMENTS]
    (data_dir / "appendix.json").write_text(json.dumps(appendix, ensure_ascii=False, indent=1), encoding="utf-8")

    candidates = [p for p in posts if (p.get("num_comments") or 0) >= MIN_COMMENTS][:MAX_CANDIDATES]
    print(f"  kandidáti: {len(candidates)} (v příloze {len(appendix)})")

    def build(post):
        comments = fetch_comments(post["id"])
        article = fetch_article(post.get("url"))
        (data_dir / "bundles" / f"{post['id']}.md").write_text(
            render_bundle(post, comments, article), encoding="utf-8"
        )
        return len(comments)

    with ThreadPoolExecutor(max_workers=6) as pool:
        counts = list(pool.map(build, candidates))
    t_bundles = time.time()
    print(f"  balíčků: {len(counts)}  (komentáře+články: {t_bundles - t_posts:.1f}s)")

    (data_dir / "candidates.json").write_text(
        json.dumps(
            [
                {
                    "id": p["id"],
                    "title": p.get("title", ""),
                    "url": p.get("url", ""),
                    "score": p.get("score") or 0,
                    "num_comments": p.get("num_comments") or 0,
                    "bundle": f"rd/{date}/_data/bundles/{p['id']}.md",
                }
                for p in candidates
            ],
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    print(f"hotovo -> {out_dir}  (celkem {t_bundles - t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
