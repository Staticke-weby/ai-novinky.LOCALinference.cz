# 50264853
**Survival LLM: AI asistent a nouzová knihovna, která běží bez internetu**

Hacker News · Luc · 27. října 2026, 20:55 · 279 bodů / 121 komentářů · [diskuse](https://news.ycombinator.com/item?id=50264853)

Survival LLM je bezplatný open source asistent, který má fungovat ve chvíli, kdy nefunguje internet. Celý běží na vlastním počítači, poradí třeba jak uchovat potraviny při výpadku proudu, ošetřit popáleninu nebo vyčistit vodu, a nic z dotazů nikam neodesílá. Nastavení se dělá dokud je člověk online, potom už připojení nepotřebuje.

Aplikace je pro Mac a Windows stejná, po otevření zkontroluje paměť počítače a stáhne model, který se do ní vejde. Větší paměť znamená chytřejší model, od IBM Granite 4.2 8B se 6 GB přes Qwen3.8 27B s 18 GB až po NVIDIA Nemotron 3.5 Super s 80 GB, ve vlastním testu na 22 otázkách z výpadků a první pomoci měly větší modely 19 až 21 správně. K tomu se stahuje knihovna o 9 GB se zhruba 930 tisíci nejčtenějšími články Wikipedie, lékařskými příručkami WikiMed, MedlinePlus a WikEM, návody FEMA a CDC, armádními manuály, wikiHow, iFixit a dalšími zdroji, každá odpověď uvede články, ze kterých čerpala, a zvýrazní v nich konkrétní pasáž.

Největší debatu rozjel rnd0 otázkou, proč kvůli tomu tahat hladové modely náchylné k halucinacím, když by stačil prohledávatelný lokální archiv typu Kiwix. Odpůrci mu oponují, že chat je prostě lepší rozhraní k informacím: nico píše, že spojení modelu s databází článků dává skvělý způsob, jak se v nich vyznat bez nutnosti všechno si pamatovat, a tourmalinetaco dodává, že Survival LLM takový archiv už v sobě má a model nad ním dělá RAG, takže pomůže i tomu, kdo neví, jaká slova do vyhledávání zadat.

Druhá linka řeší důvěru. Uživatel bityard oceňuje, že projekt se odpovědi aspoň snaží ukotvit v člověkem prověřených zdrojích, což je mnohem poctivější než holý chatbot, zároveň ale varuje, že u otázky bez opory v databázi pořád hrozí halucinace a se přežitím rodiny by tomu nevěřil. Podobně to vidí SwellJoe, podle kterého je velmi malý model offline spíš hloupý a kvůli výmyslům i nebezpečný, a saaaaaam si utahuje z toho, že Granite na běžném stroji se 14 správnými odpověďmi ze 22 se splete skoro v polovině případů a u nouzové apendektomie to zamrzí.

Třetí proud je praktický a nostalgický. Uživatel armcat vzpomíná, jak v roce 2018 pro školy bez internetu stavěl vyhledávání ve Wikipedii s TextRank souhrny na Raspberry Pi v plastové krabičce, dnes by prý přidal malý LLM s rozpoznáváním a syntézou řeči a měl by asistenta do krabičky od cigaret. Jiní navrhují alternativy jako llamafile, Project Nomad nebo Hammunition s nástroji Kiwix na externím disku, walrus01 radí nestahovat jen modely do paměti, ale pomalu streamovat z disku i mnohem větší modely, a TGower sní o verzi pro telefon za 25 dolarů v kovové krabici se solárním nabíjením.

Z diskuse tak zůstává jednoduché ponaučení: offline znalosti dávají smysl, ale hlas asistenta je jen nadstavba nad poctivou knihovnou a citacemi, které si člověk musí umět zkontrolovat.
