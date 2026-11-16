# 50211746
**UUIDv7 nefunguje tak, jak si myslíte: timestampy nejsou seřazené**

Hacker News · ibobev · 23. října 2026, 18:39 · 127 bodů / 104 komentářů · [diskuse](https://news.ycombinator.com/item?id=50211746)

Uživatel ibobev nasdílel blogový text, který tvrdí, že UUIDv7 je podivné. Autor v něm rozebírá tři často slibované vlastnosti — monotónně rostoucí identifikátory, užitečné časové razítko a neuhodnutelnost — a dochází k závěru, že striktně neplatí ani jedna z nich. Text navazuje na jeho dřívější rozbor uhodnutelnosti identifikátorů a útoků typu IDOR.

Odkazovaný článek argumentuje hlavně specifikací RFC 9562, která implementacím dovoluje časové razítko posouvat a vůbec negarantuje, jak blízko má být skutečnému času. Jako odstrašující příklad uvádí Pythoní uuid.uuid7, kde po vrácení systémových hodin o hodinu razítko zamrzne a při vyšší zátěži se rozjede do budoucnosti o tisíce sekund. Podobně prý nelze zajistit ani přísnou monotónnost, a to nejen mezi stroji s neseřízenými hodinami, ale ani na jednom uzlu bez čítače či trvalého úložiště posledního razítka. Jediné, na co se lze podle autora spolehnout, tak zůstává jedinečnost a odolnost proti kolizím.

Komunitě se ale tohle orámování příliš nelíbilo. Uživatel hackingonempty namítá, že časová složka nevznikla kvůli čtení času vzniku, ale aby spolu související řádky ležely vedle sebe v indexových stránkách a databáze nemusela dělat náhodné inserty po celém indexu. Na to navazují pkulak se zkušeností s bolestivým zpomalením MySQL na čistě náhodných identifikátorech, NyxWulf s popisem plnění stránek a extentů popořadě a dspillett s vysvětlením, proč zřetězené klíče omezují štěpení stránek a nafukování indexu, který se pak nevejde do paměti.

Druhá linka se vede o to „skoro řazení". Uživatel skrebbel píše, že právě v něm je celý smysl UUIDv7: data jdou zhruba třídit podle vzniku bez kolizí, což se hodí pro kurzory, chat nebo streamování. Uživatel roughly souhlasí, ale dodává, že marketing bez hvězdičky svádí k chybným návrhům tam, kde je potřeba přesnost, třeba v účetnictví. A uživatel vbezhenar kontruje zkušeností, že ani tohle nelze brát doslova, protože okamžik vygenerování a okamžik potvrzení transakce se rozcházejí, takže pozorované pořadí z databáze nemusí být sekvenční.

Zbytek vlákna článek označuje za přehnané šťourání. Uživatel phoronixrly přiznává, že ho nikdy nenapadlo razítko dekódovat a šetřit sloupec, šlo mu jen o výkon primárního klíče, a uživatel mahboi se ptá, kdo vlastně čas z identifikátoru čte a proč by místo toho nepoužil sériové číslo. Vedle toho se řeší alternativy: sedatk odkazuje na text, že UUID často vůbec není potřeba, kune chválí celočíselné klíče v SQLite, zatímco nodamage upozorňuje, že to platí jen pro centralizované webové aplikace. Praktickou tečku přidává uživatel awesome_dude odkazem na NTP, Lamportovy a vektorové hodiny i Spanner s atomovými hodinami jako připomínkou, že přesný čas v distribuovaném světě něco stojí.

Z debaty tak vychází UUIDv7 spíš jako pragmatický kompromis pro databáze než přesné hodiny: zhruba uspořádané, unikátní a šetrné k indexům, ale nevhodné tam, kde se počítá každá milisekunda.
