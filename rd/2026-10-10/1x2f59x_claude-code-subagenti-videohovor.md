# 1x2f59x
**Claude Code sub-agentům dal video call, prý nejlepší způsob sledování**

r/ClaudeAI · u/stickygoose · 10. října 2026, 15:19 · 650 bodů / 85 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1x2f59x/)

Autor už měl dost terminálu plného logů, ve kterém se ztrácelo, kdo dostal jaký úkol, co právě spouští a kdo už skončil. Postavil proto Agent Standup, bezplatné open-source rozšíření pro VS Code pod licencí MIT, které živou session Claude Code převléká za videohovor. Každý sub-agent v něm vystupuje jako malá postavička, která se do hovoru připojí s přidělením úkolu a odejde po odevzdání, sdílená obrazovka ukazuje jeho skutečné příkazy s výstupy, přesné diffy úprav i čtené soubory a strom prozrazuje, kdo koho požádal.

Celý projekt podle autora vznikl za asi dva dny v jedné dlouhé konverzaci s Claude Code, který napsal Node server parsující JSONL přepisy, webový frontend i postavičky, otestoval rozhraní v bezhlavém prohlížeči a připravil balíček i stránku ke stažení. Funguje přitom i mimo VS Code jako samostatný server a čte sessions z desktopové aplikace i příkazové řádky, na Macu je odladěný nejlépe a zvědavci si ho mohou vyzkoušet na demu bez vlastní session.

Nejvíc hlasů dostalo přání u/ben8192, ať už postavičky konečně dostanou hlas, aby bylo slyšet jejich rychlé pištění, a hned za ním vtip u/Ok_Music_4862 o prvním videohovoru, kde všichni opravdu něco dělají. Stejný uživatel se rovnou ptal, jestli nástroj zachytí i cloudové session, nebo jen lokální soubory v ~/.claude/projects, a další lidé řešili, zda půjde vybrat správný projekt, když jim rozšíření ukazuje jen starou neaktivní session.

Hodně vlákna se točí kolem ceny za sledování. u/iamtehryan se bál, že zábava ukrojí z jeho limitů, ale u/Dapper_Profession vysvětlil, že čtení přepisu, který Claude Code stejně zapisuje na disk, nestojí nic navíc a drahé by bylo jen to, co by se vracelo zpět do session. Automatické shrnutí diskuse to potvrzuje a dodává, že účet se zapojí až u volitelných funkcí jako překlad do francouzštiny nebo vtipný režim.

Zbytek debaty už je o tom, jak hovor dotáhnout. u/neondragony přihodil fork s lokálním přirozeným hlasem přes Kokoro a přepínačem Meme Mode se zvukem zaseknuté desky při přerušení, jiní chtějí korporátní žargon, čínské menu nebo vlastní pixelartové kamarády místo výchozích avatarů. Věcnější linku drží u/bugra_sa s nápadem, aby každá dlaždice na první pohled hlásila, zda agent pracuje, čeká, visí na schválení, nebo skončil, což podle u/BP041 s osmnácti bezhlavými agenty v OpenClaw rozhoduje o tom, zda si člověk včas všimne, že se některý tiše zatoulal z úkolu.

Kdo sleduje víc agentů najednou, odnese si z vlákna prosté ponaučení: roztomilé obličeje pobaví, ale skutečná výhra je přehled, ve kterém je na první pohled vidět, kdo maká a kde se zasekla předávka.
