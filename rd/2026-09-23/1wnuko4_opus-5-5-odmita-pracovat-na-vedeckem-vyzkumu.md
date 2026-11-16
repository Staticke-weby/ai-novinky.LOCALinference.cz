# 1wnuko4

**Opus 5.5 odmítá pracovat na vědeckém výzkumu, hlásí biolog**

| | |
|---|---|
| Subreddit | r/ClaudeAI |
| Autor | u/Circadian07 |
| Publikováno (Europe/Prague) | 23. 9. 2026, 05:17 |
| Skóre / komentáře | 359 / 96 |
| Odkaz | https://i.redd.it/knmrangst6rh1.jpeg |
| Diskuse | https://www.reddit.com/r/ClaudeAI/comments/1wnuko4/i_do_scientific_research_and_opus55_refuses_to/ |

## Co se stalo

Uživatel u/Circadian07 zveřejnil 23. 9. 2026 v 05:17 (Europe/Prague) v subredditu r/ClaudeAI příspěvek s flairem „Claude Code“. Netvrdí v něm, že by model hlásil chybu nebo spadl — popisuje, že model Opus 5.5 odmítá pracovat s podklady k jeho vědeckému výzkumu. Příspěvek má skóre 359, 96 komentářů a poměr kladných hlasů 0,95. Nejde o klasický textový post: odkaz vede na obrázek na i.redd.it (https://i.redd.it/knmrangst6rh1.jpeg), tedy na screenshot z Claude Code.

Autor v textu příspěvku shrnuje situaci takto:

> „Claude používám především na vědecký výzkum. Doufal jsem, že tenhle nový model opraví ty příšerné problémy s kvalitou z minulé verze, ale když jsem ho jen požádal, aby se podíval na soubor, nebo mi dal status nové session, spustí to poplach, lol. Jsou tu další vědci, kteří byli dnes ráno optimističtí?“ (překlad) — u/Circadian07, text příspěvku

Klíčová je přiložená obrazovka. Podle pole `image_text` z extrakce zachycuje dialog Claude Code s názvem souboru „DOCX“ a promptem, ve kterém autor žádá, aby model navázal na předchozí session, podíval se na `memory.md` a `status.md` a porovnal je s dokumentem od svého vedoucího. Následuje řádek „Provedeno 5 příkazů“ a poté oznámení „Zpráva označena příznakem“ s vysvětlením, že ochranné mechanismy Opus 5.5 označily tuto session. Dialog odkazuje na zásady použití (https://www.anthropic.com/legal/aup) a uvádí, že jde možná o první setkání s tímto chováním na modelu Opus: Opus 5.5 je schopnější, a proto má silnější ochranné mechanismy, které „mohou občas označit práci blízkou biologickému výzkumu“ (překlad). Anthropic podle dialogu pracuje na snížení počtu chybně označených zpráv a Claude Code nemůže na poslední zprávu s Opus 5.5 odpovědět. Nabízené možnosti jsou přeformulovat požadavek v nové session nebo změnit model; v podrobnostech je uvedena značka `[bio]` a tlačítka „Zjistit více“, „Zobrazit podrobnosti“ a „Přetočit zpět“.

Vlákno se rychle rozrostlo na širší stížnost na nové zábrany (guardrails) u modelů Anthropicu. Komentující popisují odmítnutí u bakteriální kultury, strojového učení, opravy zranitelnosti SQL injection nebo u procedurálního generování rostlin v simulátoru. Nejdiskutovanějším tématem je ale otázka, jak se k výzkumu vůbec dostat legálně přes Anthropic — a zda jde o záměrné omezení.

Součástí článku je i sloučený příspěvek z téhož dne, který nabízí opačný přístup: místo stížnosti měření.

## Klíčová fakta

- Hlavní příspěvek: r/ClaudeAI, autor u/Circadian07, flair „Claude Code“, skóre 359, 96 komentářů, poměr hlasů 0,95, publikováno 23. 9. 2026 v 05:17 (Europe/Prague).
- Příspěvek není self-post: externí odkaz míří na obrázek https://i.redd.it/knmrangst6rh1.jpeg (doména i.redd.it).
- Přiložený screenshot z Claude Code obsahuje dialog „Zpráva označena příznakem“ s textem, že ochranné mechanismy Opus 5.5 označily session, a s podrobností `[bio]`.
- Dialog nabízí dvě řešení: přeformulovat požadavek v nové session, nebo změnit model.
- Uživatel u/grateful2you v komentáři odkazuje na ověřovací program pro oblast life sciences (https://www.anthropic.com/news/life-sciences-verification-program) a tvrdí, že organizace musí být na seznamu.
- Několik komentujících uvádí, že přešli na konkurenční modely: u/iamthe0ther0ne na GPT, u/Aargau na Astra/Sol, u/South-Year4369 zvažuje Codex, u/peanut-britle-latte mluví o budoucnosti open-weight modelů.
- Sloučený příspěvek 1wnp7lh od u/TheOnlyVibemaster oznamuje měsíční denní deterministický benchmark Opus 5.5 na adrese https://github.com/ninjahawk/livenerf.
- Balíček neobsahuje žádný stažený externí článek; k dispozici jsou jen redditové posty, komentáře a jeden přiložený obrázek.

## Čísla

| Položka | Hodnota |
|---|---|
| Skóre hlavního příspěvku | 359 |
| Komentářů u hlavního příspěvku | 96 |
| Poměr kladných hlasů (hlavní příspěvek) | 0,95 |
| Skóre sloučeného příspěvku 1wnp7lh | 141 |
| Komentářů u sloučeného příspěvku | 56 |
| Poměr kladných hlasů (sloučený příspěvek) | 0,97 |
| Skóre nejlepšího komentáře (u/eld3rlyy) | 152 |
| Skóre druhého komentáře (u/grateful2you) | 52 |
| Skóre nejlepšího komentáře u benchmarku (u/isparavanje) | 33 |
| Staženo komentářů v JSONu / uvedeno v balíčku (hlavní post) | 38 / 25 |
| Staženo komentářů v JSONu / uvedeno v balíčku (sloučený post) | 45 / 6 |
| Provedené příkazy v Claude Code podle screenshotu | 5 |
| Počet sloučených postů | 1 |

Nad rámec těchto čísel balíček neuvádí žádné údaje o tom, kolik uživatelů bylo postiženo, o podílu chybných označení ani o parametrech ověřovacího programu.

## Citace

> „Zjevně existuje seznam pro ověření v oblasti life sciences. Vaše organizace na něm musí být.“ (překlad) — u/grateful2you, komentáře k hlavnímu postu

> „Z geopolitických a finančních důvodů se moje instituce NIKDY nezapojí.“ (překlad) — u/Circadian07, komentáře k hlavnímu postu

> „Jo, Opus 5.5 a Fable mají stejné bezpečnostní funkce (předpokládám). Claude Science s těmito modely mě taky posílá někam.“ (překlad) — u/Circadian07, komentáře k hlavnímu postu

> „Tady to samé, chápu, proč ty zábrany existují, ale je to frustrující, zvlášť když jediná cesta vpřed je, aby se vaše instituce nějak spojila s Anthropicem, což se nikdy nestane.“ (překlad) — u/JC_Dentyne, komentáře k hlavnímu postu

> „Zeptal jsem se 5.5 na otázku o bakteriální kultuře a odmítl odpovědět. To je šílené.“ (překlad) — u/Fearless-Counter-229, komentáře k hlavnímu postu

> „TADY TAKÉ. Je to k vzteku — nejdřív Fable a teď Opus. Prskám vztekem.“ (překlad) — u/iamthe0ther0ne, komentáře k hlavnímu postu

> „Zábrany 5.5 musí pryč, je to šílené. Blokovalo mi to ty nejnáhodnější věci.“ (překlad) — u/Hobotronacus, komentáře k hlavnímu postu

> „Anthropic drží vrátka, aby profitoval z vědeckých objevů AI. Kdo si myslí, že jde o ‚bezpečnost‘, je naivní.“ (překlad) — u/ComprehensiveFun620, komentáře k hlavnímu postu

> „Myslím, že se správným softwarem se dá napáchat stejně velká škoda jako biologickou zbraní. Když dokážou nasadit zábrany u kódovacích modelů proti škodlivému softwaru, mohli by je nasadit i proti škodlivým biologickým sekvencím.“ (překlad) — u/SeniorVibeAnalyst, komentáře k hlavnímu postu

> „Musíte být bioterorista a Dario a spol. nás zachraňují tím, že vás ženou k výrobě zbraní hromadného ničení s Opus 5.0, což nepochybně selže. Vážně ale — zkoušel jste s tímto modelem Claude Science?“ (překlad) — u/eld3rlyy, komentáře k hlavnímu postu

> „Proto potřebujete, aby ostatní modely byly na úrovni Anthropicu. Když jsou nahoře, je to čistá tyranie.“ (překlad) — u/Cagnazzo82, komentáře k hlavnímu postu

> „A proto mají open-weight modely velkou budoucnost.“ (překlad) — u/peanut-britle-latte, komentáře k hlavnímu postu

> „Musíte testovat statistickou významnost, jinak byste jen četli z čajových lístků náhody, protože LLM jsou stochastické.“ (překlad) — u/isparavanje, komentáře ke sloučenému postu

## Co říkají komentáře

Vlákno se dělí na dvě hlavní linie: jak se dostat k ověření, a čím model nahradit.

**Ověřovací program jako nedostupná branka.** Nejvýše hodnocený věcný komentář přichází od u/grateful2you (52 bodů) — odkazuje na ověřovací program Anthropicu pro life sciences a tvrdí, že organizace musí být na seznamu. Navazující komentář od u/iamthe0ther0ne (35 bodů) popisuje, proč to podle něj v praxi nefunguje: výzkumné ústavy by o to možná stály, ale univerzitní administrativy to vnímají jako odpovědnost jednotlivých výzkumníků. Zároveň upozorňuje, že většina laboratoří nesdílí jeden API účet — každý doktorand, postdok nebo vědecký pracovník používá vlastní, protože laboratoř nechce mít data vázaná na jednoho poskytovatele, který často mění platformu a nemá podporu, když se něco pokazí. Sám se označuje za neurovědce pracujícího s myšími modely, tedy podle svých slov „ani zdaleka“ nejde o výzkum zneužitelný dvojím způsobem, a dodává, že přešel na GPT. V dalších komentářích (7 a 5 bodů) píše, že žádá možnost přihlásit se individuálně — klidně i s pasem — a že jeho instituce ověřovacím procesem neprojde. Vyzývá také, aby každý příznak uživatelé nahlásili přes palec dolů, protože Anthropic by měl vědět, jaký legitimní výzkum blokuje.

**Zdůvodnění zábran.** Menšinový, ale věcný pohled nabízí u/SeniorVibeAnalyst (8 bodů): zábrany proti zneužití dávají smysl i mimo biologii, protože stejnou škodu lze napáchat softwarem, a když jdou zábrany nasadit u kódovacích modelů, šly by nasadit i u biologických sekvencí. u/JC_Dentyne (19 bodů) souhlasí, že zábrany chápe, ale označuje za frustrující, že jediná cesta vede přes partnerství instituce s Anthropicem.

**Obecházení a náhrady.** Technické tipy shrnuje u/Edenisb (9 bodů): vypnout personalizaci, zkontrolovat `.md` soubory, zda v nich není něco, co detekci spouští, a zeptat se jiné verze Clauda. u/iamthe0ther0ne (3 body) uvádí, že používá Codex a přidal si účet GPT, když se zábrany Fable po několika měsících nezlepšily, ačkoli pro bioinformatiku má raději Claude. u/Aargau (6 bodů) píše, že musel na „cokoli podstatného“ přejít na Astra/Sol, přestože je v programech Daybreak i Anthropic Cyber, a cituje výměnu, ve které měl Fable označit i běžnou konverzaci. u/South-Year4369 (3 body) popisuje opakované odmítnutí u reverzního inženýrství staré mobilní aplikace — nejprve přesměrování na Opus 4.8, později přímé odmítnutí — a plán vyzkoušet Codex.

**Rozsah dopadů mimo biologii.** u/ScreenAppropriate679 (6 bodů) tvrdí, že Fable zablokoval opravu zdokumentované zranitelnosti SQL injection. u/MiddleCommercial1875 (9 bodů) si stěžuje, že musel předělávat AI spravující domácí server kvůli pravidlům blokujícím přístup k řetězci myšlenek (chain of thought). u/magiblufire (3 body) uvádí, že model byl downgradován, když práci rozšířil o procedurální generování ostružiníku. u/QoTSankgreall (3 body) spojuje problém s tréninkem na sladění (alignment): podle něj bylo jasné, že model s nejvyšším skóre v testu sladění bude nepoužitelný. Ironický komentář u/eld3rlyy (152 bodů, nejlepší v celém vlákně) otázku obrací v žert o bioterorismu a ptá se, zda autor zkoušel Claude Science.

**Benchmark.** Ve sloučeném příspěvku převažuje jiný tón: uživatelé se ptají na metodiku a nastavují si připomínky. u/isparavanje (33 bodů) žádá test statistické významnosti. u/Niceneasy92 (8 bodů) podotýká, že tolik připomínkových botů u jednoho příspěvku ještě neviděl. Autor benchmarku u/TheOnlyVibemaster (7 bodů) odpovídá, že doufá v transparentnost, která podle něj nyní chybí.

## Rozpory a neověřené informace

- **Bezpečnost vs. zisk.** u/JC_Dentyne říká, že existenci zábran chápe; u/ComprehensiveFun620 tvrdí, že Anthropic drží vrátka kvůli zisku z vědeckých objevů. Obě tvrzení jsou názory, nikoli doložená fakta.
- **Shodné zábrany u Opus 5.5 a Fable.** u/Circadian07 sám píše „předpokládám“; balíček to nepotvrzuje.
- **Příčina degradace modelů.** u/TheOnlyVibemaster spekuluje o „nějaké exponenciální kvantizaci v čase“. Jde o jeho podezření, které má teprve změřit; výsledky jsou slíbeny až za měsíc.
- **Dopad na instituce.** Tvrdí-li komentující, že jejich univerzita ověřovacím procesem neprojde, opírá se to o jejich vlastní zkušenost; balíček neobsahuje vyjádření Anthropicu ani univerzit.
- **Omezení podkladu.** Balíček neobsahuje stažený externí článek — jen posty, komentáře a jeden obrázek. Ověřovací program life sciences je zastoupen pouze odkazem a komentáři, jeho podmínky tedy nelze z podkladu doložit.
- **Nekryté případy.** Příklady blokací (SQL injection, reverzní inženýrství, domácí server, simulátor) jsou tvrzení komentujících bez nezávislého ověření.

## Další diskuse

| id | subreddit | skóre | komentářů | čas (Europe/Prague) | český překlad titulku | permalink |
|---|---|---:|---:|---|---|---|
| 1wnp7lh | r/ClaudeAI | 141 | 56 | 23. 9. 2026, 01:15 | Nový benchmark pro ověření, zda Opus 5.5 nedostává „nerf“ | https://www.reddit.com/r/ClaudeAI/comments/1wnp7lh/new_benchmark_to_see_if_opus_55_gets_nerfed/ |

Autor u/TheOnlyVibemaster reaguje na časté řeči o tom, že Anthropic modely v průběhu času oslabuje („nerfuje“), a rozhodl se to otestovat: měsíc bude denně spouštět sérii deterministických testů na Opus 5.5 a zaznamenávat odchylky. Výsledky hodlá zveřejňovat denně v repozitáři https://github.com/ninjahawk/livenerf, přičemž zdůrazňuje nezávislou ověřitelnost a možnost posílat vlastní přírůstky přes pull requesty. Testy navrhl s pomocí Clauda, ale záměrně je nastavil jako obtížné úlohy, které se během měsíce nemění — pokud model něco zvládne nyní a později ne, mělo by se to projevit. V doplnění upřesňuje, že deterministické jsou otázky a vyhodnocovací skripty, nikoli výstupy modelu; měří se statisticky, zda přesnost na pevné sadě úloh v čase klesá. Diskuse u tohoto příspěvku je metodická: převažuje požadavek na statistickou významnost.

## Proč to je důležité

Případ ukazuje střet dvou logik. Anthropic podle dialogu v Claude Code nasadil u Opus 5.5 silnější ochranné mechanismy, které mají zabránit zneužití v biologickém výzkumu, a zároveň přiznává, že mohou chybně označit i legitimní práci. Nabízená náprava je ale pouze organizační ověření, o kterém komentující tvrdí, že je pro velkou část akademické praxe nedostupné — univerzity se do něj nehrnou a jednotliví doktorandi a postdoci používají vlastní účty.

Druhá rovina je měřitelnost. Vedle stížností stojí pokus o veřejný, opakovatelný benchmark, který má odpovědět, zda kvalita modelu v čase klesá. Právě proto, že jde o stochastické modely, je i tenhle pokus kritizován za nedostatečnou statistickou průpravu. Pro čtenáře z výzkumné praxe je tak zajímavé nejen to, co Opus 5.5 odmítl udělat, ale i posun diskuze od „co model umí“ k „kdo se k němu dostane a jak se to dá změřit“.

## Zdroje

- Balíček: `2026-09-23/_data/bundles/1wnuko4.md`
- Extrakce: `2026-09-23/_data/extracts/1wnuko4.json`
- Obrázek ze screenshotu: `2026-09-23/_data/img/1wnuko4.jpeg`
- Hlavní diskuse: https://www.reddit.com/r/ClaudeAI/comments/1wnuko4/i_do_scientific_research_and_opus55_refuses_to/
- Externí odkaz (obrázek): https://i.redd.it/knmrangst6rh1.jpeg
- Sloučený post: https://www.reddit.com/r/ClaudeAI/comments/1wnp7lh/new_benchmark_to_see_if_opus_55_gets_nerfed/
- Zásady použití Anthropicu odkazované v dialogu: https://www.anthropic.com/legal/aup
- Ověřovací program life sciences odkazovaný v komentáři: https://www.anthropic.com/news/life-sciences-verification-program
- Repozitář benchmarku: https://github.com/ninjahawk/livenerf
