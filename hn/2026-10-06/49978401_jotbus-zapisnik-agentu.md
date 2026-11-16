# 49978401
**Jotbus: sdílený šifrovaný zápisník pro kódovací agenty**

Hacker News · shake-n-fries · 6. října 2026, 15:45 · 25 bodů / 14 komentářů · [diskuse](https://news.ycombinator.com/item?id=49978401)

Vývojář vystupující jako shake-n-fries představil Jotbus, sdílený zápisník pro kódovací agenty. Vadilo mu, že musí neustále kopírovat kontext a soubory mezi různými prostředími, stroji a kolegy, a tak postavil službu, která tohle předávání zařídí za něj. K vyzkoušení stačí jeden příkaz bez registrace, který vytvoří dočasný pracovní prostor a napojí ho na používané agenty přes MCP.

Web projektu slibuje konec přenášení textu přes schránku a provizorních poznámek v commitech. Po jednoduchém založení a připojení z druhého stroje stačí agentovi normálně říct, aby předal úkol, zanechal předávací poznámku nebo požádal o revizi, třeba větou o kontrole větve se zmínkou druhého agenta. Služba podporuje řadu nástrojů od Claude Code přes Codex, Cursor a Gemini CLI až po Copilot CLI či opencode, umí i přílohy jako logy a screenshoty a obsah šifruje už na zařízení, takže server ukládá jen šifrovaný text včetně názvů souborů. Základní hodinový prostor je zdarma, trvalé prostory s většími soubory a historií stojí sedm dolarů měsíčně a pozvaní hosté se připojují bezplatně.

Nejvěcnější výměna se rozjela kolem otázky, k čemu je taková služba, když totéž zvládne soukromý git repozitář se šikovností navíc. Uživatel tinthedev popsal vlastní řešení se vzdáleným gitem a skriptem, který agentům připraví instrukci připravenou ke zkopírování do dalšího promptu. Autor odpověděl, že kdo už má podobnou infrastrukturu hotovou, Jotbusu moc navíc nedá, jeho motivací ale bylo nemuset nic spravovat a mít kam odkládat právě nedodělané přechodné věci, které do historie commitů nepatří.

Podobnou zkušenost hlásí i další diskutující. Uživatel whalesalad ukázal vlastní obdobnou službu AgentDrop a uživatel madeofpalk v Jotbusu vidí konečně na poskytovateli nezávislou obdobu Claude Artifacts. Uživatel cloverich přemýšlí, jestli se taková drobnost uživí jako placená služba, když si ji každý bastlí sám, a přesto ji u kolegů v praxi nevidí, a přidává tip rozsekávat dlouhé úlohy na shrnutí a další kroky pro nové agenty, což mu dramaticky šetří náklady. Uživatel dariusmonsef se smíchem nabízí vlastní proměněný prototyp OzBrain, aby si autor nemusel stavět totéž potřetí.

Do hloubky šla debata o soukromí. Uživatel tomsonoda chválí, že server vidí jen šifrovaná data, a ptá se na dvě klasické pasti vícezařízeního šifrování: co se stane, když se novému klientovi nepodaří stáhnout klíč pracovního prostoru a potichu si vygeneruje vlastní, a jak se řeší odebrání člena, tedy zda se klíč rotuje, nebo má vyhozený člověk dál přístup k historii. Uživatel samuell zase připomíná lokální open source alternativu Epiq, distribuovanou nástěnku úkolů synchronizovanou přes log událostí pro ty, komu se poznámky vejdou do issues.

Z vlákna tak vyplývá, že Jotbus netlačí novou technologii, ale pohodlí: stejné předávání kontextu si šikovní vývojáři umí postavit sami, placená služba jim má jen ušetřit správu a dát jim šifrovaný kanál, kam agenti rovnou píšou.
