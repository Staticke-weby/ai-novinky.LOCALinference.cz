# 50031614
**Talorys: vlastní osobní AI agent zdarma na Cloudflare**

Hacker News · rociiu · 10. října 2026, 12:52 · 273 bodů / 126 komentářů · [diskuse](https://news.ycombinator.com/item?id=50031614)

Autor rociiu představil Talorys, open-source osobního AI asistenta, který běží výhradně uvnitř vlastního účtu uživatele na Cloudflare. Nasazení slibuje jediným příkazem npx create-talorys@latest, bez vlastního serveru, databáze nebo účtu provozovaného vývojáři projektu. Motivací prý byla touha mít asistenta, kterého člověk vlastní a ovládá, bez měsíčního předplatného.

Stránka projektu popisuje chat se streamovanými odpověďmi, trvalou paměť na fakta a preference, správu úkolů, poznámek a projektů i jednorázové a opakované připomínky a rutiny. Technicky stojí na Pages, privátním Workeru a Durable Object s SQLite, inference zajišťuje Workers AI s modelem označeným @cf/zai-org/glm-4.7-flash. Složenka služeb se má vejít do bezplatného tarifu, s pojistkami pro limity tokenů a denní kvótu a se slibem, že úkoly či připomínky fungují i po vyčerpání AI kreditu.

Nejživější spor se strhl kolem slova soběstačný. Uživatel onionisafruit namítá, že Cloudflare zatím není veřejná služba, muvlon dodává, že místo jedné cizí služby se člověk opírá rovnou o čtyři, a rvz varuje, že bezplatná úroveň se může kdykoliv změnit. Vlákno o definici vlastního hostování pak rozebírá hranici mezi hardwarem doma, pronajatým serverem a cloudem, kdy esafak navrhuje prostší název o agentovi na bezplatné úrovni Cloudflare, zatímco coubri naopak obdivuje, že infrastrukturu platí Cloudflare místo uživatele.

Druhé velké téma jsou záhadné neurony, tedy denní jednotka pro Workers AI. Uživatel deanc se ptá, co to vůbec je, martheen přepočítává deset tisíc neuronů zhruba na 0,11 dolaru a pcthrowaway přidává odhad v tokenech podle zvoleného modelu. Uživatel 876433790 to shrnuje jako fantasy měnu z mobilních her, která zakrývá skutečnou cenu, a tln popisuje vlastní zkušenost, kdy pár minut povídání spolklo pět set neuronů a na lehké denní používání by tak stačilo možná dvacet až třicet minut konverzace.

Zbytek diskuse míchá pochvalu, rýpnutí i praktické výtky. Uživatel felixgallo vtipkuje, kde si má stáhnout Cloudflare, Jolter kritizuje oznámení jako strojově uhlazenou prózu a radí příště psát vlastními slovy. Uživatel richgroot chválí provedení, ale postrádá hlasové ovládání ve stylu reproduktorů rozesetých po domě, jehož kutilské náhrady prý příliš chybují, a tln by k tomu přidal ještě procházení stránek a vyhledávání na webu.

Pro čtenáře z toho plyne jednoduché ponaučení: jako levný a rychle nasaditelný pokus je Talorys lákavý, o plné nezávislosti na cizí infrastruktuře ale diskuse pochybuje.
