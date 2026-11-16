# 50337716
**LongCat-2.5 od Meituanu sází na nativní multimodalitu pro agentní úlohy**

Hacker News · pretext · 2. listopadu 2026, 16:00 · 82 bodů / 22 komentářů · [diskuse](https://news.ycombinator.com/item?id=50337716)

Meituan představil LongCat-2.5 jako model stavěný primárně pro agentní úlohy. Namísto slepování oddělených textových a obrazových částí sází na nativní multimodalitu, která má lépe zvládat práci s nástroji, kódem a webem.

Odkazovaný blog na longcat.ai ho staví do grafů vedle GPT-5.5, GPT-5.6-Sol a Claude-Opus 4.8 a 5 a slibuje výkon srovnatelný s DeepSeek-V4.1 Flash za stejnou cenu. Láká i na kontextové okno kolem milionu tokenů, kde mají rozhodovat rychlost a úspěšnost cache. Samotné grafy ale podle čtenářů působí odbytě, prý jsou špatně obarvené a zvýrazňují jen vlastní model.

Nejživší linka se ale netýká benchmarků, nýbrž toho, jak se k modelu vůbec dostat. Uživatel embedding-shape popisuje, že odkazy na GitHub a HuggingFace končí jen vágním slibem brzy, bez vysvětlení, zda budou ke stažení váhy a zda budou otevřené. Chat na longcat.ai ho navíc přesměroval na přihlášení přes passport.mykeeta.com, což mu přišlo podezřelé, a na pozdrav dostal představení asistenta vyvinutého Meituanem v mandarínštině. Po dalších pokusech model podle něj jen zběsile vyhledával na webu význam slova co a působil překvapivě hloupě, takže celé vydání označil za honbu za benchmarky vypuštěnou ven příliš rychle.

Na to navazují další zkušenosti s webovým ovládáním. Uživatel vfosnar líčí, že mu ve Firefoxu psaní skákalo na začátek řádku a po odeslání pozdravu model spustil 25 vyhledávání, takže za problém označil mizerný webový harness. Uživatel nmfisher připomíná, že minulý model se dal levně zkoušet v podobě velkého balíku tokenů asi za dva dolary a na běžnou rutinní práci stačil, jenže pak firma začala nutit přihlášení do konzole přes aplikaci Meituanu, a tam to pro něj skončilo. Dodává, že Keeta je zřejmě mezinárodní značka Meituanu, takže přesměrování na mykeeta.com dává smysl, z pohledu přívětivosti je to ale bída. Uživatel swiftcoder naopak poznamenává, že preview verze byla pár týdnů zdarma na OpenCode a na jednoduché programovací úkoly rozhodně fungovala.

Samostatný spor se vede o to, proč blog srovnává s několik měsíců starými verzemi konkurence bez vysvětlení. Uživatel BugsJustFindMe to považuje za neprůhledné a chtěl by pravidlo proti zastaralým srovnáním bez udání důvodu, zatímco další namítají, že právě to přesněji ukazuje schopnosti a že preview vyšlo už 25. září 2026, takže volba tehdy dávala smysl. Praktičtější test přidal uživatel InsideOutSanta, jemuž model zaplnil 200 tisíc tokenů za pět minut a v druhém vláknu držel kolem 80 tokenů za sekundu, takže mu zatím přijde rychlý. Uživatel colingauvin to shrnuje tak, že přes API vypadá konkurenceschopně, ale doma nedává smysl proti DeepSeek-V4.1 s polovičními parametry, a uživatel flr03 si jen rýpnul, že kočka, která není model od Mistralu, mate.

Z diskuse tak LongCat-2.5 vychází jako papírově slibný a levný pracant pro agenty, jehož největší slabinou je zatím přístup a prezentace.

[Zpět na index](00-index.md)
