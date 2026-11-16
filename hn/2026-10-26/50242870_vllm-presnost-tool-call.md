# 50242870
**Proč vLLM plete nástroje a jak se opravuje přesnost tool-callů**

Hacker News · coffeemug · 26. října 2026, 13:59 · 161 bodů / 66 komentářů · [diskuse](https://news.ycombinator.com/item?id=50242870)

Inženýři z Ubicloudu Jesse Donkervliet a Junhao Li popsali na blogu, proč se jim při obsluze otevřených modelů nedařilo dosáhnout stejné kvality volání nástrojů jako u původního poskytovatele. Upozorňují, že u agentních úloh stačí jedno špatně naformátované volání a celé vícekolové sezení se zanese chybovými hláškami, zpomalí a prodraží. Do diskuse přišel i jeden z autorů pod přezdívkou jesdo a nabídl, že bude odpovídat na otázky.

Podle textu dostávali při servírování Kimi K2.6 přes vLLM 0.28 správné schéma jen v 92 % případů, tedy zhruba ve dvou z každých 25 pokusů volání selhalo. Příčinu vidí v pravděpodobnostní povaze modelu, který si občas vypůjčí název nástroje nebo parametru z tréninkových dat místo aktuálního schématu. Řešením je takzvané constrained decoding, které přes knihovnu XGrammar při generování povoluje jen tokeny odpovídající schématu, ve vLLM 0.31 je dostupné jako serverový příznak a Ubicloudu po zapnutí přineslo stoprocentní přesnost schématu.

Nejživější debata se vedla o to, co tohle omezení vlastně dělá s modelem. Uživatel hypfer se ptá, jestli volání nástrojů v takovém režimu vůbec „dělá model", nebo jde jen o prořezávání neplatných tahů vzorkovačem, a zda by se podobné řízení dalo použít i jinde. Autor jesdo odpovídá, že jde o dva různé pohledy: celkovou kvalitu sestavy model plus engine plus harness, a věrnost chování vůči first-party API, přičemž Moonshot AI omezené dekódování pro Kimi doporučuje a sám ho tak provozuje.

Do toho vstupuje uživatel hansvm s přáním, aby autoři ukázali reálný dopad na kvalitu: rozdělení výstupu se podle něj mění a zajímalo by ho srovnání s metodou zálohování a opakování celého volání, která také nezanáší kontext a má stoprocentní přesnost. Uživatel saurik namítá, že omezení by mělo odpovídat převáženému původnímu rozdělení, ale připouští, že model se může „zahnat do kouta" špatnou první volbou a pak už jen zachraňovat beznadějný stav. Jesdo slibuje, že se tomu chtějí věnovat příště, a odkazuje na práce naznačující, že dopad omezeného dekódování na kvalitu se model od modelu liší.

Praktici v diskusi počítají, proč na každém procentu záleží. Uživatel draxen píše, že dělá úlohy s asi třemi sty voláními nástrojů na jeden prompt a kvůli spolehlivosti zůstal od roku 2024 u OpenAI a Anthropic, které měly stoprocentní přesnost a prompt caching vyřešené dřív. Podobně uživatel bob1029 vysvětluje, že při 95% úspěšnosti a padesáti sekvenčních voláních projde bez chyby jen asi osm procent běhů, i když chybová zpětná vazba umí leccos zachránit.

Zazněla i kritika samotného titulku a složitosti vLLM. Uživatel Aurornis tvrdí, že článek je matoucí, protože omezené dekódování je ve vLLM dávno a Ubicloud ho ve skutečnosti jen potřeboval správně nastavit, zároveň ale chválí, že firma měla benchmarky, které regresi zachytily. Uživatel jacquesm dodává, že vLLM je matoucí a křehký systém, který vyžaduje velkou investici času. Jesdo reaguje, že v jejich případě oprava skutečně vyžadovala změnu kódu a nešla vyřešit konfigurací, až později ji upstream vyřešil a dnes stačí nastavit příznak --tool-strict-level.

Z článku si čtenář odnese hlavně to, že kvalitu neurčuje jen model, ale i inference engine a jeho nastavení.
