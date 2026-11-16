# 1wwghrd
**Neuroevoluce: jak se AI učí řídit auto evolucí místo gradientního sestupu**

r/ArtificialInteligence · u/egehancry · 3. října 2026, 08:50 · 1002 bodů / 146 komentářů · [diskuse](https://www.reddit.com/r/ArtificialInteligence/comments/1wwghrd/)

Autor sdílel video, ve kterém nechává drobnou neuronovou síť naučit se projet závodní okruh. Místo obvyklého učení s gradienty používá selekci a mutaci: auta, která dojedou nejdál, přežijí a jejich kopie s drobným šumem jedou dál. Příspěvek nese značku Tutorial / Guide a autor k němu dodává, že rád dělá složité věci intuitivní.

Nejživější debata se vedla o tom, zda se auta naučila řídit, nebo jen jednu trať. u/lazo40 se ptá, jestli dokážou závodit i jinde, a autor otevřeně přiznává, že to nezkusil, ale šlo by trať během evoluce náhodně měnit, aby se naučila i nové okruhy. Na to navazuje u/Kinu4U s poznámkou, že náhodná trať pokaždé by znamenala miliardy iterací místo tisíců, u/quietbriars pochybuje, zda jde o skutečné řízení, a u/SirGelson to shrnuje jediným slovem „přeučené".

Druhá linka řeší závodění mezi sebou. u/Smittumi se ptá, jak napsat funkci, aby auta chtěla zlepšovat pozici proti ostatním, protože jinak by umělá formule jezdila v nudném dokonalém vláčku. Autor vysvětluje, že zatím trénuje jen na co nejrychlejší kolo, a pro souboje by musel poslat vozy na stejnou trať se zapnutými kolizemi, aby se naučily předjíždět bez bourání. u/TheBusterHymenOpen k tomu vtipkuje, že zmíněný skutečný závod je Monako, kde je trať tak úzká, že se stejně jen defiluje.

Technicky zvídavé potěšila odpověď na dotaz u/Tube-Goblin na funkce f a g. Autor rozepsal celou síť: sedm vstupů ze vzdáleností ke zdi, rychlosti a úhlu k silnici, dvě skryté vrstvy a 434 parametrů, kde jeden výstup znamená plyn a brzdu a druhý řízení. Běží to vždy ve dvaceti autech po třicet sekund, pět nejlepších se stane rodiči a zbytek jsou jejich zašuměné kopie s dědičnou velikostí mutace. Praktiky pak zajímalo, zda je na zopakování potřeba nadupaný počítač, a autor uklidňuje, že jde o velmi malý model, doporučuje JAX a levný běh na Modal.

Ohlas je jinak nadšený, ale s výhradami k jazyku. u/Disastrous-Action897, který o AI učí, chválí srozumitelné vysvětlení na pochopitelném příkladu, podobně děkuje i u/Fit-Tangerine-6006. Naproti tomu u/SatanRaptor varuje, abychom neříkali, že takhle funguje AI, ale že takhle fungují evoluční algoritmy, a u/According_Gift_7095 připomíná, že tvrzení „nikdo je to neučil" nesedí, protože funkce a výběr navrhl člověk a jde spíš o spolupráci lidí a strojů.

Z videa tak zůstává hlavně názorná ukázka, že i bez dat z lidského ježdění se síť dokáže evolucí propracovat k čistému kolu, byť zatím jen na jedné trati.
