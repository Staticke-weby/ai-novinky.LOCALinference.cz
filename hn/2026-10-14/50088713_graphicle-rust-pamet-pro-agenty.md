# 50088713
**Graphicle: paměť a graf kódu pro kódovací agenty v Rustu**

Hacker News · KarLexAI · 14. října 2026, 17:00 · 44 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50088713)

Autor KarLexAI v rubrice Show HN představil Graphicle, jeden program v Rustu pro kódovací agenty. Jeho engine grafu kódu je portem nástroje Graphify, k němuž přidává projektovou paměť od dokumentů a rozhodnutí po minulé relace agentů.

Podle stránky na GitHubu běží vše lokálně v jednom souboru SQLite, bez API klíče, účtu a telemetrie. Příkaz pro nastavení zaindexuje repozitář, postaví graf kódu a napojí nalezené klienty přes MCP, od Claude Code přes Cursor, Codex a VS Code až po Claude Desktop. Agent pak dostává relevantní kód, dokumenty a rozhodnutí jako úryvky se zdrojem v rámci tokenového rozpočtu a model si z nich čte sám, přičemž autor slibuje na Kubernetes s 31 tisíci soubory extrakci za 3 min 18 s proti 26 min 38 s u Graphify 0.9.88.

Nejživější je ve vlákně skeptická linka o užitku. Uživatel theLiminator se ptá, zda s tím má někdo opravdu dobré výsledky, protože v jeho vlastních, přiznaně málo vědeckých testech dopadly paměťové systémy hůř než holý harness s ripgrepem. Uživatel NewJazz vypráví, že si pročetl soubor dovedností graphify a některé příkazy si i spustil, ale vrátily tolik strukturovaných informací, se kterými model ani harness neumí dobře pracovat, takže pomoct by mohlo až zapracování takových nástrojů do trénování a dolaďování. Uživatel nonethewiser souhlasí, že víc struktury podle jeho zkušenosti znamená horší výkon, a navíc člověku přibude práce.

Na to navazuje debata o vyhodnocování. Uživatel pjm331 se ptá, kdo dnes agentům takové nástroje měří a jak to dělá. KarLexAI odpovídá, že paměťové nástroje se běžně testují na sadách LoCoMo, LongMemEval a BEAM i podle spotřeby tokenů, a že předběžnou verzi Graphicle srovnali se sedmi jinými systémy včetně Mem0 a Hindsight na třech veřejných sadách otázek, s předem sepsanými pravidly a s jedním otevřeným modelem v roli čtenáře i soudce pro všechny. Sám zároveň přiznává, že chybí to hlavní, tedy zda agent se zapnutým nástrojem dokončí víc úkolů při stejném agentovi, modelu a zadání, a zajímá se, co by čtenáře přesvědčilo. Uživatel pjm331 pak dodává čerstvou zkušenost s demem Gemini 4 Argon, které si přes codemode strukturované podklady o kódu vyrábí samo, a myslí si, že specializované nástroje pomáhají slabým modelům, ale na špičce jen zpomalují a prodražují.

Vedle toho zaznívá věcnější ocenění i otevřené pochybnosti. Uživatel dmos62 píše, že klíčové mu přijde právě svázání vzpomínek s kusy kódu, třeba funkcemi, protože paměťovým systémům nikdy nevěřil právě kvůli tomu, že nepozná, zda vzpomínka ještě platí a kdy je relevantní, a spojení grafu kódu s pamětí mu proto připadá novátorské. Uživatel cadamsdotcom naopak namítá, že bez srovnání kvality proti agentovi, který umí grepovat, se přidaná hodnota těžko posuzuje, a uživatel blackspacx se ptá na benchmarky a na to, zda nástroj vznikal s pomocí AI.

Z vlákna tak vychází Graphicle jako technicky elegantní a rychlý pomocník, jehož skutečný přínos v praxi by komunita nejraději viděla v poctivém testu proti prostému vyhledávání.
