# 50106738
**Anthropic a Scion: spor o opisování projektu Mononoke pokračuje**

Hacker News · sunshowers · 15. října 2026, 19:05 · 237 bodů / 76 komentářů · [diskuse](https://news.ycombinator.com/item?id=50106738)

Autor blogu sunshowers.io se po včerejším textu o systému pro správu zdrojových kódů Scion vrací s pokračováním. Původně se snažil být co nejvstřícnější a nedostatečné přiznání zásluh přičítal spíš chybějící pečlivosti, po soukromém potvrzení ale píše o vědomém a okázalém převzetí práce z projektu Mononoke včetně personálního překryvu týmů.

Podobnost podle něj sahá mnohem hlouběji než k pojmu odvozených dat. Týká se celého datového modelu: changesety Scionu odpovídají Bonsai changesetům z Mononoke, podobné je uvažování o indexech včetně blame i serverové API pro dotazy a změny. Model Bonsai popisuje jako záměrně protichůdný tehdejší převaze Gitu, postavený jako Merkle DAG ve stylu write-ahead logu s novátorskými serverovými rebasy, který tým ladil skoro deset let v produkci. Právě proto mu vadí jen strohá zmínka o hard-won lessons od Saplingu a trvá na tom, že problémem není kopírování, ale atribuce.

Do diskuse vstoupil přímo autor původního textu Anthropicu vystupující jako nickg-anthropic. Vysvětlil, že Sapling uvedli proto, že tak Meta sama navenek označuje celý systém včetně serveru Mononoke, a slíbil doplňující poznámku pod čarou. Zároveň uvedl inspiraci Bonsai modelem i esejí Martina Kleppmanna o převrácení databáze naruby, odmítl představu, že by jen požádali Claude o postavení verzovacího systému, a upozornil na novinky nutné při přechodu ze světa Mercurialu do velkého Git repozitáře. Autor blogu sunshowers na to odpověděl, že s novou poznámkou už považuje přiznání zásluh za dostatečné.

Zbytek vlákna se rozpadl na dva tábory. Jeden čte odpověď Anthropicu jako nepřímé potvrzení výtek, jen zabalené do slov o radosti a inspiraci, a přidává širší kritiku velkých AI firem přivlastňujících si společnou práci. Uživatel gopalv připomněl okřídlené tvrzení o kopírování a kradení a napsal, že kopie je pro původní tvůrce potvrzením kvality, problém je spíš v tom, že studna má vedle sebe mincovník a plody nerozděluje těm, kdo zaseli. Uživatel HarHarVeryFunny pak vytáhl rozpor s nářky nad destilací modelů a podivil se, že přestavba hotového návrhu zabrala pět měsíců a sedm lidí, když ji nezvládl agent sám.

Opačný proud volá po klidu. Uživatel durhamg, který se představil jako nejdéle sloužící bývalý člen source control týmu Facebooku, napsal, že s textem Anthropicu neměl problém a těší ho, když nápady posouvají obor dál. Uživatel theptip označil celou při za kyselé hrozny, protože Sapling je pod GPL a zmínka o prior artu od Piperu a Saplingu mu přijde jako slušné přiznání inspirace. Mezitím si ostatní utahují ze shody jmen, kdy Scion zní jako přeskládané Bonsai bez B, jeden z nich cituje Claude s výkladem, že scion je roub naroubovaný na podnož a roubování je běžná bonsajová technika, další dodává, že bizon už byl zkrátka zabraný.

Z přestřelky tak nakonec zbylo rychlé doplnění poznámky a smírné uznání atribuce, zatímco otevřená zůstává obecnější otázka, jak v éře AI poctivě přiznávat, na čích ramenou nový systém stojí.
