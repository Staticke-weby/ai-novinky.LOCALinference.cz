# 50591974
**Claude opravil starou televizi přes Flipper Zero a foťák**

Hacker News · Lockranor · 21. listopadu 2026, 19:16 · 5 bodů / 0 komentářů · [diskuse](https://news.ycombinator.com/item?id=50591974)

Stárnoucí televize Vizio modrá, protože její podsvícení věkem mění barvu, a majitel už zkoušel marně lovit nápravu v menu. Místo dalšího zdlouhavého laborování metodou pokus–omyl zapojil model Claude Sonnet 5.5 a ten mu během asi čtyřiceti minut pomohl obraz viditelně zlepšit, i když stárnoucí podsvícení nešlo vyléčit úplně. Místo dokonalé opravy tak vznikla praktická ukázka domácí diagnostiky s agentem v hlavní roli.

Majitel k tomu poskládal výbavu, kterou měl zrovna po ruce. Počítač s Linuxem byl připojený přímo k televizi, Mac s kamerou spolu s Flipperem Zero postavil na notový stojan a obojí namířil na obrazovku. V této sestavě pak nechal Claude pracovat jako prostředníka mezi tím, co kamera vidí, a tím, co se dá na televizi a počítači přenastavit.

Claude se podle zápisu přes shell dostal do počítače u televize a připravil testovací obraz, podle kterého se dal modrý posun posuzovat. Zároveň si ověřil, že Flipper televizi skutečně ovládá, a infračervený profil pro daný model si v něm našel sám bez dalšího upřesňování. Při procházení nabídek narazil i na nastavení vyvážení bílé, kterých si majitel dosud nikdy nevšiml, a vedle zásahů přímo na televizi doladil i vyvážení barev na hostitelském počítači pod X11.

Vlákno na Hacker News v době sběru zůstalo bez komentářů, čtenář se tak musí spolehnout na samotný zápis a připojené snímky testovacího vzoru před úpravou a výsledku po ní. I tak je pointa srozumitelná: agent spojil kameru, dálkové ovládání přes Flipper a dva počítače do jednoho postupu a ušetřil člověku zdlouhavé klikání v menu. U umírajícího podsvícení to na zázrak nestačí, ale jako recept na rychlé vylepšení staré televize to funguje překvapivě dobře.
