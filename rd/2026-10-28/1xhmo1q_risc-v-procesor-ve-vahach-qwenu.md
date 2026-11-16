# 1xhmo1q
**RISC-V procesor přímo ve váhách Qwenu: model umí spouštět instrukce**

r/LocalLLaMA · u/LatentSpacer · 28. října 2026, 13:26 · 811 bodů / 122 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xhmo1q/)

Do vah modelu Qwen3.5-4B se podařilo zabudovat plnohodnotný 32bitový RISC-V procesor, takže model nativně vykonává instrukce. Projekt s názvem Qwenputer tím stírá hranici mezi jazykovým modelem a počítačem, protože výpočet neprobíhá někde vedle v externím nástroji, ale přímo uvnitř forward passu.

K projektu patří vlastní write-up, váhy na Hugging Face a živé demo na ModelScope. Podle popisu funguje tak, že když Qwen vyvolá volání nástroje jako calc, put, get nebo list, vrstvy počítače požadavek zachytí uvnitř forward passu, vykonají kód na virtuálním RISC-V procesoru a odpověď zapíší zpět token po tokenu. Autor příspěvku věří, že právě tohle může mít důsledky pro tool calling a computer use.

Nejvýše hodnocená reakce ale nadšení brzdí. u/Toooooool přiznává, že by rád měl mozek na to posoudit, jestli jde o chytrá volání nástrojů a JSON, nebo o plnohodnotnou práci s tokeny, a dodává, že tak jako tak to vypadá skvěle. u/-dysangel- pak po prostudování podkladů shrnuje, že model musí výpočet stejně odstartovat jistým druhem tool callu, takže jde vlastně o hodně neefektivní a novátorskou variantu volání nástrojů. Za jedinou možnou výhodu považuje extrémně uzavřené sandboxové prostředí, ve kterém tyto volání běží.

Zbytek vlákna se nese v duchu obdivu ke krásně šílenému nápadu. u/mriwantchicken to glosuje jako procesor uvnitř grafické karty, u/BringTea_666 cituje autora, že když už procesor v jazykovém modelu nebyl dost prokletý, přidal mu pro jistotu i souborový systém. u/AdventurousSwim1312 a u/Aggravating-Push-207 se shodně ptají, jestli na tom poběží Doom, u/seamonn zase zajímá, zda zvýšení teploty procesor přetaktuje. u/NineThreeTilNowovi to připomíná lidi stavějící procesory z bloků v Minecraftu: ukazuje to hluboké pochopení logiky hradel a registrů, ale moc užitečné to není.

Vedle vtipů se řeší i vážnější rovina. u/b183729 smeká před lidmi, kteří něco staví jen proto, že chtějí zjistit, jestli to jde, a po přečtení článku v tom vidí zajímavou možnost přidat do modelu přesně definovaný výpočet, který model neobejde, tedy jakési zábradlí. u/sleight42 a u/Rozzemak ale namítají, že grafická karta je z definice horší procesor a že emulace přes registr volání nebo obyčejné vyhodnocení kódu hostitelským strojem by bylo levnější a lepší. A u/jacek2023 by to nejraději otočil: místo procesoru ve vahách chce čip, který má váhy Qwenu implementované přímo v obvodech. u/Ori_553 pak dodává rýpnutí, že formát safetensors měl přesně tomuhle zabránit.

Ve výsledku tak z Qwenputeru zbývá efektní demonstrace, že uvnitř modelu může běžet celý počítač, se kterým lze pracovat jako s jakýmkoliv jiným.
