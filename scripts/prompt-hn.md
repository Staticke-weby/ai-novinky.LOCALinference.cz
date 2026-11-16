# Úkol: denní AI/tech souhrn z Hacker News do složky s datem

Cíl: za **včerejší den** (Europe/Prague) vytvořit `hn/__DATE__/` s podrobnými českými markdown
články o AI/tech novinkách z Hacker News. Každý článek má v názvu souboru i na prvním řádku HN id.

Sběr je **hotový** – spustil ho `scripts/hn-collect.py` a výsledky leží v `hn/__DATE__/_data/`:

- `bundles/<id>.md` – 40–45 kandidátů: metadata, selftext, externí článek, komentáře.
- `candidates.json` – kandidáti (id, title, url, points, num_comments, cesta k balíčku).
- `appendix.json` – všechny story s ≥ 10 komentáři (pro přílohu indexu).
- `dataset.json` – všechny story v okně (jen pro dohledání).

## Co už vyšlo

`__RECENT__` má dvě části:

- **Dnes na Redditu** – stejné téma smíš zpracovat, ale v plánu ho označ `souvisi_s: <reddit_id>`.
  Ve sloučeném denním přehledu se spojí do jedné sekce s redditovým článkem.
- **Poslední 3 dny** – **přísně vynech** každého kandidáta, jehož URL, událost nebo produkt se
  v seznamu objeví, i když jde o nový post/repost. Nezařazuj ho ani jako „další diskusi“.

Po filtraci je **12–22 článků** v pořádku, raději méně a bez opakování. Když si nejsi jistý, jestli jde
o stejnou událost, téma vynech. Do metodiky indexu napiš, kolik témat bylo vyřazeno jako už vyšlá.

**Tři kroky, nic víc.** Cílem je ~8 tahů a do 12 minut:

1. **Plán článků — jeden tah** (deduplikace, `_data/plan-clanku.json`, 12–22 článků).
2. **Psaní — jedna `subagent` dávka**: agent `souhrn-writer`, všechny články.
3. **Index a kontrola — jeden `execute`/`shell`** plus jedna `cz-translator` dávka na české titulky.

**Co nedělat:** žádná úvodní rekognoskace (skripty, logy, cizí sessions), žádné zkušební requesty,
psaní plánu dvakrát, ruční úklid, `git`, poll-smyčky. Když něco selže, zapiš, co máš, a pokračuj.

## 1. Plán článků (jeden tah)

Vyber z `candidates.json`/balíčků **jen AI/tech relevantní** témata (umělá inteligence, ML, LLM,
agenti, hardware/čipy/GPU, robotika, vývojářské nástroje, bezpečnost a etika AI, AI byznys) a jen
ta, která nejsou v `__RECENT__` (same-day Reddit výjimka viz výše). Čistě obecné story (politika,
společnost, věda mimo AI, klasické programování bez AI přesahu) vynech.

Slouč duplicitní témata (stejná událost/produkt/URL = jeden článek, ostatní jako „další diskuse“)
a napiš `hn/__DATE__/_data/plan-clanku.json`:

```
[{"id": "...", "dalsi_ids": ["..."], "souvisi_s": "<reddit_id nebo null>",
  "bundle": "hn/__DATE__/_data/bundles/<id>.md",
  "titulek": "<český titulek>",
  "slug": "<mala-pismena-bez-diakritiky-max-60-znaku>", "klicova_fakta": ["...", "..."]}]
```

Cíl 12–22 článků, max 25. Název souboru je `<id>_<slug>.md`.

## 2. Psaní (jedna `subagent` dávka)

Jedno volání `subagent` na článek, agent **`souhrn-writer`**, všechny v jedné dávce. Kontrakt, tvar
souboru i jazyk má agent v system promptu – do zadání patří jen konkrétní údaje:

```
id: <hn_id>
soubor: hn/__DATE__/<id>_<slug>.md
titulek: <český titulek>
klicova_fakta: <3–6 bodů>
balicek: hn/__DATE__/_data/bundles/<id>.md
dalsi_diskuse: <řádky s odkazy na sloučené story, nebo „žádné“>
```

`subagent` v popředí počká sám, žádné poll-smyčky. Při 429 spouštěj pisatele po dávkách 8–10.

Poznámka k HN: komentáře nemají veřejné skóre (v balíčku je místo něj `-`) a žádné skóre
nezmiňuj; pořadí komentářů odpovídá řazení HN.

## 3. Index a kontrola (jeden `execute` + jedna dávka)

- `hn/__DATE__/00-index.md`: krátká metodika (kolik story, odkud, co chybělo), tabulka článků
  s odkazy a příloha se **všemi AI/tech story z `appendix.json`** (id, skóre, komentáře, čas Praha,
  titulek). Odkazy v tabulce i v příloze musí mířit na skutečný název souboru `<id>_<slug>.md`;
  u sloučených story na článek, do kterého byly sloučeny (jinak na diskusi na HN).
- Titulky v tabulce i v příloze **česky** – pošli je jedné dávce `subagent` agentů `cz-translator`
  jako JSON worklist `[{"id": "...", "title": "..."}]`, výsledek vrať do indexu.
- Kontrola: spusť `python3 scripts/check-day.py hn/__DATE__` (ověří první řádek `# <hn_id>`, tvar
  `# id` + tučný titulek + řádek metadat + **aspoň 3 odstavce prózy** a obousměrné odkazy
  index ↔ soubory). Chybějící/rozbitý článek zadej **jednou** znovu a konči.
- Nekontroluj anglické zbytky, atribuci, čísla ani citace – kvalitu drží zadání pisatele.

Na konci napiš shrnutí: počet článků, sloučená témata, počet story v příloze, časy fází
(`plán:`, `psaní:`, `index:` a celkový) a **počet svých tahů**.
