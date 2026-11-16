# 50285319
**Ručně postavený řetěz chyb v Edge. Bez AI a bez přetečení paměti**

Hacker News · austinallegro · 29. října 2026, 07:47 · 237 bodů / 38 komentářů · [diskuse](https://news.ycombinator.com/item?id=50285319)

Výzkumník Orange Tsai z týmu DEVCORE na soutěži Pwn2Own Berlin 2026 předvedl kompletní řetěz zneužití prohlížeče Microsoft Edge končící únikem ze sandboxu. Celý útok stojí na pěti logických chybách a dvou vlastnostech Windows, obejde se bez poškození paměti a vznikl kompletně ručně bez pomoci AI. Výkon mu vynesl 175 tisíc dolarů, 17,5 bodu v klání Master of Pwn a později i cenu Epic Achievement na Pwnie Awards.

V doprovodném blogu autor ukazuje, že cesta začíná u přehlížené komponenty Navigation Throttles v procesu prohlížeče, konkrétně u funkce Edge pro firemní přihlašování přes Entra ID. Protože nová navigace vyvolaná odtud nemá vazbu na původní panel, po přepnutí na jinou kartu dopadne na aktivní tab a útočník tam spustí JavaScript na libovolném webu bez ohledu na CSP. K dotažení k vykonání kódu pak spojuje automatické přihlašování, zisk e-mailu přes službu assets.msn.com a zápis souborů přes rozhraní čtečky ve vlastním schématu read://.

Diskuse se nese hlavně v obdivu k čistotě práce. darkamaul označuje autora za legendu a chválí, že jde o samé logické chyby bez haldových triků, srozumitelně vysvětlené pro čtenáře. Zaujalo ho i přiložené bonusové video s opačným směrem útoku, kdy se vychází z kalkulačky a míří se do Edge, nad kterým mschuster91 žasne a popisuje záplavu nových instancí calc.exe, vstřikování kódu zvenčí a ťukání jedniček až do přetečení.

Největší nevolnost ale budí zdánlivé drobnosti po cestě. tveita označuje za nechutné, že k vytvoření a přihlášení profilu stačí pouhá návštěva firemního webu, deburo vzpomíná, jak se mu Edge záhadně sám přihlásil, a mschuster91 se směje u každého dalšího článku řetězu a bere to jako lekci z ostudy pro Microsoft. Podobně adzm děsí, jak snadno šel z libovolné stránky vyčíst cizí e-mail, a MatthiasPortzel přiznává, že ho nejdřív šokoval trik s whitelistovaným vyskakovacím oknem a pak výdrž dotáhnout univerzální XSS až ke spuštění kódu.

Souběžně se řeší hlubší příčina i forma textu. its-summertime lituje těsného propojení webu s prohlížečem, xnickb v tom vidí nemilovaný kód přidělený juniorovi a imtringued tvrdí, že zvláštní zacházení s vlastními doménami si o zranitelnosti přímo říká. Vlákno o lidském řemesle otevřel zhiyan, cubefox oponuje, že lidé mizí spíš proto, že je modely v hledání chyb přehrávají, a spor o větu, ať si detaily navigace čtenář doplní s agentem, uzavírají maeln, est, russelg a cush konstatováním, že článek je ve skutečnosti mimořádně podrobný a čtivý.

Čtenář si tak odnese nejen návod na pět děr v jedné, ale hlavně připomínku, že největší riziko často nevzniká v jádře Chromia, nýbrž v přidaných firemních vychytávkách kolem něj.
