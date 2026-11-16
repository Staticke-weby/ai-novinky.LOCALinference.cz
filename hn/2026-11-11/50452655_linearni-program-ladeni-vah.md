# 50452655
**Lineární program nahradil osmihodinové ladění vah modelu**

Hacker News · emschwartz · 11. listopadu 2026, 13:30 · 269 bodů / 38 komentářů · [diskuse](https://news.ycombinator.com/item?id=50452655)

Navazuje na práci Sparks of Weight-Space Programming z MIT CSAIL, ve které model GPT-6 Astra upravoval váhy malých sítí bez gradientů. V jednom experimentu změnila Astra jen 0,016 % vah modelu Qwen3.5-0.8B a přesnost na MATH-500 stoupla ze 7,9 % na 48,1 %. Autor blogu její hledání analyzoval jako lineární program a ukázal, že osm hodin zkoušení jde nahradit několika minutami výpočtu.

Blog vysvětluje zásek v přemýšlecích smyčkách, kdy se malý model opakuje dokola místo dokončení odpovědi, jako posun zbytkového proudu jedním směrem. Astra našla směr smyčky a ve dvou vrstvách přepsala sloupce matice tak, aby tlačil opačně. Tatáž úloha jde zapsat jako lineární program s penalizací L1 normy, která nutí úpravu k řídkosti, takže řešení mění osmkrát méně vah při stejných výsledcích. Vlastní GPU solver PDHG našel řešení za zhruba minutu, zatímco běžný HiGHS trval přes dvacet minut, a průměrný posun šlo dokonce přidat jen jako steering vektor při inferenci.

V diskusi nejvíc rezonuje vystřízlivění z původních titulků. ultimatefan1 píše, že zprávy z minulého týdne vypadaly, jako by se frontier modely naučily číst a chápat váhy přímo, což mu přišlo nepravděpodobné, protože se modely učí z tokenů a odměn. Astry výzkum tak podle něj byla spíš šikovná série malých experimentů s úpravou vah a nález opravy jednoho problému, přičemž rychlejší postup přes lineární program je skvělý, ale od velkých titulků má daleko.

Na to navazuje debata, jestli by Astra zvládla upravit sama sebe. FrustratedMonky se ptá, zda popisuje mocný model, jak edituje menší modely, a kragen v narážce na stáří metody odpovídá, že jde vlastně o lineární optimalizaci ze čtyřicátých let, která edituje model Qwen. rsfern namítá, že princip je stejný, najít sémantický směr nežádoucího chování a odtlačit se od něj, takže s přístupem k vahám nevidí důvod, proč by ho velký model nemohl použít na sebe, klidně i za běhu.

Třetí linka řeší, co z toho plyne pro nástroje. jsw97 čte výsledek opačně, než zní titulek: nejde o to, že lineární program nahradil Astru, ale že by jí solver s vodítkem v podobě lineárních omezení mohl šetřit zdlouhavé pokusy a vyjadřovat její záměr hned, načež by model řešení dál vylepšoval. boxfire si vysnívá model, který by externí solvery, unifikaci nebo dokazovače nepoužíval přes zdlouhavá volání nástrojů, ale měl je takříkajíc zapečené v uvažování. A dansitu podotýká, že jednoduchost opravy naznačuje, že by se měla dít už při tréninku pomocí regularizace.

Stranou nezůstaly ani širší souvislosti. nullc glosuje, že se tím krok za krokem znovuobjevují techniky, které se už delší dobu používají k odstraňování odmítání z modelů. ricksunny žertuje, že by bylo divoké, kdyby operační výzkum ze čtyřicátých a padesátých let doplnil klíčový krok k rekurzivnímu sebevylepšování, na což jbjbjbjb odpovídá, že by to sebevylepšování nebylo, jen jiný algoritmus pro váhy. Praktický přesah přidává mirekrusin s nápadem na destilaci ve váhovém prostoru, kdy by se sbíraly páry příkladů, hledaly směry chování a lineárním programováním se dolaďovaly řídké úpravy vah.

Z článku si čtenář odnese, že za efektní editací se skrýval prostý lineární problém a klasická matematika tu výrazně předběhla osmihodinové zkoušení pokusem a omylem.
