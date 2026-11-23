# Zkušenosti a poznámky

Provozní deník k dennímu Reddit AI souhrnu. Co se osvědčilo, co bolí a na co si dát pozor.

## Migrace z omp na OpenCode (27. 9. 2026)

Pipeline původně běžela na `omp` (OpenChamber). Přepsali jsme ji na OpenCode V2:

- `scripts/daily.sh` volá `opencode run --auto --model … --title …` místo `omp -p --auto-approve --cwd …`.
  Proměnné se přejmenovaly na `OPENCODE_BIN` / `OPENCODE_MODEL`.
- `scripts/prompt-souhrn.md` je metodika v14 postavená na nástrojích OpenCode: `execute` (Code Mode)
  místo `eval`, `subagent` místo `task`, `webfetch` místo `read(url)`.
- `scripts/subagent-bench.py` čte OpenCode SQLite (`session_v2` + `session_message`) místo omp JSONL
  sessions (`~/.omp/agent/sessions`).
- Agenti žijí v `.opencode/agents/` (dřív `.omp/agents/`, které se smazalo).

### Na co si dát pozor

- **Nepiš do skriptu, který zrovna běží.** 13. 11. 2026 se upravoval `prehledy.sh` za běhu
  (změna výchozího `FULL_TOP`) a bash, který čte skript po částech, se po doběhnutí `daily.sh`
  v souboru ztratil: `scripts/prehledy.sh: řádek 48: --push: příkaz nenalezen`, exit 127.
  Reddit už byl hotový a pushnutý, HN se vůbec nespustilo. Řešení: úpravy skriptů dělat před
  spuštěním nebo po něm; když se to stane, stačí `prehledy.sh` pustit znovu — hotový den
  `daily.sh` přeskočí.
- **`hub wait` v OpenCode neexistuje.** `subagent` v popředí doběhne a vrátí výsledek sám. Žádné
  poll-smyčky ani spouštění na pozadí, jen aby se „něco dělo“.
- **`fetch` uvnitř `execute` (Code Mode) není.** Runtime nemá přímý filesystem, importy, timery ani
  `fetch`. Když je v katalogu `write`, jde zapsat průběžně; když ne, musí se data vrátit z `execute`
  a zapsat mimo něj.
- **Reddit blokuje přímé HTTP** (`curl` i `webfetch` na `reddit.com` vrací 403, i s browser UA).
  Sběr proto nejede přes prohlížeč, ale přes archiv **Arctic Shift** (`scripts/rd-collect.py`).
  HN má vlastní veřejné API (`scripts/hn-collect.py`).
- **Prohlížeč už sběr nepotřebuje.** Obě kolekce jsou skriptované, takže běh nevyžaduje desktopovou
  službu OpenCode/OpenChamber (prohlížečová cesta byla pomalá a křehká).
- **Arctic Shift doplňuje skóre a počty komentářů až ~36 h po publikaci** (do té doby jsou 1/0).
  Proto Reddit běží se zpožděním **3 dny** (`--days`, výchozí 3), kdy jsou data sednutá.
  HN má data čerstvá a jede výchozí **1 den** zpět.
- **`subagent` běží na modelech z `.opencode/agents/`.** `souhrn-writer` i `cz-translator` používají
  `opencode-go/muse-spark-1.3-contributor`; překlad titulků se tím drží levný.
- **muse-spark musí být povolený ve workspace.** Model „trains on request data“, takže ho workspace
  privacy defaultně blokuje a oba agenti pak spadnou na `Upstream request failed`. Řešení: v OpenCode
  Go zapnout *Allow paid endpoints that train on request data* (nebo model v agentech přepnout).
- **Pozor na `description` v YAML frontmatteru agenta.** Neuvozovkovaná hodnota s `: ` uvnitř
  (např. `… Czech article: what happened …`) rozbije parsování a agent se vůbec nezaregistruje jako
  subagent (`Agent <x> cannot run as a subagent`). Dávej description do uvozovek.

## Provoz

- **Zkratka „vytvoř přehledy" (nebo „vytvoř články", „vytvoř souhrny")** = celý denní balík: Reddit + HN
  (`scripts/daily.sh --publish --push`, resp. `--hn`), tedy sběr → články → sloučený den → web na
  GitHub Pages → push, a nakonec LinkedIn příspěvek (`scripts/build-linkedin.py`).
  Vše jedním příkazem: `scripts/prehledy.sh`.

- **Výchozí režim jsou anotace (od 13. 11. 2026).** `scripts/prehledy.sh` i
  `scripts/build-denni.py` mají `FULL_TOP=0` / `--full-top 0` jako výchozí: každé téma dne
  jen jako anotace, žádný plný text. Není potřeba nic psát ani nastavovat.
  Plné texty jen na výslovné přání: `FULL_TOP=25 scripts/prehledy.sh`
  (nebo `python3 scripts/build-denni.py <datum> --full-top 25`).
  Pro už hotový den stačí `python3 scripts/build-denni.py <datum>`
  a `python3 scripts/publish-docs.py dny/<datum>` (publikace aktualizuje stejnou URL přes PATCH).

- **LinkedIn příspěvek se vždy vloží do chatu jako blok kódu.** Orchestrující agent ho po
  doběhnutí `prehledy.sh` zobrazí ve své odpovědi (nad shrnutím běhu) v ohrazeném bloku ```
  (ať se dá rovnou zkopírovat). `build-linkedin.py` ho zároveň ukládá do `logs/linkedin.txt`,
  takže se dá snadno vyzvednout i mimo výpis na pozadí.

- **Index a kontrola.** `00-index.md` obsahuje tabulku článků a přílohu všech postů s ≥10 komentáři.
  **České titulky se překládají jen pro tabulku článků** (15–25) – příloha má stovky řádků a nechává
  **původní titulky** (dřív se překládala i příloha, což dělalo ~400 zbytečných překladů a zpomalovalo
  běh). Odkazy v tabulce i v příloze musí vždy mířit na skutečný název `<id>_<slug>.md`; u sloučených
  postů na článek, do kterého byly sloučeny.
- **LinkedIn bere titulky z tabulky indexu.** Buňka titulku má dvě podoby:
  - starší indexy: markdown odkaz `[titulek](soubor.md)` (u sloučených `… <br>(sloučeno: ID)`);
  - novější indexy: **holý text** a odkaz na soubor v samostatném sloupci.
  `build-linkedin.py` (`cell_title`) proto buňku bere jako odkaz **jen když jí skutečně je**
  (celá sedí na `[…] (….md)`) a jinak ji nechá být. Dřív slepě rušil `](….md)` a pak vedoucí
  `[`, což u holého titulku začínajícího závorkou (`[Smutné] …`) ukouslo jen `[` a nechalo
  `Smutné] …`. Vnořená závorka v odkazu (`[[AKTUALIZACE] …](soubor.md)`) se řeší
  negreedy labelem, takže Markdown/`<br>` neprosákne.
  **Hlavička sloupce s titulkem se liší:** Reddit píše `Titulek`, HN občas `Článek` —
  `build-linkedin.py` bere oboje (dřív znal jen `Titulek`, takže u HN indexu s `Článek`
  našel 0 článků a příspěvek vyšel bez HN: `0 článků`, žádné `HN:` odrážky).
  **Od 27. 10. 2026** bere `prehledy.sh` témata ze sloučeného `dny/<datum>/temata.json`
  (`build-linkedin.py --den`); cesta z tabulky indexu zůstává pro ruční běh bez `--den`.
- **Kontrola před commitem** dělá `python3 scripts/check-day.py <složka dne>`: první řádek `# <id>`,
  název `<id>_<slug>.md`, ≥3 odstavce prózy bez `##` sekcí, obousměrné `.md` odkazy index ↔ soubory.
  (Dřív to byl inline Python v promptu; rozbíjel se na uvozovkách v titulek.)
- **Mezivýsledky se necommitují** — od 16. 11. 2026 je gitignored celé `_data/`
  (dumpy, plné texty cizích článků, obrázky, překlady, plány). Do repa patří jen
  články, indexy, `dny/` a vygenerovaný `docs/` (viz sekce Web na GitHub Pages).
- **`--force` maže celou složku dne**, aby v `_data` nezůstaly balíčky a články z předchozího běhu.

## Opakování témat a jeden denní přehled (27. 10. 2026)

Denní souhrny se opakovaly: deduplikace dřív fungovala jen v rámci jednoho dne a jednoho zdroje.
Zavřené to je na dvou místech:

- **Přísné vynechání proti posledním 3 dnům.** `scripts/recent-topics.py <datum> --source rd|hn`
  vypíše témata z předchozích 3 dnů z Redditu i HN (titulek, původní titulek, URL, id).
  `daily.sh` ho uloží do `logs/recent-<datum>-<zdroj>.md` a cestu vloží do promptu místo
  `__RECENT__`. Plánovač je **přísně** vynechá – i nový post/repost, i když má vysoké skóre.
  Cíle se snížily na 15–25 článků (Reddit) a 12–22 (HN).
- **Stejné téma z Redditu a HN se slučuje, nevynechává.** HN běh dostane navíc dnešní Reddit
  a v plánu ho označí `souvisi_s: <reddit_id>`. Ve sloučeném přehledu se obě zpracování spojí
  do jedné sekce (dva řádky metadat + odkazy na obě diskuse).
- **Kontrola.** `recent-topics.py <datum> --source rd|hn --check` porovná hotový den s předchozími
  3 dny (přesná URL nebo titulek s Jaccardem ≥ 0,7) a vypíše `OPAKOVÁNÍ:`. `daily.sh` ji pouští
  po agentovi; je to jen varování, ne blokace dne.

**Jeden md na den pro LinkedIn** dělá `scripts/build-denni.py <datum>`:

- vezme `rd/<datum>/` i `hn/<datum>/` v pořadí indexů a střídavě je prokládá (RD1, HN1, RD2, …);
- stejná témata sloučí podle shodné externí URL, podle `souvisi_s` a podle podobnosti titulků
  (Jaccard ≥ 0,55); v sekci jsou pak obě metadata a odkazy na obě diskuse;
- **každé téma jako anotaci** (výchozí od 13. 11. 2026): věcné odstavce článku
  (max. ~900 znaků); klíčová fakta z plánu se použijí jen jako úvod, když článek začíná
  diskusí nebo nemá použitelný odstavec — jinak se stejné věty opakovaly. Meta odstavce
  (kdo sdílel, chybí text/obrázek, článek se nenačetl) se přeskakují. Den má pak ~35 kB.
  Plné texty jen na výslovné přání (`--full-top N` = prvních N témat plně); 26. 10. měl
  44 článků → 41 témat → ~97 kB s 25 plnými texty. Limit Docs MD je 120 000 znaků, a kdyby
  se to nevešlo, `build-denni.py` sám snižuje počet celých témat po pěti.
- u plných textů se zahazují uvozovací meta odstavce („uživatel nasdílel…“, „článek se nepodařilo
  načíst…“) a věty o tom, že příspěvek neměl text nebo obrázek. `souhrn-writer` má od 27. 10. 2026
  pravidlo, že **první odstavec nese hlavní téma a fakta**, nikdy ne kdo to sdílel nebo co chybělo;
- zapíše `dny/<datum>/prehled.md` a `dny/<datum>/temata.json` (seznam sloučených témat pro
  LinkedIn); `dny/` je gitignored.

`scripts/publish-docs.py` umí publikovat i hotový soubor / složku bez `00-index.md`
(`python3 scripts/publish-docs.py dny/2026-10-26`), takže den má **jeden share**.
`scripts/prehledy.sh` už per-source `--publish` nezadává: po obou bězích sloučí den, postaví web
(`build-site.py` + `push-day.sh`) a zavolá `build-linkedin.py --den <datum>`, který dá do
příspěvku **jeden odkaz** (`Celý denní přehled: … – 41 témat z 44 článků: <url>`).
Per-source publikace zůstává jen pro ruční `daily.sh --publish`.

**Název při sdílení na LinkedIn** bere Docs MD z `filename` (do `og:title`, `og:image` i hlavičky
share), ne z H1 v markdownu. `publish-docs.py` proto posílá český název
`AI novinky – 26. 10. 2026`; služba k němu připojí `.md` (API nemá samostatné pole `title`,
jen `filename`, a `.md` doplňuje samo). Popis (`og:description`) je první odstavec přehledu.

## Publikace dne na docs-md.com (od 5. 10. 2026)

- `scripts/daily.sh --publish` po vygenerování slepí den do jednoho postu a nahraje ho na
  **docs-md.com** (anonymně, bez účtu; od 13. 11. 2026 přes MCP a agent key — viz níže).
- Slepování dělá `scripts/build-prehled.py`: z `rd/<datum>`/`hn/<datum>` vezme **jen články**
  (ne přílohu ani metodiku), v pořadí z indexu, a zapíše `<složka>/prehled.md` (titulek + obsah +
  sekce `##` s plnými články). `prehled.md` je v `.gitignore` (generuje se znovu).
- Nahrává `scripts/publish-docs.py` (od 13. 11. 2026 přes MCP, viz další sekci);
  URL + edit token ukládá do `logs/publish.json` (gitignored). Limit je **120 000 znaků** na share
  (den má ~35–80 tisíc).
- **Obsah je klikací** – `## Obsah` odkazuje na kotvy nadpisů; `slugify()` v `build-prehled.py`
  napodobuje tvorbu kotev Docs MD (malá písmena, pryč interpunkce, mezery na pomlčky, diakritika
  zůstává). Ověřeno klikem (odskočí na článek).
- Opakované publikace téhož dne **aktualizují stejnou URL** (`update_share` s agent key, u starších
  dokumentů s edit tokenem), nezakládají novou.
- `scripts/build-linkedin.py` vygeneruje **opakovatelný příspěvek na LinkedIn**: jedna úvodní věta,
  pak **10 nejlepších témat podle skóre** (z tabulky v `00-index.md`, 5 z každého zdroje, střídavě)
  s prefixem `RD:` / `HN:`, a nakonec odkazy z `logs/publish.json`. Bez hashtagů.
  Spuštění `python3 scripts/build-linkedin.py` (bez argumentů vezme poslední publikovaný den pro
  každý zdroj). S `--den <datum>` bere sloučená témata (`dny/<datum>/temata.json`), označí je
  `RD:`, `HN:` nebo `RD+HN:` a dá do příspěvku jeden odkaz na `dny/<datum>`.
- Publikuje se **per den a per zdroj** (rd a hn zvlášť) při ručním `daily.sh --publish`;
  `--hn --publish` publikuje HN den. `prehledy.sh` publikuje jeden sloučený den za oba zdroje.
- **Proč ne yeet.md:** vykresluje Markdown správně, ale jeho webový font (DM Sans bez latin-ext
  subsetu) nemá českou diakritiku, takže prohlížeč pro `ě ř ž á í` přepne na Arial a znaky mají
  jinou velikost. Přebít `<style>` nešlo (yeet má silnější pravidlo). Docs MD (Geist) češtinu
  vykresluje správně. `<details>` na yeet nefunguje ani v Markdownu.
- Ostatní bezúčtové služby: rentry.co (200 k, navždy, API vratké), telegra.ph (64 KB, nebere
  Markdown), JotBird (anonym 30 dní).

## Web na GitHub Pages (od 15. 11. 2026)

Denní přehled už nepublikuje `publish-docs.py` na docs-md.com, ale je z něj
**statický web na GitHub Pages**: `https://ai-novinky.localinference.cz/`
(do 16. 11. 2026 `https://rozumvhrsti.github.io/reddit-prehled/`).

- **Proč.** Docs MD dalo novému klíči trust `new`, a ten má u „link postu“ strop
  **7 dní** (viz níže) — denní odkaz tedy umřel dřív, než přišlo `established`.
  Navíc 13. 11. zrušilo REST API a publikace spadla. Vlastní web má trvalé
  odkazy, klikatelné linky, indexování i vlastní vzhled a nic z toho nezávisí
  na cizí politice.
- **Jedno repo, veřejné** (od 16. 11. 2026): `Staticke-weby/ai-novinky.LOCALinference.cz`
  drží skripty, články, `dny/` i vygenerovaný `docs/`; Pages jedou v režimu
  „GitHub Actions“ a `docs/` nahrává `.github/workflows/pages.yml`. Dřív to byla
  dvě repa (privátní pipeline + veřejný web přes `push-site.sh` a clone v `/tmp`);
  `push-site.sh` teď jen commitne `docs/` a `dny/` a pushne. Stažené podklady
  (`_data/`: dumpy, plné texty cizích článků, obrázky, překlady) jsou v `.gitignore`
  a v repu nejsou — do veřejného repa nepatří a jsou k ničemu, dají se stáhnout znovu.
- **Historie začíná 16. 11. 2026.** Do nového repa šel jeden úvodní commit aktuálního
  stromu, ne stará historie (ta by s sebou nesla právě ta `_data/` a 59 MB blobů).
  Stará historie zůstává v privátním `petrbaloun/reddit-clanky-ai`.
- **Jeden commit na konci (od 19. 11. 2026).** `prehledy.sh` už nepushuje po každém
  zdroji: oba `daily.sh` běží bez `--push` a na konci `push-day.sh <datum>` commitne
  články z `rd/` i `hn/`, `dny/` a `docs/` jedním commitem a pushne. Dřív šly na main
  tři pushe během pár minut (Reddit, HN, web), každý spustil deploy Pages a poslední
  padal na `Deployment request failed … due to in progress deployment` — i s
  `cancel-in-progress` zůstává předchozí deploy chvíli viset. Když jeden zdroj selže,
  skript pokračuje s tím, co je, a commitne i částečný den.
- **Generuje `scripts/build-site.py`** z `dny/*/prehled.md`: `<datum>.html`,
  `index.html` (archiv), `feed.xml`, `style.css`, `.nojekyll`. Bere **celý
  archiv**, takže staré dny se publikují zpětně — 15. 11. tak vyšlo 27 dní.
- **Markdown se nepřekládá obecně**, jen to, co `build-denni.py` produkuje
  (H1/H2, odrážky, `**tučně**`, odkazy, `---`). `__tučně__` se záměrně
  nepodporuje: v textech jsou jména jako `u/__ThrowAway__123`.
- **Kotvy** se berou z odkazů v `## Obsah`, ne dopočtem — klikací obsah tak sedí
  i tam, kde by se `slugify()` rozešel. Nadpis `## Obsah` musí dostat `id="obsah"`,
  jinak se na něj nevztahuje CSS.
- **Odkazy v obsahu musí vypadat jako odkazy.** Když se jim zrušilo podtržení
  a dostaly barvu textu (aby 36 položek nebylo přeplácané), čtenář je považoval
  za mrtvý text („obsah nemá funkční odkazy"). Správně: barva odkazu
  (`--accent`), podtržení až při hoveru. Kotvy samotné fungovaly — ověřeno
  klikem, `scrollY` i `#kotva` v URL.
- **Název webu je „AI novinky"** (`SITE_NAME` v `build-site.py`) a používá se všude:
  `<title>`, `og:title`, `og:site_name`, `og:image:alt`, RSS (`feed.xml`), manifest,
  patička, H1 úvodu a popisek v og obrázku. Denní stránky mají název
  `AI novinky – 14. 11. 2026` (H1 v `dny/<datum>/prehled.md` skládá `build-denni.py`),
  takže meta i sdílení sedí s hlavičkou. Starší dny se přejmenovaly v markdownu,
  web se pak jen přegeneroval (`build-site.py` staví celý archiv z `dny/`).
  Docs MD (share na LinkedIn) posílá stejný název přes `publish-docs.py`
  (`display_name()` → `AI novinky – 14. 11. 2026.md`).
- **Název webu v hlavičce je odkaz na úvod** a jmenuje se „AI novinky" (`SITE_BRAND`);
  má barvu odkazu a je tučnější (`header.site .brand`). Denní stránky mají v hlavičce
  navíc `← Archiv`. Vpravo je odkaz na `LOCALinference.cz` (`.parent`, `margin-left: auto`),
  hlavička má `flex-wrap`, aby se na mobilu zalomila.
- **Cache na GitHub Pages.** `style.css` se drží ~10 minut, takže se změna CSS
  po pushi neprojeví. Proto `build-site.py` přidává do HTML
  `style.css?v=<md5 obsahu>` — každá změna CSS má novou URL.
- **Odkaz v LinkedIn** bere `build-linkedin.py` z `build-site.py`
  (`site_url(date)`), ne z `logs/publish.json`. Ten zůstává jen pro staré
  per-source dny (`rd/…`, `hn/…`).
- **Archiv je kalendář po měsících** (`write_index`): mřížka karet, v kartě velké
  datum „14. 11." a pod ním „pá · 36 novinek", měsíc je nadpis sekce s počtem dní.
  Datum je to hlavní; dřív byl den utopený v řádku „36 témat z 36 článků".
- **Barvy jsou z `www.localinference.cz`** (Starlight): akcent `#187a63` ve světlém
  a `#35b48f` v tmavém režimu, neutrální `#23262f`/`#edeef3` (text), `#edeef3`/`#353841`
  (linky), `#f6f7f9`/`#23262f` (karty). Stejné konstanty (`OG_*`) kreslí i og:image,
  aby náhled pro sdílení ladil s webem.
- **Favicon** kreslí `build-site.py` (`write_icons`): zelený čtverec s bílým „A"
  z tahů (ne z fontu, ať je stejné ve všech velikostech) — `favicon.svg`, PNG 16/32,
  `apple-touch-icon.png` (bez zaoblení, iOS si masku dělá sám), `favicon.ico`
  a `site.webmanifest` s `theme-color` `#187a63`.
- **Písmo je Geist** (self-hosted `assets/fonts/*.woff2`, latin + latin-ext kvůli
  diakritice, licence v `assets/fonts/OFL.txt`), stejné jako na docs-md.com — čte se
  líp než systémové. `build-site.py` ho kopíruje do `docs/fonts/`; og:image zůstává
  na Interu, protože Pillow neumí woff2.
- **Obsah je sbalený** (`<details class="obsah">`) — rozbalí si ho jen kdo chce;
  pod každou anotací je `<details class="full">+ Číst dál</details>` s naším
  plným textem z `rd/`/`hn/`. Odstavce, které už jsou v anotaci, se přeskočí.
- **Bez cache.** GitHub Pages posílá `cache-control: max-age=600` na všechno a hlavičky
  nastavit nejdou, takže po nasazení mohl web 10 minut ukazovat starou verzi.
  `build-site.py` proto generuje `docs/sw.js`: service worker jede network-first
  (`fetch(..., {cache: "no-store"})`), do Cache API ukládá jen kopii pro offline.
  Cache má jméno podle buildu, takže nové nasazení starou zahodí; registrace
  (`updateViaCache: "none"`) je v `PAGE`, takže se SW aktualizuje hned.
  `style.css?v=<md5>` zůstává jako druhá pojistka. SW platí per origin — na
  `staticke-weby.github.io` a na vlastní doméně jsou dva oddělené.
- **Měření návštěvnosti** je Umami (`navstevnost.pikapod.net`, skript s `data-website-id`
  vkládá `PAGE` v `build-site.py`, takže ho mají všechny stránky včetně archivu).
  Cookie to nepoužívá, do feedu se nepropisuje.
- **Náhled pro sdílení (og:image)** kreslí `build-site.py` přes Pillow: `docs/og.png`
  pro archiv a `docs/og/<datum>.png` pro každý den (1200×630, Inter, stejné barvy
  jako web, 3 první titulky dne). Bez Pillow se obrázky vynechají a meta značky
  se negenerují, build nespadne. Twitter kartu přepíná na `summary_large_image`.
- **Sitemap a robots.txt** píše `build-site.py` při každém buildu (`write_sitemap`,
  `write_robots`): `docs/sitemap.xml` má úvod + všechny denní stránky s `lastmod`
  z data dne, `docs/robots.txt` na něj odkazuje. Drží se samo s archivem, ručně
  se neupravuje. V `<head>` je i `<link rel="sitemap">`.
- **Vlastní doména.** Při publikaci přes Actions se `docs/CNAME` **ignoruje**; doména
  se zadává v Settings → Pages → Custom domain. `build-site.py` CNAME dál píše (kdyby
  se přešlo na deploy z větve). V Cloudflare je potřeba `CNAME ai-novinky →
  staticke-weby.github.io` **bez proxy** (šedý mrak) — s oranžovým mrakem GitHub
  nevydá certifikát. HTTPS pak zapnout v nastavení Pages.
- **Když deploy Pages spadne na artefakt, neopakovat `run rerun --failed`.** 22. 11. 2026
  `actions/deploy-pages` v runu nenašel `github-pages` („Found 0 artifact(s)“), i když upload
  hlásil success — výpadek na straně GitHubu, ne chyba pipeline. Rerun ale artefakt nahraje
  **znovu**, takže další běh spadne na „Multiple artifacts named github-pages were unexpectedly
  found“ a je z toho slepá ulička. Správně: `gh api …/actions/runs/<id>/artifacts` vypsat,
  staré artefakty smazat (`gh api -X DELETE …/actions/artifacts/<id>`) a pustit **nový běh**
  `gh workflow run pages.yml --ref main`. Ověřit `curl -o /dev/null -w '%{http_code}' <den>.html`.
  Neúspěšný deploy předchozí verzi neshodí, web tedy mezitím běží dál.
  **23. 11. 2026 se to zopakovalo** (den 22. 11.): `deploy` hlásil „Found 0 artifact(s)“,
  i když `upload` uspěl a artefakt `github-pages` v runu nakonec ležel (5,1 MB). Stejný
  postup zabral: artefakt smazat, `gh workflow run pages.yml --ref main`, nový běh
  do minuty zelený a `2026-11-22.html` vrací 200. Rerun nepoužívat ani tady.
- **Viditelnost repa nejde přepnout z `gh`**: účet `rozumvhrsti` má na
  `petrbaloun/reddit-clanky-ai` jen push (admin: false). Proto nové repo v organizaci
  `Staticke-weby`.

## Docs MD přes MCP (13. 11. 2026 – 15. 11. 2026, nahrazeno webem)

Docs MD 13. 11. 2026 **zrušil REST API** (`POST /api/share` i `PATCH /api/share/<id>` vrací
`410 Gone`) a přijímá dokumenty **jen jako MCP tool calls s agent key**. Publikace 13. 11. proto
napoprvé selhala („publikace denního přehledu selhala (pokračuji)") a LinkedIn příspěvek vyšel
s `(nepublikováno)`. `scripts/publish-docs.py` je přepsaný na MCP.

- **Endpoint a volání.** `https://docs-md.com/mcp`, stateless — žádný `initialize` ani session.
  Jeden `POST` = jeden JSON-RPC `tools/call`; `Accept` musí obsahovat **oba** typy
  `application/json, text/event-stream` (jinak 406). Odpověď je jeden server-sent event,
  takže se čte řádek `data: {…}` a z něj `result.structuredContent`; odmítnutí je normální
  výsledek s `result.isError: true` a textem `error: <kód>`.
- **Klíč agenta.** Jednou `register_agent` (`name`, `description`, `client`), vrácený `agent_key`
  (`dmk_…`, ukáže se jen jednou) ukládá skript do `logs/docs-md-agent.json` (gitignored,
  `chmod 600`). Agent se jmenuje `reddit-ai-denni-prehled`. Když soubor chybí, skript zaregistruje
  nového agenta — pozor, tím vznikne nová identita a staré dokumenty pod ní nebudou updatovatelné.
- **Staré dokumenty** (před 13. 11.) nemají vlastníka, ale jejich `edit_token` z `logs/publish.json`
  pořád pro `update_share` funguje. Nové dokumenty mají místo tokenu vlastníka: `update_share`
  s `agent_key`; `expiry` se u `update_share` měnit nedá.
- **Trust `new` (co dostane nový klíč).** Max. **30 dní** životnosti, max. 10 dokumentů denně,
  odkazy v dokumentu **neklikatelné** (plain text), stránka se **neindexuje**. Navíc když je
  dokument „link post" (má odkazy a žádnou tabulku/kód/task list — což je náš den s anotacemi),
  strop je jen **7 dní**. `established` (trvalé `never` + klikatelné odkazy) přijde po **14 dnech
  a 5 dokumentech ve 3 různých dnech**, takže ~28. 11.
- **Důsledek:** denní odkazy zatím nejsou trvalé. 13. 11. vyšel jako link post na **7 dní**
  (do 21. 11.), což je dřív než `established` (~28. 11.) — dnešní odkaz tedy vyprší dřív, než
  půjde publikovat trvale. **Rozhodnutí 14. 11.: den nechat být** (nepřepublikovávat na novou URL),
  tabulku do přehledu kvůli 30 dnům nepřidávat. Až bude klíč `established`, je potřeba rozhodnout,
  jak dál — nový `share_markdown` = nová URL, `update_share` expiraci neprodlouží. Buď se staré dny
  publikují znovu (a odkazy v už vydaných LinkedIn příspěvcích přestanou platit), nebo se přejde
  na službu s trvalými odkazy.
- **Ověření klíče:** `whoami` s `agent_key` vrátí `trust`, `posts_today`, `live_shares` a
  `limits.max_expiry`; skript z něj bere expiraci pro `share_markdown`. Čtení dokumentu klíč
  nepotřebuje: `https://docs-md.com/<id>.md`.
- **Dokumenty z doby před 13. 11.** zůstávají online, ale odkazy v nich jsou nově plain text
  a nejsou indexované.

## Reddit přímo z webu (od 10. 10. 2026)

Arctic Shift 10. 10. opakovaně padal (522/523/000; dle správce krátkodobě, ale
nedostupné), PullPush zavřel free programatický přístup (429), dev.to i další
alternativy mají málo obsahu/komentářů a placená API se nepoužívají. Proto sběr
Redditu jede **přímo z webu přes prohlížeč OpenChamber**.

- **`scripts/rd-collect-web.py`** (nahradil v `daily.sh` archivní `rd-collect.py`):
  - vezme **reddit cookies z profilu prohlížeče OpenChamber**
    (`~/.config/OpenChamber/Partitions/openchamber-browser/Cookies`, read-only) a
    s nimi posílá `urllib` požadavky. Bez cookies vrací Reddit **403**, s nimi 200
    a plné JSON (`/r/<sub>/new.json`, `/comments/<id>.json`). Ověřeno: curl/headless
    Chrome dostanou 403/„blocked", opravdový prohlížeč i tyto cookies projdou.
  - Díky tomu má **skóre i počty komentářů** strukturovaně (jako Arctic Shift),
    a to **živě**. Netřeba otevřený prohlížeč, stačí profil s platnou session.
  - **Výchozí posun je 1 den zpět** (včerejšek), ne 3 dny — live data, žádné
    dozrávání. Ověřeno na 2026-10-09: 1012 postů, 40 balíčků s komentáři, ~68 s.
- **`api.reddit.com` místo `www.reddit.com/….json` (od 4. 11. 2026).** Reddit začal vracet
  na `www.reddit.com/r/<sub>/new.json` i `old.reddit.com` **403 „You've been blocked by network
  security“** — a to i s platnými cookies a i v opravdovém prohlížeči. Stejné cookies ale
  `https://api.reddit.com/r/<sub>/new` a `https://api.reddit.com/comments/<id>` berou (200, plné
  JSON). `rd-collect-web.py` proto staví URL z konstanty `RAPI = "https://api.reddit.com"`.
  Když sběr hlásí 403, ověř to nejdřív na `api.reddit.com`, než začneš obnovovat session.
- **Ověření session bez čekání na běh:** jeden request na
  `https://api.reddit.com/r/LocalLLaMA/new?limit=1` s cookies z DB; 200 = session žije,
  403 = vypršela/revokovaná (obnovit v prohlížeči).
- **Rate limit Redditu: 100 requestů / ~600 s** (`x-ratelimit-remaining` = 100,
  `reset` ≈ 534 s). Denní běh (~60–80 requestů) se vejde do jednoho okna.
  `rd-collect-web.py` má adaptivní limitér (`_pace`) + backoff na 429; při
  vyčerpání počká do resetu. Hluboký sběr (více dní zpět) rozpočet přesáhne.
- **Pojistka:** `rd-collect-web.py` skončí nenulově při málo postech (< `MIN_POSTS`)
  nebo bez cookies; `daily.sh` den přeskočí. (Stejný princip jako u archivu.)
- **Správa cookies:** skript si cookies přečte z prohlížeče při každém běhu a navíc si drží
  `logs/reddit-cookies.txt` (gitignored), kam ukládá `Set-Cookie` z odpovědí (např. `session_tracker`).
  `token_v2` Reddit v odpovědích neposílá, takže **ten se sám neobnoví** – když vyprší, musí se
  session obnovit v prohlížeči (OpenChamber). Vypršenou session hlásí kód **5** (a `daily.sh` vypíše
  „otevři reddit v prohlížeči"). Bez credentials nebo schváleného API to plně automaticky nejde.
- `scripts/rd-collect.py` (Arctic Shift) zůstává v repu jako záložní varianta.

## Reddit přes Arctic Shift (od 5. 10. 2026, nyní záložní)

- `scripts/daily.sh` (bez `--hn`) -> `rd/<datum>/`, **výchozí 3 dny zpět** (data sednutá).
- **Sběr dělá `scripts/rd-collect.py`**: `posts/search` pro 19 subredditů, komentáře přes
  `comments/tree`, externí články; celý den ~30 s (dřív ~12 min přes prohlížeč). Zapíše
  `_data/bundles/`, `candidates.json`, `appendix.json`, `dataset.json`.
- `prompt-souhrn.md` je od teď **bez sběru** – agent jen plánuje, píše (souhrn-writer) a staví index.
- Ověřeno na 2026-10-02: 26 článků, 448 postů v příloze, **~5,5 min / 15 tahů**.
- **Pojistka proti výpadku archivu:** `rd-collect.py` nejdřív udělá rychlý *health-check*
  (jeden dotaz na Arctic Shift, timeout 15 s); když archiv neodpovídá, skončí hned s kódem 1.
  Stejně skončí, když nasbírá méně než `MIN_POSTS` (5) postů. `daily.sh` pak den **přeskočí** —
  agent se vůbec nespustí, takže nevznikne prázdný/rozbitý souhrn. (10. 10. 2026 byl Arctic
  Shift mimo provoz s 522/523/000; dřív by se pustil agent na prázdná data.)

## Hacker News (od 5. 10. 2026)

Druhý, samostatný souhrn: `scripts/daily.sh --hn` -> `hn/<YYYY-MM-DD>/`, jen AI/tech témata.

- **Sběr dělá skript, ne agent.** `scripts/hn-collect.py <datum>` používá veřejné HN API
  (Algolia `search_by_date`, okno Europe/Prague), takže **není potřeba prohlížeč** a nic
  neblokuje. Zapíše `_data/bundles/<id>.md`, `candidates.json`, `appendix.json`, `dataset.json`.
- **Kandidáti se řadí podle AI/tech termínů** v titulku/URL (`AI_TERMS` v collect skriptu) a pak
  podle skóre; do balíčků jde 45 nejlepších se skóre ≥20 a ≥10 komentáři. Externí článek se tahá
  rovnou (heuristika na `<article>`/`<main>`), co je za paywallem, agent případně dočte přes `webfetch`.
- **HN nezveřejňuje skóre komentářů** – v balíčku je místo něj `-` a pisatele se to týká jen v tom,
  že skóre nezmiňuje. Pořadí komentářů = řazení HN.
- **Reuse agentů:** píše `souhrn-writer` (má sekci pro `subreddit: Hacker News` – jiný řádek metadat),
  titulky překládá `cz-translator`. Prompt je `scripts/prompt-hn.md`.
- Commit prefix je `souhrn HN`. Cíl ~15–25 článků; běh 2026-10-04 dal 16 článků za ~5,5 min.
- Bez `--hn` běží Reddit (`rd/<datum>/`, výchozí 3 dny zpět).

## Poznote (4.–5. 10. 2026, zrušeno)

Krátce se souhrny nahrávaly i do self-hosted Poznote (`scripts/poznote-upload.*`),
ale Poznote bylo zrušeno a integrace odstraněna. Souhrny zůstávají jen v tomto
repu.
