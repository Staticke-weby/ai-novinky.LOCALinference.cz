# 1xriv9l
**LiveNerf po 47 dnech: Opus 5.5 se měřitelně nezhoršil**

r/ClaudeAI · u/TheOnlyVibemaster · 9. listopadu 2026, 05:58 · 434 bodů / 81 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xriv9l/)

Nezávislý projekt LiveNerf po 47 dnech souvislého testování nenašel důkaz, že by se model Opus 5.5 v čase zhoršoval. Za tu dobu nasbíral 3 666 vzorků na stejné zmrazené sadě otázek: původní desetidenní základna měla průměr 58,4 %, poslední den skončil na 61,5 %. Denní výsledky sice kolísaly, ale žádný trvalý pokles, který by splnil předem daná kritéria detekce, se neobjevil.

Autor zároveň zdůrazňuje, že měří jen samotný model, ne celý produkt kolem něj. Připomíná routování, nastavení nástrojů, správu kontextu nebo systémové prompty, které mohou zážitek změnit, aniž by se schopnosti modelu pohnuly. Dva lidé tak podle něj mohou mít s Claude Code znatelně odlišnou zkušenost, i když mluví se stejným základem, a právě proto by chtěl LiveNerf rozšířit na sledování různých modelů, rozhraní a časem i agentních systémů.

Nejvýše hodnocený hlas v diskusi ale míří na citlivost testu. u/ForwardLoop cituje z readme projektu, že záměna Opuse 5 za Opus 5.5 nebyla na 99 % rozlišitelná, a ptá se, zda takový benchmark vůbec může oslabení zachytit. Sám dodává, že zhoršení se podle jeho zkušenosti neprojevuje tolik obtížností úkolu jako jeho složitostí: model i ve slabších dnech zvládne těžkou věc, ale u složitého programu začne zapomínat, přehlížet a ztrácet souvislosti.

Na to navazuje věcná linka o agentních bězích. u/KAMIKAZEE93 popisuje LiveNerf jako 78 jednootázkových testů bez nástrojů na jednom účtu, zatímco jeho problém se ukázal až v dlouhých bězích o 25 až 38 krocích nástrojů a kontextu 70 až 130 tisíc: z 3. na 4. listopadu prý vyskočil počet výstupních tokenů na odpověď zhruba z 840 na 1 900, zatímco Sonnet a Haiku zůstaly ve stejných bězích beze změny. Podobně u/Old-Blacksmith-3174 žádá důkaz validity, tedy že sada otázek umí pokles vůbec detekovat, a u/early_burp namítá, že test nezachytí A/B testování mezi uživateli.

Zbytek vlákna je střetem dojmů. u/Needsupgrade píše, že Opus je poslední dny znatelně hloupý, u/MammayKaiseHain si stěžuje, že režim s vysokým úsilím žere mnohem víc tokenů a běží dvě až tři hodiny místo půlhodiny, a u/-DankFire upozorňuje na protichůdný post s 1,5 tisíce hlasy. Naproti tomu u/chingford-explorer za půl roku používání Opuse žádné zhoršení nepozoroval, u/Kalaminator mluví o konfirmačním zkreslení a přiznává, že pocit pomalejších odpovědí po přechodu z tarifu Ultra na Max nemá čísly podložený.

I kritici ale projekt spíš brání, než aby ho smetli. u/Aggressive_Roof488 chválí pomalu se zmenšující chybové úsečky, u/AggregationLinker vtipně poznamenává, že tři ze čtyř výkonnostních špiček připadají na neděle, kdy málokdo pracuje. Nejsurrealističtější teorii přidává u/QuantumPancake422, že zaměstnanci Anthropicu autorovi označili účet jako důležitý, aby nebyl degradován. Přes všechnu skepsi se vlákno shoduje v jednom: i nedokonalé průběžné měření je lepší než pouhé dohady o tom, zda model potichu nehl hloupne.
