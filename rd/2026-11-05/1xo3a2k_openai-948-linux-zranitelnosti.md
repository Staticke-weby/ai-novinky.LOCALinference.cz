# 1xo3a2k
**OpenAI tvrdí, že jeho bezpečnostní model opravil 948 zranitelností v Linuxu**

r/singularity · u/Distinct-Question-16 · 5. listopadu 2026, 00:25 · 821 bodů / 151 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xo3a2k/)

OpenAI oznámilo, že jeho bezpečnostní model našel a pomohl opravit 948 zranitelností umožňujících eskalaci privilegií v Linuxu. Zpráva se na síti objevila jako snímek z účtu OpenAI na X a okamžitě vyvolala debatu o tom, v jakém stavu je dnes bezpečnost operačních systémů.

Z obrázku, který diskutující rozebírají, vyplývá širší záběr celé akce: model označil celkem 2 308 potenciálních nálezů. Samotná volání API, tedy výpočetní práce modelu, přišla podle stejného snímku zhruba na 1,2 milionu dolarů.

Nejstručnější reakci napsal u/MisfiledCentury, že je to pořádná porce chyb pro eskalaci privilegií, a u/Cryptobench k tomu dodal, že si člověk má představit, jaké schopnosti v tuhle chvíli mají státní aktéři. Jeho radou je rovnou předpokládat, že jste kompromitovaní. Podobně uvažuje u/gg23456gg, kterého děsí hlavně objem nálezů: jestli se tolik děr našlo v dobře udržovaném kódu Linuxu, jak máme kdy všechno stihnout opravovat, a co teprve méně testovaný kód.

Do perspektivy to zasadil u/Jenkinswarlock, když připomněl červnový výzkum OpenAI, který tehdy popisoval automatické vygenerování 24 exploitů pro eskalaci privilegií a osmi ukázek úniku informací. Proti opraveným chybám je to zhruba čtyřicetinásobek, proti všem označeným nálezům dokonce asi šestadevadesátinásobek, jak sám počítá. Navazuje na něj u/FateOfMuffins otázkou, zda tohle všechno uniklo předchozím modelům Mythos, Sol a Astra, které měly podobné problémy čistit už od dubna.

Hodně se řeší cena. U/EffectiveMedium2683 nevěřícně žasne nad účtem jen za API, ale u/just-plain-wrong namítá, že je to ve skutečnosti výhodný obchod proti ekonomickým škodám, které dokáže napáchat jedna kritická chyba v jádře. U/Chekhov_ z toho vyvozuje znepokojivou otázku, jestli průměrného útočníka od řádění s exploity dělí už jen cena běhu modelů, zatímco u/ripMyTime0192 dodává, že pokud tolik děr bylo v Linuxu, ve Windows si to raději ani nepředstavovat. Objevují se i pochybnosti, jestli už jsou opravy skutečně v Linuxu, jak se ptá u/t3hjs, nebo zda dnes každý produkční server obsahuje všechny ty neopravené eskalace, jak provokativně nadhazuje u/Palbi.

Ať už je konečné číslo jakékoli, vlákno se shoduje v jednom: éra, kdy se dobře udržovaný open source považoval za téměř neprůstřelný, s příchodem bezpečnostních modelů končí.
