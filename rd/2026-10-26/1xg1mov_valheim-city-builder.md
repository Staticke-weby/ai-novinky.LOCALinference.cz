# 1xg1mov
**Valheim jako city builder: mod, který většinou napsal Claude**

r/ClaudeAI · u/Any-Explanation3814 · 26. října 2026, 17:26 · 364 bodů / 71 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xg1mov/)

Stisk klávesy F7 promění Valheim v městskou strategii. Do osady se stěhují Vikingové, platí daně, chtějí jídlo a medovinu, a když se jim jí nedostane, prostě odejdou. Bossové žijí v táborech, hráč na ně táhne s vlastní armádou a každý poražený boss otevře novou éru s vlastním stavebním stylem.

Většinu C# kódu pro BepInEx a Harmony napsal Claude, od AI osadníků a ekonomiky po domy, které se samy staví kousek po kousku z reálných stavebních dílů Valheimu. Model hru ovládal přes vzdálený příkazový soubor, takže postavil město, vyfotil ho a sám posoudil, jestli vypadá dobře, a když testeři hlásili bossy pronásledující hráče až do města nebo zaseknuté zvědy, našel příčiny a obojí opravil najednou. Sám si také napsal benchmark pro deset až 150 domů, který ukázal, že sloučení hotových domů pro vykreslování zvedlo výkon z 36 na 56 fps. Mod je zdarma na Nexus Mods a Thunderstore, autor si podle vlastních slov nechal design, testování a neustálé popohánění.

Diskuse je hlavně nadšená a zároveň obranná. Nejvíc hlasů má u/Rdqp s tipem, že se na autora hned sesypou odpůrci AI, jen co ji zmíní, a pochvalou nápadu i provedení. Na něj navazuje u/GMoon777 oslavou zapáleného člověka, kterému AI pomohla sdílet nápad „tím nejbláznivějším způsobem", právě v tom je podle něj smysl posilování lidské kreativní jiskry. Několik lidí vlákno popisuje jako podpůrnou skupinu po ostrém přijetí na r/valheim, u/Careless_Silver5525 si posteskl, že je z tohohle grilování unavený.

Věcnou linku vnáší dotaz u/VodkaLait, jestli se dá mezi běžným režimem a stavitelským libovolně přepínat, třeba skočit do pohledu třetí osoby a jít s vesničany bosse dorazit. Automatické shrnutí po padesáti komentářích odpovídá, že přepínání možné je. Nejpodrobněji se do techniky pustil u/kbr89, který rozebírá právě slučování domů: pokud se jen vymění vykreslování dílů za jednu spojenou síť a pod tím zůstanou kolize a WearNTear, podpora a poškození dál fungují po dílech, ale rozbitá zeď zůstane na obrazovce, dokud se dům nesloučí znovu. Doporučuje proto hák na poškození a zničení dílu, který přestaví jen jeden dům, a upozorňuje na vykreslování velkých domů vcelku i na limit 65 535 vrcholů při 16bitovém indexu, takže velký dlouhý dům potřebuje 32bitový formát.

Zbytek vlákna patří hláškám a radám. u/daniellenton lituje opravených bossů, protože pronásledování až do města bylo vlastně nájezdem zdarma, u/NorCalAthlete navrhuje pro mod jméno Age of Valheim. Jinou notu přidává u/angry_queef_master s radou, ať autor tolik nezdůrazňuje AI a hlásí se k modu jako ke svému produktu, jinak si prý zbytečně maluje terč pro iracionální nenávist. A u/ImPinkSnail celou debatu shazuje hláškou, že kritizuje všechno, co nebylo postaveno s děrnými štítky Hollerith.

Vznikl tak příklad, kdy člověk dodal nápad a dotahoval ho a Claude psal, testoval a opravoval, až z vikingské survival akce udělal stavitelskou strategii.
