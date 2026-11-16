# 1xfqc9x
**Open-source sky camera řízená Claude Code ulovila 17 meteorů**

r/ClaudeAI · u/Terrible_Award_2124 · 26. října 2026, 08:38 · 1292 bodů / 76 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xfqc9x/)

Autor už nechtěl ručně procházet hodiny nočního videa, tahat z něj snímky a přetrénovávat model, který stejně označil každou hvězdu za letící objekt. Postavil proto openskycam: 4K kameru mířící na oblohu, která nahrává nepřetržitě a záběry si drží na vlastním disku. Vše, co umí webové rozhraní, je zároveň volání API a k tomu je přibalený MCP server, takže celý systém umí řídit Claude Code.

Ranní workflow přitom vzniklo skoro samo. Claude Code ho postavil, každou noc ho pouští nad čerstvými záběry, jednotlivé detekce prochází a spojuje do stop, rozlišuje pohyblivé a stojící objekty a třídí je do škatulek na meteory, letadla a pevná světla. Když model pořád hlásil hvězdy jako letící objekty, Claude sestavil dataset z autorem schválených detekcí a model přetrénoval – na nocích, které trénink nikdy neviděl, pak podíl falešných poplachů hvězd spadl zhruba z poloviny na 7 % a zachycení meteorů zůstalo na 90 %. Ráno systém vyháže balast a autorovi pošle jen zajímavé záběry, za zamračených nocí mu se slušností radši nepíše nic.

Komunita to vzala jako vítaný důkaz, že s Claude jde postavit i něco pořádného. Nejvíc se řeší, že pravidla a návody nejsou v proměnlivém promptu, ale přímo v serveru – u/rushabhsheth si z toho chce vypůjčit právě smyčku přetrénování jen na člověkem schválených datech a ptá se, jestli autor ještě namátkově kontroluje, co Claude schválil. Podobnou zkušenost popisuje u/Inevitable_Ask_6956 ze své aplikace na pixel art: dokud byla pravidla jen v promptu, Claude je v půlce zapomínal, teprve kontrolní skript ho donutil opravit si chyby sám.

Druhá velká linka je provoz a poplatky. Na otázky, kolik tokenů takový denní provoz sežere, shrnuje automatický souhrn diskuse, že jádro detekce běží lokálně na modelu YOLO, takže o pálení milionů tokenů nejde. Kdo by to chtěl zkusit doma, potřebuje RTSP kameru, Raspberry Pi, stroj s velkým diskem a účet Cloudflare s doménou, natrénovaný noční model je přímo v repozitáři na GitHubu. Překážkou může být světelné znečištění, na které si stěžuje u/Xotta, i tak ale má doma všechen hardware a chce to vyzkoušet.

Zbytek vlákna patří vtipům o tom, co kamera vlastně loví. Autor přiznává, že nějaká verze mu kouká na oblohu už od roku 2024 a počet UFO je pořád nula, zato meteorů je dost, letadel strašně moc a ptáků tolik, že už mu chybí jen dalekohled do ornitologického spolku. Na to navazuje u/FriesAreTasty4Me přáním, ať to první UFO konečně vyjde, u/ImpluseThrowAway chce budit, jen když se objeví UFO, a u/PykcKeksas se ptá, jestli by to nenašlo i útočné drony. Den se v ukázkovém videu pozná hravě: ptáci jsou tam jako růžové tečky a každý desátý má detailní záběr skutečného ptáka, což u/account-suspenped nečekaně pobavilo.

Kdo má jasno a tmu nad hlavou, má návod i kód k dispozici a ráno mu meteor přistane ve zprávě dřív, než se stihne probudit.
