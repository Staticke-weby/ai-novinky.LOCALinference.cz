# 50195543
**pwn.watch: přehled toho, co se právě zneužívá a kde je oprava**

Hacker News · mrkd · 22. října 2026, 16:08 · 356 bodů / 164 komentářů · [diskuse](https://news.ycombinator.com/item?id=50195543)

Na Hacker News se objevil odkaz na web pwn.watch, který slibuje přehled bezpečnostních incidentů, na kterých právě teď záleží, včetně toho, zda už existuje oprava. Autor k němu nepřidal žádný vlastní komentář, takže stránka musela mluvit sama za sebe a diskuse se stočila rovnou k tomu, jak je udělaná a co ukazuje.

Stránka eviduje 240 incidentů za posledních 12 měsíců a zobrazuje je na heatmapě podle dnů. V době zachycení hlásila 41 živých incidentů, z toho 19 kritických a 20 zatím ne zcela opravených. Mezi nejnovějšími případy jsou kritická SQL injection v Arista VeloCloud Orchestrator, neověřené spuštění kódu v GitLabu přes chybu v regulárních výrazech i únik neopravených hlášení o chybách linuxového jádra na veřejnou konferenci.

Největší debatu vyvolala právě ta heatmapa. Uživatel Kevin_Flynn píše, že hledal graf incidentů a oprav v reálném čase, něco jako burzovní graf konce softwarového světa, a našel jen heatmapu. Uživatel prodigycorp navrhuje, že by byl užitečnější, srozumitelnější a pokornější jednoduchý čárový graf, s čímž souhlasí alt227, podle kterého se heatmapa velmi špatně čte. Do toho vtipkuje srveale, že heatmapa aspoň ukazuje, že AI agentům stále častěji nevadí pracovat o víkendech, a autor webu thekitze v diskusi slibuje, že přidá další grafy i historická data.

Druhá linka se točí kolem tlačítka na zkopírování instrukcí pro agenty. Uživatel ceuk nápad chválí a píše, že ho hned využil, na což contravariant odpovídá, že by bylo ještě lepší, kdyby šlo před zkopírováním poznat, k čemu instrukce jsou. Uživatel baoooooooooooo namítá, že je to skvělé pro rychlou reakci, ale nepřijde mu to moc bezpečné, a ceuk přiznává, že si text musel nejdřív někam vložit, aby zkontroloval jeho nezávadnost.

Zbytek vlákna řeší, zda incidentů skutečně přibývá a zda web není jen další generický výstup jazykového modelu. Uživatel pixl97 by rád viděl srovnání s rokem 2025 a diví se tempu, jakým se chyby objevují, zatímco turbobutton dokládá statistiku amerických úniků dat, podle které se jejich počet v posledních letech drží v řádu tisíců ročně. Uživatelé par a VCFundedGenYer stránku odbývají jako AI slop se stereotypní estetikou, na což thekitze reaguje, že web vznikl narychlo a že skončil v nemocnici s nějakým virem, takže ho nestihl doladit. Smířlivější tón přidává jbs789 s tím, že útočníci nové nástroje prostě zavádějí rychleji a obrana je časem dožene.

Kdo si chce udělat rychlý obrázek o tom, co právě hoří a zda už je k dispozici záplata, najde tu užitečný rozcestník, jen se zatím musí prokousat hustou heatmapou.
