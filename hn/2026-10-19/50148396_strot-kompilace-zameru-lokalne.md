# 50148396
**Strot: záměr jednou zkompilujte, rozhodnutí pak běží lokálně**

Hacker News · solohunter001 · 19. října 2026, 06:32 · 23 bodů / 13 komentářů · [diskuse](https://news.ycombinator.com/item?id=50148396)

Vývojář solohunter001 představil na Hacker News projekt Strot, který má zlevnit a zrychlit opakované rozhodování umělé inteligence. Místo aby se na každý tiket nebo text znovu sahalo po velkém modelu, popíše se záměr jednou a dál už všechno běží místně. Cílem je přesunout drahou a nevyzpytatelnou část práce mimo provoz, podobně jako kompilátor přesouvá práci mimo horkou cestu.

Podle popisu na GitHubu velký jazykový model při první kompilaci syntetizuje popisky, projekci vstupů a obslužné rutiny a výsledek se uloží jako zmrazený artefakt. Za běhu pak každý záznam posuzuje malý model Julia-1 se 144 miliony parametrů na procesoru, s latencí kolem 60 ms, nulovými mezními náklady a bez volání API, a vrací jen ohraničený typovaný JSON. Kompilátor si vítězné značkování vybírá měřením na učitelem olabelovaném vzorku, práh pro zdržení se při nejistotě kalibruje konformní predikcí a artefakt, který neprojde přes zlaté referenční příklady, se vůbec nenasadí. Na směrování se tak stejný model zlepšil ze 74,8 % na 92,5 % a na klasifikaci textu se skrytými popisky ze 72,7 % na 86,7 %, instaluje se příkazem pip install strot-ai.

První reakce mířila na formu. dpacmittal se ptá, jestli to nebylo celé „vibe coded", protože readme prý vypadá jako čistý Claude bez lidských úprav, a majorchord dodává, že si autor nedal práci ani s vlastním komentářem k příspěvku.

Druhá linka je neporozumění smíšené s humorem. publlus_enigma koncept chválí, ale přiznává, že z readme stále nepochopil, co přesně nástroj dělá a jak, a prosí o více detailů. wonnage do toho vtipkuje citací o duchovi na dva kroky a radí prostě požádat model, ať napíše program a ten pak pouštět lokálně navždy, na což ghurtado suše odpovídá, že přesně tohle projekt dělá.

Zbytek se ptá po podstatě. luhgor nadhazuje očividnou otázku na rozdíl proti rozhodovacím modelům ve stylu Jev, razingeden se pozastavuje nad větou o stropu modelu na nenávistných tweetech a sysguest prosí o hlubší rozbor kalibrační matematiky a návrhu cache. Filozofickou tečku přidává jMyles, podle něhož je „jednou odvodit, výslednou logiku pak opakovat navždy" jeden z nejdůležitějších a nejlidštějších způsobů, jak si soužití s umělou inteligencí představit.

Kdo hledá levné routování tiketů na vlastní infrastruktuře, má tu kandidáta – jen bude muset komunitu přesvědčit, že za ním stojí víc než vygenerované readme.
