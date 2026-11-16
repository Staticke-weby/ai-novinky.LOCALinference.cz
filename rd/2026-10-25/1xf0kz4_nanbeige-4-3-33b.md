# 1xf0kz4
**Nanbeige 4.3-33B: čínský model tvrdí, že poráží Qwen3.8-27B**

r/LocalLLaMA · u/Mysterious_Finish543 · 25. října 2026, 13:01 · 467 bodů / 104 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xf0kz4/)

Uživatel u/Mysterious_Finish543 přinesl do komunity nový čínský model Nanbeige 4.3-33B s odvážným tvrzením, že v celé řadě testů překonává Qwen3.8-27B. K příspěvku přiložil graf s naměřenými skóre a doplnil, že velký model má sloužit jako učitel pro destilaci menších verzí, například chystané 3B varianty.

Odkaz míří na kolekci Nanbeige na Hugging Face. Podrobná karta modelu se tentokrát načíst nepodařila, viditelný zůstal jen výpis kolekce se dvěma položkami aktualizovanými zhruba před dvaceti hodinami.

Největší ohlas sklidil komentář uživatele u/Easy_Refrigerator280, který slíbil, že čísla ještě ten den rychle otestuje a uvidí, kolik se jich přenese do běžného používání. Po editaci pak hlásí slušné výsledky, ale zároveň paměťově extrémně hladovou cache, kvůli níž si není jistý, zda se kompromis vůbec vyplatí.

Na to navázala architektonická debata. Uživatel u/Marcuss2 se podíval do konfiguračního souboru, našel tam LlamaForCausalLM a rovnou varoval, že právě proto bude cache problém. Uživatel u/Kahvana dodal, že proti Qwenu, Gemmě nebo Muse bude tohle řešení neefektivní, a praktické dopady hned rozebírají majitelé slabších sestav: u/p211 si stěžuje, že husté modely téhle velikosti jsou utrpením na 16 GB paměti, u/hirak99 s 24 GB čeká na 4bitovou kvantizaci a u/Ok_Year8287 hlásí na DGX Sparku jen 5–7 tokenů za sekundu, protože zatím chybí podpora pro rychlejší běh.

Zbytek vlákna balancuje mezi nadšením a skepsí k číslům. Uživatel u/pmttyji chválí, že po LiquidAI a OpenBMB konečně škáluje i další laboratoř a pásmo kolem třiceti miliard parametrů se zaplňuje, přičemž novinka podle něj nastavuje laťku pro chystané Qwen4-27B a doufá, že zaboduje i v tvůrčím psaní. Proti tomu u/Qcgreywolf ironizuje, že každý testovaný model v tom svém grafu vždycky vede nad všemi ostatními, u/Flavius_Aetius2 volá po úplně novém systému testování a u/Gohab2001 by chtěl vedle skóre vidět i počet výstupních tokenů a rychlost. Řeší se i absence vidění, kvůli které je model pro uživatele u/Ipwnurface nepoužitelný, zatímco u/FinBenton a u/blastcat4 vyhlížejí menší destilovanou verzi a zajímá je, zda si udrží pověst předchozích malých modelů pro psaní a roleplay.

Papírově jde o silného soupeře zavedených modelů kolem třiceti miliard, v praxi ale zatím rozhoduje paměť a rychlost.
