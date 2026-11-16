# 50497892
**PyPI má nové stránky s jasnějšími bezpečnostními signály**

Hacker News · rbanffy · 14. 11. 2026, 16:40 · 230 bodů / 99 komentářů · [diskuse](https://news.ycombinator.com/item?id=50497892)

PyPI dokončil redesign stránek projektů, který ohlásil v červenci, a nasadil ho do ostrého provozu. Změna má uživatelům usnadnit posouzení důvěryhodnosti balíčků v době, kdy pythonový ekosystém rychle roste a stává se lákavějším cílem útočníků.

Srdcem novinky je nová záložka Security, která ukazuje stav původu vydání a atestace u jednotlivých souborů. PyPI rozlišuje plný původ, kdy mají atestaci všechny soubory, a varování při neúplném, nekonzistentním, změněném či ztraceném původu, nově upozorňuje i na soubory přidané s velkým zpožděním. Podoba vychází z doporučení OpenSSF a z uživatelského výzkumu v python komunitě, doprovází ji přepracovaný postranní panel s metadaty a přehlednější historie vydání.

Diskuse se rychle stočila k tomu, co nové signály vlastně říkají. cowlevel shrnuje, že jde o odhalení dříve neškodných projektů, jejichž záznam byl napaden, nikoli o odhalení záměrně škodlivých balíčků. Kwpolska k tomu suše dodává, že systém umí také odhalit projekty, které se odvážily přesunout buildy pryč z velkých hostingů. djoldman přidává konkrétní ukázky stránek bez původu a s ním a MeteorMarc si stěžuje, že ikonky u zdrojových archivů a wheelů působí zmateně.

Nejživější spor se vede o důvěryhodné publikování. eesmith se ptá, zda jsou důvěryhodnými vydavateli jen velké americké firmy a jak se k nim má dostat někdo, kdo staví na vlastním hardwaru nebo hostuje na Codebergu či Sourcehutu. pdonis by uvítal možnost připojit k účtu vlastní veřejný klíč a podepisovat balíčky sám, bez workflow kontrolovaného technologickými giganty, a tzlahp připomíná zrušené PGP podpisy. woodruffw vysvětluje, že o další poskytovatele je zájem, ale musí prokázat silnou správu a rotaci klíčů, protože se fakticky stávají zprostředkovatelem přihlašovacích údajů k PyPI.

Praktickou zkušenost přidává zzzeek: jakmile má jeden soubor v balíčku atestaci, PyPI očekává atestaci u všech a jinak ukazuje výrazná varování, aniž by na chybějící soubor poslal e-mail. woodruffw oponuje, že o trvalý přepínač nejde, a odkazuje na diskusi na fóru Pythonu. Vedle toho time4tea kritizuje celý příběh důvěry jako centralizaci a podporu uzamčení u velkého cloudu, WhyNotHugo mluví spíš o plnění tabulek prokazujících shodu než o skutečné bezpečnosti, zatímco samhclark vítá keyless podpisy ve stylu Sigstore a doufá, že tlak přiměje i menší CI služby zlepšit práci s OIDC. Podle rcxdudea by přitom důvěryhodnost zdroje lépe řešily reprodukovatelné buildy s distribuovaným ověřováním.

Z vlákna tak vychází PyPI jako užitečný, ale neúplný kompas: umí upozornit na podezřelou změnu původu, o skutečné nezávadnosti kódu ale stále nic neříká.
