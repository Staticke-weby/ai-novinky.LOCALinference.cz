# 50499017
**Lovable aplikace odhalily pasy a 200 tisíc zpráv**

Hacker News · armcat · 14. listopadu 2026, 18:43 · 761 bodů / 302 komentářů · [diskuse](https://news.ycombinator.com/item?id=50499017)

Lovable je švédský AI startup založený v roce 2023, který z popisu v přirozeném jazyce staví webové aplikace i pro lidi bez zkušeností s programováním. Nezávislý výzkum prošel 159 041 projektů postavených na této platformě a u mnoha z nich našel osobní a důvěrná data dostupná bez přihlášení. Mezi exponovanými údaji byly naskenované pasy a přes 200 tisíc soukromých zpráv.

Autoři se zaměřili na databázovou službu Supabase, kterou vyhodnotili jako nejrozšířenější mezi projekty z otevřeného archivu Common Crawl od prosince 2025 do září 2026. Ze vzorku používalo Supabase 34 545 webů a 24 664 z nich posílalo záznamy z databáze hned při načtení stránky, přičemž v 10 560 tabulkách našli e-mailové adresy. Jako konkrétní případy zpráva uvádí německé lifestylové fórum s více než 80 tisíci profily, prodejce vstupenek a restaurace s údaji o platbách a adresách nebo správcovskou firmu, jíž unikaly shrnutí interních e-mailů vytvořené umělou inteligencí.

Do diskuse se zapojil i autor výzkumu neathack, podle kterého nebyly potřeba žádné pokročilé hackerské techniky. Původně chtěl začít základní konfigurací a pak přejít k sofistikovanějším útokům, ale k druhému kroku se prý nikdy nedostal, protože tolik citlivých dat leželo volně. Oras to shrnuje podobně: úniky tu byly dávno před umělou inteligencí, jenže aplikace z generátorů jsou snadným cílem, stačí prohlédnout síťové požadavky v prohlížeči a takových webů přibývají každý den tisíce. PaoloBarbolini dodává, že některé ani nebylo třeba hackovat, jejich tvůrce si prostě myslel, že přihlášení není potřeba.

Nejdelší výměna se rozjela kolem viny a prevence. adverbly přirovnal stavění veřejné aplikace bez znalostí bezpečnosti k řízení letadla pro pasažéry bez licence, což TeMPOraL a vincnetas odmítli jako maximalismus, který reálné bezpečnosti nepomáhá a vedl by až k licencím na hraní si s počítačem. gjvc kontruje, že průměrný člověk stejně nerozumí ani instalatérství či elektřině, a ivan_gammel míní, že chyba je hlavně v platformách: stavba webu má být jednoduchá, ale bezpečná už od návrhu, a produkty, které to neumí zajistit, nutí uživatele platit zbytečnou daň za vývoj.

Zbytek vlákna řeší, zda je to selhání lidí, nebo nástrojů. birdsongs si vylévá zlost nad bezohledným tempem vývoje, kdy se zkušenosti se stavbou bezpečného softwaru hází za hlavu kvůli zisku, zatímco anonym29 odpovídá, že příznivci umělé inteligence nejsou monolit a plést si nedbalé zneužití nástroje s jeho přínosem je jako zavrhnout cloud v roce 2015 kvůli otevřeným S3 bucketům. karakoram se ptá, zda je díra spíš v Lovable, nebo v integraci Supabase, kterou dnes přebírá spousta AI nástrojů. A Betelbuddy to glosuje hláškou, že o práci nepřijdete kvůli umělé inteligenci, ale kvůli někomu, kdo ji používá, a ten pak o všechno přijde kvůli někomu, kdo umí bezpečnost.

Poučení z výzkumu i diskuse je prosté: snadné vytvoření aplikace neodstraňuje nutnost zkontrolovat, kdo smí vidět co, zvlášť než se do ní vloží skutečná data zákazníků.
