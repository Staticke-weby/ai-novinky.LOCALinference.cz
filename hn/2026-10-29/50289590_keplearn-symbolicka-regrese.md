# 50289590
**Keplearn hledá rovnice v datech. Symbolická regrese za sekundy**

Hacker News · owls-on-wires · 29. října 2026, 15:22 · 93 bodů / 11 komentářů · [diskuse](https://news.ycombinator.com/item?id=50289590)

Keplearn je open-source nástroj pro symbolickou regresi, který z naměřených sloupců hledá kompaktní fyzikální zákon. Jméno odkazuje na Johannese Keplera, jenž odvozoval zákony pohybu planet z tabulek pozorování Tycha Braha. Na ukázkovém příkladu s hmotnostmi a vzdáleností program z tabulky odvodí vztah odpovídající Newtonově gravitaci, tedy síla se rovná m1 krát m2 lomeno r na druhou.

Odkazovaný projekt popisuje deterministický engine napsaný v Rustu, který rovnice hledá rekurzivní redukcí od nejlepšího kandidáta. Čte TSV nebo CSV ze standardního vstupu a na výstup tiskne kandidáty jako JSON, distribuuje se jako jediná binárka bez závislostí a přesné zákony má podle autorů obvykle vyřešit v milisekundách s možností limitovat hledání přepínačem pro čas. Konstanty navíc přichytává k blízkým zlomkům a násobkům pí, e a odmocniny ze dvou, přičemž každé přichycení ověřuje, a udávané skóre počítá vždy z vytištěné rovnice. V benchmarku SRBench dosahuje na sadě Feynman bez šumu 75 ze 116 případů, tedy 64,7 %, což je více než 55,8 % uváděných u AIFeynman, na černých skříňkách bez analytického řešení ale záměrně téměř neboduje.

V diskusi nejdřív zaujala samotná forma projektu. kamilstaszewski píše, že stránka vypadá, jako by ji psal člověk, moussore se naopak ptá, zda jde o botí účet, a unicode znaky a komentáře podle něj ukazují na stoprocentně vibe-coded dílo. Do debaty vstoupil verdverm s tím, že se na kód díval a jsou v něm zajímavé nápady, s autorem prý probírali deterministické algoritmy pro symbolickou regresi pod jiným nedávným příspěvkem a obor teď zažívá malý moment zájmu.

Nejdelší linka patří Keplerovi samotnému. seanhunter připomíná, že Kepler začínal s úplně jinou teorií a změnil názor, když data ukázala, že se mýlí, což označuje za výkon obrovské intelektuální pokory. Původně totiž věřil, že dráhy planet určují mnohoúhelníky a vepsané a opsané sféry kolem nich, model zapadající do tehdy známých šesti těles sluneční soustavy, po srovnání s přesnějšími pozorováními ho ale zahodil a začal znovu. likoya k tomu dodává, že Kepler neměl ani kapesní kalkulačku a geometrii musel spočítat bez představy kartézských souřadnic, seanhunter pak odkazuje na Keplerův spis Mysterium Cosmographicum a poznamenává, že právě odtud pochází obrat o hudbě sfér.

Zbytek vlákna se rozbíhá do odboček. westurner avizuje vlastní rychlejší řešení gravitace N těles s orbitální rezonancí přes komplexní varietu a formalizací v Lean 4 a Rustu, které zatím nepublikoval, a připojuje odkaz na rozpracovaný článek o periheliu Merkuru. Tentýž westurner se ptá, jak by si na stejných datech vedl TabPFN, základový model pro malé tabulky. joshmarlow diskusi uzavírá prostým poděkováním, že to muselo být zábavné vymyslet a postavit.

Keplearn tak zaujal jako malý, rychlý a čitelný protipól k velkým modelům: místo aproximace vrací rovnici, které jde rozumět.
