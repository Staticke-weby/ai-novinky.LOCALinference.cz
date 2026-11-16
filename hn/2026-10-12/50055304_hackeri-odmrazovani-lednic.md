# 50055304
**Hackeři spustili odmrazování lednic v evropských supermarketech**

Hacker News · Zeekaas · 12. října 2026, 14:16 · 524 bodů / 712 komentářů · [diskuse](https://news.ycombinator.com/item?id=50055304)

V noci na pondělí zasáhl francouzské supermarkety kyberútok mířící na chladicí techniku. Zasaženy jsou prodejny řetězců Intermarché, Leclerc a Coopérative U, u Intermarché se v podkladech mluví zhruba o 150 prodejnách. Prezident Coopérative U Dominique Schelcher útok potvrdil a označil ho za mimořádně závažný a bezprecedentní.

Odkazovaný článek popisuje, že terčem jsou regulátory chlazení od firmy Danfoss. Funkce automatického odmrazování, která normálně běží jen asi dvě hodiny denně, byla přepnuta do nepřetržitého režimu s teplotou nastavenou na 50 stupňů, ze skříní se podle svědků valila vlna horka. Škody se zatím odhadují na blížících se 300 tisíc eur, celostátně ale mohou dosáhnout několika milionů, souběžně v Nizozemsku hlásí Albert Heijn, Etos a Gall & Gall výpadky webů, rozvozu i elektronických cenovek a problémy má i belgický Delhaize.

V diskusi mělo největší ohlas déjà vu. Uživatel kotaKat připomněl, že před měsícem či dvěma postihl stejný scénář americké vojenské prodejny, kde prý všechna mrazicí zařízení přešla do odmrazování a všechno mražené jídlo se zkazilo. Uživatel black6 dodal, že to mělo být pro všechny ostatní varováním, a uživatel bastard_op poznamenal, že jde zřejmě znovu o stejné regulátory Danfoss, které technici klimatizací vystaví na internet bez znalostí síťové bezpečnosti a k jejich ovládnutí pak stačí triviální zneužití známé zranitelnosti.

Jádro hádky tvoří otázka, proč je chlazení vůbec připojené k internetu. Uživatel ex-aws-dude se ptá, k čemu je vzdálené odmrazování, když k vyložení lednice stejně musí někdo fyzicky přijít, a uživatel lemoncookiechip navrhuje oddělit vzdálený dohled od samotného řízení. Proti tomu uživatelé Delphiza a quickthrowman vysvětlují, že u velkých prodejen nejde o domácí lednici, ale o soustavu kompresorů, výparníků a čidel, kde dává smysl hlásit poruchu, hlídat teplotu nebo šetřit energii po zavíračce. Chyba podle nich není v připojení jako takovém, ale v tom, že je na síti přímo řízení s webovým serverem bez aktualizací, místo pouhého monitoringu.

Nejživější historku přidal uživatel Kevin_Flynn o servisní smlouvě: firma na chlazení slíbí vzdálený dohled a levnější kontrakt, řetězec s dvouprocentní marží kývne a bezpečnost sítě tak fakticky skončí u techniků, kteří nejsou síťoví specialisté. Vedle toho se řeší širší souvislosti, od hybridní války přes výzkum zranitelností regulátorů Danfoss od týmu Claroty až po obavy, že s dostupnější umělou inteligencí bude takových snadných cílů přibývat. Uživatel Lyngbakr to shrnul pocitem technologického bručouna, když jeho švagrová nadšeně vyprávěla o fritéze ovládané aplikací a on v tom viděl jen zbytečné riziko a sběr dat.

Poučení z vlákna je prosté: připojovat průmyslové řízení na síť bez promyšleného oddělení dohledu a ovládání se u drahých a citlivých zařízení nevyplácí.
