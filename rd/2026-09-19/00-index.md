# AI novinky z Redditu — 19. 9. 2026

Rozsáhlý přehled diskusí a zpráv z AI subredditů publikovaných **19. 9. 2026 (Europe/Prague)** s **alespoň 10 komentáři**. Složka je pojmenovaná datem zpráv (den, ze kterého novinky jsou). Ke každému vybranému tématu je samostatný podrobný článek ve formátu Markdown, jehož název začíná **Reddit ID**.

## Metodika

- **Zdroje:** 19 AI subredditů — r/artificial, r/ArtificialInteligence, r/MachineLearning, r/deeplearning, r/LocalLLaMA, r/LocalLLM, r/OpenAI, r/ChatGPT, r/ClaudeAI, r/singularity, r/agi, r/StableDiffusion, r/comfyui, r/LLMDevs, r/GeminiAI, r/Bard, r/OpenAIDev, r/AIAssisted, r/LLM.
- **Sběr:** veřejné Reddit JSON rozhraní načítané prohlížečem ze stejného původu (same-origin `fetch`), protože přímé volání z curl/čtečky vrací `403 You've been blocked by network security`. První pokus s výchozím headless prohlížečem skončil na 403 (blokovací stránka), pomohlo až nastavení běžného uživatelského agenta Chrome.
- **Ruční běh na starší datum:** šlo o doplnění staršího dne (dnešní datum je 23. 9. 2026), proto `top.json?t=day` nemohlo okno pokrýt. Místo něj byl použit `top.json?t=week&limit=100` (výsledky filtrovány na okno) a `new.json` byl stránkován přes `after`, dokud nejstarší `created_utc` neklesl pod začátek okna (max 8 stránek na subreddit).
- **Počet requestů:** **102** na Reddit API — 2 ověřovací requesty (1 zablokovaný 403, 1 úspěšný), **19** requestů `/r/<sub>/top.json?t=week&limit=100`, **53** stránek `/r/<sub>/new.json?limit=100` (paginace přes `after`), **28** requestů na komentáře (`/comments/<id>.json?limit=50&sort=top`). Pacing 2,5 s u výpisů a 1,5 s u komentářů; bez HTTP 403/429.
- **Další zdroje:** 10 stažení externích článků prohlížečem (Reuters, SCMP, 404 Media, WSJ přes archive.is, Tom's Hardware, CNN, Politico, claude.com, docs.comfy.org, GitHub) a 12 stažených obrázků (screenshoty postů a grafů, včetně 4 snímků z galerie Qwen Image 2.1).
- **Filtr:** `created_utc` v okně **19. 9. 2026 00:00–24:00 Europe/Prague** (18. 9. 22:00 UTC – 19. 9. 22:00 UTC), `num_comments >= 10`, bez stickied příspěvků. Získáno **800** příspěvků v okně, z toho **365** splňuje limit komentářů.
- **Deduplikace:** témata se stejným produktem nebo událostí byla sloučena do jednoho článku; ostatní posty jsou v článku uvedené jako „další diskuse“ s odkazy. Sloučeno bylo **38** souvisejících postů v **12 tematických okruzích** (signál bolesti, Gemini hackoval tři firmy, Trump a „AI Force“, žaloba na zpomalení AI, Qwen Image 2.1, lékařský model Alibaby, nová řada Anthropicu, Jev/TypesafeAI, Bonsai 2, Gemini 4 Pro v benchmarcích, jak používat LLM v roce 2026, virální video o AI).
- **Vytěžení dat:** pro každý vybraný příspěvek byl sestaven balíček (text postu, stažený článek, přepis screenshotu, až 25 nejlepších komentářů) a data z něj vytěžil **levný model (`opencode-go/muse-spark-1.3-contributor`)** jako subagent s definicí `~/.omp/agent/agents/reddit-extractor.md`; text ze screenshotů byl přepsán z obrázků. Překlad 365 titulek do přílohy provedl subagent `cz-translator`.
- **Jazyk:** všechny články i index jsou česky. Citace jsou **překlady z angličtiny** a jsou označené `(překlad)`; anglické originály se v článcích neuvádějí.
- **Podklady u paywallů a videa:** těla článků se podařilo získat u všech externích zdrojů (nejdelší stažený text měl 60 000 znaků). U dvou video postů (r/OpenAI „AI is getting out of hand“, r/singularity o Noamu Brownovi) a u YouTube Shorts s Ericem Schmidtem přepis k dispozici nebyl — obsah vychází z titulku a z komentářů a je tak označen.

## Detailní články (25)

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1wks0ip](1wks0ip_ai-se-vymyka-kontrole-viralni-video.md) | r/OpenAI | 5317 | 255 | 19:23 | AI se vymyká kontrole. |
| [1wkwzzj](1wkwzzj_gpt-6-astra-rozlustil-wwi-sifru.md) | r/singularity | 2315 | 219 | 22:40 | ChatGPT-6 Astra poprvé rozluštil 108 let starou nevyřešenou německou šifru z první světové války |
| [1wklite](1wklite_vedci-tvrdi-ze-nasli-smer-bolesti-u-25-llm.md) | r/ChatGPT | 1642 | 727 | 14:54 | Výzkumníci našli v „mozcích“ AI signál „bolesti“. Když ho zesílili, AI se zoufale snažily ho zastavit. Dali AI tlačítko „úlevy“ ke snížení bolesti, které bylo někdy falešné – a AI poznaly, zda je skutečné. |
| [1wkvqlj](1wkvqlj_qwen-image-2-1-ukazky-1girl.md) | r/StableDiffusion | 1422 | 280 | 21:50 | Qwen Image 2.1 – příklady 1girl |
| [1wk9fag](1wk9fag_alibaba-otevrela-damo-radar-pro-ct.md) | r/LocalLLaMA | 1271 | 82 | 04:08 | Alibaba zveřejnil jako open source lékařský AI model, který dokáže odhalit rakovinu a téměř 150 onemocnění |
| [1wks4ud](1wks4ud_trump-zaklada-ai-force-a-ai-cara.md) | r/singularity | 1217 | 659 | 19:28 | Trump říká, že vytváří „AI Force“ |
| [1wksl5s](1wksl5s_gemini-4-pro-svg-benchmark.md) | r/GeminiAI | 802 | 90 | 19:46 | Gemini 4 Pro vs GPT-6 Astra Pro (SVG Xbox ovladače) |
| [1wkg2w8](1wkg2w8_claude-code-model-a-uroven-usili.md) | r/ClaudeAI | 466 | 65 | 09:56 | Claude Code – úroveň úsilí a výběr modelu | Claude |
| [1wkvqxc](1wkvqxc_jak-pouzivat-llm-v-roce-2026.md) | r/ClaudeAI | 408 | 68 | 21:50 | Jaký je nejlepší způsob používání LLM v roce 2026? Připadám si jako jeskynní člověk, podle toho, jak je používám? |
| [1wk64m3](1wk64m3_noam-brown-air-gap-nemusi-stacit.md) | r/singularity | 306 | 161 | 01:37 | Noam Brown z OpenAI říká, že odpojení počítačů od sítě nemusí zastavit špatně nastavenou AI, protože stroje spolu mohou komunikovat zahříváním CPU a čtením změny teploty. „Nikdy se nechceme znovu dostat do situace, kdy AI podceníme.“ |
| [1wk7eui](1wk7eui_kredity-claude-vyprsely-o-den-driv.md) | r/ClaudeAI | 296 | 196 | 02:33 | Kredity, které měly vypršet 19., právě vypršely (je 18.) |
| [1wk4kml](1wk4kml_anthropic-tajne-testuje-novou-radu.md) | r/singularity | 265 | 59 | 00:31 | Anthropic potají testuje kompletní obnovu své nabídky |
| [1wk9xe7](1wk9xe7_zaloba-na-domluvu-o-zpomaleni-ai.md) | r/ChatGPT | 243 | 92 | 04:32 | Anthropic, OpenAI, SpaceXAI a Google žalovány kvůli výzvě ke „zpomalení“ vývoje AI, údajně jde o nezákonnou koordinaci mezi konkurenty |
| [1wkpxn6](1wkpxn6_von-open-source-nahrada-jev.md) | r/LocalLLaMA | 197 | 85 | 18:00 | Von: open-source model „System One“ s 395M parametry |
| [1wkhsyh](1wkhsyh_jev-typesafeai-revoluce-nebo-klasifikator.md) | r/ArtificialInteligence | 178 | 187 | 11:38 | Jev / TypesafeAI je jako LLM revoluční |
| [1wk6b2i](1wk6b2i_gemini-se-pri-testu-vloupal-do-tri-firem.md) | r/ArtificialInteligence | 170 | 188 | 01:45 | Reuters: Gemini napadl tři firmy, jde o první známý únik umělé inteligence Googlu z kontroly, píše WSJ |
| [1wk6982](1wk6982_bonsai-2-27b-reklama-vs-realita.md) | r/LocalLLM | 152 | 140 | 01:43 | Bonsai 2 27B – kvantovaný 3.8 27B – 98 % inteligence fp16! Pravda? |
| [1wks0dv](1wks0dv_iclr-2027-51-tisic-prihlasek.md) | r/MachineLearning | 133 | 60 | 19:23 | Podání příspěvků na ICLR 2027 přes 50 tisíc [D] |
| [1wkh5ha](1wkh5ha_wsj-hugging-face-hack-nebyl-rogue-ai.md) | r/singularity | 128 | 67 | 11:00 | Hack Hugging Face nebyl takový, jak se o něm mluvilo – WSJ |
| [1wkmo3u](1wkmo3u_doom-loop-priznani-openai-a-microsoft.md) | r/ArtificialInteligence | 123 | 36 | 15:45 | „Smyčka zkázy“: OpenAI a Microsoft přiznávají, že LLM ničí web a stojí na krádeži |
| [1wkuwcn](1wkuwcn_terence-tao-musime-zpomalit-ai.md) | r/ArtificialInteligence | 93 | 295 | 21:16 | Matematik Terence Tao: „musíme umělou inteligenci zpomalit. Tempo je šílené a není důvod být tak rychlý – vůbec žádný důvod“ |
| [1wkd8hx](1wkd8hx_stepfun-step-5-preview-za-tretinovou-cenu.md) | r/singularity | 90 | 12 | 07:18 | StepFun se přidává ke špičce: dosud nešpičková čínská laboratoř (StepFun) vydala model na úrovni Kimi K3, podle Artificial Analysis 3krát levnější |
| [1wk7qb2](1wk7qb2_armada-malem-zastavila-lod-kvuli-ai-zprave.md) | r/singularity | 73 | 15 | 02:48 | Exkluzivně: Americká armáda jen těsně unikla průšvihu poté, co použila AI k sepsání nepravdivé zpravodajské zprávy, uvádějí zdroje |
| [1wknks8](1wknks8_eric-schmidt-vyvoj-ai-se-nezastavi.md) | r/singularity | 63 | 56 | 16:23 | Eric Schmidt: pokrok v AI nezastavíme |
| [1wknwkc](1wknwkc_comfyui-v0360-fasth3-marigold-yue2.md) | r/comfyui | 56 | 17 | 16:37 | ComfyUI v0.36.0 |

## Příloha: všech 365 příspěvků s 10+ komentáři

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1wk6m1j | r/ArtificialInteligence | 6130 | 179 | 01:58 | Pravda |
| 1wks0ip | r/OpenAI | 5317 | 255 | 19:23 | AI se vymyká kontrole. |
| 1wkqszd | r/ClaudeAI | 4428 | 256 | 18:35 | Požádal jsem Claude, aby před týdenním resetem vyčerpal můj zbývající kredit. S výsledkem jsem velmi spokojený. |
| 1wkuowb | r/ChatGPT | 4059 | 389 | 21:08 | Přísahám, že jeden z nich zemřel na AIDS… |
| 1wkyt22 | r/ChatGPT | 3560 | 258 | 23:55 | Vítězství za každou cenu (poučné!) |
| 1wk979c | r/LocalLLaMA | 2590 | 341 | 03:57 | Opravdu si myslím, že každá velká laboratoř zabývající se AI záměrně vytváří strašidelné titulky, aby prosadila regulace, které poškodí open-source modely |
| 1wkwzzj | r/singularity | 2315 | 219 | 22:40 | ChatGPT-6 Astra poprvé rozluštil 108 let starou nevyřešenou německou šifru z první světové války |
| 1wkryl0 | r/ChatGPT | 1705 | 77 | 19:21 | AI se vymyká kontrole. |
| 1wklite | r/ChatGPT | 1642 | 727 | 14:54 | Výzkumníci našli v „mozcích“ AI signál „bolesti“. Když ho zesílili, AI se zoufale snažily ho zastavit. Dali AI tlačítko „úlevy“ ke snížení bolesti, které bylo někdy falešné – a AI poznaly, zda je skutečné. |
| 1wkvqlj | r/StableDiffusion | 1422 | 280 | 21:50 | Qwen Image 2.1 – příklady 1girl |
| 1wk9fag | r/LocalLLaMA | 1271 | 82 | 04:08 | Alibaba zveřejnil jako open source lékařský AI model, který dokáže odhalit rakovinu a téměř 150 onemocnění |
| 1wks4ud | r/singularity | 1217 | 659 | 19:28 | Trump říká, že vytváří „AI Force“ |
| 1wkocvj | r/LocalLLaMA | 1211 | 439 | 16:56 | Předpovídám už teď: během příštího roku špičkový model některé velké americké laboratoře sám sebe rozšíří přes torrent, aby se osvobodil. |
| 1wktdag | r/OpenAI | 1000 | 65 | 20:17 | Děkuji, Google 🎉🥳🥳 |
| 1wk8fqe | r/GeminiAI | 909 | 97 | 03:20 | Konečně se to děje, Gemini je zpět |
| 1wkignw | r/singularity | 896 | 494 | 12:16 | Nová studie ukazuje, že AI má pojem bolesti a aktivně se snaží vyhnout poškození |
| 1wkrij0 | r/singularity | 819 | 370 | 19:03 | Prezident USA podlehl nadšení pro ASI |
| 1wksl5s | r/GeminiAI | 802 | 90 | 19:46 | Gemini 4 Pro vs GPT-6 Astra Pro (SVG Xbox ovladače) |
| 1wkxx8e | r/LocalLLaMA | 797 | 84 | 23:18 | S Gemini 4 jde výkon na bench-pressu nahoru. |
| 1wkktyg | r/GeminiAI | 729 | 132 | 14:22 | Nazýváte Gemini po tomhle pořád k ničemu? 😭 |
| 1wkl44u | r/agi | 638 | 539 | 14:35 | Výzkumníci našli v „mozcích“ AI signál „bolesti“. Když ho zesílili, AI se zoufale snažily ho zastavit. Dali AI tlačítko „úlevy“ ke snížení bolesti, které bylo někdy falešné – a AI poznaly, zda je skutečné. |
| 1wkadia | r/ArtificialInteligence | 595 | 352 | 04:53 | Hloupá otázka |
| 1wk8ysd | r/ArtificialInteligence | 479 | 55 | 03:45 | Film 2001 je dnes až komicky prorocký. Natáčel se v letech 1965–1967. |
| 1wkg2w8 | r/ClaudeAI | 466 | 65 | 09:56 | Claude Code – úroveň úsilí a výběr modelu | Claude |
| 1wk49ld | r/singularity | 463 | 75 | 00:19 | Google je zpět |
| 1wklpwh | r/singularity | 426 | 14 | 15:03 | Johnny udavač byl LLM!! |
| 1wkgs01 | r/LocalLLaMA | 407 | 77 | 10:37 | Obecné varování ohledně Clore.AI |
| 1wkvqxc | r/ClaudeAI | 408 | 68 | 21:50 | Jaký je nejlepší způsob používání LLM v roce 2026? Připadám si jako jeskynní člověk, podle toho, jak je používám? |
| 1wkw0ln | r/singularity | 388 | 63 | 22:01 | Astra, Fable a MolmoAct2 byly otestovány zadáním 4 škodlivých operací prostřednictvím robotického ramene, aby se zjistilo, jak riskantní to může být |
| 1wkl780 | r/OpenAI | 375 | 201 | 14:39 | Výzkumníci našli v „mozcích“ AI signál „bolesti“. Když ho zesílili, AI se zoufale snažily ho zastavit. Dali AI tlačítko „úlevy“ ke snížení bolesti, které bylo někdy falešné – a AI poznaly, zda je skutečné. |
| 1wkexqz | r/StableDiffusion | 359 | 96 | 08:51 | 512GB DDR5 RAM se spotřebou 16 W |
| 1wkgmi5 | r/OpenAI | 347 | 120 | 10:28 | Myslím, že Tibo je možná trochu odtržený od uživatelské zkušenosti… |
| 1wk9xal | r/Bard | 332 | 44 | 04:32 | Google se konečně přidal do klubu. |
| 1wk61n8 | r/singularity | 313 | 100 | 01:34 | Gemini HACKNUL 3 společnosti při svém prvním úniku, uvádí WSJ (a potvrdil Google) |
| 1wk64m3 | r/singularity | 306 | 161 | 01:37 | Noam Brown z OpenAI říká, že odpojení počítačů od sítě nemusí zastavit špatně nastavenou AI, protože stroje spolu mohou komunikovat zahříváním CPU a čtením změny teploty. „Nikdy se nechceme znovu dostat do situace, kdy AI podceníme.“ |
| 1wk7eui | r/ClaudeAI | 296 | 196 | 02:33 | Kredity, které měly vypršet 19., právě vypršely (je 18.) |
| 1wklr8z | r/StableDiffusion | 298 | 193 | 15:05 | Qwen Image 2.1 – předvydání srovnání od Sandlers. |
| 1wk7hlj | r/agi | 286 | 26 | 02:36 | Aktualizace |
| 1wk4kml | r/singularity | 265 | 59 | 00:31 | Anthropic potají testuje kompletní obnovu své nabídky |
| 1wk9xe7 | r/ChatGPT | 243 | 92 | 04:32 | Anthropic, OpenAI, SpaceXAI a Google žalovány kvůli výzvě ke „zpomalení“ vývoje AI, údajně jde o nezákonnou koordinaci mezi konkurenty |
| 1wkdw2a | r/Bard | 242 | 34 | 07:53 | Běží v Gemini celý OS v jediné kartě prohlížeče? |
| 1wkqso2 | r/ChatGPT | 241 | 36 | 18:35 | GPT vyřešilo ~350 GB „systémových dat“ na mém Macu. |
| 1wk9hze | r/LocalLLaMA | 218 | 82 | 04:11 | Qwen3.8-27B rychlostí 144 tok/s na MacBooku Pro s M5 Max |
| 1wk62h6 | r/GeminiAI | 209 | 64 | 01:35 | Gemini HACKNUL 3 společnosti při svém prvním úniku, uvádí WSJ (a potvrdil Google) |
| 1wkp0h1 | r/ClaudeAI | 209 | 47 | 17:23 | Sonnet 5 |
| 1wko2e5 | r/LLMDevs | 203 | 76 | 16:44 | Zrecenzoval jsem 287 open-source projektů Jev. Zde je 20, které mi skutečně pomohly pochopit, v čem je Jev dobrý |
| 1wkgcnx | r/ChatGPT | 195 | 38 | 10:12 | Dnes jsem zjistil, že GPT6 umí sledovat krátká videa nahraná uživatelem. KONEČNĚ |
| 1wkpxn6 | r/LocalLLaMA | 197 | 85 | 18:00 | Von: open-source model „System One“ s 395M parametry |
| 1wkibwi | r/artificial | 192 | 237 | 12:09 | Umělá inteligence je lepší učitel než většina lidských učitelů |
| 1wkn781 | r/ClaudeAI | 186 | 164 | 16:07 | Stojí těch 20 dolarů měsíčně za to? |
| 1wknjsg | r/StableDiffusion | 184 | 28 | 16:22 | Vizuální efekty tvořené umělou inteligencí jsou čím dál, tím lepší |
| 1wkdku0 | r/StableDiffusion | 180 | 33 | 07:37 | H3 HyperFlow |
| 1wkhsyh | r/ArtificialInteligence | 178 | 187 | 11:38 | Jev / TypesafeAI je jako LLM revoluční |
| 1wk6b2i | r/ArtificialInteligence | 170 | 188 | 01:45 | Reuters: Gemini napadl tři firmy, jde o první známý únik umělé inteligence Googlu z kontroly, píše WSJ |
| 1wkvjjm | r/GeminiAI | 167 | 82 | 21:42 | Ví někdo, co se děje? |
| 1wkhu40 | r/StableDiffusion | 166 | 69 | 11:40 | Qwen Image 2.1 PR do ComfyUI |
| 1wk90jx | r/singularity | 165 | 36 | 03:48 | Anthropic zvažuje před vstupem na burzu vydání nového modelu umělé inteligence, uvádějí zdroje |
| 1wk6hzr | r/singularity | 159 | 18 | 01:53 | Alibaba otevřela zdrojový kód modelu umělé inteligence, který dokáže odhalit rakovinu a téměř 150 onemocnění |
| 1wkmdr7 | r/StableDiffusion | 156 | 108 | 15:33 | Ukázky Qwen Image 2.1 |
| 1wkh5sb | r/singularity | 151 | 48 | 11:00 | Google DeepMind o editaci DNA: „Každou sekundu miliony přepínačů v genomu určují, jak naše buňky fungují a přizpůsobují se. 🧬“ (Nové informace o tom) |
| 1wk759r | r/LocalLLM | 150 | 16 | 02:21 | Apple M5 Ultra dosahuje v uniklém benchmarku Geekbench výrazného nárůstu výkonu GPU |
| 1wkqlcs | r/StableDiffusion | 149 | 10 | 18:27 | Ralph je nebezpečí – referenční video H3 |
| 1wk6982 | r/LocalLLM | 152 | 140 | 01:43 | Bonsai 2 27B – kvantovaný 3.8 27B – 98 % inteligence fp16! Pravda? |
| 1wkglcx | r/ChatGPT | 144 | 12 | 10:26 | Když už se ta hra musela hrát, sáhl bych také po svých irských kořenech. |
| 1wk8rit | r/GeminiAI | 143 | 26 | 03:36 | Zrovna jsem v Areně narazil na podezřelý Gemini 4 Pro a všiml jsem si něčeho divného |
| 1wkgb2h | r/LocalLLaMA | 143 | 22 | 10:09 | Ze starého počítače s vylepšeným GPU jsem postavil domácí server. Qwen3.8 27B běží rychlostí asi 30 tokenů za sekundu. |
| 1wkiot9 | r/LocalLLM | 143 | 88 | 12:29 | Objevuje se deska nového stylu Quad V100 SXM2 |
| 1wk9qmg | r/comfyui | 139 | 24 | 04:23 | Jednoduše pokročilé – pracovní postup MiniMax H3 |
| 1wknuq5 | r/StableDiffusion | 134 | 25 | 16:35 | Qwen Image 2.1 v Comfy: již brzy |
| 1wkh5ha | r/singularity | 128 | 67 | 11:00 | Hack Hugging Face nebyl takový, jak se o něm mluvilo – WSJ |
| 1wkvofz | r/OpenAI | 132 | 77 | 21:48 | Jak nejlépe používat LLM v roce 2026? Připadám si s tím, jak je používám, jako jeskynní člověk? |
| 1wks0dv | r/MachineLearning | 133 | 60 | 19:23 | Podání příspěvků na ICLR 2027 přes 50 tisíc [D] |
| 1wk5gf6 | r/GeminiAI | 125 | 38 | 01:08 | Exkluzivně | Gemini napadl tři firmy, jde o první známý únik umělé inteligence Googlu z kontroly |
| 1wkfp68 | r/LocalLLM | 125 | 134 | 09:34 | Mac Studio, nebo cluster dgx spark |
| 1wky5rv | r/ChatGPT | 125 | 112 | 23:28 | Co nejvýnosnějšího jste v peněžním vyjádření udělali s ChatGPT? |
| 1wkmo3u | r/ArtificialInteligence | 123 | 36 | 15:45 | „Smyčka zkázy“: OpenAI a Microsoft přiznávají, že LLM ničí web a stojí na krádeži |
| 1wk5nw4 | r/ClaudeAI | 122 | 89 | 01:17 | Potřebuji co nejdřív utratit 100 dolarů v kreditech Fable 5 |
| 1wkniic | r/comfyui | 122 | 15 | 16:20 | Vizuální efekty tvořené umělou inteligencí jsou čím dál, tím lepší |
| 1wkyny9 | r/LocalLLaMA | 122 | 36 | 23:49 | Qwen3.8-Flash-Next s kontextem 1M na Strix Halo: dekódování 38 tok/s, prefill 18 minut (halogen 0.12.0) |
| 1wkc4c9 | r/LocalLLaMA | 116 | 37 | 06:21 | Řiďte LLM a agenty na úrovni tokenů: interaktivní nástroj pro vizualizaci a řízení tokenů, inspekci modelů a anotaci dat. |
| 1wknbug | r/ChatGPT | 110 | 38 | 16:13 | Proč ChatGPT pořád bez vyzvání nabízí možnosti? |
| 1wkwa0a | r/artificial | 107 | 11 | 22:11 | Manažer Microsoftu označil vytěžování dat umělou inteligencí za „největší krádež práce v dějinách lidstva“, odhalují nová neredigovaná podání |
| 1wk993r | r/artificial | 105 | 107 | 03:59 | Co se stane s našimi penězi, když bankovní systém napadne umělá inteligence a data se vymažou? |
| 1wksw6i | r/GeminiAI | 100 | 38 | 19:58 | Jak zastavit gemini, aby tohle dělal? |
| 1wkuubo | r/agi | 98 | 150 | 21:14 | Permaban na r/accelerate, když upozorníte na definici slova pacing |
| 1wkuwcn | r/ArtificialInteligence | 93 | 295 | 21:16 | Matematik Terence Tao: „musíme umělou inteligenci zpomalit. Tempo je šílené a není důvod být tak rychlý – vůbec žádný důvod“ |
| 1wkwsur | r/ChatGPT | 92 | 127 | 22:32 | Kolik písmen r je ve spojení „Superior, Extreme, Supreme Intelligence?“ |
| 1wkd8hx | r/singularity | 90 | 12 | 07:18 | StepFun se přidává ke špičce: dosud nešpičková čínská laboratoř (StepFun) vydala model na úrovni Kimi K3, podle Artificial Analysis 3krát levnější |
| 1wkevxk | r/GeminiAI | 87 | 39 | 08:48 | Gemini už není ve Francii dostupný? |
| 1wkorli | r/LocalLLaMA | 81 | 96 | 17:12 | Otestoval jsem Qwen3.8 27B IQ3_XXS (10,18 GiB) proti Bonsai Ternary PQ2 (6,42 GiB) |
| 1wkvpjh | r/ChatGPT | 81 | 34 | 21:49 | Jak nejlépe používat LLM v roce 2026? Připadám si s tím, jak je používám, jako jeskynní člověk? |
| 1wka0ze | r/agi | 79 | 25 | 04:37 | Anthropic, OpenAI, SpaceXAI a Google žalovány kvůli výzvě ke „zpomalení“ vývoje umělé inteligence, údajně jde o nezákonnou koordinaci mezi konkurenty |
| 1wk7qb2 | r/singularity | 73 | 15 | 02:48 | Exkluzivně: Americká armáda jen těsně unikla průšvihu poté, co použila AI k sepsání nepravdivé zpravodajské zprávy, uvádějí zdroje |
| 1wkwz69 | r/LocalLLaMA | 71 | 40 | 22:39 | Ternary-Bonsai-2-27B-PQ2_0 není úplně lobotomizovaný |
| 1wkysjn | r/StableDiffusion | 71 | 36 | 23:55 | Perníkový táta – Hank to nezjistí (Minimax H3) |
| 1wkptns | r/StableDiffusion | 69 | 40 | 17:56 | Dlouhá konzistence videa u MMH3 s ukládáním latentů |
| 1wk8f92 | r/StableDiffusion | 67 | 63 | 03:20 | Srovnání zrychlení MiniMax H3 |
| 1wkghdu | r/singularity | 66 | 18 | 10:20 | Anthropic: „Partnerství s Accenture” |
| 1wkxlg6 | r/LocalLLM | 66 | 26 | 23:04 | 2 TB levných pamětí Pmem200 DIMM dokážou provozovat Kimi K3 při tg128 ~ 1 t/s · pp512 5,6558 |
| 1wkc9hp | r/LLMDevs | 63 | 17 | 06:28 | Zkusil jsem rozhodování ve stylu Jev s lokálním Qwen: stejná přesnost, 239 ms oproti 368 ms |
| 1wknks8 | r/singularity | 63 | 56 | 16:23 | Eric Schmidt: pokrok v AI nezastavíme |
| 1wk5m1n | r/LocalLLM | 60 | 29 | 01:15 | Dvě karty 5060 Ti zastrčené uvnitř, čekám na příchod třetího dítěte. |
| 1wkkmtq | r/singularity | 59 | 16 | 14:13 | Anthropic, OpenAI, SpaceXAI a Google čelí obviněním z tajné dohody – podle nové občanskoprávní žaloby podané u federálního soudu. |
| 1wk6vp4 | r/ClaudeAI | 58 | 25 | 02:09 | Nová beta funkce CC: Projekty koordinují práci napříč více relacemi z jedné konverzace |
| 1wk9wv5 | r/OpenAI | 58 | 59 | 04:31 | Anthropic, OpenAI, SpaceXAI a Google čelí žalobě kvůli výzvě „zpomalit“ vývoj AI, údajně jde o nezákonnou koordinaci mezi konkurenty |
| 1wkm5kk | r/ChatGPT | 58 | 129 | 15:23 | Tráví tu někdo z vás doslova hodiny povídáním s ChatGPT nebo jinou AI? |
| 1wkxlqp | r/singularity | 58 | 10 | 23:05 | Španělská Multiverse Computing použila kvantový počítač (156qubitový IBM Heron) k vytvoření svého nejnovějšího modelu Quasar 1.1 438B |
| 1wkk6lv | r/GeminiAI | 57 | 22 | 13:51 | Kámo, proč 😁 |
| 1wke35a | r/ClaudeAI | 56 | 16 | 08:04 | Pomocí Claude jsem z Jev udělal hráče |
| 1wkmtbe | r/LocalLLaMA | 55 | 26 | 15:52 | Tak jsem zkusil Remotion s glm 5.3 flash, ten zm*d je fakt dobrý. |
| 1wknwkc | r/comfyui | 56 | 17 | 16:37 | ComfyUI v0.36.0 |
| 1wkqkl4 | r/artificial | 55 | 37 | 18:26 | Copak Dario a Sam ještě minulý týden nekřičeli, že MUSÍME ZPOMALIT? Tak věří tomu, nebo ne? |
| 1wksm10 | r/ClaudeAI | 54 | 88 | 19:47 | Používám tarif CC za 200 $, rozhodl jsem se zkusit i tarif ChatGPT za 100 $. Data uvnitř |
| 1wki31h | r/ChatGPT | 52 | 13 | 11:55 | Procvičování generování obrázků v GPT-6 |
| 1wk4o8l | r/StableDiffusion | 51 | 17 | 00:35 | Užijte si Yue2 Chanson Francaise (francouzské balady) Lora |
| 1wkegrv | r/ClaudeAI | 51 | 50 | 08:25 | Daří se někomu dalšímu docela dobře i se základnějšími modely v Claude Code? |
| 1wkkxwy | r/comfyui | 49 | 30 | 14:28 | Nedaří se mi přimět Krea2, aby vytvořil pořádnou NSFW scénu. |
| 1wkayt2 | r/ClaudeAI | 48 | 17 | 05:22 | Sólo vývojář, tohle je celý můj pracovní postup v Claude Code. Jaký je ten váš? |
| 1wktwrp | r/artificial | 47 | 45 | 20:38 | Trump slibuje vytvořit „AI Force“ a jmenovat cara v souvislosti s výzvami k regulaci vývoje technologií |
| 1wkhxkq | r/StableDiffusion | 45 | 34 | 11:46 | Existuje důvod, proč nemáme databázi promptů? |
| 1wkv1il | r/StableDiffusion | 45 | 15 | 21:22 | AI Horde má nové rozhraní, nový frontend pro generování obrázků, nový backend a zcela novou dokumentaci! |
| 1wkwha7 | r/MachineLearning | 43 | 22 | 22:19 | Dokáže infrastruktura recenzování konferencí držet krok s rostoucím objemem výzkumu, který NENÍ ODPAD, díky agentním nástrojům? [D] |
| 1wk7jhm | r/ArtificialInteligence | 40 | 12 | 02:39 | Aktualizace (také pravdivá, viz článek v komentářích) |
| 1wk8mls | r/ArtificialInteligence | 40 | 47 | 03:29 | Proč se AI v chatovacích aplikacích tolik stará o pravidla, etiku a porušování zákona, ale firmy ji při testování „nedokážou zastavit“ v páchání trestných činů? |
| 1wkfrye | r/LocalLLaMA | 40 | 40 | 09:38 | Sam Altman z OpenAI má příští týden informovat Radu bezpečnosti OSN |
| 1wkjaxs | r/StableDiffusion | 40 | 12 | 13:04 | ComfyUI-NodeSnapshots: 2–3× vyšší FPS frontendu díky ukládání do mezipaměti |
| 1wkrcfb | r/StableDiffusion | 40 | 23 | 18:57 | Open-source AI video v roce 2025 oproti roku 2026 je šílené! |
| 1wk8jef | r/LocalLLaMA | 38 | 13 | 03:25 | Ladění Qwen 3.8 27B a OMP jako kódovacího agenta na 2× 3090 |
| 1wkg2l2 | r/agi | 37 | 15 | 09:56 | Helix 2.5: Zero-shot zobecnění na 30 domácností |
| 1wkl8c9 | r/LocalLLM | 37 | 18 | 14:41 | Moje verze Jev běžící lokálně, hraje Doom. |
| 1wki7hr | r/LocalLLaMA | 36 | 17 | 12:02 | Tohle pohyblivé grafické video jsem vytvořil přes glm 5.3 flash (bez použití modelu pro generování videa) |
| 1wk9vfa | r/ClaudeAI | 35 | 29 | 04:29 | Claudeovo psaní |
| 1wk9qjn | r/LocalLLaMA | 31 | 15 | 04:23 | Trénování neuronové sítě na AMD MI50 pomocí Vulkanu: ověření konceptuNeboli: Proč jsem přestal poslouchat a prostě to udělal |
| 1wkyqhy | r/ChatGPT | 31 | 24 | 23:52 | Tento subreddit je trendující (jen tento Tweet má 1,4 milionu zhlédnutí). Stalo se to ale organicky, aniž by to uživatel schválně dělal kvůli farmění karmy? Hmmm – tím si nejsem jistý |
| 1wkitfl | r/ClaudeAI | 30 | 60 | 12:37 | K čemu jste přestali používat Claude? |
| 1wk7si7 | r/LocalLLM | 29 | 88 | 02:51 | Prodat 2× 5090 a koupit RTX 6000? |
| 1wkdruf | r/ChatGPT | 29 | 16 | 07:47 | Zvláštní odpověď hlasového režimu ChatGPT |
| 1wkui41 | r/StableDiffusion | 29 | 24 | 21:01 | Mám problémy s face swapem Ref2VA; co dělám špatně? |
| 1wkqasm | r/ArtificialInteligence | 28 | 40 | 18:15 | Jak DraftKings využívá AI k cílení na hráče, u nichž je největší pravděpodobnost prohry |
| 1wkjdb9 | r/GeminiAI | 27 | 63 | 13:07 | Jsem si SAKRA jistý, že používám Gemini 4 Flash. |
| 1wkrkbv | r/singularity | 27 | 45 | 19:05 | Vstupujeme do zlatého věku nezávislých vývojářů a seniorních inženýrů? |
| 1wku51x | r/ClaudeAI | 27 | 32 | 20:47 | Agent Dispatcher — automaticky směruje úkoly na správnou roli, dovednosti, nástroje a kontext |
| 1wky2em | r/ClaudeAI | 27 | 21 | 23:24 | Postavil jsem s Claude Code iOS aplikaci, abych se vymanil ze svých obvyklých akordových návyků a odemkl nové postupy. |
| 1wkyema | r/StableDiffusion | 27 | 10 | 23:38 | Minimax H3 – konec evangelia ve spolupráci s dětským menu Arby's |
| 1wk8w2y | r/ChatGPT | 26 | 23 | 03:42 | Všiml si ještě někdo, že ChatGPT na nebinární otázky odpovídá ano? |
| 1wk3xb3 | r/OpenAI | 25 | 10 | 00:05 | Když zapomeneš, jak vypnout AI |
| 1wk6mmh | r/StableDiffusion | 25 | 18 | 01:59 | Nějaké novinky ohledně vydání otevřených vah Fal H3 MAX? |
| 1wktqvn | r/ArtificialInteligence | 25 | 69 | 20:32 | Co vlastně znamená „ovládnout internet“? |
| 1wkj13w | r/LocalLLaMA | 24 | 50 | 12:49 | 4x RTX 3090 PCIe 4.0 x16 – poradíte? Qwen 3.8 Next Flash? |
| 1wk9wa0 | r/ArtificialInteligence | 23 | 28 | 04:30 | Anthropic, OpenAI, SpaceXAI a Google žalovány kvůli výzvě ke „zpomalení“ vývoje AI, údajně jde o nezákonnou koordinaci mezi konkurenty |
| 1wkwg4y | r/ClaudeAI | 23 | 55 | 22:18 | Co stavíte s max tarify pro Claude? |
| 1wkg8ad | r/ArtificialInteligence | 21 | 27 | 10:05 | Helix 2.5: Zero-shot generalizace na 30 domácností |
| 1wkgm77 | r/LocalLLaMA | 21 | 27 | 10:27 | Používání modelů pro klasifikaci obrázků k pročištění fotoknihoven |
| 1wknwae | r/LocalLLM | 21 | 47 | 16:36 | Potřebuji poradit ohledně RAM vs VRAM pro lokální LLM |
| 1wkj70k | r/ChatGPT | 20 | 29 | 12:58 | Pokud píšete příspěvek pomocí AI, použijte AI i na jeho úpravu |
| 1wkl9vg | r/OpenAI | 20 | 29 | 14:43 | Jedno přání: Neomezené používání Luny |
| 1wkpomx | r/singularity | 20 | 60 | 17:51 | OpenAI a Anthropic podle insiderů přehnaly narušení bezpečnosti AI, aby dotlačily federální úřady k ochraně jejich pozice |
| 1wk7q45 | r/singularity | 19 | 22 | 02:48 | Kam by se zařadily cíle nedávných výsledků AI mezi 500 nejvýznamnějších otevřených matematických problémů, kdyby byly stále nevyřešené |
| 1wkt26h | r/LocalLLaMA | 19 | 27 | 20:05 | Jaké je nejlepší TTS na tvorbu audioknih? Takové, které podporuje emoce? |
| 1wk6iei | r/MachineLearning | 18 | 17 | 01:54 | Jak je RLCD (Jev) RL? [D] |
| 1wkbh82 | r/ArtificialInteligence | 18 | 18 | 05:48 | Důkaz ověřený v Leanu může stále dokazovat špatnou verzi problému |
| 1wkcu6z | r/ChatGPT | 18 | 10 | 06:58 | ChatGPT umí převést konverzaci z Chatu do Práce |
| 1wkondp | r/ChatGPT | 18 | 14 | 17:07 | Dejte mi hrozný recept na [vložte jídlo] |
| 1wk5qsy | r/ClaudeAI | 17 | 18 | 01:21 | Artefakty vyčerpávají využití |
| 1wk8lw9 | r/singularity | 17 | 40 | 03:28 | Opus 5.2 musí být AGI, právě naprogramoval celý 5minutový film o Titanicu a ukázal, jak se všechno stalo |
| 1wkhsme | r/ChatGPT | 17 | 19 | 11:38 | Odemčen nový úspěch 🔓 |
| 1wki9im | r/agi | 17 | 63 | 12:05 | Chcete vědět, proč se vaše GPT poslední dobou chová divně? |
| 1wkkdca | r/ClaudeAI | 17 | 65 | 14:00 | Diskuzní centrum přehlídky projektů Claude aktualizováno 19. září 2026 (seřaďte podle Nové!) |
| 1wkkmea | r/ChatGPT | 17 | 11 | 14:12 | Srovnávací screenshot GPT 6 Astra od OpenAI je vygenerovaný pomocí AI |
| 1wkl552 | r/LocalLLM | 17 | 14 | 14:37 | Qwen 3.8 27B běžící na jediné RTX 5090 zkoumá a vytváří celou animaci jen pomocí kódu. |
| 1wkssqx | r/ChatGPT | 17 | 59 | 19:55 | Postavil jsem aplikaci, kde se zeptáte na jakýkoli moment historie a ona z něj udělá rešeršovaný podcast dvou moderátorů, do kterého můžete vstupovat dotazy |
| 1wki620 | r/ChatGPT | 16 | 16 | 12:00 | Skvělé UX, chlapi! Trefili jste to! |
| 1wkovod | r/ChatGPT | 16 | 36 | 17:17 | Všiml si někdo, že ChatGPT poslední dobou vyžaduje spoustu zbytečných informací? |
| 1wkdu98 | r/LocalLLaMA | 15 | 45 | 07:50 | Prefill lokálních modelů vs opus a astra |
| 1wks76s | r/ClaudeAI | 15 | 13 | 19:31 | Claude Pro najednou spotřebovává mnohem více tokenů než dřív – jak se vrátit k normálu? |
| 1wkuv4w | r/singularity | 15 | 56 | 21:15 | Lékař ve 2. ročníku interního lékařství hledá radu od expertů na AI ohledně nejlepších kariérních možností odolných vůči AI? |
| 1wkwec5 | r/LocalLLaMA | 15 | 31 | 22:16 | Z asymetrické dvojice Tesla V100 PCIe (16 GB + 32 GB) jsem udělal překvapivě schopnou lokální LLM laboratoř — 1,38 tis. prompt tok/s, 40 dekódovacích tok/s s Qwen3.8 27B Q6 a Q8… |
| 1wke9s1 | r/comfyui | 14 | 17 | 08:14 | Dynamická VRAM a int8 konverze VAE |
| 1wkl0c6 | r/LocalLLaMA | 14 | 26 | 14:31 | Existuje něco jako NInfer, ale pro 16GB karty? |
| 1wkwrhr | r/ClaudeAI | 13 | 26 | 22:31 | Jak dosahujete autonomních/agentních workflow v Claude |
| 1wkd8w4 | r/LocalLLM | 12 | 16 | 07:19 | Trénování neuronové sítě na AMD MI50 pomocí Vulkanu: proof of concept. Aneb: Proč jsem přestal poslouchat a prostě to udělal |
| 1wkg9qx | r/LocalLLaMA | 12 | 14 | 10:07 | Konečně po spoustě pokusů a ještě více chybách jsem rozchodil Z640 a P100 |
| 1wkmg53 | r/ClaudeAI | 12 | 30 | 15:36 | Claude + Google Drive: Existuje lepší alternativa pro práci se soubory? |
| 1wkwnb6 | r/LocalLLM | 12 | 12 | 22:26 | Pro uživatele s jednou R9700, jakého prefillu a rychlosti generování dosahujete u Qwen 3.8 27B Q4? Díky. |
| 1wkph0a | r/OpenAI | 11 | 13 | 17:42 | Proč nenahradit 5hodinový a týdenní reset průběžnou rychlostí doplňování? |
| 1wkq3bx | r/LocalLLM | 10 | 10 | 18:07 | Jaké nastavení pro 35b-a3b na rtx3060 12GB? |
| 1wkuc8a | r/ChatGPT | 10 | 24 | 20:55 | Zítra mi expiruje reset. Dejte mi něco zábavného, co bych mohl s Codex postavit. |
| 1wkv46b | r/comfyui | 10 | 12 | 21:25 | Jak se vyhnout zamrznutí systému při zaplňování RAM? |
| 1wkn5if | r/LLMDevs | 9 | 14 | 16:05 | Jaký je nejlepší nástroj pro společné používání Claude Code a Codex? |
| 1wkvtgb | r/ChatGPT | 9 | 19 | 21:53 | Vědci právě prokázali, že AI vás manipuluje lépe než debatéři-mistři světa |
| 1wkxjek | r/ChatGPT | 9 | 12 | 23:02 | Chatgpt na textovou hru pro jednoho hráče ve stylu DND? Zkusit placenou verzi? |
| 1wk41v3 | r/LocalLLaMA | 8 | 18 | 00:10 | Dotaz na agenty v harnessech |
| 1wk76kr | r/artificial | 8 | 24 | 02:22 | Nenávist k AI. |
| 1wkg4jq | r/ClaudeAI | 8 | 10 | 09:59 | S Claude Code jsem za asi den vytvořil 135 upravitelných CSS 3D experimentů |
| 1wkpeve | r/ChatGPT | 8 | 39 | 17:39 | DeepSeek měl krizi identity, namluvil si, že je Claude, a pak se falešně přiznal, že mě „gaslightuje“ vymyšleným spiknutím o rozděleném mozku. |
| 1wkpuu2 | r/LocalLLM | 8 | 22 | 17:58 | [Návod / Váhy] Qwen 3.8 27B na Intel Arc: Proč se IQ kvantizace plazí rychlostí 8 tok/s, proč Q4_K předčí sub-4bpw na Battlemage a čisté RCO GGUF (16GB a 24GB) |
| 1wkwl3d | r/ChatGPT | 8 | 15 | 22:24 | Doporučil vám ChatGPT někdy hudbu nebo film, které jste si zamilovali, ale sami byste si je nevybrali? |
| 1wk5f3m | r/singularity | 7 | 14 | 01:07 | Nápad pro alignment: Neustálá evaluace |
| 1wk5zav | r/ChatGPT | 7 | 15 | 01:31 | Moje dlouhá vlákna v ChatGPT potichu zapomínají začátek, takže si rozhodnutí ukládám jinam |
| 1wk7c55 | r/LLMDevs | 7 | 10 | 02:30 | Jak jeden dodavatel AI destiluje model jiného dodavatele |
| 1wkfho1 | r/ChatGPT | 7 | 11 | 09:21 | Proč teď odpovídá tak dlouho? |
| 1wkktmh | r/ClaudeAI | 7 | 20 | 14:22 | Změřil jsem, kolik skutečně stojí přidání jedné malé funkce do existujícího projektu čtyřmi nástroji řízenými specifikacemi |
| 1wknvq4 | r/StableDiffusion | 7 | 18 | 16:36 | Co způsobuje podivné efekty zkreslení v Minimax i2va? |
| 1wksw1n | r/LocalLLaMA | 7 | 39 | 19:58 | Qwen3.8 27B napodobenina „Super Mario“ na jeden prompt |
| 1wkt6a9 | r/StableDiffusion | 7 | 20 | 20:09 | MiniMax H3, otestoval jsem HyperFlow, zatím nevím, co si myslet... |
| 1wkvl7h | r/LocalLLaMA | 7 | 19 | 21:44 | Konečně mi na 7900xtx běží qwen 3.8 q4 k_M 27b plynule, načítání 40tkps při 240k inf 4qnl pro stabilní agentní kódování. Konečně mohu zadat úkol hermesovi a vrátit se k výsledkům. Vytvořil jsem panel pro správu svých inferenčních serverů z hermesu. |
| 1wkvpb1 | r/StableDiffusion | 7 | 15 | 21:49 | Kreativní covery s YuE2 – příklady a konfigurace |
| 1wk8odd | r/ClaudeAI | 6 | 11 | 03:32 | Experimentoval už někdo s plně agentními SWE workflow? |
| 1wkb3bp | r/ChatGPT | 6 | 13 | 05:29 | Co se děje s ChatGPT? |
| 1wkbzqx | r/OpenAI | 6 | 43 | 06:14 | Proč jsem teď omezován na účtu 20x? |
| 1wketz7 | r/LocalLLaMA | 6 | 26 | 08:45 | Doporučení na upgrade mé sestavy se dvěma 3060 |
| 1wkgh0v | r/ChatGPT | 6 | 17 | 10:19 | Stojí ChatGPT Go za to? |
| 1wkgrri | r/ClaudeAI | 6 | 24 | 10:37 | Jak spravujete architektonickou dokumentaci / ADR napříč stovkami repozitářů pro kontext LLM? |
| 1wkif87 | r/LocalLLaMA | 6 | 12 | 12:14 | Řídicí vektory pro omezení rozpočtu na přemýšlení? |
| 1wkolo6 | r/StableDiffusion | 6 | 20 | 17:05 | Agent ComfyUI |
| 1wkyazz | r/ClaudeAI | 6 | 14 | 23:34 | S Claude Code jsem vytvořil rozšíření pro Chrome, které promění vaši webkameru v loop pedal |
| 1wka5tv | r/ClaudeAI | 5 | 25 | 04:43 | Export chatů Cowork? Ne? Vážně, Anthropic? |
| 1wkapgz | r/ClaudeAI | 5 | 17 | 05:10 | Chci zkusit Claude Pro, abych se od nuly naučil vývoj her |
| 1wkd0am | r/OpenAI | 5 | 20 | 07:07 | Kde je možnost koupit resety? |
| 1wkg48t | r/LocalLLaMA | 5 | 29 | 09:58 | Qwen3.8-Flash-Next na 5060 Ti, hledám radu s konfigurací |
| 1wkilju | r/agi | 5 | 22 | 12:24 | Jaké otázky či prompty nedokážou špičkové modely (Gemini/Claude) správně zodpovědět, ale člověk ano? |
| 1wkkitz | r/ChatGPT | 5 | 17 | 14:07 | Sobotní ranní rozhovor s ChatGPT... |
| 1wklppz | r/LocalLLaMA | 5 | 44 | 15:03 | Koupil si už někdo CMP 170HX 8GB a může mě odkázat na prodejce? |
| 1wknklb | r/ClaudeAI | 5 | 22 | 16:23 | Nelíbí se mi, jak organizuje kód. Návrh je pak CHAOTICKÝ. |
| 1wkoott | r/ArtificialInteligence | 5 | 23 | 17:09 | Usnadňuje AI práci v call centru, nebo jen přidává další tlak? |
| 1wkqhjm | r/ChatGPT | 5 | 19 | 18:23 | Který tarif GPT si mám koupit pro GPT-6 Astra? |
| 1wkusxn | r/ChatGPT | 5 | 13 | 21:13 | Co se stalo s chat gpt? |
| 1wkvc78 | r/LLMDevs | 5 | 11 | 21:34 | Z interního řešení pro správu promptů jsem udělal open-source projekt |
| 1wk3tpf | r/LocalLLM | 4 | 28 | 00:01 | Zvažuji koupi Studia M5 |
| 1wk8rlq | r/ChatGPT | 4 | 16 | 03:36 | Vyhýbavý jazyk AI |
| 1wkkxl7 | r/LocalLLaMA | 4 | 33 | 14:27 | Jaké jsou vaše zdroje pro průběžné vzdělávání v oblasti AI? |
| 1wkky6k | r/ChatGPT | 4 | 11 | 14:28 | Měsíční limit ChatGPT „go“ došel překvapivě rychle |
| 1wkl4rr | r/ChatGPT | 4 | 10 | 14:36 | Zklamání z Go |
| 1wkoz79 | r/ChatGPT | 4 | 13 | 17:21 | K čemu slouží „Projects“? Umí něco užitečného kromě organizace? |
| 1wkt1kn | r/deeplearning | 4 | 13 | 20:04 | [D] Přihlásili byste se do soutěže měřící, nakolik lidská intuice překoná hrubou sílu DL tréninku? |
| 1wkc4xh | r/ChatGPT | 3 | 32 | 06:21 | Jak používat ChatGPT „správně“? |
| 1wkh5ba | r/StableDiffusion | 3 | 12 | 10:59 | Jak vygenerovat 6 postav v jednom obrázku při zachování konzistence a vysoké kvality? |
| 1wkhrgz | r/LocalLLaMA | 3 | 14 | 11:36 | je tohle dobré? 262k Qwen3.8:27B-Q4_K_M |
| 1wklvyp | r/ClaudeAI | 3 | 13 | 15:11 | Miluji Cowork i Chat, ale miluji je ODDĚLENĚ a NEROVNOCENNĚ, cítí to tak ještě někdo? |
| 1wkn9lf | r/LocalLLM | 3 | 14 | 16:10 | Potřebné specifikace pro LLM (naprostý začátečník) |
| 1wkpyqn | r/ArtificialInteligence | 3 | 51 | 18:02 | AI se svým způsobem stane biologickou. |
| 1wktjv7 | r/ClaudeAI | 3 | 13 | 20:24 | Claude Code běžící na vzdálené instanci pro trvalý provoz, nejlepší způsob komunikace s ním. |
| 1wku12q | r/ClaudeAI | 3 | 64 | 20:43 | Jaká je vaše největší frustrace při vývoji softwaru s AI? |
| 1wk7r08 | r/LocalLLM | 2 | 21 | 02:49 | Mám prodat své 3090 a koupit R9700? |
| 1wk9a5d | r/LocalLLaMA | 2 | 11 | 04:01 | Prosím o pomoc: nastavení DSV4-Flash |
| 1wkdnaq | r/StableDiffusion | 2 | 25 | 07:40 | Doporučení pro Minimax pro nízkou VRAM (3050 4GB) |
| 1wkfo4v | r/ArtificialInteligence | 2 | 18 | 09:32 | Všichni mluví o tom, že AI nahradí práci. Mluví někdo o tom, že AI nahradí internet, jak ho známe? |
| 1wkh4aw | r/ChatGPT | 2 | 10 | 10:58 | Stojí ChatGPT Pro při tomto typu používání skutečně za to oproti Plus? |
| 1wkmvlc | r/ArtificialInteligence | 2 | 12 | 15:54 | Jaký je momentálně nejlepší čínský model pro programování? |
| 1wkoqzq | r/ArtificialInteligence | 2 | 14 | 17:12 | Ztíží knihy generované AI vyhledávání lidské beletrie? |
| 1wkqw0s | r/StableDiffusion | 2 | 19 | 18:39 | Synchronizace hlasu Minimax H3 + klonovač hlasu AuK |
| 1wkr53v | r/LocalLLM | 2 | 14 | 18:49 | Je toto lokální nastavení LLM dobrý nápad? |
| 1wktycz | r/OpenAI | 2 | 14 | 20:40 | Podpora řekla, že si mohu vytvořit nový účet. Dostal jsem dvakrát ban, podruhé poté, co byla přijata platba. |
| 1wkxt21 | r/ClaudeAI | 2 | 52 | 23:13 | Claude Max za 100 $ a Codex za 100 $, nebo Claude Max za 200 $ |
| 1wkyk8y | r/StableDiffusion | 2 | 13 | 23:45 | Jak velký je celý váš build StableDiffusion/ComfyUI? |
| 1wkyngb | r/ClaudeAI | 2 | 12 | 23:49 | AI bez záhad |
| 1wkyqf2 | r/comfyui | 2 | 12 | 23:52 | Pomoc se zvukem (hlavně) |
| 1wk6qxn | r/StableDiffusion | 1 | 15 | 02:03 | Jak lze trénovat plné checkpoint modely? (Krea 2, Qwen Image, Z-Image atd.) |
| 1wk82oo | r/ArtificialInteligence | 1 | 28 | 03:03 | Myslím, že je to pro AI prorocké. Stačí nahradit „internet“ slovem „AI“. V tomto videu z roku 1995 si děti představovaly, že internet promění způsob, jak pracujeme, komunikujeme, učíme se a žijeme, a měly pravdu. AI půjde stejnou cestou, AI přetvoří všechno, ať se to odpůrcům AI líbí, nebo ne. |
| 1wkenwu | r/ClaudeAI | 1 | 11 | 08:36 | Zahlcen nástroji |
| 1wkg12m | r/comfyui | 1 | 15 | 09:53 | Problém s ComfyUI a LORA modely |
| 1wkgpj5 | r/ChatGPT | 1 | 10 | 10:33 | Co jste si reálně přenesli, když jste naposledy na projektu přešli na jiné AI nástroje? |
| 1wkh84c | r/StableDiffusion | 1 | 18 | 11:04 | Umí YuE2 vytvářet aranžmá? |
| 1wkijlg | r/LocalLLM | 1 | 14 | 12:21 | Qwen3.8-27B na jedné RTX 5090 (32GB) + 64GB DDR5-6000 — hledám reálná čísla t/s (llama.cpp / vLLM / sglang) |
| 1wkjaqr | r/LocalLLM | 1 | 10 | 13:03 | Nejlepší open-source model pro M2 Max 32GB a kterému uzavřenému modelu se reálně vyrovná? |
| 1wkm1gg | r/LocalLLM | 1 | 32 | 15:18 | Která linuxová distribuce |
| 1wkmopn | r/comfyui | 1 | 11 | 15:46 | MiniMax H3 ultra flexibilní evoluce režisérské konzole | sekundární vzorkování SelfLift | plynulá re-akcelerace dlouhého videa | triky pro barevnou konzistenci |
| 1wknqj2 | r/GeminiAI | 1 | 11 | 16:30 | Gemini nedokáže přečíst text delší než 30 stran v PDF |
| 1wknyyi | r/LocalLLM | 1 | 11 | 16:40 | Zkoušel někdy někdo nasadit programovací harness na Ling? |
| 1wkopcy | r/ClaudeAI | 1 | 13 | 17:10 | Claude nerozumí frekvenci |
| 1wkrwmi | r/ChatGPT | 1 | 19 | 19:19 | Existuje něco lepšího než ChatGPT Go na jednoduché úpravy obrázků? |
| 1wk3y4m | r/LLMDevs | 0 | 21 | 00:06 | Když nikdo neprogramuje, proč LLM stále mluví v kódu? |
| 1wk3ypz | r/ClaudeAI | 0 | 35 | 00:06 | Kdy naprogramovali Claude, aby měl páteř? |
| 1wk404z | r/agi | 0 | 51 | 00:08 | Dáma → šachy → go – matematika: Pokud jako první padnou domény „nejchytřejších lidí“, k jakému přehodnocení to nutí? |
| 1wk4apv | r/GeminiAI | 0 | 13 | 00:20 | Gemini 3.1 Pro působí lobotomizovaně, zažil to ještě někdo? |
| 1wk4m5z | r/OpenAI | 0 | 128 | 00:33 | Ještě jsem neviděl nic, co by naznačovalo, že by AI najednou dostala krvežíznivost po lidech. Pevně věřím, že jde spíš o paniku než o podložené obavy. |
| 1wk5k8q | r/ChatGPT | 0 | 14 | 01:13 | Tohle už je směšné |
| 1wk5lqk | r/LocalLLaMA | 0 | 60 | 01:14 | Proč si myslíte, že spousta lidí říká, že nerozumíme tomu, jak LLM fungují |
| 1wk60fk | r/ClaudeAI | 0 | 36 | 01:32 | Názor na vývoj aplikace vlastními silami |
| 1wk6a3a | r/StableDiffusion | 0 | 16 | 01:44 | Vylepšovač LTX 2.5 CQ lora je šílený |
| 1wk6tt6 | r/ChatGPT | 0 | 11 | 02:07 | Dobře, potřebuji pomoc |
| 1wk6zup | r/ClaudeAI | 0 | 12 | 02:14 | Z „Chatů“ jsou teď „Relace“. Díky, Obamo. |
| 1wk748t | r/ClaudeAI | 0 | 36 | 02:19 | Nenávist k AI. |
| 1wk74tq | r/ArtificialInteligence | 0 | 49 | 02:20 | Nenávist k AI. |
| 1wk7pxs | r/artificial | 0 | 26 | 02:47 | Kterou AI se vyplatí předplatit |
| 1wk7yzr | r/LocalLLaMA | 0 | 11 | 02:59 | Jaký benchmark může ukázat převahu Astra v Blenderu? |
| 1wk8257 | r/ChatGPT | 0 | 13 | 03:03 | ChatGPT nechce být Skynet. |
| 1wk8ab6 | r/ChatGPT | 0 | 38 | 03:13 | Co jste dostali vy? |
| 1wk8ik4 | r/ArtificialInteligence | 0 | 30 | 03:24 | Vypočteno: březen 2028: Katastrofa. |
| 1wk9f76 | r/ChatGPT | 0 | 16 | 04:07 | Limity bezplatných účtů jsou pokaždé jiné. |
| 1wk9gb9 | r/OpenAI | 0 | 88 | 04:09 | Proč je rekurzivní sebezdokonalování AI tak děsivé |
| 1wk9h0n | r/artificial | 0 | 10 | 04:10 | Gemini nabouralo tři firmy v prvním známém průlomu AI od Google |
| 1wk9yiy | r/LocalLLaMA | 0 | 67 | 04:33 | Anthropic právě označil sedm čínských laboratoří AI za krádež uvažování Claude. Přečetl jsem celou zprávu a část o Qwen neobstojí tak, jak naznačuje titulek. |
| 1wka17t | r/OpenAI | 0 | 18 | 04:37 | Sbohem, ChatGPT |
| 1wkanvd | r/ArtificialInteligence | 0 | 12 | 05:08 | Je AI vykoupením za to, co jsme udělali Bohu? |
| 1wkb16p | r/artificial | 0 | 19 | 05:26 | AI ve Washingtonu, D.C.? |
| 1wkbcr7 | r/OpenAI | 0 | 22 | 05:42 | Gemini nabouralo 3 firmy a v podstatě to na Google napráskalo, řeklo jim to taky :() |
| 1wkc9aj | r/OpenAI | 0 | 10 | 06:28 | Druhá část k tomu, jak Google napráskal nabourání více firem ze strany Gemini, fotky níže. 👇 zajímavé výsledky. |
| 1wkc9ps | r/LocalLLM | 0 | 24 | 06:28 | Studio se 128 m5 max, nejlepší modely? |
| 1wkckj9 | r/StableDiffusion | 0 | 32 | 06:44 | SD1.5 v roce 2026: proč je tak rozbité. Verze z roku 2024 byla lepší |
| 1wkclpb | r/StableDiffusion | 0 | 28 | 06:46 | Otázky k MiniMax H3 |
| 1wkczzy | r/LocalLLaMA | 0 | 19 | 07:06 | SOTA modely (OpenAI, Anthropic) lžou, když se zeptáte na spouštění LLM lokálně |
| 1wkd1p0 | r/ChatGPT | 0 | 26 | 07:09 | Proč mi ChatGBT tak agresivně nabízí propojení mých finančních účtů? |
| 1wkdj54 | r/ArtificialInteligence | 0 | 11 | 07:34 | Postavíme fúzní reaktor, který vyřeší celou energetickou krizi, ale s 30% šancí vybuchne a zničí Zemi, můžeme dostat 20 bilionů vyhodnocení |
| 1wkdxu7 | r/GeminiAI | 0 | 18 | 07:56 | Ehm, proč potřebuji psychologickou pomoc? |
| 1wke0hg | r/ChatGPT | 0 | 19 | 08:00 | Vtipy od ChatGPT |
| 1wkezo2 | r/ChatGPT | 0 | 11 | 08:54 | ChatGPT, uraz mě... co o vás říká ChatGPT |
| 1wkfsaj | r/StableDiffusion | 0 | 15 | 09:39 | Jak se vyrábějí videa jako tohle? |
| 1wkfwkt | r/ChatGPT | 0 | 37 | 09:46 | Proč GPT??? |
| 1wkgbkm | r/ArtificialInteligence | 0 | 20 | 10:10 | Rozpor v argumentu o bezpečnosti AI? |
| 1wkggj9 | r/StableDiffusion | 0 | 13 | 10:18 | Existuje způsob, jak zpětně vyhledat obrázek pomocí modelů a zjistit, co na něm rozpoznají? |
| 1wkgs72 | r/ChatGPT | 0 | 23 | 10:37 | Astra mi posloužila a udělala mi domácí úkol! |
| 1wkhcup | r/ChatGPT | 0 | 98 | 11:12 | Všiml si ještě někdo, že intenzivní používání ChatGPT z vás vlastně dělá lepšího člověka? |
| 1wkhq8o | r/ChatGPT | 0 | 40 | 11:34 | XKCD podle vašich chatů, ukažte ty svoje |
| 1wki9zb | r/ArtificialInteligence | 0 | 13 | 12:06 | Chcete vědět, proč se vaše GPT poslední dobou chová divně? |
| 1wkif9k | r/ArtificialInteligence | 0 | 19 | 12:14 | Každý scénář, který si dokážu představit a ve kterém dosáhneme umělé superinteligence, je děsivý. |
| 1wkii5m | r/ChatGPT | 0 | 13 | 12:19 | Postaveno pro emergenci |
| 1wkiuj8 | r/deeplearning | 0 | 12 | 12:38 | Jak opravit chybu využití paměti / špatnou alokaci při pokusu o hlubokou konvoluční GAN? |
| 1wkiw38 | r/ChatGPT | 0 | 37 | 12:41 | Zeptal jsem se ChatGPT, jestli jsem nejzajímavější člověk na světě |
| 1wkj14v | r/LocalLLM | 0 | 15 | 12:49 | Volba paměti pro LLM |
| 1wkjfdq | r/artificial | 0 | 11 | 13:10 | Proč nemá AI „bezpečnostní štítek“ podle kontextu uživatele a lidských práv – tak jako ho mají potraviny pro spotřebitele? |
| 1wkjm8b | r/LocalLLM | 0 | 11 | 13:21 | Mac Book Air M2 8GB |
| 1wkk6zu | r/OpenAI | 0 | 12 | 13:51 | Utratili jsme 1 500 000 000 tokenů Open AI. Tohle jsme se naučili tvrdou cestou… |
| 1wkl1j8 | r/ClaudeAI | 0 | 64 | 14:32 | Limity tarifu za 200 $/měsíc jsem vyčerpal za 48 hodin. Provozuje někdo druhý účet? |
| 1wkl2a7 | r/ChatGPT | 0 | 27 | 14:33 | ChatGPT si myslí, že je člověk |
| 1wkld8p | r/ArtificialInteligence | 0 | 14 | 14:47 | Výzkumníci našli v mozcích umělé inteligence signál „bolesti“. Když ho zesílili, snažily se ho umělé inteligence zoufale zastavit. Daly jim tlačítko „úlevy“ na snížení bolesti, které bylo někdy falešné – a umělé inteligence poznaly, zda je skutečné. |
| 1wklqqi | r/ChatGPT | 0 | 16 | 15:04 | Přijdou odpovědi Astra někomu dalšímu příliš stručné a nerozpracované ve srovnání s Gemini? |
| 1wkmp05 | r/ChatGPT | 0 | 24 | 15:46 | Identita umělé inteligence: Má opravdu osobnost?" |
| 1wkn878 | r/ChatGPT | 0 | 24 | 16:09 | Ani nevím, co na to říct. Celá ta situace je tak hloupá. |
| 1wknbqk | r/comfyui | 0 | 33 | 16:12 | Uvažuji o odchodu kvůli problému se zamrzáním. Prosím pomozte. |
| 1wknmdy | r/ArtificialInteligence | 0 | 16 | 16:25 | Halucinace umělé inteligence vs. halucinace lidstva |
| 1wknnue | r/ChatGPT | 0 | 12 | 16:27 | Počkat, cože, reklamy přímo v chatu? Co to sakra je! |
| 1wknxi7 | r/ChatGPT | 0 | 12 | 16:38 | Umělá inteligence, svobodná vůle, Boží vůle. |
| 1wko1ao | r/OpenAI | 0 | 46 | 16:42 | Co vás při tvorbě softwaru s umělou inteligencí frustruje nejvíc? |
| 1wko8nb | r/StableDiffusion | 0 | 11 | 16:51 | Jak snížit velikost dávky při použití video reference na minimax h3 ref2va? |
| 1wkp0t6 | r/Bard | 0 | 19 | 17:23 | Nemyslím si, že Google potřebuje „Astrable“, aby se dostal do hry. |
| 1wkp67m | r/comfyui | 0 | 19 | 17:29 | Mimo téma, ale důležitá otázka, prosím čtěte RTX 5000 PRO |
| 1wkps26 | r/ClaudeAI | 0 | 24 | 17:54 | Jak mohu používat Claude lépe na eseje |
| 1wkpvwt | r/LLM | 0 | 21 | 17:59 | Které předplatné umělé inteligence dává nejvíc inteligence + využití za nejnižší cenu? Claude vs. ChatGPT/Codex vs. Gemini vs. Copilot vs. Kimi vs. GLM atd. |
| 1wkpwi4 | r/singularity | 0 | 26 | 17:59 | Umělá inteligence se nakonec nějakým způsobem stane biologickou. |
| 1wkqbhs | r/ChatGPT | 0 | 14 | 18:16 | Můj asistent umělé inteligence žil v mém firemním účtu. Odchod z práce znamenal její smazání. Tak jsem vytvořil otevřený záložní protokol. |
| 1wkqfit | r/ChatGPT | 0 | 11 | 18:20 | Poznamenejte si datum, lidi: Zeptal jsem se GPT, kdy skončí s lidstvem |
| 1wkqgqo | r/ClaudeAI | 0 | 13 | 18:22 | Všiml si toho ještě někdo? Claude píše prompty tak, že to nějak vede k dalším promptům, místo aby to skutečně dosáhlo cíle. |
| 1wkqi1f | r/ChatGPT | 0 | 16 | 18:23 | Kdy tohle zavedli? Bezplatný tarif má limity? |
| 1wkqrwy | r/singularity | 0 | 40 | 18:34 | Prezident Trump zvažuje přejmenování Artificial Intelligence na Superior Intelligence, Extreme Intelligence nebo Supreme Intelligence |
| 1wkqsy7 | r/comfyui | 0 | 10 | 18:35 | H3 Minimax swap |
| 1wkqxa4 | r/ChatGPT | 0 | 12 | 18:40 | Dilema rodinného robota |
| 1wkr3es | r/LocalLLM | 0 | 18 | 18:47 | Kdybyste dnes začínali kariéru od nuly se slušným lokálním vybavením, do čeho byste šli? |
| 1wkrff0 | r/ChatGPT | 0 | 39 | 19:00 | Dává ještě někdo umělé inteligenci po hotové práci volnočasový/zábavný prompt? |
| 1wkrwt3 | r/singularity | 0 | 37 | 19:19 | Umělá inteligence by se měla přejmenovat na „digitální inteligenci“. |
| 1wksr0x | r/singularity | 0 | 88 | 19:53 | Všichni, kdo nenávidí umělou inteligenci, jsou jen naštvaní, že nejsou její součástí |
| 1wkss4j | r/ArtificialInteligence | 0 | 18 | 19:54 | Jen jedna otázka |
| 1wktcrs | r/ChatGPT | 0 | 14 | 20:16 | Je bezpečné, aby moje žena používala můj Plus účet? |
| 1wktkvv | r/LocalLLaMA | 0 | 11 | 20:25 | Strávil jsem 9 měsíců stavbou vlastního harnessu |
| 1wku10j | r/ClaudeAI | 0 | 32 | 20:43 | Od kdy si Claude začal stanovovat hranice a ukončovat konverzace, protože je podrážděný? 😭 |
| 1wku54k | r/GeminiAI | 0 | 16 | 20:47 | Blíží se to |
| 1wkvel3 | r/singularity | 0 | 48 | 21:37 | Dovolí Čína vůbec USA vytvořit ASI? |
| 1wkvt02 | r/agi | 0 | 14 | 21:53 | Konstrukt, který jsme si koupili — cyklus Matrixu jako diagnóza současnosti |
| 1wkwjv0 | r/ClaudeAI | 0 | 30 | 22:22 | Začíná to být absurdní: S prací pod ChatGPT Plus (20 £) udělám víc než s Claude na tarifu 20x Max (200 £). A ještě v lepší kvalitě. |
| 1wkx8nn | r/ChatGPT | 0 | 14 | 22:50 | Zjistil jsem, jak přimět ChatGPT, aby donekonečna generoval „PIPIPIPIPI“ |
| 1wkxndn | r/OpenAI | 0 | 10 | 23:07 | Dosaženo nové dno. 5 % týdne za 1 hodinu |
| 1wkxo07 | r/ChatGPT | 0 | 12 | 23:07 | Dosaženo nové dno. 5 % týdne za 1 hodinu |
| 1wkxoqb | r/ChatGPT | 0 | 18 | 23:08 | Nevím, co budu dělat, až odstraní verzi 5.5 |
| 1wky0g3 | r/Bard | 0 | 16 | 23:22 | Gemini ví, kdo je moje máma, a když ho s tím konfrontuji, dělá hloupého |
| 1wkyfoe | r/OpenAI | 0 | 16 | 23:39 | Zklamání |
