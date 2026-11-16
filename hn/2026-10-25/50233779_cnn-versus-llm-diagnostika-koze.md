# 50233779
**Deset let stará CNN poráží špičkové LLM v diagnostice rakoviny kůže**

Hacker News · sungam · 25. října 2026, 18:15 · 526 bodů / 230 komentářů · [diskuse](https://news.ycombinator.com/item?id=50233779)

Dermatolog Magnus Lynch vzal 200 biopticky potvrzených lézí, každou s klinickou i dermoskopickou fotkou, a nechal z šesti možných diagnóz vybírat GPT-6 Astra, Claude Fable 5.1 a doladěný Inception v3 z roku 2015. Stará konvoluční síť trefila správnou diagnózu u 125 případů (62 %), obě špičková LLM jen u 84 a 85 (42 %). Nejvíc bije do očí invazivní melanom na uchu tenký pod 0,8 milimetru: obě LLM ho označily za neškodnou seboroickou keratózu vhodnou k propuštění, zatímco CNN melanom poznala.

Lynch síť záměrně nehnal na hranu možností, jen ji asi dvacet minut doladil na veřejných dermatologických datech a model je dodnes tak malý, že běží celý v prohlížeči telefonu přes WebGPU. V článku přiznává limity pokusu: vzorek je malý, všechny léze byly bioptované a tedy těžší než běžný průměr, každý případ u LLM běžel jen jednou. Když se obou modelů zeptal jako pacient s jedinou klinickou fotkou, jestli má jít k lékaři, poslaly k doktorovi skoro všechno včetně neškodných nálezů.

Diskuse se okamžitě stočila k obligátní hlášce, kterou nadhodil uživatel MitPitt: kalkulačka také porazí LLM v násobení a dělení. Ostatní ale odpovídají, že právě tohle je potřeba připomínat pořád dokola, protože masy věří, že LLM je „krabice na všechno", a výzkumníci podle uživatele jszymborski stále častěji reagují na jakýkoliv úkol slovy proč trénovat nový model, když se stačí zeptat LLM. Sám autor testu se v komentářích přiznal, že po nedávných matematických výsledcích čekal od LLM mnohem víc, zvlášť když jsou po internetu desítky tisíc trénovacích fotek kožních nádorů.

Jádro vlákna patří sporu o takzvané Jev-style rozhodovací modely. Uživatel snitty píše, že ho udivuje nadšení z nich: pro jakoukoliv aplikaci ve velkém měřítku bude přesnější dedikovaný klasifikátor se správnou architekturou a LLM jen srazilo cenu jeho výroby téměř na nulu. Uživatel foolswisdom namítá, že LLM se hodí jako odrazový můstek, nasbírá první jistější případy a data na nich pak uživí specializovaný model, zatímco uživatel softwaredoug přirovnává debatu k tvrzení, že nepotřebujeme Dropbox, protože máme FTP servery.

Třetí linka řeší lenost a tření. Uživatel andrewmutz shrnuje obvyklý kompromis: trénink potřebuje popisky a data, kdežto rozjet LLM stačí promptem, takže je rychlejší a snazší, i když dobrý úzký model vyhraje. Uživatel Routine8502 dodává paretovský pohled, že osmdesát procent aplikací si vystačí s dvaceti procenty inteligence a hotové API bez shánění kvalitních trénovacích dat je výhra, jen rakovina kůže mezi ně asi nepatří. Uživatel tgv to uzavírá poznámkou, že špičkové modely jsou zkrátka dobré v programování, kde mají hory dat, ale obrázky rakoviny se do vnitřní reprezentace jazykového modelu překládají špatně.

Čtenář si odnese prosté ponaučení z titulku: kde jde o úzkou vizuální úlohu a vysokou cenu omylu, malý starý specialista dál poráží velkého generalistu.
