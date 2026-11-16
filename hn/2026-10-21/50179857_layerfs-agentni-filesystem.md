# 50179857
**LayerFS: filesystem na míru kódovacím agentům**

Hacker News · l2dy · 21. října 2026, 14:34 · 71 bodů / 43 komentářů · [diskuse](https://news.ycombinator.com/item?id=50179857)

Na Hacker News se objevil odkaz na LayerFS, souborový systém, který autoři šijí na míru kódovacím agentům. Nemá to být další univerzální úložiště, ale vrstva, která rozumí tomu, jak agenti pracují se soubory a shellem. Diskuse se rychle stočila k tomu, jestli jde o novou myšlenku, nebo jen hezky zabalený návrat starých nápadů.

Web projektu stojí na myšlence efemérního výpočtu, tedy že výpočet existuje jen po dobu běhu příkazu. Každé volání souborového nástroje se podle autorů promítne jako jedna atomická operace úložiště a každé volání Bashe dostane vlastní efemérní pracovní prostor, který se po skončení zapíše zpět. Autoři k tomu dodávají jedno číslo na vysvětlení motivace: agenti prý tráví asi 80 % času přemýšlením a jen kolem 10 % v shellu.

Nejživější linku otevřel uživatel trollbridge prostou otázkou, čím se to liší od btrfs. Odpověď uživatele rvz byla kousavá: btrfs je léty prověřené v jádře Linuxu a nasazené v mission critical systémech, zatímco LayerFS působí jako rychle „vibe codovaný“ projekt s lákavým webem. Věcněji kontroval uživatel fnordpiglet, podle kterého je LayerFS spíš orientovaný na obsah a verzovaná data než na bloky, odkazoval i na benchmark dedupování na stránkách projektu a přiznával, že sémantika pracovních kopií, kterou dnes agenti a jejich postroje používají ve velkém, je přinejmenším otravná.

Druhá velká část vlákna ale neřeší soubory, nýbrž formu. Uživatel Sathwickp utrousil, že hezký je tak akorát web, uživatel robofanatic oponoval, že je to plné otravných animací, kvůli kterým se text skoro nedá číst, a další si stěžovali na únos scrollování a roztahaný layout. Zapadl do toho i postřeh uživatele toddmorey, jak může projekt hlásit verzi jedna, když stránka s architekturou je teprve „coming soon“, a poznámka uživatele Rapzid, že jméno je vzhledem k UnionFS, overlay2 a zavedenému pojmu vrstvových souborových systémů nešťastné a matoucí.

Třetí proud diskuse hledá předchůdce a náhrady. Uživatel compsciphd tvrdí, že skoro totéž už s kolegy dělal před lety a před třinácti lety si to i patentoval, a přihodil odkazy na Apiary a patent, na což uživatel amelius rýpl, proč na ten patent neupozornil agent samotného autora. Uživatel mpalmer to zobecnil do evergreenové výtky, že se s pomocí AI jen znovu vynalézají vyřešené problémy převlečené za nové agentské problémy. Mezi tím probleskují tipy: uživatel nico nabízí hravé demo v prohlížeči, uživatel shayonj odkaz na vlastní interní verzovaný systém pro jednorázové sandboxy a uživatel vagoz nástroj try, který nechá cokoli včetně agenta běžet v zrcadle systému a pak umožní změny zkontrolovat, použít nebo zahodit. Stranou nezůstala ani poznámka uživatele alchemist1e9, že jde o zhruba 245 tisíc řádků Rustu napsaných modely, což je samo o sobě působivé bez ohledu na to, co si o projektu myslíme.

Kdo čeká hotové úložiště do produkce, v diskusi ho nenajde, kdo hledá směr uvažování o agentech a souborovém stavu, má o čem přemýšlet.
