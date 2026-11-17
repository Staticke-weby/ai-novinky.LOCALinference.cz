# 50523459
**OpenCode Browse půjčuje agentům váš skutečný prohlížeč i s přihlášeními**

Hacker News · mfiguiere · 16. listopadu 2026, 22:20 · 194 bodů / 88 komentářů · [diskuse](https://news.ycombinator.com/item?id=50523459)

OpenCode představilo Browse, kombinaci MCP serveru a rozšíření pro Chromium, která pouští AI agenty do skutečného prohlížeče uživatele. Agent tak pracuje s otevřenými záložkami, přihlášeními i rozšířeními, karty si otevírá na pozadí ve sbalených skupinách a umí na stránkách číst, klikat, psát, pořizovat snímky i nahrávat dění na kartě. Když narazí na přihlášení, dvoufaktorové ověření nebo platbu, kartu předá člověku a po kliknutí na Pokračovat jede dál.

Stránka produktu popisuje instalaci nejdřív přes rozšíření pro Chrome, které provede zbytkem nastavení, a dále láká na funkce jako zapůjčení právě otevřené karty kliknutím na tlačítko v liště, omezení agenta na povolené weby nebo záznam snímků, videa a síťového provozu. Browse má fungovat s OpenCode, Claude Code, Cursorem, Codexem, Zedem a dalšími MCP klienty a zdrojový kód je veřejný na GitHubu.

Nejživější debata se stočila k tomu, co v seznamu podporovaných prohlížečů chybí. Uživatel sixtyj se ptá po Firefoxu a mitchitizedovi vadí samotný slogan o skutečném prohlížeči, když jde ve skutečnosti jen o prohlížeče na bázi Chromia. Uživatel guipsp vysvětluje, že rozšíření má ve Firefoxu jiné programové rozhraní, a ihsw připomíná, že Firefox má vlastní MCP server pro vývojářské nástroje, který navíc umí určit profil, což považuje za klíčové pro izolaci.

Druhá linka řeší, čím je Browse jiné než existující nástroje. Uživatel jeremyjacob píše, že funkce se překrývá s Playwright MCP serverem, který sám používá právě proto, že agentům zpřístupní už otevřené stránky a sezení, jen varuje před kombinací rizik a doporučuje oddělené profily. Uživatel mrdw se dvakrát ptá po oficiálním MCP serveru Chrome DevTools a jauntywundrkind dodává, že vedle Browse zkouší i odlehčený systém Kitesurf od Cloudflaru a zatím se rozhoduje, u kterého zůstane. Proti tomu uživatel cyanydeez tvrdí, že zásuvný modul v jeho vlastním prohlížeči bezpečně zvládne i citlivé kontexty typu Outlooku, kde agent prochází zprávy, což Playwright podle něj bezpečně neumí.

Hodně prostoru dostala i nedůvěra k samotnému OpenCode. Uživatel testtestmetest firmu obviňuje z překotného vydávání nedodělků, zahození bezpečnosti ve verzi V2 i z toho, že ovládání prohlížeče přes nízkoúrovňové rozhraní CDP by zvládl jazykový model zabalit za pár hodin. Uživatel arcanemachiner oponuje z vlastní zkušenosti, že smysluplné a konzistentní zpřístupnění funkcí CDP agentům zabere mnohem víc práce, protože se funkce postupně nabalují. Praktickou výtku přidává uživatel esafak, kterému se spojení občas rozpadá a musí znovu párovat, a doufá, že vestavěný prohlížeč OpenCode s trvalými sezeními tenhle MCP server časem zbyteční.

Kdo chce nechat agenta klikat v prostředí, kde je už přihlášený, dostává s Browse pohodlnou zkratku, za kterou ale platí důvěrou v oddělení agentských karet od vlastního brouzdání.
