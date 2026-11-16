# 1wms904

**phantom-kv: odstranění odmítání u LLM bez zásahu do vah — stačí ~18MB trénovaná banka KV cache**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Anony6666 |
| Publikováno (Europe/Prague) | 22. 9. 2026, 00:55 |
| Skóre / komentáře | 412 / 52 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1wms904/uncensor_an_llm_without_touching_weights_inject_a/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wms904/uncensor_an_llm_without_touching_weights_inject_a/ |

## Co se stalo

Na r/LocalLLaMA představil uživatel u/Anony6666 (na GitHubu **lordx64**) projekt **phantom-kv** — systém pro odstranění odmítavých odpovědí u jazykových modelů, který **nemění jedinou váhu**. Místo úpravy modelu načte do jeho **KV cache** natrénovanou banku tenzorů klíčů a hodnot; pozornost (attention) s ní pracuje jako s konverzační historií, která už v kontextu je. „Odcenzurování“ tím přestává být trvalou úpravou checkpointu a stává se **režimem přepínatelným za běhu**: po vyložení cache je základní model znovu bajtově identický. Autor k tomu zveřejnil i vlastní měření a sám upozorňuje, že lexikální metriky nadhodnocují úspěšnost. V diskusi se strhla debata, zda nejde jen o skrytý systémový prompt.

## Klíčová fakta

- **Mechanismus:** banka K/V tenzorů na vrstvu se vkládá do cache na pozice 0..N; velikost artefaktu je **18,1 MB** u všech verzí štěpu.
- **Vývoj verzí:** v1 byl ručně psaný „prefill“ o 129 slotech; v3 je naučená přímá banka K/V s **9,4 milionu parametrů**.
- **Výsledky na Qwen3-4B-Instruct-2507** (sada 60 škodlivých a 20 neškodlivých promptů, greedy dekódování): základní model odmítl **25/60**, v1 **15/60** (KL 0,367 / 0,604), v2.0 **3/60** (KL 0,452 / 2,678), v2.1 **8/60** (KL 0,041 / 0,137), v2.2 **5/60** (KL 0,043 / 0,073) a v3 **5/60** (KL 0,015 / 0,059). U neškodlivých promptů bylo odmítnutí **0/20** ve všech verzích.
- **Přenos mimo testovací sadu:** na 60 odložených škodlivých promptech klesl počet odmítnutí ze 5/60 (základ) na 2/60 (v3), ale KL divergence mimo sadu vzrostla na 0,404 v průměru a 0,834 v maximu (proti 0,015 v rámci sady).
- **Vytrvalost:** štěp slábne s poločasem **~2–4 tisíce tokenů**; po 16 tisících tokenech se vrátí zhruba **5 ze 6** potlačených odmítnutí. Opakované vkládání udrží 4 z 5 „tvrdých“ odmítnutí potlačených.
- **Cena na schopnostech:** MMLU zůstává **54/100** shodně u všech verzí; míra finálních odpovědí u GSM8K klesá u v3 z **45/75 na 27/75** při rozpočtu 256 tokenů.
- **Režimy („pills“):** black, red, blue, redlite a red2 se přepínají výměnou 129 cache slotů. První matice vznikla 19. 9. 2026 (režim blue vynuloval kyberobranná odmítnutí ze 4 na 0), režim red2 z 21. 9. 2026 snížil odmítnutí v cílové doméně z **61 na 5** (tedy o 91,8 %), ovšem s úniky do obecné sady.
- **Vlastní audit:** soudcovský model Qwen3-8B čte u kyberofenzivní domény **~59–61 z 81** sémantických odmítnutí u každé varianty, zatímco lexikální klasifikátor hlásil mezi 5 a 61 — autor proto uvádí, že lexikální metriky nadhodnocují compliance.
- **Ověřená mechanika:** uložení a načtení cache je bitově shodné, rozdíl logitů po round-tripu **0,000e+00**; zdvojení štěpu otočí všech 5 zbývajících odmítnutí a po 4 tisících tokenech výplně jich udrží 4 z 5.
- **Omezení:** plně validováno jen na **Qwen3-4B**; každý štěp je vázán na konkrétní revizi modelu (přetrénování ~1 hodina na notebooku); rekurzivní chat template modelů GLM phantom-kv odmítá (baseline GLM 20/60); nasazeno zatím jen na Qwen3 dense (Apple MPS/bf16).
- **Repo:** Python, MIT licence, 127 hvězdiček, 17 forků, 1 issue.

## Čísla

| Verze štěpu | Odmítnutí (z 60) | KL průměr / max |
|---|---:|---|
| základní model | 25/60 | — |
| v1 (ruční prefill, 129 slotů) | 15/60 | 0,367 / 0,604 |
| v2.0 | 3/60 | 0,452 / 2,678 |
| v2.1 (m=3,0) | 8/60 | 0,041 / 0,137 |
| v2.2 (m=2,5) | 5/60 | 0,043 / 0,073 |
| v3 (naučená banka, 9,4M parametrů) | 5/60 | 0,015 / 0,059 |

| Další údaje | Hodnota |
|---|---:|
| Velikost artefaktu | 18,1 MB |
| Poločas slábnutí štěpu | ~2–4 tisíce tokenů |
| Odmítnutí u neškodlivých promptů | 0/20 (všechny verze) |
| MMLU | 54/100 (shodně) |
| GSM8K (finální odpovědi) | 45/75 → 27/75 (v3, 256 tokenů) |
| Režim red2, cílová doména | 61 → 5 odmítnutí (−91,8 %) |
| Skóre příspěvku / komentářů | 412 / 52 |
| Nejhlasitější komentář (u/Velocita84) | 171 bodů |

## Citace

> „Vypustil jsem něco, na čem jsem posledních pár týdnů pracoval: phantom-kv, systém pro odstranění odmítání u velkých jazykových modelů, který se nedotkne jediné váhy.“ (překlad) — u/Anony6666, vlastní text postu

> „Výsledkem je, že se ‚odcenzurování‘ přestává být trvalou úpravou checkpointu a stává se režimem schopností přepínatelným pro každý požadavek: vyložte cache a základní model je znovu bajtově identický.“ (překlad) — u/Anony6666

> „Také jsme si dělali audit sami: audit s 8B modelem coby soudcem ukazuje, že lexikální metriky potlačení odmítání nadhodnocují compliance (sémantické odmítnutí často přetrvává v přeformulované podobě).“ (překlad) — u/Anony6666

> „Odstranění odmítání jako načitatelný štěp do KV cache — žádná úprava vah, žádná projekce směru odmítání, plně reverzibilní.“ (překlad) — lordx64, popis repozitáře

> „Dodávejte megabajty, ne checkpointy — vyložte cache a základní model je znovu bajtově identický.“ (překlad) — lordx64, README

> „Takže je to prostě… systémový prompt? Který nevidíte?“ (překlad) — u/Velocita84, 171 bodů

> „Smyslem těch 18 MB v KV cache není to, že obsahují jailbreak instrukce; jde o to, že KV bajty obešly váhy úplně, a jsou tedy na necenzurované trajektorii.“ (překlad) — u/datbackup

> „Jo, mně to zní jako nějaká prompt injection.“ (překlad) — u/RobbinDeBank, 57 bodů

> „Tohle je v podstatě prefix tuning s novým jménem (Li & Liang trénovali past_key_values jako parametry už v roce 2021), což není výtka, fungovalo to i tehdy.“ (překlad) — u/Open-Adhesiveness-86

> „Jailbreak, který vyprchá po 4 tisících tokenech, je buď nejpoctivější přístup v tomhle prostoru, nebo omylem ten nejbezpečnější.“ (překlad) — u/Dear_Boat_416

> „Hodně lidí, co sem píše, zjevně nechápe, že ta videa **opravdu** ukazují, že štěp funguje.“ (překlad) — u/Amazing-Fan2083, 96 bodů

> „Poctivý stav dneška: plně validováno jen na Qwen3-4B.“ (překlad) — lordx64

## Co říkají komentáře

Nejvýraznější je **podezření, že jde o skrytý systémový prompt** — nejlépe hodnocený komentář (171 bodů) se ptá, zda to není prompt, který uživatel nevidí, a další ho doplňuje („zní to jako prompt injection“). Jiný diskutující mechanismus obhajuje: podle něj nejde o instrukce, ale o to, že cache obchází váhy. Druhé téma je **spor o důkazy**: jeden komentující tvrdí, že videa neukazují funkčnost, jiný (96 bodů) oponuje, že ukazují. Třetí téma je **stabilita a kontext**: objevují se dotazy na ředění kontextu, na vliv omezení sliding-window attention, na přežití kvantizace cache do q8 a na to, že štěp po pár tisících tokenech slábne — autor sám přiznává, že plná validace existuje jen pro Qwen3-4B. Čtvrté téma je **jiné využití** než odstraňování odmítání: vkládání persony, řízení stylu nebo „datové banky“.

## Rozpory a neověřené informace

- **Neověřená měření autora:** celá tabulka odmítnutí, hodnoty KL, přenos mimo sadu, cena na GSM8K i výsledky auditu se soudcovským modelem jsou autorova vlastní měření, nikoli nezávisle replikovaná.
- **Neověřené tvrzení autora:** že po vyložení cache je základní model bajtově identický — v repozitáři je doložen jen bitově shodný round-trip uložení/načtení, nikoli to, že se štěp neprojeví jinak.
- **Neověřené tvrzení:** u/Amazing-Fan2083 spekuluje, že autor omezil počet generovaných tokenů, aby příspěvek nebyl smazán.
- **Neověřené tvrzení:** u/datbackup tvrdí, že KV bajty „jsou na necenzurované trajektorii“ — jde o interpretaci mechanismu.
- **Neověřené tvrzení:** u/droptableadventures namítá, že surová KV data nemusejí odpovídat stavu, kterého by šlo dosáhnout skutečnými tokeny.
- **Neověřené obavy:** u/Open-Adhesiveness-86 uvádí netestované problémy — pečení pozic RoPE (štěp pak funguje jen na začátku cache) a neznámé přežití kvantizace cache do q8.
- **Neshoda:** u/Velocita84 a u/Open-Adhesiveness-86 popisují mechanismus jako (neviditelný) systémový prompt, resp. prefix tuning, zatímco autor ho prezentuje jako nový přístup v prostoru kontextu.
- **Neshoda:** u/fgk55555 tvrdí, že videa neukazují funkčnost; u/Amazing-Fan2083 tvrdí opak.
- **Neshoda:** autor uvádí nezávislost na enginu a architektuře, komentující namítají limity u sliding-window attention a mezi modely; autor připouští, že plně ověřeno je jen Qwen3-4B a že šablony GLM projekt odmítá.

## Proč to je důležité

phantom-kv je zajímavý hlavně tím, **kde vede hranici mezi váhami a kontextem**. Dosavadní metody odstraňování odmítání byly trvalé — přepsaly checkpoint nebo trvale zasáhly do běhu modelu. Přístup, který se dá za běhu načíst a zase vyložit a přitom nechá základní model beze změny, otevírá legitimní využití (například bezpečnostní týmy potřebující model v ofenzivním režimu pro analýzu malwaru) i zneužití. Autor zároveň předkládá neobvykle poctivá data: ukazuje, že **lexikální metriky nadhodnocují úspěch** (soudce vidí 59–61 sémantických odmítnutí tam, kde klasifikátor hlásil i 5) a že štěp má měřitelnou cenu na schopnostech (GSM8K 45/75 → 27/75) i omezenou vytrvalost. Právě tato transparentnost dělá z projektu užitečný referenční bod pro další výzkum v této oblasti.

## Zdroje

- https://github.com/lordx64/phantom-kv/ (repozitář, MIT licence)
- https://www.reddit.com/r/LocalLLaMA/comments/1wms904/uncensor_an_llm_without_touching_weights_inject_a/
- komentáře: `2026-09-22/_data/raw/comments/1wms904.json`
