# 1y3enps
**GLM-5.4: Loop Transformer míří na kód. Váhy mají přijít až po bezpečnostním ořezu**

r/LocalLLaMA · u/petuman · 23. listopadu 2026, 11:11 · 1074 bodů / 346 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y3enps/)

Z.ai představilo GLM-5.4 postavené na architektuře Loop Transformer, která opakovaně provádí prostřední vrstvy místo jediného průchodu. Model míří především na programování a podle ohlasů v kódu exceluje, zatímco v běžném psaní působí toporně, příliš doslovně a jazykově chudě.

Blog podle citací v diskusi slibuje, že váhy vyjdou jako open weights teprve po dokončení bezpečnostního ořezu, a architekturu obhajuje postupným ověřením na základních modelech o velikostech 1B, 4B, 30B a 750B. Na 30B modelu se stejnou stavbou jako 750B základ při pouhých zhruba deseti procentech tréninkového výpočtu navíc přinesla smyčková verze jasné zlepšení, přičemž výsledný model prochází smyčkou jen dvakrát a druhý průchod navazuje na první se znovuvyužitím klíčů, hodnot a řídkých indexů pozornosti.

Právě věta o zodpovědném vydání se stala rozbuškou. u/LegacyRemaster ji přeložil jako chystané vykastrování kyberbezpečnostních dovedností a vysloužil si tím nejvíc hlasů ve vlákně, u/RedMatterGG namítl, že otevřené váhy mají být právě pojistkou pro ty, kdo nemají přístup k nejlepším uzavřeným modelům a potřebují se bránit proti skupinám, které ho mají. u/__JockY__ mluví o zklamání z ořezávání čínských modelů, u/artisticMink čeká osekání kyberbezpečnosti i bio, hardwarového inženýrství a reverzního inženýrství a u/FrogsJumpFromPussy to shrnuje, že po takovém ořezu z modelu prakticky nic nezbyde.

Druhá velká linka se ptá, kde jsou menší modely. u/DoorStuckSickDuck cituje pasáž o ověření na 1B, 4B, 30B a 750B a ptá se, kde ty varianty pod 30B vězí, u/No-Refrigerator-1672 a u/silenceimpaired v tom vidí náznak možné třicetimilardové verze a rádi by ji viděli i nedotrénovanou. u/goingbankai sní o tom, že by si smyčkovou verzi do čtyř gigabajtů pustil i na starých slabých serverech, jiní se rovnou ptají po svižné odlehčené verzi Flash po vzoru 5.3.

Technicky nejvěcnější hlasy řeší, proč se smyčkuje jen střed. u/NandaVegg vysvětluje, že právě střední vrstvy bývají chaotické a v jediném průchodu špatně využité, takže jejich zacyklení zjednoduší interpretovatelnost a zrychlí běh, u/naftalinus doplňuje, že GLM je předtrénovaný model dodatečně převedený na smyčkový, zatímco jiné přístupy trénují smyčku od nuly. Do toho u/VotZeFuk spílá tomu, že se z jazykových modelů stávají počtářky na kód, kterým se záměrně kazí jazyk, a připomíná postřehy z komunity kolem SillyTavern, že schopnosti GLM přes rozhraní těsně před oznámením viditelně klesly. Protiváhu přidává u/fgnm s nadšením z písně o Hello World, kterou označuje za nejlepší prezentaci, jakou kdy od jazykového modelu viděl.

Vlákno tak čte GLM-5.4 jako další důkaz, že se otevřené modely čím dál víc zužují na programování, zatímco všechno ostatní se obětuje bezpečnosti a číslům v testech.
