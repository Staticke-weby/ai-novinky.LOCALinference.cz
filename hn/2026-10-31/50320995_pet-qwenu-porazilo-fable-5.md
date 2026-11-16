# 50320995
**Pět malých Qwenů porazilo Fable 5 v těžkém kódování**

Hacker News · guregodevo · 31. října 2026, 23:46 · 198 bodů / 97 komentářů · [diskuse](https://news.ycombinator.com/item?id=50320995)

Tým složený z pěti nasazení malého modelu Qwen3.8-27B porazil v těžkém programátorském testu LiveCodeBench Hard mnohem větší Fable 5. V pěti bězích na prvních deseti úlohách dosáhl průměru 9,8 z 10, zatímco původní sestava autorů metody GVS5H měla 9,6 a samotný Fable 5 jen 8,0.

Odkazovaný repozitář popisuje řešení jako pracovní postup Memdoor postavený přesně na autorských promptech a smyčce s limitem 128 tisíc tokenů na odpověď. Pět rolí – plánovač, dva navrhovatelé, řešitel a manažer s opravářem – startuje vždy z čistého kontextu a domlouvá se jen přes soubory na disku, o úspěchu rozhoduje skript pouštějící vzorové testy, nikoli model. Všech padesát běhů je zveřejněných včetně dotazů, odpovědí a cen, autor zároveň přiznává, že únik testovacích úloh do trénovacích dat nelze vyloučit.

Nejživější spor se vede o to, zda to znamená vítězství lokálních modelů. Uživatel roenxi spočítal, že s dvoubitovou kvantizací Bonsai 2 běží Qwen 27B na běžném herním stroji rychlostí kolem 50 tokenů za sekundu, takže výkon Fable by šel zvládnout doma s chytrým zapojením. Odpůrci mu to rychle rozbili – SwellJoe i Havoc namítají, že dvoubitové váhy jsou výrazně hloupější, Aurornis dodává, že pro programování začínají být použitelné až kvantizace Q5 či Q6, a ani desítky milionů tokenů denně podle něj nenahradí inteligenci, kterou Astra či Fable předvedou za hodinu.

Druhá linka řeší, v čem je trik týmu, ne modelu. Uživatel topspin hádá, že dělba práce násobí a lépe využívá kontext, protože každý člen má vlastní a užší záběr, edg5000 oponuje, že nejde o množství, ale o správu kontextu – v podobných sestavách je podle něj spousta nevyužitého potenciálu, jen se modely musí umět odchýlit od toho, na co je laboratoře naučily. Do toho uživatel 0xbadcafebee suše rýpl, že malý model s obrovským množstvím tokenů a mnoha dotazy porazil velký model s jedním dotazem – a ptá se, zda se čekalo něco jiného.

Nechybí ani skepse k samotnému měření. Uživatel zihotki volá po dalších testech, protože jde jen o deset úloh ze starého a možná přesyceného souboru, BrandoDev_it mluví o zbožném přání a vikramkr o nové módě laciných sestav, které sbírají body za vyrovnání se špičce na kontaminovaných úlohách místo skutečné agentní práce. Autor guregodevo v diskusi slibuje zkusit chytřejší Qwen 3.8-Flash-Next, který by podle něj mohl dát plných deset bodů rychleji a s menší spotřebou, a přiznává, že nejtěžší úloha trvala přes hodinu při stu tokenech za sekundu.

Z diskuse tak zůstává dvojí ponaučení: promyšlené rozdělení rolí umí malý model vybičovat vysoko, důkaz pro reálné nasazení ale deset úloh ještě nedává.
