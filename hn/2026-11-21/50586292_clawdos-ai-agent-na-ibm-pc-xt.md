# 50586292
**ClawDOS: AI agent pro kódování běží na IBM PC XT z roku 1981**

Hacker News · Ricapar · 21. listopadu 2026, 06:38 · 162 bodů / 51 komentářů · [diskuse](https://news.ycombinator.com/item?id=50586292)

ClawDOS je AI coding agent, který běží přímo na IBM PC XT s procesorem 8088 na 4,77 MHz, 640 kB paměti a grafikou CGA. Po zadání příkazu CLAWDOS čte a upravuje soubory na disku, píše programy, překládá je v Turbo C, spouští je a dívá se, co vykreslí na obrazovku, a mezi rozhovory si vede poznámky v C:\MEMORY.

Srdcem je program HARNESS.EXE o velikosti 176 kB, který sám skládá požadavky na Claude Messages API, parsuje streamovanou odpověď a spouští osmnáct nástrojů. Vše kromě šifrovaného spojení zvládne samotná 8088, TLS obstarává pomocný bridge počítač, který jen kopíruje bajty mezi obyčejným HTTP a API. Celý repozitář přitom podle stránky projektu napsal Claude, pouze doprovodný text o historii rodinného počítače psal člověk.

V diskusi je znát hlavně nadšení z roztomilé lumpárny pouštět agenty v neobvyklém prostředí. Uživatel Tiberium to popisuje jako spouštění agentů v DOSu, Windows 95 nebo Linuxu na tlačítkovém telefonu a sledování, jak zareagují. Uživatel unleaded vypráví, že si podobného agenta postavil ve Win32 a sledoval, jak si DeepSeek v řetězci úvah uvědomí, že běží v NT 4.0: našel si DirectX SDK u Visual Studia 6 a na první pokus napsal 3D střílečku. Uživatel xhevahir k tomu přihazuje, ať někdo agenta zavře do Red Star OS a sleduje, jak shodí elektrickou síť.

Vážnější linka se točí kolem toho, že trhu citelně chybí agent pro zástupy starších strojů s Windows XP a Windows 7, ne na vývoj, ale na ladění. Uživatel linzhangrun si stěžuje, že skoro všichni agenti chtějí Windows 10 1809 a novější a na starých zařízeních zbývá jen zprovoznit SSH. Uživatel egeozcan oponuje, že často stačí vzdálená plocha, obraz disku ve virtuálce, a když není internet ani virtualizace, pomůže adaptér USB na COM, se kterým kdysi obsluhoval stroj s Windows 3.1 přes TERMINAL.EXE. K tomu se přidávají tipy na lehké agenty: perlová varianta pro starý Perl 5.0001, Igor běhající na ReactOS, XP a Windows 7, agent ve Free Pascalu a Delphim bez Node.js a Psi psané celé v ANSI C a Lua.

Zbytek vlákna patří vtipům a rýpnutí do současnosti. Hraje se tu na návrat skvělého DOSu, který konečně překoná TempleOS, na přepsání starých Lemmings pomocí AI i na optimalizaci config.sys a autoexec.bat. Uživatel ahofmann si říká o přepsání v Go s názvem GlaDOS a uživatel drob518 to shrnuje hláškou, že dřív byla móda spouštět Doom na každém kousku starého železa, teď se na něm spouští AI agent. Mezi tím zazní i věcná otázka, zda tenhle projekt dokazuje, že Claude Code se nemusí distribuovat jako dvousetmegabajtové binárky, a dotaz, jestli umí ClawDOS kromě Claude i Codex.

Z ClawDOS se tak stává víc než kuriozita: ukázka, že i stroj starý přes čtyřicet let dokáže s moderním modelem vést smysluplný rozhovor o kódu.
