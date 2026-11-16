# 50218277
**Indické vládní weby dál vydávají revokované eMudhra certifikáty**

Hacker News · adityaathalye · 24. října 2026, 06:05 · 51 bodů / 22 komentářů · [diskuse](https://news.ycombinator.com/item?id=50218277)

Sedmnáctého října se ukázalo, že osm mezilehlých autorit firmy eMudhra navázaných na kořen emSign ECC Root CA - G3 má triviálně obnovitelné soukromé klíče. Druhý den byly certifikáty revokovány a Mozilla s Chromem tomuto kořenu přestaly důvěřovat, o den později firma z důvodu „Superseded“ zneplatnila i 9 356 certifikátů v dosud důvěryhodné RSA hierarchii G1. Řada indických vládních webů přesto zneplatněné certifikáty dál nabízí, zatímco ministerstvo elektroniky a IT dopady zlehčuje.

Autor odkazovaného blogu rozebírá prohlášení ministerstva z 21. října, podle kterého byl dopad velmi omezený a trval velmi krátce. Namítá, že vadné klíče vznikly už v dubnu 2025, takže je mohl kdokoli osmnáct měsíců zneužívat, a že kvůli nedůvěře ke kořenu G3 musí eMudhra migrovat odhadem 30 tisíc certifikátů, z nichž většina patří americkým univerzitám přes InCommon. Jeho vlastní sken z 24. října našel 1 377 indických vládních domén na revokovaných certifikátech, z nichž 811 revokovaný certifikát stále podává, včetně vízových portálů, ministerstva vnitra, stipendijních či volebních webů a čtyř úřadů přímo pod zlehčujícím ministerstvem.

Nejostřeji zní hlas samotného zadavatele diskuse adityaathalye, který jako občan mluví o zločinné míře neschopnosti veřejné firmy, jež sama způsobila mezinárodní ostudu a doma nic neopravila. Diví se, že vedení eMudhry ani ministerstvo nevyhlásilo nouzový režim a nevyměnilo vše ve vlastním domě, a uživatel zombocomvibes k tomu dodává, že pokud je firma dobře napojená na vládní BJP, žádné následky nebudou.

Z toho se rozvinula hádka o pracovní kultuře. Uživatel cluckindan tvrdí, že v Indii vládne kultura přitakávačů, kde nikdo neklade otázky, všichni všemu rozumí, a přitom nerozumí ničemu, takže se věci dělají z rituálu a země je tak trochu nákladním kultem. Uživatel leonidasrup oponuje, že tak velkou zemi nelze házet do jednoho pytle, a připomíná Čándrasekhara, Rámana, Rámanudžana a Bhabhu, zatímco uživatel drutaTushar hledá příčinu spíš v socialistických politikách a přežívání v práci než v povaze, která je podle něj jinak hádavá a zvídavá.

Technická linka řeší, zda zjištění ještě platí. Uživatel mirages tvrdí, že je zastaralé, protože spousta webů už jede z kořene G1, který revokován ani kompromitován nebyl. Uživatel sprinter123 ale odpovídá, že zastaralé není, protože mnoho webů dál podává revokované certifikáty a ve Firefoxu ani v opraveném cURLu je nenačte. Mezi tím problesknou ironie o tom, že se to stává jen v Indii, a návrh přeříznout podmořské kabely, na který další diskutující suše připomíná, že Indie je obklopená i pevninou.

Z diskuse tak zůstává obraz průšvihu, který Firefox pozná a odmítne, zatímco Chrome či Safari ho mlčky pustí dál.
