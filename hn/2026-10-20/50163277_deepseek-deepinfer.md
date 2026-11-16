# 50163277
**DeepSeek otevřel DeepInfer, inferenční framework pro své modely**

Hacker News · ggcr · 20. října 2026, 11:08 · 2188 bodů / 848 komentářů · [diskuse](https://news.ycombinator.com/item?id=50163277)

DeepSeek zveřejnil na GitHubu DeepInfer, inferenční framework, který podle vlastního popisu pohání jeho rozsáhlé produkční služby. Odkaz bez dalšího komentáře přidal uživatel ggcr a vlákno se rychle rozrostlo do jedné z nejživějších diskusí dne.

Open-source vydání nabízí offline inferenci pro model DeepSeek-V4.1-Flash a stojí na optimalizovaných kernelech FlashMLA, DeepGEMM, DeepEP, TileKernels a DeepSelect. Láká na paralelismus Attention DP a MoE EP s vyvažováním zátěže, asynchronní plánovač překrývající práci procesoru s během na akcelerátoru, deterministické vzorkování, strukturované výstupy i verifikaci draft tokenů řízenou spolehlivostí. Běží na Nvidii SM100 a Huawei Ascend 950, vyšlo pod licencí Apache 2.0 a přiznává, že původně vyrostlo hlavně na vLLM s inspirací v SGLang a TensorRT-LLM.

Největší rozruch ale nevzbudil seznam funkcí, nýbrž čísla, která z čínského serveru Zhihu vytáhl uživatel schneehertz: jeden cluster prý zvládne 155 bilionů tokenů denně a při mimosezónní ceně generuje 38 dolarů na kartu za hodinu. Uživatel abound to přivítal jako konečně tvrdá data proti tezi, že se za dolar utrácený za umělou inteligenci vydělává jen padesát centů, protože amortizované náklady na datacentrum plné grafik jsou hluboko pod touto částkou. Uživatel schleck8 dopočítal, že při čistých 35 dolarech za hodinu a třech dolarech provozních nákladů by se grafika za 30 tisíc dolarů zaplatila za zhruba 850 hodin, tedy asi 35 dní, a uživatel throwa356262 připomněl strategii DeepSeeku, že se každý projekt musí zaplatit do deseti měsíců.

Vedle nadšení se ozvaly i pochyby o měřítku. Uživatel carstonh upozornil, že OpenRouter hlásí za celý minulý týden 164 bilionů tokenů, takže jeden takový cluster by teoreticky pokryl skoro celou jeho poptávku, a ptá se, zda se neztratilo něco v překladu jednotek. Uživatel itkovian_ mluví o zásadním datovém bodu a marži o řád vyšší, než se běžně diskutuje, když srovnává 38 dolarů s nájmem H100 kolem dvou dolarů za hodinu. Uživatel louiereederson z toho vyvozuje opačný závěr pro poskytovatele výpočetního výkonu: pokud se open-source inferenční enginy rozšíří, stlačí cenu inference k holým nákladům na kartu.

Třetí linka vlákna řeší geopolitiku a originalitu. Uživatel wg0 označil vydání za kamikaze pro americké frontier laboratoře a cestu k bilionovým valuacím, uživatel BetterThanSober v čínských otevřených modelech vidí zástupnou ekonomickou válku proti americkému monopolu na špičkové modely. Do toho uživatel Tepix klade věcnou otázku, proč by měl být projekt postavený na vLLM naprostým měničem hry, a uživatel bonplan23 dodává, že investoři podobnému nadšení nevěří, protože západní korporace podle nich čínské modely kvůli bezpečnosti, regulaci a kontinuitě provozu stejně nenasadí.

Z diskuse tak zůstává hlavně otázka, zda otevřený a vysoce efektivní inference framework přepíše ekonomiku provozu modelů, nebo jen přitlačí na ceny a nervy konkurence.
