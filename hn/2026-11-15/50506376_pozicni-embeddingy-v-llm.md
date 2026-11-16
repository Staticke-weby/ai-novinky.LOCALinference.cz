# 50506376
**Jak moderní LLM chápou pořadí tokenů: průvodce pozičními embeddingy**

Hacker News · vismit2000 · 15. listopadu 2026, 13:14 · 238 bodů / 27 komentářů · [diskuse](https://news.ycombinator.com/item?id=50506376)

Sebastian Raschka vydal obsáhlého průvodce tím, jak velké jazykové modely reprezentují pozici tokenu ve vstupu. Postupuje od naučených absolutních embeddingů přes fixní sinusové kódování původního transformeru až po relativní metody typu RoPE a ukazuje, jaké volby dnes dělají otevřené modely. Text má sloužit jako stavební kámen před chystanou analýzou architektonických trendů a jako splátka starého dluhu čtenářům, kteří chtěli konečně srozumitelný výklad RoPE.

Odkazovaný článek vede čtenáře mechanismy s obrázky, trochou matematiky a malou implementací v PyTorch. Na dvojici vět o červené a šedé lišce ukazuje, proč na pořadí slov záleží, srovnává GPT-2, který přičítá poziční vektor k tokenovým embeddingům před prvním blokem, s MiniMax-M3, který vkládá pozici přes RoPE uvnitř pozornosti v každém bloku, a vysvětluje, že kauzální maska dává jen nepřímý signál o pořadí, zatímco explicitní metoda rozliší i vzdálenost jednoho a deseti tokenů.

Jádro diskuse ale obstaral uživatel programjames, který tvrdí, že pro skutečné pochopení je potřeba teorie: poziční embeddingy jsou podle něj reprezentace grup. Rotační embeddingy popisuje jako reprezentace translační grupy, kde se vícerozměrná reprezentace skládá z několika momentových vektorů coby učitelných parametrů, a pro zachování rotace odkazuje na reprezentace speciální euklidovské grupy včetně spinu.

Právě tahle odbočka k algebře vyvolala největší ohlas. Uživatel augment_me namítá, že cílovou skupinou blogu nejsou studenti abstraktní algebry, a připomíná, že řešení může být strukturální, jako u NoPE, kdy pozice vyplyne ze samotné architektury a není třeba explicitní reprezentace. Uživatel mathisfun123 to označuje za naroubovanou teorii lží tam, kam nepatří, a uživatel nlitened dodává, že jde spíš o dodatečnou racionalizaci: výzkumníci prý zkoušejí všechno možné a uchytí se to, co zrovna funguje lépe, teorie se dopíše až zpětně.

Věcnější linka vlákna pak hledá most mezi oběma světy. Uživatel ankkalinna odkazuje na text Jane Street o grupách a pozičních kódováních, zatímco uživatel LudwigNagasena připomíná, že sám autor RoPE svou motivaci vysvětluje mnohem přízemněji, inženýrskými cíli a geometrickou intuicí, a odkazuje na jeho blog. Do toho se uživatel tsimionescu ptá, co mají elektrony coby elementární částice společného s protony a s geometrií čtyřrozměrného prostoru, a uživatel empiricus se zajímá, k čemu by v modelech byly poločíselné reprezentace spinu pro obrázky či trojrozměrné tvary.

Kdo chce nahlédnout pod pokličku transformeru, dostane v Raschkově průvodci pevný základ, diskuse k tomu přidává užitečnou připomínku, že elegantní matematika a inženýrská praxe se k funkčnímu řešení často dostávají z opačných stran.
