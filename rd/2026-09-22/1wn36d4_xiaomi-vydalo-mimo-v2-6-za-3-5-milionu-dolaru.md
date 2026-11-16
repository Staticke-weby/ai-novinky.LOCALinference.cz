# 1wn36d4

**Xiaomi vydalo a otevřelo sérii MiMo-V2.6: RL trénink stál 3,5 milionu dolarů a Pro skóruje 46,32 v indexu Artificial Analysis**

| | |
|---|---|
| Subreddit | r/MachineLearning |
| Autor | u/we_are_mammals |
| Publikováno (Europe/Prague) | 22. 9. 2026, 09:56 |
| Skóre / komentáře | 66 / 17 |
| Odkaz | https://mimo.xiaomi.com/mimo-v2-6 |
| Diskuse | https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/ |

## Co se stalo

Xiaomi 22. 9. 2026 vydalo a **otevřelo** sérii **MiMo-V2.6**, kterou tvoří nativně omnimodální modely **MiMo-V2.6-Pro** a **MiMo-V2.6-Flash** a varianta **MiMo-V2.6-Pro-UltraSpeed**. Oznámení nese heslo „Frontier intelligence, all the modalities, built in public.“ a rámuje vydání jako krok k prozkoumání cesty k samovylepšujícím se systémům (RSI) pomocí škálování RL výpočtu na ověřitelných a složitých úlohách. Podle Xiaomi skóruje MiMo-V2.6-Pro **46,32** v indexu Artificial Analysis Intelligence Index, což z něj podle výrobce dělá nejsilnější otevřený model k datu vydání — před Kimi K3 a Qwen3.8 Max. Autor příspěvku zdůraznil, že **celkové náklady RL tréninku byly 3,5 milionu dolarů** a že model má živý „benchmaxxing“ dashboard.

## Klíčová fakta

- **Vydané modely:** MiMo-V2.6-Pro, MiMo-V2.6-Flash a MiMo-V2.6-Pro-UltraSpeed (UltraSpeed běží až **20× rychleji** než Pro).
- **Skóre:** MiMo-V2.6-Pro 46,32 v Artificial Analysis Intelligence Index v4.3 (září 2026) — podle Xiaomi nejvyšší mezi otevřenými modely.
- **RL běh:** 30 kroků, zhruba **750 000 trajektorií**, necelých šest dní; náklady přibližně **0,85 mil. $** (Flash) a **2,62 mil. $** (Pro), celkem tedy 3,5 mil. $ podle textu postu.
- **Zlepšení na benchmarcích:** DeepSWE v1.1 u Flash z 48,8 na 65,68 (asi 17 bodů), u Pro z 58,4 na 72,57 (asi 14 bodů).
- **Konečné hodnoty v kroku 30:** DeepSWE v1.1 72,6 (Pro) / 65,7 (Flash); AutomationBench v1.0.6 55 (Pro) / 52,7 (Flash); MiMo Visual Coding 74,9 (Pro) / 72,9 (Flash).
- **Ceny API** za milion tokenů zůstávají stejné jako u V2.5: Flash 0,0028 $ / 0,14 $ / 0,28 $; Pro 0,0036 $ / 0,435 $ / 0,87 $; Pro-UltraSpeed 0,036 $ / 4,35 $ / 8,7 $ (cache hit / cache miss / výstup).
- **Konfigurace RL:** 1 568 vzorků na update, kontext až 1 milion tokenů, 3,5–3,7 mld. tokenů na krok; předtrénink na 48 bilionech tokenů (Flash) a 30 bilionech (Pro) podle autora postu, který cituje technickou zprávu.
- **Matematika:** MiMo-V2.6-Pro dokončil formalizaci hlavní věty práce Li a Yorkeho „Period Three Implies Chaos“ v Lean 4 — přes 6 000 řádků ověřených jádrem Leanu.
- Aplikace **MiMo Desktop** opouští early access a přichází s oběma modely vestavěnými.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Skóre MiMo-V2.6-Pro (AA Intelligence Index) | 46,32 |
| Celkové náklady RL tréninku (podle postu) | 3,5 mil. $ |
| Náklady RL u Flash / Pro | 0,85 mil. $ / 2,62 mil. $ |
| RL kroků u každého modelu | 30 |
| Trajektorií v RL běhu | ~750 000 |
| Délka RL běhu | necelých 6 dní |
| Zrychlení UltraSpeed proti Pro | až 20× |
| Ověřené řádky v Lean 4 | přes 6 000 |
| Skóre příspěvku / komentářů | 66 / 17 |

## Citace

> „Frontier intelligence, all the modalities, built in public.“ (překlad) — Xiaomi

> „MiMo-V2.6-Pro skóruje 46,32 v Artificial Analysis Intelligence Index a překonává Kimi K3 a Qwen3.8 Max, čímž se stává nejsilnějším otevřeným modelem k dnešnímu dni.“ (překlad) — Xiaomi

> „RL se ukázal jako vzorkově efektivní, zlepšoval se po celou dobu běhu a zobecňoval nad rámec trénovací distribuce.“ (překlad) — Xiaomi

> „Celkové náklady RL tréninku byly 3,5 milionu dolarů.“ (překlad) — u/we_are_mammals, vlastní text postu

> „Post-trénink byl 3,5 milionu. Nebere v potaz pre- a mid-training…“ (překlad) — u/Salt-Bodybuilder-518, nejlépe hodnocený komentář (40 bodů)

> „Spálili skoro 2,5 milionu jen na třicet kroků u verze Pro.“ (překlad) — u/ummitluyum

> „Mám rád reporty, kde se předtrénink na desítkách bilionů tokenů zamete stranou, aby se mohli chlubit haléři utracenými za fine-tuning.“ (překlad) — u/ummitluyum

> „S kontextem milion tokenů a modelem o velikosti kolem 180 GB je lokální běh bez clusteru čtyř karet H200 tak jako tak mimo hru.“ (překlad) — u/ummitluyum

## Co říkají komentáře

Diskuse se soustředí na **výklad čísla 3,5 milionu dolarů**. Nejlépe hodnocený komentář upozorňuje, že jde jen o post-trénink, a autor postu ho akceptoval („Upraveno, díky!“). Několik komentujících kritizuje, že se v oznámení zamlčuje předtrénink — autor sám extrapoluje jeho náklady na zhruba **2 miliardy dolarů** a poznamenává, že toto číslo v oznámení chybí, možná z politických důvodů. Druhé téma je **praktická dostupnost**: podle jednoho komentáře je na lokální běh potřeba cluster čtyř H200, což jiný komentující rozporuje („H200 má 141 GB, 2× H200 je 282 GB, to stačí na model i kontext“). Třetí téma je riziko **přeučení**: autor postu upozorňuje, že pokud se skóre na benchmarcích zvedají i poté, co bylo RL zastaveno, může jít o výrazný překryv trénovacích úloh s benchmarky.

## Rozpory a neověřené informace

- **Nesoulad ve výkladu nákladů:** text postu mluví o „celkových nákladech RL tréninku 3,5 mil. $“, komentující u/Salt-Bodybuilder-518 upřesňuje, že jde pouze o post-trénink bez pre- a mid-training; autor to uznal.
- **Neověřený odhad:** extrapolace autora postu, že předtrénink Flash na 48 bilionech a Pro na 30 bilionech tokenů odpovídá zhruba **2 miliardám dolarů** nákladů. Xiaomi toto číslo neuvádí.
- **Neověřené tvrzení:** domněnka autora, že zastavení RL tréninku znamená blížící se přeučení a výrazný překryv trénovacích úloh s benchmarky.
- **Marketingové tvrzení výrobce:** že MiMo-V2.6-Pro je „nejsilnější otevřený model k dnešnímu dni“ a překonává Kimi K3 a Qwen3.8 Max — v balíčku není nezávislé ověření.
- **Neshoda o hardwaru:** u/ummitluyum tvrdí, že je potřeba cluster čtyř H200, u/MDSExpro namítá, že stačí dvě.

## Proč to je důležité

MiMo-V2.6 je dalším dokladem, že **otevřené modely se dotahují na uzavřenou špičku** — 46,32 v indexu Artificial Analysis a formalizace matematické věty v Lean 4 posouvají otevřené modely do oblasti, kde se ještě nedávno měřily jen komerční systémy. Zároveň je to zajímavý údaj o ekonomice RL: 3,5 milionu dolarů za 30 kroků a 750 tisíc trajektorií zní jako „málo“, ale při započtení předtréninku na desítkách bilionů tokenů jde o projekt v řádu miliard. Pro lokální komunitu je podstatné, že modely zůstávají dostupné přes API za ceny V2.5, ale na vlastním hardwaru vyžadují velký VRAM.

## Další diskuse

- [1wmtjqu](https://www.reddit.com/r/LocalLLaMA/comments/1wmtjqu/) — r/LocalLLaMA, 185 bodů, 39 komentářů: MiMo-V2.6 se destilovalo do Qwen 9B.
- [1wn59vj](https://www.reddit.com/r/LocalLLaMA/comments/1wn59vj/) — r/LocalLLaMA, 102 bodů, 27 komentářů: XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B na Hugging Face.
- [1wn6qwi](https://www.reddit.com/r/LocalLLaMA/comments/1wn6qwi/) — r/LocalLLaMA, 69 bodů, 23 komentářů: o architektuře MiMo 2.6.
- [1wmr3nu](https://www.reddit.com/r/LocalLLaMA/comments/1wmr3nu/) — r/LocalLLaMA, 29 bodů, 33 komentářů: MiMo 2.6 Pro je dobrý, ale potřebuje více promptování než Sol.
- [1wnjbwn](https://www.reddit.com/r/LocalLLaMA/comments/1wnjbwn/) — r/LocalLLaMA, 13 bodů, 11 komentářů: MiMo-V2.6-Flash na vLLM — opravy prázdných odpovědí s thinking a nástroji.

## Zdroje

- https://mimo.xiaomi.com/mimo-v2-6 a https://mimo.xiaomi.com/mimo-v2-6/article.html (oznámení Xiaomi)
- https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/
- lokální snímek dashboardu: `2026-09-22/_data/img/1wn36d4-1.png`
- komentáře: `2026-09-22/_data/raw/comments/1wn36d4.json`
