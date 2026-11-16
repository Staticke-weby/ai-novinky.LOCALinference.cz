# 50106054
**Sygal převádí PDF, scany a weby do Markdownu lokálně**

Hacker News · cyrillsemah · 15. října 2026, 18:26 · 39 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50106054)

Na Hacker News představil uživatel cyrillsemah vlastní nástroj Sygal, který má z nepřehledných dokumentů udělat čistý text pro umělou inteligenci. Aplikace slibuje jednorázovou platbu 25 eur bez předplatného a účtu, se čtrnáctidenní zkušební verzí zdarma.

Podle odkazovaného webu stačí přetáhnout soubor, vložit adresu nebo screenshot přes schránku a Sygal vrátí Markdown a strukturované JSON, které lze rovnou vložit do promptu, znalostní báze nebo pipeline. Převod má trvat kolem 1,7 sekundy, výsledek zůstává v prohledávatelné místní knihovně s ukázkou originálu, možností úprav a počtem tokenů. U obrázků, scanů a webů má čistý text proti pixelům a značkám ušetřit zhruba dvakrát až sedmkrát tolik tokenů, odkazy na YouTube se mění v přepis připravený k shrnutí.

Jádro sporu ale bylo jediné slovo v titulku: lokálně. Uživatel cameronbedard se ptá, v čem se Sygal liší od otevřeného Markeru, a označuje za zavádějící mluvit o lokálním převodu, když výchozí OCR míří do cloudu přes klíč od OpenAI, Claude, Mistral, NVIDIE či Gemini. Podobně to vidí uživatel kennywinker, podle kterého dokumenty ve skutečnosti putují k vybranému jazykovému modelu. Odpověď uživatele MrDrMcCoy je stručná, že modely už lze nějakou dobu provozovat na vlastním serveru.

Zbytek vlákna se tak proměnil v přehlídku alternativ. Uživatel bbor chválí Marker 2 za pokrytí otravných okrajových případů, uživatel mrkn1 upozorňuje na TextSnap, který běží celý lokálně přes ONNX na procesoru bez klíče. Uživatel axm997 přidává vlastní AIDocPrep s důrazem na provoz zcela bez internetu a s redakcí, uživatel cachius odkazuje na službu Into.md a uživatel fishisnow na bezplatný mdpdf.net běžící celý v prohlížeči. Právě u tabulek, bloků kódu a OCR vidí největší bolest převodu PDF do Markdownu.

Praktickou otázku položil jen uživatel Benard-dev, který staví podobnou aplikaci a zajímalo ho, jak Sygal zvládá nepořádné scany a tabulky. Odpovědi se v balíčku nedočkal, diskuse se místo toho stočila k tomu, kde končí lokální konverze a začíná cloud.
