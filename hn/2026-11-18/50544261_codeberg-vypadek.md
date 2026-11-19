# 50544261
**Codeberg zmizel z DNS. Výpadek oživil debatu o závislosti na jedné službě**

Hacker News · hans_castorp · 18. listopadu 2026, 11:02 · 299 bodů / 301 komentářů · [diskuse](https://news.ycombinator.com/item?id=50544261)

Neziskový evropský hostitel kódu Codeberg.org byl 18. listopadu zcela nedostupný, doména dokonce zmizela z DNS. Pro projekty, které na něm stavěly jako na nezávislé alternativě ke GitHubu, to znamenalo, že se ke svému kódu najednou vůbec nedostaly.

Odkazované oznámení týmu Codebergu popisuje, že doména byla registrovaná u společnosti Namesilo a z účtu beze stopy zmizela. Později tým dostal potvrzení, že doména byla pozastavena a případ byl předán týmu pro zneužívání, na jehož konečné rozhodnutí se čekalo.

Na Hacker News se k výpadku objevily hned dvě diskuse, hlavní z nich přilákala přes tři stovky komentářů. Nejživější linka se ptá, proč německý spolek, který si zakládá na provozu výhradně v Evropě, sáhl po americkém registrátorovi. Uživatel antonvs se podivuje, proč lidé svěřují něco důležitého takovým malým firmám, layer8 a MrGilbert se diví, že organizace nemá pro tak kritickou věc lokální kontakt, a PaoloBarbolini doufá, že evropské služby přestanou být závislé na amerických koncovkách. Oponuje jim alexdns s tím, že nemá smysl dělat z toho otázku země, protože německé registry prý pozastavují domény stejně ochotně, a eloy připomíná, že koncovku .org stejně spravuje americká organizace Public Interest Registry.

Druhá velká debata řeší, jak se proti takovému selhání vůbec bránit. Uživatel octoberfranklin to shrnuje otázkou, zda se má služba s vysokou dostupností stát vlastním registrátorem, a firen777 označuje registrátora za zneužitelný jediný bod selhání. Uživatel partsch vypráví, že mu minule registrátor bez varování pozastavil účet a za obnovu chtěl 90 eur za doménu, a ptá se, zda má firma kvůli tomu držet záložní domény u jiného registrátora a na jiné koncovce, řešit záložní poštu a aplikace – a končí povzdechem, že by chtěl být instalatérem. Praktické tipy přidává smallnix s dotazem na náhradní doménu či záznam v hosts, ivanjermakov namítá, že architektura DNS je díky distribuci odolná, pokud se člověk nespolehne jen na jeden server bez zálohy.

Ozývá se i zklamání těch, kteří na Codeberg přesouvali projekty z GitHubu. Uživatel syngrog66 popisuje Codeberg jako svou zálohu při útěku před lumpárnami GitHubu a Microsoftu, manarth mu radí, že při lokálním hostování je dobrou volbou Forgejo, a cowlevel nabízí přepsat si adresy v hosts a hlavně se nevracet k velkým technologickým firmám, které za tohle prý mohou. Do toho vstupuje spor o zákaz příspěvků z umělé inteligence, kvůli kterému část lidí Codeberg opouští, a glosa o zákazu prázdného subredditu r/Codeberg, který podle archivu nevykazoval žádnou aktivitu a nejspíš ho kdysi převzali spamoví boti.

Z výpadku tak zůstává hlavně poučení, že i decentralizovaná alternativa může spadnout na jednom centralizovaném místě – u registrátora domény.
