# 50014150
**Edi Life OS: self-hosted dashboard s MCP serverem pro AI**

Hacker News · edris0077 · 9. října 2026, 02:02 · 39 bodů / 15 komentářů · [diskuse](https://news.ycombinator.com/item?id=50014150)

Autor v rubrice Show HN představil Edi Life OS, klidný domácí dashboard pro soustředění, návyky, cíle, peníze a projekty. Má nahradit roztříštěný život napříč několika aplikacemi a propojit drobnosti, které člověk udělá dnes, se směrem, kam chce svůj život vést.

Podle stránky na GitHubu běží vše na PHP, MySQL a čistém JavaScriptu bez frameworku a build kroku, nasadit se dá přes Docker i na levném sdíleném hostingu a všechno zůstává ve vlastní databázi bez předplatného a sledování. Deset pracovních ploch sdílí jeden design, přihlášení a databázi – od přehledu s denním skóre přes růstové dimenze a SMART cíle až po Pomodoro se soundtrackem, Kanban, kalendář, finance, návyky, markdownový blok a lepíky. Volitelný MCP server vystavuje patnáct nástrojů a s asistentem se tak dá domluvit prostou větou, přičemž s aplikací mluví jen přes tokenem chráněné HTTP API a nikdy nesahá přímo do databáze.

První reakce byly přívětivé. Uživatel esseph projekt označil za šikovný nápad a uživatel thefourthchime za super myšlenku, autor oběma stručně poděkoval a u druhé odpovědi dodal, že uvítá zpětnou vazbu po vyzkoušení. Uživatel onaclov2000 napsal, že se o něco podobného pokouší pro osobní zdravotní data.

Vedle pochval se ozvala i tvrdší kritika kódu. Uživatel ceejayoz se ptal, jestli autor nechal kód zkritizovat Claudem, protože výsledek podle něj není příliš lichotivý a obsahuje návrhové antipatterny, jaké dvacet let neviděl. Podobně uživatel GaiusCoffee napsal, že myšlenka je dobrá, ale provedení prý hodně pokulhává.

Nejdelší výměna se stočila k Notionu. Uživatel hmyn se ptal, proč prostě nepoužít šablonu v Notionu, na což autor odpověděl, že pokud to někomu vyhovuje, je to dobrá volba, jemu ale nevyhovoval. Uživatel toppa33 popsal, že Notion používá a Claude mu sám navrhl dát před něj MCP s pravidly pro úpravy stránek a další MCP pro ostatní akce přes Tailscale. Věcnou tečku přidal uživatel armanckeser, kterému se osvědčilo dávat agentům jen přístup pro čtení do databází aplikací – když mají k dispozici zdrojový kód, naučí se volat běžná HTTP rozhraní, a pokud je služba postavená jako local first se synchronizačním enginem, funguje to jako kouzlo.

Projekt tak v diskusi stojí mezi sympatií k soukromému celku bez vendor lock-inu a pochybnostmi o řemeslném zpracování – kdo hledá jednoduchý základ pod vlastní data s AI po ruce, má si co naklonovat.
