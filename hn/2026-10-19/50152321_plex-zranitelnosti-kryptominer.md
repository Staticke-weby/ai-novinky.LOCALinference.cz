# 50152321
**Plex zranitelnosti zneužívané k těžbě kryptoměn**

Hacker News · mindracer · 19. října 2026, 15:36 · 186 bodů / 91 komentářů · [diskuse](https://news.ycombinator.com/item?id=50152321)

Uživatel mindracer odkázal na zápis provozovatele honeypotu o živém zneužívání starších verzí Plex Media Serveru. Po zářijové bezpečnostní výzvě k aktualizaci a říjnovém zveřejnění řetězení chyb s názvem plex2shell se podle něj objevily první útoky na nezaktualizované servery. Diskuse se rychle stočila k tomu, kdo má takový server vůbec vystavený do internetu.

Autor blogu sledoval zranitelnou instalaci od začátku září a ráno 17. října zachytil pokusy končící stažením podezřelého souboru z cizí adresy. Uvnitř byl kryptominer, v pozdější aktualizaci doplněný o nástroj myawesomeproxy a program xmrig. I relativně nudný miner je podle něj nebezpečný, protože domácí server s rezidenční adresou se hodí jako proxy pro přístup ke korporátním sítím a e-mailům.

Nejživější přestřelka začala u povzdechu foobarian, že představa serverů otevřených do internetu je děsivá a kdo tohle dělá. Odpovědi se jen hrnuly: dewey připomněl, že televize a kamarádi se musejí nějak připojit a nikomu se nechce vysvětlovat Tailscale, symlinkk dodal, že Plex vystavení do sítě sám doporučuje a dokonce ho vyžaduje varovnou ikonou. Uživatel ppchain to shrnul, že jde o zamýšlený způsob použití pro sdílení s rodinou a přáteli, od kterých nelze čekat nasazení tailnetu, podobně blntechie píše o tunelech přes Cloudflare a bigstrat2003 o streamování hudby do telefonu na cestách.

Řada lidí pak popsala, že je miner už navštívil. Uživatel iamjackg přiznal, že přehlédl e-mail z 1. září a jel třináct měsíců starou verzi, server vyskočil na stoprocentní vytížení a škodlivý proces se jmenoval mylovelyminer. Uživatel xavdid si na mac mini všiml přetočených ventilátorů a procesu icloud-services na sto procentech procesoru, po restartu našel složku s odkazem na moneroocean, i když Plex měl aktuální a pozadu byl jen systém. Uživatel leptons poznal napadení podle neustálého bufferování vlastních rádiových stanic a s opravou na linuxovém serveru mu pomohla umělá inteligence, freedomben zase ocenil minery, kteří se ani nesnaží skrývat.

Závěrem se vlákno odklonilo k nedůvěře vůči samotnému Plexu. Uživatel coreyburnsdev si stěžuje, že nové rozhraní je mimo prohlížeč na počítači nepoužitelné a pomalé, další si pochvalují staré verze aplikací nebo alternativní klienty. Uživatel TacticalCoder popisuje opačný přístup: věří jen datům, Jellyfin pouští v dočasném kontejneru se svazkem jen pro čtení a po dokoukání filmu kontejner prostě smaže.

Kdo provozuje Plex přístupný zvenčí, měl by zkontrolovat aktualizace a vytížení serveru, útok je podle popisovaných zkušeností poznat překvapivě rychle podle hluku a zpomalení.
