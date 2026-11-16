# 49963171
**Cloudflare představil Web Search API**

Hacker News · tosh · 5. října 2026, 12:47 · 509 bodů / 234 komentářů · [diskuse](https://news.ycombinator.com/item?id=49963171)

Cloudflare spustil nové rozhraní pro vyhledávání na webu určené agentům a aplikacím s umělou inteligencí. Má jim umožnit opřít odpovědi o aktuální informace z internetu místo hádání odkazů a spoléhání na zastaralá tréninková data.

Podle oznámení je novinka zatím v betaverzi a na výběr dává tři poskytovatele vyhledávání: Ceramic.ai, Exa a Linkup. Všichni podporují režim Zero Data Retention a zavázali se k pravidlům pro ověřené boty, volání prochází přes AI Gateway, takže se objevují v logách a účtují se do kreditů bez přirážky, případně si lze přinést vlastní klíč.

Nejčastější otázka diskuse zněla jednoduše, slovy uživatele binarymax: proč nepoužít ty poskytovatele přímo a proč musí být Cloudflare uprostřed všeho. Uživatel unified101 odpovídá, že jde o snadnější integraci a fakturaci, převzetí při výpadku a vyšší důvěru, uživatel patwolf přidává vlastní zkušenost s vyhledáváním v OpenRouteru, kde je pohodlné zkoušet nové modely a enginy bez vyřizování dalšího předplatného. Uživatel hobofan to shrnuje tak, že se Cloudflare pro firmy, které ho už používají, stává hlavním důvěryhodným dodavatelem cloudu, přes kterého se účtuje většina nákladů a odpadá nové výběrové řízení.

Do vážnější roviny to posunul uživatel ForHackernews, podle kterého se Cloudflare staví do role rozhodčího, jenž bude určovat, co je člověk, autorizovaný bot a zakázaný bot. Vzhledem k tomu, kolik lidí si stěžuje na scrapéry a další boty, to podle něj někdo udělat musel. Odlehčení obstarali uživatel rithdmc s narážkou na předávání zpravodajských informací Spojeným státům a uživatel tucnak s hláškou o národní bezpečnosti. Praktickou pochybnost nadhodil uživatel tom1337, jestli se ty tři enginy dostanou přes captchu a botí ochranu na stránkách chráněných Cloudflarem, na což uživatel astonex odpovídá, že nejspíš ne.

Zbytek vlákna řeší, co v nabídce chybí a k čemu to vlastně je. Uživatel timpera lituje absence Brave Search API, které považuje za lepší než Exa, a nepřítomnost vyhledávání od Perplexity prý nepřekvapí vzhledem k tomu, jak se obě firmy nesnášejí. Uživatel Oras, který vývojářskou platformu Cloudflaru chválí, přiznává, že bránu API nikdy nepoužil a vystačil si s OpenRouterem, smysl tak vidí hlavně pro ty, kdo chtějí mít logy na jednom místě. Debatu o cenách vyhledávání rozjel uživatel iphonecorridor chválou Gemini Flash Lite 2.5 s tisícovkou vyhledávání denně zdarma, uživatel apwheele ale namítá, že pro aplikaci postavenou na vyhledávání je limit tvrdým stropem a sám zůstává u rychlého vyhledávání od Perplexity, protože potřebuje stahovat celé stránky, ne jen souhrny.

Kolem novinky se tak mísí nadšení z pohodlného účtování s nedůvěrou k dalšímu prostředníkovi, který bude hlídat celý web.
