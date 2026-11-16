# 50341174
**GPT-6 Astra umí číst a přepisovat váhy modelů. Malému Qwenu zvedl matematiku z 7,9 na 48,1 procenta**

Hacker News · dbreunig · 2. listopadu 2026, 19:21 · 2336 bodů / 735 komentářů · [diskuse](https://news.ycombinator.com/item?id=50341174)

Tým z MIT CSAIL představil výzkum nazvaný Weight-Space Programming, podle kterého špičkový model GPT-6 Astra dokáže nativně číst a přepisovat váhy neuronových sítí. Bez gradientového tréninku přímou editací pouhých 0,016 % vah zvedl malému modelu Qwen3.5-0.8B skóre v testu MATH-500 ze 7,9 % na 48,1 %. Autoři to označují za možný zlom pro optimalizaci i interpretovatelnost.

V textu ukazují i pokusy na malých sítích: Astra prý ze syrových vah poznala, pro jakou hru byla trénována herní politika, a od nuly napsala sítě pro MinAtar a Go, které porazily sítě cvičené algoritmem PPO na stovkách milionů kroků. U zaseknutého autíčka na rampě stačila jediná editace 3,5 % vah, aby se úspěšnost zvedla z nuly na sto procent ve všech testovaných jízdách.

Diskuse je plná úžasu. jstummbillig píše, že to zpětně vypadá zcela zjevně a zároveň potenciálně nesmírně důležitě, a bere to jako další ukázku lidské namyšlenosti, že ho taková možnost nikdy nenapadla. vessenes přiznává otřes: kdyby se ho někdo ráno ptal, řekl by, že modely rozumí vlastním vahám hůř než lidé neuronům, a žádný člověk přece neumí chirurgicky upravit mozek, aby byl lepší v matematice. famouswaffles dodává prosté „svatá prostoto, jak to?", mentos to pro laika přirovnává k významu objevu pozornosti v neuronových sítích.

Nejvěcnější korekci přinášejí l9o a augment_me. Qwen podle nich matematiku už uměl, jen se při řešení zacyklil a v 85 z prvních 96 odpovědí narazil na limit délky. Astra s pomocí Pythonu našla směr v aktivačním prostoru, který smyčku způsoboval, a odstranila ho, což pomohlo i v testu dodržování instrukcí. Důkazem je prý neúspěch u modelu Gemma 3 270M, který se nezacyklil a byl prostě jen slabý v matematice – tam nové znalosti vložit nešlo.

Zbytek vlákna řeší, co to znamená dál. famouswaffles vzpomíná, že rekurzivní sebevylepšování si představoval spíš jako návrh lepších architektur, protože představa přímé editace obřích sítí trénovaných týdny mu přišla zavřená. Wheen ale chladí nadšení: mnohatriliardový obr tu vylepšuje osmisetmilionového trpaslíka, takže o sebevylepšení to nic neříká. Aurornis připomíná, že podobné ruční úpravy vah už lidé dělají u „odcenzurovaných" modelů, jen pomaleji a s více nástroji, a charm137 z toho vyvozuje hlavní ponaučení, že zpětná propagace chyby už není jedinou hrou ve městě.

Čtenář si odnese, že hranice mezi programováním a trénováním se právě začala rozmazávat – místo optimalizátoru typu Adam nastupuje model, který o vahách uvažuje ve slovech.

[Zpět na index](00-index.md)
