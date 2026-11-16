# 1wkpxn6

**Von: open-source model s 395 miliony parametrů chce nahradit Jev. Nezávislý test ale ukázal, že Jev vede**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/wFXx |
| Publikováno (Europe/Prague) | 19. 9. 2026, 18:00 |
| Skóre / komentáře | 197 / 85 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1wkpxn6/von_opensource_395m_system_one_model/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wkpxn6/von_opensource_395m_system_one_model/ |

## Co se stalo

Uživatel u/wFXx oznámil na r/LocalLLaMA model **Von** — open-source model typu „System One“ s **395 miliony parametrů**, který má být **přímou náhradou (drop-in replacement) za JEV** od TypeSafe. Podle autora běží **zcela na CPU s 1–2 GB paměti**, odpovídá za **25–300 ms** a „překonává JEV ve všech benchmarcích“. Odkazy vedou na GitHub (`wfzyx/von`) a Hugging Face (`wfzyx/von-1.0`); v popisu jsou tři rozhodovací primitiva **Choice** (kategorická volba), **Noul** (binární pravděpodobnost) a **Score** (ordinální hodnocení) a kompatibilita s protokolem `/v1/systemone`.

Nadšení ale narazilo na **komunitní testování**. Jeden z komentujících zveřejnil vlastní syntetický test: **Jev 97,4 %, Von 92,3 %** (po opravě na verzi 1.0.1; před ní 65,4 %) a GLiNER2 79,5 %. Autor uznal, že kvalita prvních checkpointů pokulhávala, část problému podle něj způsobila chyba v Python kódu, přejmenoval balíček na `von-sdk` kvůli obsazenému jménu na PyPI a přislíbil nové checkpointy. Řada komentujících zároveň tvrdí, že jde o **běžný klasifikátor na bázi BERT**, jen s lepším obalem a marketingem.

## Klíčová fakta

- **Model:** Von, 395 M parametrů, nerekurzivní (non-autoregressive) obousměrný model, licence Apache-2.0.
- **Cíl:** přímá náhrada za TypeSafe JEV, kompatibilita s protokolem `/v1/systemone`.
- **Provoz:** CPU, 1–2 GB paměti, uváděná odezva 25–300 ms (v popisu repozitáře sub-15 až sub-25 ms).
- **Primitiva:** Choice (kategorická), Noul (binární), Score (ordinální); více otázek najednou přes `von.system_one`.
- **Instalace:** `pip install von-sdk` nebo `bun add von-sdk`, server přes `von serve` na portu 8000.
- **Benchmarky z repozitáře:** Von 1.1 dosahuje 72,0 % makro skóre v2 proti 96,6 % u Jevu, ale vede na ViZDoom (9,00 zabití proti 5,62).
- **Nezávislý test v komentářích:** Jev 97,4 %, Von 92,3 %, GLiNER2 79,5 %.
- **Trénink:** ~250 000 vyvážených příkladů, resp. korpus ~290 000 příkladů; RLCD a teplotní škálování.
- **Reakce autora:** uznání mezery, oprava chyby v kódu, přejmenování balíčku, příslib nových checkpointů.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Parametry | 395 M |
| Velikost modelu (v závorce) | 1,5 GB |
| Paměť při běhu na CPU | 1–2 GB |
| Uváděná odezva | 25–300 ms |
| Latence na GPU (repozitář) | ~18 ms |
| Latence Jev API (komentář) | ~115 ms |
| Latence LLM (komentář) | 500–2 000 ms |
| Makro skóre v2: Von 1.1 / Jev | 72,0 % / 96,6 % |
| Choice makro: Von / Jev | 83,0 % / 96,8 % |
| ViZDoom zabití: Von / Jev | 9,00 / 5,62 |
| Syntetický test: Von / Jev / GLiNER2 | 92,3 % / 97,4 % / 79,5 % |
| Tréninkové příklady | ~250 000 |
| Tréninkový korpus | ~290 000 |
| Skóre / komentáře postu | 197 / 85 |
| Komentářů v balíčku | 28 |

## Citace

> „Von: open-source ‚System One‘ přímá náhrada za JEV od TypeSafe.“ (překlad) — u/wFXx, vlastní text postu

> „Běží zcela na CPU s 1–2 GB paměti (optimalizaci jsem zatím moc času nevěnoval), odpovídá v 25–300 ms a překonává JEV ve všech benchmarcích. Užijte si to!“ (překlad) — u/wFXx

> „P.S. Jsem otevřený nabídkám pracovat v AI výzkumných laboratořích. Klidně mi napište, pokud nějakou máte.“ (překlad) — u/wFXx

> „Von implementuje výpočetní paradigma System One: reflexivní, paralelní, deterministické a statisticky kalibrované rozhodování.“ (překlad) — popis repozitáře

> „Von dosahuje 9,00 průměrných zabití v Defend the Center, čímž překonává proprietární Jev 1.13 od TypeSafe (+60,1 % více zabití) a všechny open modely, a to při lokální inferenci s latencí pod 18 ms.“ (překlad) — popis repozitáře

> „Takže TypeSafe potřeboval dva roky výzkumu a dobře financovaný tým, aby postavil Jev, a najednou jsou tu všechny ty ‚drop-in‘ náhrady za pár dní a údajně ho překonávají… Určitě to nebude tak snadné? Co mi uniká?“ (překlad) — u/glitchsir

> „Když čtu, že nějaká nová drop-in náhrada vyvinutá za pár dní tvrdí, že v benchmarcích překonává Jev, jsem víc než skeptický.“ (překlad) — u/Fluxx1001

> „Taky jsem předpokládal, že Jev je větší model s lepším tréninkem, ale není neuvěřitelné, že je to vlastně jen poměrně obyčejný BERT s hezčím DX a velkým marketingovým rozpočtem…“ (překlad) — u/look

> „Někteří kolegové z Redditu hlásili, že kvalita modelu není tak vysoko, od té doby jsem vydal nový checkpoint, který je Jevu obecně mnohem blíž.“ (překlad) — u/wFXx

## Co říkají komentáře

Vlákno je převážně **skeptické**. První námitka je časová: TypeSafe prý na Jevu pracoval dva roky s dobře financovaným týmem, takže tvrzení, že ho někdo překoná za pár dní, budí nedůvěru. Druhá námitka je **technická**: podle části diskutujících jde o běžný klasifikátor na bázi BERT s lepším obalem, nikoli o novou technologii — a takový typ modelu existuje déle než LLM. Třetí, nejkonkrétnější, je **nezávislý test**, ve kterém Jev vede (97,4 % vs. 92,3 %). Na druhé straně autor otevřeně přiznává mezery, opravil chybu v kódu a slíbil nové checkpointy, což část diskuse oceňuje; objevují se i praktické stížnosti na instalaci a na obsazené jméno balíčku na PyPI.

## Rozpory a neověřené informace

- **Neshoda:** autor tvrdí, že Von překonává JEV ve všech benchmarcích, ale jeho vlastní tabulka ukazuje Jev vpředu v makro skóre v2 (96,6 % vs. 72,0 %), zatímco Von vede jen ve ViZDoom (9,00 vs. 5,62 zabití); komentující se přou, který benchmark je pro praxi relevantní.
- **Neshoda:** nezávislý syntetický test (u/look) dává Jevu 97,4 % a Vonu 92,3 %, tedy opak autorova tvrzení.
- **Neshoda:** část diskuse považuje Jev za výsledek dvou let výzkumu, jiní za obyčejný BERT s marketingem.
- **Neověřené tvrzení:** autorovo „překonává JEV ve všech benchmarcích“ — vyvráceno testy komentujících.
- **Neověřená tvrzení z repozitáře:** 91,23% přesnost na adversariálních vícekrokových úlohách, +60,1 % zabití ve ViZDoom a latence pod 18 ms.
- **Neověřené tvrzení:** autor uvádí, že dokončil jen 1 z 6 tréninkových epoch, takže přesnost může ještě růst.

## Proč to je důležité

Případ je poučný ze dvou důvodů. Za prvé ukazuje **zdravý mechanismus ověřování**: tvrzení o překonání etablovaného modelu bylo během hodin podrobeno nezávislému testu, který ho nepotvrdil — a autor na to reagoval opravou a novými checkpointy místo přehnaných tvrzení. Za druhé odhaluje, že v kategorii „rozhodovacích“ modelů je **hranice mezi inovací a obalem tenká**: jde o architekturu, která existuje roky, a konkurenční výhoda často spočívá v balení, protokolu a latenci. Právě proto je pro uživatele podstatnější měřit na vlastních datech než věřit benchmarkům z repozitáře.

## Zdroje

- https://github.com/wfzyx/von
- https://huggingface.co/wfzyx/von-1.0
- https://www.reddit.com/r/LocalLLaMA/comments/1wkpxn6/von_opensource_395m_system_one_model/
- komentáře: `2026-09-19/_data/raw/comments.json` (klíč `1wkpxn6`), balíček `2026-09-19/_data/bundles/1wkpxn6.md`
