# 50562636
**Chrome AI funkce spotřebují stovky GB dat. Jde je vypnout**

Hacker News · speckx · 19. listopadu 2026, 17:54 · 128 bodů / 49 komentářů · [diskuse](https://news.ycombinator.com/item?id=50562636)

Webový vývojář Jeff Starr řešil záhadu, proč mu před několika měsíci prudce vyletěla spotřeba přenesených dat. Jako viníka označil nové AI funkce prohlížeče Chrome, které jsou zapnuté ve výchozím stavu. Stačilo prý v nastavení vypnout všechny volby v sekci AI innovations a On-device a síťový provoz se okamžitě srovnal.

Starr čtenáře vyzývá, ať mu nevěří a sami si pustí monitor sítě: při zapnutých funkcích je vidět trvalý datový tok z Chromu, po jejich vypnutí křivka prakticky spadne na nulu. Kritizuje, že Google takto náročné funkce nezapíná na bázi opt-in, a ptá se, kolik energie a pásma se tím zbytečně propálí u milionů lidí, kteří AI v prohlížeči vůbec nepoužívají. Sám píše, že zkouší alternativní prohlížeče.

Největší debata se vede o tom, zda je jeho odhad stovek GB měsíčně u běžného uživatele vůbec reálný. Uživatel xnx píše, že neví, co se na jeho počítači děje, ale AI funkce Chromu tolik dat nespotřebují, a uživatel jeffbee suše dodává, že s výzvou „nevěřte mi" souhlasí. Uživatel skullone žádá logy, jinak je to podle něj bezcenný blogový spam, a uživatel londons_explore připomíná, že Chrome je většinou open source, a chce ukázat konkrétní funkci a změřit její spotřebu. Proti tomu se staví uživatel autoexec s argumentem, co jiného by provoz zastavilo právě ve chvíli vypnutí nastavení, a dodává, že firmám věří méně než náhodnému vývojáři z internetu, protože rády potají experimentují jen na části uživatelů.

Nejvěcnější vysvětlení nabízí uživatel patch_v1: podezřelým je on-device model Gemini Nano za vestavěnými AI rozhraními Chromu. Má několik GB, jeho stav jde zkontrolovat na stránce chrome://on-device-internals a podle dokumentace se při nedostatku místa na disku maže a později znovu stahuje. Počítač balancující kolem této hranice tak může stejný balík stahovat pořád dokola a bez potíží se dostat na velká měsíční čísla. Uživatel bikeshaving souhlasí, že jde nejspíš jen o opakované stahování vah, ale přihazuje i odvážnější teorii o zneužití lokálního modelu k inferenci, kterou přirovnává k čínskému útoku Great Cannon na GitHub z roku 2015.

Třetí linka diskuse řeší, jak se zátěže zbavit. Uživatel josephernest popisuje, že mu proces On device bere 300 % CPU na slabém notebooku s integrovanou grafikou, psaní se zpožďuje o vteřinu a vypnutí volby v nastavení nepomáhá, takže proces musí zabíjet ručně. Uživatel g0ld3nrati0 radí vynutit zákaz přes soubor s politikami a hodnotami GenAiDefaultSettings či GeminiSettings a uživatel BatchJob tvrdí, že 4GB model se Chrome snaží stahovat pořád, pokud se mu nezmění práva k souborům. Zbytek vlákna pak utíká k útěku z Chromu: padají tipy na Chromium, Ungoogled Chromium i Firefox, který uživatel cadamsdotcom doporučuje jako trvalé vypnutí AI funkcí, zatímco uživatel autoexec glosuje, že oba prohlížeče dělá reklamní firma, jen Firefox je zatím menší zlo.

Kdo má neomezený tarif, nic nepozná, kdo platí za data nebo hlídá výkon notebooku, tomu se vyplatí zkontrolovat nastavení AI a změřit si vlastní spotřebu.

Zpět na [denní přehled](00-index.md).
