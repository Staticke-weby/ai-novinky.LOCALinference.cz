# 50574772
**llms.txt a MCP nepřinesly výsledky. Autor popsal, co fungovalo**

Hacker News · moebrowne · 20. listopadu 2026, 15:00 · 30 bodů / 21 komentářů · [diskuse](https://news.ycombinator.com/item?id=50574772)

Správce balíčku Backpack for Laravel Cristian Tabacitu sepsal, že dvě nejčastěji doporučované věci pro „AI připravenost" jeho produktu skoro nepomohly: soubor llms.txt ani vlastní MCP server pro dotazování nad dokumentací. Administrativní panel pro jednoduchý web mu přitom dřív trval den až dva, dnes ho s agentem postaví výrazně rychleji – popíše zadání, agent pustí generátory, napíše konfiguraci i testy a on výsledek jen zkontroluje. Jde o zkušenost z reálného deset let starého produktu, ne o benchmark.

Největší posun podle něj přinesly věci, které vznikly dávno před nástupem agentů a cílily na lidi. Stabilní API se propsalo do tréninkových dat modelů, otevřené jádro nasbíralo deset let příkladů na GitHubu a fórech a placený kód se instaluje čitelný do vendor/, takže si ho agent sám otevře a pochopí. Z cílených novinek pak nejvíc zabral plugin pro Laravel Boost, který dostane pokyny k nainstalované verzi přímo do kontextu, dále příkazové generátory pro scaffolding a testy, předvídatelné názvy a Markdown verze dokumentace.

Začátek diskuse byl trpký. Uživatel antiloper označil text za jeden z nejhorších příkladů needitovaného strojového slopu a vyčetl autorovi, že výstup jen zkopíroval ven. Jiným to tak nepřišlo – StilesCrisis se ptal, co bylo poznávacím znamením, a SomewhatLikely napsal, že na něj článek působil jako žitá zkušenost. Sám Tabacitu se do vlákna vrátil jen krátce s omluvou, že se příště pokusí psát lépe.

Nejživěji se řešilo, zda si agenti souboru llms.txt vůbec všimnou. Uživatel rcymerys napsal, že marketéři ho přesvědčují o jeho nutnosti, ale důkazem jsou jim jen příspěvky jiných konzultantů na LinkedInu, a při vlastních pokusech se mu nepovedlo přimět Claude ani ChatGPT, aby soubor samy hledaly. Uživatel 0x696C6961 to shrnul tak, že jde spíš o úsporu tokenů a jakýsi rejstřík dokumentace, který si musí agent explicitně vyžádat. Podobnou zkušenost přidal petercooper: do llms.txt svého newsletteru dopsal pro strojové odesílatele odlišná pravidla, ale ani jeden agent je zatím nedodržel, a ani jeho vlastní agenti si souboru při běžném čtení stránek nevšímají.

Ještě ostřejší byla kritika dokumentačního MCP. Uživatel drbscl se divil, proč by někdo takové MCP vůbec stavěl, když na to existuje Context7, a zodwick poznamenal, že článek by dával smysl tak před deseti měsíci. Uživatel deadbabe dodal, že nikdo by neměl používat MCP na to, co má být vyhledáváním v korpusu, a vorticalbox rýpl, že důvodem bude asi nechuť pořádně zdokumentovat API ve Swaggeru. Na otázku uživatele canadiantim, co je dnes místo Context7 nejlepší, už ale vlákno odpověď nedalo.

Poučení je tak až provokativně nudné: vyhrává to, co má agent rovnou před sebou nebo v hlavě, ne to, na co si musí vzpomenout a dojít si pro to.
