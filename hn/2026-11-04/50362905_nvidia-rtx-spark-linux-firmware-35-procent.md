# 50362905
**Nvidia RTX Spark na Linuxu: firmware zamkne GPU na 780 MHz a inference spadne na 35 %**

Hacker News · novaRom · 4. listopadu 2026, 09:46 · 597 bodů / 276 komentářů · [diskuse](https://news.ycombinator.com/item?id=50362905)

Linux na laptopu s Nvidií RTX Spark, například MSI Prestige N16 Flip AI Plus, normálně naběhne včetně akcelerace grafiky přes otevřený kernel driver. Jakmile se ale stroj připojí k síti, grafika se zamkne kolem 780 MHz místo více než 2 GHz ve Windows a model se 120 miliardami parametrů tak spadne zhruba z 65 na necelých 14 tokenů za sekundu.

Odkazovaný test popisuje zdlouhavou instalaci přes Debian a distribuci Omarchy, po které běží desktop ve 4K na 120 Hz i CUDA, jen Linux vidí nejdřív jen 28 GB ze 128 GB sjednocené paměti, protože zbytek si firmware rezervuje pro grafiku a povolit jde jen z Windows. Na vině je komponenta Nvidia Platform Controllers and Framework, která řídí společný napájecí rozpočet procesoru a grafiky a jejíž šifrovanou tabulku umí rozluštit jen windowsový ovladač, takže praktickým kompromisem zatím zůstává WSL jedoucí nad windowsovým stackem téměř plnou rychlostí.

Nejživější debata se hned na začátku stočila k názvu. Čtenáři upozorňovali, že titulek mluví o DGX Sparku, zatímco problém se týká jen laptopové RTX Spark, protože desktopový DGX Spark má Linux od Nvidie rovnou z výroby. Autor podnět přijal a titulek opravil, což část diskutujících brala jako důkaz, že si redakce plete dvě dost odlišné platformy.

Jádro podezření shrnul rich_sasha obavou, že z dnešní chyby se zítra stane placená brána na lokální modely, a další hlasy přidávaly historické paralely s omezením počtu hardwarových video streamů na GeForce. Proti tomu stojí střízlivější výklad, že Nvidia jen tradičně kašle na linuxový desktop a šifrovanou správu napájení prostě nikdy neportovala, jak píše FartyMcFarter s odkazem na Hanlonovu břitvu. Podobně to vidí GuB-42: nejde o válku proti lokální inferenci, ale o klasickou segmentaci trhu, kdy se firemní zátěž na levnějším hardwaru uměle přibrzdí.

Zvláštní vlákno se rozvinulo kolem otázky, proč vůbec honit velké modely na notebooku, když doma může běžet malý server přístupný přes Tailscale. Odpovědi se sešly u soukromí a kontroly: lokálně nikdo neposílá data cizí firmě, nikdo neplatí kvóty a nikdo nemění podmínky pod rukama, jak píší spaceywilly a alerighi. Někdo připomněl i méně pohodlnou stránku věci, že stabilní domov s rychlým internetem nemá každý a notebook, který má člověk u sebe, mu nikdo nevezme.

Z toho plyne pro zájemce o RTX Spark jednoduché poučení: kdo chce nativní Linux, musí zatím počítat s pětinovou rychlostí na kabelu a čekat, až Nvidia přenese správu napájení do linuxového ovladače, do té doby dává největší smysl dual-boot s upravenou pamětí a běh přes WSL.
