# 1y46vww
**Claude prý přímo napsal váhy transformeru. Řeší Sudoku i Hanoj**

r/artificial · u/Eliv_nurotic · 24. listopadu 2026, 08:17 · 342 bodů / 100 komentářů · [diskuse](https://www.reddit.com/r/artificial/comments/1y46vww/)

Claude měl místo klasického tréninku gradientním sestupem přímo napsat váhy malého transformeru, který na sto procent řeší bludiště, Sudoku i Hanojské věže. Výsledné modely mají být menší a levnější než běžně trénované a u malých kousků prý jde vysvětlit, k čemu slouží každý jednotlivý parametr. Metoda se má navíc zobecňovat na booleovské výrazy, procházení grafů, řetězce úvah i úlohy zadané přirozeným jazykem, třeba síť lží, sledování zamíchaných předmětů nebo Blocksworld.

Nejvíc hlasů nasbíral údiv u/nedteel, který vůbec nechápe, na čem by se něco takového trénovalo, jestli na syrových vahách všech modelů, co kdy existovaly. Podobně se ptá u/ImmerLustig, zda model váhy napsal od nuly, nebo jen doladil existující síť, a u/duffmanhb dodává, že mu není jasné, co si pod přímým zápisem transformeru prakticky představit. Uživatel u/LongIslandSmedium nadhazuje vlastní tip, že do vah se zakódovalo prohledávání do šířky, tedy klasické BFS.

Věcnou protiváhu přinesl u/ExoticBamboo: transformery normálně používáme na úlohy, pro které neznáme deterministický algoritmus, a učíme je ze zkušenosti, zatímco tady model jen zachytil algoritmy, které už lidé znají. Připomíná, že každý deterministický algoritmus lze zapsat jako matematickou funkci, tedy jako maticové operace, a tím pádem jako neuronovou síť. Na to navazuje u/impatiens-capensis, podle kterého nejde o novinku, protože váhy transformeru aproximující grafové algoritmy umíme ručně nastavit bez gradientního sestupu už roky a odkazuje na dva roky starý článek.

Třetí linka diskuse řeší, zda je stoprocentní úspěch vůbec úspěch. U/ElioPoon píše, že zajímavých není těch sto procent, ale jak k nim model došel: pravidla vepsal rovnou do vah, spíš jako by zkompiloval program, než že by ho trénoval, takže stoprocentní přesnost dává smysl, protože stroj jen běží podle přesného algoritmu. Hned se ale ptá, jestli to obstojí i na větším bludišti nebo na Sudoku 16x16, tedy na instancích, pro které nebyl postaven. Podobně u/peekitup řeší, zda model jen jinak nereprezentuje dataset a zda zabírá méně místa a vyřeší i neviděné případy, zatímco u/Super_Pole_Jitsu, u/Snosnorter a další to shrnují slovem přeučení. Do toho u/Insomniac897 suše glosuje, že každé bludiště ostatně vyřeší i pravidlo vždy zahni doleva, a u/jeffgerickson dodává, že za ten čas si člověk mohl napsat řešič bludiště sám.

Humor obstaraly praktické požadavky: u/doimaarguello prosí o transformer, který platí nájem, u/TenshiS chce, aby jazykový model teď napsal váhy pro model, který píše váhy, a u/wordserif lituje umělé inteligence, které se nově musí bát, že jim práci vezmou metaumělé inteligence.

Z vlákna tak zůstává hlavně otázka, zda jde o chytrou kompilaci známých postupů do drobné a čitelné sítě, nebo jen o elegantně zabalené přetrénování na známých hádankách.
