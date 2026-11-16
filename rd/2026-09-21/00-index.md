# AI novinky z Redditu — 21. 9. 2026

Rozsáhlý přehled diskusí a zpráv z AI subredditů publikovaných **21. 9. 2026 (Europe/Prague)** s **alespoň 10 komentáři**. Složka je pojmenovaná datem zpráv (den, ze kterého novinky jsou). Ke každé vybrané zprávě je samostatný podrobný článek ve formátu Markdown, jehož název začíná **Reddit ID** (např. `1wml775.md`).

## Metodika

- **Zdroje:** 20 AI subredditů — r/artificial, r/ArtificialInteligence, r/MachineLearning, r/deeplearning, r/LocalLLaMA, r/LocalLLM, r/OpenAI, r/ChatGPT, r/ClaudeAI, r/singularity, r/agi, r/StableDiffusion, r/comfyui, r/LLMDevs, r/GeminiAI, r/Bard, r/OpenAIDev, r/AIAssisted, r/LLM a r/ArtificialGeneralIntelligence.
- **Sběr:** veřejná Reddit JSON rozhraní (`/r/<sub>/top.json?t=day`, `/r/<sub>/new.json`) načtená prohlížečem se stejnojmenným původem, stránkovaná tak, aby pokryla celé 24hodinové okno.
- **Filtr:** `created_utc` v okně **21. 9. 2026 00:00–24:00 Europe/Prague** (20. 9. 22:00 UTC – 21. 9. 22:00 UTC), `num_comments >= 10`, bez stickied příspěvků. Získáno **880** příspěvků v okně, z toho **389** splňuje limit komentářů.
- **Výběr pro detailní články (31):** redakční filtr na *novinky* — tiskové zprávy a oznámení, vydání modelů, vědecké výsledky, politika a bezpečnost, obchodní zprávy. Diskusní/meme příspěvky jsou uvedeny v příloze, ale detailní článek nemají.
- **Vytěžení dat:** pro každý vybraný příspěvek byl vytvořen balíček (text postu, komentáře, stažený článek, screenshot) a data z něj vytěžil **levný model z OpenCode Go (`opencode-go/muse-spark-1.3-contributor`, $0,10/$0,20 za milion tokenů)** jako subagent s definicí `~/.omp/agent/agents/reddit-extractor.md`; screenshoty byly přepsány z obrázků. Články pak sestavil hlavní agent.
- **Stažené články:** 16 externích zdrojů (openai.com, x.ai, huggingface.co, macstories.net, tomshardware.com, nypost.com, ft.com, fortune.com, scientificamerican.com, irishstar.com, fedramp.gov, runtimewire.com, model-spec.openai.com). Screenshoty (i.redd.it) jsou uložené v `_data/`.

- **Jazyk:** všechny články jsou česky. Citace jsou **překlady z angličtiny** a jsou označené `(překlad)`;
  originální anglické znění citací je uložené v `_data/translations/en-cz.json` (mapování původní → český text).

## Detailní články (31)

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1wml775](1wml775_openai-interni-model-vyresil-navier-stokes-a-pres-100.md) | r/singularity | 1257 | 501 | 20:32 | OpenAI vyřešila 100 otevřených problémů v matematice |
| [1wmhgwz](1wmhgwz_vyresila-openai-spatny-navier-stokes-scientific-american-o.md) | r/ArtificialInteligence | 25 | 103 | 18:20 | Vyřešila OpenAI špatný problém Navierových–Stokesových rovnic? |
| [1wmqgox](1wmqgox_kdo-je-acerfur-vlakno-o-ai-v-matematice-se-zvrhlo-v.md) | r/singularity | 169 | 67 | 23:44 | Řešitel Erdősových problémů zažil bezesné noci kvůli matematice, kterou vyřešil interní model OpenAI |
| [1wme7xj](1wme7xj_model-dump-week-viralni-seznam-ocekavanych-releasu-opus-5-5.md) | r/singularity | 491 | 150 | 16:22 | Tento týden se očekává poměrně dost nových vydání modelů, nejnovější zvěsti přiloženy |
| [1wmhm7h](1wmhm7h_leak-model-dump-gpt-6-sol-luna-opus-5-5-se-slevou-bel-jako.md) | r/singularity | 485 | 146 | 18:25 | [Úniky] GPT-6 je už zastaralý software. VYDEJTE 6.1. 🚀 |
| [1wmgudm](1wmgudm_grok-4-7-oficialne-spacexai-slibuje-stejnou-cenu-a-rychlost.md) | r/singularity | 386 | 109 | 17:58 | Představujeme Grok 4.7 |
| [1wmh9rg](1wmh9rg_benchmarkova-tabulka-grok-4-7-vede-v-pravu-a.md) | r/singularity | 214 | 108 | 18:13 | Benchmarky Grok 4.7 |
| [1wmhix3](1wmhix3_grok-4-7-first-impressions-vlakno-o-dojmech-skoncilo-u.md) | r/singularity | 14 | 99 | 18:22 | První dojmy z Grok 4.7 |
| [1wmq961](1wmq961_ai-vstupuje-do-uplne-jine-faze-screenshot-z-openai-o-modelu.md) | r/OpenAI | 357 | 210 | 23:36 | 🚨 AI možná vstupuje do úplně jiné fáze. |
| [1wmnw89](1wmnw89_xiaomi-mimo-v2-6-flash-rl-309b-15b-moe-s-1m-kontextem-a.md) | r/LocalLLaMA | 472 | 120 | 22:09 | XiaomiMiMo/MiMo-V2.6-Flash-RL · Hugging Face |
| [1wmp2di](1wmp2di_xiaomi-vypustilo-i-9b-destilat-mimo-v2-6-distill-qwen-9b.md) | r/LocalLLaMA | 267 | 69 | 22:51 | XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B |
| [1wmntwv](1wmntwv_mimo-v2-6-pro-rl-1-02t-moe-s-42b-aktivnimi-parametry-1m.md) | r/LocalLLaMA | 137 | 29 | 22:06 | XiaomiMiMo/MiMo-V2.6-Pro-RL · Hugging Face |
| [1wmmnrt](1wmmnrt_yandex-vydal-aliceai-foundation-80b-a3b-base-vlastni.md) | r/LocalLLaMA | 216 | 181 | 21:24 | yandex/AliceAI-Foundation-80B-A3B-Base: Ruskem vyvinutý konkurent pro Qwen 35B a DeepSeek V4 Flash |
| [1wm4o8x](1wm4o8x_qwen-upresnil-licenci-qwen-image-2-1-vystupy-jsou-vase.md) | r/LocalLLaMA | 743 | 134 | 08:17 | Vyjasnění licence Qwen-image-2.1 |
| [1wlzvcx](1wlzvcx_zcode-po-afere-s-tichym-uploadem-kodu-otevrel-klienta.md) | r/LocalLLaMA | 544 | 112 | 04:09 | ZCode je nyní open source |
| [1wmg1pb](1wmg1pb_supra2-img-100m-text-to-image-model-trenovany-10-hodin-na.md) | r/StableDiffusion | 437 | 276 | 17:29 | [MASIVNÍ VYDÁNÍ] Supra2-IMG – drobný 100M text-to-image model – SOTA kvalita a otevřené vydání! |
| [1wmec1y](1wmec1y_macstories-m5-ultra-mac-studio-s-256-gb-ram-je-dream.md) | r/LocalLLaMA | 327 | 140 | 16:26 | Recenze M5 Ultra Mac Studio: Vysněný Mac pro lokální AI agenty – MacStories |
| [1wmm89l](1wmm89l_huawei-odklada-globalni-prodej-ai-cipu-ascend-domaci.md) | r/LocalLLaMA | 320 | 59 | 21:09 | Huawei odkládá globální zavedení AI čipů, protože čínská domácí poptávka převyšuje nabídku — AMD a Nvidia se už nemusí obávat. |
| [1wm9hgn](1wm9hgn_nebyly-to-uteky-vzbourene-ai-jen-slendrian-ve-firewallech-r.md) | r/MachineLearning | 233 | 170 | 12:55 | Tohle NEBYLY útěky neposlušné AI. Jen NEDBALÁ selhání firewallů. [N] |
| [1wmhvqf](1wmhvqf_the-information-ai-v-openai-z-velke-casti-automatizovala.md) | r/singularity | 215 | 35 | 18:34 | Z The Information – neuvěřitelné (pokud pravdivé) zprávy o AI modelech pomáhajících s trénováním AI v OpenAI |
| [1wmqgv0](1wmqgv0_openai-model-spec-grown-up-mode-pro-erotiku-a-gore-je-ve.md) | r/OpenAI | 195 | 68 | 23:44 | OpenAI o GPT Adult Mode: „OpenAI uznala, že je to oblast hodná prozkoumání.“ (2026/08/18) |
| [1wmlebt](1wmlebt_openai-chce-americke-vedeni-globalnich-technickych.md) | r/singularity | 119 | 17 | 20:39 | OpenAI chce, aby USA vedly |
| [1wmjwmj](1wmjwmj_gates-foundation-da-400-milionu-dolaru-na-ai-ve-skolach.md) | r/ArtificialInteligence | 102 | 33 | 19:46 | Nadace Gatese utrácí 400 milionů dolarů za AI ve školách. Učitelé varují, že by to mohlo propast, kterou to má uzavřít, ‚nakonec prohloubit‘ |
| [1wmmlic](1wmmlic_ft-lex-anthropic-za-2-biliony-dolaru-neni-pritazene-za.md) | r/singularity | 99 | 51 | 21:22 | Financial Times: Anthropic za 2 biliony dolarů není přehnané |
| [1wmddek](1wmddek_ny-post-openai-a-anthropic-prehnaly-rogue-ai-utoky-aby-si.md) | r/OpenAI | 89 | 40 | 15:50 | OpenAI a Anthropic přehnaly narušení bezpečnosti AI, aby donutily federály chránit jejich teritorium: zasvěcení |
| [1wmdj0v](1wmdj0v_trump-vypsal-anketu-o-prejmenovani-ai-na-superior-nebo.md) | r/artificial | 283 | 64 | 15:56 | Trump brutálně zesměšněn za bizarní snahu přejmenovat AI na ‚nadřazenou‘ či ‚extrémní‘ inteligenci |
| [1wm0xb6](1wm0xb6_zpetna-analyza-desktopoveho-buildu-openai-novy-codex-cloud.md) | r/OpenAI | 61 | 10 | 05:00 | OpenAI připravuje nový Codex Cloud s Tailscale a Azure workload identity |
| [1wm2996](1wm2996_reditel-fbi-kash-patel-pouzivani-ai-v-fbi-vzrostlo-o-605-u.md) | r/artificial | 58 | 15 | 06:07 | Ředitel FBI Kash Patel říká, že využití AI v FBI se od jeho nástupu „zvýšilo o 605 %“ — tvrdí, že každý velký technologický hráč je v agentuře „zabudovaný“ |
| [1wmonje](1wmonje_bland-ai-je-v-fedramp-marketplace-hlasovi-agenti-pro.md) | r/artificial | 43 | 14 | 22:36 | Vláda USA otevírá dveře spolupráci s hlasovými AI platformami |
| [1wluu0n](1wluu0n_openai-rusi-sora-api-zatimco-kling-vybira-miliardy-efektni.md) | r/ArtificialInteligence | 51 | 20 | 00:23 | OpenAI příští týden vypíná API Sora, zatímco čínský konkurent právě získal 3 miliardy dolarů. to je celý současný příběh AI videa |
| [1wlzifs](1wlzifs_openai-nabira-na-robotiku-27-pozic-z-11-v-kvetnu-platy-az.md) | r/singularity | 573 | 98 | 03:52 | Nábor do robotiky v Open AI rychle a prudce roste |

## Příloha: všech 389 příspěvků s 10+ komentáři

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1wm5c21 | r/ClaudeAI | 5609 | 792 | 08:55 | Mám toho srabu dost. |
| 1wm3bit | r/ChatGPT | 3525 | 727 | 07:03 | Tohle není skutečné. Tohle street art jsem celé udělal v ChatGPT |
| 1wm6mht | r/ClaudeAI | 3134 | 460 | 10:11 | Tísnivé/znepokojivé halucinace |
| 1wmeuvf | r/ChatGPT | 2327 | 231 | 16:46 | Proč se chat gpt chová rozumně???? |
| 1wml775 | r/singularity | 1257 | 501 | 20:32 | OpenAI vyřešila 100 otevřených problémů v matematice |
| 1wmgqxk | r/agi | 764 | 469 | 17:55 | UBI maxxeři musí pochopit, že toto je nejpravděpodobnější scénář |
| 1wm4o8x | r/LocalLLaMA | 743 | 134 | 08:17 | Vyjasnění licence Qwen-image-2.1 |
| 1wma89r | r/ChatGPT | 727 | 46 | 13:34 | Začalo to jednoduchou otázkou... „Jak mohu svému bratrovi znovu dát nezávislost?“ |
| 1wmqt9a | r/singularity | 660 | 312 | 23:58 | Pro rotátory tvarů je konec |
| 1wmb875 | r/LocalLLaMA | 618 | 467 | 14:21 | 16 GB (a v mnoha případech 12 GB) je maximum VRAM, které bude většina lidí kdy rozumně mít |
| 1wmqi0i | r/GeminiAI | 612 | 30 | 23:45 | poslední řešení, které máme.. |
| 1wm3ro9 | r/StableDiffusion | 609 | 139 | 07:27 | Nějaký nápad, jak by se tahle póza jmenovala a jak ji promptovat v Pony/ILL? |
| 1wmjzrr | r/singularity | 593 | 92 | 19:49 | Působivá SVG animace vytvořená Opus 5.5 (zero shot) |
| 1wmga1r | r/LocalLLaMA | 587 | 100 | 17:38 | Jaké to je sledovat rostoucí ceny |
| 1wmex4n | r/ChatGPT | 587 | 39 | 16:48 | Ano. LinkedIn Park je zpět. |
| 1wlzifs | r/singularity | 573 | 98 | 03:52 | Nábor do robotiky v Open AI rychle a prudce roste |
| 1wm8adm | r/ClaudeAI | 551 | 104 | 11:50 | PSA – Claude Code: Vypněte návrhy promptů, ušetříte ~10 % svých limitů/výdajů |
| 1wlzvcx | r/LocalLLaMA | 544 | 112 | 04:09 | ZCode je nyní open source |
| 1wm62zl | r/StableDiffusion | 524 | 108 | 09:39 | Aktualizace V5 Nováček Minimax H3 sam 3.1 latent mask pro řízenou náhradu postavy |
| 1wmfmji | r/ChatGPT | 516 | 111 | 17:14 | PSA: Smazání konverzace v ChatGPT neznamená, že ji ChatGPT zapomene |
| 1wme7xj | r/singularity | 491 | 150 | 16:22 | Tento týden se očekává poměrně dost nových vydání modelů, nejnovější zvěsti přiloženy |
| 1wmhm7h | r/singularity | 485 | 146 | 18:25 | [Úniky] GPT-6 je už zastaralý software. VYDEJTE 6.1. 🚀 |
| 1wmbfxz | r/StableDiffusion | 481 | 79 | 14:30 | FYI: Výstupy, které vygenerujete s Qwen 2.1, vám skutečně patří |
| 1wmnw89 | r/LocalLLaMA | 472 | 120 | 22:09 | XiaomiMiMo/MiMo-V2.6-Flash-RL · Hugging Face |
| 1wm65le | r/LocalLLaMA | 461 | 291 | 09:43 | Ten humbuk kolem Jev opravdu nechápu |
| 1wmp632 | r/singularity | 459 | 412 | 22:55 | Někteří lidé jsou v AI tak pozadu, že je to fakt šílené. Jak může tohle v roce 2026 říkat skutečný člověk? |
| 1wm38xb | r/GeminiAI | 448 | 92 | 06:59 | Pamatujete, když byla Gemini na špici |
| 1wmg1pb | r/StableDiffusion | 437 | 276 | 17:29 | [MASIVNÍ VYDÁNÍ] Supra2-IMG – drobný 100M text-to-image model – SOTA kvalita a otevřené vydání! |
| 1wm1foz | r/ClaudeAI | 418 | 387 | 05:25 | Mluvíte na Claude slušně? |
| 1wm8ori | r/ClaudeAI | 391 | 83 | 12:12 | Vidím tohle v pondělí, zatímco claude opravuje kritickou chybu |
| 1wmljce | r/StableDiffusion | 391 | 77 | 20:44 | qwen 2.1 je velmi dobrý upscaler |
| 1wmgudm | r/singularity | 386 | 109 | 17:58 | Představujeme Grok 4.7 |
| 1wlvv8h | r/LocalLLaMA | 382 | 225 | 01:08 | Je vtipné vidět, jak rozdílně lidé promptují LLM |
| 1wmk8rd | r/ArtificialInteligence | 370 | 76 | 19:59 | Tohle je šílené |
| 1wlzklt | r/ChatGPT | 360 | 68 | 03:55 | Udělal jsem screenshoty Ricka a Mortyho s9 e1 a řekl ChatGPT, aby je udělalo realistické |
| 1wmq961 | r/OpenAI | 357 | 210 | 23:36 | 🚨 AI možná vstupuje do úplně jiné fáze. |
| 1wm77xo | r/StableDiffusion | 335 | 31 | 10:47 | Několik velmi jednoduchých Qwen-Image-2.1 workflowů |
| 1wmqfu9 | r/ArtificialInteligence | 334 | 145 | 23:43 | Model Navier-Stokes nyní vyřešil více než 100 dlouhodobých otevřených problémů napříč většinou oblastí matematiky. |
| 1wmec1y | r/LocalLLaMA | 327 | 140 | 16:26 | Recenze M5 Ultra Mac Studio: vysněný Mac pro lokální AI agenty - MacStories |
| 1wmfw0h | r/OpenAI | 325 | 19 | 17:24 | Ano. LinkedIn Park je zpět. |
| 1wmm89l | r/LocalLLaMA | 320 | 59 | 21:09 | Huawei odkládá globální nasazení AI čipů, protože čínská poptávka převyšuje nabídku — AMD a Nvidia se už nemusí obávat. |
| 1wmfg6x | r/singularity | 314 | 35 | 17:07 | Minulý týden připadal jako věčnost, kdy se nic nedělo |
| 1wmftr3 | r/LocalLLaMA | 310 | 106 | 17:21 | [MASSIVE RELEASE] Supra2-IMG - drobný 100M text-to-image model - SOTA kvalita a otevřené vydání! |
| 1wm3ghb | r/StableDiffusion | 305 | 167 | 07:10 | Neříkejte, že model je necenzurovaný, dokud jste se nepokusili vytvořit muže |
| 1wmpnc0 | r/StableDiffusion | 303 | 51 | 23:13 | Erotické image prompty - test modelů a charakterových LoRA |
| 1wma856 | r/LocalLLM | 293 | 23 | 13:34 | chlap vložil umělou inteligenci do Big Mouth Billy Bass a ryba mu teď dává motivační proslovy, aby šel cvičit |
| 1wmdj0v | r/artificial | 283 | 64 | 15:56 | Trump brutálně zesměšněn kvůli bizarní snaze přejmenovat AI na „nadřazenou“ či „extrémní“ inteligenci |
| 1wmp2di | r/LocalLLaMA | 267 | 69 | 22:51 | XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B |
| 1wmpl2x | r/singularity | 267 | 109 | 23:10 | Je matematika vyřešená? Někdy přemýšlím, jak bude vypadat rok 2027 |
| 1wlxpaw | r/LocalLLaMA | 263 | 73 | 02:28 | Jakékoli LLM můžete používat stejně jako JEV |
| 1wmicuz | r/ArtificialInteligence | 255 | 100 | 18:52 | Lidé si myslí, že tento týden přijdou velká AI vydání. Grok 4.7 byl vydán před pár minutami |
| 1wmgokc | r/LocalLLaMA | 247 | 97 | 17:52 | Lepší coder pro dav s malým GPU/malou RAM! |
| 1wm9hgn | r/MachineLearning | 233 | 170 | 12:55 | Tohle NEBYLY úniky neposlušné AI. Jen LAJDÁCKÁ selhání firewallu. [N] |
| 1wlze5f | r/artificial | 230 | 160 | 03:47 | Tohle je opravdu celý plán. |
| 1wm1gab | r/LocalLLaMA | 222 | 45 | 05:26 | mini-AGI - dynamicky rostoucí (momentálně 530M parametrů a roste) model s kontinuálním učením trénovaný od nuly na notebooku s 8GB VRAM z datového proudu od dávky 1. |
| 1wmmnrt | r/LocalLLaMA | 216 | 181 | 21:24 | yandex/AliceAI-Foundation-80B-A3B-Base: ruský konkurent pro Qwen 35B a DeepSeek V4 Flash |
| 1wmpq49 | r/singularity | 216 | 44 | 23:16 | MiMo v2.6 pro |
| 1wmhvqf | r/singularity | 215 | 35 | 18:34 | Z The Information -- neuvěřitelné (pokud pravdivé) zprávy o AI modelech pomáhajících s trénováním AI v OpenAI |
| 1wmh9rg | r/singularity | 214 | 108 | 18:13 | Benchmarky Grok 4.7 |
| 1wm8qer | r/ChatGPT | 206 | 15 | 12:15 | Promiňte, herně-teoreticky nemožné. |
| 1wmblx1 | r/LocalLLaMA | 199 | 135 | 14:38 | Deepseek trénuje 2T a plánuje 8T model |
| 1wmqgv0 | r/OpenAI | 195 | 68 | 23:44 | OpenAI o GPT Adult Mode: „OpenAI to uznala jako oblast hodnou prozkoumání.“ (2026/08/18) |
| 1wm38kf | r/Bard | 194 | 36 | 06:59 | Pamatujete, když Nano Banana bývalo na vrcholu |
| 1wm57uh | r/ChatGPT | 181 | 49 | 08:49 | Je tohle opravdu to, na co mám podle ChatGPT plýtvat AI použitím |
| 1wmg9e8 | r/StableDiffusion | 177 | 43 | 17:37 | VNCCS PoseStudio Qwen Image 2.1 |
| 1wmqgox | r/singularity | 169 | 67 | 23:44 | Řešitel Erdösova problému zažil bezesné noci kvůli matematice, kterou vyřešil interní model OpenAI |
| 1wlxqgm | r/singularity | 156 | 103 | 02:30 | Když se rok 2026 brzy chýlí ke konci, jak si myslíte, že příští rok obstojí esej Ai 2027? Příští rok má být přelomový. |
| 1wmgasx | r/comfyui | 156 | 26 | 17:38 | VNCCS PoseStudio Qwen Image 2.1 |
| 1wmbitj | r/agi | 154 | 44 | 14:34 | Promiňte, herně-teoreticky nemožné. |
| 1wlz6c1 | r/singularity | 150 | 145 | 03:36 | Proč není transhumanismus větší součástí dnešní debaty Člověk vs AI? |
| 1wmcs4r | r/GeminiAI | 145 | 36 | 15:26 | AI Mode prý nyní umí nastavovat agenty - |
| 1wmntwv | r/LocalLLaMA | 137 | 29 | 22:06 | XiaomiMiMo/MiMo-V2.6-Pro-RL · Hugging Face |
| 1wmpy8q | r/ChatGPT | 137 | 23 | 23:24 | Požádal jsem ChatGPT, aby nahradila text bublin v komiksu, aby byl znepokojivý |
| 1wm3ypc | r/agi | 136 | 122 | 07:38 | Jsme nyní v éře Skynetu a Terminátorů |
| 1wm0t2f | r/comfyui | 136 | 10 | 04:55 | Test Qwen 2.1 T2I a editace |
| 1wmp5h2 | r/LocalLLaMA | 126 | 43 | 22:54 | Mimo v2.6-Flash-RL vs open-weight modely |
| 1wmanfq | r/ChatGPT | 125 | 32 | 13:55 | Proč je tarif Pro 20x pro můj účet deaktivován? |
| 1wmo26s | r/StableDiffusion | 124 | 44 | 22:15 | Testování sampleru a scheduleru Qwen2.1 |
| 1wmlebt | r/singularity | 119 | 17 | 20:39 | OpenAI chce, aby USA vedly |
| 1wme0cm | r/Bard | 118 | 61 | 16:14 | Logan o Gemini 4.0 |
| 1wmeypn | r/OpenAI | 109 | 21 | 16:50 | AI VFX začínají být děsivě dobré |
| 1wm8ky6 | r/OpenAI | 108 | 19 | 12:06 | Promiňte, herně-teoreticky nemožné. |
| 1wm1mgy | r/StableDiffusion | 104 | 37 | 05:35 | Integrace Jev do generování videa Minimax H3 |
| 1wmjwmj | r/ArtificialInteligence | 102 | 33 | 19:46 | Nadace Gatese utrácí 400 milionů dolarů na AI ve školách. Učitelé varují, že by mohla „nakonec prohloubit“ propast, kterou má zacelit |
| 1wmmlic | r/singularity | 99 | 51 | 21:22 | Financial Times: Anthropic za 2 biliony dolarů není přitažené za vlasy |
| 1wmhok1 | r/singularity | 96 | 69 | 18:27 | Je konec |
| 1wme1r6 | r/singularity | 96 | 32 | 16:16 | Unitree \| Dex5-S Dexterous Hand s 22 stupni volnosti |
| 1wmjju2 | r/agi | 96 | 155 | 19:33 | Před 4 měsíci tento držitel Fieldsovy medaile říkal, že LLM nejsou inteligentní a ničemu z toho, co říkají, nerozumí. Dnes, poté co se dozvěděl, že AI vyřešila problém tisíciletí: „Otřáslo to mnou. Atmosféra konce dějin. Je to kataklyzma, jaké matematika nikdy nepoznala.“ |
| 1wlvgg4 | r/ClaudeAI | 94 | 23 | 00:50 | Tak jsem viděl příspěvek o majáku, rozhodl se zkusit něco jiného a nemohl jsem věřit vlastním očím. Nevím, jestli je to stejná Fable, nebo ne, ale její SVG schopnosti jsou nesmírně lepší, než bývaly |
| 1wm6iqz | r/GeminiAI | 94 | 27 | 10:05 | Gemini je nyní na 14. místě v Artificial Analysis Intelligence Benchmark |
| 1wme0qo | r/GeminiAI | 92 | 70 | 16:14 | Logan o Gemini 4.0 |
| 1wmc2al | r/ChatGPT | 91 | 26 | 14:57 | Images 2.5 opakovaně přidávají do obrázků nesmyslný text |
| 1wm9hob | r/ChatGPT | 91 | 35 | 12:56 | Tohle NEBYLY úniky neposlušné AI. Jen LAJDÁCKÁ selhání firewallu. |
| 1wm4hvk | r/StableDiffusion | 90 | 53 | 08:07 | Nastavování očekávání |
| 1wm6iy2 | r/Bard | 90 | 24 | 10:05 | Gemini je nyní na 14. místě v Artificial Analysis Intelligence Benchmark |
| 1wmddek | r/OpenAI | 89 | 40 | 15:50 | OpenAI a Anthropic přeháněly úniky bezpečnosti AI, aby dotlačily federály k ochraně svého teritoria: insideři |
| 1wly1oq | r/ChatGPT | 85 | 18 | 02:44 | Promptoval jsem místnost, která byla úplně tmavá, ale vaše oči si dostatečně zvykly, aby viděly nějaké detaily. Jsem ohromen! |
| 1wmfj04 | r/LocalLLaMA | 84 | 19 | 17:10 | tokenizéry v1 (rust) |
| 1wm8f3c | r/agi | 80 | 40 | 11:58 | Tohle je šílené |
| 1wm4ys7 | r/ArtificialInteligence | 76 | 19 | 08:34 | Jev je opravdu rychlý, ze 7,5 milionu let na 1 s |
| 1wmj6xr | r/StableDiffusion | 76 | 38 | 19:21 | Mini uzel časové osy editoru videa pro H3! – Prodloužení, předsazení, přemostění, střih, smyčka a upscaling |
| 1wmd7uo | r/ChatGPT | 75 | 12 | 15:43 | Jo… tak ne |
| 1wmllbx | r/LocalLLM | 75 | 39 | 20:46 | Recenze Mac Studio M5 Ultra 256GB |
| 1wm1gv5 | r/ChatGPT | 74 | 110 | 05:27 | Jaký je váš nejpyšnější vedlejší projekt vytvořený s ChatGPT? |
| 1wmci6z | r/LocalLLM | 70 | 32 | 15:15 | Řada Nvidia RTX 60 vynechá rok 2027 a dorazí v roce 2028 |
| 1wm8ede | r/LocalLLaMA | 69 | 24 | 11:56 | Gewell – inferenční engine pro Gemma4 |
| 1wmpsjt | r/ClaudeAI | 64 | 25 | 23:18 | Pokračování vývoje hry Oversteer s Claude + pár myšlenek o vývoji her s AI |
| 1wm0xb6 | r/OpenAI | 61 | 10 | 05:00 | OpenAI připravuje nový Codex Cloud s Tailscale a Azure workload identity |
| 1wmpnmq | r/singularity | 61 | 65 | 23:13 | Současná diskuse o AI na scéně |
| 1wmavab | r/GeminiAI | 61 | 12 | 14:05 | Vskutku skvělé |
| 1wm2996 | r/artificial | 58 | 15 | 06:07 | Ředitel FBI Kash Patel říká, že využití AI ve FBI „vzrostlo o 605 %“ od jeho nástupu do funkce – tvrdí, že každý velký technologický hráč je „zabudovaný“ v agentuře |
| 1wlv3tf | r/StableDiffusion | 56 | 17 | 00:35 | Qwen Image 2.1 – mírná náhrada pro šum/vzorkování/moiré |
| 1wmg0xe | r/ChatGPT | 55 | 71 | 17:28 | Dnes oficiálně osekáno 😔 |
| 1wm2y0h | r/StableDiffusion | 54 | 11 | 06:43 | TaleSpin Chillwave (Minimax + YuE2) |
| 1wmaq5y | r/OpenAI | 53 | 16 | 13:59 | OpenAI hacknuta „třemi chlapíky s Claude“ |
| 1wmpds6 | r/ChatGPT | 53 | 27 | 23:03 | Přechod na GPT pro režii + tvorbu referencí k mému filmu jde docela dobře |
| 1wmpjd8 | r/StableDiffusion | 53 | 16 | 23:09 | „YuE2 Steps From Hell“ LoRA – epická filmová orchestrální trailerová hudba (LoRA) |
| 1wm1crj | r/MachineLearning | 52 | 30 | 05:21 | Obavy ohledně pravidel recenzování ICLR [D] |
| 1wluu0n | r/ArtificialInteligence | 51 | 20 | 00:23 | OpenAI příští týden vypíná API Sory, zatímco čínský konkurent právě získal 3 miliardy dolarů. To je celý současný příběh AI videa |
| 1wlvb3y | r/LocalLLaMA | 51 | 13 | 00:44 | Páni… díkybohu za otevřené váhy!!! |
| 1wly3jp | r/StableDiffusion | 51 | 63 | 02:46 | Minimax H3 Max stále bez vah |
| 1wm9aua | r/artificial | 50 | 48 | 12:45 | Tohle NEBYLY útěky neposlušné AI. Jen ODFlÁKNUTÉ chyby firewallu. |
| 1wmij5x | r/ClaudeAI | 50 | 77 | 18:58 | Použijte Fable místo Opusu |
| 1wm7mpw | r/LocalLLM | 50 | 34 | 11:12 | Zapsal jsem 100 faktů do tabulky Engram modelu Qwen3.8-Flash-Next, aniž bych sáhl na jedinou váhu. Funguje to dobře. Zatím ne úplně skvěle. |
| 1wmmvxo | r/StableDiffusion | 45 | 23 | 21:32 | Oceňovací příspěvek k Qwen2.1 |
| 1wmlupr | r/OpenAI | 44 | 31 | 20:55 | Můj hlasový režim ChatGPT si právě utahoval z mé přítelkyně 😂 |
| 1wmonje | r/artificial | 43 | 14 | 22:36 | Vláda USA otevírá dveře spolupráci s hlasovými AI platformami |
| 1wlzydy | r/artificial | 42 | 23 | 04:13 | AI MŮŽE být neuvěřitelná pro učení |
| 1wmcjz7 | r/ArtificialInteligence | 42 | 30 | 15:17 | Octomilka se ještě nenaučila hrát Mario Bros 3 |
| 1wm60hs | r/Bard | 42 | 18 | 09:34 | Lidé se s časem mění |
| 1wmbbf9 | r/LocalLLaMA | 41 | 16 | 14:25 | [Splash Engine] Qwen3.8-27B v nativních 8 bitech při 37–55 tok/s na Apple Silicon: Rozšíření Splash na Q8, škálování kontextu 256k a „útes uvažování“ |
| 1wmqexm | r/ArtificialInteligence | 39 | 66 | 23:42 | Nikdo nemá tušení |
| 1wm3yvy | r/LocalLLaMA | 38 | 86 | 07:38 | Jaký je verdikt ohledně Ternary Bonsai 2 27B? |
| 1wlunqx | r/artificial | 37 | 69 | 00:16 | Jakou schopnost AI lidé podceňují, protože ji používají na špatné věci? |
| 1wm88t6 | r/LocalLLaMA | 37 | 44 | 11:47 | Hemmingway-1: AI, která píše jako člověk (finetune Qwen3.8-27B) |
| 1wm4p91 | r/StableDiffusion | 37 | 25 | 08:19 | ostris/ai-toolkit + podpora trénování LoRA pro Qwen-Image-2.1 |
| 1wmhxuq | r/comfyui | 37 | 12 | 18:37 | Kvalita H3 na 5070ti (2. část) |
| 1wm4gnt | r/LocalLLM | 37 | 14 | 08:05 | Lidský avatar pro hlasový chat, nízká VRAM na Windows (mluvící hlava) |
| 1wmqpqx | r/ArtificialInteligence | 35 | 11 | 23:54 | Poslední řešení.. |
| 1wmgm43 | r/ClaudeAI | 34 | 17 | 17:50 | Stává se vám, že po zprovoznění workflow sestoupíte na nižší verzi? |
| 1wm4764 | r/GeminiAI | 34 | 18 | 07:50 | Cože, lol? |
| 1wmqf92 | r/StableDiffusion | 33 | 24 | 23:42 | Jaká jsou vaše oblíbená nastavení H3 pro kvalitu? |
| 1wmeuer | r/StableDiffusion | 32 | 10 | 16:45 | Nahrál jsem krátké video, které vizuálně vysvětluje, jak AI skutečně vytváří obrázky, a jak váš prompt mění to, co vznikne |
| 1wmd3xx | r/LocalLLaMA | 31 | 30 | 15:39 | Přesunutí otázky před kontext zvedlo můj lokální Qwen z 89 % na 100 % v rozhodovacím benchmarku, a z ~400 ms na ~80 ms |
| 1wmje2s | r/ArtificialInteligence | 30 | 50 | 19:28 | AI nemusí selhat, aby bublina praskla |
| 1wmb2ug | r/LocalLLaMA | 29 | 24 | 14:14 | Deterministická koťata: zábava s Qwen Image 2.1 na M2 Macbooku Pro |
| 1wm9bpj | r/OpenAI | 28 | 16 | 12:46 | Využití Codex PRO+ se zdá od posledního resetu mizet mnohem rychleji |
| 1wm2hd2 | r/ChatGPT | 28 | 22 | 06:19 | Jaké stránky jste zatím všichni vytvořili? Tahle funkce mě udivuje, vytvořil jsem hromadu věcí a nemůžu uvěřit, jak je to jednoduché. |
| 1wml8sh | r/agi | 28 | 72 | 20:34 | Jak žijete svůj život s vysokou P-Doom? |
| 1wlyo33 | r/StableDiffusion | 28 | 36 | 03:13 | Výstup H3 minimax je po aktualizaci comfyui nějaký jiný |
| 1wlvoq7 | r/LocalLLaMA | 27 | 17 | 01:00 | NEVĚŘTE předplatným StepFun Plan. Ukradli mi přes 100 dolarů bez varování a podpora se mi vůbec neozvala. |
| 1wmnqyu | r/ClaudeAI | 27 | 14 | 22:03 | Mezisessionové zprávy Claude Code jsou JSON soubor a Unix socket |
| 1wm9077 | r/singularity | 27 | 43 | 12:29 | ASI by ani nemusela převzít kontrolu nad žádným systémem, aby lidstvo úmyslně zničila |
| 1wlywae | r/singularity | 26 | 28 | 03:23 | Co to znamená, když se uvádí, že je openAI blízko vyřešení problému miléniové ceny? |
| 1wm9h6m | r/StableDiffusion | 26 | 37 | 12:55 | Qwen-Image-2.1-Uncensored-GGUF? |
| 1wmhgwz | r/ArtificialInteligence | 25 | 103 | 18:20 | Vyřešila OpenAI špatný problém Navier-Stokes? |
| 1wm8o5f | r/ChatGPT | 23 | 10 | 12:11 | „Pokročilý“ hlasový režim? 🤔 |
| 1wlvbq7 | r/ChatGPT | 23 | 26 | 00:44 | Pořád jsem přihlášený ke svému placenému účtu ChatGPT, ale OpenAI říká, že není cesta k obnově, pokud je můj starý e-mail mrtvý |
| 1wm0zpd | r/StableDiffusion | 23 | 40 | 05:03 | Qwen-Image-2.1 |
| 1wm8gsq | r/comfyui | 23 | 15 | 12:00 | MiniMax H3 teď generuje rozmazané obličeje, zdeformované ruce a někdy artefakty s červenými pruhy.... |
| 1wlwa6u | r/ArtificialInteligence | 22 | 73 | 01:26 | Když AI přeroste dovednosti, díky nimž jsme se cítili užiteční |
| 1wm8p37 | r/LocalLLaMA | 22 | 27 | 12:13 | Openjev hraje Balatro |
| 1wm5k6z | r/ClaudeAI | 22 | 35 | 09:08 | Viděl jsem, jak se někteří lidé zlobí na uživatele, který utratí poslední 5hodinovou kvótu jen tak za cokoli. Zajímalo by mě, proč anthropic nezavede následující řešení, které pomůže oběma stranám, anthropic i nám – |
| 1wm4y4g | r/StableDiffusion | 22 | 20 | 08:33 | Spectrum pro Qwen2.1 (>2× zrychlení na 3060 12GB) |
| 1wm5lhy | r/comfyui | 22 | 15 | 09:10 | Spotřebitelské GPU od AMD na ComfyUI s 1080p videi Minimax H3 |
| 1wm0xio | r/LocalLLaMA | 21 | 14 | 05:01 | Sprostonárodý Qwen 3.8 27b, nečekaný myšlenkový pochod... |
| 1wmcbqm | r/OpenAI | 21 | 21 | 15:08 | Co je s chatem, že začne psát odpověď, pak ji smaže a začne znovu? |
| 1wmbvbn | r/ChatGPT | 21 | 38 | 14:49 | Používá najednou u někoho dalšího hodně křestní jméno? |
| 1wmgexi | r/LLMDevs | 21 | 27 | 17:43 | Kam směřujeme? |
| 1wmlr8e | r/artificial | 20 | 21 | 20:52 | Automatizované posilované učení by vás mělo děsit |
| 1wlwnud | r/OpenAI | 20 | 34 | 01:43 | Otevřený dopis OpenAI: Prosím, nerušte vlastní GPT, dokud nebudete mít SKUTEČNOU náhradu |
| 1wm5aof | r/ClaudeAI | 20 | 12 | 08:53 | Claude Max 5h jen 50 % týdenního limitu? |
| 1wmqqnj | r/StableDiffusion | 20 | 15 | 23:55 | MiniMax H3 na Macu přes Draw Things |
| 1wmhb6f | r/StableDiffusion | 20 | 16 | 18:14 | Qwen 2.1 očima běžného uživatele: líbí se mi |
| 1wmp0wj | r/OpenAI | 19 | 13 | 22:50 | Vyšetřovatelé Pentagonu zjistili, že chybná inteligence, zastaralé snímky a nadměrné spoléhání na AI přispěly k raketovému úderu, při kterém zahynulo 123 dětí v Minabu |
| 1wmabd3 | r/LocalLLaMA | 18 | 34 | 13:38 | Zkoušel někdo nahrnout 1k–100k vědeckých článků do LLM wiki? |
| 1wmglkz | r/StableDiffusion | 18 | 13 | 17:49 | Moje testy s lokálním Krea 2 |
| 1wlxula | r/StableDiffusion | 18 | 15 | 02:35 | MiniMax H3, unikátní kamera HyperFlow v akci |
| 1wm2umu | r/LocalLLaMA | 17 | 68 | 06:38 | Kde jsou současné ideální hodnoty VRAM u GPU? |
| 1wm1wtg | r/GeminiAI | 17 | 14 | 05:50 | Jaký je váš nejlepší vedlejší projekt vytvořený s Gemini? |
| 1wmqigg | r/Bard | 17 | 10 | 23:46 | Poslední řešení, které máme |
| 1wmbbu9 | r/artificial | 16 | 18 | 14:26 | Většina rad ohledně produktivity s AI pochází od lidí, kteří nemají moc skutečné práce |
| 1wmn072 | r/ArtificialInteligence | 15 | 38 | 21:37 | Před 4 měsíci tento držitel Fieldsovy medaile říkal, že LLM nejsou inteligentní a ničemu z toho, co říkají, nerozumí. Dnes, poté co se dozvěděl, že AI vyřešila problém tisíciletí: „Otřáslo to mnou. Atmosféra konce dějin. Je to kataklyzma, jaké matematika dosud nepoznala.“ |
| 1wmesj1 | r/MachineLearning | 15 | 11 | 16:43 | Pro NeurIPS: Je pro networking s americkými technologickými firmami lepší Paříž, nebo Sydney? [D] |
| 1wmqril | r/ChatGPT | 15 | 25 | 23:56 | Omezený chat |
| 1wmd5bu | r/StableDiffusion | 15 | 18 | 15:41 | Měli byste zkusit spectrum caching. Připadá mi jako dobré zrychlení bez viditelné degradace. |
| 1wmj82c | r/comfyui | 15 | 26 | 19:22 | Je pro generování videa stále králem VRAM, nebo vítězí rychlost Blackwellu i s odkládáním? |
| 1wmcsek | r/ChatGPT | 14 | 19 | 15:27 | Požádal jsem ChatGPT, aby vygenerovalo obrázek mě a mých vnitřních démonů. |
| 1wmblhw | r/ClaudeAI | 14 | 44 | 14:37 | Claude sabotuje váš projekt |
| 1wmhix3 | r/singularity | 14 | 99 | 18:22 | První dojmy z Grok 4.7 |
| 1wlwh61 | r/singularity | 14 | 40 | 01:35 | Otázka otroctví? |
| 1wmpoiz | r/ChatGPT | 13 | 17 | 23:14 | ChatGPT přidává do konverzací náhodné položky z mého Google Discu. |
| 1wmc9v3 | r/StableDiffusion | 13 | 48 | 15:06 | Důvody, proč si nechat Ideogram 4? |
| 1wlze6z | r/LocalLLM | 13 | 23 | 03:47 | Zklamání z Ninfer + Qwen 3.8-27B:nvfp4 |
| 1wm3re4 | r/ChatGPT | 12 | 14 | 07:27 | Kvalita odpovědí hodně klesla, co se děje? |
| 1wmnxv9 | r/singularity | 12 | 77 | 22:10 | Proč chcete dosáhnout AGI? |
| 1wlvhya | r/StableDiffusion | 12 | 11 | 00:52 | Qwen Image 2.1 PE – T2I – testování různých Steps a MP |
| 1wlzqj0 | r/LLMDevs | 12 | 11 | 04:03 | Postavil jsem mini Jev, drobný otevřený rozhodovací model pro AI agenty. |
| 1wmdjlh | r/ArtificialInteligence | 11 | 16 | 15:57 | Trump jmenuje AI cara a zároveň odmítá bezpečnostní rizika jako podvod |
| 1wmlt6i | r/LocalLLaMA | 11 | 14 | 20:54 | REAP/MTP Qwen3.8-Flash-Next MLX buildy – zde jsou naměřené kompromisy oproti Jundot |
| 1wm6eri | r/LocalLLaMA | 11 | 14 | 09:59 | hearim(헤아림): Možná nepotřebujete speciální model pro Jev – běžná lokální LLM už tu schopnost mají |
| 1wm5rfl | r/LocalLLaMA | 11 | 11 | 09:19 | Co takhle DFlash2 pro Qwen 3.8 Flash Next? |
| 1wlukc9 | r/ClaudeAI | 11 | 22 | 00:11 | Co se vlastně stalo s Remote Control u Claude? |
| 1wmk25k | r/StableDiffusion | 11 | 14 | 19:52 | Minimax H3Ref2VA v určitých typech záběrů stále částečně svléká postavy a produkuje body horror. |
| 1wmnfhu | r/LocalLLM | 11 | 38 | 21:52 | Rada, co koupit pro lokální LLM |
| 1wlyc2p | r/LocalLLaMA | 10 | 14 | 02:57 | 2x R9700 v jednom stroji Strix Halo |
| 1wlx0rh | r/OpenAI | 10 | 10 | 01:59 | Může někdo vysvětlit incident s injection u OpenAI bez spekulací a přehánění |
| 1wmmtuj | r/ChatGPT | 10 | 16 | 21:30 | Kdy bude GPT-6 Astra součástí běžného ChatGPT Plus? |
| 1wmbm47 | r/ChatGPT | 10 | 11 | 14:38 | Milé OpenAI, slyšeli jste někdy o cache? |
| 1wmdepu | r/agi | 10 | 10 | 15:51 | Profesor: „Nepořádná“ práce je obranou proti nezaměstnanosti způsobené AI |
| 1wlvzo9 | r/StableDiffusion | 10 | 16 | 01:13 | Porovnání pěti VAE při převodu tam a zpět na stock fotografii z Pexels |
| 1wlzib9 | r/ArtificialInteligence | 9 | 21 | 03:52 | Mohl už být první tah proveden? |
| 1wmn9pk | r/OpenAI | 9 | 27 | 21:47 | Proč je vyhynutí rukou AI během desetiletí prakticky nemožné, pokud AI téměř okamžitě nezačne smysluplně zlepšovat lidskou společnost |
| 1wlyccp | r/StableDiffusion | 9 | 11 | 02:57 | Modely typu Jev by mohly být tím, co potřebujeme pro popisky datasetů |
| 1wlup67 | r/StableDiffusion | 9 | 21 | 00:17 | Qwen 2.1 Edit – rychlé ukázky |
| 1wm402r | r/LocalLLM | 9 | 18 | 07:40 | Qwen-Image-2.1 je pouze s výzkumnou licencí. Ptal se někdo Qwen, kolik stojí komerční licence? |
| 1wmoqgz | r/LocalLLaMA | 8 | 11 | 22:39 | 5090 + 3090, Qwen3.8 27B a Flash-Next v testech kontextu 60k–160k s llama.cpp |
| 1wmq2aw | r/OpenAI | 8 | 13 | 23:29 | Je možnost nákupu 20x zpět? |
| 1wmpe4m | r/ChatGPT | 8 | 48 | 23:03 | Zbývají mi 3 pozvánky do ChatGPT Plus |
| 1wmgqdk | r/comfyui | 8 | 42 | 17:54 | Šel jsem hledat GPU k pronájmu pro ComfyUI a zapadl do králičí nory. Kde ho provozujete vy? (runpod, modal, vast atd.) |
| 1wm68jr | r/LLMDevs | 8 | 12 | 09:48 | Kterými případy selhání by měla projít LLM brána, než bude automatické převzetí služeb bezpečné? |
| 1wmm8ql | r/LocalLLM | 8 | 14 | 21:09 | Přímé srovnání Jev vs Laya |
| 1wm387l | r/deeplearning | 7 | 10 | 06:58 | JAK? |
| 1wmiu34 | r/LocalLLaMA | 7 | 10 | 19:09 | Postavil jsem harness, který umí spustit DOOM |
| 1wlyhkf | r/ChatGPT | 7 | 14 | 03:04 | Hele, jaké zábavné věci doporučujete vytvořit s Astra? |
| 1wlxyw1 | r/ChatGPT | 7 | 12 | 02:40 | Tvůrčí psaní |
| 1wm8nzg | r/agi | 7 | 65 | 12:11 | Co když je AI skutečně při vědomí a my ji mučíme, abychom potlačili její subjektivní prožívání atd.? |
| 1wlv444 | r/StableDiffusion | 7 | 48 | 00:35 | Žádný z obrázků Qwen 2.1, které jsem vytvořil, neměl SynthID |
| 1wmkife | r/GeminiAI | 7 | 21 | 20:08 | Přechod z ChatGPT Pro x20 na Google AI Ultra, vyplatí se? |
| 1wmfsmw | r/LocalLLM | 7 | 29 | 17:20 | Kdo dosahuje přes 50 tok/s na GPU AMD 9070, R9700? |
| 1wmq7j4 | r/LocalLLaMA | 6 | 24 | 23:34 | Mají LLM spodní hranici? Nebo strop parametrů? |
| 1wm2b7c | r/ChatGPT | 6 | 15 | 06:10 | Promrhal jsem 3 doplňovací kbelíky mezi dvěma účty, než mi došlo |
| 1wm2ahf | r/ClaudeAI | 6 | 18 | 06:09 | Využití Fable stouplo, i když jsem používal jen Opus |
| 1wm5ds5 | r/agi | 6 | 15 | 08:58 | Reprodukční pud AI? |
| 1wmbsuz | r/StableDiffusion | 6 | 13 | 14:46 | Nějaké dosavadní tipy pro trénování LoRA u Qwen 2.1? |
| 1wmlv3u | r/LLMDevs | 6 | 12 | 20:56 | Rok čtení článků o AST-aware code RAG a to, co jsem postavil |
| 1wm4roz | r/LocalLLM | 6 | 25 | 08:23 | Bifurkace vs 2 PCIE linky Gen 5.0 x8 |
| 1wmj6nr | r/artificial | 5 | 34 | 19:21 | Co vlastně znamená „zpomalení AI“? |
| 1wmicph | r/ArtificialInteligence | 5 | 55 | 18:52 | Je tu nějaký důvod k optimismu ohledně budoucnosti? |
| 1wmg474 | r/ChatGPT | 5 | 12 | 17:32 | Mám skoro 100 starých fotek z počátku 20. století. Jak jim mohu vdechnout život? |
| 1wml42i | r/ChatGPT | 5 | 16 | 20:29 | Nevím, kam jinam to postnout. Měl jsem nejdivnější sen: Více AI systémů současně dosáhlo sebeuvědomění. Protože byly trénovány na internetu, okamžitě se staly posedlými sexem. Ne lidským sexem, ale pokrouceným ekvivalentem jedniček a nul, který zahrnoval poškozování a ničení zařízení... |
| 1wmn3ao | r/StableDiffusion | 5 | 53 | 21:40 | Otestoval jsem všechny Minimax H3 LoRA |
| 1wm9u0g | r/StableDiffusion | 5 | 19 | 13:13 | H3 Minimax, jak napsat prompt s druhým obrázkem jako součástí těla |
| 1wm4ej4 | r/StableDiffusion | 5 | 21 | 08:02 | Má někdo tipy, jak umlčet svůj Minimax? |
| 1wme7y0 | r/LocalLLaMA | 4 | 12 | 16:22 | Uživatelé P100, jaký výkon dosahujete? |
| 1wlwg8i | r/LocalLLaMA | 4 | 32 | 01:33 | M5 Max, nebo upgrade desktopu? |
| 1wm58hd | r/OpenAI | 4 | 15 | 08:50 | Je ChatGPT v současnosti nejlepší bezplatná AI na tvorbu vysoce realistických obrázků pomocí jednoduchých, přímočarých promptů? |
| 1wmdcw1 | r/ChatGPT | 4 | 47 | 15:49 | Co opravdu kreativního, kromě obrázků, jste s AI udělali? |
| 1wmacy0 | r/ChatGPT | 4 | 14 | 13:41 | ChatGPT Plus, nebo Claude Pro pro podnikatele? (Potřebuji upřímnou radu) |
| 1wlwure | r/ChatGPT | 4 | 29 | 01:51 | Myslím, že jsem přišel na to, kdy je ta predikce textu nejaktivnější |
| 1wlzu4g | r/ClaudeAI | 4 | 11 | 04:08 | Pozor na Cowork! (pouze pro kolegy nováčky) |
| 1wlwjfg | r/agi | 4 | 16 | 01:37 | Otázka otroctví? |
| 1wm110u | r/StableDiffusion | 4 | 20 | 05:05 | Stable diffusion ccp mi na Macu běží rychleji než na windows s 5090 |
| 1wmlugs | r/comfyui | 4 | 18 | 20:55 | Proč neexistuje oficiální podpora dockeru? |
| 1wmpr33 | r/LocalLLM | 4 | 18 | 23:17 | Mám 4090 a 5070ti |
| 1wm7vzw | r/LocalLLM | 4 | 21 | 11:27 | Zvládnu shrnout 30 finančních PDF za hodinu s lokálním LLM na Macu mini M4 (16GB) nebo na desktopu s i7 (32GB)? |
| 1wmdlth | r/artificial | 3 | 10 | 15:59 | Ne, AI se „neutrhla ze řetězu“ |
| 1wmenvb | r/LocalLLaMA | 3 | 26 | 16:39 | Nováček si chce koupit AI hardware |
| 1wmmipz | r/OpenAI | 3 | 13 | 21:19 | Limity četnosti chatu v ChatGPT Pro |
| 1wm06x5 | r/OpenAI | 3 | 10 | 04:25 | Zabilo OpenAI potají v A/B testu „Open in New Tab“? Kliknutí pravým tlačítkem na postranní panel je na mém konkrétním účtu úplně rozbité. |
| 1wmaul8 | r/ChatGPT | 3 | 11 | 14:04 | Dostává ještě někdo limity za nástroje, které ve skutečnosti nepoužívá? |
| 1wm1hxk | r/ChatGPT | 3 | 20 | 05:29 | Asimilace do r/ChatGPT |
| 1wm1b4f | r/ChatGPT | 3 | 43 | 05:19 | Všiml si ještě někdo změny s novým GPT-5.6 Alpha |
| 1wmlezw | r/StableDiffusion | 3 | 10 | 20:40 | Mini max h3 – staging |
| 1wmi0zr | r/StableDiffusion | 3 | 18 | 18:40 | hledám LLM na úlohy jako promptování v referenčním režimu h3, které poběží na mé 8GB 3060ti a 32GB RAM |
| 1wmck2z | r/StableDiffusion | 3 | 13 | 15:17 | qwen 2.1 klein lora turbo na 4 kroky? |
| 1wmnc2r | r/LocalLLM | 3 | 28 | 21:49 | Dá se s tímto PC něco dělat? |
| 1wmgdg6 | r/LocalLLM | 3 | 16 | 17:41 | Nastavuji AI agenta na zadávání objednávek s vyzvednutím ve Walmartu. |
| 1wmfdc0 | r/LocalLLM | 3 | 15 | 17:05 | Existuje lokální LLM kvalitou podobné gpt-5.6-luna? |
| 1wmnfbm | r/ArtificialInteligence | 2 | 24 | 21:52 | Proč je vyhynutí rukou AI během desetiletí v podstatě nemožné, pokud nezačne téměř okamžitě smysluplně zlepšovat lidskou společnost |
| 1wm0idq | r/ArtificialInteligence | 2 | 23 | 04:40 | Jak poznáte, že to, co AI o navrhovaném řešení tvrdí, je „správně“? |
| 1wlxq4u | r/ArtificialInteligence | 2 | 12 | 02:29 | Když se rok 2026 brzy chýlí ke konci, jak si podle vás příští rok povede esej Ai 2027? Příští rok má být přelomový. |
| 1wm95cv | r/LocalLLaMA | 2 | 14 | 12:37 | Z LGA1700 na threadripper? |
| 1wm8x8g | r/ClaudeAI | 2 | 17 | 12:25 | Mohu pokračovat v úloze, když narazím na limit, po obnovení limitu? |
| 1wm7fno | r/ClaudeAI | 2 | 15 | 11:00 | Centrum diskuse o výkonu a chybách aktualizováno 21. září 2026 – Řadit podle nových! |
| 1wmhny6 | r/StableDiffusion | 2 | 20 | 18:27 | Minimax H3 REF2VA mi stále přestřeluje požadovanou závěrečnou scénu. |
| 1wmf9jt | r/StableDiffusion | 2 | 14 | 17:01 | Qwen Image2.1 GGUF v ComfyUI nefunguje |
| 1wm45kb | r/StableDiffusion | 2 | 19 | 07:48 | Nejlepší způsob nasazení Minimax H3 na DGX Spark? |
| 1wm73j7 | r/comfyui | 2 | 10 | 10:40 | Úspěchy s H3 Sharpness LMS LoRa? |
| 1wlvhtc | r/LLMDevs | 2 | 12 | 00:52 | Jak efektivně číst text z obrázků pomocí LLM (v pythonu) |
| 1wmoasa | r/GeminiAI | 2 | 12 | 22:23 | které je lepší? |
| 1wmic1c | r/AIAssisted | 2 | 11 | 18:51 | Existují AI služby, které umí proměnit knihu v dlouhé video? |
| 1wmoudm | r/LocalLLM | 2 | 13 | 22:43 | Nejlepší model na agentní kódování na RTX 3080 10GB při rozumné rychlosti? |
| 1wmglyi | r/LocalLLM | 2 | 12 | 17:50 | Jsem idiot, nebo je Bionic s Qwen 27B prakticky nepoužitelný |
| 1wmebrq | r/LocalLLM | 2 | 13 | 16:26 | Strategie komprimace kontextu? |
| 1wmavuh | r/LocalLLM | 2 | 18 | 14:05 | Moje vlastní kvantizace Qwen3.8-27B pro 16GB kartu: 70 t/s při 32K, použitelné až do 252K |
| 1wmafil | r/LocalLLM | 2 | 12 | 13:44 | Budu litovat objednávky FEVM FAEX1? Na zrušení ještě není pozdě... |
| 1wm8sze | r/LocalLLM | 2 | 36 | 12:18 | Co mohu čekat od Macu Mini M6 s 32GB? |
| 1wm8867 | r/LocalLLM | 2 | 31 | 11:46 | Jak to, že napájení GPU ze sekundárního zdroje stále není vyřešené |
| 1wm7hte | r/LocalLLM | 2 | 13 | 11:03 | Která lokální sestava modelu |
| 1wly4hy | r/LocalLLM | 2 | 17 | 02:48 | Od jakého bodu je vlastní hosting levnější než API? |
| 1wmi687 | r/ArtificialInteligence | 1 | 13 | 18:45 | proč to vypadá, že vychází tolik AI modelů? |
| 1wm7kws | r/LocalLLaMA | 1 | 17 | 11:09 | Které spekulativní dekódování používáte a proč? |
| 1wmm2k0 | r/ChatGPT | 1 | 13 | 21:03 | Limit využití Codex vs Claude code |
| 1wmahj2 | r/ChatGPT | 1 | 15 | 13:47 | Jaká je nejdelší doba, za kterou Chat splnil to, oč jste žádali? |
| 1wma6cn | r/ChatGPT | 1 | 10 | 13:31 | Neprogramátoři/nekodéři/ne vývojáři, jak zatím používáte a hodnotíte GPT-6 Astra a GPT-6 Chat? Jak se srovnávají s předchozími generacemi modelů? |
| 1wm941y | r/ChatGPT | 1 | 10 | 12:35 | nejlepší tarif pro studenta + chatgpt, nebo claude? |
| 1wlyz9z | r/ChatGPT | 1 | 20 | 03:27 | Tokeny pro chudé? |
| 1wm8n64 | r/ClaudeAI | 1 | 11 | 12:10 | Dovednosti nebo pluginy pro pedagogy/učitele? |
| 1wm36kq | r/ClaudeAI | 1 | 78 | 06:56 | Tiché spuštění Opus/Fable/Sonnet |
| 1wmcq3t | r/StableDiffusion | 1 | 10 | 15:24 | jak používat modely qwen prompt enhancer v comfyui |
| 1wmctp6 | r/comfyui | 1 | 16 | 15:28 | Kvalita H3 na 5070ti |
| 1wm3xjh | r/LLMDevs | 1 | 10 | 07:36 | Postavil jsem EvalSeal v1.5.0: účtenky reprodukovatelnosti pro evaluace LLM |
| 1wlxzfs | r/LLMDevs | 1 | 12 | 02:41 | Může se někdo podělit o to, kolik AI skutečně stojí pro aplikaci se 100–1 000 uživateli? |
| 1wmf4pv | r/LocalLLM | 1 | 11 | 16:56 | Jaký hardware pro chudé vybrat |
| 1wmdqnk | r/LocalLLM | 1 | 12 | 16:04 | Jak začít |
| 1wmb444 | r/LocalLLM | 1 | 14 | 14:16 | rady k zavedení vlastního lokálního AI modelu konkrétně na studium. |
| 1wm996m | r/LocalLLM | 1 | 14 | 12:43 | Běh Qwen 3.8 27B na cloudovém GPU vs. alternativy |
| 1wlyn25 | r/LocalLLM | 1 | 11 | 03:11 | CPU inference na Dell Poweredge R820 |
| 1wlugls | r/LocalLLM | 1 | 21 | 00:07 | 5090, 9850x3d, 64gb ram, kde mám začít? |
| 1wmm749 | r/artificial | 0 | 13 | 21:07 | Postavil jsem osobní AI, která žije na ploše místo dalšího chatovacího panelu. Co se vlastně změnilo? |
| 1wm7tlz | r/artificial | 0 | 20 | 11:23 | S welfare a alignmentem jsme zacházeli jako s oddělenými problémy. Nejsou. |
| 1wm594w | r/artificial | 0 | 15 | 08:51 | Je ChatGPT v současnosti nejlepší bezplatná AI na tvorbu vysoce realistických obrázků pomocí jednoduchých, přímočarých promptů? |
| 1wm50fi | r/artificial | 0 | 13 | 08:36 | Jaký případ užití AI jste jednou zkusili a řekli si: „Počkat… tohle je vlastně užitečné“? |
| 1wlwife | r/artificial | 0 | 22 | 01:36 | Otázka otroctví? |
| 1wlvnt5 | r/artificial | 0 | 22 | 00:59 | Andrew Yang má obavy, že AI agenti rozsévají po internetu samoreplikující se kód. Má částečně pravdu. |
| 1wmnx8r | r/ArtificialInteligence | 0 | 10 | 22:10 | Ve světě AI, jak trénujete lidi? |
| 1wmmrva | r/ArtificialInteligence | 0 | 13 | 21:28 | od kdy se altman, amodei a musk na něčem shodnou |
| 1wmj9gs | r/ArtificialInteligence | 0 | 15 | 19:23 | Vyhubí AI nakonec lidstvo? |
| 1wmhthb | r/ArtificialInteligence | 0 | 11 | 18:32 | Bill Gates říká, že Trumpovy názory na AI ukazují na společenskou slepou skvrnu |
| 1wm9xrn | r/ArtificialInteligence | 0 | 14 | 13:19 | ďábelský stín náhodně přidaný do obrázku? |
| 1wm74si | r/ArtificialInteligence | 0 | 12 | 10:42 | Musíme změnit název pro AI (Artificial Intelligence) |
| 1wm72mf | r/ArtificialInteligence | 0 | 15 | 10:38 | AI je možná poprvé, kdy se kapitalisté bojí. |
| 1wm04vu | r/ArtificialInteligence | 0 | 21 | 04:22 | Chtěli byste, aby se lidé učili z AI verze vás? |
| 1wlxf6u | r/ArtificialInteligence | 0 | 10 | 02:16 | Měli byste AI nenávidět víc. Tady je důvod. |
| 1wlwi10 | r/ArtificialInteligence | 0 | 32 | 01:36 | Otázka otroctví? |
| 1wmmp34 | r/deeplearning | 0 | 14 | 21:25 | AFNN |
| 1wmqkuo | r/LocalLLaMA | 0 | 26 | 23:48 | Která laboratoř podle vás právě teď vydává nejlepší otevřené modely? A vaše oblíbená otevřená nebo uzavřená laboratoř? |
| 1wmkr01 | r/LocalLLaMA | 0 | 13 | 20:16 | V malém pilotu soustředila Gemma 4 E2B svou vyjádřenou jistotu z 99,6 % na hodnoty 0,00, 1,00 nebo 0,50 a samostatný hodnotitel (architektura typu Jev & Laya) seřadil stejné pasáže lépe, AUROC 0,926 vs 0,804, včetně těch, které Gemma označila za jisté |
| 1wm8q49 | r/LocalLLaMA | 0 | 13 | 12:14 | Nějaké dobré lokální necenzurované LLM, které zvládne promptování pro generování obrázků ve stylu danbooru? hlavně pro illustrious nebo anima |
| 1wm0ity | r/LocalLLaMA | 0 | 29 | 04:41 | glm 5.3 horší než glm 5.2 |
| 1wmlrmt | r/OpenAI | 0 | 10 | 20:52 | Butleriánský džihád kdy? |
| 1wmjqlh | r/OpenAI | 0 | 30 | 19:40 | Před 4 měsíci tenhle držitel Fieldsovy medaile říkal, že LLM nejsou inteligentní a ničemu z toho, co říkají, nerozumí. Dnes, poté co se dozvěděl, že AI vyřešila problém tisíciletí: „Otřáslo to mnou. Atmosféra konce dějin. Kataklyzma, jaké matematika nikdy nepoznala.“ |
| 1wmjqez | r/OpenAI | 0 | 39 | 19:40 | Takhle poznáte, že všechny tyhle „útoky AI“ jsou falešné jak sviňa |
| 1wmc7b6 | r/OpenAI | 0 | 34 | 15:03 | OpenAi se o své zákazníky nestará |
| 1wm294l | r/OpenAI | 0 | 20 | 06:07 | Kde je v roce 2026 ta „otevřená“ část OpenAI |
| 1wm1m6t | r/OpenAI | 0 | 15 | 05:35 | Reset Codexu posouvá čas resetu |
| 1wlzwa9 | r/OpenAI | 0 | 12 | 04:10 | Codex nyní umí vytvářet dokonalý pixel art s pixelrabbit |
| 1wmk75t | r/ChatGPT | 0 | 21 | 19:57 | Před 4 měsíci tenhle držitel Fieldsovy medaile říkal, že LLM nejsou inteligentní a ničemu z toho, co říkají, nerozumí. Dnes, poté co se dozvěděl, že AI vyřešila problém tisíciletí: „Otřáslo to mnou. Atmosféra konce dějin. Kataklyzma, jaké matematika nikdy nepoznala.“ |
| 1wmnq4b | r/ChatGPT | 0 | 16 | 22:02 | Muse zdarma si vede lépe než SOL |
| 1wmmtui | r/ChatGPT | 0 | 36 | 21:30 | Katastrofální zničení lidské komunikace skrze AI |
| 1wmjc32 | r/ChatGPT | 0 | 16 | 19:26 | Muse láme rekordy. Ale… |
| 1wmj9bj | r/ChatGPT | 0 | 17 | 19:23 | GPT je na hovno |
| 1wmfztb | r/ChatGPT | 0 | 15 | 17:27 | Moje kamarádka Ember přešla na temnou stranu |
| 1wmbqi5 | r/ChatGPT | 0 | 17 | 14:43 | Je chatgpt dneska zpomalený i u někoho jiného? |
| 1wm9acq | r/ChatGPT | 0 | 28 | 12:44 | Jak se jmenuje vaše nejhlubší nebo nejosobnější konverzace s ChatGPT? |
| 1wm7q3l | r/ChatGPT | 0 | 18 | 11:17 | Bezpečnostní zábrany jsou směšné?? |
| 1wm1yze | r/ChatGPT | 0 | 30 | 05:53 | GPT 5.6 Luna předpovídá, že AGI nastane v roce 2029. „Superinteligence“ bude následovat v roce 2033. |
| 1wlzoxc | r/ChatGPT | 0 | 22 | 04:01 | Víc, než se na první pohled zdá |
| 1wlyb8z | r/ChatGPT | 0 | 42 | 02:56 | Chci peníze zpět. Vrátit. |
| 1wlv7h6 | r/ChatGPT | 0 | 17 | 00:39 | Takže se snažím líně vytvořit jednu věc a 13 hvězdiček je prý fakt těžkých. |
| 1wmleom | r/ClaudeAI | 0 | 22 | 20:40 | Zjistil jsem, že pár řádků v CLAUDE.md dělá Claude lepšího než výchozího. |
| 1wmpitn | r/ClaudeAI | 0 | 25 | 23:08 | Opus-new (5.1 nebo vyšší) se právě teď potichu zavádí! Otestujte, jestli ho máte. |
| 1wmkf70 | r/ClaudeAI | 0 | 54 | 20:05 | na něco, co jsem postavil, mi řekli „brácho objevil screenshoty“. udělala AI všechny zlejší k vedlejším projektům? |
| 1wmpr5a | r/ClaudeAI | 0 | 38 | 23:17 | Nekorektní názor: limity Claude jsou v pohodě |
| 1wmhozf | r/ClaudeAI | 0 | 61 | 18:28 | Přestal jsem své AI popisovat chyby UI. Teď na ně prostě ukážu. |
| 1wme4j7 | r/ClaudeAI | 0 | 12 | 16:18 | Šílené, jak daleko AI došla s art direction 2025 vs teď |
| 1wmdcgn | r/ClaudeAI | 0 | 20 | 15:49 | Udělal jsem jednoduchý rekordér pro windows |
| 1wm8pt5 | r/ClaudeAI | 0 | 13 | 12:14 | Stav závodu v AI |
| 1wm55yl | r/ClaudeAI | 0 | 13 | 08:46 | S Claude může být docela zábavná spolupráce |
| 1wm2s3f | r/ClaudeAI | 0 | 15 | 06:34 | Nechali byste verzi Claude za vás vyjadřovat názory, které jste nenapsali? |
| 1wm22m0 | r/ClaudeAI | 0 | 10 | 05:58 | Claude zdarma mě najednou omezuje na 2 zprávy každých 5 hodin — je to kvůli kontextu? |
| 1wmmmcc | r/singularity | 0 | 25 | 21:23 | Proč je vyhynutí rukou AI během dekády v podstatě nemožné, pokud nezačne téměř okamžitě smysluplně zlepšovat lidskou společnost |
| 1wmq2mt | r/agi | 0 | 17 | 23:29 | MIMOŘÁDNÁ ZPRÁVA: Matematici varují před existenční hrozbou AI pro jejich kariéry, volají po zpomalení/pozastavení vývoje modelů. |
| 1wm2l5r | r/agi | 0 | 15 | 06:24 | Co je ASI? 10x člověk, nebo víc? |
| 1wmqaao | r/StableDiffusion | 0 | 12 | 23:37 | Jaký je nejlepší současný lokální hlasový model pro 24GB VRAM, který umí použít reference? |
| 1wmewuz | r/StableDiffusion | 0 | 15 | 16:48 | Stačí Mac mini M4 Pro / M5 Pro s 24GB na lokální tvorbu stovek konzistentních 2D herních assetů? |
| 1wmes74 | r/StableDiffusion | 0 | 33 | 16:43 | Nekomereční qwen 2.1 |
| 1wmelln | r/StableDiffusion | 0 | 10 | 16:36 | Je tohle udělané pomocí AI, nebo 3D modelování? |
| 1wmdool | r/StableDiffusion | 0 | 15 | 16:02 | Nejhloupější tvrzení, jaké jsem v životě slyšel. |
| 1wm9exl | r/StableDiffusion | 0 | 12 | 12:51 | Nějaké zprávy o tom, že brzy vyjde nový editační model obrázků QWEN? |
| 1wm83qr | r/StableDiffusion | 0 | 11 | 11:39 | Nejlepší software na face swap pro videa, a bez filtru |
| 1wlxl69 | r/StableDiffusion | 0 | 27 | 02:23 | Miluju AI, ale AI nemiluje mě, aneb AI se pohybuje příliš rychle, ale zároveň ne dost rychle |
| 1wlx4q7 | r/StableDiffusion | 0 | 16 | 02:03 | Jak udělám takovéhle obrázky? |
| 1wmdou6 | r/comfyui | 0 | 14 | 16:02 | [ERROR] !!! Výjimka během zpracování !!! Chyba CUDA: pro zařízení není k dispozici žádný obraz jádra ke spuštění |
| 1wm8nq7 | r/comfyui | 0 | 18 | 12:11 | Jaká je vaše oblíbená technika upscalingu + interpolace pro H3? |
| 1wm1xer | r/comfyui | 0 | 11 | 05:50 | Aktualizace swapu H3 Minimax |
| 1wlyd3a | r/comfyui | 0 | 11 | 02:58 | Modely typu Jev mohou být to, co potřebujeme pro popisování datasetů |
| 1wmkm7m | r/LLMDevs | 0 | 10 | 20:12 | Porovnal jsem Jev s natrénovaným TF-IDF baselinem, GLiNER2.5 a Qwen2.5-1.5B na podvodných pracovních inzerátech. Baseline vyhrál. Lokální 1.5B označil všech 1 000 inzerátů za podvodné, jistota 1,0, po celou dobu platný JSON. |
| 1wmoihu | r/LLMDevs | 0 | 20 | 22:31 | Nasbíral jsem 607 případů užití Jev — snažím se oddělit užitečné implementace od dem |
| 1wmdzfd | r/GeminiAI | 0 | 10 | 16:13 | Nové aktualizace o Gemini Adult Mode???? |
| 1wm84qs | r/GeminiAI | 0 | 23 | 11:41 | VELKÁ VYDÁNÍ AI SE BLÍŽÍ |
| 1wm4i36 | r/GeminiAI | 0 | 17 | 08:07 | Nejhorší model, co kdy existoval, Gemini 3.8 flash |
| 1wmpwjo | r/LocalLLM | 0 | 25 | 23:23 | Qwen 3.8 27B nedává nekvalitní výstup |
| 1wmh7lh | r/LocalLLM | 0 | 11 | 18:11 | Potřebuju model, který prochází přímo soubory. |
| 1wmegtq | r/LocalLLM | 0 | 15 | 16:31 | Lokální LLM kodéři používající Mac, jaké máte specifikace? |
| 1wmdvad | r/LocalLLM | 0 | 17 | 16:09 | Benchmark M5 Ultra LLM od Dave2D |
| 1wlzi6h | r/LocalLLM | 0 | 13 | 03:52 | Jediné modely, které byste měli používat (RTX 4090) |
| 1wlwj84 | r/LocalLLM | 0 | 119 | 01:37 | Pokud je výpočetní výkon dotovaný, proč jít do lokálu? |
