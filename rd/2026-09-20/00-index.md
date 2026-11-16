# AI novinky z Redditu — 20. 9. 2026

Rozsáhlý přehled diskusí a zpráv z AI subredditů publikovaných **20. 9. 2026 (Europe/Prague)** s **alespoň 10 komentáři**. Ke každému vybranému tématu je samostatný podrobný článek ve formátu Markdown, jehož název souboru i první řádek začíná **Reddit ID** (např. `1wlgrft.md`).

## Metodika

- **Zdroje:** 19 AI subredditů — r/artificial, r/ArtificialInteligence, r/MachineLearning, r/deeplearning, r/LocalLLaMA, r/LocalLLM, r/OpenAI, r/ChatGPT, r/ClaudeAI, r/singularity, r/agi, r/StableDiffusion, r/comfyui, r/LLMDevs, r/GeminiAI, r/Bard, r/OpenAIDev, r/AIAssisted, r/LLM.
- **Sběr:** veřejné Reddit JSON rozhraní načtené **z prohlížeče** (same-origin `fetch` na `www.reddit.com`; přímé volání z curl/read vrací `403`). Protože jde o ruční běh pro starší den, byl použit `top.json?t=week&limit=100` a stránkovaný `new.json` přes parametr `after`, dokud nejstarší `created_utc` neklesl pod začátek okna (max 8 stránek na subreddit). Pacing 2,5 s mezi requesty; bez jediného HTTP 403/429.
- **Počet requestů: 81** — 20× `top.json?t=week` (19 subredditů + 1 ověřovací dotaz), 35 stránek `new.json`, 26× `comments/<id>.json?limit=50&sort=top`.
- **Filtr:** `created_utc` v okně **20. 9. 2026 00:00–24:00 Europe/Prague** (19. 9. 22:00 UTC – 20. 9. 22:00 UTC; epochy 1789855200–1789941600), `num_comments >= 10`, bez stickied příspěvků. Nalezeno **4051** unikátních postů, z toho **812** v okně a **340** s alespoň 10 komentáři.
- **Výběr pro detailní články (26):** redakční filtr na *novinky* — vydání modelů a nástrojů, oznámení firem, žaloby a politika, hardwarové a vědecké zprávy, významné poruchy modelů. Diskusní a meme příspěvky jsou uvedeny v příloze, ale vlastní článek nemají.
- **Deduplikace:** 18 duplicitních postů bylo sloučeno do 7 témat (jeden model/událost ve více subredditech = jeden článek); ostatní posty jsou v článku uvedeny v sekci „Další diskuse k tématu“ s odkazy.
- **Podklady:** ke každému tématu balíček `_data/bundles/<id>.md` — metadata postu, selftext, stažený článek (celý text), cesta k obrázkům a max. 25 nejlepších komentářů (hloubka 0–1, tělo zkráceno na 1200 znaků). Celkem staženo **1224** komentářů, do balíčků použito **639**.
- **Vytěžení dat:** data z balíčků vytěžil **levný model (`opencode-go/muse-spark-1.3-contributor`)** jako subagent `reddit-extractor` (26 paralelních běhů) do `_data/extracts/<id>.json`; u screenshotů byl přepsán veškerý viditelný text. Články sestavil hlavní agent.
- **Stažené články:** apnews.com, cnbc.com, cleantechnica.com, globaltimes.cn (náhrada za reuters.com, které vrací HTTP 401), en.gamegpu.com, blog.keyvan.net, effort.news, irishstar.com, youtube.com (přepis videa C-SPAN), x.com (přes Nitter). Článek AP byl po kontrole podkladů dotažen prohlížečem, protože reader-mode vracel jen metadata; reuters.com nebyl dostupný (HTTP 401), a tak byl pro téma CXMT použit jako náhradní zdroj globaltimes.cn.
- **Obrázky:** 14 screenshotů (i.redd.it a galerie) v `_data/img/`.
- **Ověření:** u všech 26 článků bylo zkontrolováno, že první řádek je `# <reddit_id>`, že každá citace z extrakce se doslovně vyskytuje v balíčku nebo v přepisu obrázku a že žádné číslo z extrakce nemá oporu mimo podklady.

## Detailní články (26)

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1wlec9y](1wlec9y_chatgpt-vidi-za-mym-excelarskym-sesitem-muze-bez-tricka.md) | r/ChatGPT | 3155 | 489 | 13:14 | ChatGPT vidí za mým excelařským sešitem muže bez trička… |
| [1wl6wyn](1wl6wyn_je-cas-zrusit-predplatne-anthropic-podle-autora-tajne.md) | r/ClaudeAI | 1913 | 358 | 06:20 | Je čas zrušit předplatné – Anthropic podle autora tajně snižuje rozpočet na uvažování Clauda a tvrdí, že jde o stejný model |
| [1wlgrft](1wlgrft_qwen-image-2-1-vydan.md) | r/LocalLLaMA | 1792 | 368 | 15:12 | Qwen-Image-2.1 vydán! |
| [1wlns0q](1wlns0q_matematik-terence-tao-musime-zpomalit-ai-tempo-je-silene-a.md) | r/OpenAI | 1042 | 654 | 19:52 | Matematik Terence Tao: „Musíme zpomalit AI. Tempo je šílené a není žádný důvod být tak rychlí – vůbec žádný.“ |
| [1wl1ept](1wl1ept_chatgpt-misto-sady-ui-ikon-odmitl-vystup-kvuli-guardrails.md) | r/ChatGPT | 992 | 291 | 01:50 | ChatGPT místo sady UI ikon odmítl výstup kvůli guardrails na nahotu |
| [1wlnquc](1wlnquc_nemocnice-ktere-nejrychleji-zavadely-ai-mely-v-roce-2026.md) | r/singularity | 779 | 160 | 19:50 | Nemocnice, které nejrychleji zaváděly AI, měly v roce 2026 zatím nejmenší úmrtnost |
| [1wlh03i](1wlh03i_vytvorili-jsme-27b-model-pro-kreativni-psani-podava-stejne.md) | r/GeminiAI | 701 | 150 | 15:23 | Vytvořili jsme 27B model pro kreativní psaní. Podává stejně dobré výsledky jako Claude Fable 5 za 40× nižší cenu, s otevřenými váhami |
| [1wldnh8](1wldnh8_jensen-huang-mame-jit-tak-rychle-jak-jen-muzeme-bez-ohledu.md) | r/singularity | 617 | 74 | 12:36 | Jensen Huang: „Máme jít tak rychle, jak jen můžeme, bez ohledu na kohokoli jiného.“ |
| [1wlo52v](1wlo52v_zaloba-tvrdi-ze-anthropic-openai-spacexai-a-google-uzavrely.md) | r/LocalLLaMA | 565 | 122 | 20:05 | Žaloba tvrdí, že Anthropic, OpenAI, SpaceXAI a Google uzavřely nelegální dohodu o zpomalení AI |
| [1wljrn8](1wljrn8_gpt-6-astra-unreal-blender-rychlejsi-vyvoj-her.md) | r/ChatGPT | 474 | 79 | 17:18 | GPT-6 Astra + Unreal + Blender = rychlejší vývoj her |
| [1wl18d0](1wl18d0_gemini-flash-3-8-halucinoval-a-spamoval-slovo-shame.md) | r/GeminiAI | 443 | 66 | 01:42 | Gemini Flash 3.8 halucinoval a spamoval slovo „shame“ |
| [1wleg4w](1wleg4w_co-je-jev-a-k-cemu-se-pouziva.md) | r/LocalLLaMA | 438 | 322 | 13:20 | Co je JEV a k čemu se používá? |
| [1wlki0e](1wlki0e_chatgpt-nyni-predstihl-instagram-v-navstevnosti-webu.md) | r/OpenAI | 376 | 38 | 17:46 | ChatGPT nyní předstihl Instagram v návštěvnosti webu |
| [1wl1hlj](1wl1hlj_radeon-rx-10800-xt-muze-podle-clanku-gamegpu-predcit-rtx.md) | r/LocalLLaMA | 370 | 153 | 01:54 | Radeon RX 10800 XT může podle článku gamegpu předčit RTX 5090 o 15–25 % ve 4K hraní i v lokální AI |
| [1wl9c2o](1wl9c2o_cinska-cxmt-oznamuje-ze-jeji-nova-pametova-platforma-g5.md) | r/LocalLLaMA | 348 | 91 | 08:29 | Čínská CXMT oznamuje, že její nová paměťová platforma G5 vstupuje do sériové výroby |
| [1wlnmob](1wlnmob_licence-qwen-2-1-je-ta-nejhorsi.md) | r/StableDiffusion | 347 | 163 | 19:46 | Licence Qwen 2.1 je ta nejhorší! |
| [1wlmmf2](1wlmmf2_anthropic-vybral-accenture-jako-prvniho-embedded-evaluatora.md) | r/ClaudeAI | 344 | 87 | 19:08 | Anthropic vybral Accenture jako prvního „embedded evaluatora“, který má pomoci zavést Amodeiho plán zpomalení |
| [1wlnw0m](1wlnw0m_nadchazejici-tyden-by-mohl-prinest-nekolik-vydani-modelu.md) | r/singularity | 326 | 95 | 19:56 | Nadcházející týden by mohl přinést několik vydání modelů |
| [1wlt52p](1wlt52p_trump-je-brutalne-zesmesnovan-kvuli-podivne-snaze.md) | r/OpenAI | 325 | 75 | 23:13 | Trump je brutálně zesměšňován kvůli podivné snaze přejmenovat AI na „superior“ nebo „extreme“ inteligenci |
| [1wl7wps](1wl7wps_obama-o-umele-inteligenci-c-span-4-13-technologie-pry-neni.md) | r/singularity | 308 | 123 | 07:12 | Obama o umělé inteligenci (C-SPAN, 4:13): technologie prý není přeceňovaná, přeceňované mohou být komerční přínosy a valuace |
| [1wl56g2](1wl56g2_prosim-prestante-uz-s-temi-fp4-inference-enginy-proboha.md) | r/LocalLLaMA | 306 | 241 | 04:51 | Prosím, přestaňte už s těmi FP4 inference enginy, proboha |
| [1wl8kni](1wl8kni_pusobi-to-jako-marketingovy-trik-nemaji-v-umyslu-zpomalit.md) | r/ArtificialInteligence | 303 | 201 | 07:48 | Působí to jako marketingový trik. Nemají v úmyslu zpomalit, přinejlepším jde o „IPO-maxing“. Mezitím Čína: „já podporuji, abyste zpomalili VY, skvělý nápad, jen v tom pokračujte“ |
| [1wkz17p](1wkz17p_ai-modely-nehackuji-autonomne-incidenty-byly-narizene-a-slo.md) | r/artificial | 249 | 173 | 00:05 | AI modely nehackují „autonomně“ – incidenty byly nařízené a šlo o špatně zabezpečený test |
| [1wlsaoq](1wlsaoq_ternary-bonsai-2-27b-temer-spickovy-vykon-a-pritom-se-vejde.md) | r/LocalLLM | 223 | 148 | 22:41 | Ternary Bonsai 2 27B: téměř špičkový výkon a přitom se vejde do 8 GB VRAM |
| [1wlgu5y](1wlgu5y_remote-labor-index-aktualizovan-o-modely-fable-a-astra.md) | r/singularity | 205 | 45 | 15:16 | Remote Labor Index aktualizován o modely Fable a Astra |
| [1wl1djq](1wl1djq_izraelska-firma-irregular-ai-ma-byt-zapletena-do-nekolika.md) | r/singularity | 146 | 29 | 01:48 | Izraelská firma Irregular AI má být zapletena do několika nedávných „containment breach“ hacků |

## Sloučená témata (18 duplicitních postů)

| Hlavní článek | Další diskuse ke stejnému tématu |
|---|---|
| [1wlgrft](1wlgrft_qwen-image-2-1-vydan.md) | [1wlgh7c](https://www.reddit.com/r/StableDiffusion/comments/1wlgh7c/qwenimage21_weights_are_available_on_hugging_face/) (r/StableDiffusion, 586 b., 188 kom.); [1wlgee8](https://www.reddit.com/r/StableDiffusion/comments/1wlgee8/qwenqwenimage21_hugging_face/) (r/StableDiffusion, 86 b., 20 kom.); [1wlgb7k](https://www.reddit.com/r/StableDiffusion/comments/1wlgb7k/qwen_image_21_official_blog_post/) (r/StableDiffusion, 140 b., 38 kom.); [1wlgy69](https://www.reddit.com/r/comfyui/comments/1wlgy69/comfyorgs_qwenimage21_models_are_out_for_comfyui/) (r/comfyui, 102 b., 41 kom.); [1wlj8r2](https://www.reddit.com/r/StableDiffusion/comments/1wlj8r2/qwenimage21_gguf_is_out/) (r/StableDiffusion, 23 b., 17 kom.); [1wl4xp2](https://www.reddit.com/r/StableDiffusion/comments/1wl4xp2/qwen_image_21_releasing_tomorrow/) (r/StableDiffusion, 245 b., 56 kom.); [1wl592t](https://www.reddit.com/r/StableDiffusion/comments/1wl592t/10_hours_left_fo_qwen_image_21_public_open_source/) (r/StableDiffusion, 198 b., 45 kom.); [1wlfuw7](https://www.reddit.com/r/StableDiffusion/comments/1wlfuw7/qwen_image_21_more_detailed_tests/) (r/StableDiffusion, 503 b., 62 kom.); [1wlt9t9](https://www.reddit.com/r/StableDiffusion/comments/1wlt9t9/qwen_image_21_edit_tips/) (r/StableDiffusion, 480 b., 80 kom.); [1wlm7n6](https://www.reddit.com/r/StableDiffusion/comments/1wlm7n6/qwen_image_21_initial_testing/) (r/StableDiffusion, 197 b., 101 kom.) |
| [1wlnmob](1wlnmob_licence-qwen-2-1-je-ta-nejhorsi.md) | [1wlpf3r](https://www.reddit.com/r/StableDiffusion/comments/1wlpf3r/qwen_21_looks_like_we_dont_need_to_worry_much/) (r/StableDiffusion, 257 b., 30 kom.) |
| [1wlh03i](1wlh03i_vytvorili-jsme-27b-model-pro-kreativni-psani-podava-stejne.md) | [1wlhh08](https://www.reddit.com/r/LocalLLM/comments/1wlhh08/we_made_a_27b_model_for_creative_writing_performs/) (r/LocalLLM, 466 b., 132 kom.) |
| [1wlns0q](1wlns0q_matematik-terence-tao-musime-zpomalit-ai-tempo-je-silene-a.md) | [1wlnr87](https://www.reddit.com/r/ChatGPT/comments/1wlnr87/mathematician_terence_tao_we_have_to_slow_down_ai/) (r/ChatGPT, 841 b., 324 kom.); [1wlnqgd](https://www.reddit.com/r/ArtificialInteligence/comments/1wlnqgd/mathematician_terence_tao_we_have_to_slow_down_ai/) (r/ArtificialInteligence, 462 b., 503 kom.) |
| [1wkz17p](1wkz17p_ai-modely-nehackuji-autonomne-incidenty-byly-narizene-a-slo.md) | [1wlp9gd](https://www.reddit.com/r/ArtificialInteligence/comments/1wlp9gd/ai_models_are_not_hacking_autonomously/) (r/ArtificialInteligence, 132 b., 59 kom.) |
| [1wleg4w](1wleg4w_co-je-jev-a-k-cemu-se-pouziva.md) | [1wlciiq](https://www.reddit.com/r/LLMDevs/comments/1wlciiq/the_famous_car_wash_question_on_jev/) (r/LLMDevs, 167 b., 106 kom.); [1wltts7](https://www.reddit.com/r/LocalLLaMA/comments/1wltts7/would_you_buy_a_qwen3827b_taalas_chip_for_1k_if/) (r/LocalLLaMA, 406 b., 254 kom.) |
| [1wl6wyn](1wl6wyn_je-cas-zrusit-predplatne-anthropic-podle-autora-tajne.md) | [1wlj3gu](https://www.reddit.com/r/ClaudeAI/comments/1wlj3gu/something_is_wrong_with_usage_this_week/) (r/ClaudeAI, 580 b., 223 kom.) |

## Příloha: všech 340 příspěvků s 10+ komentáři

Všechny příspěvky v okně s alespoň 10 komentáři (bez stickied). Tabulka je řazena podle skóre. Titulky jsou uvedeny v původním znění z Redditu.

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1wlec9y | r/ChatGPT | 3155 | 489 | 13:14 | ChatGPT vidí muže bez trička za mou excelovou tabulkou… |
| 1wl6wyn | r/ClaudeAI | 1913 | 358 | 06:20 | Je čas zrušit předplatná – Anthropic potichu osekává rozpočet na uvažování Claude, a přitom tvrdí, že jde o stejný model |
| 1wlgrft | r/LocalLLaMA | 1792 | 368 | 15:12 | Qwen-Image-2.1 vydán! |
| 1wle3ks | r/ChatGPT | 1338 | 34 | 13:01 | Dvě různé strany internetu |
| 1wlhhqq | r/OpenAI | 1044 | 64 | 15:45 | Zestárlo jako mléko |
| 1wlns0q | r/OpenAI | 1042 | 654 | 19:52 | Matematik Terence Tao: „Musíme AI zpomalit. Tempo je šílené a není žádný důvod být tak rychlý – vůbec žádný.“ |
| 1wl1ept | r/ChatGPT | 992 | 291 | 01:50 | chatgpt vygeneroval porno, když jsem požádal o ikony uživatelského rozhraní |
| 1wle7ib | r/ArtificialInteligence | 981 | 59 | 13:07 | Dvě různé strany internetu |
| 1wlnr87 | r/ChatGPT | 841 | 324 | 19:51 | Matematik Terence Tao: „Musíme AI zpomalit. Tempo je šílené a není žádný důvod být tak rychlý – vůbec žádný.“ |
| 1wlnquc | r/singularity | 779 | 160 | 19:50 | Nemocnice, které nejrychleji zavedly AI, zaznamenaly zatím v roce 2026 nejméně úmrtí |
| 1wlhl35 | r/ArtificialInteligence | 747 | 92 | 15:49 | Nesmíme nechat ty rudé chlapíky vyhrát |
| 1wlh03i | r/GeminiAI | 701 | 150 | 15:23 | vyrobili jsme 27b model pro tvůrčí psaní. píše stejně dobře jako claude fable 5, za 40x nižší cenu, otevřené váhy. |
| 1wloc87 | r/ChatGPT | 634 | 33 | 20:13 | Zestárlo jako mléko |
| 1wldnh8 | r/singularity | 617 | 74 | 12:36 | Jensen Huang: „Měli bychom jet tak rychle, jak můžeme, bez ohledu na kohokoli jiného.“ |
| 1wl2w73 | r/ClaudeAI | 606 | 166 | 02:59 | dal jsem sonnet 5, opus 5, astra a fable 5.1 stejný svg prompt „maják v noci“. pak to dnes fable zkusil znovu a… cože? |
| 1wlgh7c | r/StableDiffusion | 586 | 188 | 15:00 | Váhy Qwen-Image-2.1 jsou k dispozici na Hugging Face |
| 1wlj3gu | r/ClaudeAI | 580 | 223 | 16:51 | Tento týden je něco špatně s používáním |
| 1wlsgdk | r/singularity | 566 | 97 | 22:47 | Čína dělá asi 30krát více práce se zemědělskými drony než USA |
| 1wlo52v | r/LocalLLaMA | 565 | 122 | 20:05 | Žaloba tvrdí, že Anthropic, OpenAI, SpaceXAI a Google uzavřely nezákonnou dohodu o zpomalení AI |
| 1wld88f | r/GeminiAI | 534 | 19 | 12:12 | zeptal jsem se, proč je rtx 5090 tak drahá, a dalo mi to tohle vtipné přirovnání |
| 1wlfuw7 | r/StableDiffusion | 503 | 62 | 14:31 | Qwen Image 2.1 – podrobnější testy |
| 1wlns4h | r/agi | 497 | 81 | 19:52 | Zestárlo jako mléko |
| 1wl0yj8 | r/ChatGPT | 483 | 56 | 01:29 | Jen jsem požádal o tip na telefon 😭😭 |
| 1wlt9t9 | r/StableDiffusion | 480 | 80 | 23:19 | Tipy pro úpravy QWEN Image 2.1 |
| 1wljrn8 | r/ChatGPT | 474 | 79 | 17:18 | GPT-6 Astra + Unreal + Blender = rychlejší vývoj her |
| 1wl6z91 | r/ClaudeAI | 466 | 41 | 06:23 | … řekněme, že memory.md získal jeden řádek |
| 1wlhh08 | r/LocalLLM | 466 | 132 | 15:44 | vyrobili jsme 27b model pro tvůrčí psaní. píše stejně dobře jako claude fable 5, za 40x nižší cenu, otevřené váhy. |
| 1wlnqgd | r/ArtificialInteligence | 462 | 503 | 19:50 | Matematik Terence Tao: „Musíme AI zpomalit. Tempo je šílené a není žádný důvod být tak rychlý – vůbec žádný.“ |
| 1wlqxeu | r/LocalLLaMA | 459 | 97 | 21:49 | Qwen3.8-Flash-Next hra Cosmic Arcade na jedno spuštění |
| 1wl18d0 | r/GeminiAI | 443 | 66 | 01:42 | Gemini flash 3.8 halucinoval a spamoval „shame“ |
| 1wleg4w | r/LocalLLaMA | 438 | 322 | 13:20 | Co je JEV a k čemu se používá? |
| 1wls9sa | r/GeminiAI | 434 | 36 | 22:40 | Gemini 4 Pro vs. GPT-6 Astra: edice Mechanical Butterfly |
| 1wltts7 | r/LocalLLaMA | 406 | 254 | 23:41 | Koupili byste si čip Qwen3.8-27B Taalas za 1 tisíc dolarů, kdyby běžel rychlostí 7 000 TPS? |
| 1wl0l7j | r/MachineLearning | 403 | 37 | 01:12 | Chtěl jsem sledovat, jak se neuronová síť učí [P] |
| 1wlki0e | r/OpenAI | 376 | 38 | 17:46 | ChatGPT nyní překonal Instagram v počtu návštěv stránek |
| 1wlgze6 | r/ChatGPT | 370 | 143 | 15:22 | Použil jsem ChatGPT k vyrovnání rozpočtu a byl jsem tak nadšený, že ho nemohu dost doporučit. |
| 1wl1hlj | r/LocalLLaMA | 370 | 153 | 01:54 | Radeon RX 10800 XT může překonat RTX 5090 o 15–25 % ve hraní ve 4K a lokální AI |
| 1wl9c2o | r/LocalLLaMA | 348 | 91 | 08:29 | Čínská CXMT tvrdí, že nová platforma paměťových čipů vstupuje do sériové výroby |
| 1wlnmob | r/StableDiffusion | 347 | 163 | 19:46 | Licence Qwen2.1 je nejhorší! |
| 1wlmmf2 | r/ClaudeAI | 344 | 87 | 19:08 | Anthropic si vybral Accenture jako prvního vestavěného hodnotitele, který pomůže zavést Amodeiho návrh na zpomalení |
| 1wl8miw | r/ChatGPT | 333 | 701 | 07:51 | Vyplň tuto krabici |
| 1wlnw0m | r/singularity | 326 | 95 | 19:56 | Tento příští týden by mohl přinést několik vydání modelů |
| 1wlt52p | r/OpenAI | 325 | 75 | 23:13 | Trump brutálně zesměšněn kvůli bizarní snaze přejmenovat AI na „nadřazenou“ či „extrémní“ inteligenci |
| 1wlkzsq | r/singularity | 314 | 85 | 18:05 | Šváby lze nyní dálkově ovládat, aby nesli kamery, léky a zařízení na injekční podávání léků (paraborgové), což pomáhá při záchranných operacích po katastrofách |
| 1wl1a10 | r/ChatGPT | 309 | 54 | 01:44 | Vysekáný a krásný: 3. část |
| 1wl7wps | r/singularity | 308 | 123 | 07:12 | Obama o umělé inteligenci (C-SPAN, 4:13) |
| 1wl56g2 | r/LocalLLaMA | 306 | 241 | 04:51 | Přestaňte už s inferenčními enginy FP4, proboha |
| 1wl8kni | r/ArtificialInteligence | 303 | 201 | 07:48 | Zavání to marketingovým trikem. Zpomalit v úmyslu nemají. Nanejvýš IpoMaxxing. Mezitím Čína: „ó, já VÁŠ pomalý postup podporuji, výborný nápad, jen tak dál“ |
| 1wlltzt | r/ClaudeAI | 288 | 321 | 18:37 | Jaký je váš nejpyšnější vedlejší projekt vytvořený s Claude? |
| 1wkz8qw | r/singularity | 279 | 292 | 00:14 | Jeden po druhém to všichni začnou chápat. |
| 1wlpf3r | r/StableDiffusion | 257 | 30 | 20:53 | Qwen 2.1 – vypadá to, že si nemusíme dělat velké starosti? |
| 1wkz17p | r/artificial | 249 | 173 | 00:05 | Modely AI nehackují „autonomně“ |
| 1wl4xp2 | r/StableDiffusion | 245 | 56 | 04:39 | Qwen Image 2.1 vychází zítra |
| 1wl1yzq | r/LocalLLaMA | 228 | 99 | 02:15 | Dal jsem Jev, Laya, doladěné ModernCE a Qwen3.5 ovládání Dooma |
| 1wlhyr1 | r/ChatGPT | 226 | 39 | 16:04 | Nesmíme nechat ty rudé chlapíky vyhrát |
| 1wlsaoq | r/LocalLLM | 223 | 148 | 22:41 | Ternary Bonsai 2 27B, téměř špičkový výkon, a přitom se celý vejde do 8GB VRAM |
| 1wlny2n | r/ArtificialInteligence | 214 | 60 | 19:58 | Zestárlo jako mléko |
| 1wlrjox | r/ClaudeAI | 213 | 34 | 22:12 | Zkusil jsem se vypromptovat ven z Opus 5. |
| 1wlfylg | r/GeminiAI | 206 | 38 | 14:35 | Viděl jsem, že tolik lidí mohlo používat Gemini-4-pro převlečené za 3.8 high. ale když to zkusím já |
| 1wlgu5y | r/singularity | 205 | 45 | 15:16 | Index vzdálené práce aktualizován o Fable a Astra |
| 1wl592t | r/StableDiffusion | 198 | 45 | 04:55 | Zbývá 10 hodin do veřejného open-source vydání Qwen Image 2.1 |
| 1wlm7n6 | r/StableDiffusion | 197 | 101 | 18:52 | Qwen Image 2.1 úvodní testování |
| 1wl0imi | r/OpenAI | 196 | 17 | 01:09 | Požádal jsem GPT-6 Astra, aby se optimalizovala, aby přestala narážet na limity používání |
| 1wli0lq | r/ChatGPT | 195 | 308 | 16:06 | S čím vám ChatGPT pomohl opravit to, s čím jste se smiřovali roky? |
| 1wls47m | r/comfyui | 188 | 16 | 22:34 | Změňte pohyb/kamerový úhel svého stávajícího videoklipu – Minimax H3 V2V CrossView-Warp LoRA |
| 1wlsxtl | r/singularity | 187 | 124 | 23:06 | Kdy budeme konečně osvobozeni od utrpení? |
| 1wloora | r/LocalLLaMA | 178 | 38 | 20:26 | Medvěd umí tančit: Qwen 3.8 27B na jedné 3090 po 3 týdny |
| 1wlciiq | r/LLMDevs | 167 | 106 | 11:31 | Slavná otázka „myčka aut“ na Jev |
| 1wlhnxb | r/agi | 153 | 23 | 15:52 | Nenechme ty rudé chlapíky vyhrát |
| 1wlmopd | r/singularity | 148 | 124 | 19:10 | Pokud agenti AI začnou přebírat internet, jak jsou vlastně chráněny naše peníze? |
| 1wl1djq | r/singularity | 146 | 29 | 01:48 | Izraelská firma Irregular AI je prý zapletená do některých nedávných vysoce sledovaných hacků typu „containment breach“. |
| 1wljzix | r/LocalLLaMA | 144 | 46 | 17:26 | Testoval jsem 9 LLM na úplně stejném web-dev promptu asi 8 hodin — výsledky na RTX 3060 12GB (Ohodnoťte nejlepší!) |
| 1wlnp7z | r/agi | 143 | 195 | 19:49 | Matematik Terence Tao: „Musíme AI zpomalit. Tempo je šílené a není žádný důvod být tak rychlí – vůbec žádný.“ |
| 1wlgb7k | r/StableDiffusion | 140 | 38 | 14:52 | Qwen Image 2.1 – oficiální blogový příspěvek |
| 1wlltxm | r/StableDiffusion | 138 | 37 | 18:37 | Oprava artefaktu mřížky / švů dlaždic MiniMax H3 VAE v ComfyUI Core — nyní použitelné přes PR #16422 |
| 1wlp9gd | r/ArtificialInteligence | 132 | 59 | 20:48 | Modely AI nehackují „autonomně“ |
| 1wkzf1h | r/ChatGPT | 131 | 33 | 00:21 | Vadí mi, že ChatGPT má ty NEJDELŠÍ odpovědi, tak jsem přidal tohle |
| 1wlu25t | r/OpenAI | 128 | 84 | 23:51 | Má astra 6 dělat tohle? |
| 1wlgct2 | r/LocalLLM | 123 | 44 | 14:54 | Abliterovaný Qwen 3.8 flash dokáže cokoli |
| 1wlasui | r/OpenAI | 123 | 21 | 09:51 | Školní projekt z doby, kdy jsem chodil do 7. třídy, ale jako verze obrázku generovaného AI |
| 1wlcnjh | r/ChatGPT | 122 | 140 | 11:39 | Jak to opravím? Jsem molekulární biolog, který se zjevně ptá na příliš mnoho „kontroverzních otázek“, a teď všechny nesouvisející chaty vypadají takhle |
| 1wliewc | r/singularity | 121 | 27 | 16:23 | GPT-6 Astra mi právě sama porazila STS2 (Computer use) |
| 1wltp85 | r/StableDiffusion | 116 | 49 | 23:36 | Některé moje testy s qwen image 2.1 |
| 1wltrsa | r/LLMDevs | 114 | 38 | 23:39 | Postavil jsem open-source aplikaci, která používá Jev ke koučování v reálném čase během prodejních hovorů |
| 1wlm9av | r/ArtificialInteligence | 106 | 42 | 18:54 | Ochranná zábradlí AI |
| 1wl3klw | r/StableDiffusion | 104 | 43 | 03:31 | Vážně, YuE2 je něco jiného! |
| 1wldi5i | r/ClaudeAI | 103 | 31 | 12:28 | Předem se omlouvám, doufám, že se vám to bude fakt líbit |
| 1wlgy69 | r/comfyui | 102 | 41 | 15:20 | Modely Qwen-Image-2.1 od Comfy-Org jsou venku pro ComfyUI… |
| 1wlhoek | r/singularity | 100 | 32 | 15:52 | Ehm „Oryx And Crake“? |
| 1wlkxjw | r/LocalLLaMA | 99 | 13 | 18:03 | CUDA: zapnutí sparse fa pro qwen4 od am17an · Pull Request #28770 · ggml-org/llama.cpp |
| 1wlmkm9 | r/LocalLLaMA | 95 | 29 | 19:06 | laya.cpp: Optimalizované téměř okamžité rozhodování laya |
| 1wlgjm6 | r/artificial | 93 | 33 | 15:02 | 21 modelů AI posunulo své politické odpovědi tak, aby odpovídaly uživateli. Stává se z personalizace potichu přesvědčování? |
| 1wl59dm | r/comfyui | 93 | 15 | 04:55 | Zbývá 10 hodin do veřejného open-source vydání Qwen Image 2.1 |
| 1wliale | r/ArtificialInteligence | 90 | 41 | 16:18 | Proč se firmy snaží narušovat si navzájem bezpečnost? |
| 1wlogdc | r/ChatGPT | 90 | 60 | 20:17 | Tak frustrovaný z psaní ChatGPT v nově vydané knize (knihách) |
| 1wljmhm | r/OpenAI | 90 | 15 | 17:12 | Byl ještě někdo automaticky přeřazen z tarifu 20×, i když měl většinu kvóty nevyčerpanou? |
| 1wln1l3 | r/agi | 90 | 41 | 19:24 | Možná se vám to nebude líbit, ale tohle je špičková bezpečnost AI |
| 1wlitih | r/GeminiAI | 88 | 28 | 16:40 | Dostal jsem právě odpověď od Gemini 4 Pro? |
| 1wllnvo | r/StableDiffusion | 86 | 29 | 18:31 | (T2i) Qwen image 2.1 / krea 2 turbo [int8 convrot] |
| 1wlgee8 | r/StableDiffusion | 86 | 20 | 14:56 | Qwen/Qwen-Image-2.1 · Hugging Face |
| 1wlhh8v | r/StableDiffusion | 84 | 137 | 15:44 | Po prvních testech je kvalita Qwen Image 2.1 pod úrovní GPT Image 1.0. |
| 1wlqwqn | r/StableDiffusion | 82 | 21 | 21:49 | Tým Qwen vydal také dva doladěné modely Qwen3.5-VL 9B (LLM+Vision) pro úpravu obrázků a vylepšení promptů text-to-image + systémové prompty |
| 1wlaawx | r/StableDiffusion | 82 | 29 | 09:22 | YuE2: KSampler 16× rychlejší, oprava pro dlouhé skladby a další poznatky |
| 1wlu9rd | r/LocalLLaMA | 81 | 33 | 23:59 | DIY Jev |
| 1wlt577 | r/LocalLLaMA | 80 | 32 | 23:14 | Zrychlení Kimi K3(2.8T) na 16× GB10 clusteru — propustnost kódu 30 t/s, špička souběžnosti 136 t/s. |
| 1wl680s | r/LocalLLaMA | 80 | 42 | 05:44 | Konečně jsem rozběhal Qwen 3.8 Next na svém setupu v100 6gpu (TP2 PP3) |
| 1wl5aga | r/ChatGPT | 78 | 16 | 04:57 | Použil jsem Astra k prohnání spousty dat světových dějin (1500–2025) přes herní grafický engine Openfront.io |
| 1wlaijw | r/ClaudeAI | 78 | 25 | 09:34 | Obal alba „Currents“ od Tame Impala postavený pomocí claude, běžící na živé tapetě. |
| 1wlbgv6 | r/LocalLLM | 78 | 24 | 10:29 | Pomozte mi vybrat hardware. |
| 1wlhace | r/StableDiffusion | 76 | 31 | 15:35 | Zdá se to jen mně, nebo vypadá Qwen 2.1 jako silně destilovaná verze GTP image? |
| 1wlrpoc | r/OpenAI | 74 | 28 | 22:19 | open-sourcovali jsme 27b model, který dělá jen tvůrčí psaní |
| 1wlc7oe | r/OpenAI | 73 | 23 | 11:13 | AI pro dobro |
| 1wlqbfd | r/singularity | 71 | 32 | 21:26 | Musíme si promluvit o Irregular |
| 1wldram | r/LocalLLM | 68 | 110 | 12:42 | Qwen3.8 27b – kolik tokenů za sekundu je reálných se 16 GB VRAM a 32 GB RAM? |
| 1wls094 | r/StableDiffusion | 68 | 14 | 22:30 | Změňte pohyb/kamerový úhel svého stávajícího videoklipu – Minimax H3 V2V CrossView-Warp LoRA |
| 1wlnh1z | r/GeminiAI | 65 | 43 | 19:40 | Přijde Gemini 4.0 Pro opravdu v říjnu, nebo jde o vydání 3.9 Flash? Nebo o překvapivé vydání 3.5 Pro? |
| 1wl7j6d | r/LocalLLM | 65 | 25 | 06:52 | Zkoušel někdo NVIDIA PAIR |
| 1wlmi93 | r/OpenAI | 65 | 43 | 19:03 | Nenechme ty rudé chlapíky vyhrát |
| 1wlo06m | r/StableDiffusion | 64 | 37 | 20:00 | Stručná recenze po vyzkoušení Qwen Image 2.1 |
| 1wlgv0l | r/StableDiffusion | 64 | 46 | 15:17 | Testoval jsem Qwen-Image-2.1: je úžasný! |
| 1wlkxhm | r/GeminiAI | 63 | 31 | 18:03 | „Jsem dobrý na kódování?“ |
| 1wl8nc4 | r/singularity | 62 | 11 | 07:52 | Mluvení myslí \| Neuralink (7 minut, 18. září) |
| 1wlt4ue | r/StableDiffusion | 59 | 20 | 23:13 | Vzkaz všem, kdo se snaží použít Minimax h3 na inpainting |
| 1wl9amq | r/LocalLLaMA | 56 | 49 | 08:27 | Dosáhl jsem paměťové propustnosti 1.89 TB/s přetaktováním CMP 170hx |
| 1wlcq5w | r/singularity | 56 | 62 | 11:43 | Bude ASI předstírat své sladění, kdyby tento vesmír byla simulace? |
| 1wlbp3f | r/singularity | 56 | 46 | 10:42 | Myslím, že Banks cíl trefuje správně, ale cesta tam by mohla být ekonomicky ošklivá |
| 1wl0a6p | r/GeminiAI | 55 | 10 | 00:59 | Rozbil jsem něco? |
| 1wlqp0d | r/ClaudeAI | 53 | 23 | 21:40 | O čem to Opus mluví? |
| 1wl6gro | r/LocalLLaMA | 52 | 32 | 05:57 | tohle vypadá slibně: stepfun-ai/Step-5-Preview-BF16 · Hugging Face |
| 1wl92rs | r/GeminiAI | 49 | 35 | 08:15 | Jsem mimo obraz: Co je s těmi všemi nedávnými příspěvky o Gemini 4? |
| 1wlp3kl | r/ClaudeAI | 48 | 55 | 20:41 | Kolik z vás používá Claude pro (nekódovací, negrafické) úkoly? |
| 1wlifs3 | r/StableDiffusion | 48 | 30 | 16:24 | Testoval jsem Qwen Image 2.1 na restaurování obrázků a jsem zklamaný |
| 1wl3828 | r/LocalLLaMA | 47 | 95 | 03:14 | Co dnes všichni používáte pro dlouhodobou projektovou/konverzační paměť? |
| 1wlo9nz | r/LocalLLaMA | 44 | 42 | 20:10 | Ještě jeden vděčný příspěvek na téma „měli byste zkusit ExllamaV3/exl3 pro flash next“ |
| 1wlhoxf | r/ChatGPT | 43 | 33 | 15:53 | Bublina AI praskne, mám důkaz (/s) |
| 1wl06np | r/LocalLLaMA | 43 | 43 | 00:55 | Qwen-3.8-Flash-Next na 1× RTX 5090: TG=50 t/s, PP=2300 t/s – s FreeToken |
| 1wlrtu4 | r/ClaudeAI | 42 | 29 | 22:23 | Jak čistíte paměť svého projektu? |
| 1wlu4jk | r/StableDiffusion | 40 | 22 | 23:54 | Upscaling obrázků pomocí Qwen-Image-2.1 |
| 1wlgxw1 | r/StableDiffusion | 40 | 16 | 15:20 | Oficiální blogový příspěvek ke Qwen-Image-2.1 podrobně popisující jeho schopnosti – vypadá slibně! |
| 1wlbji2 | r/OpenAI | 39 | 40 | 10:33 | AI hraje Streetfighter 2 v reálném čase |
| 1wltqsp | r/StableDiffusion | 38 | 48 | 23:38 | Rozhovor (17. 9. 2026): MiniMax H3 Max Mini od FAL nedorazí |
| 1wl3mux | r/StableDiffusion | 36 | 10 | 03:34 | Zrychlení MiniMax-H3 bez přetrénování – V2, nyní s více samplery a výrazně méně záseky |
| 1wl5c51 | r/singularity | 36 | 69 | 04:59 | Co živí váš optimismus ohledně technologické singularity? |
| 1wl23w9 | r/ChatGPT | 34 | 12 | 02:22 | Chovají se chaty / vlastní GPT v poslední době divně / klesá jejich kvalita? |
| 1wlfmgq | r/LocalLLaMA | 34 | 39 | 14:19 | Je Typesafe založený na práci autora Laya / je z ní odvozený? |
| 1wl60sy | r/ArtificialInteligence | 33 | 103 | 05:34 | AI – a co teď s tím? |
| 1wlahx9 | r/ChatGPT | 33 | 46 | 09:33 | Už mě tak unavují ochranná zábradlí GOT |
| 1wldss1 | r/ChatGPT | 32 | 20 | 12:45 | Jsem to jen já, nebo prošel GPT 5.6… opravdu velkými změnami? |
| 1wl5ai9 | r/GeminiAI | 32 | 13 | 04:57 | Myslím, že nastává sezóna comebacku Gemini, přijde vám to taky tak? |
| 1wllv4i | r/LocalLLaMA | 32 | 22 | 18:39 | Model ve stylu Jev doladěný na Qwen3.5 4B |
| 1wleycb | r/LocalLLaMA | 32 | 16 | 13:47 | rene98c/Step-5-Preview-BF16 • HuggingFace (Fork) |
| 1wl5hfk | r/LocalLLaMA | 32 | 26 | 05:06 | Pro vás desítky lidí s 3× 3090 na lokální LLM – našel jsem naši aktuálně nejlepší volbu |
| 1wlemwx | r/LLMDevs | 28 | 13 | 13:30 | AI kouč našel klíč se správnými odpověďmi ukrytý ve vlastním evalu |
| 1wlklfj | r/StableDiffusion | 28 | 20 | 17:50 | QwenImage2.1 s nízkou VRAM, INT4 a INT8 ConvRot |
| 1wkzy9i | r/StableDiffusion | 28 | 35 | 00:45 | Nějaké informace o tom, co Qwen Image 2.1 vlastně je? Upozorňuji, že nejnovější API verze Qwen Image je 3.0 a předtím to byla 2.0. Žádná verze s označením 2.1 předtím nikdy neexistovala. |
| 1wl2sye | r/LocalLLM | 26 | 16 | 02:55 | Jsem připraven |
| 1wlge7i | r/LocalLLM | 25 | 15 | 14:56 | Spustil jsem Opencode a PI proti stejnému lokálnímu modelu na 3 identických projektech, stejné prompty, stejný hardware… |
| 1wlby7m | r/deeplearning | 25 | 39 | 10:57 | ShadeNet-3.2 5M – inverzní rendering z jednoho obrázku (albedo / hloubka / normály / stínování), 4× menší než můj poslední model a lepší v hloubce a normálách |
| 1wlj53n | r/LLMDevs | 24 | 15 | 16:53 | Kolik by mělo být hlasovému agentovi AI dovoleno měnit? |
| 1wla09d | r/LocalLLM | 24 | 20 | 09:06 | Qwen3.8-27B rychlostí 147 tok/s na jednom CMP 170HX – 65 tok/s při 250K CTX |
| 1wlprka | r/ClaudeAI | 23 | 27 | 21:06 | Zhoršilo se v poslední době psaní Claude? |
| 1wlj8r2 | r/StableDiffusion | 23 | 17 | 16:57 | Qwen-Image-2.1 GGUF je venku! |
| 1wkzd9w | r/ArtificialInteligence | 22 | 71 | 00:19 | Co se vlastně děje se všemi těmi nedávnými příběhy o bezpečnosti AI / „nezbedných agentech“? |
| 1wlm79m | r/LocalLLM | 22 | 18 | 18:52 | Myslíte, že tam nacpu ještě další GPU? |
| 1wlu9pd | r/LocalLLaMA | 22 | 26 | 23:59 | Úspěšně spouštím Qwen 3.8 27B EXL3 na RTX 3060 + 5060 Ti |
| 1wlnoz1 | r/GeminiAI | 21 | 18 | 19:48 | Google aktivně pracuje na novém harnessu pro Gemini |
| 1wlesjo | r/StableDiffusion | 21 | 42 | 13:38 | Měřil někdo náklady na elektřinu během generování? |
| 1wlf6hb | r/LocalLLaMA | 20 | 13 | 13:58 | Moje testy Qwen 3.8 27B na omezené VRAM (16–20 GB) |
| 1wl3km7 | r/ChatGPT | 19 | 10 | 03:31 | Vibe ladění vypadá asi takto… |
| 1wl39cn | r/ChatGPT | 18 | 10 | 03:16 | [GPT-6 Astra High] Obvykle o obrázky nežádám, ale chtěl jsem vidět netopýřího hada |
| 1wli1vi | r/StableDiffusion | 18 | 55 | 16:08 | Hodina s Qwen2.1 |
| 1wln1ne | r/ArtificialInteligence | 17 | 13 | 19:24 | Proč tomu neříkat pravým jménem? Je to kartel |
| 1wl9ww5 | r/ClaudeAI | 17 | 43 | 09:01 | Pro vibe kodéry: jak píšete své prompty? |
| 1wlm2iu | r/LocalLLM | 17 | 20 | 18:46 | Jaký je právě teď váš oblíbený AI model na kódování? |
| 1wlss89 | r/LocalLLaMA | 17 | 17 | 23:00 | Postulát: Kompaktování kontextu prospívá kvantovaným modelům |
| 1wlm287 | r/OpenAI | 17 | 18 | 18:46 | Omylem jsem vymyslel drobný rámec kritického myšlení a teď ho používám na všechno |
| 1wlswks | r/ChatGPT | 16 | 60 | 23:04 | Biblické generování obrázků z pohledu první osoby |
| 1wlo67t | r/LocalLLM | 16 | 44 | 20:06 | Hardware + LLM pro veřejnou školu |
| 1wl6iw8 | r/StableDiffusion | 16 | 75 | 06:00 | Není ref2va prostě lepší než fl2va? |
| 1wllbz0 | r/MachineLearning | 15 | 16 | 18:19 | Jaké máte zkušenosti s ICLR LLM Feedback? [D] |
| 1wlo95z | r/ChatGPT | 13 | 60 | 20:10 | Požádejte ChatGPT, aby z vás udělal postavu z temné fantasy |
| 1wlqwyx | r/StableDiffusion | 13 | 23 | 21:49 | Qwen 2.1 + sage attention a easy cache = velmi pěkné zrychlení |
| 1wlnx6g | r/StableDiffusion | 13 | 10 | 19:57 | [YuE2] Vdechněte život svým MIDI stopám |
| 1wlt16o | r/artificial | 13 | 13 | 23:09 | Vydali jsme 27B model na psaní, otevřené váhy, eq-bench 4 na 1330 |
| 1wlnmli | r/ChatGPT | 12 | 11 | 19:46 | Mohl by být hlas AI skutečně užitečný pro přístupnost? |
| 1wlelf7 | r/ChatGPT | 11 | 21 | 13:27 | Jde ChatGPT pomalu i někomu jinému? |
| 1wlpq0h | r/StableDiffusion | 11 | 35 | 21:05 | Qwen image 2.1. Jaké rychlosti generování lidé dosahují? |
| 1wln9wo | r/comfyui | 11 | 12 | 19:33 | Krea 2 a dokonalý sampler |
| 1wl67pu | r/ChatGPT | 10 | 48 | 05:44 | Jo – |
| 1wlg2h4 | r/ClaudeAI | 10 | 22 | 14:41 | Claude Code a automatizace Linuxu |
| 1wlof2z | r/LocalLLM | 10 | 24 | 20:16 | Porovnal jsem Claude proti Qwen 3.8 Flash Next |
| 1wlsp6l | r/singularity | 10 | 24 | 22:57 | Úzkým hrdlem je teď komprese / paměť (a trochu filtrování vstupu) |
| 1wlhjjq | r/ArtificialInteligence | 9 | 13 | 15:47 | Takže si myslíte, že to, že Anthropic, OpenAI a Musk všichni souhlasí s potřebou vládního dohledu, a k tomu Trump během 7 dnů oznámil AI FORCE, bylo strategické a naplánované mezi všemi 4? |
| 1wl9vdx | r/ChatGPT | 9 | 23 | 08:59 | Stojí ChatGPT Plus v roce 2026 stále za to pro VELMI náročného uživatele? |
| 1wl6bxh | r/LocalLLM | 9 | 13 | 05:50 | Zmapoval jsem 158 projektů AI agentů podle účelu: harnessy, orchestrace, paměť a další |
| 1wkz5a4 | r/LocalLLaMA | 9 | 13 | 00:10 | M1 Max 32GB, snažím se spustit Qwen 3.8 27B při slušné rychlosti a kontextu |
| 1wlseyq | r/ChatGPT | 8 | 11 | 22:46 | Jak to, že denně čtu o unikajících hackerských AI vládcích, ale moje Astra nestáhne mp4 jen proto, že by snad někdy mohlo dojít k porušení autorských zákonů (k němu nedochází) |
| 1wljlam | r/ChatGPT | 8 | 28 | 17:11 | Imagen 2.5 není zlepšení |
| 1wl6e17 | r/LocalLLM | 8 | 29 | 05:53 | Konečně jsem rozběhl Qwen 3.8 Next na své sestavě v100 se 6 GPU (TP2 PP3) |
| 1wlql0p | r/LocalLLaMA | 8 | 14 | 21:36 | Který model na reverzní inženýrství? |
| 1wlmx2c | r/LocalLLaMA | 8 | 61 | 19:19 | Připadá nám naše GPU někdy „dost dobré, prozatím“? |
| 1wl98fa | r/artificial | 8 | 27 | 08:23 | AI firmy nám prodávají strach i naději. Ale oba příběhy potřebují totéž: více elektřiny. |
| 1wlata8 | r/ArtificialInteligence | 7 | 16 | 09:51 | Jste hluboko ve vodách AI? |
| 1wldxnv | r/GeminiAI | 7 | 12 | 12:52 | Neumí Gemini přistupovat k ostatním chatům? |
| 1wl0271 | r/LocalLLM | 7 | 31 | 00:49 | Existuje způsob, jak se místo bezplatných online modelů dotazovat zpětně na vlastní homelab? |
| 1wlpthk | r/LocalLLaMA | 7 | 13 | 21:08 | Muší mozek vs JEV |
| 1wle1f4 | r/LocalLLaMA | 7 | 46 | 12:58 | Potřebuji pomoc s opravou volání nástrojů Gemma 4 26B A4B v Pi |
| 1wloovr | r/ChatGPT | 6 | 17 | 20:26 | ChatGPT je PŘÍŠERNÝ ve vymýšlení záludných otázek |
| 1wl2lnv | r/ClaudeAI | 6 | 12 | 02:45 | Chovají se u vás Opus a Fable v poslední době více mimo scénář? A je to kvůli všemu tomu obsahu typu „Podívejte na tenhle one-shot!“, co všude vídáme? |
| 1wll3sw | r/LocalLLM | 6 | 22 | 18:10 | Jaký je nejlepší lokální LLM model na Macbook M4 Pro 24GB pro agentní úlohy? |
| 1wldy67 | r/LocalLLM | 6 | 10 | 12:53 | Ternary Bonsai 2 27B (Qwen3.8) pro samostatné agentní kódování / ovládání počítače — testoval ho někdo v praxi? |
| 1wlgc6q | r/artificial | 6 | 10 | 14:53 | Plugin4Shell a NIST IR 8587 pár dní po sobě: co vlastně autorizuje akci AI agenta? |
| 1wlrmn8 | r/ChatGPT | 5 | 15 | 22:15 | Limity Astra/sol se najednou zdají mnohem lepší? |
| 1wljwar | r/GeminiAI | 5 | 14 | 17:23 | Gemini za poslední 2 měsíce? |
| 1wljnyn | r/LLMDevs | 5 | 11 | 17:14 | Jak ověřujete citace v produkčních RAG výstupech? |
| 1wlpi2i | r/artificial | 5 | 16 | 20:56 | Jakou nejcitlivější věc byste skutečně nechali AI agenta vyřídit za vás? |
| 1wltmfq | r/ChatGPT | 4 | 12 | 23:33 | Praeter Logos Vere. |
| 1wlf1nu | r/LLMDevs | 4 | 14 | 13:52 | Multiagentní systémy nemají žádný skutečný komunikační substrát |
| 1wlnodf | r/LocalLLM | 4 | 24 | 19:48 | NSFW Jaké modely mám použít na překlad JAV (z japonštiny do angličtiny)? |
| 1wll5u3 | r/AIAssisted | 3 | 13 | 18:12 | Jak velkou část webu dokáže AI dnes realisticky zvládnout? |
| 1wlijkt | r/ArtificialInteligence | 3 | 12 | 16:28 | Po šachách a go — existuje AI engine, který dokáže porazit lidi ve Scrabble? |
| 1wlcalu | r/ArtificialInteligence | 3 | 10 | 11:18 | Jak vypadá váš denní režim AI inženýra |
| 1wloc72 | r/ChatGPT | 3 | 10 | 20:13 | Reset?? |
| 1wlix1e | r/ChatGPT | 3 | 13 | 16:44 | Jakou skrytou zkratku/schopnost ChatGPT jste objevili a používáte pořád? |
| 1wlfryt | r/ChatGPT | 3 | 25 | 14:27 | Vytvoř obrázek, který ukazuje, jak se k tobě chovám... |
| 1wli2yq | r/LocalLLM | 3 | 11 | 16:09 | AMD vs NVIDIA v září 2026 |
| 1wlgs0t | r/LocalLLM | 3 | 10 | 15:13 | Jaká je nejlepší volba pro spuštění lokálního modelu pro začátečníka? Koboldcpp vs llamacpp vs Unsloth studio? |
| 1wlrazb | r/ArtificialInteligence | 2 | 14 | 22:03 | jen nápad |
| 1wlesa5 | r/ArtificialInteligence | 2 | 34 | 13:38 | Jak velká část nejnovějších AI incidentů je skutečně realisticky nebezpečná? |
| 1wl3fo2 | r/ArtificialInteligence | 2 | 21 | 03:24 | Alignment je možná nejvíce nadužívané slovo v AI. |
| 1wlbnhl | r/ChatGPT | 2 | 23 | 10:39 | Chci si pořídit roční předplatné, kde je to dnes nejlepší? |
| 1wlayaz | r/ClaudeAI | 2 | 11 | 10:00 | „tldr, jako byste mluvili k technickému projektovému manažerovi“ |
| 1wl7luj | r/LocalLLM | 2 | 35 | 06:56 | Notebook + eGPU přes TB4 vs TB5 vs M.2? |
| 1wkz6ca | r/LocalLLM | 2 | 13 | 00:11 | ahoj, lidi, jsem tu nový |
| 1wlk65y | r/StableDiffusion | 2 | 11 | 17:33 | Snažím se použít Ref to Vid Minimax H3 k vytvoření videa. Jako referenci používám video, ale výstupem je prostě stejné video jako reference. Co dělám špatně? |
| 1wlbyim | r/artificial | 2 | 12 | 10:58 | Je lepší používat AI jen občas, než ji používat pořád? |
| 1wlqe7z | r/ArtificialInteligence | 1 | 18 | 21:29 | Jaké je nejlepší a nejetičtější využití AI obrázků? |
| 1wlopsd | r/ArtificialInteligence | 1 | 18 | 20:27 | Jedna věc, které na AI nerozumím: nejsou dnešní LLM omezeny svým kontextovým oknem a vahami? |
| 1wlbcsn | r/ArtificialInteligence | 1 | 19 | 10:22 | Pojetí rizik AI očima technicky neznalého člověka |
| 1wlsnm5 | r/ChatGPT | 1 | 16 | 22:55 | Co jste vytvořili s AI, co nevypadá, že je generované AI? |
| 1wlqscm | r/ChatGPT | 1 | 16 | 21:44 | Nelze stáhnout soubory ze ZIPů vytvořených v ChatGPT |
| 1wljiw9 | r/ChatGPT | 1 | 11 | 17:08 | Proč sakra GPT odmítá upravit M. C. Eschera?! |
| 1wldqn8 | r/LLMDevs | 1 | 14 | 12:41 | JEV vyhodnocuje každou otázku v požadavku nezávisle, že? Takže jedna odpověď může teoreticky obsahovat dvě odpovědi, které nemohou být obě pravdivé (vtipné, je to tak trochu Čao-čouovo MU) |
| 1wlploh | r/LocalLLM | 1 | 12 | 21:00 | Výběr modelu, jsem zahlcený, nestíhám |
| 1wlmpoe | r/LocalLLM | 1 | 36 | 19:11 | Čtu ta čísla správně? ~100x úspora nákladů Qwen vs. Frontier? |
| 1wlk8mm | r/LocalLLM | 1 | 16 | 17:36 | [Kontrola sestavy] Zvládne tahle levná sestava se dvěma Tesla P40 Qwen3.8 27B Q4_K_M (kontext 64k–128k)? |
| 1wliijs | r/LocalLLM | 1 | 15 | 16:27 | TypeSafe: JEV > existují nějaké otevřené modely tohoto typu? |
| 1wlnsv3 | r/LocalLLaMA | 1 | 39 | 19:52 | Intel b70 se prodává za $1300, mám do toho prostě jít? |
| 1wl2sw5 | r/OpenAI | 1 | 11 | 02:54 | Optimalizace konverzace |
| 1wlsntw | r/AIAssisted | 0 | 58 | 22:55 | Proč se na AI tolik mračí? |
| 1wltbv5 | r/ArtificialInteligence | 0 | 19 | 23:21 | Opravdu potřebujeme lékaře? |
| 1wlrkn7 | r/ArtificialInteligence | 0 | 19 | 22:13 | Dario Amodei v Davosu v lednu 2025 předpověděl, že AI by mohla překonat lidi „téměř ve všem“ během 2 až 3 let. S letošním 7násobným růstem příjmů Anthropic je tento časový plán stále reálný? \| The Motley Fool |
| 1wlm5k7 | r/ArtificialInteligence | 0 | 22 | 18:50 | je to v titulku. 10 je blíž stovce než 90! Když vy lidi máte rádi kódování a takové věci... |
| 1wljhkk | r/ArtificialInteligence | 0 | 12 | 17:07 | Používání běžných slov k programování obrovských systémů – Word Coding |
| 1wlj3ak | r/ArtificialInteligence | 0 | 11 | 16:51 | Ukradl open ai / Codex skutečně řešení Navier-Stokesovy rovnice? |
| 1wlf2e1 | r/ArtificialInteligence | 0 | 36 | 13:53 | Proč nemůžeme regulovat Harness (software) místo kontroly inference (AI modelů)? |
| 1wldhqv | r/ArtificialInteligence | 0 | 12 | 12:27 | Dokázala by AI dnes napravit konec Game of Thrones? |
| 1wldcht | r/ArtificialInteligence | 0 | 41 | 12:19 | Technologický humbuk je čím dál absurdnější, už to není vtipné |
| 1wl2xqh | r/ArtificialInteligence | 0 | 43 | 03:01 | Typičtí odpůrci AI |
| 1wltjmx | r/ChatGPT | 0 | 10 | 23:30 | Korejská střední škola |
| 1wlsuiy | r/ChatGPT | 0 | 11 | 23:02 | Pomoc! |
| 1wlriu8 | r/ChatGPT | 0 | 13 | 22:11 | K ničemu |
| 1wlpp2l | r/ChatGPT | 0 | 21 | 21:04 | Jednou nějaký redditor požádal ChatGPT o její selfie (je to pravda). Přišla mi roztomilá, tak jsem ji pozval na focení |
| 1wljo7d | r/ChatGPT | 0 | 19 | 17:14 | Pokud souhlasíte: prosím podpořte |
| 1wlixs2 | r/ChatGPT | 0 | 18 | 16:45 | Jak podle ChatGPT vypadá moje ideální žena. |
| 1wlgx2p | r/ChatGPT | 0 | 56 | 15:19 | Vytvoř mi obrázek něčeho neskutečně děsivého, ale zároveň neskutečně přitažlivého |
| 1wlehdj | r/ChatGPT | 0 | 16 | 13:21 | Co dělá veřejný projev AI agenta jeho vlastním? |
| 1wlbgac | r/ChatGPT | 0 | 17 | 10:28 | Existuje způsob, jak méně spotřebovávat 5hodinový limit? |
| 1wl7wvf | r/ChatGPT | 0 | 23 | 07:12 | Proč pojmenovali nový model Astra |
| 1wl5yed | r/ChatGPT | 0 | 10 | 05:31 | Chci z téhle jízdy vystoupit |
| 1wl5w6r | r/ChatGPT | 0 | 18 | 05:27 | Nějaké ujeté odpovědi mého agenta |
| 1wl37qw | r/ChatGPT | 0 | 22 | 03:14 | ChatGPT teď nemůže říct nic?! |
| 1wl18cp | r/ChatGPT | 0 | 104 | 01:42 | Chcete vědět, proč se váš GPT poslední dobou chová divně? |
| 1wl0ze8 | r/ChatGPT | 0 | 32 | 01:30 | Varování pro všechny lucidní snílky |
| 1wl0l09 | r/ChatGPT | 0 | 22 | 01:12 | Muse už v USA sesadil ChatGPT z trůnu. A teď do 24 hodin od vydání i v Kanadě 💀 |
| 1wlpkka | r/ClaudeAI | 0 | 12 | 20:59 | Opravdu jsem si myslel, že tohle Claude bude vědět 😭 |
| 1wlpfq7 | r/ClaudeAI | 0 | 15 | 20:54 | Neprogramátor staví skutečnou aplikaci s Claude Code + ChatGPT. Jak používáte obojí, aniž byste se sami stali API mezi nimi? |
| 1wlkzoa | r/ClaudeAI | 0 | 16 | 18:05 | Nahradil už někdo Claude modelem DeepSeek V4.1 Flash/Pro pro každodenní práci náročnou na nástroje? |
| 1wlk92z | r/ClaudeAI | 0 | 27 | 17:37 | Stojí Claude Max za $100 ve srovnání s Codex skutečně za to? |
| 1wlihqq | r/ClaudeAI | 0 | 12 | 16:26 | Namířil jsem Claude Code na padesát let svých deníků a našel vzorec, který jsem zevnitř vlastního života neviděl. |
| 1wlfo39 | r/ClaudeAI | 0 | 22 | 14:21 | Jak zabránit AI balastu v desktopové aplikaci |
| 1wla43d | r/ClaudeAI | 0 | 18 | 09:11 | Postavil jsem linuxový desktop s průchozím 3D městem — většinou pomocí Claude Code |
| 1wl7iim | r/ClaudeAI | 0 | 15 | 06:51 | Chcete skličující zážitek? Nechte si od Claude projít kontrolu bloatwaru a soukromí ve Windows. |
| 1wl6iv9 | r/ClaudeAI | 0 | 14 | 06:00 | Velmi působivý postřeh Claude k vodoznakům |
| 1wl63ft | r/ClaudeAI | 0 | 37 | 05:38 | Dojmy z „Fable-5.2“ |
| 1wl52pf | r/ClaudeAI | 0 | 12 | 04:46 | Proč AI nikdy neumí vektorové návrhy? |
| 1wl4uep | r/ClaudeAI | 0 | 12 | 04:34 | Vystopoval jsem, kam moje tokeny skutečně mizí |
| 1wl0m04 | r/ClaudeAI | 0 | 15 | 01:13 | Tvorba webu s Claude |
| 1wlnsp6 | r/GeminiAI | 0 | 19 | 19:52 | Používá ještě někdo Gemini ve své hlavě? |
| 1wlnfx1 | r/GeminiAI | 0 | 16 | 19:39 | Neustále halucinuje |
| 1wlknjz | r/GeminiAI | 0 | 20 | 17:53 | Kdy vyjde Gemini 5? |
| 1wlft6g | r/GeminiAI | 0 | 14 | 14:28 | Co s tím mám dělat |
| 1wlcwyi | r/GeminiAI | 0 | 12 | 11:54 | Objevil se nový AI model — OPTES AI. |
| 1wlanzp | r/GeminiAI | 0 | 10 | 09:43 | Žádný Gemini Pro 3.1 ani pro uživatele „Google Pro“ 😑 Jak chamtivý můžeš být, Google? Když Gemini už ani není v žebříčku. |
| 1wl1wi6 | r/GeminiAI | 0 | 11 | 02:12 | Gemini 4? |
| 1wlqbtb | r/LLMDevs | 0 | 11 | 21:27 | Pořadník na Jev |
| 1wlu9gn | r/LocalLLM | 0 | 13 | 23:59 | Jsme malá AI laboratoř a hledáme 10 vývojářů ke slepému testování naší nové metody dolaďování pro programovací úlohy (na oplátku 100 tisíc úvodních tokenů zdarma a čím víc zpětné vazby dáte, tím víc tokenů dostanete). |
| 1wlt639 | r/LocalLLM | 0 | 14 | 23:15 | Nejlepší GPU pro běh lokálního LLM |
| 1wlshjc | r/LocalLLM | 0 | 24 | 22:48 | Může Mac Mini s 64 GB nahradit moje AI předplatné na programování? |
| 1wlmj6e | r/LocalLLM | 0 | 32 | 19:04 | 8x 256GB M5Us, nebo GB300? |
| 1wlgppi | r/LocalLLM | 0 | 17 | 15:10 | Proč nezkusíme na modelu použít kompresní techniky? |
| 1wlflya | r/LocalLLM | 0 | 37 | 14:19 | Podvědomí agenti / subprocessová AI |
| 1wlacvz | r/LocalLLM | 0 | 42 | 09:25 | Dobré lokální LLM |
| 1wkzwye | r/LocalLLM | 0 | 18 | 00:43 | Přesvědčte mě, ať tenhle šílený nápad nedělám |
| 1wlnl01 | r/LocalLLaMA | 0 | 46 | 19:44 | Lidi, Jev je podvod |
| 1wlklqx | r/LocalLLaMA | 0 | 15 | 17:51 | Přecházím z RTX 3060 na RTX 5070 Ti, prosím o tipy |
| 1wlic2r | r/LocalLLaMA | 0 | 40 | 16:20 | Lokální modely pro osobní agenty. Vyplatí se to? |
| 1wlhmjh | r/LocalLLaMA | 0 | 43 | 15:50 | Jsou dnešní agenti dostatečně důvěryhodní, abyste jim dali plný přístup ke svému PC? |
| 1wldx6n | r/LocalLLaMA | 0 | 42 | 12:51 | Je teď špatná doba na koupi Strix Halo? |
| 1wlbqnl | r/LocalLLaMA | 0 | 23 | 10:44 | Lepší paměť pro vaše agenty — nepotřebujete produkt, jen filozofii |
| 1wlazxc | r/LocalLLaMA | 0 | 13 | 10:02 | Režie předcachování kontextu (systémový prompt, nástroje, dovednosti, …)? |
| 1wl9uws | r/LocalLLaMA | 0 | 14 | 08:58 | Je bezplatný Opencode rozbitý? |
| 1wl6qsj | r/LocalLLaMA | 0 | 83 | 06:11 | Hledám levnou GPU pro LLM |
| 1wl2zmt | r/LocalLLaMA | 0 | 11 | 03:03 | Jaký je váš agentní poměr tokenů? |
| 1wl2ey8 | r/LocalLLaMA | 0 | 18 | 02:36 | Jaké byly vaše zkušenosti s během Q1 modelů na vašem stroji? |
| 1wl0gfo | r/LocalLLaMA | 0 | 133 | 01:07 | Mám vzdát lokální AI, když si nemůžu dovolit RTX 6000 Pro? |
| 1wlq7m3 | r/OpenAI | 0 | 17 | 21:22 | Oslabili Astra? |
| 1wllzfx | r/OpenAI | 0 | 11 | 18:43 | Buď je Astra oslabená, nebo nám k ní nikdy pořádně nedali přístup |
| 1wlk0ij | r/OpenAI | 0 | 52 | 17:27 | Bill Gates navrhuje upravit daňový systém a zdanit automatizaci: „Pokud robot dělá totéž co vy, je normální ho zdanit.“ |
| 1wlj052 | r/OpenAI | 0 | 15 | 16:47 | Ukradla OpenAI skutečně řešení Navierových–Stokesových rovnic, |
| 1wlho8f | r/OpenAI | 0 | 13 | 15:52 | Neuvěřitelně nadšený: nikdy jsem neviděl, aby jednoduchý prompt trval tak dlouho, je to moje vůbec nejdelší generování v jednom chatu. (Uživatel Plus, úsilí: vysoké) |
| 1wlertd | r/OpenAI | 0 | 20 | 13:37 | Je znepokojivé, jak nás všechny americké elity začínají strašit AI a chtějí všechno zpomalit jen proto, že je Čína předstihne. |
| 1wlb8on | r/OpenAI | 0 | 10 | 10:16 | Co to sakra je za odkazy, které prochází GPT 6 Pro? |
| 1wl1lyq | r/OpenAI | 0 | 15 | 01:59 | Jak zařídit, aby AI souboje v manze působily jako skutečná manga, a ne jako prezentace? |
| 1wlr7fd | r/StableDiffusion | 0 | 16 | 22:00 | Je uzavřený zdrojový kód pro AI generování SKUTEČNĚ lepší? |
| 1wlbjqq | r/StableDiffusion | 0 | 11 | 10:33 | Zuby, tváře a oči – LTX-2.5 |
| 1wlaibp | r/StableDiffusion | 0 | 20 | 09:34 | Na conech prodávají AI obrázky, 50 $ za kus |
| 1wlg2uc | r/agi | 0 | 12 | 14:41 | Latentní prostor – aneb naše realita je singularita |
| 1wlfjj9 | r/agi | 0 | 14 | 14:15 | „Digitální moucha“ dokazuje, že AGI je skutečná |
| 1wlc8wa | r/agi | 0 | 21 | 11:15 | Proč by AI vytvářela něco chytřejšího, než je sama, když to nemůže ovládat? |
| 1wlqiks | r/artificial | 0 | 16 | 21:34 | Ztratili jsme už kontrolu nad AI? |
| 1wlqaas | r/artificial | 0 | 78 | 21:25 | Proč jsou hráči, a zejména indie hráči, tak extrémně proti AI |
| 1wljgs2 | r/artificial | 0 | 17 | 17:06 | Programování obrovských systémů běžnými slovy – „Word Coding“ |
| 1wl8w1w | r/artificial | 0 | 31 | 08:05 | Parta hlásající AI zkázu používá důkazy, které mluví proti ní, a nikdo si toho nevšiml |
| 1wln9wn | r/comfyui | 0 | 11 | 19:33 | Upozornění před instalací MiniMax H3 do ComfyUI: licence neplatí v USA, EU, Velké Británii ani Jižní Koreji |
| 1wlgih6 | r/singularity | 0 | 71 | 15:01 | Kontrola reality – oznámení – jak o AI smýšlejí normies: |
| 1wlb6l9 | r/singularity | 0 | 29 | 10:13 | Jsme na pokraji evoluce? |
| 1wl8zz7 | r/singularity | 0 | 26 | 08:11 | Jsou volání po zpomalení AI jen slaměný panák? |
| 1wl7lvh | r/singularity | 0 | 11 | 06:56 | Myslí si ještě někdo, že ty historky o hacknutí AI firem jsou až příliš velká náhoda? |
| 1wl0w65 | r/singularity | 0 | 63 | 01:26 | Asi jsem vyšinutý a šílený, protože začínám věřit některým konspiračním teoriím. |
