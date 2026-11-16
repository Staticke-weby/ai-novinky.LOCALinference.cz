# 1wobyjp

**HLE-Diamond: vyčištěný test Humanity's Last Exam vede GPT-6 Astra se 60,6 %**

| | |
|---|---|
| Subreddit | r/singularity |
| Autor | u/socoolandawesome |
| Publikováno (Europe/Prague) | 23. 9. 2026, 19:10 |
| Skóre / komentáře | 350 / 101 |
| Odkaz | https://www.reddit.com/gallery/1wobyjp |
| Diskuse | https://www.reddit.com/r/singularity/comments/1wobyjp/updated_version_of_humanitys_last_exam_hlediamond/ |

## Co se stalo

Organizace Center for AI Safety (CAIS) a Scale AI oznámily 22. září 2026 nový soubor otázek nazvaný **HLE-Diamond**. Nejde o zcela nový test, ale o vyčištěnou podmnožinu dosavadního benchmarku Humanity's Last Exam (HLE). Podle oznámení jde o výsledek rok trvajícího procesu čištění a zpřesňování, do kterého přispěla výzkumná komunita.

Redditový příspěvek na r/singularity zveřejnil uživatel u/socoolandawesome 23. září 2026 v 19:10 středoevropského času. Post odkazuje na tweet účtu CAIS a na blog `lastexam.ai/blog/hle-diamond`. V době sběru dat měl skóre 350, poměr kladných hlasů 0,98 a 101 komentářů; vlákno se zařadilo pod flair „AI“.

HLE-Diamond obsahuje **1 000 otázek** a je rozdělen na dvě poloviny: 500 otázek na uvažování (reasoning) a 500 otázek na odborné znalosti (knowledge). Otázky jsou navržené tak, aby se daly zodpovědět v režimu bez přístupu k vnějším zdrojům (closed-book). Autoři zároveň připomínají, že původní HLE se používá i pro hodnocení agentních systémů, a proto zvlášť definují doporučené nastavení pro testování HLE-Diamond s nástroji.

Hlavní srovnání modelů proběhlo bez nástrojů a se všemi modely na úrovni uvažování „high“ (vysoká). V tomto nastavení vede **GPT-6 Astra se 60,6 %**, následovaný Claudem Opus 5.5 (55,0 %) a Claude Fable 5.1 (51,3 %). S nástroji pro web a kód se výsledky výrazně zvedají: GPT-6 Astra dosahuje 82,9 %.

## Klíčová fakta

- **Vydavatelé:** Center for AI Safety a Scale AI; oznámení je datované 22. září 2026.
- **Povaha souboru:** vyčištěná podmnožina Humanity's Last Exam (HLE), nikoli nový benchmark postavený od nuly.
- **Velikost:** 1 000 otázek — 500 na uvažování a 500 na znalosti.
- **Režim:** otázky jsou navržené jako zodpověditelné bez externích zdrojů; autoři nicméně vydávají i doporučení pro hodnocení s nástroji.
- **Nastavení hodnocení:** všechny modely v hlavních výsledcích jsou hodnoceny na úrovni uvažování „high“.
- **Vítěz bez nástrojů:** GPT-6 Astra se 60,6 %; s nástroji (web + kód) 82,9 %.
- **Načtení datové sady:** `load_dataset("cais/hle-diamond")`.
- **Návaznost:** autoři děkují přispěvatelům otázek i odborníkům a výzkumníkům, jejichž vstupy v rámci HLE-Rolling formovaly HLE-Diamond.
- **Kontakt:** agibenchmark@safe.ai.

Rozdělení skóre na obě části testu ukazuje jiný obrázek než celkové pořadí. V části na uvažování je pořadí obdobné jako v součtu (GPT-6 Astra 75,6 %), ale ve znalostní části je rozdíl mezi prvním a druhým místem malý: GPT-6 Astra 45,6 % proti Claudu Opus 5.5 s 46,8 %. Claude Opus 5.5 tedy v čistě znalostní části prvního modelu v podkladu mírně konkuruje.

## Čísla

**Celkové skóre podle modelů (úroveň uvažování „high“):**

| Model | Bez nástrojů | S nástroji (web + kód) |
|---|---|---|
| GPT-6 Astra | 60,6 % | 82,9 % |
| Claude Opus 5.5 | 55,0 % | 73,9 % |
| Claude Fable 5.1 | 51,3 % | 72,4 % |
| Claude Opus 5 | 38,6 % | 69,1 % |
| Gemini 3.8 Flash | 34,3 % | 60,3 % |
| GPT-6 Sol | 33,8 % | 64,9 % |
| GPT-5.6 Sol | 31,2 % | 56,5 % |
| Muse Spark 1.3 | 25,4 % | 55,5 % |
| Grok 4.7 | 23,4 % | hodnota v podkladu neuvedena |

**Rozpad na uvažování a znalosti:**

| Model | Uvažování (reasoning) | Znalosti (knowledge) |
|---|---|---|
| GPT-6 Astra | 75,6 % | 45,6 % |
| Claude Opus 5.5 | 63,2 % | 46,8 % |
| Claude Fable 5.1 | 62,0 % | 40,6 % |
| Claude Opus 5 | 47,0 % | 30,2 % |
| Gemini 3.8 Flash | 38,6 % | 30,0 % |
| GPT-6 Sol | 44,2 % | 23,4 % |
| GPT-5.6 Sol | 38,8 % | 23,6 % |
| Muse Spark 1.3 | 31,6 % | 19,2 % |
| Grok 4.7 | 32,4 % | 14,4 % |

**Parametry podkladu a příspěvku:**

| Ukazatel | Hodnota |
|---|---|
| Počet otázek v HLE-Diamond | 1 000 |
| Otázky na uvažování | 500 |
| Otázky na znalosti | 500 |
| Skóre redditového postu | 350 |
| Poměr kladných hlasů | 0,98 |
| Komentářů | 101 |
| Komentářů zpracovaných v extrakci | 37 |
| Komentářů uvedených v balíčku | 25 |
| Délka staženého článku | 2 987 znaků |

Z tabulek vyplývá i jedna netypická změna pořadí: zatímco bez nástrojů je GPT-6 Sol (33,8 %) pod Gemini 3.8 Flash (34,3 %), s nástroji se pořadí obrací — GPT-6 Sol má 64,9 % a Gemini 3.8 Flash 60,3 %. U Grok 4.7 podklad srovnání s nástroji vůbec neuvádí.

## Citace

> „Vydáváme HLE-Diamond, vyčištěnou podmnožinu sbírky otázek Humanity's Last Exam (HLE), a to po rok trvajícím procesu čištění a zpřesňování za přispění výzkumných komunit.“ (překlad) — autoři oznámení, blog HLE-Diamond

> „HLE-Diamond obsahuje 1 000 otázek.“ (překlad) — autoři oznámení, blog HLE-Diamond

> „Všechny modely jsou hodnoceny s uvažováním na úrovni high.“ (překlad) — autoři oznámení, blog HLE-Diamond

> „Humanity's Last Exam – opravená verze – FINÁLNÍ.“ (překlad) — u/Zorander22, komentáře pod příspěvkem

> „Humanity's Last Exam – opravená verze – FINÁLNÍ – FINÁLNÍ_v2 – SKUTEČNĚ_FINÁLNÍ.“ (překlad) — u/frogsarenottoads, komentáře pod příspěvkem

> „Takže to nebyl ten poslední.“ (překlad) — u/phenotype001, komentáře pod příspěvkem

> „Stojí za zmínku, že všechny modely jsou podle jejich webu hodnoceny na úrovni uvažování ‚high'. Takže na režimech ‚max' s nástroji už může být benchmark úplně saturovaný.“ (překlad) — u/socoolandawesome (autor postu), komentáře pod příspěvkem

> „Tohle přece zvedne skóre Astra v Artificial Analysis, ne? Předtím bylo horší než Fable a Opus. Celkem to ukazuje, jak špatné benchmarky jsou — i takhle velké testy jsou hluboce chybné.“ (překlad) — u/Sensitive_Cell_119, komentáře pod příspěvkem

## Co říkají komentáře

**Vtipy o „posledním“ testu.** Nejvýše hodnocený komentář vlákna (244 bodů) je jen krátká parodie na název: u/Zorander22 píše „Humanity's Last Exam – opravená verze – FINÁLNÍ“ a u/frogsarenottoads (117 bodů) ho rozvádí do řetězce „FINÁLNÍ – FINÁLNÍ_v2 – SKUTEČNĚ_FINÁLNÍ“. Motiv se táhne celým vláknem: u/phenotype001 konstatuje „Takže to nebyl ten poslední“, u/RevoDS přidává „Humanity's Last Last Exam“, u/Mindrust „FINAL (1)“, u/Altares13 „R-Type Final 3 Evolved“ a u/TuringGoneWild „Humanity's předposlední exam (zatím)“. Věcný protiargument nabízí u/ThatsALovelyShirt: „poslední“ prý znamená „předchozí“ — tedy že ten minulý test byl fakt těžký, ale později může přijít ještě těžší.

**Spolehlivost benchmarků a Artificial Analysis.** Druhé velké téma je důvěryhodnost čísel. u/Waiting4AniHaremFDVR (42 bodů) očekává, že HLE-Diamond „pravděpodobně lépe nakalibruje index inteligence Artificial Analysis“. u/reduction-oxidation (31 bodů) to vítá s odkazem na zprávu Epoch AI, podle níž měl původní HLE chyby. Proti samotnému indexu Artificial Analysis se ale ostře vymezuje u/spottiesvirus (30 bodů): váhy jednotlivých úloh jsou podle něj svévolné, programování tvoří 20 % skóre a v rámci toho polovinu zabírá Terminal Bench 4.0 a polovinu „SciCode (???)“, což nedává smysl. Kritizuje také to, že se vše hodnotí jedním pokusem (one-shot), zatímco v reálu nikdo nezvládne úlohu o 9 750 krocích, kterých má celý evaluační balík tolik.

**Je to stejný test, nebo ne.** u/Maleficent_Sir_7562 (26 bodů) upozorňuje, že jde pořád o tentýž HLE, jen jeho podmnožinu. Na to reaguje i diskuze o tom, co vlastně „benchmaxxing“ znamená: u/the_pwnererXx a u/FateOfMuffins tvrdí, že Opus je na HLE „vytuněný“ a Astra je lepší, kdežto u/tetoing se ptá, jak může lepší výsledek jednoho modelu dokazovat tunění druhého. u/Flope jde ještě dál a označuje HLE za benchmark na PR body, který měří triviality typu „skládání divně barevných polygonů do jiných polygonů“, zatímco u/Chemical_Hawk_6307 oponuje, že výkonnostně vytuněný není: Astra podle něj zůstává nejlepší model pro hluboké a široké uvažování, Opus je zase „jasný denní pracant“, protože je dobrý a levný.

**Srovnání modelů v praxi.** u/Paralda (8 bodů) hodnotí, že Opus 5.5 je o něco lepší než Fable 5.1 a výrazně levnější, ale ani jeden zatím není na úrovni Astra; pro běžné použití a cenu podle něj Opus 5.5 „rozdrtí všechno ostatní“. u/midgaze (7 bodů) si všímá rozdílu v režimech uvažování: GPT-6 Astra si vede téměř stejně dobře na „high“ jako na „max“, kdežto GPT-6 Sol je znatelně lepší na „max“ než na „xhigh“, což se má odrážet právě v těchto výsledcích. Objevují se i nostalgické a pozitivní reakce: u/PVORY (16 bodů) píše, že HLE „tak dlouho vydržel a byl tak dobrý“, u/TheReedemer69 ho označuje za nejdéle stojící benchmark a u/Alarming_Welder_7190 celý závod baví.

## Rozpory a neověřené informace

Do této sekce patří vše, co balíček nebo extrakce označují jako tvrzení třetích stran, spekulaci nebo názor, který nelze ověřit z podkladu:

- **Údajný report Epoch AI o chybách původního HLE.** Komentář u/reduction-oxidation odkazuje na tweet Epoch AI, podle kterého měl být původní HLE chybný. Podklad samotný obsah tweetu neobsahuje, jde tedy o druhotné tvrzení.
- **Obvinění z „benchmaxxingu“.** Tvrzení u/FateOfMuffins a u/the_pwnererXx, že Anthropic (respektive model Opus) se na HLE „vytunil“, a že test měl „spoustu chyb“, není v podkladu doloženo; jde o názor komentujících.
- **Kalibrace indexu Artificial Analysis.** Očekávání u/Waiting4AniHaremFDVR, že HLE-Diamond zlepší kalibraci indexu Artificial Analysis, je spekulace. Totéž platí pro úvahu u/Sensitive_Cell_119, že se tím zvedne skóre Astra, protože dřív bylo horší než u Fable a Opus.
- **Saturovanost při režimu „max“.** Poznámka autora postu, že na režimech „max“ s nástroji může být benchmark „úplně saturovaný“, je spekulace; podklad uvádí jen výsledky na úrovni „high“.
- **Kritika vah Artificial Analysis.** Konkrétní čísla z komentáře u/spottiesvirus (20 % skóre za programování, polovina z toho Terminal Bench 4.0, 9 750 kroků v celém evaluačním balíku) pocházejí výhradně z komentáře a nejsou ověřena z oznámení CAIS.
- **Omezení podkladu u obrázků.** Příspěvek je galerie (odkaz vede na `reddit.com/gallery/1wobyjp`), ale extrakce neobsahuje žádný text obrázků (pole `image_text` je prázdné). Obsah přiložených obrázků proto nelze popsat a v článku se neuvádí.

Rozpor mezi komentujícími zůstává i v základní interpretaci: část vlákna považuje lepší skóre Astra za doklad vytunění konkurence, část (u/tetoing, u/Chemical_Hawk_6307) tuto logiku odmítá.

## Proč to je důležité

Humanity's Last Exam byl vnímán jako jeden z nejdéle vydrživších a nejnáročnějších testů pro jazykové modely. To, že po roce čištění vzniká jeho podmnožina s jasně definovaným režimem hodnocení, mění způsob, jak se budou srovnávat špičkové modely: výsledky už se neopírají o původní, kritizovanou sbírku otázek, ale o zúžený soubor 1 000 otázek rozdělených na uvažování a znalosti.

Zároveň je vidět, kde modely stále ztrácejí. I nejlepší model bez nástrojů zvládne 60,6 % otázek a ve znalostní části jen 45,6 %. Teprve s přístupem k webu a kódu se dostává přes 80 %. Rozdíl mezi režimy „bez nástrojů“ a „s nástroji“ je tedy větší než rozdíl mezi jednotlivými špičkovými modely navzájem — a právě na tuto hranici se soustředí debata o tom, zda se benchmark nemá hodnotit rovnou s nástroji.

Pro české čtenáře je podstatné i to, že podklad sám upozorňuje na metodický detail: hlavní tabulky platí pro úroveň uvažování „high“, nikoli „max“. Jakákoli další interpretace čísel — včetně odhadů dopadu na agregované indexy, jako je Artificial Analysis — zůstává nad rámec zveřejněných dat.

## Zdroje

- Reddit příspěvek: https://www.reddit.com/r/singularity/comments/1wobyjp/updated_version_of_humanitys_last_exam_hlediamond/
- Odkaz příspěvku (galerie): https://www.reddit.com/gallery/1wobyjp
- Tweet CAIS: https://x.com/CAIS/status/2102787839964729431
- Blog HLE-Diamond: https://lastexam.ai/blog/hle-diamond
- Tweet Epoch AI (zmíněn v komentáři): https://x.com/EpochAIResearch/status/2100704765332394255
- Balíček: `2026-09-23/_data/bundles/1wobyjp.md`
- Extrakce: `2026-09-23/_data/extracts/1wobyjp.json`
