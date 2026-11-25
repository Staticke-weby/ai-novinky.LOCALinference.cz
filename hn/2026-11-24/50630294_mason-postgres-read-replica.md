# 50630294
**Mason nabízí čtecí repliku Postgresu postavenou na sloupcovém úložišti**

Hacker News · tagspace · 24. listopadu 2026, 17:11 · 89 bodů / 16 komentářů · [diskuse](https://news.ycombinator.com/item?id=50630294)

Mason je open-source náhrada čtecí repliky Postgresu, která slibuje stejné SQL i stejné odpovědi, ale analytické dotazy počítá ve sloupcovém enginu DuckDB. V ukázkovém dotazu nad deseti miliony řádků vrátil primární Postgres výsledek za 15,7 sekundy, zatímco Mason za 0,193 sekundy, tedy jedenaosmdesátkrát rychleji. Jde o jediný proces v Node.js, který si konfiguraci i synchronizovaná data drží lokálně ve složce, odkud běží.

Podle webu projektu si uživatel vybere, které tabulky a sloupce se mají synchronizovat a jak – na vyžádání, dotazováním, nebo logickou replikací. Mason pak příchozí postgresové dotazy za běhu přepisuje do podoby, kterou DuckDB spočítá nejrychleji. Nejvíc získají dotazy, které čtou spoustu řádků přes pár sloupců, jako počty, součty a grupování pro dashboardy a reporty, zatímco vyhledání jednoho řádku podle primárního klíče je naopak pomalejší než na Postgresu. Projekt je pod licencí Apache-2.0 a míří na týmy, které nechtějí provozovat těžký analytický stack.

V diskusi se nylonstrung ptá, co to přidává proti prostému spojení DuckDB s Postgresem přes ADBC. Autor pod přezdívkou tagspace odpovídá, že většina práce je ve dvou věcech: v replikační logice, která drží DuckDB v synchronizaci jako běžnou čtecí repliku, a v přepisovači dotazů, který většinu dotazů stlačí na pár stovek milisekund i nad deseti miliony řádků. S ADBC by podle něj zátěž dál dopadala na Postgres, nebyla by jistota stejné odpovědi a každý by si musel stavět vlastní ETL.

Na to navazuje aleda145: proč vůbec honit analytiku proti postgresové replice, když by šlo číst WAL a posílat změny jinam, zvlášť když u ad-hoc dotazů krátké zpoždění nevadí. NewJazz to čte jako snahu vyhnout se provozní tíze ClickHousu a přepisování dotazů – prostě vzít existující SQL a jen je zrychlit, navíc s možností snadno roztočit analytickou databázi v prostředí zákazníka. Sám tagspace v úvodním příspěvku popisuje podobnou cestu: ClickHouse je skvělý, když člověk zná tvary dotazů předem, ale pro jejich nahodilé postgresové zátěže měl velkou křivku učení a odlišný dialekt.

Zbytek vlákna míchá praktické dotazy s nadsázkou. alex_hirner se ptá, zda by replikované tabulky mohly žít jen na S3 v parketách, tagspace přiznává, že to nezkoušeli, protože teď vše synchronizují na lokální disk, ale vzhledem k podpoře v DuckDB by to prý mělo jít snadno. Vedle toho hum3hum3 ukazuje podobný pokus přepsat Postgres nad jedno souborovou SQLite běžící ve WebAssembly a ForHackernews připomíná PGlite. Nejstručnější odbočku obstarají neilsimp1 a akshay180, podle nichž je na světě příliš mnoho softwaru – a kamarádů – se jménem Mason.

Kdo má pomalé reporty nad Postgresem a nechce překlápět celý stack, má tak další lehkou zastávku k vyzkoušení.
