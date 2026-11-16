#!/usr/bin/env python3
"""PROTOTYP: sběr Redditu přímo z webu (místo Arctic Shift).

Používá cookies z prohlížeče OpenChamber (`Partitions/openchamber-browser`).
S nimi Reddit vrátí i JSON endpointy (`/new.json`, `/comments/<id>.json`), které
obyčejnému curl/urllib vrací 403. Výstup má stejný tvar jako `rd-collect.py`
(`_data/bundles/`, `dataset.json`, `appendix.json`, `candidates.json`).

Použití:
    python3 scripts/rd-collect-web.py 2026-10-07
    python3 scripts/rd-collect-web.py 2026-10-07 --subs LocalLLaMA,ClaudeAI
    python3 scripts/rd-collect-web.py 2026-10-07 --out /tmp/proto
"""
import argparse
import importlib.util
import json
import os
import sqlite3
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor

_spec = importlib.util.spec_from_file_location("rdc", Path(__file__).resolve().parent / "rd-collect.py")
rdc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rdc)

TZ = ZoneInfo("Europe/Prague")
PROJECT = Path(__file__).resolve().parent.parent
COOKIE_DB = Path.home() / ".config" / "OpenChamber" / "Partitions" / "openchamber-browser" / "Cookies"
COOKIE_JAR = PROJECT / "logs" / "reddit-cookies.txt"  # obnovované cookies (gitignored)
CK = {}  # aktuální cookie jar (browser + obnovené Set-Cookie), plní read_cookies()
# `www.reddit.com/....json` je od 11/2026 zablokované i s platnými cookies
# („You've been blocked by network security“), ale `api.reddit.com` stejné
# cookies bere a vrací plné JSON. Proto jde všechno přes api.reddit.com.
RAPI = "https://api.reddit.com"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0 Safari/537.36")
MIN_COMMENTS = rdc.MIN_COMMENTS
MAX_CANDIDATES = rdc.MAX_CANDIDATES
COMMENT_DEPTH = rdc.COMMENT_DEPTH
MAX_COMMENTS = rdc.MAX_COMMENTS
RL_INTERVAL = 1.0  # min. odstup mezi reddit requesty
_rl_lock = threading.Lock()
_rl_last = 0.0
_rl_remaining = None
_rl_reset_at = 0.0


def _pace():
    """Zpozdí request podle hlaviček x-ratelimit-* z Redditu."""
    global _rl_last
    while True:
        with _rl_lock:
            now = time.time()
            if _rl_remaining is not None and _rl_remaining <= 1 and now < _rl_reset_at:
                wait = _rl_reset_at + 1 - now
            else:
                wait = _rl_last + RL_INTERVAL - now
            if wait <= 0:
                _rl_last = now
                return
        time.sleep(min(wait, 30))


def _update_limits(headers):
    global _rl_remaining, _rl_reset_at
    rem = headers.get("x-ratelimit-remaining")
    reset = headers.get("x-ratelimit-reset")
    if rem is not None:
        try:
            _rl_remaining = float(rem)
        except ValueError:
            pass
    if reset is not None:
        try:
            _rl_reset_at = time.time() + float(reset)
        except ValueError:
            pass


SESSION_DEAD = False


def load_jar():
    d = {}
    if COOKIE_JAR.exists():
        for line in COOKIE_JAR.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                n, v = line.split("=", 1)
                d[n.strip()] = v.strip()
    return d


def save_jar():
    COOKIE_JAR.parent.mkdir(parents=True, exist_ok=True)
    COOKIE_JAR.write_text(
        "# reddit cookies (autoobnovované; zdroj: prohlížeč OpenChamber)\n"
        + "\n".join(f"{k}={v}" for k, v in CK.items()) + "\n",
        encoding="utf-8",
    )


def read_cookies():
    """Načte reddit cookies z prohlížeče OpenChamber a slije je s lokálním cookie jarem."""
    global SESSION_DEAD
    try:
        con = sqlite3.connect(f"file:{COOKIE_DB}?mode=ro", uri=True)
        rows = con.execute(
            "select name,value from cookies where host_key like '%reddit%'"
        ).fetchall()
        con.close()
    except sqlite3.Error as exc:
        print(f"nelze přečíst cookies z {COOKIE_DB}: {exc}", file=sys.stderr)
        raise SystemExit(5)
    if not rows:
        print(f"v {COOKIE_DB} nejsou žádné reddit cookies — přihlas se do redditu v prohlížeči OpenChamber", file=sys.stderr)
        raise SystemExit(5)
    CK.clear()
    CK.update(rows)
    CK.update(load_jar())  # obnovené cookies (např. session_tracker) mají přednost
    if "token_v2" not in CK:
        print("  ! chybí token_v2 — session vypršela; otevři reddit v prohlížeči OpenChamber", file=sys.stderr)
        SESSION_DEAD = True
    return CK


def cookie_header():
    return "; ".join(f"{k}={v}" for k, v in CK.items())


def _capture_set_cookie(headers):
    for sc in headers.get_all("Set-Cookie") or []:
        pair = sc.split(";", 1)[0]
        if "=" in pair:
            n, v = pair.split("=", 1)
            n = n.strip()
            if n and n != "token_v2":
                CK[n] = v.strip()


def get_json(url, timeout=30, retries=5):
    global SESSION_DEAD
    last = None
    for attempt in range(retries + 1):
        try:
            _pace()
            req = urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept": "application/json", "Cookie": cookie_header(),
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                _update_limits(r.headers)
                _capture_set_cookie(r.headers)
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code == 403:
                print("  ! HTTP 403 — session vypršela; otevři reddit v prohlížeči OpenChamber", file=sys.stderr)
                SESSION_DEAD = True
                return None
            if exc.code == 429:
                _update_limits(exc.headers)
                reset = exc.headers.get("x-ratelimit-reset")
                wait = (float(reset) + 1) if reset else (5 * (attempt + 1))
                wait = max(2, min(wait, 90))
                print(f"  ! HTTP 429 — pauza {wait:.0f}s a zkusím znovu", file=sys.stderr)
                time.sleep(wait)
                continue
        except Exception as exc:  # noqa: BLE001
            last = exc
        if attempt < retries:
            time.sleep(3)
    print(f"  ! request selhal: {url} ({last})", file=sys.stderr)
    return None


def window(date):
    start = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=TZ)
    return int(start.timestamp()), int((start + timedelta(days=1)).timestamp())


def fetch_subreddit(sub, w0, w1):
    """Stránkuje /new.json od nejnovějších, dokud nedojde pod okno."""
    posts, after, pages = [], None, 0
    while pages < 20:
        params = {"limit": 100, "raw_json": 1}
        if after:
            params["after"] = after
        url = f"{RAPI}/r/{sub}/new?" + urllib.parse.urlencode(params)
        d = get_json(url)
        pages += 1
        if not d:
            break
        ch = d.get("data", {}).get("children", [])
        if not ch:
            break
        past = False
        for c in ch:
            p = c.get("data", {})
            ts = p.get("created_utc") or 0
            if ts < w0:
                past = True
                continue
            if ts < w1:
                posts.append({
                    "id": p.get("id"), "author": p.get("author"),
                    "title": p.get("title"), "selftext": p.get("selftext") or "",
                    "url": p.get("url"), "score": p.get("score") or 0,
                    "num_comments": p.get("num_comments") or 0,
                    "created_utc": ts, "subreddit": p.get("subreddit"),
                    "link_flair_text": p.get("link_flair_text"),
                })
        after = d.get("data", {}).get("after")
        if past or not after:
            break
    print(f"  r/{sub}: {len(posts)} postů ve okně ({pages} stránek)")
    return posts


def fetch_comments_web(post_id):
    url = f"{RAPI}/comments/{post_id}?limit=200&depth={COMMENT_DEPTH}&sort=top&raw_json=1"
    d = get_json(url)
    if not isinstance(d, list) or len(d) < 2:
        return []
    tree = d[1].get("data", {}).get("children", [])
    out = []

    def walk(nodes, depth):
        for n in nodes:
            if n.get("kind") != "t1":
                continue
            dd = n.get("data", {})
            body = (dd.get("body") or "").strip()
            if body:
                out.append({"score": dd.get("score") or 0, "depth": depth,
                            "author": dd.get("author") or "?", "body": body[:rdc.COMMENT_CHARS]})
            rep = dd.get("replies")
            if depth < COMMENT_DEPTH and isinstance(rep, dict):
                walk(rep.get("data", {}).get("children", []), depth + 1)

    walk(tree, 0)
    out.sort(key=lambda c: -c["score"])
    return out[:MAX_COMMENTS]


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("date")
    ap.add_argument("--subs", default=None, help="čárkou oddělené subreddity (výchozí: SUBREDDITS z rd-collect.py)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    subs = [s.strip() for s in args.subs.split(",")] if args.subs else list(rdc.SUBREDDITS)
    date = args.date
    out_dir = Path(args.out) if args.out else PROJECT / "rd" / date
    data_dir = out_dir / "_data"
    (data_dir / "bundles").mkdir(parents=True, exist_ok=True)

    read_cookies()
    w0, w1 = window(date)
    t0 = time.time()
    print(f"web sběr {date} (okno {w0}..{w1}), subredditů: {len(subs)}")

    with ThreadPoolExecutor(max_workers=4) as pool:
        per = list(pool.map(lambda s: fetch_subreddit(s, w0, w1), subs))
    seen, posts = set(), []
    for found in per:
        for p in found:
            if p.get("id") and p["id"] not in seen:
                seen.add(p["id"])
                posts.append(p)
    print(f"  postů celkem: {len(posts)}  ({time.time()-t0:.1f}s)")
    if len(posts) < rdc.MIN_POSTS:
        print(f"  nasbíráno jen {len(posts)} postů (< {rdc.MIN_POSTS}) — sběr přeskočen", file=sys.stderr)
        return 5 if SESSION_DEAD else 1

    posts.sort(key=lambda p: (-(p.get("score") or 0), -(p.get("num_comments") or 0)))
    (data_dir / "dataset.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
    appendix = [p for p in posts if (p.get("num_comments") or 0) >= MIN_COMMENTS]
    (data_dir / "appendix.json").write_text(json.dumps(appendix, ensure_ascii=False, indent=1), encoding="utf-8")
    candidates = appendix[:MAX_CANDIDATES]

    def build(post):
        comments = fetch_comments_web(post["id"])
        article = rdc.fetch_article(post.get("url"))
        (data_dir / "bundles" / f"{post['id']}.md").write_text(
            rdc.render_bundle(post, comments, article), encoding="utf-8")
        return len(comments)

    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(build, candidates))
    (data_dir / "candidates.json").write_text(json.dumps([
        {"id": p["id"], "title": p.get("title", ""), "url": p.get("url", ""),
         "score": p.get("score") or 0, "num_comments": p.get("num_comments") or 0,
         "bundle": f"rd/{date}/_data/bundles/{p['id']}.md"}
        for p in candidates], ensure_ascii=False, indent=1), encoding="utf-8")
    save_jar()
    print(f"hotovo -> {out_dir}  (kandidátů {len(candidates)}, balíčků {len(candidates)}, celkem {time.time()-t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
