# 1xaflhy
**Nepřecházejte na novou Strata, varuje uživatel. Přináší breaking changes**

r/LocalLLaMA · u/randylush · 20. října 2026, 03:52 · 202 bodů / 122 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xaflhy/)

Uživatel u/randylush varuje před aktualizací nástroje Strata, se kterou má na Windows i na Linuxu spoustu problémů s nekompatibilními změnami. Vadí mu hlavně nové zbytečné požadavky kolem servírování modelů a posun webového rozhraní směrem k desktopové aplikaci. Radí proto ostatním, aby si před upgradem aspoň udělali zálohu, a rovnou dodává, že za varování čeká downvote od nejvrtkavějšího subredditu všech dob.

Největší ohlas měla smířlivá linka, že Strata je projekt jednoho vývojáře, který má právo jít vlastním směrem. Jak píše u/ForsookComparison, subreddit by chtěl něco jako model Married k llama.cpp, ale autor Straty měl sen, který se s tím protíná jen částečně – není to padouch a nic nikomu nedluží. Pokud se bojíte, forkněte repozitář nebo pomáhejte třeba s testováním a hlášením chyb, vzkazuje. Na to navazuje u/Interpause s přáním, aby se aplikace oddělila od enginu, a prosbou o podporu svého feedbacku na GitHubu.

Druhá velká debata se točí kolem povinného lokálního ověřování a API klíče pro připojení v místní síti. Uživatel u/Gullible-Special-31 chápe varování i otravenost z tlačení uživatelů webového UI do desktopové obálky, zvlášť když někdo provozuje Stratu bezhlavě na domácím serveru. Zároveň ale píše, že vymáhání lokální autentizace bylo dávno na čase, aby lidé omylem nevystavovali nezabezpečené servery do celé sítě. Podobně to vidí u/MindfulMan1984, podle kterého je klíč celkem základní bezpečnostní praxe a jediná „nekompatibilní“ změna, na kterou po upgradu narazil.

Zbytek vlákna popisuje bolest poslední bety i vtípky na účet vibe codingu. Uživatel u/Dreeew84 si stěžuje, že se beta nemůže rozhodnout mezi novým textovým rozhraním a JSON konfigurací, úpravy jsou nepřehledné a ruční zásahy do JSON se po startu přepisují, k tomu přihazuje nutnost pouštět server přes PowerShell a ruční odinstalaci. Praktický protipól přidává u/Joralk_, který Stratu provozuje denně bez UI jako engine pro benchmarky: doporučuje připnout konkrétní tag, nechat si autentizaci a vázat na localhost, a když konfigurace po změně kalibrace cache padá na nedostatek VRAM, explicitně nastavit příznak pro rezervu paměti. Mezitím se nahoře směje u/fgk55555, že vibe coding dává a vibe coding bere, a u/jacek2023 dodává, že je to úžasné jako výherní automat.

Kdo váhá, ať zůstane na poslední funkční verzi, zálohuje a před skokem si projde změny v enginu – návrat ke starému releasu jsou, jak tu padlo, dvě minuty.
