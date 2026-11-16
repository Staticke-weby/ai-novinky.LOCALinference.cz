# 50018817
**bigarrow: AI agent nakreslí na obrazovku šipku, kam kliknout**

Hacker News · franze · 9. října 2026, 13:03 · 391 bodů / 173 komentářů · [diskuse](https://news.ycombinator.com/item?id=50018817)

Vývojář franze představil bigarrow, nástroj, který dává AI agentovi prst. Agent sice umí přepsat monorepo nebo napsat migraci, ale když po člověku potřebuje jediné kliknutí na tlačítko, jen to vypíše do terminálu, na který se nikdo nedívá. Místo toho má rovnou ukázat na obrazovku.

Podle přiloženého popisu jde o nástroj pro macOS, který přes všechna okna a všechny plochy vykreslí šipku, rámeček nebo cedulku s celou větou. Ovládá se třemi příkazy přes souřadnice, obdélník, okno i prvek rozhraní a umí se jako skill naučit Claude Code a Codex. Kliknutí procházejí skrz, fokus při psaní se nehne a šipka se sama odstraní po časovém limitu, odchodu agenta nebo kliknutí na ni. Kreslení samo nepotřebuje žádné povolení systému, vše je v jednom Swift bináru bez démona, ikony, účtu a telemetrie, pod licencí MIT.

Právě tohle „klikej za mě“ vyvolalo nejostřejší výhradu. Uživatel ForHackernews to nazval ponurým: jestli má být člověk jen u mačkání tlačítek pro bota, ať mu rovnou dá root. Autor franze oponuje, že Claude v jeho testech na vlastním Macu odmítal zadávat hesla, měnit bezpečnostní nastavení nebo zakládat účty na externích službách, a to i v režimu Yolo se sudem. Uživatel satyanash zase rýpe, zda se potvrzovací dialogy v agentních postupech vůbec objevují mimo terminál a zda by pomohlo, kdyby dialogy samy vyskakovaly do popředí.

Jiná linka v tom naopak vidí hlavně učitele, ne sluhu. Uživatel inanutshellus píše, že největší potenciál má režim „nauč mě to udělat“, tedy provázející agent místo konajícího, a navrhuje přetočit ukázky na výuku ve složité aplikaci. Uživatel ravila4 souhlasí a vzpomíná, jak se při učení Blenderu dlouho dohadoval s modelem, které tlačítko myslí, když radilo se zobrazením normál. Podobně uživatel FinnLobsien chválí nápad na dokumentaci, protože snímky obrazovky s pokynem „klikni na X“ ho dnes nutí tlačítko stejně hledat poslepu.

Třetí proud se točí kolem pomoci na dálku. Uživatel arshxyz píše, že si u takového nástroje hned představí mámu, které po telefonu vysvětluje stažení a tisk dokumentu, a uživatel conception přitakává, že obří anotační šipka Zoomu je k nezaplacení. Uživatel lbreakjai by za verzi pro iPad, která starší rodiče provede třeba bankovním převodem, dobře zaplatil, a uživatel ghm2180 dodává, že dnes tuhle roli hraje osobně přes vzdálenou plochu. Nechybí ani humor: uživatel isoprophlex žádá duhové kapající šipky a airhorn přehlušující ztlumení, uživatel thih9 varuje, že cílem je být užitečný a nedávat agentům moc značky blink, a uživatel htrp glosuje, že agent sarkasmus nepozná a rovnou to naprogramuje.

Do toho vnesl nadhled uživatel DonHopkins se vzpomínkou, že ukazující ruku jako překryv psal už v roce 1989 v PostScriptu pro NeWS. Vedle nostalgie zaznívá i výhled: uživatel alansaber bere bigarrow jako důkaz, že agenti potřebují vizuálnější rozhraní než postranní panel a vyskakovací okna, a uživatel melvinroest rozvíjí, že by modely měly umět ukazovat na cokoli v aplikaci i v celém počítači, podobně jako lidé zvýrazňovačem na papíře, a pro web zmiňuje WebMCP.

Z vlákna tak zůstává prostá pointa: vysvětlovat kliknutí slovy je pomalé, ukázat prstem je rychlejší.
