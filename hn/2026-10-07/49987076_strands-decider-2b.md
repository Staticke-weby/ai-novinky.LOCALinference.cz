# 49987076
**Strands Decider 2B: malý open-source rozhodovací model**

Hacker News · gmays · 7. října 2026, 04:02 · 275 bodů / 78 komentářů · [diskuse](https://news.ycombinator.com/item?id=49987076)

Tým Strands Agents představil Strands Decider 2B, malý otevřený model určený čistě na rozhodování. Místo generování textu vybírá z nabídnutých možností a ke každé přiřazuje skóre spolehlivosti, přitom běží lokálně na běžném procesoru i grafice v řádu desítek milisekund.

Oproti velkým jazykovým modelům je v tomto úzkém úkolu rychlejší a úspornější, zato neumí psát, programovat ani shrnovat dokumenty a na složité problémy se nehodí. Technicky vzali trup předtrénovaného modelu Qwen3.5-2B, odebrali mu hlavu pro generování textu a nahradili ji malou ukazovací hlavou s něco přes milion parametrů. Podle tvůrců je model na veřejné sadě JevBench třetí z 33 v kategorii do dvou miliard parametrů a na grafice RTX 3090 rozhoduje typicky kolem 115 ms, na MacBooku s čipem M3 kolem 153 ms.

Nejživější je v diskusi praktická linka o tom, kam tak levné a rychlé rozhodování nasadit. miguelspizza ho provozuje přímo v rozšíření pro Chrome na třídění e-mailů a chválí kombinaci velikosti, schopností a rychlosti, k tomu přihodil i verzi pro WebGPU a živé demo. Podobně mattstir si ho maluje jako mozek jednoduchého domácího asistenta, který by rozpoznal „nastav světla na 30 %“ od „jaké bude počasí“ a to druhé poslal dál levnému modelu, a davvie ho chce zkusit na menší automatizace na Macu mini.

Do vlákna vstoupil i jeden z autorů vystupující jako mjb, který děkuje za pochvalu srozumitelně napsaného oznámení a přiznává, že texty s jeho jménem nepíše umělá inteligence. Nejvíc ho lákají hybridní agentní postupy, něco mezi pevnými kroky typu StepFunctions a plně autonomními agenty s největšími modely, kde Decider převezme rutinní volby jako směrování, výběr nástrojů, hlídání pravidel nebo správa kontextu. K běhu na procesoru hlásí gopalv z M3 v dockeru přes 1700 ms na dotaz a avereveard zhruba půl sekundy na rozhodnutí na šesti jádrech, takže na optimalizaci pro notebooky se ještě čeká.

Zbytek diskuse se rozpadl do vtipů a terminologie. adenta si přeje komika, který vydá rozhodovací model, za nímž bude ve skutečnosti člověk Jerry odpovídající na otázky, a ostatní hned přidávají odkazy na Jerryho rozhodovatele a závodění s Jerrym. Vážnější debata řeší, proč se binárním volbám říká noul, což haarts, hiimkeks a lr1970 vysvětlují jako kousek z Bernoulliho rozdělení, zatímco WASDx by byl raději, kdyby se prosadilo strohé „predicate“ z nového Decisions API od OpenAI místo humbuku kolem rychlého myšlení. Skepsi přidal soltanov s tím, že dobrá kalibrace na benchmarku ještě nezaručí spolehlivost na neznámých datech z provozu, na dotaz po obrazových vstupech pak mjb odpověděl, že verze v21 už vidění umí.

Čtenář si tak odnese jednoduchý obrázek: na těžké přemýšlení velké modely, na tisíce drobných ano či ne po cestě malý rozhodovač, který běží doma a nestojí skoro nic.
