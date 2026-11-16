# 50029123
**Zranitelnost Telegram Desktop umožnila krádež souborů na jeden klik**

Hacker News · g-b-r · 10. října 2026, 05:02 · 436 bodů / 277 komentářů · [diskuse](https://news.ycombinator.com/item?id=50029123)

Bezpečnostní výzkumník popsal řetězec, kdy stačilo přidat oběť do skupiny a přimět ji kliknout na zdánlivě nevinný odkaz. Kliknutí vedlo ke čtení libovolného souboru přístupného uživateli a jeho odeslání do útočníkova chatu, v krajním případě k plnému převzetí účtu Telegramu. Chyba se týkala Telegram Desktop do verze 7.2.8 a dostala označení CVE-2026-107181 se závažností 8,1.

Odkazovaný rozbor ukazuje dvě navazující vady. Telegram po kliknutí předává odkaz už běžící instanci přes lokální socket jako text ve formátu s příkazy oddělenými středníkem, jenže středník uvnitř samotného odkazu nijak neescapuje, takže se jeden odkaz na druhé straně rozpadne na několik příkazů. Vstříknutý příkaz pak míří na interní schéma interpret:, pozůstatek nástroje pro publikování vlastních verzí, který bez potvrzení a bez kontroly přečte soubor popsaný v instrukčním textovém souboru a pošle ho do zvoleného kanálu či supergroupu.

Autor příspěvku na Hacker News link znovu vystavil právě kvůli tomuto přesahu: původní titulek mluvil jen o převzetí účtu, ale krádež jakéhokoli souboru mu přišla pozoruhodnější. Nejvíc ho zarazilo, odkud se nebezpečná funkce vzala, tedy že si vývojáři pro vydávání releasů zabudovali do klienta mechanismus, který na povel nahraje kamkoli libovolný soubor. Diskuse na to navázala vtipy, že to není chyba, ale funkce, a uživatel arjie to označil za funkci na úrovni JiaTan, tedy šílenou, ale s věrohodným popřením.

Z toho se rozvinul spor, zda jde o chybu Telegramu, nebo všech moderních desktopových systémů, kde každý proces vidí na soubory uživatele. Uživatel Panzerschrek prosazoval druhou verzi a volal po izolaci programů, ale g-b-r oponoval, že Telegram soubory potají sám nahrává na cizí účet, a nvme0n1p1 dodal, že za normální nelze považovat ani vynesení databáze zpráv. Uživatel lxgr připomněl, že aplikace si dnes mohou samy omezit následky takové chyby, jen to musí udělat, a další hlasy řešily sandbox na macOS, unveil na OpenBSD či spouštění Firefoxu ve firejail s přístupem jen do složky se staženými soubory.

Paralelně se vrátila stará nedůvěra k Telegramu jako takovému. Zaznělo, že protokol a architektura jsou kritizované už dekádu, včetně odkazu na text Filippa o podivné implementaci ECDH, i že služba visící na telefonním čísle s defaultně vypnutým dvoufázovým heslem působí směšně. Uživatel sunaookami to mírnil tím, že o novém přihlášení přijde upozornění a čerstvá session má omezení, uživatel misiek08 pak přiznal, že spousta lidí zůstává kvůli pohodlí a pocitu, že pro běžného člověka je sběr dat reklamními firmami horší hrozba.

Kdo neaktualizoval na verzi 7.2.9, která schéma interpret: ruší a oddělovač na socketu escapuje, tomu rozbor jako nouzová opatření radí vypnout automatické stahování, omezit přidávání do skupin jen na kontakty a nastavit si lokální heslo.
