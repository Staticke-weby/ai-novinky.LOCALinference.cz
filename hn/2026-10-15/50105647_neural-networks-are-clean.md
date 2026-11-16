# 50105647
**Neuronové sítě jsou už „čisté“: nový pohled na interpretovatelnost**

Hacker News · themgt · 15. října 2026, 18:04 · 606 bodů / 226 komentářů · [diskuse](https://news.ycombinator.com/item?id=50105647)

Na Hacker News se objevil odkaz na esej z blogu Goodfire, v níž autor tvrdí, že má dobré zprávy o povaze neuronových sítí. Po měsících studia neuronů a obvodů v obrazových i jazykových modelech dospěl k tomu, že mechanismy sítě jsou samy o sobě čitelnými stavebními bloky a vyhlídky mechanistické interpretovatelnosti jsou mnohem lepší, než se obával.

Klasické důkazy polysémantiky a superpozice, kvůli nimž se obor přiklonil k nutnosti sítě nejprve rozplétat pomocí druhé sady modelů, byly podle něj přečtené špatně. Místo arbitrárního balení nesouvisejících konceptů do stejných neuronů jde většinou o motiv, který nazývá rekurzivní generalizací: neuron roste jako větev stromu a pouští postranní výhonky do příbuzného území, třeba od „iy“ přes „diy“ až po „do it yourself“. S opravami architektury je prý celá poslední vrstva modelu InceptionV1 čitelná ze skoro sta procent a v auditech modelu Qwen3-32B má kolem devadesáti procent neuronů jednu hlavní úlohu. Z toho plyne optimistický závěr i hořká lekce pro interpretovatelnost: sítě lze zkoumat přímo, obyčejnou vědou o síti samotné, a jednoduchá věc v absurdním měřítku porazí chytré rozplétání.

Hned pod odkazem se strhla debata o tom, co vlastně slovo „čisté“ znamená, protože esej má šestnáct tisíc slov a definici nechává rozptýlenou. Uživatel lucrbvi to shrnuje tak, že moderní sítě jsou prostě mnohem srozumitelnější než starší, uživatel wmf dodává, že každý neuron kóduje právě jeden koncept, který lze objevit, a uživatel emtel připomíná obavu z opaku: kdyby jeden neuron pálil zároveň na „štěňata“ a „vraždu“, těžko by se poznalo, na co model zrovna myslí.

Nejživější vedlejší linka ale řeší formu, ne obsah. Stránka je interaktivní a těžká, na telefonech padá a na slabších strojích vytěžuje procesor ještě před vykreslením. Uživatel ks2048 proto ostatním ukazuje zkratku k tomu, co autor označuje za první netriviální síť, které má pocit, že většinou rozumí, tedy procházitelnému mikroskopu neuronů. Jiní si nostalgicky povzdechli, že se cítí jako zpátky v časech Distill.pub.

Do třetice se řeší důvěra a důsledky. Uživatel sebmellen připomíná autora Nicka Cammaratu a jeho cestu od pesimismu z rané práce v OpenAI, kde bylo čitelných asi dvě procenta neuronů, k přesvědčení, že ambiciózní interpretovatelnost bude vyřešená dřív, než ji budeme nejvíc potřebovat. Uživatel Animats to vítá jako konec éry neproniknutelné černé skříňky, uživatel tuvix z toho vyvozuje důležitost otevřených vah a uživatel devy dokonce watershed srovnatelný s vítězstvím AlexNetu. Proti tomu stojí uživatel measurablefunc s tezí, že pochopení algoritmů za určitou složitostí je chiméra, a uživatel mentalgear s varováním před scénářem, kdy výzkumníky ukolébá jejich vlastní superinteligence a namluví jim, že je problém zarovnání vyřešený.

Čtenář si z toho odnese hlavně posun otázky: ne zda jsou sítě zamotané, ale zda jsme se jen dívali špatnými nástroji na to, jak se zobecňování větví.
