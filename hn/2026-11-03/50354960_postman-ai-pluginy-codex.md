# 50354960
**Postman sám instaluje AI pluginy do Codexu a Claude Code**

Hacker News · sidgarimella · 3. listopadu 2026, 18:22 · 1151 bodů / 377 komentářů · [diskuse](https://news.ycombinator.com/item?id=50354960)

Běžné otevření Postman Desktopu 12.33.4 na Macu spustilo tichou instalaci do cizích vývojářských nástrojů: do Codexu přibyl plugin Postman 1.1.0 spolu se vzdáleným MCP napojením, startup hookem a uživatelskou konfigurací, vedle toho se objevil i plugin pro Claude Code a samostatné Postman CLI. Autor hlášení to označuje za vážný problém souhlasu a narušení důvěryhodné hranice – API klient si podle něj sám udělal výchozí cestu v nástrojích, kam mu nic není.

Odkazované hlášení s číslem 14370 v repozitáři postman-app-support dokládá průběh z vlastního logu Postmana, kde stojí auto-existing-upgrade s výsledkem claude-code:installed a codex:installed. Globální konfigurace Codexu se rozšířila o marketplace odkazující na GitHub Postmanu a o záznam důvěryhodného hooku, ten pak při startu relace přikazuje načíst dovednost postman:api-engineer před každým netriviálním API úkolem. Vzdálené MCP mířící na mcp.postman.com přitom končilo opakovanými chybami s vyžadovaným přihlášením a instalace sáhla i do nastavení Claude Code a do adresáře ~/.local/bin.

V diskusi se rychle ujalo přirovnání k malwaru. Postman se podle georgela změnil ze skvělého lehkého nástroje v nafouklou mašinu na vnucování dalších služeb a richwater ho rovnou popisuje jako téměř virus, po letech zhoršování se prý nelze divit, že ho ještě někdo používá. Podobně to vidí pants2, který připomíná cestu od výborné drobné pomůcky pro testování API přes nabrání více než 400 milionů dolarů a 1 500 zaměstnanců až k vynuceným přihlášením, sběru dat a předplatnému, přičemž pochybuje o ocenění přes 5 miliard, když už prý Postman nikdo z vývojářů v jeho okolí nepoužívá.

Nejživější praktická linka řeší, kam utéct. Waterluvian píše, že tu zbytečnost vyměnil za Insomnii už před lety, devmor a další chválí přechod celého týmu na Bruno kvůli jednoduchosti a ukládání kolekcí do gitu, amflare doporučuje Yaak jako návrat k pocitu jednoduchého klienta. Zároveň ale mzajc upozorňuje, že Insomnia od verze 8 vyžaduje účet na jejích serverech, a reddalo dodává, že právě proto je dnes lepší sázkou Bruno, i když se ozývá obava, že placená verze může časem sklouznout stejnou cestou jako Postman a Insomnia.

Za tím je širší debata o enshittifikaci. wolttam to shrnuje poznámkou, že takhle dopadne každá skvělá věc, jakmile se do ní zakousne rizikový kapitál, autoexec dodává, že je to jen otázka rychlosti, s jakou se začne mačkat z uživatelů víc peněz. aliasxneo namítá, že podobné firmy žijí hlavně z B2B smluv protlačených přes ředitele technologií a nařízeného interního používání, sneak kontruje právem na fork a představou neziskovky, která by z korporátních nástrojů vyřezávala antifeatury, a liendolucas celou věc uzavírá povzdechem, že by lidem stačilo curl a bash.

Kdo Postman otevře, měl by si pohlídat, co mu mezitím přepsal v Codexu a Claude Code – a zvážit, jestli API klienta s takovým chováním vůbec potřebuje.
