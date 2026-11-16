# 50091794
**Neckbeard: DevOps plugin pro vašeho kódovacího agenta**

Hacker News · bealesh · 14. října 2026, 19:45 · 64 bodů / 49 komentářů · [diskuse](https://news.ycombinator.com/item?id=50091794)

Na Hacker News představil bealesh svůj projekt neckbeard, plugin pro kódovacího agenta, který má z aplikace udělat cloudovou infrastrukturu včetně měsíčního účtu. Vychází z postřehu, že agenti píší aplikační kód dobře, ale na pokyn „nasaď to na AWS" s jistotou vychrlí stovky řádků věrohodně vypadajícího HCL se skupinou otevřenou do světa a hvězdičkou v IAM politice, aniž by tušili, kolik to bude stát.

Práci proto dělí na dvě poloviny: lidé udržují katalog verzovaných OpenTofu modulů, testovaných v CI pro jeden poctivý tvar zátěže od kontejnerového obrazu přes worker a cron až po Postgres, úložiště a tajemství, zatímco agent jen čte repozitář a skládá profil aplikace s odkazy na soubory. Deterministické jádro v Go pak z hashově ověřeného blueprint.yaml vyrenderuje infrastrukturu, pipeline pro GitHub Actions či GitLab CI i ceník od Infracostu, nikdy nepřepíše ručně upravený soubor a když něco neumí, raději vydá pojmenované zjištění, že katalog třeba Redis zatím nemá.

Nejživější linka je otázka, proč další vrstvu mezi sebe a Terraform vůbec chtít. hangrybear666 se upřímně ptá, k čemu mu bude další rozhraní mezi ním, plánem a běžícím prostředím, a bealesh odpovídá přirovnáním k Rails či Phoenixu: generátor syntaxe nemá názor na architekturu ani na provozní náklady. Podobně janwirth nadhazuje, proč prostě nepsat OpenTofu a Ansible, na což autor přiznává, že kdo si píše vlastní tofu, plugin nepotřebuje, protože cílí na kontejnery a serverless. A jablongo se diví, proč nestačí agenta jen poprosit, když mu to prý funguje, načež si sám odpovídá, že jde asi o předvídatelnost, a bealesh to potvrzuje: v repozitáři jsou knihovny dost vyhraněného OpenTofu, které agentům vstřikují názory, jež samy nemají.

Hodně se řeší peníze a bezpečnost. llama052 v tom vidí spolehlivý způsob, jak se probudit s vystřelenou útratou za cloud, protože model něco špatně odhadne, ale autor ho odkazuje zpět na návrh, který právě takové improvizaci brání. piterrro kontruje, že server u Hetzneru za 25 dolarů měsíčně dá víc prostoru i škálování, ZeWaka přitakává s VPS za šest dolarů a bealesh slibuje, že Hetzner je další na řadě. Do toho chrisweekly přihazuje tip na disco.cloud jako PaaS na vlastní VPS postavený jen na Docker obrazech, jehož spoluzakladatel gregsadetsky v diskusi vysvětluje, že nasazení zůstávají plně přenositelná a na infrastruktuře nezávislá.

Zbytek vlákna odlehčuje název. Stitch4223 přiznává, že už kvůli jménu má chuť to použít, i když pro to nemá využití, a bealesh děkuje, že pojmenovávání věcí ho jako umělce i technologa prostě baví. manlymuppet glosuje, že pravý Gilfoyle by si to hostoval sám, na což autor odpovídá, že dělej, co neckbeard říká, ne co dělá. Kritičtější je luckydata, podle kterého je readme ukecané a bolestivé na čtení, tak autor slibuje zklidnění a žertem varuje svým vzděláním na americkém Jihu.

Kdo nasazuje sám a bojí se noční stránky i faktury, dostává návod, jak obojí zachytit už ve chvíli, kdy je to pořád jen diff k revizi.
