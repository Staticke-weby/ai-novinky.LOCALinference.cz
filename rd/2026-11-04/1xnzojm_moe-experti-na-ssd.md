# 1xnzojm
**MoE experti na SSD: 60 procent modelu mimo RAM a jen 1–3 ms na token**

r/LocalLLM · u/Harin007 · 4. listopadu 2026, 21:57 · 208 bodů / 66 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xnzojm/)

Vývojář postavil na základech llama.cpp engine, který dokáže odložit 60 až 70 procent směrovaných expertů MoE modelů na SSD a latenci streamování přitom schovat do 1 až 3 ms na token. Model se tak tváří, jako by celý žil v paměti, i když většina vah leží na disku. K tomu přidal autotuner, který do dvou minut vybere nejlepší nastavení pro daný hardware, výpočet promptu po vrstvách místo batchingu a skoro bezztrátový engine na zhutnění kontextu, to celé chce brzy vydat jako open source.

Vlastní čísla zní silně: vrstva po vrstvě má zrychlit zpracování promptu dvakrát u sestav s RAM a VRAM a čtyřikrát při zapojení SSD. Flint 40B v kvantizaci Q4K_XL prý běží na stroji se 16 GB RAM bez dedikované grafiky přes 20 tokenů za sekundu, Ling 3.0 Flash v MXFP4 kolem 50 tokenů za sekundu při dekódování a 600 až 700 tokenů za sekundu při prefillu na kombinaci 32 GB RAM a 12 GB VRAM. Autor rovnou odpovídá na obvyklou obavu o životnost disku, že engine jen čte a nezapisuje, a láká na video s Lingem při kontextu 262 tisíc tokenů na laptopu. Váhá jen nad tím, zda ještě přidat podporu Qwen 3.8 Flash Next, nebo už čekat na rodinu Qwen 4.

Nejvýše hodnocený hlas patří radě od u/looselyhuman, aby autor držel engine, tuner a uživatelské rozhraní odděleně a neřešil všechny problémy najednou, jinak vyhoří. Hned pod tím se ozývá únava z množství novinek, když se u/Ok-Thanks-6785 ptá, čím se projekt liší od Strata, Maya a záplavy dalších, které vznikají každý den. Podobnou notu hraje u/Slow_Ball561, který upozorňuje na svůj NestQuant se stejnou myšlenkou prefillu po vrstvách a ptá se, zda autor také používá prediktory pro přednačítání expertů.

Neživěji se řeší, na kterých modelech to poběží. u/Lissanro by chtěl dostat do vyšší kvantizace Kimi K3 tím, že by polovinu expertů odložil na NVMe, u/Glatiinz zase prosí o Kimi K 3.1, jejíž nejmenší jednobitová kvantizace má 466 GB a oficiální FP4 rovnou 1,56 TB. Přidávají se hlasy pro GLM a DeepSeek, u/Ready_Maybe_3406 to shrnuje cenami pamětí, které dělí svět na ty, co na AI mají, a ty, co ne. Skepsi přináší u/alphapussycat s pochybností, zda za čísly nejsou čtyři NVMe páté generace v raidu.

Kolem Qwenu panuje v diskusi jasno: u/doneddat i u/returnity radí podporovat Qwen 3.8, protože čtyřka do ní zapadne s minimálními úpravami a nejpopulárnější MoE model přitáhne nejvíc testerů. Zbytek vlákna jsou hlavně natažené ruce, u/long4994 žádá GitHub k vyzkoušení, u/ninjazombielurker slibuje testy na CMP 170HX, třech generacích GeForce i síťovém úložišti přes NVMe-oF a u/dinominant nabízí CPU testy plných vah GLM a Kimi K3.

Pro běžného uživatele je pointa prostá: pokud čísla sedí i mimo autorův stroj, velké MoE modely by se vešly na obyčejný notebook a SSD by se stalo levnou náhradou za drahou RAM.
