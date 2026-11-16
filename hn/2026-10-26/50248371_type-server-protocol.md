# 50248371
**Microsoft zveřejnil Type Server Protocol pro Python**

Hacker News · adamnemecek · 26. října 2026, 19:14 · 221 bodů / 146 komentářů · [diskuse](https://news.ycombinator.com/item?id=50248371)

Microsoft v repozitáři Pylance tiše zveřejnil dokumentaci nového protokolu nazvaného Type Server Protocol. Odkaz bez dalšího komentáře se během pár hodin vyhoupl mezi nejsledovanější příběhy dne a nasbíral přes dvě stě bodů.

Podle zveřejněného textu jde o JSON-RPC protokol, přes který se nástroje ptají typového serveru na výsledky analýzy pythonovského workspace. Server si drží stav analýzy, vydává snapshoty a odpovídá na dotazy na verzi protokolu, Python search paths, překlad importů a tři druhy typů – odvozený, deklarovaný a očekávaný. Tvar dat přebírá z LSP včetně Position a Range, metody nesou prefix typeServer/ a závazné definice leží vedle dokumentu jako TypeScript rozhraní a strojově čitelný model.

Nejživější spor se stočil k názvu. Anonymní kritik se ptá, proč si protokol uzurpuje obecné jméno, když umí jen Python, zvlášť od firmy stojící za skutečně obecným LSP. Jiní přitakávají, že dává smysl jen přidat Python do názvu nebo čekat podporu Elixiru a dalších dynamických jazyků, zatímco Tarean protokol čte spíš jako strojově čitelný dotaz na typ v bodě, který umožní oddělit Pylance a Pyright. Výsledek je podle něj natolik svázaný s Pythonem, že ho jiný jazyk sotva převezme, na což ocamoss namítá, že by se mohl hodit právě jazykům bez oficiálního typového checkeru jako PHP, Erlang nebo Ruby.

Druhá linka řeší technické detaily a cenu. Někdo lituje, že protokol převzal UTF-16, a vidí v nové specifikaci promarněnou šanci staré rozhodnutí opravit, jiný ale krotí očekávání, že jde jen o pár set řádků schématu pro rozšiřující zprávy, ne o revizi od základů. K tomu se přidává postesk, jestli teď bude vedle LSP žrát paměť ještě i TSP, a hláška, že zkratky už rostou do řady LSP, DAP, MCP a TSP – přičemž TSP je prý také fosforečnan sodný, výborný na úklid nepořádku.

Třetí proud diskusi rychle unesl k samotnému Pythonu. Výrok, že je ostudou, jak taková katastrofa ovládla scénu a jen lepí věci, které promyšlenější jazyky mají desítky let, vyvolal lavinu odpovědí od smířlivého „horší je lepší“ až po lamentaci nad venvy, aktivacemi a instalací na novém Macu. Denní uživatelé Python brání, že je v zásadě v pořádku a rozhodně čitelnější než TypeScript, zatímco rubyista přiznává, že Rust, Elixir, C# nebo Lisp mají vždy něco skvělého – borrow checker, pattern matching nebo balíčkování – a Pythonu kromě list comprehension připadá všechno tak nějak vlažné.

Čtenář si z toho odnese, že Microsoft otevřel Pylance strojům mnohem systematičtěji než dosud, ale komunita zatím víc než specifikaci řeší, pro koho tu vlastně je.
