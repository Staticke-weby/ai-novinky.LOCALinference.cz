# 1x6o31q
**NVIDIA Nemotron 3.5 Bolt: 74B model do 24 GB paměti**

r/LocalLLaMA · u/jacek2023 · 15. října 2026, 17:04 · 467 bodů / 228 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x6o31q/)

NVIDIA vydala Nemotron 3.5 Bolt 74B-A9B 24GB, vision-language model pro každodenní agentské úlohy na lokálním stroji. Trik je v nativní 2bitové kvantizaci s tréninkem vědomým kvantizace, díky níž se 74 miliard parametrů vejde do 24 GB a vedle modelu běží i další aplikace. Autor příspěvku přihodil odkazy na GGUF varianty včetně verze pro spekulativní dekódování.

Podle karty modelu jde o hybrid Mamba-2 a Transformeru s LatentMoE a vision enkodérem, z 74 miliard parametrů je aktivních 9 miliard. Kontext sahá až k 256 tisícům tokenů, na vstupu zvládne text, obrázky i video a režim uvažování se přepíná šablonou chatu. Pro nasazení se počítá s vLLM na Ampere, Hopper a Blackwell, spekulativních 7 tokenů řeší drafter LiLiCorr a licence je OpenMDW-1.1 pro komerční i nekomerční užití.

Diskuse se okamžitě stočila ke srovnání s Qweny. u/ForsookComparison žasne, že se 74 GB po kvantizaci vešlo na 24 GB na disku, a tipuje, že by model mohl u někoho poslat do důchodu Qwen3.6-35B. u/MerePotato ho má za nejlepší model pro spotřebitelský hardware hned po Qwen 3.8 27B, který ale všechno ostatní shazuje, zatímco u/hurn2k jen suše utrousí, že poměřovat se s Qwen 3.6 bolí. Skeptičtější hlas přidává u/_Slave_to_Armok_, jemuž Bolt na vlastních testech přijde pomalejší a hloupější než Qwen3.6-35B-A3B v Q6.

Nejcennější jsou hlášení z reálného provozu. u/Budkovsky ho zkoušel na dvou RTX 5060Ti po 16 GB v režimu dělení vrstev: při čerstvé relaci naměřil kolem 58 tokenů za sekundu při generování a asi 1700 při prefillu, při využitých 35 tisících kontextu pak 50 tokenů za sekundu. Umí prý moderní syntaxi a hodí se na procházení kódu, ale v polštině píše hůř než Qwen 27B a na jednoduchém problému se zasekl. u/Painted-Arcana na 5070 Ti se 128 GB RAM dává asi 45 tokenů za sekundu při 128tisícovém kontextu a spotřebě kolem 15 GB VRAM, chystá se ho zapřáhnout do opencode.

Zbytek vlákna řeší detaily a špičkuje. u/Hefty_Wolverine_553 cituje pasáž o syntetických datech z Kimi-K3 cílených na AIME, GPQA Diamond či Terminal Bench a ptá se, zda NVIDIA právě nepřiznala ladění na benchmarky. u/geldonyetich se diví, že u modelu jménem Bolt chybí čísla o rychlosti, a zjišťuje, jestli LiLiCorr verze nechce Blackwell. Vedle nadšení u/Septerium, že 2bitový QAT MoE model by mohl založit nový trend, tak zapadá i poctivý kouřový test u/RedditUsr2, v němž se model nedokázal přesvědčit, že běží lokálně.

Kdo má 16 až 24 GB grafiky a nechce model drtit agresivní kvantizací, dostal další vážnou volbu vedle Qwenů.
