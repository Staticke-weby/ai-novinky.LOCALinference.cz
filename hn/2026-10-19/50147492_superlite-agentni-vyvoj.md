# 50147492
**Superlite: lehčí recept na agentní vývoj než Superpowers**

Hacker News · iheatuchriswogu · 19. října 2026, 04:01 · 147 bodů / 67 komentářů · [diskuse](https://news.ycombinator.com/item?id=50147492)

Autor snil o ideálním zadání agentovi: předat specifikaci, zavřít notebook, udělat si sandwich a vrátit se k hotové, otestované a commitnuté práci. Místo toho se dočkal vyptávání za vyptáváním, kdy agent po odstavcích schvaloval design, pak specifikaci, plán i způsob jeho provedení. Stavění se pak vleklo v cyklu udělej, zrecenzuj, oprav a zrecenzuj znovu, takže se člověk bál odejít, aby se nevrátil k otázce čekající dvacet minut na slovo ano.

Odpovědí má být Superlite, plugin pro Claude Code postavený na kostře projektu Superpowers, ale laděný na samostatný vývoj v rychlosti. Místo osmi až dvanácti lidských bran slibuje jednu várku otázek a jedno schválení, plán jako graf úloh s vlastními soubory, rozhraními a testy, které mohou běžet vedle sebe, a práci rozdělenou podle náročnosti mezi koordinující Opus, stavějící Sonnet a Haiku na drobné mechanické úkoly. Pravidla nevymáhá prosbami v promptu, ale hooky v kódu, každý běh měří tokeny, cenu a čas a v ukázkovém testu statického generátoru se spreadsheet enginem hlásí 177 ze 177 skrytých testů za 16,1 minuty s až 18 agenty najednou.

Nejživější debata se stočila k tomu, zda je něco takového vůbec ještě potřeba. PierceJoy píše, že ho nadšení pro Superpowers přešlo po dni kvůli nekonečným schvalovacím promptům, a ptá se, co by mu Superlite dalo navíc proti samotnému Opus 5.5. Podobně jemdiggity vypráví, že si udělá sandwich a vrátí se ke specifikaci, diffu a dalším stopám hotové práce, Nursie to přirovnává k pomíjivé módě prompt inženýrství z časů DALL-E 2 a tarr11 se ptá prostě, proč Claude jen nepožádat, ať to vymyslí a jede.

Do té skepse vstoupil uživatel ra s tezí, že dovednosti jsou proces neboli postup, který špičkové modely pořád nemají odolný, a DannyBee ji rozvedl: kdo chtěl jen slušné chování modelu, ten už dovednost nepotřebuje, ale kdo chce pokaždé stejné artefakty ve stejném formátu, bez návodu je nedostane. InsideOutSanta oponuje, že mu stačí krátký odstavec v promptu o plánu, levnějších subagentech a reakci na připomínky, a __alexs dodává, že ani s dovednostmi není proces odolný, protože každá aktualizace modelu mění výklad.

Zbytek vlákna řeší praxi. michelb chválí brainstorm a plán z Compound Engineering i dovednost grill-me od Matta Pococka, zatímco zbytek přirovnává k podnikovému schvalování radami, které vysává tokeny. johannessjoberg přiznává, že si ze Superpowers nechal právě jen brainstorming, protože aktivní rozhodování mu pomáhá látku pochopit. Stranou zůstaly dvě věcné otázky bez jasné odpovědi: codeugo se ptá, jak paralelní agenti zabrání tomu, aby si sahali do práce, a CasualSuperman, o kolik paralelismus zvedne cenu tokenů.

Kdo si z toho má co odnést, najde to v autorově větě, že pomalost nebývá hlubokým přemýšlením modelu, ale frontou práce a neustálým čekáním na svolení.
