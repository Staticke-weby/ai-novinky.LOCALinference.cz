# 50560461
**OpenAI sází na WebRTC. Pro hlasové AI je to stále problém**

Hacker News · surprisetalk · 19. listopadu 2026, 15:20 · 94 bodů / 28 komentářů · [diskuse](https://news.ycombinator.com/item?id=50560461)

Hlasové funkce od OpenAI stojí na WebRTC, tedy na protokolu vymyšleném pro konferenční hovory mezi lidmi. Autor odkazovaného blogu tvrdí, že právě v tom je zakopaný pes: síť drží zpoždění u nuly tím, že nemilosrdně zahazuje opožděné zvukové pakety, a při běžném výpadku se tak z otázky na hlavní město Francie stane nesrozumitelný útržek.

Blog to rozebírá na retransmisích a vyrovnávacích pamětech. Opakované poslání zvuku je ve výchozím stavu vypnuté a jitter buffer na něj ani nečeká, záložní kopie v rámci Opusu kryje nanejvýš jeden ztracený rámec. Místo záplatování WebRTC autor tlačí Media over QUIC, který pošle všechno hned a přehrávač si zvuk podrží v paměti podle časových značek, takže má na opravy sekundy času; řešení už prý podporuje i Pipecat.

Do diskuse se vložil Sean-Der, který na hlasových systémech pracuje. Odmítá, že by se WebRTC zvuku vzdávalo: přijímač má k dispozici NACK a sám rozhoduje, jestli mezeru v tocích přijme, nebo si řekne o opakování. Pro převod řeči na řeč prý počítá s úseky po 20 a 200 milisekundách a žádné velké buffery nechce, vadí mu ale hlavně to, že se v kritice míchá dohromady protokol, software a prohlížečové rozhraní, což přirovnává k útoku na HTTP kvůli nastavení jednoho serveru.

Zbytek vlákna se přetahuje o to, jestli je text spíš analýza, nebo prodejní leták. Tschellenbach namítá, že posílání syntetického hlasu rychleji než v reálném čase naráží na skákání do řeči a vyžaduje chytřejší logiku na straně klienta, zatímco opakování už WebRTC umí přes NACK, FEC a Opus RED. Podobně FLeXMurphy shrnuje text jako zdlouhavou reklamu na MoQ a fidotron vyčítá jeho autorům, že ignorují důvody, proč výchozí nastavení vznikla, a jen znovu objevují staré pravdy.

Nechybí praktické odbočky ani humor. Na otázku jpterryho, jestli by volba TCP v popisu relace většinu potíží nevyřešila, Sean-Der odpovídá, že mezi UDP a TCP lze přepínat i uprostřed hovoru. Návrh na lokální rozpoznávání v nativních aplikacích sráží argumentem o velikosti modelů s nárokem přes 256 GB paměti, zatímco ernestrc se u článku baví, směrově s autorem souhlasí a WebRTC popisuje jako bolestivý, ale obdivuhodný kus inženýrství.

Čtenář si tak odnáší prostý spor o latenci a spolehlivost: co je pro lidský hovor otrava, může být pro model cenný čas na opravu chyby.

Zpět na [denní přehled](00-index.md).
