# 1xsg8bv
**Patnáct megabajtů a vlastní Netflix. Media server vznikl s Claudem**

r/ClaudeAI · u/CoderLuii · 10. listopadu 2026, 07:57 · 675 bodů / 131 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xsg8bv/)

Vývojář Luis vydal HolyArrs, bezplatnou aplikaci pro domácí mediální server velkou jen kolem 15 MB, kterou z velké části napsal s Claude Code. Jediný program v kabátě připomínajícím Netflix má nahradit šestici nástrojů pro hledání a stahování filmů, seriálů a hudby a napojuje se na to, co už lidé doma mají, tedy na stahovače typu qBittorrent a přehrávače typu Plex, Jellyfin nebo Emby. O minulou ukázku byl takový zájem, že se v čekajícím subredditu sešlo přes tisíc lidí, a nová verze je teď venku jako beta.

Největší potlesk sklidila právě ta lehkost. u/Filipehdbr píše, že skutečným titulkem je spotřeba kolem 70 MB paměti, protože samotný Sonarr toho prý sní víc, než se vůbec stihne spustit. Sám autor popisuje divokou startovací noc: lidé na Discordu hlásili chyby i s přesným souborem a řádkem, kde to spadlo, takže verze 1.0.1, 1.0.2 a 1.0.3 vyšly během čtyř hodin, a když si někdo řekl o ukrajinštinu, web i dokumentace ji měly do hodiny. Svůj postup shrnuje prostě: on navrhne a napíše specifikaci, většinu kódu napíše Claude Code, druhý agent ho zkontroluje a pak to sám projde a otestuje na vlastním serveru.

Zároveň se rychle nasčítal seznam podmínek pro přechod. u/Outrageous_Song_484, který si postavil podobný projekt přezdívaný Notflix, se ptá, jestli se videa překódují a vyrábějí varianty pro různé pásmo v SDR a HDR. u/ortius84 projekt chválí, ale vadí mu, že plakáty a vyhledávání leží na autorově placeném metadata serveru, a raději by si vybral vlastního poskytovatele metadat. Nejčastěji se ale vrací podpora Torboxu a Real-Debridu, k tomu cizojazyčné titulky a dabing, o které stojí u/Sir_Leon_BN001, a dotazy na knihy, audioknihy či podcasty.

Do debaty vstoupilo i varování před únavou z umělé inteligence. u/Xarishark připomíná projekt, který kvůli nenávisti kolem bezpečnosti a použití AI autor nakonec smazal, a radí s tímto tématem opatrně hlavně v tradičních komunitách kolem arr stacku. Luis na to odpovídá zkušeností z více než deseti let v bezpečnosti: všechno kolem klíčů, přihlašování a sítě četl řádek po řádku a před vydáním proběhl plný pentest, přičemž dál drží pravidlo, že změna, která aplikaci nafoukne, nevyjde. Praktičtější přání přidává u/typical-predditor, který by do kontejneru přibalil ještě yt-dlp pro stahování webových videí do offline knihovny.

Kdo má doma sbírku rozházenou v několika nástrojích, dostal ochutnávku toho, že by to šlo i v jednom lehkém okně s trailery po najetí na plakát.
