# 50455332
**Proč neexpedujeme rychleji? AI zvyšuje aktivitu, ne výsledky**

Hacker News · azhenley · 11. listopadu 2026, 17:33 · 111 bodů / 103 komentářů · [diskuse](https://news.ycombinator.com/item?id=50455332)

Christian Bird vystoupil 30. října 2026 na softwarově-inženýrském semináři UC Irvine s přednáškou Proč teď neexpedujeme rychleji? Jeho teze zní, že kolem kódu díky AI vzniká mnohem víc aktivity, ale výsledky se nemění úměrně tomu – popisuje to jako mezeru mezi aktivitou a výsledkem. Kód se generuje rychleji, expedice a dopad na uživatele ale zůstávají zhruba na místě.

Odkazovaná stránka shrnuje jednadvacetiminutový záznam s titulky, slajdy i příručku a odkazuje na sérii výzkumných prací. Jde mimo jiné o pracovní studii NBER Writing Code vs. Shipping Code o efektech jednotlivých generací nástrojů, o srovnání agentů pro code review a hledání chyb a o texty o tom, kde vývojáři autonomii AI zastavují. Základ tvoří i třicet rozhovorů o tom, co AI vývojářům nově odemkla, a praktické doporučení měřit expedici a výsledky, ne objem vygenerovaného kódu.

Nejhlasitější odpověď vlákna zní: ale my expedujeme. Uživatel throwitaway222 popisuje, že plné migrace, které dřív zabraly čtyři týdny koordinace tří týmů, jsou dnes jediným pull requestem hotovým za den, a 0xb0565e486 shrnuje zkušenost většiny větou, že se měsíc práce smrskl do jednoho dne. Podobně to vidí hackboyfly z retailové firmy nebo ferguess_k, který ale hned dodává podstatnou výhradu – expedice zrychlila, lepší produkty z toho nutně neplynou.

Druhá linka diskuse proto řeší, kam se nová kapacita reálně lije. Uživatel 9cb14c1ec0 píše, že expeduje mnohem víc, ale zákazníci by si toho nemuseli všimnout: konečně se dělají odložené přepisy, záplatují se bezpečnostní díry a zkracuje se čas od nahlášení po vyřešení podpůrných tiketů. Na to navazuje intrasight s masivní interní aplikací, kde díky modelům splácí obrovský technický dluh asi za pětinu času, a MBCook dodává, že spousta nové kapacity jde na stabilizaci, protože starý kód byl často tak chatrný, že na něm nešlo dál stavět.

Třetí spor je o úzká hrdla. Uživatel choult tvrdí, že vzrušení se točí kolem produktivity inženýrů, zatímco review a QA zůstávají ucpané, protože firmy pustily kohoutek nového kódu, aniž by nejdřív postavily dálnici. ManuelKiessling to glosuje starým přirovnáním, že rychle jezdit umožňují hlavně brzdy, tedy testy, a MisterPea označuje za největší brzdu CI/CD a experimentování na straně inženýringu a sladění s produktem na straně byznysu. Uživatel xp84 to říká ještě přímočařeji: se dvakrát tolika produktovými manažery by stejný tým stihl mnohem víc.

Nechybí ani ironie. Uživatel bad_haircut72 žertuje, že se zbavili databáze a nechávají model spravovat soubory s údaji zákazníků, takže se rychlost dodávání za poslední týden zečtyřnásobila, a smy20011 kontruje, že rozhodně přibývá rozbitých funkcí, které se po chvíli zase tiše odstraní. Z toho plyne pointa, kterou opakuje i jayd16: řádky kódu a commity se nepočítají, podstatné je, zda se k uživatelům dostává víc funkcí rychleji.
