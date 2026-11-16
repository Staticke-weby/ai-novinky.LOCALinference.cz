# 50040547
**Výpadky Yandex Cloudu po zásazích dronů**

Hacker News · defly · 11. října 2026, 09:34 · 567 bodů / 689 komentářů · [diskuse](https://news.ycombinator.com/item?id=50040547)

Během čtyř dnů vyřadily zásahy tři hlavní datacentra Yandexu a mechanismy převzetí provozu se podle zpráv zhroutily. Uživatel defly v diskusi upřesňuje, že z veřejných zdrojů jde o zásahy v Sasovu, Kaluze a Vladimiru, a přiložený odkaz míří na incidentní stránku Yandex Cloudu, která se ostatně v době debaty sama chvílemi neotvírala.

Sloučené druhé vlákno odkazuje na veřejné metriky Cloudflare Radar pro botovský provoz z autonomního systému AS13238 patřícího Yandexu. Jde o filtr, který má podle glosáře Cloudflare zachycovat tradiční webový provoz bez API volání a stahování obrázků či skriptů.

Nejkonkrétnější popis škod přinesl uživatel schleck8 z dashboardu Yandex Cloudu: ruský compute core je offline včetně Kubernetes, PostgreSQL, ClickHouse, MySQL, YDB, Kafky nebo balanceru, a mimo provoz je i zálohování. Výpadky se podle něj přelily přes Yandex Go, Yandex Pay, rozvoz jídla, chytrou domácnost a interní logistiku až po firemní zákazníky cloudu a pocítily je i Bělorusko, Kazachstán, Arménie a Srbsko. Zajímavým detailem je, že status stránka údajně odkazuje zákazníky na konkurenční Selectel a K2Cloud, uživatel alephnerd ale situaci mírní tím, že kazašské regiony podle dashboardu běží a katastrofa tedy není úplná.

Kolem grafu z Radaru se rozjela debata, co vlastně zmizelý provoz byl. Ukazuje prudký propad automatizovaného provozu téměř k nule, což část komentujících čte jako v podstatě utichlé indexování webu. Uživatel londons_explore připomíná, že Yandex je ruský Google a indexování je úloha s nízkou prioritou, takže při ztrátě poloviny kapacity klesne botovský provoz o víc než polovinu. Uživatel dgellow oponuje, že Yandex dávno není jen vyhledávač a jeho servery hostí i skutečný botovský provoz, uživatel walrus01 doplňuje, že podobný propad hlásí i druhé yandexovské AS200350 pro hostingovou platformu. Odlehčení dodali uživatelé toomuchtodo a Pikamander2 nápady, že by měl Cloudflare přispět ukrajinské armádě za úklid internetu a že nový tarif obsahuje „Super Duper Bot Fight Mode" s náletem na datacentrum v sankcionované zemi.

Zbytek vláken řeší, co to znamená pro stavbu datacenter ve válce. Uživatel Bluestein to označuje za budoucí případovou studii pro lidi kolem vysoké dostupnosti a provozu, uživatel usrnm se ptá, zda přijde éra decentralizovaných sítí menších center, na což uživatel yablak odpovídá stroze, že jen přibude stavění pod zemí. Uživatel qingcharles to shrnuje obrazem měnící se války, kdy pár malých dronů vypne lidem taxi, doručování a sociální sítě, a ptá se, kde bude sankcionovaná země brát stojany Xeonů, paměti DDR5 a grafiky Nvidia.

Z diskuse tak zůstává obrázek digitální infrastruktury, která je překvapivě křehká právě tam, kde se o ní mluví jako o cloudu.
