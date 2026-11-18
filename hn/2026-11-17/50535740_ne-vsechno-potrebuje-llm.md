# 50535740
**Ne všechno potřebuje LLM. Rozhodovací modely jsou až 444krát levnější**

Hacker News · speckx · 17. listopadu 2026, 19:16 · 139 bodů / 56 komentářů · [diskuse](https://news.ycombinator.com/item?id=50535740)

PostHog v produkci nasazuje takzvané rozhodovací modely pro jednoduché úkoly, na které je velký jazykový model zbytečně drahý a upovídaný. Místo volného textu vracejí typovanou odpověď s pravděpodobností, podle firmy jsou až 444,6krát levnější a 193,6krát rychlejší než špičkové modely a slouží hlavně jako filtr, který rozhodne, zda má vůbec smysl dražší model volat.

Odkazovaný text Jiny Yoonové vysvětluje princip na příkladu ježků: otázka „Jsou ježci savci?“ vrátí „Ano, 0,99“, přičemž u kalibrovaného modelu znamená skóre 0,8, že odpověď sedí zhruba v 80 procentech případů. V produktu Replay Vision takhle dvě úzké otázky hlídají osobní údaje v souhrnech nahrávek, přes bránu projde bez volání Gemini 98,7 procent případů, a podobně funguje třídění zpráv pro bota ve Slacku, směrování na nejlevnější dostatečný model nebo přerovnání výsledků hledání, kde se kvalita řazení zvedla asi o čtvrtinu.

Nejživější spor se vede o to, co rozhodovací model vlastně je. Uživatel jakeydus se ptá napřímo, zda to není jen LLM s pokynem omezit odpovědi, a orbital-decay odpovídá, že jde spíš o diskriminativní než generativní model po vzoru BERT, jen zabalený do nového marketingu. Do stejné linky patří povzdech pj_mukh, že pointou je „jen typově bezpečná obálka kolem LLM“, i poznámka saejox, že strukturované JSON výstupy používá od dob GPT-4 a humbuk kolem Jev nikdy nepochopil.

Z praktického soudku nejvíc rezonuje varování před šetřením na nesprávném místě. Uživatel aabdi tvrdí, že by všichni měli brát nejdražší model, dokud neumí pořádné evaluace, protože špatné testy, které neměří reálný provoz a dlouhý chvost případů, vyrobí rozbitý produkt pro většinu zákazníků. Na to navazuje abhgh úvahou o kaskádě chyb, kdy pravděpodobnostní funkce hodnotí pravděpodobnostní soudce, zatímco mrbungie oponuje, že bez zpětné vazby od uživatelů jsou špatné evaluace ten nejmenší problém. Podobně skepticky zní throwawayffffas k nápadu směrovat modely rozhodovacím modelem, který o novějších modelech ví jen z krátkého popisku, a Rapzid kroutí hlavou nad tím, že firma ukazuje hlídání osobních údajů zrovna na tak křehké technologii.

Třetí proud diskuse míří ještě výš a řeší, proč se LLM cpe úplně všude. Uživatel b3ing viní manažery, kteří neznají nic než LLM, a tak jím nahrazují algoritmy, funkce i regulární výrazy, na což cookiengineer odpovídá, že počítače mají sloužit lidem a nulová bariéra je pokrok, ne úpadek. Jako důkaz absurdity pak whycombinetor vzpomíná na návrh převádět obsah polí webového formuláře na JSON pro přenos přes LLM místo obyčejného mapování. Filozofickou tečku dodává socketcluster: lidé chtějí jednoduché odpovědi na krátké otázky, ale realita je otravně složitá a krátká otázka ještě neznamená jednoduchou.

Kdo hledá levnější cestu, najde v PostHogu návod i varování zároveň: malý rozhodovač ušetří spoustu volání, ale práh je třeba ladit pro každý úkol a model zvlášť.
