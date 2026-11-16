# 50172041
**PHP chystá kritickou opravu dvou RCE zranitelností**

Hacker News · xd · 20. října 2026, 22:15 · 309 bodů / 112 komentářů · [diskuse](https://news.ycombinator.com/item?id=50172041)

PHP tým ohlásil mimořádnou bezpečnostní verzi, která vyjde ve středu 21. října 2026 ve 14:00 UTC. Oznámení přišlo nezvykle předem a naznačuje, že situace je vážná a správci by měli být připraveni aktualizovat okamžitě po vydání.

Odkazované oznámení mluví o dvou kritických zranitelnostech s hodnocením CVSS v4.0 9,2. Tým zároveň varuje, že verzi vydá dřív, pokud se detaily dostanou na veřejnost nebo se objeví důkazy o aktivním zneužívání.

Diskuse se od začátku točí kolem videa, které koluje po síti X. Uživatel Gigachad popisuje, že stačí vložit něco do adresního řádku a útočník získá na serveru shell, a radí do vydání opravy servery prostě vypnout. Uživatel ndiddy upřesňuje průběh: útočník spustí python skript, přiměje PHP vykonat libovolný příkaz a důkazem je nápis „pwned" zapsaný na veřejně dostupné místo, které pak ukáže obnovení stránky v prohlížeči. Podobně uživatel enews01 píše, že z opatrnosti dočasně vypnul svůj web s MediaWiki, protože záběry vypadají děsivě.

Nejživější linka řeší provizorní ochranu. Objevila se rada vypnout v php.ini volbu session.upload_progress.enabled, případně i file_uploads. Uživatel lynndotpy ale upozorňuje, že to PHP oficiálně nedoporučuje jako náhradu opravy, a uživatel robwayne dodává s odkazem na jednoho z vývojářů jádra, že opatření je nedostatečné. Do toho uživatel jeffbee připomíná obranu do hloubky, třeba zakázání funkce system nebo běh bez shellu a souborového systému, jenže uživatel Operyl oponuje, že jde o RCE chybu a exploit chain vedoucí k vykonání libovolného kódu, takže vypnutí php funkcí nepomůže.

V pozadí visí otázka, kterých verzí se to týká. Uživatel gnabgib cituje dřívější zprávy, že zranitelnosti mohou sahat od PHP 5 přes šestku a sedmičku až po osmičku, což odpovídá i dřívějšímu vláknu Tell HN o dvou RCE s hodnocením CVSS 10,0. Právě rozdíl mezi tehdy zmiňovanou desítkou a nyní oficiálně uváděných 9,2 v diskusi několikrát zaznívá. Jinak převládá obava z rozsahu dopadů: uživatel philipwhiuk předpovídá masakr neudržovaných instalací WordPressu na LAMPU, uživatel bakugo spekuluje, že by to mohlo být horší než Log4Shell, a uživatel redox99 varuje, že s jazykovými modely zvládnou agenti během hodin napadnout desítky tisíc webů.

Závěr vlákna patří frustraci z čekání. Uživatel bwoebi vysvětluje, že vydání dělá jen hrstka lidí, kteří zrovna spí, a únik videa je prý důvodem, proč oznámení vůbec vyšlo v tento čas. Mnohem rychlejší únik exploitu ho přitom překvapil. Vedle volání, aby se oprava vydala hned, tak zůstává rada, která se opakuje nejčastěji: mít všechno připravené a aktualizovat v minutě, kdy to vyjde.
