# 1wwl7y6
**Aleph Alpha vydal Kolibri-1: 78B MoE s 3,46B aktivními parametry**

r/LocalLLaMA · u/Nunki08 · 3. října 2026, 13:44 · 527 bodů / 161 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wwl7y6/)

Německá laboratoř Aleph Alpha představila nový otevřený model Kolibri-1. Jde o architekturu Mixture-of-Experts se 78 miliardami parametrů, z nichž je aktivních 3,46 miliardy. Příspěvek s označením New Model kromě samotného vydání odkazuje i na oznámení na síti X a na technickou zprávu ke stažení.

Samotný odkaz vede do sbírky Kolibri-1, která v době načtení obsahovala dvě položky a byla aktualizovaná před třemi dny. Model je k dispozici pod licencí Apache 2.0, tedy i pro komerční využití, a podporuje kontext až 1 milion tokenů.

Nejvíc hlasů posbíral propočet uživatele u/FullstackSensei: trénink na 20 bilionech tokenů na clusteru se 768 kartami B300 zabral čtyři týdny, což při osmi dolarech za hodinu na grafiku vychází zhruba na 4 miliony dolarů. Šílené je podle něj to, jak moc ceny tréninku za poslední dva roky spadly. Na to navázal u/stoppableDissolution poznámkou, že sehnat a zpracovat 20 bilionů kvalitních dat by stálo další miliony navíc, zatímco u/oxygen_addiction čeká, že tahle částka se za rok dva smrskne na pár tisíc a zabere mnohem méně času.

Druhá velká linka řeší výkon. Podle u/Training_Visual6159 je model v podstatě horší než Qwen 3.6 s 35 miliardami parametrů při dvojnásobné velikosti, nejde ale o úplný propadák a slušný první pokus, jen musí velmi rychle přijít verze dvě, aby Evropa a Německo měly šanci. Podobně to vidí u/SnooPaintings8639, podle kterého je Kolibri-1 na první pohled z benchmarků srovnatelný s Qwen 3.5 35B a stojí za zkoušku na sestavách s 96 GB videopaměti. Uživatel u/datbackup k tomu doplnil složení tréninkového korpusu zhruba z 62,5 % angličtiny, 23,9 % němčiny a 13,6 % kódu a pochválil silnou matematiku i slušné agentské schopnosti, i když ho mrzí ztráta s Qwenem právě v němčině.

Nejpodrobnější rozbor přinesl u/tejaskumarlol přímo z technické zprávy. Na celé německé ústavě o 185 KB prý tokenizer Kolibri potřeboval o 15 % méně tokenů než tokenizer GPT-5, v angličtině skončil nerozhodně. V angličtině dosáhl 96,9 bodu na AIME 2025 před všemi MoE v porovnání, slabinou jsou znalosti bez dokumentů s 51,0 body na RGB a vícestupňové volání nástrojů s 39,8 body na BFCL proti 58,2 u GLM-4.7 Flash. Pro domácí běh to podle něj znamená asi 78 GB vah ve FP8, tedy dvě 80GB karty nebo jednu H200, zatím jen přes vLLM plugin laboratoře.

Kolem původu se rozjela i humorná linka. Uživatel u/AdOne8437 připomněl, že Aleph Alpha úzce spolupracuje se Schwarz Digits a částečně ji vlastní, a Schwarz to je Lidl. U/Marcuss2 proto navrhl přezdívku Parkside LLM podle hobby značky z Lidlu, u/Kein_Spass novinku z Evropy vítal, jen postrádal kvantizace a ptal se po podpoře architektury v llama.cpp. Do toho zapadl kritický hlas u/NineThreeTilNow, podle kterého je model z pohledu výzkumu dost rozházený, 20 bilionů tokenů v předtréninku bylo zbytečně moc a v němčině ho stále poráží Gemma 4. Jak to shrnul u/jacek2023, velká zpráva je open source model z Evropy, na což redditoví experti odpovídají, že benchmarky jsou jejich náboženství a není to Qwen.

Pro Evropu hledající vlastní otevřenou cestu je Kolibri-1 spíš nadějným začátkem než vítězem benchmarků.
