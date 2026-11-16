# 50090842
**První patch Linuse Torvaldse napsaný s pomocí LLM**

Hacker News · janvdberg · 14. října 2026, 18:55 · 115 bodů / 96 komentářů · [diskuse](https://news.ycombinator.com/item?id=50090842)

Na summitu maintainerů Linus Torvalds přiznal, že dlouho odkládaný problém v jádře zkusil rozlousknout s velkým jazykovým modelem. Výsledek následně poslal k běžné recenzi jako sérii patchů. Pro komunitu jde o symbolický okamžik, protože právě Torvalds byl dlouho vnímán jako bašta střízlivého odporu k módním vlnám.

Podle textu LWN čítá série deset patchů a vylepšuje vyhledávání folií tím, že si všímá rozpálených folií a odkládá jejich uvolnění až za RCU periodu. Rychlá cesta pak nemusí brát refcount a čte data z folia celá v chráněné RCU oblasti, pokud kopie pro uživatele nezpůsobí výpadky stránek. U benchmarku těžce stojícího na čtení to přineslo řádové zrychlení, hned první recenze ale našla race condition, takže bude potřeba další práce.

Největší ohlas mělo překvapení, že se do toho pustil zrovna Torvalds. Uživatel tombert přiznává, že AI používá jako většina lidí, ale u Linuse ho to zarazilo, protože ho měl za posledního staromilce, který nesáhl ani na C++. Uživatelé furyofantares a gvfsa oponují, že odmítnutí C++ nebyla ideologie ani tvrdohlavost, ale věcné výtky, a připomínají, že v jádře už je i Rust. Uživatel steveklabnik přidává zkušenost z akademické konference, kde respektované starší kapacity berou AI střízlivě jako další užitečný nástroj do sady.

Právní rovinu nadhazuje uživatel DiabloD3 s tím, že pomoc je v pořádku, pokud kód projde auditem maintainera a je výrazně dílem člověka, protože strojově psaný kód nelze chránit autorským právem, a tedy nemůže být open source. Uživatel tarkin2 poznamenává, že Torvalds už hlavně čte a spravuje cizí kód, takže je skoro jedno, zda předloha přijde od člověka nebo stroje. Do toho uživatel mono442 rýpe, že aspoň commit message mohl napsat sám, protože ukecané zdůvodnění modelu se špatně čte, a uživatel manbash cituje Torvaldsův vzkaz z prázdného commitu, že kód, testy i první návrh textu vznikly s Claude Code pod jeho vedením.

Kolem toho se rozhořel spor o laťku pro nováčky. Uživatel vatsachak si stěžuje, že si mnozí odnášejí dojem, že když Linus vylepšil jádro s Claude, zvládne to každý, uživatel atniomn mu dává za pravdu v tom, že je v tom jasný faktor šikovnosti při pilotování modelů. Uživatel rfgplk naopak tvrdí, že Torvalds nemohl modelu nic přinést, jako amatér se Stockfishem, a že si každý do hodiny nechá napsat fungující modul. Do debaty vstupuje i vtip uživatele relativeadv, že když to uděláš ty, je to odpad, když on, je to řemeslo, což uživatel teekert s úsměvem potvrzuje, že pro některé kombinace lidí to opravdu platí.

Provokativní otázku položí uživatel dorianniemiec, co teď řeknou odpůrci AI, když je s její pomocí stavěna kritická infrastruktura. Odpovědi se rozbíhají od vtipů o forku všeho a návratu k GNU Hurd či NetBSD až po vážnější hlasy. Uživatel ASalazarMX rozlišuje střízlivé použití s poctivou recenzí a zneužití, kdy někdo jen povrchně zkontroluje složitý program a vydává ho za svůj. Uživatel jraph odpovídá za odpůrce motivované ekologií a ekonomií, že obavy z datacenter, bezohledného scrapování a krize, kterou mohou AI firmy způsobit, nezmizí ani tehdy, kdyby byl nárůst produktivity skutečný.

Z vlákna tak zůstává obraz AI ne jako náhrady úsudku, ale jako posilovače zkušeného vývojáře, jehož práci pořád musí podržet lidská recenze.
