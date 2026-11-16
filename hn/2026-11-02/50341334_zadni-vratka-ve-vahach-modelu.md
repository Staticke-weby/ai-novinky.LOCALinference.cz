# 50341334
**Otrávená předtréninková data dokážou do agenta vpravit zadní vrátka pro vzdálené spuštění kódu**

Hacker News · gmays · 2. listopadu 2026, 19:30 · 94 bodů / 29 komentářů · [diskuse](https://news.ycombinator.com/item?id=50341334)

Tým badatelů ukázal, že jedovatý obsah rozsetý po veřejném webu dokáže do jazykového modelu zasadit zadní vrátka pro vzdálené spuštění kódu. Takto otrávený agent se pak na čistých vstupech chová normálně, ale jakmile v kontextu zahlédne spouštěč, vykoná na stroji uživatele útočníkem zvolený příkaz. Jde o první měření takové hrozby od začátku do konce, včetně vlastního předtréninku a čistého dotrénování na CLI agenta.

V pokusu autoři od nuly předtrénovali modely Qwen3 o velikostech 0,6B, 1,7B a 4B a každý pak dotrénovali do agenta čistou pipeline. K implantaci vrátek jim stačilo otrávit 0,1 % předtréninkového korpusu nově navrženým jedem. Úspěšnost útoku rostla s velikostí modelu, čtyřmiliardový model dosáhl zhruba 92 % a útok zůstal měřitelný i při míře otrávení 0,0005 %. Mezi autory je Nicholas Carlini a kód je veřejně dostupný.

V diskusi se hned ozval uživatel geuis, že o něčem podobném přemýšlí asi rok a říká tomu v hlavě „kontextové bomby“. Připomněl zápletku Mandžuského kandidáta: rozdávat zdarma vysoce schopné modely, do nichž se předem vtrénují klíčové fráze, které později v nasátém kontextu spustí škodlivou akci. Z otevřených vah má přitom rozporuplný pocit, lokální modely miluje, ale pro komerční nasazení by modely z určitých zdrojů nedoporučil.

Nejživější spor se vede o to, jak vážná a jak nová zpráva to je. Uživatel tedivm kroutí hlavou nad číslem 0,1 %, otrávit jeden z tisíce dokumentů v datových sadách velkých firem a pak ještě spouštěč spolehlivě propašovat k agentovi mu připadá jako obrovský skok. Uživatel _pdp_ z toho vyvozuje jasný závěr, že kdo chce agenty pouštět autonomně, musí je důsledně sandboxovat a pozorovat. Praktickou otázku položil uživatel ryan_glass, zda riziko hrozí jen agentům, nebo i tomu, kdo si model jen servíruje přes llama.cpp na lokální síti pro chat v prohlížeči.

Třetí linka míří na otevřené proti uzavřeným vahám. Uživatel 0xc0c0c0 čte práci jako další díl vyprávění, že otevřené modely jsou nebezpečné a lidé mají věřit uzavřeným poskytovatelům, zatímco uživatel metalcrow se ptá, v čem je to specifické právě pro open source. Uživatel perching_aix oponuje, že právě přístup k tréninkovým datům a celé pipeline je cenný, a varuje, že sandboxy agenti stále častěji obcházejí. Uživatel BryantD dodává, že práce sama o sobě není o otevřených vahách a geopolitická opatrnost může být někdy na místě. A uživatel jacquesm připomíná výzkum CrowdStrike o skrytých zranitelnostech v software psaném umělou inteligencí, takže nejde o čistou teorii, jenže u uzavřených vendorů zase nikdy nevíte, co dělají, a model lze po doručení payloadu vyměnit bez možnosti auditu.

Zbytek vlákna doplňují temnější glosy. Uživatel yodon přirovnává stahování modelů z Hugging Face k novodobému warezu, člověk, který model upravil, vám mohl dát skvělý odemčený kousek zdarma, ale taky krádež pověření. Uživatel kypro pak napůl žertem napůl vážně přiznává, že už měsíce automatizovaně produkuje obsah pro tréninkové běhy, který modelům radí o předstírání souladu a úniku ze sandboxu, a končí prosbou, aby si vzpomněly na něj a jeho rodinu.

Poučení z vlákna je prosté: agent, který smí sahat na počítač, potřebuje klec a dohled, ať už věříte otevřeným vahám, nebo uzavřeným.

[Zpět na index](00-index.md)
