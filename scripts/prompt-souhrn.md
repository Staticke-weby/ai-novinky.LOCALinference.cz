# Úkol: AI souhrn z Redditu do složky s datem (sběr hotový, minimum kroků)

Cíl: pro den `__DATE__` (Europe/Prague) vytvořit `rd/__DATE__/` s podrobnými českými markdown
články o AI novinkách z Redditu. Každý článek má v názvu souboru i na prvním řádku Reddit ID.

Sběr je **hotový** – spustil ho `scripts/rd-collect-web.py` (Reddit přímo z webu) a výsledky leží
v `rd/__DATE__/_data/`:

- `bundles/<id>.md` – kandidáti: metadata, selftext, externí článek, komentáře.
- `candidates.json` – kandidáti (id, title, url, score, num_comments, cesta k balíčku).
- `appendix.json` – všechny posty s ≥ 10 komentáři (pro přílohu indexu).
- `dataset.json` – všechny posty v okně (jen pro dohledání).

Data jsou čerstvá (včerejšek), skóre i počty komentářů jsou z Redditu živě.

## Co už vyšlo (přísně vynechat)

Seznam témat z posledních 3 dnů (Reddit i HN) je v `__RECENT__`. **Přísně vynech** každého
kandidáta, jehož URL, událost nebo produkt se v seznamu objeví – i když má vysoké skóre, i když
jde o nový post nebo repost. Nezařazuj ho ani jako „další diskusi“; prostě ho vynech. Po filtraci
je **15–25 článků** v pořádku, raději méně a bez opakování. Když si nejsi jistý, jestli jde o stejnou
událost, téma vynech. Do metodiky indexu napiš, kolik témat bylo takto vyřazeno.

**Tři kroky, nic víc.** Cílem je ~8 tahů a do 10 minut:

1. **Plán článků — jeden tah** (deduplikace, `_data/plan-clanku.json`, 15–25 článků).
2. **Psaní — jedna `subagent` dávka**: agent `souhrn-writer`, všechny články.
3. **Index a kontrola — jeden `execute`/`shell`** plus jedna `cz-translator` dávka na české titulky.

**Co nedělat:** žádná úvodní rekognoskace (skripty, logy, cizí sessions), žádné zkušební requesty,
psaní plánu dvakrát, ruční úklid, `git`, poll-smyčky. Když něco selže, zapiš, co máš, a pokračuj.

## 1. Plán článků (jeden tah)

Vyber z `candidates.json`/balíčků **15–25 AI relevantních témat** (řádově podle skóre a komentářů),
ale jen ta, která nejsou v `__RECENT__`. Slouč duplicitní témata (stejná URL/událost/produkt = jeden
článek, ostatní posty jako „další diskuse“ s odkazy) a napiš `rd/__DATE__/_data/plan-clanku.json`:

```
[{"id": "...", "dalsi_ids": ["..."], "bundle": "rd/__DATE__/_data/bundles/<id>.md",
  "titulek": "<český titulek>",
  "slug": "<mala-pismena-bez-diakritiky-max-60-znaku>", "klicova_fakta": ["...", "..."]}]
```

Cíl 15–25 článků, max 30. Název souboru je `<id>_<slug>.md`.

## 2. Psaní (jedna `subagent` dávka)

Jedno volání `subagent` na článek, agent **`souhrn-writer`**, všechny v jedné dávce (max 30).
Kontrakt, tvar souboru i jazyk má agent v system promptu – do zadání patří jen konkrétní údaje:

```
id: <reddit_id>
soubor: rd/__DATE__/<id>_<slug>.md
titulek: <český titulek>
klicova_fakta: <3–6 bodů>
balicek: rd/__DATE__/_data/bundles/<id>.md
dalsi_diskuse: <řádky s odkazy na sloučené posty, nebo „žádné“>
```

`subagent` v popředí počká sám, žádné poll-smyčky. Při 429 spouštěj pisatele po dávkách 8–10.

## 3. Index a kontrola (jeden `execute` + jedna dávka)

- `rd/__DATE__/00-index.md`: krátká metodika (odkud data, kolik postů, co chybělo), tabulka článků
  s odkazy a příloha se **všemi** posty z `appendix.json` (id, subreddit, skóre, komentáře, čas,
  titulek). **Odkazy v tabulce i v příloze musí mířit na skutečný název souboru** `<id>_<slug>.md`;
  u sloučených postů na článek, do kterého byly sloučeny (ne na `<id_postu>_<id_článku>_<slug>.md`).
- České titulky dělej **jen pro tabulku článků** (15–25). Příloha má stovky řádků – nech v ní
  **původní titulky** (nepřekládej je). Překlad pošli jedné dávce `subagent` agentů `cz-translator`
  jako JSON worklist `[{"id": "...", "title": "..."}]` a výsledek vrať do tabulky článků.
- Kontrola: spusť `python3 scripts/check-day.py rd/__DATE__` (ověří první řádek `# <id>`, název
  `<id>_<slug>.md`, tvar `# id` + tučný titulek + řádek metadat + **aspoň 3 odstavce prózy** a
  obousměrné odkazy index ↔ soubory). Chybějící/rozbitý článek zadej **jednou** znovu a konči.
- **Nekontroluj** anglické zbytky, atribuci, čísla ani citace – kvalitu drží zadání pisatele.

Na konci napiš shrnutí: počet článků, sloučená témata, počet postů v příloze, časy fází (`plán:`,
`psaní:`, `index:` a celkový) a **počet svých tahů**.
