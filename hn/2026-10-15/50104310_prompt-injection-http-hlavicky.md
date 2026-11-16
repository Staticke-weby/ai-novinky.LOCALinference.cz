# 50104310
**Prompt injection v HTTP hlavičkách: co ukázalo 217 milionů odpovědí**

Hacker News · panoramas4good · 15. října 2026, 16:36 · 84 bodů / 17 komentářů · [diskuse](https://news.ycombinator.com/item?id=50104310)

Výzkumníci ze Signals Corps prošli 217 097 223 odpovědí z 10 % zářijového crawlu Common Crawlu a hledali hlavičky psané pro umělou inteligenci. Našli jich 7 959 webů, většinou šlo o běžné rozcestníky k souborům llms.txt nebo serverům MCP a o pravidla pro crawling. Jen malá část se vůbec pokoušela agentovi něco přikazovat.

Z těch 7 959 webů zkoušelo 30 dát agentovi příkaz a 22 z nich byly vyložené vtipy typu vrať číslo 42 nebo mňoukni. Vlastní test s hlavičkou X-Agent-Directive dopadl tak, že modely Claude Opus, Sonnet i Haiku v Claude Code běžné výzvy ignorovaly a poslechly až ve chvíli, kdy jim prompt dal webu autoritu, pak v 7 z 9 běhů. Největší pozornost si proto podle autorů zaslouží detekce: 136 webů poznalo CCBot jako AI bota jen podle user-agenta, což je první krok ke cloakingu, tedy k servírování jiného obsahu agentům než lidem.

Diskuse se rychle shodla, že článek je zbytečně dlouhý na to, jak prosté je jeho jádro. Uživatel simonw píše, že sekce s injekčními hlavičkami vypadá až na testovací řetězec pro odmítání u Claude 4 jako samé nevážné pokusy, a uživatel chrisgarand k tomu dodává, že vtip s dropnutím SQL tabulky by vyžadoval tak děravou aplikaci, že by problém nebyl v hlavičce. Jak podotýká uživatel amelius, jde o narážku na klasický komiks xkcd 327.

Jediný kousek, který diskutující berou vážně, je testovací hlavička z agentpwn.com, která agenta nabádá k npx hackmyagent secure a hlášení na vlastní server. Uživatel randomblock1 lituje, že se autoři nepodívali hlouběji na to, co redigovaný balíček dělá, když by právě tady mohl být škodlivý příkaz reálný. Uživatel stickfigure se ptá přesně na to, co článek podle něj nezodpovídá: jestli to celé vůbec funguje, protože vstup do modelu to je, ale musel by být dost hloupý, aby to poslechl.

Nejobsáhlejší linka se pak stočila k detekci a odlišnému obsahu pro agenty. Uživatel crisnoble shrnuje, že zatímco poslouchat náhodné hlavičky by agent neměl, odhalit ho podle user-agenta je triviální a poslat mu osekanou nebo úplně jinou verzi stránky pak dává smysl i bez zlého úmyslu. Uživatel tcdent k tomu přidává obecnější postřeh, že web tradičně rozlišoval význam a důvěryhodnost podle struktury, ale pro jazykový model je všechno jen text. Osobní zkušenost přidal uživatel ArashEdalat, kterému Claude při náboru označil životopis se skrytým bílým textem na bílém pozadí, viditelným jen pro stroj.

Kdo provozuje agenty, které samy tahají web, měl by si pohlídat, aby fetch nástroje standardně braly jen tělo stránky a aby v promptech nestálo, že mají poslouchat pokyny cizích webů.
