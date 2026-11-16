# 1xhjqsi
**Spánkový rámec Google Research: jak naučit LLM nezapomínat**

r/singularity · u/Jame92 · 28. října 2026, 10:51 · 582 bodů / 154 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xhjqsi/)

Google Research představil takzvaný sleep framework pro průběžné učení jazykových modelů. Model v něm střídá aktivní fázi, kdy sbírá podněty do rychlé krátkodobé paměti, a offline spánek, kdy nové poznatky konsoliduje do stabilních dlouhodobých parametrů. Cílem je potlačit katastrofické zapomínání a zbavit se pevného data, ke kterému sahají znalosti modelu.

Odkazovaný článek Aliho Behrouze a Vahaba Mirrokniho popisuje spánek ve dvou krocích: konsolidaci paměti a snění. Při konsolidaci model odemyká předalokované nízko-rankové experty v architektuře Mixture-of-Experts a destilací a imitačním učením do nich přepisuje křehké vzpomínky z kontextu, aniž by přepisoval staré váhy. Ve fázi snění pak náhodně zapojuje nestandardní experty, generuje si syntetické tréninkové vzorky a ty nejlepší dál zušlechťuje doladěním a odměnovým učením. Autoři hlásí téměř dokonalé škálování na benchmarku BABILong až do 10M tokenů, téměř nulový propad při postupném učení překladu do dosud neviděných jazyků jako mančuština a kalamangština a lepší výsledky v matematickém uvažování na testech AIME 24/25 a HMMT 25.

Diskuse se nejdřív chytla velkých slov. Nejvýše hodnocený u/141_1337 napsal, že pokud se průběžné učení opravdu vyřeší, spousta lidí „ucítí AGI". u/sckchui oceňuje eleganci nápadu: původní váhy se vůbec nemění, nové znalosti se učí do dynamických expertních modulů odložených stranou, takže modelu nehrozí, že zapomene původní trénink. u/The_man_69420360 se baví tím, jak moc se tyhle koncepty modelují podle lidského učení, a připomíná, jak často o podobnosti s mozkem mluvil i Ilya na podcastu Dwarkesh.

Vedle nadšení se řeší, jestli už to není proto-rekurzivní sebezdokonalování. u/Cronos988 píše, že spánková fáze je v podstatě trénování nástupnického modelu na syntetických datech z kontextu, a přemýšlí, jak malá přetrénovávaná část proti celému modelu vlastně je. u/Gotisdabest k tomu dodává, že rozhodne praxe: vyladění na míru uživateli, firemní nasazení nebo robotika dávají smysl, ale proti roku 2024 už by to nebyl takový skok. Mezitím u/fxvv poznal prvního autora Aliho Behrouze jako člověka za architekturou Titans a u/Abipolarbears se ptá, proč by Google takovou konkurenční výhodu vůbec zveřejňoval.

Zbytek vlákna sklouzl k vtipům o unavené umělé inteligenci a k filozofii. u/inglandation se těší, až bude moct říct Claudovi, aby šel spát, u/omicron8 hlásí, že jeho AI je dneska k ničemu, protože v noci neměla dost REM spánku, a u/Illustrious_Air_8914 suše konstatuje, že Google vynalezl spaní. Vážnější linku drží u/grimorg80, pro kterého je trvalost základní vlastností lidské mysli, jež běží nepřetržitě od prvních výbojů neuronů až do smrti, a u/BenevolentCheese, kterého fascinuje, jak při stavbě modelů znovu objevujeme vzorce, které už dávno objevila evoluce.

Když to shrnout: místo většího kontextového okna navrhuje Google model, který si v klidu zdřímne a probudí se chytřejší.
