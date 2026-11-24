# 50619103
**GPUI od Zed míří do vlastního repozitáře. Řeší se licence i výkon**

Hacker News · EvilGoose · 23. listopadu 2026, 21:52 · 207 bodů / 73 komentářů · [diskuse](https://news.ycombinator.com/item?id=50619103)

Zed vyčlenil svůj grafický framework GPUI z monorepozitáře editoru do samostatného repozitáře. GPU akcelerovaná knihovna v Rustu má nově vlastní web gpui.rs a je k mání na crates.io, takže odpadá dosavadní nepohodlné vytahování přímo ze zdrojáků editoru. Krok vítá i uživatel giancarlostoro, který přiznává, že používat framework schovaný uvnitř editoru mu přišlo nepatřičné.

Samotné nové repo je zatím úsporné a působí jako rozcestník: láká na návrat za pár týdnů a odkazuje právě na web a záznam na crates.io. Právě ta stručnost ale část komunity dráždí, protože u grafické knihovny čekala ukázky, dokumentaci a hotové příklady.

Nejvážnější výhrada míří na licenci. Uživatel throwaway69123 upozorňuje, že samotné UI prvky v balíku crates/ui zůstávají pod GPL, což pro něj dělá použití v podstatě zbytečným. Uživatel nextaccountic oponuje, že copyleft je opakem restrikce a těší se na jeho návrat do knihoven, zatímco uživatel kelnos to shrnuje pragmaticky: pro open source projekty v pohodě, pro korporace nepoužitelné. Vlákno tak rychle sklouzlo k věčné přetahované, jestli GPL chrání svobodu, nebo komerčnímu využití překáží.

Druhá velká debata je o dojmu a praktičnosti. Uživatel okasaki si rýpl, že web, dokumentace ani repozitář nemají žádné screenshoty, a přidávají se uživatelé thrance, FrustratedMonky nebo yieldcrv: u grafického produktu má být demo hned nahoře, ne zapadlé kdoví kde, a vizuální příklady neměly být dodatečným nápadem. Uživatel slopinthebag pak provokuje otázkou, proč se GPUI věnuje tolik pozornosti, když prý není rychlé, přístupné, ergonomické ani krásné a v rustovém světě jsou zralejší volby. Odpověď mu dává uživatel rubyn00bie z praxe: přístupnost sice není hotová, ale s pomocí modelů Claude a DeepSeek ji za týden doplnil, výkonnostní cíle plní a pamětí je sice náročnější, než by chtěl, ale pořád třetinová proti Electronu. Uživatel tensor doplňuje, že právě sada GPUI kit přístupná je a umí i plynulé animace a rychlost řeší fork gpui-fast, zmíněn je i Slint.

Zbytek vlákna řeší minulost a budoucnost ekosystému. Uživatel nixosbestos se ptá, co bude s komunitním forkem gpui-ce, když už se GPUI jednou vydělovalo a zase vracelo zpět. Uživatel Ciantic odpovídá, že neudržovaný fork nebude nikdo oplakávat a jeden oficiální repozitář přináší jasno, uživatel yedpodtrzitko ale připomíná aktivní fork longbridge/gpui-fast a spekuluje, zda se jeho opravy dostanou upstream. A nechybí obligátní přestřelka o Rustu: ukázkový hello world přijde uživateli drnick1 upovídaný a ošklivý, jiní to svádějí spíš na sílu knihovny než na jazyk a uživatel bloppe to glosuje, že Rust je ošklivý pro začátečníky, krásný pro pokročilé a zase trochu ošklivý pro experty.

Kdo čekal hotový návod, zatím ho nedostane — samostatné GPUI je spíš pozvánka. Pro zvědavce je dobrá zpráva, že už žije vlastním životem, pro firmy otazník, zda se vejdou do licence a zda si přístupnost a ukázky doplní sami.
