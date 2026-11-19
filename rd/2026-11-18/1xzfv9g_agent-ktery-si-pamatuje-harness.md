# 1xzfv9g
**Agent Google si pamatuje vlastní úpravy. Vývoj softwaru se má skládat, ne začínat znovu**

r/singularity · u/141_1337 · 18. listopadu 2026, 14:58 · 641 bodů / 71 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xzfv9g/)

Google Research popsal systém, ve kterém agent vylepšuje vlastní software a staví na předchozích úpravách, místo aby po výměně modelu nebo úlohy začínal znovu od nuly. Jádrem není přepisování samotného modelu, ale takzvaného harnessu kolem něj — promptů, nástrojů, paměti a skriptů, které určují, jak agent pracuje. Právě schopnost přenést naučené úpravy dál má podle autorů z vývoje udělat skládání, nikoli opakované začínání.

Klíčovou novinkou je paměť optimalizátoru, která přepisování řídí. Ukládá si záznam o každé úpravě, o důvodu, proč ji udělal, co od ní čekal a jaký byl skutečný výsledek. Díky tomu pozná, která minulá oprava patřila ke kterému problému, a nedědí jen hromadu nevysvětlených zásahů. Zdroj k práci u/141_1337 doplnil odkazem na text arXiv 2611.18856. V deseti kódovacích bězích překonalo pokračování s touto pamětí pokračování jen ze starého harnessu v průměru o 2,36 bodu — reálný, ale zatím skromný posun.

Nejvýše v diskusi vystoupal komentář u/michaelTM_ai, který právě tohle upřesnění považuje za podstatné. Váhy modelu se podle něj nikdy nemění, přepisuje se jen to kolem, a proto nemá smysl mluvit o přepisování vlastního mozku umělé inteligence. Na něj navázala debata o tom, co se vůbec smí nazývat rekurzivním sebevylepšováním. Pro u/Orchicon pojem RSI dál znamená, že model dokáže sám sebe přetrénovat, tohle je pro něj jen další forma správy paměti. Podobně u/Expensive_Try_3028 píše, že jde o změnu kontextu kolem modelu, nikoli o chytřejší váhy transformeru v dlouhodobém horizontu.

Vedle pochybností se objevila i zvědavost, jak velký krok to je. Uživatel u/cnhuyaa prosil o vysvětlení pro laiky a škálu od jedné do deseti, u/bartturner se ptal, zda právě tohle stojí za tím, proč jsou poslední modely Googlu tak dobré. U/Happy_Owl4205 zaujal hlavně bezproblémový přenos naučených vzorců při výměně modelu bez přetrénování, u/mega-modz zase řešil, kdo bez člověka ve smyčce rozhodne, kdy přestat a kdy zkusit jiný směr. Odlehčení dodal u/EthanPrisonMike s povzdechem, ať se tedy připoutáme.

Do stejného tématu zapadlo i souběžné vlákno, zda zaměstnanec DeepMind naznačil příchod RSI. I proto část komentářů krotí nadšení: nejde o stroj, který by sám přepisoval sám sebe, ale o pečlivější evidenci pokusů a omylů. A právě v tom je pointa pro čtenáře — pokrok se tu neskrývá v jednom zázračném přepisu, ale v tom, že se příští verze nemusí učit to, co už se jednou osvědčilo.
