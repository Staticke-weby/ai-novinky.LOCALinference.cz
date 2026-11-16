# 50214373
**Corgi: multiplexer pro agenty a terminály**

Hacker News · eiopa · 23. října 2026, 21:46 · 67 bodů / 16 komentářů · [diskuse](https://news.ycombinator.com/item?id=50214373)

Autor eiopa představil Corgi, multiplexor pro agentní kódování, který několik týdnů používá jako svůj hlavní nástroj. Inspiroval se projektem Herdr a vsadil na ergonomii: na první pohled je vidět, co jednotliví agenti dělají a kdo potřebuje pozornost, přičemž klávesa F1 skočí na dalšího nepřečteného. Vznik popisuje i osobně, jako výzvu během frustrující nemocenské, kdy si chtěl vyzkoušet, zda se dokáže vrátit k práci.

Web projektu slibuje přehled ve stylu stavů pracuje, potřebuje tě, hotovo a nečinnost, jednotný spouštěč pro Claude Code, Codex, Pi a OpenCode s rychlým vyhledáváním a obnovením sezení i průběžným sledováním spotřeby tokenů. Agenti a procesy běží na pozadí jako v tmuxu, Corgi ukazuje každý soubor, na který agent sáhl, pomáhá organizovat workspaces a sleduje vytížení procesoru, paměti a grafiky po jednotlivých prostředích. K tomu přidává drobnosti pro práci v terminálu: odkazy jdou kopírovat kliknutím, vkládání přes klávesovou zkratku zvládne i obrázky přes SSH, obrázky mají náhled a zavřený panel se vrací zkratkou pro vrácení.

První ohlasy jsou vesměs zvědavé. JakeSc chválí nápad a přiznává, že postavil něco podobného, otevřený projekt Exawatt, protože ho ergonomie agentů také zajímá. Uživatel pokpokpok píše, že Corgi měsíc používá jako náhradu za cmux a oceňuje na něm jednoduchý design, uživatel xfalcox v něm zase vidí druhou verzi Herdr, kterou chce vyzkoušet.

Nejdelší výměna se stočila k instalaci. Uživatel robsalasco prosí o verzi pro brew, protože nemá rád instalační skripty stahované přes bash. Autor odpovídá, že většina správců balíčků dnes přeskočí sandboxing, takže spuštěný kód má stejná práva a stejné riziko jako skript stažený z internetu, snad jen s výhodou explicitního verzování. Vedle toho se uživatel esafak zastává myšlenky registrů pro instalaci a odkazuje na Aqua Registry.

Zbytek vlákna řeší vztah k Herdr a vzhled. Na otázku uživatele Lord_Zero, kolik z toho by mohlo být jen zásuvnými moduly pro Herdr, odpovídá uživatel eleventen, že asi velmi málo, protože systém zásuvných modulů je zatím omezený a nezralý, sám Herdr denně používá a doufá, že si dobré nápady převezme. Uživatel crossroadsguy rýpe, že tvůrce, který agentovi nezadá i světlé téma, nestojí za pozornost, na což eiopa reaguje popisem vestavěného tématu Animal Style, které přebírá paletu terminálu a snaží se přizpůsobit i světlým motivům, byť zatím není tak dotažené jako výchozí tmavé. Skeptický tón vnáší uživatel syngrog66 s poznámkou, zda má smysl světu oznamovat projekt starý pár týdnů, na což moderátor dang lakonicky odpovídá otázkou, proč ne.

Z diskuse tak vychází Corgi jako útulný dohled nad hejnem agentů, kde nejvíc rezonuje prostá potřeba vědět, co se kde děje, a rychle se k tomu dostat.
