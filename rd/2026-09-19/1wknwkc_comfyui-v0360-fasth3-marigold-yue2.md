# 1wknwkc

**ComfyUI v0.36.0: podpora FastH3, Marigold V2 a YuE2, nové smyčky a uzly pro video**

| | |
|---|---|
| Subreddit | r/comfyui |
| Autor | u/Gremlation |
| Publikováno (Europe/Prague) | 19. 9. 2026, 16:37 |
| Skóre / komentáře | 56 / 17 |
| Odkaz | https://www.reddit.com/r/comfyui/comments/1wknwkc/comfyui_v0360/ |
| Diskuse | https://www.reddit.com/r/comfyui/comments/1wknwkc/comfyui_v0360/ |

## Co se stalo

Uživatel u/Gremlation zveřejnil na r/comfyui **poznámky k vydání ComfyUI v0.36.0** (samotné vydání je datováno **15. září 2026**). Verze přidává podporu tří open-source modelů: **FastVideo FastH3** pro převod textu a obrázku na video s nativním zvukem, **Marigold V2** pro odhad hloubky, normál a albeda a **YuE2** pro generování hudby ze stylových promptů a textu.

Mezi novými vestavěnými uzly jsou **Video Concatenate**, **obecné smyčky nad seznamy** (Generic Loops), lineární varianta ImageColorSpace a **GeminiNodeV3**, který nahrazuje zastaralý uzel V2. Aktualizace partnerských uzlů přinášejí 3D generování **Tripo P2**, video **Pruna P-Video-2**, **Flux Video Edit** pro úpravy videa textovými instrukcemi a sadu úprav Bria včetně Video Eraseru. Součástí jsou i optimalizace paměti u VAE pro MiniMax-H3, rychlé kernely pro llama rope a opravy na AMD. Šablony workflowů se posunuly na v0.11.62.

Diskuse je krátká a smíšená: jeden uživatel je nadšený z obecných smyček, jiný hlásí **zhoršení výkonu** po aktualizaci a další **problémy s instalací na Ubuntu**. Objevila se i poznámka, že příspěvek je o čtyři dny opožděný.

## Klíčová fakta

- **Verze a datum:** ComfyUI v0.36.0, vydáno 15. 9. 2026.
- **Nové modely:** FastVideo FastH3 (video s nativním zvukem), Marigold V2 (hloubka/normály/albedo), YuE2 (hudba ze stylu a textu).
- **Nové uzly:** Video Concatenate, obecné smyčky nad seznamy, lineární ImageColorSpace, GeminiNodeV3 (V2 zastaralý).
- **Partnerské uzly:** Tripo P2 (3D), Pruna P-Video-2 (video, 720p/1080p, draft režim), Flux Video Edit, sada Bria + Video Eraser.
- **Výkon a stabilita:** automatická detekce rychlých disků pro `--fast-disk`, optimalizace paměti VAE pro MiniMax-H3, rychlé kernely llama rope, kvóta 4 TB u AMD Windows VA, opravy YuE2 na AMD (skladby až 900 sekund).
- **Opravy chyb:** Add Noise už nepřidává šum do alfa kanálu; H3 Fun ControlNet při aktivním model compileru.
- **Šablony:** v0.11.62 s novými šablonami pro FastH3, Marigold V2 a YuE2.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Datum vydání v0.36.0 | 15. 9. 2026 |
| Skóre / komentáře postu | 56 / 17 |
| Verze šablon workflowů | v0.11.62 |
| Maximální délka skladby YuE2 | 900 sekund |
| Kvóta AMD Windows VA | 4 TB |
| Rozlišení Pruna P-Video-2 | 720p / 1080p |
| Distilovaný MiniMax H3 (komentář) | 8 kroků |
| Komentářů v balíčku | 12 |

## Citace

> „Na obecné smyčky se velmi těším! Vypadá to jako robustnější verze toho, co bylo v balíčku uzlů Easy-Use.“ (překlad) — u/altoiddealer, 8 bodů

> „Jsi trochu pozdě, to bylo před 4 dny.“ (překlad) — u/Davikar

> „Klidně to sem postněte sami dřív.“ (překlad) — u/Gremlation

> „Nefunguje to na Ubuntu 26.4. Aktualizace na .36 drží aimdo na 0.5.3 a ruční aktualizace aimdo stejně nespustí fast disk.“ (překlad) — u/car_lower_x

> „Špatná aktualizace pro moji sestavu s r9700, Krea2 bylo 2 s/iterace a teď je 4 s/iterace. Nevím, co způsobilo takový propad výkonu. ComfyUI se někdy taky prostě zastaví a načtení text encoderu nebo start generování trvá znatelně dlouho.“ (překlad) — u/Alekite

> „Díky za sdílení. Líbí se mi fastH3, 8 kroků je lepších než 4kroková LoRA s 8 kroky.“ (překlad) — u/Diligent_Garlic_5350

> „Testoval jsem všechny nízkokrokové modely… nic nepřekonalo původní šablonu H3 s předstaženými 8 kroky v Comfy.“ (překlad) — u/seppe0815

## Co říkají komentáře

Vlákno je krátké a **smíšené**. Na jedné straně stojí nadšení z **obecných smyček**, které podle komentujícího nahrazují dřívější řešení z balíčku Easy-Use, a chvála kvality **fastH3 v 8 krocích**. Na druhé straně jsou **konkrétní problémy po aktualizaci**: nefunkční detekce rychlých disků na Ubuntu, výrazné zpomalení u Krea2 na kartě r9700 a stížnost, že se ComfyUI občas zasekne při načítání text encoderu. Zaznívá i názor, že původní šablona H3 s předstaženými 8 kroky je stále nejlepší — tedy spor o to, zda nové distilované modely skutečně přinášejí zlepšení.

## Rozpory a neověřené informace

- **Neshoda:** u/Diligent_Garlic_5350 tvrdí, že 8 kroků u fastH3 je lepší než 4kroková LoRA s 8 kroky, u/seppe0815 tvrdí, že nic nepřekonalo původní šablonu H3 s předstaženými 8 kroky.
- **Neshoda:** u/Davikar považuje příspěvek za opožděný („to bylo před 4 dny“), autor odpovídá, že si to může kdokoli postnout dřív.
- **Neověřená hlášení:** konkrétní chyby a propady výkonu (Ubuntu 26.4, aimdo 0.5.3, Krea2 z 2 s/it na 4 s/it) jsou zkušenosti jednotlivých uživatelů, bez doloženého potvrzení.

## Proč to je důležité

Vydání ukazuje, kterým směrem se ComfyUI posouvá: od generátoru obrázků k **jednotnému uzlu pro video, zvuk a hudbu** — FastH3 s nativním zvukem a YuE2 pro hudbu jsou v jednom balíčku s 3D generováním a sadou pro úpravy videa. Pro praktické uživatele je ale nejcennější právě ta druhá část vlákna: **konkrétní regrese po aktualizaci**. U nástroje, který se aktualizuje tak často, je zkušenost komunity s kompatibilitou (a možnost zůstat na starší verzi) stejně důležitá jako seznam novinek.

## Zdroje

- https://docs.comfy.org/changelog
- https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.36.0
- https://www.reddit.com/r/comfyui/comments/1wknwkc/comfyui_v0360/
- komentáře: `2026-09-19/_data/raw/comments.json` (klíč `1wknwkc`), balíček `2026-09-19/_data/bundles/1wknwkc.md`
