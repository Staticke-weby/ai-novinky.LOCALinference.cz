#!/usr/bin/env python3
"""Jeden denní přehled z Redditu a Hacker News pro LinkedIn.

- Vezme články z `rd/<datum>/` a `hn/<datum>/` v pořadí indexů.
- **Sloučí stejná témata z Redditu a HN** do jedné sekce: podle shodné URL
  externího článku, podle `souvisi_s` z HN plánu a podle podobnosti titulků.
- Výchozím režimem jsou **anotace**: každé téma jen jako první odstavec
  (anotace), žádný plný text (`--full-top 0`). Dřív se prvních 25 témat dávalo
  v plném znění; dnes to jde jen na výslovné přání (`--full-top N`).
  Limit Docs MD je 120 000 znaků; kdyby se to nevešlo, počet celých témat
  se sám snižuje po pěti.
- Zapíše `dny/<datum>/prehled.md` a `dny/<datum>/temata.json`.

Použití:
    python3 scripts/build-denni.py 2026-10-26                  # vše anotace (výchozí)
    python3 scripts/build-denni.py 2026-10-26 --full-top 15     # 15 témat plně, zbytek anotace
    python3 scripts/build-denni.py            # včerejšek (Europe/Prague)
"""

import importlib.util
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

PROJECT = Path(__file__).resolve().parent.parent
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

_spec = importlib.util.spec_from_file_location(
    "build_prehled", Path(__file__).resolve().parent / "build-prehled.py"
)
build_prehled = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build_prehled)


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


def stems(text):
    """Kmeny slov (prvních 5 znaků) — česká flexe jinak shodu tokenů zabije."""
    return {w[:5] for w in toks(text)}


def bundle_url(src, day, cid):
    path = PROJECT / src / day / "_data" / "bundles" / f"{cid}.md"
    if not path.is_file():
        return ""
    m = re.search(r"^- url:\s*(\S+)", path.read_text(encoding="utf-8", errors="replace"), re.M)
    return m.group(1).strip() if m else ""


def parse_article(path, src, day):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    title = path.stem
    meta = ""
    body = []
    state = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if state >= 2:
                body.append("")
            continue
        if state == 0:
            m = re.match(r"^\*\*(.+?)\*\*\s*$", stripped)
            if m:
                title = m.group(1).strip()
                state = 1
                continue
            title = stripped
            state = 1
            continue
        if state == 1:
            meta = stripped
            state = 2
            continue
        body.append(line)
    paragraphs = [p.strip() for p in "\n".join(body).split("\n\n") if p.strip()]
    cid = path.name.split("_", 1)[0]
    return {
        "src": src,
        "id": cid,
        "title": title,
        "meta": meta,
        "lead": paragraphs[0] if paragraphs else "",
        "paragraphs": paragraphs,
        "full": "\n\n".join(paragraphs),
        "url": bundle_url(src, day, cid),
    }


def plan_souvisi(src, day):
    path = PROJECT / src / day / "_data" / "plan-clanku.json"
    if not path.is_file():
        return {}, {}
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}, {}
    id_to_primary = {}
    links = {}
    for item in plan:
        primary = item.get("id", "")
        for cid in [primary] + list(item.get("dalsi_ids") or []):
            id_to_primary[cid] = primary
        if item.get("souvisi_s"):
            links[primary] = item["souvisi_s"]
    return id_to_primary, links


def plan_facts(src, day):
    """Klíčová fakta z plánu dne (id -> seznam faktů), včetně sloučených id."""
    path = PROJECT / src / day / "_data" / "plan-clanku.json"
    if not path.is_file():
        return {}
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}
    out = {}
    for item in plan:
        facts = item.get("klicova_fakta") or []
        for cid in [item.get("id", "")] + list(item.get("dalsi_ids") or []):
            if cid:
                out[cid] = facts
    return out


def ordered_articles(day_dir):
    return build_prehled.ordered_articles(day_dir)


def pretty_date(day):
    y, m, d = day.split("-")
    return f"{int(d)}. {int(m)}. {y}"


def is_post_meta(text):
    """Je odstavec jen o tom, kdo post sdílel / že chybí text, obrázek nebo článek?"""
    head = (text or "").strip()[:260].lower()
    if not head:
        return False
    if re.match(r"^(příspěvek|vlastní text|externí článek)\b", head):
        return True
    if re.match(r"^(uživatel|uživatelka)\b", head) and any(
        w in head
        for w in (
            "nasdílel",
            "sdílel odkaz",
            "hodil odkaz",
            "přiložil odkaz",
            "přidal odkaz",
            "odkázal",
            "přidal",
            "nepřidal",
            "bez vlastního textu",
            "neměl vlastní text",
            "neměla vlastní text",
            "vlastní text",
            "samotný příspěvek",
            "příspěvek obsah",
            "jen odkaz",
            "pouze odkaz",
        )
    ):
        return True
    if re.match(r"^(na hacker news|na redditu)\b", head) and any(
        w in head for w in ("objevil odkaz", "bez vlastního", "odkaz na")
    ):
        return True
    if "se nepodařilo načíst" in head or "nepodařilo načíst" in head:
        return True
    if re.match(r"^(článek|text|odkazovaný text)\b", head) and any(
        w in head for w in ("nepodařilo", "nedostupn", "paywall", "placen")
    ):
        return True
    return False


def lead_penalty(text):
    """Čím víc je úvod jen „uživatel nasdílel odkaz“ nebo shrnutí diskuse, tím horší."""
    head = (text or "")[:180].lower()
    if is_post_meta(text):
        return 2
    if re.match(r"^(diskuse|v diskusi|ve vlákně|komentující|reakce se|debata se)\b", head):
        return 1
    return 0


def best_lead(rec):
    """První odstavec, který není jen o sdílení/chybějícím textu; jinak původní lead."""
    for para in rec.get("paragraphs", []):
        if not is_post_meta(para):
            return para
    return rec.get("lead", "")


def strip_meta_sentences(text):
    """Z prvního odstavce vyhodí věty typu „příspěvek neměl text/obrázek“."""
    sentences = re.split(r"(?<=[.!?])\s+", text or "")
    keep = [
        s
        for s in sentences
        if s.strip()
        and not is_post_meta(s)
        and not re.search(r"story dne|nasbíral stovky komentářů", s, re.I)
    ]
    cleaned = " ".join(keep).strip()
    return cleaned or text


def full_body(rec):
    """Celý článek bez uvozovacích meta odstavců; když článek začínal meta textem,
    dostane na začátek věcná klíčová fakta, aby první věta nesla téma."""
    paras = list(rec.get("paragraphs", []))
    if not paras:
        return rec.get("full", "")
    meta_opening = is_post_meta(paras[0])
    while paras and is_post_meta(paras[0]):
        paras = paras[1:]
    if paras:
        paras[0] = strip_meta_sentences(paras[0])
    body = "\n\n".join(paras)
    if meta_opening and paras:
        first = paras[0]
        if is_discussion_start(first) or is_source_note(first):
            intro = " ".join(clean_facts(rec))
            if intro and not body.startswith(intro):
                body = intro + ("\n\n" + body if body else "")
    return body or rec.get("full", "")


def is_discussion_start(text):
    return bool(
        re.match(
            r"^(diskuse|v diskusi|ve vlákně|komentující|komentáře|nejvíc hlasů|"
            r"nejviditelnější|nejhlasitější|nejvýraznější|nejzajímavější|"
            r"reakce|debata|uživatelé v)\b",
            (text or "").strip().lower(),
        )
    )


def is_source_note(text):
    head = (text or "").strip().lower()
    if not re.match(r"^(samotný odkazovaný text|odkazovaný text|text je|článek je)\b", head):
        return False
    return any(w in head for w in ("placen", "paywall", "nedostup", "nepodařilo"))


def trim_sentences(text, limit=900):
    """Zkrátí na celé věty, aby anotace nekončila uprostřed."""
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    # Dělit jen tam, kde další věta začíná velkým písmenem nebo uvozovkou.
    # Tím zůstanou celé „1. října“ i zkratky typu „např. další“.
    parts = re.split(r"(?<=[.!?])\s+(?![a-zá-ž0-9])", text)
    out = []
    total = 0
    for part in parts:
        if out and total + len(part) + 1 > limit:
            break
        out.append(part)
        total += len(part) + 1
    return " ".join(out).strip() or text


def clean_facts(rec):
    picked = []
    for fact in rec.get("facts", []):
        fact = (fact or "").strip()
        if not fact or is_post_meta(fact):
            continue
        low = fact.lower()
        if re.match(r"^(uživatel|uživatelka)\b", low):
            continue
        if re.match(
            r"^(komentující|komentáře|diskuse|v diskusi|ve vlákně|reakce|debata|uživatelé)\b",
            low,
        ):
            continue
        if low.startswith(("story měla", "příspěvek měl")):
            continue
        if ("story" in low or "hacker news" in low or "reddit" in low) and (
            "bod" in low or "komentář" in low
        ):
            continue
        if picked and len(" ".join(picked + [fact])) > 520:
            break
        picked.append(fact)
        if len(picked) == 2:
            break
    return picked


def repeats_facts(para, facts_text):
    """Pokrývá odstavec většinu klíčových faktů? Pak by se v anotaci opakoval."""
    ft = stems(facts_text)
    pt = stems(para)
    if not ft or not pt:
        return False
    return len(ft & pt) / len(ft) >= 0.6


def annotation_body(rec):
    """Delší anotace: věcné odstavce článku, max. ~900 znaků.
    Klíčová fakta z plánu se použijí jen jako úvod, když článek začíná diskusí
    nebo nemá použitelný odstavec — jinak by se stejné věty opakovaly."""
    facts_text = " ".join(clean_facts(rec))
    paras = []
    for para in rec.get("paragraphs", []):
        if is_post_meta(para) or is_source_note(para):
            continue
        cleaned = strip_meta_sentences(para)
        if cleaned.strip():
            paras.append(cleaned)

    lead_is_weak = not paras or is_discussion_start(paras[0])
    parts = [facts_text] if facts_text and lead_is_weak else []

    start = 0
    if facts_text and paras and re.match(
        r"^(uživatel|uživatelka|autor|autorka)\b", paras[0].lower()
    ):
        start = 1
    para_count = 0
    for para in paras[start:]:
        if parts and facts_text and repeats_facts(para, facts_text):
            continue
        parts.append(para)
        para_count += 1
        if len(" ".join(parts)) >= 700 or para_count >= 2:
            break

    body = " ".join(parts).strip() or best_lead(rec)
    return trim_sentences(body, 900)


def build(day, full_top=0):
    day_dir = PROJECT / "dny" / day
    day_dir.mkdir(parents=True, exist_ok=True)

    rd_dir = PROJECT / "rd" / day
    hn_dir = PROJECT / "hn" / day
    records = {}
    for src, folder in (("rd", rd_dir), ("hn", hn_dir)):
        if not (folder / "00-index.md").is_file():
            continue
        for path in ordered_articles(folder):
            rec = parse_article(path, src, day)
            records[(src, rec["id"])] = rec

    if not records:
        raise SystemExit(f"pro {day} nejsou články ani v rd/, ani v hn/")

    facts = {}
    for src in ("rd", "hn"):
        facts.update(plan_facts(src, day))
    for rec in records.values():
        rec["facts"] = facts.get(rec["id"], [])

    # Explicitní propojení z HN plánu (souvisi_s) -> redditový článek.
    rd_ids, _ = plan_souvisi("rd", day)
    _, hn_links = plan_souvisi("hn", day)
    rd_by_primary = {
        r["id"]: k for k, r in records.items() if k[0] == "rd"
    }
    for hn_key, reddit_id in hn_links.items():
        hn_key = ("hn", hn_key)
        reddit_id = rd_ids.get(reddit_id, reddit_id)
        rd_key = rd_by_primary.get(reddit_id)
        if hn_key in records and rd_key:
            records[hn_key]["_link"] = rd_key

    parent = {k: k for k in records}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for key, rec in records.items():
        if rec.get("_link"):
            union(rec["_link"], key)

    by_url = {}
    for key, rec in records.items():
        u = norm_url(rec["url"])
        if u:
            by_url.setdefault(u, []).append(key)
    for keys in by_url.values():
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i][0] != keys[j][0]:
                    union(keys[i], keys[j])

    rd = [(k, r) for k, r in records.items() if k[0] == "rd"]
    hn = [(k, r) for k, r in records.items() if k[0] == "hn"]
    for rk, rr in rd:
        rt = toks(rr["title"])
        for hk, hr in hn:
            if jaccard(rt, toks(hr["title"])) >= 0.55:
                union(rk, hk)

    groups = {}
    for key in records:
        groups.setdefault(find(key), []).append(key)

    seen_groups = set()
    topics = []
    longest = max(len(rd), len(hn))
    for i in range(longest):
        for bucket in (rd, hn):
            if i >= len(bucket):
                continue
            key = bucket[i][0]
            root = find(key)
            if root in seen_groups:
                continue
            seen_groups.add(root)
            members = sorted(groups[root], key=lambda k: (0 if k[0] == "rd" else 1))
            primary_key = members[0]
            primary = records[primary_key]
            title = primary["title"]
            sources = []
            for k in members:
                if k[0] not in sources:
                    sources.append(k[0])
            topics.append(
                {
                    "title": title,
                    "sources": sources,
                    "ids": {k[0]: records[k]["id"] for k in members},
                    "members": members,
                    "primary": primary_key,
                }
            )

    counts = {"rd": len(rd), "hn": len(hn)}
    full_count = max(0, min(full_top, len(topics)))
    if full_count == 0:
        scope = "Každé téma je anotace s odkazem na původní diskusi."
    elif full_count == len(topics):
        scope = "Všechna témata jsou v plném znění."
    else:
        scope = (
            f"Nejlepších **{full_count}** témat je v plném znění, zbytek tvoří anotace "
            "s odkazy na původní diskuse."
        )
    parts = [f"# AI novinky – {pretty_date(day)}", ""]
    summary = []
    if counts["rd"]:
        summary.append(f"**{counts['rd']}** článků z Redditu")
    if counts["hn"]:
        summary.append(f"**{counts['hn']}** z Hacker News")
    parts.append(
        "Denní souhrn: " + " a ".join(summary) + f", po sloučení **{len(topics)}** témat. "
        + scope
    )
    parts += ["", "## Obsah", ""]

    used_anchors = {}
    anchors = []
    for topic in topics:
        base = build_prehled.slugify(topic["title"]) or "tema"
        anchor = base
        if anchor in used_anchors:
            used_anchors[base] += 1
            anchor = f"{base}-{used_anchors[base]}"
        else:
            used_anchors[base] = 1
        anchors.append(anchor)
        parts.append(f"- [{topic['title']}](#{anchor})")
    parts.append("")

    for idx, (topic, anchor) in enumerate(zip(topics, anchors)):
        members = [records[k] for k in topic["members"]]
        primary = records[topic["primary"]]
        with_lead = [r for r in members if r["lead"]]
        lead_rec = (
            min(with_lead, key=lambda r: (lead_penalty(best_lead(r)), -len(best_lead(r))))
            if with_lead
            else primary
        )
        parts += ["---", "", f"## {topic['title']}", ""]
        for rec in members:
            meta = rec["meta"]
            if rec["src"] == "hn":
                meta = re.sub(r"^Hacker News\s*·\s*", "", meta)
                parts.append(f"- **Hacker News** · {meta}")
            else:
                parts.append(f"- **Reddit** · {meta}")
        parts.append("")
        body = full_body(lead_rec) if idx < full_count else annotation_body(lead_rec)
        if body:
            parts += [body, ""]
        main_lead = best_lead(lead_rec)
        for rec in members:
            if rec is lead_rec:
                continue
            other = best_lead(rec)
            if not other or lead_penalty(other) >= 2:
                continue
            if jaccard(toks(main_lead), toks(other)) < 0.45:
                label = "Hacker News" if rec["src"] == "hn" else "Reddit"
                parts += [f"**{label}:** {other}", ""]

    out = day_dir / "prehled.md"
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")

    data = {
        "date": day,
        "clanky": len(records),
        "temata": [
            {
                "title": t["title"],
                "sources": t["sources"],
                "ids": t["ids"],
            }
            for t in topics
        ],
    }
    (day_dir / "temata.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    return out, len(topics), len(records)


def main(argv):
    full_top = 0  # výchozí režim: každé téma jen jako anotace
    args = []
    i = 0
    while i < len(argv):
        if argv[i] == "--full-top" and i + 1 < len(argv):
            try:
                full_top = max(0, int(argv[i + 1]))
            except ValueError:
                raise SystemExit("--full-top bere celé číslo")
            i += 2
        else:
            args.append(argv[i])
            i += 1
    if len(args) > 1:
        raise SystemExit("použití: build-denni.py [YYYY-MM-DD] [--full-top N]")
    day = args[0] if args else (date.today() - timedelta(days=1)).isoformat()

    n = full_top
    while True:
        out, topics, articles = build(day, n)
        size = len(out.read_text(encoding="utf-8"))
        if size <= 120000 or n == 0:
            break
        n = max(0, n - 5)

    print(
        f"{out} ({topics} témat z {articles} článků, {size} znaků, "
        f"{min(n, topics)} celých)"
    )
    if size > 120000:
        print("VAROVÁNÍ: soubor přesahuje limit Docs MD 120 000 znaků")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
