# 50007993
**Jevman: rozhodovací AI modely hrají Pac-Mana**

Hacker News · felix089 · 8. října 2026, 18:34 · 52 bodů / 10 komentářů · [diskuse](https://news.ycombinator.com/item?id=50007993)

Autor představil benchmark Jevman, ve kterém poslal šest populárních rozhodovacích modelů hrát Pac-Mana proti klasickým duchům z arkády. Každý z nich – jev 1.13, kev, clef, clef flash, GPT-6 Luna a Laya – odehrál sto her a výsledky vyšly na veřejném žebříčku. Nízká latence modelů podle něj umožňuje hru v reálném čase a jedna hra vyjde zhruba na dva centy, na zkoušení přidal kredity zdarma.

Odkazovaná stránka popisuje pravidla měření: na každé křižovatce hra pošle modelu bludiště, tečky a duchy jako JSON a ten vrátí pravděpodobnost pro každý směr, přičemž na odpověď má dvě sekundy, jinak nastoupí jednoduché záložní pravidlo. Hraje se na tři životy nebo maximálně pět minut, i když nejdelší hra vydržela jen 2 minuty a 24 sekund, a pořadí určuje průměrné skóre s 95% pásmem chyby. Každá hra je nahraná a jde přesně přehrát, vlastní model za HTTP endpointem může přidat kdokoli přes pull request.

Reakce jsou vesměs nadšené. gsandahl napsal jen „moc cool“ a ozozozd přidal, že by si přál pohodlnější ovládání na mobilu. NichoPaolucci se pochlubil, že je pořád lepší než modely, a zaujal ho nápad společného poolu kreditů, na kterém si lidé mohou věci zkoušet – sám uvažoval o něčem podobném, že by do svého hračkového projektu dal deset dolarů a uživatelé by mohli přihazovat po dolaru.

Vedle toho se rozjela věcná linka o smyslu celého testu. hung se ptal, jestli by se model neměl ptát v každém tiku hry, a ne jen na křižovatkách, když Pac-Man může měnit směr kdykoli. hyperhello namítl, že to možná nehraje roli, pokud je další tah duchů na tu krátkou vzdálenost předvídatelný. soltanov to celé označil za vrchol moderního softwarového inženýrství a tvrdil, že dvoumegový lokální ONNX model na jednom jádru CPU hravě porazí zpoždění síťových dotazů na cloudové API.

Nejvtipnější výměna patří bayarearefugee, který to shrnul větou „platit dva centy za hru, abych ji nemusel hrát, v jaké to žijeme realitě“. Autor se tomu jen zasmál. Vážněji pak zněl dotaz nica, zda se testují i lokální modely běhatelné na CPU – sám prý některé trénoval, včetně hraní Dooma, a pro tenhle benchmark si jeden zkusí natrénovat. Sám autor navíc láká, že si člověk může zahrát Pac-Mana proti duchům ovládaným modely, a přiznává, že překonat vysoké skóre jevu je překvapivě těžké.
