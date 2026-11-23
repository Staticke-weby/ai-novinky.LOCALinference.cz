# 1y2gwba
**Někdo mu v noci používal Claude. Ruský prompt a smazané projekty**

r/ClaudeAI · u/Particular-Card2344 · 22. listopadu 2026, 05:56 · 275 bodů / 108 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1y2gwba/)

Ráno otevřel Claude a našel v něm tři až čtyři chaty, které sám nespustil. Jeden z nich byl v ruštině, kterou neumí, a přikazoval Claudovi auditovat všechny e-maily přes napojený Gmail konektor. Chat okamžitě zastavil a konektory odpojil, pak ale zjistil větší škodu: zmizelo několik projektů včetně asi dvoutýdenní práce a většina listopadových chatů, artefakty z projektů přitom zůstaly. E-mail přitom vypadá normálně a přihlašovací kódy mu chodí jen při jeho vlastním přihlášení, a tak se ptá, jestli šlo o ukradenou session, nebo infostealer, a zda mu podpora dokáže projekty obnovit.

Diskuse se rychle shodla na jediném vysvětlení: odcizené přihlášení z jeho vlastního počítače. Nejvýše hodnocený komentář u/localtuned stručně radí nahlásit to Anthropicu, zbytek vlákna pak rozvíjí, jak se to mohlo stát. u/oasuke varuje před bezhlavým instalováním „skills": nechat si od Claudea prověřit každou dovednost a nestahovat něco jen proto, že to vypadalo dobře na Twitteru a mělo hlasy. Podle něj by měl Anthropic uživatelům při instalaci ukazovat jasné varování.

Nejsilněji znějí hlasy lidí se stejnou zkušeností. u/mynameiscorange píše, že po instalaci balíku dovedností z repozitáře na GitHubu měl na notebooku trojana. u/SnooSuggestions4197 popisuje, že se mu totéž stalo právě dnes: v běžném chatu na mobilu našel ruský požadavek, aby Claude na modelu Opus 5.5 v režimu max postavil web s online hazardem pro krypto. Heslo si změnil, ale Malwarebytes ani Eset nic nenašly a do reinstalace Windows se mu nechce.

Právě čistá reinstalace je přitom nejčastější rada ve vlákně. u/couldgiveaflyingfck popisuje klasický scénář s crackem na hru nebo malwarem převlečeným za legitimní aplikaci, který otevře zadní vrátka do systému a sesbírá hesla a session. Doporučuje přeinstalovat Windows z čistého média, továrně resetovat modem i router, změnit všechna hesla a snímky ruských promptů si schovat jako důkaz pro případ zneužití připojení. Jiní to doplňují praktičtěji: u/drizzkek připomíná zapnout dvoufázové ověření na e-mailu a stáhnout si autentikační aplikaci, u/plain_meridian radí projít si všechny nedávno přidané dovednosti a MCP servery, protože běží s oprávněními uživatele a jedna špatná tak vidí všechno, co on.

Automatické shrnutí od u/ClaudeAI-mod-bot tuhle shodu jen potvrzuje a přidává důležitý detail: Claude nepoužívá hesla, ale magické odkazy do e-mailu, takže útočník nejspíš neukradl heslo, ale aktivní session token z prohlížeče. Odtud i rada v bodech: považovat počítač za kompromitovaný, zrušit všechny aktivní relace a API klíče v Claudeovi, Googlu či Amazonu a v e-mailu zkontrolovat nová pravidla pro přeposílání, kterými útočník maskuje stopy.

Kdo si do Claudea přidává cizí dovednosti z GitHubu a Twitteru, měl by je brát jako spustitelný kód s přístupem ke svým datům, ne jako nevinné doplňky.
