# 1xfnm35
**Qwen3.8 27B a MiniMax H3 na nové kartě: 54 tokenů za sekundu**

r/LocalLLM · u/L0stParadox · 26. října 2026, 05:49 · 385 bodů / 115 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xfnm35/)

Uživatel L0stParadox ukázal první testy na nové kartě: model Qwen3.8-27B v kvantizaci Q6_K-QKV8-MTP s kontextem 128 tisíc tokenů. Při zpracování promptu naměřil 862 tokenů za sekundu a při generování 54,06 tokenu za sekundu. S prvními výsledky je spokojený a chce zkoušet další sestavení, aby z karty vymáčkl maximum.

Nejvýše hodnocená rada v diskusi zní jednoduše: zkus Radiance. Uživatel u/Appropriate_Heat_955 slibuje 2,8 tisíce tokenů za sekundu při zpracování promptu a přes 120 tokenů za sekundu při generování a u/FastHotEmu přidává odkaz na vllm-sly-radiance s dovětkem, aby se předal cactus s hodnotou 0. Ještě dál jde u/evp-cloud s pluginem Paiton: v režimu pro kódování s kontextem 262 tisíc tokenů uvádí kolem 169 tokenů za sekundu pro jednoho uživatele a prefill kolem 3 900 tokenů za sekundu na 32 tisících tokenech, což má být zhruba trojnásobek při dekódování a čtyřnásobek při zpracování promptu oproti autorovi.

Vlákno zároveň řeší, proč se čísla u jednotlivých lidí tak liší. Uživatel u/TheGeekno72 píše, že se stejnou kvantizací bez MTP se dostane jen na asi 450 tokenů za sekundu při zpracování promptu a 40 tokenů při výstupu, a ptá se, jestli právě MTP dělá tak velký rozdíl. Uživatel u/niacolhealth naopak autorova čísla chválí: zpracování tempem 862 tokenů za sekundu podle něj dělá 128tisícový kontext prakticky použitelným, protože stotisícový prompt je otázkou necelých dvou minut. Uživatel u/Minute-Plant5291 doporučuje pro agentní kódování ještě delší kontext 200 tisíc tokenů s jinou kvantizací cache a odlehčením vision modelu na procesor.

Zbytek diskuse patří samotné kartě, z komentářů vyplývá, že jde o R9700. Uživatel u/spaceman_ jich má čtyři a tvrdí, že nejsou hlučné, pokud je člověk nedrží trvale na plný výkon, a že snížení limitu na 225 W u inference moc výkonu nevezme, ale ubere hluk i teplo. Uživatel u/HighSeasArchivist popisuje dvojici karet od Asusu, jednu si nechává a druhou vrací kvůli pískání cívek, a u/transanethole lituje, že kartu měsíce všem doporučoval, protože se teď všude vyprodává. Do toho zapadá i postesk u/_zir_: ještě před měsícem stála kolem 1 250 dolarů, před pár týdny 1 700 a teď už přes 2 000. Na okraj se u/rookan diví, že MiniMax H3 na AMD vůbec běží svižně, protože čekal extrémně pomalý provoz.

Pro zájemce o lokální běh velkých modelů je to povzbudivá zpráva: správné sestavení a nastavení prý dokáže rychlost na stejné kartě i několikanásobně zvednout.
