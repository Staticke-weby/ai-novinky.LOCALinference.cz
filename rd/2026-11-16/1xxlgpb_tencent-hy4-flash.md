# 1xxlgpb
**Tencent představil Hy4 flash: 224 miliard parametrů, 12 aktivních a milionový kontext**

r/LocalLLaMA · u/noctrex · 16. listopadu 2026, 10:52 · 331 bodů / 114 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xxlgpb/)

Tencent představil Hy4 flash, úspornou variantu své řady Hy. Model má celkem 224 miliard parametrů, z toho 64 miliard tvoří takzvané Engram parametry, na jeden token se jich ale aktivuje jen 12 miliard. Je nativně multimodální a zvládne kontextové okno o délce milion tokenů.

Podle citace v příspěvku ho Tencent popisuje jako dosud nejúspornější model řady Hy s výrazně nižšími cenami za API než u předchozích verzí. Slíbit má i vydání otevřených vah a časté aktualizace, které mají postupně zlepšovat jeho užitečnost a efektivitu v reálné práci.

Nejvíc hlasů v diskusi dostala shoda, které si všiml u/tat_tvam_asshole: Engram tabulka tvoří u Hy4 flash i u Qwen3.8 Flash Next přesně 28,5 procenta všech parametrů. Podle něj to nemůže být náhoda. Navazuje na to i u/Legitimate-Theory156, kterého těší, že engramy po DeepSeeku V4.1 a Qwenu nasazuje už třetí otevřená laboratoř, protože předchozí dva modely podle něj hrály vysoko nad svou váhovou kategorii.

Druhá velká linka vlákna řeší, kdy a jestli vůbec se model dostane ven. Dotaz u/LebiaseD, kde jsou otevřené váhy a kde je model, patří k nejhlasovanějším, u/TheRealMasonMac připomíná, že Tencent zatím nezveřejnil ani váhy plného Hy4 starého zhruba dva týdny. O to větší je chuť na lokální běh: u/jomic01 označuje kombinaci 12 miliard aktivních parametrů a milionového kontextu za velmi pěknou velikost pro domácí provoz, u/Monkey_1505 vítá další přírůstek do málo obsazené kategorie modelů, které se akorát vejdou do 128 GB, a u/Weak-Shelter1698 slaví, že jde konečně o velikost, kterou rozběhá.

Z praktických ohlasů zaujalo srovnání u/CoastAgreeable928, který model nasadil na dlouhou agentní práci se čtením velkého CSV, analýzou dat a generováním sešitu s tisíci vzorci a prezentace. Proti GLM 5.3 Flash byl prý lepší a s DeepSeekem 4.1 Flash srovnatelný, přitom stál patnáctinu a práci dokončil zhruba za šest desetin času. Podobně uvažuje u/crusaderky, podle kterého je datacentrová cena modelu tak levná, že by si ho vybral pro agenta běžícího nonstop pro tisíce uživatelů. Opačnou zkušenost hlásí u/_Zibri_, kterému model při ladění a úpravách v prostředí Opencode opakovaně odmítal spolupracovat a zatím tak dává přednost GLM 5.3 a DeepSeeku 4.1.

Pokud Tencent otevřené váhy opravdu vydá, mohla by komunita získat dalšího silného a levně provozovatelného hráče vedle Qwenu a DeepSeeku.
