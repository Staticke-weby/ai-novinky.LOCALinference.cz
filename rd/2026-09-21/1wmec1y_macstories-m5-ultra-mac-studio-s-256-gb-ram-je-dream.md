# 1wmec1y

**MacStories: M5 Ultra Mac Studio s 256 GB RAM je „dream machine“ pro lokální AI agenty**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/themixtergames |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 327 / 140 |
| Recenze | https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmec1y/m5_ultra_mac_studio_review_the_dream_mac/ |

## Co se stalo

Federico Viticci (MacStories) publikoval recenzi **M5 Ultra Mac Studio s 256 GB RAM**, kterou označuje za **„vysněný stroj pro lokální AI agenty“** (překlad) — osobní asistenty na lokálních modelech bez dalších cloudových nákladů. Testoval ji od minulého čtvrtka proti **M3 Ultra s 512 GB RAM** a desktopu s **RTX 5090**; podle recenze si 5090 drží výhodu v paměťové propustnosti.

Zmíněno je i to, že **Qwen3.8-Flash-Next** byl dost rychlý, aby se stal autorovým defaultem v Open Minis pro iOS. Post upozorňuje, že **embargo na recenze M5 Mac Studio a M6 Mac Mini právě spadlo**, ale většina videí AI část řeší povrchně (staré 70B Llama nebo Qwen 2.5).

## Čísla z diskuse

- M5 Ultra: **1,2 TB/s** paměťová propustnost, **1,8 TB/s** interconnect (tvrzení komentujících).
- Ceny a alternativy: „12 tisíc dolarů hardwaru“, „2× Pro 6000 za 30 tisíc“, „2,5× RAM za 70 % ceny jednoho 6000“.
- Ekonomika: leasing ~**240 USD/měsíc** vs Codex ~100 USD/měsíc; prodej po 3 letech za ~50 % → ~167 USD/měsíc.
- Naměřené hodnoty v diskusi: 80 tok/s, **997 tok/s u 5.3 Flash při 128K kontextu**, 30–40 tok/s u Qwen3.8-flash-next na Strix Halo, dual DGX Spark 273×2 = 546 GB/s.

## Citace

> „Půjdu rovnou k věci: M5 Ultra Mac Studio je vysněný stroj pro lokální AI agenty.“ (překlad) — Federico Viticci

> „Posledních pár dní testuji (momentálně) špičkový M5 Ultra Mac Studio s 256 GB RAM.“ (překlad) — Federico Viticci

> „Embargo na recenze M5 Mac Studio a M6 Mac Mini bylo zrušeno, ale žádné z videí zatím nejde do hloubky ohledně AI…“ (překlad) — u/themixtergames

> „Ta čísla jsou úžasně dobrá.“ (překlad) — u/OvertaxedOne

> „Tohle je hardware za 12 tisíc, za to bych nečekal nic menšího.“ (překlad) — u/sn2006gy

## Hlavní linky diskuse

- **Apple vs Nvidia.** Srovnání s 2× RTX Pro 6000, dual DGX Spark a 5090: část lidí považuje výkon za výborný za cenu, část upozorňuje, že na souběžné (paralelní) agenty je stále potřeba Nvidia.
- **Cena, leasing a předplatná.** Klíčová otázka: vyplatí se vlastnit Mac za ~12 tisíc, nebo platit 240 USD/měsíc a mít jistotu odepisu?
- **Kvalita recenzí.** Kritika recenzentů, kteří testují staré modely — reálný přínos mají jen měření s aktuálními (Flash-Next, Qwen 27B, GLM 5.3 Flash).

## Rozpory a neověřené informace

- **Rozpor:** jsou čísla „astoundingly good“ vs pomalejší než dvě DGX Spark / jedna RTX Pro 6000 s vLLM.
- **Rozpor:** je lokální inference dnes reálná pro práci (Qwen3.8-flash-next > Opus 4.6 lokálně) vs „na paralelní agenty to zdaleka nestačí“.
- **Neověřené:** leakované benchmarky omlx/qwen3.8-flash-next, konfigurace 512GB Macu na říjen, různé tok/s hodnoty od komentujících.

## Proč to je důležité

Recenze kodifikuje pozici Applu v lokální AI: **hodně sjednocené paměti a slušná propustnost za cenu, kterou Nvidia nenabídne** — ale bez absolutní špičky a s horším poměrem při souběžné zátěži. Pro tým nebo jednotlivce, který chce provozovat agenty lokálně (a neplatit za tokeny), je M5 Ultra dnes nejdiskutovanější volbou; ekonomické srovnání s předplatnými ale vychází překvapivě vyrovnaně.

---

*Zdroje: [MacStories recenze](https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmec1y/m5_ultra_mac_studio_review_the_dream_mac/).*
