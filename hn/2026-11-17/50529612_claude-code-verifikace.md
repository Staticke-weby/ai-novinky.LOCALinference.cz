# 50529612
**Tým Claude Code: verifikační smyčky pustí desítky agentů najednou**

Hacker News · craigmart · 17. listopadu 2026, 11:20 · 278 bodů / 223 komentářů · [diskuse](https://news.ycombinator.com/item?id=50529612)

Tým Claude Code popsal, jak udržuje kvalitu ve chvíli, kdy zhruba 90 procent kódu píše a recenzuje sám Claude. Klíčem jsou podle něj verifikační smyčky s důkazy: bez nich člověk uhlídá jen jednoho či dva agenty najednou, s nimi jich může běžet desítky až stovky paralelně. V interním testu strukturovaného generování souborů prý samostatný hodnotitel kontrolující výstup proti rubrice zvedl úspěšnost až o deset procentních bodů, nejvíc u nejtěžších úloh.

Odkazovaný text od Addyho Osmaniho doporučuje investovat hlavně do tří typů testů: end-to-end testů popisujících reálné uživatelské cesty, property testů generujících tisíce okrajových vstupů a diferenciálních testů porovnávajících starý a nový systém na stejných datech. K tomu tým přidává vlastní praxi – dovednost verify pro kouřové otestování aplikace před commitem, pravidlo tří neúspěšných pokusů, po kterých nastupuje člověk, a zásadu, že změna nesmí přepisovat pravidla, která ji hodnotí.

Nejživější debata se stočila k penězům. Uživatel girvo píše, že už s jedním či dvěma agenty utrácí dva tisíce dolarů měsíčně za tokeny, a ptá se, jak má pouštět desítky agentů. Uživatel simianwords oponuje, že osobní útrata se nedá srovnávat s fungováním ziskové firmy, náklady na inference navíc klesají a verifikace releasu se dělá jednou pro celý tým. Jiní si z toho utahují: uživatel thatsabadlook radí vyhodit sám sebe, uživatel duskdozer mluví o nekonečné peněžní kličce a uživatel philipwhiuk doporučuje vstoupit na burzu s bilionovou valuací.

Druhá linka řeší, zda to celé nejde levněji bez tokenů. Uživatel OtherShrezzing tvrdí, že článek působí dojmem neomezeného rozpočtu a že stejné či lepší výsledky dá deterministický Playwright napsaný jednou a pouštěný téměř zadarmo. Uživatel arbll namítá, že dát agentům do ruky správné nástroje včetně Playwrightu je právě pointou textu, uživatel xnorswap připomíná přednášku Lauren Tan o levných deterministických kontrolách typu statické analýzy na prvním místě. Uživatel simianwords pak hájí přirozený jazyk: invariant popsaný slovy je oddělený od architektury kódu, zatímco testy svázané s kódem s ním korelují a snáz přehlédnou stejnou chybu.

Zbytek vlákna patří rýpnutí a detailům. Uživatele dude250711 nejvíc zajímá zbývajících deset procent, které Claude nepíše, uživatel mrheosuper tipuje, že jde o změny nasazené bez recenze. Uživatelé Ampersander a Goto80 vtipkují, proč vůbec přemýšlí tým, když by za něj měl přemýšlet produkt. A uživatel ForHackernews si všímá ironie, že stránka o špičkovém inženýrství se sama načte s polorozbitým stylem a varováním o nevyužitém preloadu.

Kdo chce škálovat agenty, musí podle článku nejdřív definovat, co znamená hotovo, a pak jen kontrolovat důkazy – samotné testy ale musejí zůstat rychlé, nespolehlivé a mimo dosah hodnocené změny.
