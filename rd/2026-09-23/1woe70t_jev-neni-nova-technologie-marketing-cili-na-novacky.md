# 1woe70t

**Jev není nová technologie, jeho marketing cílí na lidi od LLM**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/tiensss |
| Publikováno (Europe/Prague) | 23. 9. 2026, 20:33 |
| Skóre / komentáře | 668 / 259 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1woe70t/jev_isnt_new_tech_its_marketing_targets_people/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1woe70t/jev_isnt_new_tech_its_marketing_targets_people/ |

## Co se stalo

Uživatel u/tiensss zveřejnil 23. 9. 2026 ve 20:33 (Europe/Prague) v r/LocalLLaMA diskusní příspěvek, podle kterého technologie „Jev" není novou třídou rozhodovacích modelů, ale běžné chování klasifikátoru s moderními zero-shot schopnostmi (klasifikace bez tréninku na konkrétní úloze).

Autor tvrdí, že Jev vydává pravděpodobnosti nad omezenou množinou voleb, negeneruje autoregresivně, nemůže vrátit neplatnou třídu a umí použít popisky definované až při inferenci. Nic z toho podle něj není nové — variacemi se roky zabývají zero-shot/NLI klasifikátory, embeddingové modely, cross-encodery a rerankery.

Srovnávání Jevu s LLM označuje za zavádějící: specializovaný klasifikátor je pochopitelně rychlejší a levnější, což ale nový paradigma nedokazuje. Zmiňuje benchmark BTZSC (22 datových sad) a experiment na Banking77 (93,3 % vs. 83,2 %).

Kritizuje i rámování „nemůže halucinovat": výrobce podle něj připouští, že údaj o 0 % halucinací není empirický, a garantuje jen shodu odpovědi s povoleným schématem — to zabrání neplatným výstupům, ne špatné, leč platné volbě.

Autor uzavírá, že Jev může být dobrý produkt a jeho nezveřejněná architektura či metoda RLCD mohou být nové, ale veřejné důkazy neprokazují, že „System One Models" jsou novou třídou AI.

## Klíčová fakta

- Podle autora všechny inzerované vlastnosti Jevu odpovídají standardnímu chování klasifikátoru a srovnání s LLM jsou zavádějící; odkazuje na benchmark BTZSC (22 datových sad) a na Banking77.
- Firemní vysvětlení podle něj připouští, že 0 % halucinací není empirický údaj; garantována je jen shoda se schématem.
- Příspěvek 1wo6o0f (skóre 1143, 238 komentářů) žádá moderátory o zásah proti reklamním postům o Jevu.
- Parodický článek NobodyWho (22. 9. 2026, Duarte O.Carmo) replikuje klasifikaci 25 řádky Pythonu s modelem Qwen3-0.6B-GGUF.
- Post 1wo6x7e popisuje otevřenou alternativu Bonsai-Llama-Jev nad Qwen3.8-27B; obrázek nese text „Bonsai-Llama-Jev" a „typed decisions · chat · image".

## Čísla

| Údaj | Hodnota |
|---|---|
| Skóre anchor postu 1woe70t | 668 |
| Komentářů u anchor postu | 259 |
| Podíl kladných hlasů anchor postu | 0,91 |
| Datové sady v benchmarku BTZSC | 22 |
| Banking77 — BGE-small + logistická regrese | 93,3 % |
| Banking77 — Jev | 83,2 % |
| Latence baseline na Banking77 | ~9 ms |
| Řádků kódu v názvu článku NobodyWho | 25 |
| Pravděpodobnosti Legitimate / Spam / Phishing | 0,031 / 0,084 / 0,885 |
| Logity Legitimate / Spam / Phishing | 26,254 / 27,262 / 29,614 |
| Kontext modelu Qwen3-0.6B v článku | 512 tokenů |
| Rozhodnutí v typed-decision-bench (post 1wo6x7e) | více než 22 000 |
| Případů užití v typed-decision-bench | 175 |
| Soft Accuracy Bonsai-Llama-Jev / Jev-1.13 | ~76 % / ~88 % |
| VRAM Bonsai-Llama-Jev | méně než 10 GB |
| p50 latence Bonsai-Llama-Jev / Jev | ~171 ms / 716 ms |
| Zrychlení oproti Jevu | ~4× |
| Kalibrační chyba ECE-15 Bonsai / Jev | 13 % / 8,4 % |
| Chat na RTX 5090 | ~143 tok/s |
| mmBERT s vlastním fine-tuningem | ~55 % |

Hodnoty z postu 1wo6x7e jsou vlastní měření jeho autora, v podkladu nezávisle neověřená.

## Citace

> „Vydává pravděpodobnosti nad omezenou množinou voleb, negeneruje autoregresivně, nemůže vydat neplatnou třídu a umí použít popisky definované až v okamžiku inference." (překlad) — u/tiensss, anchor post 1woe70t

> „Jejich vlastní vysvětlení přiznává, že údaj o 0% halucinacích není empirický, a že to, co skutečně garantují, je odpověď odpovídající povolenému schématu." (překlad) — u/tiensss, anchor post 1woe70t

> „Jev je placený produkt, který nasypal hodně peněz od venture kapitálu do vychvalování svého produktu tady i v jiných subredditech." (překlad) — u/Acrobatic_Stress1388, post 1wo6o0f

> „Pointa není v tom, že by to samo o sobě bylo něco nového, ale že to zjevně funguje opravdu dobře." (překlad) — u/radarsat1, komentář k anchor postu

> „Je to prostě obecný klasifikátor — levný a rychlý obecný klasifikátor, který používá vložené obecné znalosti místo specifického tréninku." (překlad) — u/ketosoy, komentář k postu 1wo07r8

> „Pointa je, že to není zázrak, ale dobrý marketing." (překlad) — u/johnnyApplePRNG, komentář k postu 1wo07r8

## Co říkají komentáře

Nejvýše hodnocený komentář (u/caldazar24, 154 bodů) připouští, že Jev může být jen mnohem větší zero-shot klasifikátor, a přirovnává to ke GPT-2 a GPT-3: šlo spíš o inženýrství než o vědu, ale svět to změnilo. Autor namítá, že GPT-2 a GPT-3 otevřeně dokumentovaly, co škálují, kdežto architektura Jevu zůstává skrytá.

u/puzzleheadbutbig (123 bodů) upozorňuje, že vývojáři Jevu sami říkají, že Jev není LLM ani SLM; autor oponuje, že marketing Jevu ho s LLM srovnával také a cílí na lidi, kteří znají jen LLM.

Praktický přínos hájí u/clduab11 (24 bodů): fine-tunovaný ModernBERT či GLiClass (GLiner) může Jev překonat v přesnosti na dolar, ale Jev nabízí rozhraní a levné kalibrované pravděpodobnosti nad velkým objemem dat s libovolnými schématy. u/GenAIDataScientist (16 bodů) mluví o zlomové kombinaci rychlosti, ceny a inteligence, u/ketosoy (154 bodů u parodického postu) o obecném klasifikátoru se správnou ergonomií.

Část diskuse tvoří únava z hype: u/Bird_ee (15 bodů) viděl víc stížností na nadšení než skutečného nadšení a u/Superb-Pair-2000 (5 bodů) soudí, že při takovém hype jde nejspíš o brak. u/4thepower (5 bodů) se ptá na důkaz vyšší přesnosti; autor odpovídá, že NLI zero-shot klasifikátory zvládaly libovolné popisy bez tréninku na úloze už od roku 2019.

## Rozpory a neověřené informace

- **S LLM, nebo s klasifikátory?** Anchor post považuje srovnání s LLM za zavádějící, u/puzzleheadbutbig namítá, že Jev sám LLM není.
- **Jsou posty reklama?** Post 1wo6o0f je označuje za placené promo, u/Illustrious_Grade608 (184 bodů) a u/profcuck (73 bodů) tvrdí, že většina zmínek řeší replikaci open-source modely.
- **Je Jev nový?** Autor odkazuje na klasifikátory z roku 2019, u/radarsat1 a u/GenAIDataScientist na výjimečnou kombinaci rychlosti, ceny a inteligence.
- **Koupená hype:** tvrzení, že tým Jevu zaplatil redditové a twitterové posty, je v podkladu bez důkazu.
- **Nezávisle neověřená čísla:** Banking77 pochází z druhého zdroje (jev-baselines-eval) a hodnoty z postu 1wo6x7e jsou vlastní měření jeho autora.
- **Laya jako předchůdce:** tvrzení o stopě výzkumu do roku 2025 je rámování autora postu 1wnyf0o.

## Další diskuse

Do souhrnu byly sloučeny čtyři související posty.

| id | Subreddit | Skóre | Komentářů | Čas (Europe/Prague) | Titulek | Odkaz |
|---|---|---:|---:|---|---|---|
| 1wo6o0f | r/LocalLLaMA | 1143 | 238 | 15:54 | Moderátoři: můžeme něco udělat s tím, že se půlka fóra plní reklamními posty o Jevu? | https://www.reddit.com/r/LocalLLaMA/comments/1wo6o0f/mods_can_we_do_something_about_half_the_forum/ |
| 1wo07r8 | r/LocalLLaMA | 271 | 95 | 10:31 | Jev ve 25 řádcích Pythonu | https://www.reddit.com/r/LocalLLaMA/comments/1wo07r8/jev_in_25_lines_of_python/ |
| 1wnyf0o | r/LocalLLM | 54 | 40 | 08:43 | Laya byla první… tak proč všichni pořád mluví jen o Jevu? | https://www.reddit.com/r/LocalLLM/comments/1wnyf0o/laya_came_first_so_why_is_everyone_still_only/ |
| 1wo6x7e | r/LocalLLaMA | 0 | 30 | 16:03 | Proměnil jsem Qwen3.8-27B Q2_64 + llama.cpp v systém podobný Jevu s podporou vidění: 76 % vs. 88 % Jev-1.13 na benchmarku s 22 000 rozhodnutími | https://www.reddit.com/r/LocalLLaMA/comments/1wo6x7e/i_turned_qwen3827b_q2_64_llamacpp_into_a_fully/ |

**1wo6o0f** (r/LocalLLaMA, u/Acrobatic_Stress1388, skóre 1143, 238 komentářů) — žádost moderátorům o zásah proti reklamním postům o Jevu. Nejlépe hodnocený komentář (u/SKX007J1, 405 bodů) je vtip „jmenuji se Jev" (překlad). u/Illustrious_Grade608 (184 bodů) namítá, že většina zmínek řeší replikaci open-source modely, u/johan2114h (155 bodů) přiznává, že pořád neví, kdo Jev je, a u/profcuck (73 bodů) přikládá průzkum posledních deseti postů, které podle něj vesměs popisují volně licencované alternativy.

**1wo07r8** (r/LocalLLaMA, u/johnnyApplePRNG, skóre 271, 95 komentářů) — parodický článek NobodyWho z 22. 9. 2026 od Duarte O.Carma. Načte Qwen3-0.6B-GGUF přes llama-cpp-python, vloží volby Legitimate, Spam a Phishing a z logitů posledního tokenu spočítá pravděpodobnosti 0,031 / 0,084 / 0,885. Ironicky vypočítává, co autoři nedělali (System One decision model, API, syntetická data, RLCD), a odkazuje na otevřené implementace OpenJev.

**1wnyf0o** (r/LocalLLM, u/userwhome, skóre 54, 40 komentářů) — otázka, proč se mluví jen o Jevu, když openweight Laya přišla dřív; autor zmiňuje vzorec, kdy indická práce dostane jen zdvořilé „jo, hustý", zatímco západní produkt zažije hype cyklus. Komentáře staženy nebyly.

**1wo6x7e** (r/LocalLLaMA, u/kyr0x0, skóre 0, 30 komentářů) — představení otevřeného systému Bonsai-Llama-Jev nad Qwen3.8-27B s vlastním benchmarkem, post-hoc kalibrací a rozšířením API System One o vidění. Komentáře nebyly staženy.

## Proč to je důležité

Spor není jen o jednom produktu, ale o tom, jak se v ekosystému lokálních modelů pozná skutečná novost: pokud jsou lepší klasifikátory k dispozici roky, má jejich prezentace jako nové třídy modelů dopad na to, co lidé volí, financují a na čem stavějí. Zároveň se ukazuje, že subreddit plnící se příspěvky, které část členů vnímá jako reklamu, nemá jednoduché vodítko, jak je odlišit od poctivé replikace.

## Zdroje

Podklady:

- `2026-09-23/_data/bundles/1woe70t.md`
- `2026-09-23/_data/extracts/1woe70t.json`
- `2026-09-23/_data/img/1wo6x7e.png`

Odkazy z balíčku:

- https://www.reddit.com/r/LocalLLaMA/comments/1woe70t/jev_isnt_new_tech_its_marketing_targets_people/
- https://www.reddit.com/r/LocalLLaMA/comments/1wo6o0f/mods_can_we_do_something_about_half_the_forum/
- https://www.reddit.com/r/LocalLLaMA/comments/1wo07r8/jev_in_25_lines_of_python/
- https://www.reddit.com/r/LocalLLM/comments/1wnyf0o/laya_came_first_so_why_is_everyone_still_only/
- https://www.reddit.com/r/LocalLLaMA/comments/1wo6x7e/i_turned_qwen3827b_q2_64_llamacpp_into_a_fully/
- https://www.nobodywho.ai/posts/jev-in-25-lines/
- https://i.redd.it/7ezul9h11arh1.png
- https://proceedings.iclr.cc/paper_files/paper/2026/hash/417e1c15b3d49852fceded8aa104107d-Abstract-Conference.html
- https://github.com/ickma2311/jev-baselines-eval
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://aclanthology.org/D19-1404/
- https://huggingface.co/tasks/zero-shot-classification
- https://huggingface.co/docs/inference-providers/tasks/zero-shot-classification
- https://huggingface.co/models?library=gguf
- https://github.com/kyr0/Bonsai-Llama-Jev
- https://github.com/kyr0/typed-decision-bench
- https://kyr0.github.io/typed-decision-bench/
- https://kyr0.github.io/typed-decision-bench/paper/
- https://kyr0.github.io/Bonsai-Llama-Jev/
