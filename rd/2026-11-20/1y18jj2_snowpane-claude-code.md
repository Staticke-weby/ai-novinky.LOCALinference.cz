# 1y18jj2
**Neprogramátor vytvořil s Claude Code aplikaci Snowpane. Sníh padá na okna i taskbar**

r/ClaudeAI · u/Lol99-Meier · 20. listopadu 2026, 17:55 · 544 bodů / 86 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1y18jj2/)

Člověk bez programátorské praxe si chtěl z plochy ve Windows udělat výhled do chumelenice, a tak vznikla aplikace Snowpane. Klidné sněžení padá na plochu, hromadí se na oknech i na hlavním panelu a při přetažení okna sklouzne dolů. Aplikace je zdarma v Microsoft Store, bez reklam a sledování, a režim natural weather čerpá z výzkumu sněhu a dat z reálných meteostanic.

Autor popisuje dělbu práce tak, že on psal požadavky, testy a rozhodnutí, zatímco většinu kódu v C# a .NET včetně Direct3D 11 a vlastních HLSL shaderů psal Claude Code. Fyziku vloček ladil naživo na notebooku po mnoha kolech zpětné vazby, co vypadá špatně. Za nejtěžší část označuje výkon, který dál řeší.

Diskuse se rychle proměnila v nostalgickou vlnu. Nejvíc hlasů má postřeh u/BetoPaudeConcreto, že je skvělé, když lidé, co nikdy neotevřeli vývojové prostředí, prostě staví věci, které nikdo nepotřebuje a bez umělé inteligence by nevznikly. Uživatel u/LostInDarkForest připomíná cédéčka z let 1998 až 2000 plná tančících postaviček, sněhu a akvárií, kdy největší boj byl sehnat knihovny vbrun, a dodává, že to nepotřebuje, ale chce. Další přidávají vzpomínky na podobné serepetičky z Windows XP, na padající lumíky nebo tučňáky a u/KassFrisson by chtěl zpátky ovce z přelomu tisíciletí.

Druhá velká linka je úklid sněhu. Uživatel u/DrHumorous se ptá, kdo to všechno uklidí, a žádá úklidovou službu s lopatami a košťaty. Nápad rozvíjí u/WarpCoreWitch představou panáčka s lopatou, kterého člověk chytne za límec a přenese na zapadané okno. Do žertu se přidává i návrh u/Objective-Pie-7499 na odhazovací minihru a placené odhazování u cizích lidí s pětiprocentní provizí pro autora, a u/sergen213 zase naříká, že se mu sníh z plochy odhazovat nechce.

Vážnější tón vnáší debata o důvěře a výkonu. Uživatel u/HandshakeOfCO píše, že bez veřejného repozitáře na GitHubu by si aplikaci nenainstaloval. Uživatel u/astrolafi radí honit chybu s pomalým režimem na 144Hz a rychlejších monitorech až do konce, protože překreslování celé plochy každý snímek zbytečně žere grafiku i baterii. Doporučuje úplně vynechat vykreslování při zamčené relaci nebo zakryté ploše, oddělit fyziku od obnovovací frekvence monitoru a data meteostanic načítat mimo vykreslovací vlákno, aby výpadek připojení neznamenal zasekávání.

Čtenář si z vlákna odnese hlavně to, že zbytečná radost je někdy dostatečný důvod něco postavit.

---

[Zpět na index](00-index.md)
