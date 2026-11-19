# 1xzqpzu
**Inworld vydal model na izolaci hlasu. Apache 2.0, 48 kHz, běží lokálně**

r/LocalLLaMA · u/mrfakename0 · 18. listopadu 2026, 22:01 · 387 bodů / 53 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xzqpzu/)

Inworld pustil do otevřeného světa model voice-isolator, který z nahrávky vytáhne čistou řeč a potlačí všechno ostatní. Podporuje vzorkování 48 kHz, je licencovaný pod Apache-2.0 a podle autora příspěvku je levný a rychlý na lokální běh. Model je k vyzkoušení na Hugging Face i v komunitním Space.

Nabízí dvě varianty o velikosti 64M a 58M parametrů: offline verzi počítající s osmisekundovými bloky a realtime verzi pracující s dvacetimilisekundovými bloky. Trénováno bylo na přibližně 10 tisících hodinách audia. Nejde o obnovu ani vylepšení hlasu ve stylu Resemble Enhance, ale čistě o izolaci – oddělení řeči od šumu a pozadí.

Nejsilnější moment celé diskuse patří uživateli u/bradjones6942069. Zůstala mu jediná nahrávka hlasu jeho otce, který zemřel ještě před narozením jeho syna, četba vánočního příběhu ve špatné kvalitě. Nic z toho, co dosud zkoušel, nefungovalo, až kombinace tohoto modelu a opravovače od Nvidie. Když otcův hlas konečně uslyšel znovu, rozbrečel se.

Kolem srovnání s konkurencí se rozjela věcná linka. u/coder543 připomněl, že Nvidia před pár týdny vydala komerčně přívětivý model RE-USE, a zajímalo ho přímé porovnání. u/EngelbertStuss přidal vlastní video test Inworldu proti Nvidii Nemotron a Sidonu a poznamenal, že gigový Sidon na procesoru běží hodně svižně a hlas spíš zvýrazňuje. Na tlumených nahrávkách z auta s mobilem položeným daleko mu prý Sidon fungoval výrazně lépe, a dodal, že někdy dává smysl nechat v pozadí trochu šumu kvůli autentičnosti.

Zbytek vlákna řeší praktické nasazení. u/Iostminds by konečně rád odstranil přehnaný smích publika ze svých oblíbených seriálů z 80. a 90. let. u/Secret_Experience_17 a u/maxtrix7 ho chtějí použít na předabování videí a dokumentů – oddělit hlas, znovu ho namluvit a vrátit zpět do hudby. u/grundlegawd poznamenal, že ještě před půl rokem byly otevřené možnosti slabé a ani vestavěný nástroj v DaVinci Resolve nebyl tak dobrý. Ozval se i skeptik u/heliosythic, podle kterého zní výstup pořád dost roboticky a podobnou kvalitu prý loni natrénoval za hodinu na vlastní 4090 s modelem o 7 až 14 milionech parametrů.

Pro každého, kdo má doma zašumělou nahrávku nebo točí v hlučném prostředí, je to malý dárek, který může mít velkou cenu – někdy až takovou, že vrátí hlas člověku, který už tu není.
