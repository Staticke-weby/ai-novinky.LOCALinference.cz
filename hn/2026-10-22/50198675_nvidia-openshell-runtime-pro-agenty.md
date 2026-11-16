# 50198675
**NVIDIA OpenShell: bezpečné sandboxové prostředí pro flotily AI agentů**

Hacker News · niemandhier · 22. října 2026, 19:44 · 343 bodů / 183 komentářů · [diskuse](https://news.ycombinator.com/item?id=50198675)

Na Hacker News se objevil odkaz na repozitář NVIDIA OpenShell, otevřeného běhového prostředí pro flotily autonomních agentů. Projekt slibuje dát agentům praktické schopnosti, aniž by jim otevřel celý stroj, a láká na instalaci jedním příkazem i dokumentaci s návody.

Podle popisu na GitHubu mohou agenti číst soubory, instalovat balíčky, volat API a používat přihlašovací údaje, přičemž co smí dotknout určuje deklarovaná politika. OpenShell ji hlídá na úrovni jádra u každého přístupu k souborům, systémového volání a síťového spojení a reálné klíče agentům vůbec neukazuje, doplňuje je jen do požadavků na schválené cíle. Před změnou politiky ještě formální ověření upozorní na rizikové rozšíření přístupu a pošle ho k lidskému posouzení. Verze 0.1.x pak přináší pravidelná vydání, nové izolační primitivy a širší API, na PyPI je balíček a v repozitáři SDK pro Python, TypeScript, Go a Rust i bezpečnostní politika.

Nejživější přestřelka se strhla kolem telemetrie. overflowy citoval pasáž o sběru anonymních provozních dat a vypnutí přepínačem, xyst přidal, že ze zdrojů jde telemetrie vykompilovat úplně pryč, f3408fh se ptal, čeho se lidé u anonymních dat bojí, a Y_Y odpověděl vtípkem o braní peněz na pomoc a možnosti odhlášení.

Druhá vlna si utahovala z toho, kdo sandbox staví. nasretdinov rýpl, že to musel udělat výrobce herních karet a ne AI firmy, na což kbenson a LoganDark namítli, že NVIDIA už dávno není hlavně o hraní, a nickv dodal, že z herních karet má jen 5,5 % tržeb a časopis Economist ji označil za centrální banku AI. altmanaltman to dotáhl hláškou, že Anthropic, Meta a OpenAI jen ve velkém nakupují karty, aby si zahrály GTA 6, a layer8 s opengrass mezitím varovali před záměnou se známou úpravou nabídky Start Open-Shell-Menu.

Jádro debaty ale bylo praktické: jak agenty skutečně izolovat. mfro napsal, že pouštět agenty mimo kontejnery je bláznovství, Reddit_MLP2 ale namítl, že z běžných kontejnerů moderní modely snadno uniknou, a fennecbutt popsal proxy jen na povolené domény s výměnou přihlašovacích údajů, aby agent nikdy neviděl ty pravé. walrus01 a thway15269037 šli ještě dál a drží si agenty v oddělené KVM virtuálce na bezhlavém serveru za síťovým filtrem, zatímco toddmorey a dangoodmanUT upozornili, že OpenShell sám o sobě není sandbox, ale nadstavba nad Dockerem či virtualizací, jejíž pedantská kontrola dává smysl hlavně náročným firmám.

Čtenář si tak odnáší návod i varování zároveň: politika a izolace se hodí, ale bez vlastní obezřetnosti kolem sítě a klíčů se agentům věřit nedá.
