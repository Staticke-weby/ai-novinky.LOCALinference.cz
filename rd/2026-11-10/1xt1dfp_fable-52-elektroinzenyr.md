# 1xt1dfp
**Fable 5.2 jako elektroinženýr. Uživatel ukázal návrh obvodu**

r/ClaudeAI · u/ScarionnS · 10. listopadu 2026, 23:56 · 406 bodů / 68 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xt1dfp/)

Fable 5.2 si podle autora sáhl na pořádnou elektrotechnickou práci. Na šestivrstvé desce vedl HDMI pro 4k, DDR3, rychlé USB i FPGA, návrh ověřil elektrickou simulací, opravil chyby ve stopách, poklesy napětí a cenu kusovníku srazil o 44 dolarů za desku. Ten pocit přirovnává k okamžiku, kdy poprvé viděl kódovat Opus 4.6, desku chce poslat do výroby a o výsledek se podělit.

Největší ohlas v diskusi má ale podrobná kritika od u/Natural_Explorer_694. Vadí mu přerušená zemní plocha v místě, kde vedou prokovy v řadě u U19 a VTT, špatné rozvržení zakončení DDR i zbytečně velké kondenzátory místo několika menších paralelně pro nižší impedanci u FPGA. Regulátor zakončení DDR by podle něj potřeboval mnohem víc mědi a prokovů do plochy, rozložení USB je prý podivné a oscilátor by k USB kabelu nikdy nedával. Závěr zní dost tvrdě: jen z viditelného se rýsuje řada vážných problémů s rušením a do testů elektromagnetické kompatibility jde návrh s velmi vysokým rizikem.

Právě tahle výtka určila tón zbytku vlákna. Vtipně ji shrnul u/daniel hláškou o tom, že se omlouvá, že dotyčnému shořel dům, a u/FreXxXenstein se ptá přímo, jestli to vůbec bude fungovat, protože hezky vypadající desky umí modely už dlouho. Připomíná, že Anthropic v oznámení mluvil o třech zařízeních od Fable, ale bez důkazu, že fungují, bez videa a bez čehokoliv dalšího je to podle něj zbytečné.

Druhá linka diskuse je praktická: jak to autor udělal a v čem. u/pearfire575 se ptá na postup a použitý návrhářský program, u/ineedanamegenerator prosí o popis pracovního postupu a nástrojů. Nejkonkrétnější odpověď dává u/Miserable_Escape_146, který podobnou desku skoro dokončil od začátku do konce: na počítači mu běží Claude Code s téměř plným přístupem, krok za krokem prošel schéma, osazování, spoje i stopy včetně vlastních, po každé relaci vše zkontroloval a poradil, jak dál, stačí prý KiCAD a Claude Code. K tomu se přidávají zkušenosti s jednoduššími deskami, třeba u/kdawg89 píše, že pár mnohem jednodušších desek z Opus 5.5 s KiCAD a volným routerem mu funguje perfektně, zatímco u/onahorsewithnoname to přirovnává k začátkům Claude při kódování: detaily nic moc a zbytečně překombinované, ale tenkrát se to také rychle zlepšovalo.

Rozhodnutí, jestli desku poslat vyrobit, tak komunita bere jako test pravdy. u/delabay autora povzbuzuje, ať to postaví, že se hodně naučí a možná ušetří týdny, u/devaspark mu přeje hodně štěstí při stavbě a zajímají ho výsledky, jen varuje před tenkými napájecími spoji a souběžným vedením, které může přinést šum.
