# 1wy1o7y
**Frankenserver: domácí AI server z havarované desky**

r/LocalLLM · u/XDude74 · 5. října 2026, 08:44 · 669 bodů / 142 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1wy1o7y/)

Autor přestavěl poškozenou serverovou desku Supermicro, která při nehodě přišla o kanál H prvního procesoru, obrazový výstup i SATA, na čtyřkilowattové napájecí centrum pro úložiště a dvojici karet v620. Grafické karty pak pověsil na naroubovanou desku MC62-G40, protože se Supermicro se karty prostě nechtěly kamarádit. Dohromady tak v sestavě běží 192 GB paměti v kartách 3090 a 64 GB ve v620, další karty v kompaktních vodních blocích s celkem 240 GB už ale autorovi leží bokem a přemýšlí, jak je připojit přes dvojici expanzních desek PEX88096 a shání tip na lépe spolupracující dvouEpycovou desku.

Diskuse se okamžitě chytla spotřeby a vzhledu. u/FinalTap stroj suše označil za dobré topení na zimu, u/PsychologicalFlow143 se ptal, jestli to červené světlo jen svítí, nebo už to vyrábí lávu, a autor odvětil, že červená byla jasná volba, protože sestavě říká HAL900.1. u/sleight42 pak navrhl odpadním teplem vytápět skleník ve vedlejší místnosti, případně jím pohánět turbínu, a dodal, že zákony termodynamiky ať jdou k čertu, když se rýsuje perpetuum mobile. Autor k tomu přiznal, že celé monstrum jede stoprocentně na solární energii, takže je to jeho vlastní malý kousek slunce.

Souběžně se rozjela klasická přestřelka o výkonu. u/sumane12 nadhodil obligátní otázku, jestli to utáhne Crysis, u/Comfortable_Ebb7015 kontroval, že si to umí vyrobit vlastní Crysis, a u/Educational_Let811 stroj odepsal jako kanón na Skyrim. Do vtipkování se míchají i obavy, u/captainabrasive totiž píše, že na odkrytých zásuvkách s napájením je vidět strach v očích.

Věcná linka vlákna řeší, k čemu to vlastně je a jestli to může fungovat. u/Civil_Fee_7862 se ptá, jak autor všechny karty využívá a zda je pronajímá, u/ZealousidealBunch220 prosí o podrobnosti k zapojení PCIe a napájení. u/Technical_Ad_6106 pochybuje o efektivitě, protože úzké PCIe podle něj bude brzdit prefill všech karet a řešením by prý bylo více základních desek. u/SQrQveren zase prosí o lidštější popis, protože čísla dílů jako MC62-G40, PEX88096 nebo H12DSG-O-CPU si z hlavy nevybaví a musel si je googlit. Autor slibuje, že bude o milnících dál informovat, právě teď zkouší rozchodit Kimi K2.6, jen má pocit, že každé řešení na téhle cestě vyrobí dva nové problémy.

Z vlákna tak zůstává obraz kutilského extrému, kde se špičkový lokální hardware rodí z polomrtvé desky, solárních panelů a pořádné dávky improvizace.
