# 50403097
**Apple Intelligence si vede tajný graf znalostí o uživateli**

Hacker News · infwhispers · 7. listopadu 2026, 10:46 · 669 bodů / 372 komentářů · [diskuse](https://news.ycombinator.com/item?id=50403097)

Výzkumníci z 8rank popsali nedokumentovanou součást Apple Intelligence, takzvaný personal knowledge graph. Systém si na Macu tiše buduje síť vztahů a odvozených znalostí o uživateli, k dokumentaci se ale podle nich nedá najít téměř nic. Data sice zůstávají lokálně na disku, modely Apple Intelligence se na ně však mohou dotazovat.

Autoři k výzkumu připojili i nástroj iKnow, přes který si může každý prohlédnout vlastní graf. Na GitHubu ho zveřejnili s tím, že je testovaný na posledních verzích macOS 26 a raných verzích 27. Jeden z uživatelů hlásí, že mu nástroj našel 137 živých faktů i s rozborem zdrojů a spolehlivosti, samotný obsah faktů ale hledal marně.

První reakce jsou syrové. Uživatel conartist6 píše, že bude hodně naštvaný, pokud se ukáže, že to jeho Mac opravdu dělá, uživatel Ungh strávil půl hodiny procházením dat a výsledek označil za naprosto děsivý. Vadí mu hlavně to, že sběr běží, i když má všechny funkce inteligence a Siri vypnuté a zablokované, a přemýšlí proto o přechodu na Debian. Podobně uživatel gattilorenz zůstává na systému Sequoia a říká, že příští laptop možná poběží na Linuxu, zatímco uživatel veonik ostatním radí, ať se podívají do složky ~/Library/IntelligencePlatform.

Jádro sporu je, co se s grafem děje dál. Autor výzkumu infwhispers v diskusi ujišťuje, že výstup zůstává lokálně na disku, zároveň ale přiznává, že se k němu může dostat Apple Intelligence a nikdo přesně neví jak. Právě proto by podle něj byla rozumná alespoň dokumentace a možnost funkci vypnout, jinak je podle něj všechno teoreticky jeden prompt injection daleko. Uživatel slickytail se ptá, zda se části grafu, otisky nebo odvozené závěry neposílají na servery Applu, uživatel zaptheimpaler zůstává optimistou a říká, že pokud informace neopouštějí zařízení, je to v pořádku. Uživatel apples_oranges kontruje, že v to už víru ztratil.

Do právní roviny debatu posunul uživatel DSpinellis, podle kterého sběr dat pro jiný účel, než pro jaký byla původně poskytnuta, porušuje evropské nařízení GDPR. Uživatel mimotomo2009 oponuje, že vše se staví i využívá na počítači uživatele, uživatel eastbound připomíná roli správce dat a uživatel jadamson nadhazuje praktický problém, zda by na žádost o výmaz musel vydat i fakta o jiných lidech, která mu Apple helpful databáze nasbírala. Mezitím uživatel arcanemachiner shrnul náladu větou, že uzavřený software se na dostatečně dlouhé časové ose vždycky promění ve spyware, na což uživatel MonkeyClub navrhl, že by se to mělo jmenovat jeho zákonem.

Zvláštní odbočku si našla i forma samotného výzkumu. Uživatelé asdfsa32, atombender a abandonliberty si stěžují na náhlý přechod od lidského úvodu k strojovému textu, který je donutil článek jen proletět nebo vzdát v půli, a uživatel mmooss lituje, že tahle hádka o psaní pomocí AI odsunula věcné otázky až na konec. Vedle toho řeší uživatel jamienk, jak nástroj použít na macOS 27.2 bez přepínače plného přístupu k disku, a uživatel yubblegum rozebírá bezpečnostní rizika spouštění cizího kódu.

Kdo chce vědět, co si o něm jeho vlastní počítač myslí, má teď aspoň kam sáhnout.
