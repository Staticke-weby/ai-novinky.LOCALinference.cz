# 1x682nm
**Úplně lokálně: majitel pivovaru přesedlal na Qwen 3.8 Next Flash**

r/LocalLLM · u/bushizell · 15. října 2026, 02:48 · 503 bodů / 84 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1x682nm/)

Autor provozuje jednočlenný pivovar a skoro čtyři měsíce mu celý backend běžel na Claude Cowork, hlavně na extrakci z PDF. Když Anthropic oznámil, že se Scheduled Tasks, na kterých pivovar stojí, přesouvají do cloudových verzí, rozhodl se odejít. Než mu dorazil nový Ryzen box, rozchodil na kartě 5070 Ti model Qwen 3.6-35B-A3B a za hektický týden se naučil, co je llama.cpp, Hermes, harness a inference enginy.

Novou sestavu se mu nakonec podařilo rozjet s enginem Gufo, modelem 3.8 Next Flash a několika boty přes Hermes. Sám tvrdí, že je teď téměř ze sta procent mimo předplatné, i když mu ještě zbývá práce, a těší se na další ladění.

Diskuse se nejdřív rozjela vtipkováním o hardwaru. Nejvýše hodnocený u/AmuckDismissal píše, že ta malá AMD krabice vypadá jako součást kyberpunkové pletací sady, a u/derspenti glosuje, že pivo bylo vždycky lokální a teď je lokální i backend. Věcnější notu přidal u/devtools-dude, podle kterého je Flash Next úžasný i proto, že lze engramy odkládat do RAM a na SSD a výkon je pořád skvělý – sám na něm prý postavil web subshell.sh, což dokazuje, že se na něm dají dělat složité věci.

Hodně lidí zajímalo, jak pivovarský provoz v praxi vypadá. u/specialmoose prosí o vysvětlení, co přesně dělá s extrakcí z PDF, u/Stunning-Sherbet1853 se ptá, jak jako mezistupeň obstála 5070 Ti s modelem 35B-A3B a jestli narazil na strop 16 GB paměti. u/MikaMoments to shrnuje pochvalou, že skutečná výhra je rozjet si lokálně reálné firemní workflow, ne jen si povídat s modelem, a ptá se, co bylo větší překvapení – kvalita modelu, nebo to, co dokáže správný harness. Podobným směrem míří i u/Own-Storm4557, který řeší specifikace a ceny grafik, a u/bySimori, jenž zvažuje odchod z cloudu a neví, zda jít do více Nvidií, počkat na M5 Ultra, nebo vzít Halo.

Sám autor se do vlákna vrátil s aktualizací ze zátěžového testu. Přes SSH a Tailscale VPN ještě dopracovává nastavení pomocí Opus 5.5 a 3.8 Next Flash podle něj s přehledem zvládl nejtěžší úkol – zrekonstruovat plný letní den se všemi fermentory plnými a čerstvým záznamem o dni várky při zvýšené kompresi. Sedmasedmdesát volání nástrojů a ani jedno vadné, jak píše, ho viditelně nadchlo.

Zbytek vlákna patří radám kolem sestavy. u/mainstsavage doporučuje inference engine vLLM s vlastními přepínači a jako harness Hermes Agent Desktop, případně pro týmy botů zkusit Qwen 3.6-35B-A3B nebo hutný Qwen 3.8-27B na agentní kódování. u/iceadobe chválí Int4 variantu, se kterou se při dobrém MTP návrhu dostává na 90 tokenů za sekundu a běžně drží přes 50 i se třemi souběžnými agenty na různých repozitářích. Někdo se ptá na přesný typ Ryzen boxu a rozdíl proti DGX Spark, jiný doufá v srovnání x86 a ARMu na sjednocených mašinách.

Příběh tak působí jako malá studie o digitální soběstačnosti: z donucení kvůli cloudu se vyklubal funkční lokální backend na pivo.
