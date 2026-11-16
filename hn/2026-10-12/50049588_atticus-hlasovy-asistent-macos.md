# 50049588
**Show HN: Atticus – hlasový asistent pro macOS postavený na Claude**

Hacker News · SaarthRanka · 12. října 2026, 02:15 · 88 bodů / 16 komentářů · [diskuse](https://news.ycombinator.com/item?id=50049588)

Deváťák Saarth představil na Hacker News vlastního asistenta pro Mac jménem Atticus. Vyvolá se přidržením Control-Option-Space, pak stačí úkol vyslovit nebo napsat a po puštění kláves se rovnou vykoná. Projekt je zdarma a s otevřeným zdrojovým kódem.

Jednoduché požadavky jako otevření aplikace, přeskládání oken, hledání na webu nebo puštění hudby na Spotify se vůbec nedotknou umělé inteligence a hotové jsou typicky do vteřiny. Složitější zadání míří přes příkaz claude -p do Claude, takže stačí stávající předplatné Pro nebo Max a žádný API klíč. Atticus si z povedeného postupu uloží přesné kroky a příště je jen přehraje bez AI, navíc si pamatuje jméno, aplikace a pravidla typu „zapamatuj si…“. Před smazáním, odesláním, nákupem nebo zápisem do souboru si vždy řekne o potvrzení a příkazy jako rm nebo sudo má trvale zakázané.

Nejživější odbočka vlákna patří Windows. Uživatel FindlayH napsal, že nápad ho nadchl, o víkendu spálil nějaké kredity a portoval ho, včetně napojení na domácí služby jako Home Assistant, Jellyfin nebo Immich. Autor mu poděkoval, slíbil fork připnout do readme a zajímalo ho, na jaké problémy při portaci narazil. Vedle toho se handfuloflight ptal po podpoře OpenCode a blakeashleyjr sháněl něco podobného na Linux.

Hodně prostoru dostala ochrana soukromí. Uživatel car Atticus chválil jako to, čím měla být Siri, ale vadilo mu posílání soukromých dat Anthropicu a navrhoval volbu lokálního modelu přes rozhraní kompatibilní s OpenAI, jaké nabízejí třeba Llama.app nebo Unsloth Studio. Jako příklad zmínil uzavřený macOS asistent OOMU s lokálním režimem a vlastními modely. Saarth odpověděl, že každodenní povely běží bez AI, ale obavu chápe a o lokální variantě bude přemýšlet, jen se bojí výkonu, protože při vícekrokových úlohách už podle něj klopýtá i menší Haiku.

Závěr patřil praktickým a jedné rýpavé otázce. Uživatel joertemple se ptal, jak Atticus pozná, že uložená zkratka zastarala, když aktualizace aplikace posune tlačítko nebo vyskočí nový dialog, a zda selhání samo vrátí k Claude k novému naučení. Uživatel jmathai zas nadhodil levnější cloudový model DeepSeek a pochválil video. Uživatel trollbridge se s omluvou, že nechce být nepříjemný, zeptal na podmínky Claude, které nedovolují registraci pod osmnáct let ani sdílení účtu, a dodal, že právě mladí by se s agenty učit měli.

Z vlákna tak zbyl obrázek šikovného studentského projektu, který sází na rychlost bez AI tam, kde to jde, a komunitu, která hned řeší porty, soukromí a výdrž naučených triků.
