# 1x3yeti
**Linus Torvalds použil LLM a našel čtyři chyby v jádru Linuxu**

r/singularity · u/PointmanW · 12. října 2026, 12:34 · 982 bodů / 192 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1x3yeti/)

Nils Ollrogge nahlásil chybu v knihovně assoc_array a přiložil i návrh opravy, jenže Torvaldsovi připadal ten kód příliš zamotaný na to, aby ho rozplétal ručně. V tagu assoc-array-fixes proto napsal, že udělal to, co káže, a sáhl po moderních nástrojích LLM. Vznikla tak asistovaná větev, která rozsekala velké nepřehledné funkce na čitelnější celky, a testovací program v uživatelském prostoru pak potvrdil původní hlášení a našel další tři chyby sahající až k prvnímu commitu knihovny z roku 2013.

Server Phoronix to zasazuje do širšího víkendového experimentování: Torvalds předtím s Claude Code připravil návrh zásadního vylepšení vstupně-výstupní cesty včetně testovacího programu a nový tag se objevil vedle odloženého vydání 7.3-rc7 a větve noref-filemap-read-with-llm. Připomíná, že assoc_array slouží v jádru jako implementace asociativních polí a že opravy se do hlavní větve zatím nedostaly, míří tak zřejmě do slučovacího okna verze 7.4.

Diskuse se nese hlavně ve znamení nadšení z toho, co se stane, když se k umělé inteligenci dostane někdo Torvaldsova kalibru. u/Different_Berry5015 píše, že takový člověk získává s umělou inteligencí multiplikátor a budoucnost je tady, nejvýše hodnocený u/141_1337 z toho vyvozuje, že se Linux stane nejlepším systémem vůbec. u/emptyharddrive dodává, že Torvalds dodává kódu generovanému umělou inteligencí tolik potřebnou důvěryhodnost: je to prý jen nástroj jako překladač, vždyť dnes také nikdo nepíše v assembleru.

Druhá linka řeší, v čem je tenhle postup vzorový. u/bugra_sa oceňuje tu nejméně efektní část: umělá inteligence Torvaldsovi pomohla přečíst kód, do kterého se mu nechtělo, ale on stále musel ověřit, jestli výklad sedí na skutečné chování jádra, což je něco jiného než přijmout uhlazené shrnutí jen proto, že zní dobře. Podobně u/chronographer poznamenává, že správci používající jazykové modely jsou dobrý nápad, zatímco u externích přispěvatelů to tak slavné není, a u/xrmb popisuje stejnou zkušenost s desítky let starým kódem ze své praxe. Do toho u/Roggieh rýpe do věčného sporu o neudržovatelný kód z umělé inteligence poznámkou, že možná jde jen o problém dovedností.

Nechybí humor ani skepse. u/TerribleFault7929 parafrázuje Torvaldsův vzkaz jako vibefix a dodává, že při pohledu na autora jsme vyřízení, u/FlyByPC na to reaguje popěvkem o devadesáti devíti broucích v kódu, z nichž po opravě jednoho je jich sto. Optimističtější tón vnáší u/buckzor122 s přirovnáním ke fázím smutku od odmítání přes připouštění až po nadšení z toho, co všechno je najednou možné, byť osamocený kritik u/billyhatcher312 nadává na odporný paskvil a s Linuxem se loučí.

Z vlákna tak zůstává hlavně obrázek umělé inteligence jako čtecího a úklidového nástroje pro zkušeného správce, ne jako náhrady za něj.
