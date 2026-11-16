# 1wmh9rg

**Benchmarková tabulka Grok 4.7: vede v právu a elektrotechnice, ale spotřebuje ~2× víc tokenů než 4.6**

| | |
|---|---|
| Subreddit | r/singularity |
| Autor | u/krizzalicious49 |
| Publikováno (Europe/Prague) | 21. 9. 2026, 18:13 |
| Skóre / komentáře | 216 / 108 |
| Odkaz | https://i.redd.it/i84bqhdeewqh1.jpeg (screenshot benchmarkové tabulky) |
| Diskuse | https://www.reddit.com/r/singularity/comments/1wmh9rg/grok_47_benchmarks/ |

## Co je v tabulce (opsáno ze screenshotu)

Srovnání **Grok 4.7 (xhigh)**, **Grok 4.6 (high)**, **GPT-5.6 Sol (max)** a **Fable 5.1 (max)**:

| Metrika | Grok 4.7 | Grok 4.6 | GPT-5.6 Sol | Fable 5.1 |
|---|---|---|---|---|
| Cena vstupu ($/M) | 2 | 2 | 4 | 10 |
| Cena výstupu ($/M) | 6 | 6 | 20 | 50 |
| CursorBench 4.0 (SWE) | 46,3 % | 40,4 % | 41,7 % | **51,8 %** |
| DeepSWE v1.1 (SWE) | 71,0 %* | 65,2 % | **72,7 %** | 70,0 % |
| AA Briefcase v1.1 (multi-hour office) | 1 657 | 1 546 | 1 487 | **1 678** |
| Terminal-Bench 4.0 | 38,0 % | 20,3 % | 37,3 % | **57,9 %** |
| Harvey Legal Agent Benchmark | **19,6 %** | 15,8 % | 2,5 % | 6,7 % |
| HealthBench Professional | 56,7 % | 48,5 % | 60,5 % | **62,1 %** |
| EEBench (elektrotechnika) | **64,0 %** | 53,0 % | 39,4 % | 56,4 % |

## Klíčová fakta

- Grok 4.7 vede pouze **legal work (19,6 %)** a **EEBench (64,0 %)**; ve většině ostatních řádků vede Fable 5.1.
- Model je provozován v režimu **xhigh** reasoning proti **high** u 4.6 — srovnání tedy není izolované od úsilí.
- U DeepSWE v1.1 má Grok 4.7 hodnotu s **hvězdičkou** (71,0 %*), vysvětlení v tabulce chybí — diskuse se na to ptá.

## Čísla a sporný bod

- Podle komentujících (u/Momo--Sama) jsou výstupní tokeny na úkol dle AA: **Grok 4.5 High 27k → 4.6 High 36k → 4.7 High 66k**.
- Z toho plyne: při stejné ceně za token by průměrný úkol mohl být ~2× dražší.

## Citace

> „Všimněte si „xhigh“ u úrovně uvažování oproti pouhému „high“ u 4.6. Jistě, stejná cena, ale pokud uvažuje déle a plýtvá více tokeny, může jít o podobný model s velmi nepatrným ziskem, ale vyššími inferenčními náklady.“ (překlad) — u/ImplementAbject3617

> „Ježíši… takže v podstatě trojnásobná cena za průměrný úkol.“ (překlad) — u/ASQQS

> „Na tu cenu je to docela působivé.“ (překlad) — u/Forward_Yam_4013 (skóre 71)

> „V podstatě pokračování stejného trendu kupování vyšších skóre v benchmarcích za více výstupních tokenů“ (překlad) — u/FateOfMuffins

## Co říkají komentáře

- **Cena vypadá skvěle** — dokud se nepodíváte na tokeny na úkol (nejvýš hodnocená chvála vs nejsilnější kritika).
- **Nefer srovnání úsilí:** xhigh vs high znamená, že „stejná cena“ je při vyšším výpočetním úsilí jen nominální.
- **Právní a elektrotechnické výsledky** jsou označovány za reálný pokrok (u/PilgrimofHaqq2: „Muse má pořád navrch“, překlad).
- **Předplatné vs API:** pro běžné uživatele je důležitější, kolik použití dostanou v rámci subscription než cena za token.

## Neověřené informace

- Čísla output tokenů na úkol jsou z komentáře, ne z tabulky.
- Spekulace, že vyšší EEBench souvisí s napojením na data SpaceX.
- Tvrzení, že 4.7 „spěchal tokeny“ a byl špatný na analogovém EE benchmarku.

## Proč to je důležité

Tabulka je názorný příklad nové generace benchmarků (vícehodinová kancelářská práce, právní agent, klinické uvažování, elektrotechnika) místo klasických akademických sad. Zároveň ukazuje, že **vítězství v benchmarku se dá koupit delším přemýšlením** — proto je při hodnocení nutné číst i cenu za token a úsilí, ne jen skóre.

---

*Zdroje: [screenshot tabulky](https://i.redd.it/i84bqhdeewqh1.jpeg), [Reddit diskuse](https://www.reddit.com/r/singularity/comments/1wmh9rg/grok_47_benchmarks/).*
