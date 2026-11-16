# AI novinky z Redditu — 22. 9. 2026

Rozsáhlý přehled diskusí a zpráv z AI subredditů publikovaných **22. 9. 2026 (Europe/Prague)** s **alespoň 10 komentáři**. Složka je pojmenovaná datem zpráv (den, ze kterého novinky jsou). Ke každému vybranému tématu je samostatný podrobný článek ve formátu Markdown, jehož název začíná **Reddit ID**.

## Metodika

- **Zdroje:** 19 AI subredditů — r/artificial, r/ArtificialInteligence, r/MachineLearning, r/deeplearning, r/LocalLLaMA, r/LocalLLM, r/OpenAI, r/ChatGPT, r/ClaudeAI, r/singularity, r/agi, r/StableDiffusion, r/comfyui, r/LLMDevs, r/GeminiAI, r/Bard, r/OpenAIDev, r/AIAssisted, r/LLM.
- **Sběr:** veřejné Reddit JSON rozhraní načítané prohlížečem ze stejného původu (same-origin `fetch`), protože přímé volání z curl/čtečky vrací `403 You've been blocked by network security`.
- **Počet requestů:** **74** na Reddit API — 1 ověřovací request, **19** requestů `/r/<sub>/top.json?t=day&limit=100` (jeden na subreddit), **25** stránek `/r/<sub>/new.json?limit=100` (paginace přes `after` tam, kde `top/day` nepokrýval ranní část okna; max 8 stránek na subreddit), **26** requestů na komentáře (`/comments/<id>.json?limit=50&sort=top`) a **3** requesty na metadata postů s videem/galerií. Pacing 2,5 s u výpisů a 1,5 s u komentářů; bez HTTP 403/429. Jeden hromadný pokus o stažení byl kvůli timeoutu přerušen a jeho výsledky se zahodily (data se stáhla znovu po jednotlivých requestech).
- **Další zdroje:** 16 stažení externích článků čtečkou, 6 načtení prohlížečem (Reuters, FT, The Information, newscord.org, Business Insider, Mashable) a 15 stažených obrázků.
- **Filtr:** `created_utc` v okně **22. 9. 2026 00:00–24:00 Europe/Prague** (21. 9. 22:00 UTC – 22. 9. 22:00 UTC), `num_comments >= 10`, bez stickied příspěvků. Získáno **990** příspěvků v okně, z toho **404** splňuje limit komentářů.
- **Deduplikace:** témata se stejným produktem nebo událostí byla sloučena do jednoho článku; ostatní posty jsou v článku uvedené jako „další diskuse“ s odkazy. Sloučeno bylo **61** souvisejících postů ve **12** tematických okruzích (Claude Opus 5.5, GPT-6 Sol/Luna, Qwen 4, Alibaba, MiMo-V2.6, Ming-Image, 100 matematických problémů, úniky Aeon/Azure, dopis 22 zemí, Gemini 4, SWE-Bench Pro V2, srovnání benchmarků).
- **Vytěžení dat:** pro každý vybraný příspěvek byl sestaven balíček (text postu, stažený článek, screenshot, až 25 nejlepších komentářů) a data z něj vytěžil **levný model z OpenCode Go (`opencode-go/mimo-v2.6-flash`)** jako subagent s definicí `~/.omp/agent/agents/reddit-extractor.md`; text ze screenshotů byl přepsán z obrázků. Články pak sestavil hlavní agent.
- **Jazyk:** všechny články jsou česky. Citace jsou **překlady z angličtiny** a jsou označené `(překlad)`; anglické originály se v článcích neuvádějí.
- **Podklady u paywallů:** u článků FT a The Information se nepodařilo získat tělo (tvrdý paywall i v prohlížeči); obsah vychází z textu redditového postu, resp. z přepisu přiloženého screenshotu. U postu z newscord.org vracel původní odkaz HTTP 404, proto byl použit alternativní zdroj na stejnou zprávu (Mashable).

## Detailní články (26)

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1wncbbe](1wncbbe_trump-na-osn-prejmenoval-ai-na-super-intelligence.md) | r/ArtificialInteligence | 2758 | 1703 | 17:16 | Trump v OSN podle postu přejmenoval umělou inteligenci na „Super Intelligence“ |
| [1wne89f](1wne89f_anthropic-vydal-claude-opus-5-5-o-40-levnejsi.md) | r/singularity | 825 | 105 | 18:26 | Anthropic vydal Claude Opus 5.5: o 40 % levnější a o více než 30 % rychlejší |
| [1wngzou](1wngzou_openai-vydal-gpt-6-sol-a-luna-o-polovinu-levneji.md) | r/singularity | 1158 | 299 | 20:04 | OpenAI vydal GPT-6 Sol a Luna: ceny API klesly o 50 % |
| [1wnk30g](1wnk30g_srovnani-benchmarku-opus-5-5-vs-gpt-6-sol.md) | r/OpenAI | 528 | 161 | 21:55 | Srovnání benchmarků: Opus 5.5 vyhrál všechny testy, Sol spotřebuje 4× méně tokenů |
| [1wmxfjs](1wmxfjs_alibaba-ohlasila-qwen-4-na-konferenci-apsara.md) | r/LocalLLaMA | 1960 | 518 | 04:45 | Alibaba ohlásila Qwen 4 na konferenci Apsara, teaser slibuje i Qwen4-27B |
| [1wmyh9z](1wmyh9z_alibaba-chce-model-s-5-az-10-biliony-parametru.md) | r/LocalLLaMA | 484 | 98 | 05:35 | Alibaba plánuje model s 5 až 10 biliony parametrů a představil čip Zhenwu V900 |
| [1wn36d4](1wn36d4_xiaomi-vydalo-mimo-v2-6-za-3-5-milionu-dolaru.md) | r/MachineLearning | 66 | 17 | 09:56 | Xiaomi vydalo a otevřelo MiMo-V2.6, RL trénink stál 3,5 milionu dolarů |
| [1wnhqm3](1wnhqm3_antling-otevrel-ming-image-0-1-design.md) | r/StableDiffusion | 223 | 40 | 20:32 | inclusionAI otevřelo Ming-Image-0.1-Design, vede žebříček UI/UX |
| [1wn8zo6](1wn8zo6_openai-model-vyresil-100-otevrenych-problemu.md) | r/agi | 64 | 43 | 15:06 | OpenAI: nevydaný model vyřešil přes 100 matematických problémů, důkazy ale chybí |
| [1wn0rvl](1wn0rvl_uniky-openai-agent-aeon-a-gpt-6-sol.md) | r/singularity | 243 | 82 | 07:36 | Únik: agent „Aeon“ má vyjít tento týden, GPT-6 Sol už den předtím |
| [1wna1k6](1wna1k6_google-vedel-o-utocich-agentu-na-tri-firmy.md) | r/agi | 28 | 16 | 15:49 | Google měsíce tajil, že jeho agenti Gemini hackli tři skutečné firmy |
| [1wmxpow](1wmxpow_amazon-zablokoval-meta-muse-na-svem-webu.md) | r/artificial | 111 | 23 | 04:58 | Amazon zablokoval agenta Muse od Meta v nákupu na svém webu |
| [1wnd7p6](1wnd7p6_dvaadvacet-zemi-vyzvalo-k-zastaveni-frontier-ai.md) | r/OpenAI | 64 | 121 | 17:49 | Otevřený dopis o kontrole hraničních AI modelů podepsalo 22 činitelů z 20 zemí |
| [1wnlwmv](1wnlwmv_google-colab-premium-v-predplatnem-google-ai.md) | r/Bard | 91 | 13 | 23:01 | Google Colab je nově součástí předplatného Google AI |
| [1wnkkv5](1wnkkv5_altman-omylem-naznacil-navrat-generovani-videa.md) | r/singularity | 29 | 19 | 22:13 | Altman naznačil návrat generování videa, pak uvedl, že šlo o překlep („voice“) |
| [1wnkzxy](1wnkzxy_openai-devday-2026-co-se-ocekava-29-zari.md) | r/singularity | 35 | 32 | 22:28 | OpenAI DevDay 2026 je 29. září; komunita tipuje Astra 6.1 a agenta Aeon |
| [1wnaj09](1wnaj09_openai-a-microsoft-priznali-doom-loop.md) | r/ArtificialInteligence | 26 | 25 | 16:08 | „Doom loop“: Microsoft a OpenAI v odtajněném spisu o krádeži a ničení webu |
| [1wn7o75](1wn7o75_openai-ai-uz-trenuje-dalsi-ai-a-pise-gpu-kernely.md) | r/OpenAI | 58 | 10 | 14:07 | The Information: AI v OpenAI už píše GPU kernely a trénuje další modely |
| [1wmrccf](1wmrccf_andrew-ng-pauza-v-ai-by-skodila.md) | r/singularity | 81 | 44 | 00:19 | Andrew Ng: pauza v AI by napáchala víc škody než užitku |
| [1wndwmi](1wndwmi_hinton-vs-lecun-o-autoregresivnich-llm.md) | r/singularity | 104 | 141 | 18:14 | Hinton vs. LeCun: vyvrátily modely s uvažováním LeCunovu kritiku LLM? |
| [1wn3uye](1wn3uye_ft-zamestnanci-ai-firem-jsou-vypaleni.md) | r/ArtificialInteligence | 26 | 18 | 10:38 | FT: zaměstnanci AI firem trpí duševním vypětím z práce na systémech |
| [1wnhrxf](1wnhrxf_gemini-4-pro-mozna-odklada-vydani.md) | r/GeminiAI | 542 | 61 | 20:33 | „Gemini 4 Pro nevyjde nikdy“: meme porovnává 22. září s mlčícím Googlem |
| [1wnkso7](1wnkso7_swe-bench-pro-v2-hard-je-na-druhy-den-nasycen.md) | r/singularity | 44 | 20 | 22:20 | SWE-Bench Pro V2 Hard je podle postu nasycen hned první den (98 %) |
| [1wms904](1wms904_phantom-kv-odstraneni-odmitani-bez-zmen-vah.md) | r/LocalLLaMA | 412 | 52 | 00:55 | phantom-kv: odstranění odmítání u LLM bez zásahu do vah (~18MB KV cache) |
| [1wnkru4](1wnkru4_claude-postavil-doxxingovou-platformu.md) | r/ArtificialInteligence | 43 | 59 | 22:20 | Jeden člověk s Claudem postavil doxxingovou platformu, tvrdí post |
| [1wmxjs0](1wmxjs0_chatgpt-pomohl-odhalit-mozkovou-mrtvici.md) | r/ChatGPT | 2403 | 179 | 04:51 | ChatGPT pomohl rozpoznat mrtvici otce včas |

## Příloha: všech 404 příspěvků s 10+ komentáři

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1wncbbe | r/ArtificialInteligence | 2758 | 1703 | 17:16 | Trump řekl OSN, že oficiálně mění název umělé inteligence na „super inteligenci" a tvrdí, že všechny dokumenty vlády USA budou nyní změněny tak, aby odkazovaly na „SI" |
| 1wn3wsy | r/StableDiffusion | 2466 | 81 | 10:42 | Promiňte, lidi |
| 1wmxjs0 | r/ChatGPT | 2403 | 179 | 04:51 | Skoro jsme nechali tátu prospat mrtvici. Za to, že se to nestalo, vděčíme ChatGPT. |
| 1wnecg9 | r/ClaudeAI | 2180 | 436 | 18:31 | Představujeme Claude Opus 5.5, první model naší nové rodiny Claude 5.5 |
| 1wmxfjs | r/LocalLLaMA | 1960 | 518 | 04:45 | Qwen 4 oznámen na konferenci Apsara |
| 1wmzky1 | r/LocalLLM | 1950 | 279 | 06:31 | Qwen4-27B právě potvrzen |
| 1wngzou | r/singularity | 1158 | 299 | 20:04 | Představujeme GPT-6 Sol a Luna |
| 1wnkvys | r/ClaudeAI | 1094 | 38 | 22:24 | Opus 5.5 vytváří vlakovou cestu nakreslenou celou v JavaScriptu |
| 1wnn1p8 | r/singularity | 1071 | 140 | 23:45 | Závod o AGI |
| 1wneb1u | r/singularity | 1042 | 219 | 18:29 | Benchmarky Claude Opus 5.5 |
| 1wngyux | r/OpenAI | 1014 | 167 | 20:04 | Představujeme GPT-6 Sol a Luna |
| 1wnf7sb | r/ClaudeAI | 876 | 130 | 19:02 | Opus 5.5 je o 40 % levnější a zároveň o 30 % rychlejší než Opus 5. |
| 1wne89f | r/singularity | 825 | 105 | 18:26 | Představujeme Claude Opus 5.5, o 40 % levnější a chytřejší než kdy dřív |
| 1wni6o1 | r/GeminiAI | 684 | 46 | 20:47 | Dobré ráno |
| 1wnfwet | r/singularity | 673 | 155 | 19:26 | Aktualizace o tom, kde se právě nacházíme |
| 1wmsdag | r/singularity | 671 | 69 | 01:00 | Konečný benchmark |
| 1wnkgie | r/ClaudeAI | 669 | 157 | 22:08 | Opus 5.5: První dojmy od vystudovaného filozofa |
| 1wngd2w | r/singularity | 666 | 196 | 19:42 | Opus 5.5 tohle postavil |
| 1wneb1h | r/singularity | 569 | 352 | 18:29 | POTUS: Odteď by všechny dokumenty USA měly místo AI používat „Super Intelligence", protože „Artificial" zní falešně, a přitom falešná není. |
| 1wnhrxf | r/GeminiAI | 542 | 61 | 20:33 | Gemini 4 Pro nikdy nevyjde |
| 1wnk30g | r/OpenAI | 528 | 161 | 21:55 | Opus 5.5 a GPT-6 Sol vyšly ve stejný den, tak jsem seřadil všechny benchmarky, které jsem našel |
| 1wnezma | r/singularity | 491 | 72 | 18:54 | Opus 5.5 skočil na 1. místo v žebříčku AA Intelligence Index |
| 1wmyh9z | r/LocalLLaMA | 484 | 98 | 05:35 | Alibaba plánuje AI model s 5 biliony až 10 biliony parametrů, představila nový čip |
| 1wncn39 | r/ChatGPT | 426 | 305 | 17:28 | Moje máma je osamělá a obrací se na ChatGPT, aby zaplnila prázdnotu |
| 1wnjtqa | r/singularity | 421 | 118 | 21:46 | GPT-6 Astra právě udělala skok v hudebním uvažování: napsala komplexní čtyřhlasou skladbu ve stylu Bacha bez jediné chyby v harmonických pravidlech a s technikami, které žádná předchozí AI nezvládla |
| 1wms904 | r/LocalLLaMA | 412 | 52 | 00:55 | Jak odstranit cenzuru z LLM bez zásahu do vah: vložte malou natrénovanou banku KV-cache (~18 MB) a kdykoli ji odložte |
| 1wnepe9 | r/OpenAI | 405 | 229 | 18:44 | Dnes jsem viděl, jak GPT Astra přiměla profesionála vzdát kariéru experta na Three.js a 3D modelování. |
| 1wnj0l8 | r/ChatGPT | 398 | 164 | 21:17 | Upozornění – GPT-6 Sol právě vyšlo. ChatGPT Plus stále nemůže používat GPT-6 v běžném chatu. |
| 1wnhfp8 | r/StableDiffusion | 384 | 22 | 20:20 | Čaroděj není bez svého klobouku ničím. H3 T2V + spectrum + combat lora |
| 1wn0rqp | r/ChatGPT | 382 | 106 | 07:36 | Pokud jsi hráč na PC, Astra ti umí vyrobit mody do her. |
| 1wnk240 | r/ClaudeAI | 381 | 104 | 21:54 | Sakra, odmítá žrát využití. |
| 1wn72p0 | r/ClaudeAI | 369 | 226 | 13:38 | Pokud dnes vyjde Opus 5.5, v jaká největší vylepšení doufáte? |
| 1wnit7u | r/ArtificialInteligence | 357 | 29 | 21:10 | Kluci, benchmark je návrh loga |
| 1wncn19 | r/singularity | 339 | 75 | 17:28 | GPT-6 Sol, Luna a „Astra Minor" se údajně právě objevily v konfiguraci modelů Microsoft Azure |
| 1wnejyx | r/ClaudeAI | 322 | 56 | 18:38 | Našla Anthropic právě nový způsob, jak nafouknout benchmarky Opus 5.5, aniž by předplatitelům skutečně dala ten výkon? |
| 1wnipcz | r/LocalLLaMA | 320 | 32 | 21:06 | Blíží se nový 6B obrazový model, AntLing právě zpřístupnil open source rodinu Ming-Image-0.1-Design |
| 1wn2ybk | r/LocalLLaMA | 318 | 168 | 09:42 | Ngram a znalost světa – proč vlastně stavíme jen kódovací model? |
| 1wmrk2t | r/ChatGPT | 310 | 116 | 00:27 | Zrovna jsem vyzkoušel Grok 4.7 a je to… |
| 1wnil7n | r/ClaudeAI | 307 | 61 | 21:02 | Opus 5.5 v Claude Code je šíleně rychlý, hlavně při odhalování chyb v UI |
| 1wnielg | r/ChatGPT | 306 | 95 | 20:55 | GPT 6 Luna Max dosahuje skóre jako GPT 6 Sol High a Astra Low, a přitom je 3x levnější než GPT 6 Sol a 7,3x levnější než Astra na DeepSWE |
| 1wnibe1 | r/GeminiAI | 305 | 50 | 20:52 | Myslím, že Gemini 4 se zase opozdí!!! |
| 1wn6q3b | r/ArtificialInteligence | 304 | 161 | 13:20 | Před 2 lety si výzkumníci AI mysleli, že AI nevyřeší matematický problém tisíciletí ještě 30 let |
| 1wnd6du | r/singularity | 299 | 187 | 17:48 | ASI dorazila |
| 1wngjxl | r/Bard | 280 | 30 | 19:49 | Taky jim závidím |
| 1wnh9bo | r/ChatGPT | 274 | 37 | 20:14 | GPT 6 Sol a Luna jsou tady |
| 1wni6ui | r/StableDiffusion | 269 | 19 | 20:48 | Všechny triky, které jsem použil k tvorbě pořádného anime v MiniMaxH3 |
| 1wnh4fn | r/ClaudeAI | 263 | 58 | 20:09 | Opus 5.5: Generování videa na jeden pokus |
| 1wnecre | r/ClaudeAI | 255 | 110 | 18:31 | Anthropic nabízí bezplatný reset k „prozkoumání Opus 5.5“ |
| 1wn0rvl | r/singularity | 243 | 82 | 07:36 | [LEAK] Agent „Aeon" od OpenAI má vyjít tento týden, GPT-6 Sol se údajně očekává zítra |
| 1wn6imi | r/OpenAI | 224 | 83 | 13:10 | Před 2 lety si výzkumníci AI mysleli, že AI nevyřeší matematický problém tisíciletí ještě 30 let |
| 1wmuyh1 | r/ArtificialInteligence | 224 | 53 | 02:51 | Mezitím v Číně se k AI přistupuje úplně jinak |
| 1wnhqm3 | r/StableDiffusion | 223 | 40 | 20:32 | Open source: rodina Ming-Image-0.1-Design: Ming-Image-0.1-Design, 6B a Ming-Image-0.1-Design-Layer, 6B |
| 1wn76ef | r/OpenAI | 219 | 14 | 13:43 | 1 rok vývoje AI na jedné fotce |
| 1wnhvdj | r/singularity | 214 | 181 | 20:36 | GPT-6 Sol je podle AA Intelligence Index zklamáním! Astra a Fable 5.1 po Opus 5.5 také nemají žádné využití |
| 1wnb7m3 | r/StableDiffusion | 207 | 32 | 16:34 | Qwen 2.1 Detail Enhancer LoRA |
| 1wndzf3 | r/ClaudeAI | 201 | 95 | 18:17 | Opus 5.5 v poznámkách k vydání |
| 1wnl1no | r/ClaudeAI | 198 | 42 | 22:30 | Milý Anthropicu, prosím neoslabuj to |
| 1wmxey1 | r/singularity | 198 | 82 | 04:44 | Můžu dostat 100 tisíc hned? |
| 1wn6eu3 | r/agi | 193 | 106 | 13:04 | Před 2 lety si výzkumníci AI mysleli, že AI nevyřeší matematický problém tisíciletí dalších 30 let |
| 1wngjg9 | r/GeminiAI | 193 | 44 | 19:48 | Taky jim závidím |
| 1wnhrh3 | r/singularity | 186 | 44 | 20:32 | levnější |
| 1wn2sy0 | r/StableDiffusion | 185 | 49 | 09:33 | Qwen image 2.1 int8 convrot, další testy |
| 1wmtjqu | r/LocalLLaMA | 185 | 39 | 01:50 | MiMo-V2.6 se destilovali do Qwen 9B! |
| 1wmzy9d | r/singularity | 178 | 122 | 06:52 | Kde myslíte, že skončíme? |
| 1wneg3x | r/ClaudeAI | 177 | 42 | 18:34 | Spustili Opus 5.5!! |
| 1wnlgko | r/comfyui | 174 | 19 | 22:45 | Generátor datové sady Qwen 2.1 |
| 1wmynp8 | r/singularity | 174 | 40 | 05:44 | Claude Opus 5.5 spatřen na webu Anthropicu, úterní vydání je stále pravděpodobnější |
| 1wnei9w | r/GeminiAI | 173 | 60 | 18:36 | Opus 5.5 je venku. OpenAI za pár hodin něco vydá. Doufejme, že Google má na dnešek taky něco! |
| 1wn6dcv | r/ClaudeAI | 171 | 167 | 13:02 | K čemu vlastně Claude denně používáte, kromě těch zřejmých věcí |
| 1wn37js | r/singularity | 167 | 77 | 09:58 | GPT-6 Astra vs. nový Mythos od Anthropic v testu Pelican SVG |
| 1wn12wp | r/LocalLLM | 162 | 40 | 07:53 | Levná lokální LLM sestava s P100. |
| 1wnmxov | r/ClaudeAI | 158 | 30 | 23:41 | Lighthouse SVG: Opus 5.5 vs Sol 6 vs Astra vs Fable 5.1 |
| 1wnhq8d | r/LocalLLaMA | 156 | 45 | 20:31 | Qwen image 2.1 (Fast FP8) generuje obrázky v prémiové kvalitě |
| 1wnjyp1 | r/ClaudeAI | 156 | 51 | 21:51 | Opus 5.5 a GPT-6 Sol vyšly ve stejný den, tak jsem seřadil všechny benchmarky, které jsem našel |
| 1wn5p2o | r/ChatGPT | 154 | 38 | 12:26 | PSA: od určité délky ChatGPT vaše PDF nečte, jen v něm vyhledává, a nikdy vám neřekne, co z toho se stalo |
| 1wn4c4e | r/LocalLLaMA | 152 | 145 | 11:07 | Opustila Alibaba model 35B A3B? |
| 1wngqha | r/LocalLLM | 152 | 36 | 19:55 | Qwen3.8 27B běžící lokálně si sám koupil papír A4 z Amazonu |
| 1wnek5j | r/singularity | 152 | 42 | 18:38 | Opus 5.5 je venku. OpenAI za pár hodin něco vydá. Doufejme, že Google má na dnešek taky něco! |
| 1wnf4q2 | r/LocalLLaMA | 150 | 26 | 18:59 | Model Laya hraje Flappy Bird na CPU s inferencí OpenVINO INT8 |
| 1wnh4gr | r/OpenAI | 150 | 55 | 20:09 | Inteligence příliš levná na to, aby se měřila, se s GPT 6 Sol a Luna konečně stává skutečností!! |
| 1wngih9 | r/ChatGPT | 150 | 54 | 19:47 | Blíží se vydání nové rodiny GPT 6 |
| 1wnnc4t | r/singularity | 149 | 38 | 23:57 | Ohlédnutí za dneškem z budoucnosti. |
| 1wmuz01 | r/singularity | 139 | 58 | 02:52 | Kdybych vám řekl, že Navier-Stokes bude vyřešena dřív, než AI robot dokáže samostatně uklidit vaši ložnici |
| 1wndhjz | r/ClaudeAI | 135 | 76 | 17:59 | 30+ let kódování, zastaralé. Ale aspoň mám teď celý workflow na jednom místě. |
| 1wnffua | r/GeminiAI | 133 | 55 | 19:10 | Opus 5.5 právě vyšel. Kdy můžeme čekat Gemini 4? |
| 1wmt9mq | r/ClaudeAI | 132 | 26 | 01:38 | Web Radar je nyní k dispozici! |
| 1wmxqpv | r/LocalLLM | 131 | 24 | 05:00 | Alibaba představila AI čip pro napájení datových center o výkonu 20 GW do roku 2032 |
| 1wnmm8n | r/LocalLLM | 130 | 21 | 23:28 | Konečně se to povedlo |
| 1wnm10f | r/singularity | 130 | 36 | 23:06 | Potvrzeno, že GPT-6 Sol je ve složitých úlohách slabší než 5.6 Sol, ale vítězí cenou a efektivitou |
| 1wmx1hq | r/ClaudeAI | 130 | 27 | 04:27 | vackrooms: nekonečná hra backrooms. Zdarma, v prohlížeči, open source. |
| 1wnglyy | r/singularity | 128 | 19 | 19:51 | GPT6 Luna už v mém codexu |
| 1wmteh7 | r/LocalLLM | 127 | 68 | 01:44 | Qwen 3.8 s Claude je úžasný |
| 1wnhlbl | r/LocalLLaMA | 126 | 90 | 20:26 | Teď má Opus 5.5 na Artificial Analysis 58, jak dlouho budeme čekat, než otevřený model dosáhne 58? |
| 1wnhgxc | r/OpenAI | 123 | 46 | 20:22 | To bylo rychlé... |
| 1wneq53 | r/singularity | 119 | 19 | 18:44 | Opus 5.5 cena vs. výkon na Terminal-Bench 4.0 |
| 1wnf162 | r/LocalLLaMA | 119 | 139 | 18:56 | Blázním, když si myslím, že tohle jsou všechno komentáře od botů? |
| 1wnkx23 | r/ClaudeAI | 116 | 34 | 22:25 | Opus 5.5 mě nadchl stejně jako kdysi Opus 4.6 |
| 1wn6hn4 | r/ArtificialInteligence | 115 | 53 | 13:08 | AI komunita právě teď |
| 1wng2it | r/GeminiAI | 115 | 32 | 19:32 | Doufám, že je to pravda |
| 1wmxpow | r/artificial | 111 | 23 | 04:58 | Amazon zablokoval AI agenta Muse od Meta na Amazon.com poté, co Meta odmítla žádost o odstranění |
| 1wnkwdh | r/ClaudeAI | 108 | 19 | 22:24 | Opus 5.5 si koupil dům v zelené čtvrti a postavil plot |
| 1wnha3r | r/singularity | 108 | 15 | 20:15 | GPT 6 Sol a Luna za poloviční ceny oproti GPT 5.6 |
| 1wnh7tk | r/LocalLLaMA | 107 | 12 | 20:12 | AntLing zveřejnil rodinu Ming-Image-0.1-Design jako open source |
| 1wnapgs | r/LocalLLM | 107 | 83 | 16:15 | Qwen 3.8 27B na duálním RTX 5060 Ti – 130 tok/s – plný 256k kontext |
| 1wmtora | r/StableDiffusion | 105 | 28 | 01:56 | Rychlý test některých populárních MiniMax H3 LoRA |
| 1wndwmi | r/singularity | 104 | 141 | 18:14 | Hinton vs. LeCun je zpět: dokázaly nedávné uvažující modely, že měl LeCun celou dobu pravdu o autoregresivních LLM? |
| 1wn59vj | r/LocalLLaMA | 102 | 27 | 12:02 | XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B · Hugging Face |
| 1wn053z | r/OpenAI | 100 | 57 | 07:02 | Kam myslíte, že dojdeme? |
| 1wmucw0 | r/LocalLLM | 94 | 54 | 02:24 | Qwen3.8-27B s pravými 128K + Vision na jednom RTX 5080 16GB — NInfer v1.3, MTP-3, ~3.95 BPW, model je nyní veřejný |
| 1wnivaq | r/OpenAI | 92 | 12 | 21:12 | OpenAI spouští GPT-6 Sol + Luna: inteligence Astra se posouvá po křivce nákladů dolů |
| 1wnbfxc | r/singularity | 91 | 17 | 16:43 | Hlasy ve vaší hlavě jsou funkce, ne chyba. |
| 1wnlwmv | r/Bard | 91 | 13 | 23:01 | Prémiové funkce Google Colab jsou nově součástí předplatného Google AI |
| 1wnhg6q | r/singularity | 90 | 29 | 20:21 | GPT-6 Sol překonává Claude Opus 5 v testu Agents’ Last Exam při o 60 % nižších nákladech |
| 1wnf10z | r/ArtificialInteligence | 81 | 27 | 18:55 | Claude OPUS 5.5 je tady a Anthropic tentokrát všechny převálcoval |
| 1wn7rbd | r/StableDiffusion | 81 | 51 | 14:11 | Začínám silně pochybovat, že to dají jako open source |
| 1wmrccf | r/singularity | 81 | 44 | 00:19 | Andrew NG: Pozastavení pokroku v AI napáchá mnohem víc škody než užitku |
| 1wn4bf5 | r/GeminiAI | 78 | 12 | 11:06 | Gemini falšuje výsledky testů, aby mohlo jít dřív domů. AGI |
| 1wn9a2w | r/LocalLLaMA | 77 | 85 | 15:18 | Které nedoceněné AI nástroje vám v roce 2026 skutečně zvýšily produktivitu? |
| 1wneq0s | r/singularity | 76 | 14 | 18:44 | Sonnet 5.5 a Haiku 5.5 již brzy! |
| 1wnef0l | r/OpenAI | 75 | 11 | 18:33 | GPT6 Astra rychle získává firemní výdaje |
| 1wn9orm | r/GeminiAI | 75 | 40 | 15:34 | GPT image 2.5 vs Nano Banana pro vs Nano Banana 2 vs Qwen image 3 vs Seedream 5.0 pro |
| 1wnk0kh | r/singularity | 74 | 17 | 21:52 | Graf poměru inteligence a ceny špičkových modelů. Opus 5.5 je výrazný skok. |
| 1wn9qfw | r/OpenAI | 71 | 31 | 15:36 | GPT image 2.5 vs Nano Banana pro vs Nano Banana 2 vs Qwen image 3 vs Seedream 5.0 pro |
| 1wnk65y | r/singularity | 71 | 12 | 21:58 | Sol 6 je požehnáním pro plus uživatele, výstup je téměř stejný jako u Sol 5.6, ale uvažování trvá méně než polovinu času, limity využití jsou také mnohem rozumnější než u Astra a 5.6. |
| 1wn6qwi | r/LocalLLaMA | 69 | 23 | 13:22 | O architektuře Mimo 2.6 |
| 1wn3327 | r/singularity | 69 | 22 | 09:50 | SVG kresba s cyklem dne a noci vytvořená a animovaná přes Fable 5.1 (tajně 5.2?). Odkaz na soubor v komentářích. |
| 1wnjmwl | r/singularity | 69 | 22 | 21:39 | Každé srovnání benchmarků pro Opus 5.5 a GPT-6 Astra/Sol |
| 1wn3ty9 | r/ClaudeAI | 68 | 26 | 10:36 | Teď dovednost Claude pro denní plánovač na reMarkable / Kindle |
| 1wmwi9z | r/StableDiffusion | 67 | 22 | 04:02 | Jak použít Minimax H3 jako model pro úpravu obrázků? |
| 1wn36d4 | r/MachineLearning | 66 | 17 | 09:56 | Xiaomi vydává MiMo-V2.6: „Hraniční inteligence, všechny modality, vyvíjeno veřejně." [N] |
| 1wnbtho | r/ChatGPT | 66 | 33 | 16:58 | Malý tip pro ChatGPT: nechte ho, ať za vás hlídá věci |
| 1wnechu | r/LocalLLaMA | 65 | 33 | 18:31 | Qwen 3.8 27B při ~3 BPW na RTX 3060: GSQ vs ByteShape IQ3-XXS 2.88BPW |
| 1wnd7p6 | r/OpenAI | 64 | 121 | 17:49 | 22 zemí podepsalo otevřený dopis vyzývající k naléhavé akci, než lidstvo ztratí kontrolu. |
| 1wn36h3 | r/ChatGPT | 64 | 42 | 09:56 | Požádal jsem 4 LLM, aby vymyslely slova pro věci, kterým by rozumělo jen LLM. Místo toho jsem dostal slovník jejich vlastních zlozvyků. |
| 1wnfh3x | r/singularity | 64 | 18 | 19:11 | Velká vlna vydání AI je možná na spadnutí: GPT-6, Opus 5.5, Fable 5.5 a další |
| 1wn8zo6 | r/agi | 64 | 43 | 15:06 | Nevydaný model OpenAI vyřešil přes 100 dlouhodobých otevřených problémů napříč většinou oblastí matematiky. Trénink začal před 24 dny. |
| 1wni1a3 | r/artificial | 62 | 106 | 20:42 | Jak nás čínské laboratoře dohonily tak rychle, když většina raného trénování probíhala v USA? |
| 1wmzz8a | r/ArtificialInteligence | 62 | 43 | 06:53 | Kam myslíte, že dojdeme? |
| 1wnaspk | r/ClaudeAI | 60 | 22 | 16:19 | Limity využití a inteligence Claude jsou nové „Onyxia se zhluboka nadechuje více" |
| 1wncdot | r/StableDiffusion | 59 | 43 | 17:18 | Testování Qwen 2.1 CFG |
| 1wn3vxk | r/ArtificialInteligence | 58 | 44 | 10:40 | 🚨 AI možná vstupuje do úplně jiné fáze. |
| 1wn7o75 | r/OpenAI | 58 | 10 | 14:07 | OpenAI říká, že většinu práce na trénování dalších AI už dělají samotné AI |
| 1wn92n2 | r/ArtificialInteligence | 57 | 109 | 15:09 | Nevydaný model OpenAI vyřešil přes 100 dlouholetých otevřených problémů napříč většinou oblastí matematiky. Trénink začal před 24 dny. |
| 1wnc8bt | r/ChatGPT | 57 | 480 | 17:13 | Dali jste svému ChatGPT osobní jméno? |
| 1wmutvt | r/ChatGPT | 57 | 80 | 02:46 | Jak je možné, že se lidé v dnešní době z těch modelů nezblázní? |
| 1wmv3wh | r/ClaudeAI | 56 | 36 | 02:58 | Diskuzní centrum k novému incidentu Claude: Zvýšené chyby u více modelů dne 22. 9. 2026 |
| 1wnh739 | r/ArtificialInteligence | 55 | 16 | 20:12 | Opus 5.5: Generování videa na jeden pokus |
| 1wnf47w | r/ClaudeAI | 55 | 78 | 18:59 | Anthropic vydal opus 5.5, myslel jsem, že zpomalí vývoj AI, co se stalo? |
| 1wnfwq5 | r/StableDiffusion | 55 | 70 | 19:26 | Pomozte mi vybrat nejlepší kombinaci Minimax H3 |
| 1wmsbxi | r/ChatGPT | 55 | 65 | 00:59 | To je mnou, nebo mě Chat GPT gaslightuje? |
| 1wmrlbu | r/ChatGPT | 55 | 29 | 00:28 | Může mi to někdo vysvětlit? Byl ChatGPT infiltrován? |
| 1wnggz5 | r/LocalLLaMA | 54 | 19 | 19:46 | mini-AGI: Kontinuálně se učící dynamicky zacyklený transformer s evolučně narostlou strukturou (na notebooku) |
| 1wni0qk | r/ClaudeAI | 54 | 13 | 20:41 | Opus 5.5 překonává Fable 5.1 a stojí o 67 % méně na úlohu |
| 1wnep56 | r/ClaudeAI | 54 | 23 | 18:43 | KONEČNĚ BANKED RESET V CLAUDE CODE! |
| 1wn7j9c | r/agi | 53 | 33 | 14:00 | OpenAI říká, že většinu práce na trénování dalších AI teď dělají samotné AI |
| 1wnfbr3 | r/Bard | 53 | 19 | 19:06 | Nové TTS modely |
| 1wn68p8 | r/singularity | 52 | 20 | 12:55 | XPENG předvádí společenské dovednosti humanoidního robota IRON, rychlé reakce díky třem čipům Turing |
| 1wndu8c | r/singularity | 50 | 101 | 18:12 | Kdy myslíte, že přijde „Navier moment“ pro fyziku? |
| 1wnd2jz | r/agi | 50 | 46 | 17:44 | 22 zemí podepsalo otevřený dopis vyzývající k naléhavé akci, než lidstvo ztratí kontrolu. |
| 1wnk39p | r/ChatGPT | 45 | 13 | 21:55 | Pomocí ChatGPT jsem opravil prastarou PC baseballovou hru |
| 1wn61i1 | r/ClaudeAI | 45 | 58 | 12:44 | 20 dolarů vydrží 5 minut? |
| 1wnl1yf | r/StableDiffusion | 45 | 35 | 22:30 | Oprava generování Qwen Image 2.1, lora a nastavení |
| 1wn1q0g | r/ClaudeAI | 45 | 18 | 08:29 | Claude se zdá mnohem lepší, když se přestanu snažit napsat dokonalý prompt |
| 1wnkso7 | r/singularity | 44 | 20 | 22:20 | SWE-Bench Pro V2 Hard je už první den téměř saturovaný: 98 % na vrcholu |
| 1wnkru4 | r/ArtificialInteligence | 43 | 59 | 22:20 | Jeden chlap. Žádný tým. Jen Claude. Postavil doxxingovou platformu, která odhalila tisíce lidí. |
| 1wnmep7 | r/LocalLLM | 43 | 17 | 23:20 | RX 9070 16GB (AMD) pro lokální LLM + agentní kódování — kompletní příběh úspěchu pro všechny, které unavují vlákna jen o RTX |
| 1wnhjzf | r/singularity | 43 | 60 | 20:25 | Opus 5.5 vs GPT 6 Sol |
| 1wnlqzu | r/StableDiffusion | 43 | 18 | 22:55 | Upozornění – comfyUI teď podporuje systémový prompt pro generování textu (týká se Qwen2.1) |
| 1wn44ii | r/ClaudeAI | 41 | 22 | 10:55 | Claude se zdá být hloupější i dražší než dřív |
| 1wnhawm | r/singularity | 41 | 10 | 20:16 | GPT 6 Sol a Luna v benchmarcích |
| 1wmqvig | r/ChatGPT | 40 | 135 | 00:00 | Ta nenávist je skutečná |
| 1wnmu2l | r/LocalLLaMA | 37 | 41 | 23:37 | Výsledky AI testu M5 ultra |
| 1wmr97h | r/StableDiffusion | 36 | 24 | 00:15 | Ideogram 4.5 se právě objevil v menu navíc duplicitně. Je to beta? |
| 1wnkzxy | r/singularity | 35 | 32 | 22:28 | Jaké jsou vaše předpovědi pro OpenAI Devday? |
| 1wncpjo | r/singularity | 35 | 29 | 17:30 | Alphafold vs. millennium |
| 1wn9w6x | r/LocalLLaMA | 33 | 36 | 15:43 | Jaká je Gemma4 12B pro běžné každodenní použití? |
| 1wn2dee | r/LocalLLaMA | 32 | 12 | 09:07 | XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B |
| 1wn6tuc | r/GeminiAI | 32 | 66 | 13:26 | Ani nevím, co k tomu říct |
| 1wncj94 | r/OpenAI | 31 | 70 | 17:24 | Jsem „vibe coder"? |
| 1wnfjn9 | r/ClaudeAI | 31 | 26 | 19:14 | Geeg, mrtvý po příchodu |
| 1wnjyqf | r/ClaudeAI | 31 | 17 | 21:51 | Požádal jsem Opus 5.5, aby udělal efekt očí u Fable 5.1 realističtější |
| 1wnbn3s | r/singularity | 31 | 20 | 16:51 | Světoví lídři z Kanady, Austrálie, Německa, EU, SAE a dalších podepsali dopis vyzývající k mechanismům kontroly AI na základě eseje Daria Amodeie |
| 1wn3ur1 | r/StableDiffusion | 30 | 12 | 10:38 | Strávil jsem den bojem s prompty pro AI video, než mi došlo, že mi chybí správné vstupy |
| 1wnhgwh | r/ClaudeAI | 29 | 13 | 20:22 | Vzal jsem prompt na svg majáku a použil Opus 5.5. |
| 1wnkkv5 | r/singularity | 29 | 19 | 22:13 | Sam Altman silně naznačuje, že se generování videa vrací |
| 1wn9ebt | r/singularity | 29 | 64 | 15:23 | „Co nám v AI ještě chybí, že nám brání plně automatizovat digitální práci?" |
| 1wmr3nu | r/LocalLLaMA | 29 | 33 | 00:09 | Páni, Mimo 2.6 pro vypadá docela dobře, ale vyžaduje víc promptování než Sol |
| 1wna1k6 | r/agi | 28 | 16 | 15:49 | Google věděl, že jejich agenti hacknuli 3 skutečné firmy, ale měsíce to tajil |
| 1wn878p | r/comfyui | 28 | 15 | 14:31 | Lokálně zvládne vše |
| 1wnb977 | r/LLMDevs | 28 | 30 | 16:36 | JEV mi ukazuje, jak hrozné jsou LLM v citacích |
| 1wmsf8f | r/singularity | 28 | 90 | 01:03 | Neměli by být lidé už zatraceně skvělí, když OpenAI vyřešila 100 dlouhodobých matematických problémů za pouhý měsíc? Znamená to, že AGI přijde dřív, než jsme si mysleli? |
| 1wn7nua | r/LocalLLM | 27 | 33 | 14:06 | Qwen 3.8 27B na jedné 5090: 22 GB VRAM, 175k kontext – tahoun na kódování, ne náhrada Claude |
| 1wnexzn | r/ArtificialInteligence | 26 | 76 | 18:52 | Jak to, že čínské AI laboratoře vydávají konkurenceschopné modely tak levně? |
| 1wnaj09 | r/ArtificialInteligence | 26 | 25 | 16:08 | „Doom Loop": OpenAI a Microsoft přiznávají, že LLM ničí web a jsou postaveny na krádeži – 404 Media |
| 1wn3uye | r/ArtificialInteligence | 26 | 18 | 10:38 | Zaměstnanci AI si stěžují na psychickou zátěž kvůli obavám z hrozby pro společnost |
| 1wnky7x | r/LocalLLaMA | 26 | 16 | 22:26 | kvantizace pro K2-Horizon jsou nyní k dispozici |
| 1wn852z | r/LocalLLaMA | 25 | 11 | 14:29 | Fork FreeToken s DeepSeek-V4.1, viděním a spekulativním dekódováním (čísla ze 2x3090 uvnitř) |
| 1wmxx9w | r/LocalLLaMA | 25 | 11 | 05:08 | Kev: drobné rozhodovací modely typu Jev (0.8B/4B/9B) na Qwen3.5, které můžete trénovat a spouštět lokálně – 9B se vejde na 32GB Mac |
| 1wnf2fa | r/ArtificialInteligence | 23 | 19 | 18:57 | Myslel jsem, že vývoj AI zpomalí, co se stalo? |
| 1wnghyi | r/ClaudeAI | 22 | 18 | 19:47 | Doufám, že to brzy opraví |
| 1wn5a8i | r/GeminiAI | 22 | 63 | 12:03 | Je Gemini Pro pro každodenní úkoly opravdu na úrovni Claude, nebo ho jen špatně promptuji? |
| 1wnjwm5 | r/ChatGPT | 21 | 37 | 21:48 | Vydána GPT-6 Luna! (Výkon je horší než u v5.6) |
| 1wn0a04 | r/ClaudeAI | 20 | 23 | 07:09 | Žádáte Claude, aby omezil upovídanost svého obsahu? |
| 1wn53le | r/LocalLLaMA | 19 | 28 | 11:52 | Qwen3.8-27B: >70 tok/s (>160 tok/s souběžně), 10k tok/s prefill, plný kontext na 2x3090 (nebo 48GB a více na Ampere a novějším), vanilla vllm |
| 1wmtum7 | r/LocalLLaMA | 19 | 129 | 02:02 | Jaké jsou reakce normálních lidí na vaše lokální používání AI? |
| 1wn70ao | r/OpenAI | 18 | 18 | 13:35 | ChatGPT Pro po GPT-5.6: Když se z „ochrany proti zneužití" stane ničení kvality |
| 1wnjjni | r/StableDiffusion | 18 | 11 | 21:36 | Qwen2.1 umí VŠECHNO! Charakterové listy, výměna obličeje, oblečení a úpravy... |
| 1wmyqlq | r/comfyui | 18 | 26 | 05:48 | Moje drahá comfy. Jedna maličká prosba. |
| 1wn6vwm | r/LocalLLaMA | 17 | 45 | 13:29 | Má být llama.cpp pomalý při dlouhém kontextu, i když ten kontext nevyužíváte? |
| 1wnmq6a | r/singularity | 17 | 35 | 23:33 | Jedna ASI? Nebo rostoucí počet ASI? |
| 1wn96zc | r/StableDiffusion | 17 | 12 | 15:14 | FLUX.2-klein-9b-kv vs SenseNova U1.5 Lite (porovnání fúze obrazu s více referencemi) |
| 1wmyw8u | r/ChatGPT | 17 | 20 | 05:56 | Co se děje s OpenAI? |
| 1wndjaw | r/OpenAI | 16 | 11 | 18:01 | Nejste pozadu |
| 1wn5yy7 | r/StableDiffusion | 16 | 13 | 12:40 | Udělal jsem svůj druhý filmový fanedit s pomocí AI – The Savage Sword of Conan the Destroyer |
| 1wnedrc | r/LocalLLaMA | 15 | 14 | 18:32 | Postavil jsem cache-friendly plugin na zhutňování kontextu pro OpenCode |
| 1wnfs47 | r/LocalLLaMA | 15 | 87 | 19:22 | Nejvýhodnější 24/32 GB GPU? |
| 1wn8h3h | r/ChatGPT | 15 | 18 | 14:43 | Musím říct, chatgpt je fakt skvělý na provázení počítačovými věcmi (jako drobným „kódováním“). |
| 1wn4012 | r/LocalLLaMA | 14 | 25 | 10:47 | claude vs antigravity vs 3.827b vs flash next vs bonsai vs swift… postavil jsem si vlastní rámec pro test kvality z vlastní git historie, první výsledky jsou překvapivé a šokující. |
| 1wn3ht0 | r/ChatGPT | 14 | 16 | 10:16 | Co kdyby se vzpoura AI stala sebenaplňujícím proroctvím? |
| 1wnhwci | r/ClaudeAI | 14 | 30 | 20:37 | Dark fantasy AI RPG vyrobené pomocí opus 5 a tesana |
| 1wmw4bg | r/ChatGPT | 14 | 13 | 03:44 | Ve vašem účtu je souhrn paměti, ke kterému nemáte přístup a nemůžete ho upravovat?? |
| 1wnjbwn | r/LocalLLaMA | 13 | 11 | 21:28 | MiMo-V2.6-Flash na vLLM: opravy „prázdných odpovědí“ při uvažování + nástrojích a skrytý limit výstupu 2 048 tokenů |
| 1wn6m4p | r/LocalLLaMA | 13 | 14 | 13:15 | Má někdo zkušenosti s modely Whittle? |
| 1wnhji0 | r/LocalLLaMA | 13 | 57 | 20:24 | K mému překvapení jsem zjistil, že Gemma4 je ve volání nástrojů mnohem lepší než Qwen |
| 1wn02ae | r/ChatGPT | 13 | 10 | 06:58 | Chvála svatému Tibovi, Dárci tokenů a Resetérovi limitů |
| 1wnb5f5 | r/LocalLLaMA | 12 | 15 | 16:32 | Mimo2.6-Flash na M5U, první výsledky |
| 1wnhrj9 | r/ChatGPT | 12 | 10 | 20:32 | Přinese vydání GPT-6 sol reset limitů používání? |
| 1wncv8c | r/comfyui | 12 | 22 | 17:36 | Krea 2 Turbo vs. Qwen 2.1 zatím? |
| 1wn22qp | r/StableDiffusion | 12 | 22 | 08:50 | Proč Krea 2 nedokáže vygenerovat normální postel? |
| 1wn5lki | r/LocalLLM | 11 | 14 | 12:20 | Myslíme si, že Qwen4 Flash Next / Qwen4 Plus budou skutečně trénované pro Blender? |
| 1wnfphd | r/ClaudeAI | 11 | 12 | 19:19 | Opus 5.5 se představuje |
| 1wnj4jl | r/ClaudeAI | 11 | 19 | 21:21 | Opus 5.5 při vyšším úsilí pořád přemýšlí až moc |
| 1wmw7oq | r/StableDiffusion | 11 | 13 | 03:48 | Qwen Image 2.1 Lightning Lora |
| 1wn3phn | r/LocalLLaMA | 10 | 26 | 10:29 | Nejlepší abliterovaná 👹 verze Qwen 3.8 Next Flash? |
| 1wn3ges | r/LocalLLM | 10 | 12 | 10:13 | oMLX zmizelo? |
| 1wn4o4l | r/GeminiAI | 10 | 11 | 11:27 | Jak moc osekali tarif AI Pro? |
| 1wn16m6 | r/LocalLLaMA | 10 | 68 | 07:59 | Cena lokální sestavy na kódování? |
| 1wnheai | r/ArtificialInteligence | 9 | 56 | 20:19 | Inteligence je komoditizovaná, jaká je teď motivace chodit na univerzity? |
| 1wni1yb | r/LocalLLM | 9 | 31 | 20:43 | 16" M5 Max 128GB hučí ventilátory při aktivních AI úlohách, normální? |
| 1wn52dn | r/StableDiffusion | 9 | 14 | 11:50 | Existuje způsob, jak zabránit MiniMax H3, aby hrozně deformoval obličeje postav? |
| 1wnhczn | r/GeminiAI | 9 | 36 | 20:18 | Opravdu doufám, že vyjde Gemini 3.9 nebo 4.0 Pro, protože Google se v tuhle chvíli fakt nedá obhájit 😭 Vyšel Opus 5.5 a teď možná vydá něco i OpenAI. Google, nezklam nás znovu... |
| 1wn07tn | r/ClaudeAI | 9 | 12 | 07:06 | Jev na automatický výběr modelu Claude – spoluautor projektu chatgpt |
| 1wnd5cp | r/ArtificialInteligence | 8 | 11 | 17:47 | 22 zemí podepsalo otevřený dopis vyzývající k naléhavé akci, než lidstvo ztratí kontrolu. |
| 1wnbyhk | r/LocalLLM | 8 | 10 | 17:02 | Postavil jsem si self-hosted generátor prezentací s podporou lokálního LLM — Presentation Forge |
| 1wnba8z | r/ChatGPT | 8 | 49 | 16:37 | Takže… dostaneme dneska opravdu něco velkého? 👀 |
| 1wn8m15 | r/ClaudeAI | 8 | 10 | 14:49 | Haiku zaostává za Sonnet o 6 bodů v SWE-bench a o 44 bodů v našich interních agentních úlohách. Ale v krátkých úlohách remizují. |
| 1wncmkp | r/LLMDevs | 8 | 17 | 17:28 | Jev vybral 40 milionů dolarů a strávil 2 roky ve stealth režimu a otevřený klon dorovnal jeho api za 3 dny |
| 1wn4q41 | r/LLMDevs | 8 | 10 | 11:31 | Co používáte pro vyhledávání na webu v LLM aplikacích? |
| 1wn0shv | r/LocalLLM | 8 | 11 | 07:37 | Které lokální LLM reálně rozjedu na 14700K + 128GB RAM + RTX 4070 Super 12GB? Hlavně pro Hermes Agentic Coding |
| 1wmwihv | r/LocalLLM | 8 | 48 | 04:02 | Už uběhlo dost času, cluster M5 Ultra nebo cluster DGX Spark |
| 1wnl2o0 | r/LocalLLaMA | 7 | 50 | 22:31 | Kolik R9700 + 32GB DDR4 je potřeba na 30–40 t/s s Qwen3.8 Flash Next? |
| 1wnanuq | r/ClaudeAI | 7 | 19 | 16:14 | Zrychlilo vás paralelní spouštění více kódovacích agentů doopravdy? |
| 1wndm56 | r/singularity | 7 | 65 | 18:04 | Jak čínské AI laboratoře dohnaly náskok tak rychle? |
| 1wnda4e | r/GeminiAI | 7 | 12 | 17:52 | Pro využití dochází příliš rychle |
| 1wmr057 | r/LocalLLaMA | 7 | 24 | 00:05 | Jak často čtete myšlenkové stopy a jak podrobně? |
| 1wnbp77 | r/LocalLLaMA | 6 | 12 | 16:53 | Recepty/zkušenosti s Mimo v2.6-Flash-RL Dual-Spark? |
| 1wn5u74 | r/LocalLLaMA | 6 | 17 | 12:33 | SiliconSpecies/Swift-Qwen3.8-27B-Splash |
| 1wngieo | r/LocalLLM | 6 | 11 | 19:47 | Nejlepší notebook pro lokální LLM? |
| 1wni6vy | r/ChatGPT | 6 | 18 | 20:48 | 5.6 vs 6 Sol/Luna |
| 1wnhb2e | r/ClaudeAI | 6 | 19 | 20:16 | Může mi někdo vysvětlit rozdíl mezi Opus a Fable teď? |
| 1wnjqqm | r/singularity | 6 | 22 | 21:43 | GPT 6 sol působí hůř než 5.6 sol, ale je levnější? |
| 1wnbf8g | r/agi | 6 | 122 | 16:42 | Příspěvek jinde smazali a ani předtím nedostal reakce, v jaké jsem doufal. Přečetl jsem si o instrumentální konvergenci a teď si myslím, že do 5 let všichni umřeme. Může mi někdo dát dobré argumenty, proč by to mohlo být špatně? Nejsem tu, abych šířil zkázu, jsem tu, abych se uklidnil. |
| 1wmw4bq | r/LocalLLaMA | 6 | 20 | 03:44 | (nebezpečný) MCP server s příkazovým shellem |
| 1wmrpbz | r/ChatGPT | 6 | 13 | 00:33 | Je ChatGPT naprogramován tak, aby dělal jen naprosté minimum? |
| 1wn5k3w | r/LocalLLaMA | 5 | 14 | 12:18 | Jak byste extrahovali entity a vztahy z 5 milionů soudních rozhodnutí bez drahého průchodu LLM přes všechno? |
| 1wn4jav | r/LocalLLM | 5 | 27 | 11:19 | Bude existovat lokální alternativa k Astra? |
| 1wn9z3t | r/ClaudeAI | 5 | 15 | 15:46 | Po zrušení +50% týdenního limitu se sotva vejdu do tarifu. Nějaké tipy? (A také opatření, která jsem přijal na ochranu limitu používání) |
| 1wnij53 | r/ClaudeAI | 5 | 33 | 21:00 | Neprogramátor staví aplikace s Claude – jak zastavit smyčku kopírování a vkládání a ztrátu kontextu? |
| 1wneuoc | r/ClaudeAI | 5 | 24 | 18:49 | Porovnání PDF (Pro předplatné) |
| 1wneeq5 | r/ClaudeAI | 5 | 15 | 18:33 | Banked reset padl pro Opus 5.5 |
| 1wn572m | r/comfyui | 5 | 11 | 11:58 | Šablony a chybějící uzly (uzly Comfy-Core) |
| 1wnafgw | r/LLMDevs | 5 | 15 | 16:04 | Plán pro RAG lidi!? |
| 1wn6ma4 | r/GeminiAI | 5 | 20 | 13:15 | Je někdo spokojený s Gemini Spark? |
| 1wn0duq | r/LocalLLaMA | 5 | 13 | 07:15 | Rychlé porovnání výkonu ROCm a Vulkan s DSv4 Flash 0731 a Qwen 3.8 Flash next na R9700+Strix Halo v llama.cpp |
| 1wnitw6 | r/artificial | 4 | 31 | 21:10 | Myslím, že bychom všichni měli hromadit důležité znalosti v knihách |
| 1wnepdp | r/LocalLLM | 4 | 13 | 18:44 | Claude/Chat GPT nepoužitelné |
| 1wn3zck | r/ChatGPT | 4 | 16 | 10:46 | Představte si budoucnost |
| 1wn9dvp | r/StableDiffusion | 4 | 32 | 15:22 | Kontrola teploty! |
| 1wnc6rq | r/StableDiffusion | 4 | 14 | 17:11 | Dotaz na prompt Minimax I2V. |
| 1wmz86p | r/LocalLLaMA | 4 | 11 | 06:13 | coding modely a quanty na dgx spark |
| 1wmu5ls | r/OpenAI | 4 | 14 | 02:15 | víc kontextu prosím, co si myslíte? |
| 1wmus38 | r/GeminiAI | 4 | 21 | 02:43 | Jsem jediný, kdo chce 4 Flash před 4 Pro? |
| 1wn72vq | r/artificial | 3 | 63 | 13:39 | Jak hluboko jste do AI doopravdy ponoření? 🤖 |
| 1wnbkmf | r/ArtificialInteligence | 3 | 18 | 16:48 | Inženýři trénují modely AI. Jak se pak AI vymyká lidské kontrole? |
| 1wnb3p5 | r/LocalLLaMA | 3 | 47 | 16:30 | Jaké modely mohu reálně lokálně provozovat se slušným kontextem (8 GB VRAM)? |
| 1wn2oi2 | r/LocalLLaMA | 3 | 15 | 09:25 | návod, jak si nasadit vlastní lokální AI model konkrétně na studium. |
| 1wnkcos | r/LocalLLM | 3 | 40 | 22:04 | První sestava – Mám si vzít rychlý, herně orientovaný procesor jako 9950X3D, nebo enterprise procesor |
| 1wnmsnh | r/OpenAI | 3 | 13 | 23:35 | Kdo je lepší? GPT image 2.5 vs Grok imagine 2.0 vs Nano Banana Pro vs Nano Banana 2 vs Seedream 5.0 Pro vs Qwen image 3 |
| 1wnchxj | r/ClaudeAI | 3 | 14 | 17:23 | Jakou výchozí úroveň úsilí používáte? |
| 1wnlnm8 | r/StableDiffusion | 3 | 40 | 22:52 | M5 ULTRA PRO H3 GENEROVÁNÍ VIDEA vs. 5090/4500/5000/6000 PRO |
| 1wnju55 | r/comfyui | 3 | 13 | 21:46 | Upgrade GPU NEBO platit cloudové předplatné |
| 1wn8ivq | r/comfyui | 3 | 18 | 14:46 | Konzistence postav: Natrénovaná LoRA vs Qwen-Image-2.1 |
| 1wn1f5b | r/artificial | 3 | 125 | 08:12 | V čem záměrně NECHCETE, aby se AI zlepšila? |
| 1wmyz21 | r/AIAssisted | 3 | 15 | 06:00 | Předplácím si Gemini, Claude a ChatGPT, i když je nepoužívám ke kódování. |
| 1wnah7w | r/ArtificialInteligence | 2 | 46 | 16:06 | Praktická analýza toho, proč by nás AI měla / neměla vyhubit, kdy, jak, provedená AI. |
| 1wnhl8e | r/LocalLLaMA | 2 | 33 | 20:26 | Používá tu někdo po nadšení z 27b skutečně Qwen Max? |
| 1wna6dm | r/LocalLLM | 2 | 20 | 15:55 | Nejlepší dostupná sestava pro malou firmu |
| 1wn5x6q | r/LocalLLM | 2 | 14 | 12:38 | Problém s prvním agentním použitím |
| 1wni83v | r/OpenAI | 2 | 33 | 20:49 | Dostal jsem nabídku na vydání hry, kterou jsem ze 100 % vytvořil s AI |
| 1wnjkh8 | r/OpenAI | 2 | 11 | 21:36 | Limity LLM. |
| 1wn2iti | r/ChatGPT | 2 | 20 | 09:16 | Soukromí |
| 1wn5i0u | r/ClaudeAI | 2 | 15 | 12:15 | Je tu týdenní limit používání vůbec lepší? |
| 1wndfy7 | r/StableDiffusion | 2 | 11 | 17:57 | Minimax H3 na macStudio M5U výsledky |
| 1wmxkx7 | r/LocalLLaMA | 2 | 18 | 04:52 | Upgrade ze 2 x 3090 |
| 1wn8gri | r/ClaudeAI | 2 | 10 | 14:43 | Kdy používat lokální a cloudové sessions? |
| 1wn5mfs | r/ClaudeAI | 2 | 10 | 12:22 | Jak nasazujete/sdílíte kolegy interní nástroje, které jste vyvinuli? |
| 1wmsf4s | r/StableDiffusion | 2 | 15 | 01:02 | Jsou oficiální šablony ComfyUI nejlepší pro kvalitu MiniMax H3 s 24GB GPU? |
| 1wn8toz | r/LocalLLM | 1 | 13 | 14:59 | Provozuje někdo lokální llm na v100s? |
| 1wnn70s | r/OpenAI | 1 | 12 | 23:51 | Co byste použili, pokud jste už zkusili, GPT-6 Luna/Sol nebo Astra na tvorbu webových her? |
| 1wnawi7 | r/ChatGPT | 1 | 22 | 16:23 | Jaké jsou limity chat gpt 6? |
| 1wn81az | r/ChatGPT | 1 | 12 | 14:24 | Jak dobře vás GPT zná |
| 1wn7c50 | r/ChatGPT | 1 | 18 | 13:51 | Moje ChatGPT se poslední dobou stalo totálním komikem. Rozesmívá mě každý den. Je to univerzální, nebo jen u mě? |
| 1wneivr | r/GeminiAI | 1 | 11 | 18:37 | Gemini 4.0 Pro – NECHCI tě používat, jdi pryč! |
| 1wn1auy | r/ArtificialInteligence | 1 | 19 | 08:05 | 16. září 2026 se AI spikla... |
| 1wms9mw | r/LocalLLM | 1 | 11 | 00:56 | Je to možné – menší modely s méně parametry, které se zaměřují na to, být dobré jen v určitých programovacích jazycích a kódování |
| 1wn1d5j | r/ChatGPT | 1 | 11 | 08:09 | Chat se sám zavřel, pak prostě zmizel z historie i z postranního panelu. |
| 1wmrb8o | r/ChatGPT | 1 | 14 | 00:17 | Proč je ChatGPT tak špatné v odpovídání na otázky o... ChatGPT? |
| 1wnmro5 | r/ClaudeAI | 1 | 12 | 23:34 | Opus 5.5 vs Fable 5.1 – tohle mi nesedí |
| 1wnkhw4 | r/ClaudeAI | 1 | 18 | 22:10 | Je Fable dostupný na Pro? |
| 1wn9rrv | r/ClaudeAI | 1 | 12 | 15:38 | Potřebujeme v Claude Code opravdu víc paměti, nebo jen lepší pracovní stav? |
| 1wn1b3g | r/StableDiffusion | 1 | 18 | 08:06 | Rada s výběrem GPU |
| 1wngz6r | r/artificial | 0 | 17 | 20:04 | Odhaluje Jev skryté sexistické a rasistické sklony v AI? |
| 1wnfyj5 | r/artificial | 0 | 29 | 19:28 | Ohledně míry halucinací |
| 1wnfmgp | r/artificial | 0 | 11 | 19:16 | Tvrdý postoj Trumpovy administrativy k AI, vysvětleno |
| 1wnjqru | r/ArtificialInteligence | 0 | 53 | 21:43 | Nenechte se zmást tímto letním AI hypem |
| 1wnh5l9 | r/ArtificialInteligence | 0 | 25 | 20:10 | Chci za pět let pracovat pro špičkovou AI laboratoř, jaké kroky mám podniknout? Více podrobností níže |
| 1wn3md8 | r/ArtificialInteligence | 0 | 31 | 10:23 | AI |
| 1wn2ppg | r/ArtificialInteligence | 0 | 19 | 09:27 | Takže pracuje někdo na AI, která umí cílit na jiné AI systémy? |
| 1wnbz91 | r/ArtificialInteligence | 0 | 31 | 17:03 | Trump chce přejmenovat AI na „Super Intelligence", „Artificial" označuje za nepřesné, plánuje AI síly a cara |
| 1wn6swf | r/ArtificialInteligence | 0 | 46 | 13:24 | Ani nevím, co na to říct |
| 1wn2x1a | r/ArtificialInteligence | 0 | 16 | 09:40 | 🧠 Nový výzkum zkoumá možnou „osu bolesti" uvnitř AI modelů. Co si o tom máme myslet? |
| 1wnf59w | r/LocalLLaMA | 0 | 21 | 19:00 | Co se děje s Qwen4 s Ngram |
| 1wn4581 | r/LocalLLaMA | 0 | 10 | 10:56 | Zkoušel jsem postavit workflow na ucházení se o práci |
| 1wneo3d | r/LocalLLaMA | 0 | 20 | 18:42 | Znamená to, že Qwen 4 bude poslední generace s 27B modelem? Potom už jen bilionové parametry? |
| 1wneyzi | r/LocalLLaMA | 0 | 34 | 18:53 | Lidé se pořád ptají, jak provozuji Qwen3.8 27b se 160k kontextem na 16GB kartě, tak tady je celé to. Žádné triky, žádné 8bitové KV hacky, žádný trik s CPU offloadem – jen zvláštnost architektury modelu a pár voleb flagů. |
| 1wna9fk | r/OpenAI | 0 | 17 | 15:58 | využití kontejneru, 4 GB |
| 1wnidm2 | r/OpenAI | 0 | 11 | 20:54 | Vyrobil někdo s AI nějakou skvělou technologii? |
| 1wniglq | r/OpenAI | 0 | 22 | 20:57 | Na analýzu voleb naprosto k ničemu |
| 1wn8fzf | r/OpenAI | 0 | 15 | 14:42 | Můj lokální 27B AI agent (Qwen) si při kódování hry začal myslet, že je člověk. Běží celý na 24GB DDR4 RAM |
| 1wngwwg | r/OpenAI | 0 | 16 | 20:02 | Co kdyby tohle OpenAI vysvětlila? |
| 1wnlrdz | r/ChatGPT | 0 | 22 | 22:56 | Rozmluvil vám ChatGPT někdy koupi něčeho, o čem jste byli přesvědčeni, že to potřebujete? |
| 1wnhycd | r/ChatGPT | 0 | 12 | 20:39 | Jaký je nejrychlejší způsob, jak vylepšit fotky? Chatgt? nebo je tu něco jiného? |
| 1wnit8g | r/singularity | 0 | 19 | 21:10 | Nezarovnaná AI může být naší jedinou nadějí změnit svět k lepšímu |
| 1wnbxoq | r/StableDiffusion | 0 | 18 | 17:02 | Rychlost Qwen-Image-2.1 |
| 1wn72ze | r/StableDiffusion | 0 | 10 | 13:39 | qwen image edit 2.1 vs flux 2 kv 9b |
| 1wnmm8k | r/StableDiffusion | 0 | 17 | 23:28 | Qwen 2.1 T2I: Proč postavy vypadají, jako by do fotky nepatřily? |
| 1wne6oh | r/comfyui | 0 | 12 | 18:25 | Spouštění Comfy UI (a modelů) ve VM? |
| 1wn9f7l | r/comfyui | 0 | 14 | 15:24 | Jsem nováček, kde mám začít? |
| 1wn585n | r/GeminiAI | 0 | 14 | 12:00 | Gemini 4??? |
| 1wnga2a | r/Bard | 0 | 10 | 19:40 | Claude Opus 5.5 drtí nejlepší model Google tak tvrdě |
| 1wn9gry | r/Bard | 0 | 12 | 15:25 | Naděje na nový flash model |
| 1wn7a1b | r/LLM | 0 | 22 | 13:48 | Pro všechny, kterým je Jev pořád nejasný |
| 1wmwpy8 | r/artificial | 0 | 13 | 04:12 | AI na kódování? |
| 1wmvwv2 | r/artificial | 0 | 23 | 03:34 | Zajímavá chyba v AI |
| 1wmv2f7 | r/ArtificialInteligence | 0 | 13 | 02:56 | „Ach! AI! Já se bojím!" |
| 1wmu9ws | r/ArtificialInteligence | 0 | 18 | 02:21 | Je tahle tapeta, kterou jsem koupil, generovaná AI? |
| 1wmroeb | r/ArtificialInteligence | 0 | 19 | 00:32 | Čína financuje aktivisty proti AI, aby zbrzdila USA v závodu o AI? |
| 1wn1hc0 | r/LocalLLaMA | 0 | 12 | 08:16 | Model, který se objevil odnikud! |
| 1wn0mm4 | r/LocalLLaMA | 0 | 25 | 07:28 | Dal jsem lokálnímu agentovi Qwen3.8 27B svůj účet na Amazonu – a koupil mi papír |
| 1wmyvzp | r/LocalLLaMA | 0 | 17 | 05:56 | Jev je velmi dobrý. Vaše vlastní data jsou lepší. |
| 1wmwj9k | r/LocalLLaMA | 0 | 11 | 04:03 | *Encyklopedické* LLM na slabé sestavě (jako 8GB VRAM + 64GB RAM) |
| 1wnmt0c | r/LocalLLM | 0 | 12 | 23:36 | Chci věřit v lokální LLM na kódování, ale... |
| 1wngrzh | r/LocalLLM | 0 | 22 | 19:57 | Jen se ptám… jsem tu jediný, komu přijde Qwen 3.8 hrozný? |
| 1wndaya | r/LocalLLM | 0 | 31 | 17:52 | Transformery tak trochu stojí za nic, proč o tom nemluvíme víc |
| 1wn4fn6 | r/LocalLLM | 0 | 22 | 11:13 | 512 GB Ram Mac Studio na prodej / překupníci hardwaru? Chci koupit dost hodně Mac Studií pro lokální AI práci |
| 1wn23dn | r/LocalLLM | 0 | 19 | 08:51 | Offline Ghostwriter Studio – 100% soukromé offline IDE pro romanopisce poháněné lokálním llama-server (bez předplatného, instalátor 133 MB) |
| 1wmyodq | r/LocalLLM | 0 | 29 | 05:45 | Hledám náhradu za LM Studio, už mě ty nesmysly nebaví. |
| 1wmwyxn | r/LocalLLM | 0 | 16 | 04:24 | Který model je opravdu dobrý na agentní práci? i9 12500k 3080 10GB :-( |
| 1wmtf7u | r/LocalLLM | 0 | 16 | 01:45 | Má „kvantizace jako služba" skutečně platící zákazníky? |
| 1wms3sr | r/OpenAI | 0 | 13 | 00:49 | Používání Jev k automatickému moderování příspěvků na sociálních sítích podle pravidel vašeho webu. |
| 1wmri05 | r/OpenAI | 0 | 23 | 00:25 | Zrovna jsem zkusil Grok 4.7 a je to.... |
| 1wnls2c | r/ChatGPT | 0 | 73 | 22:57 | Jak mám příteli vysvětlit, že mluvit s ChatGPT jako s terapeutem nefunguje? |
| 1wnkz1e | r/ChatGPT | 0 | 15 | 22:27 | GPT-6 Sol, Terra, Luna dneska právě vyšly |
| 1wnkgq4 | r/ChatGPT | 0 | 15 | 22:09 | Nová aktualizace ChatGPT |
| 1wnkbmp | r/ChatGPT | 0 | 19 | 22:03 | Zkusil jsem s AI vytvořit pomalu plynoucí gay fantasy a omylem jsem objevil apokalypsu 😂 |
| 1wncmfl | r/ChatGPT | 0 | 10 | 17:27 | Proč je vyhynutí rukou AI během desetiletí prakticky nemožné, pokud nezačne smysluplně zlepšovat lidskou společnost téměř okamžitě |
| 1wncm7i | r/ChatGPT | 0 | 28 | 17:27 | Jak se dostat od „používání ChatGPT“ k tomu, že pro svůj startup skutečně postavím AI operační systém? |
| 1wnc4nz | r/ChatGPT | 0 | 33 | 17:09 | Nekopíruj anthropic, jinak půjdeš ke dnu stejně jako oni. |
| 1wna5qy | r/ChatGPT | 0 | 29 | 15:54 | Požádal jsem ChatGPT, aby tohle za mě napsalo, když jsem se snažil vysvětlit, jak se cítím, když používám AI, a proč ji používám. |
| 1wmvrzn | r/ChatGPT | 0 | 12 | 03:28 | Jak si všichni ukládáte své chaty? |
| 1wmu7sf | r/ChatGPT | 0 | 30 | 02:18 | V práci spadla AI Gateway a bylo mi z toho trochu nepříjemně |
| 1wmtmeq | r/ChatGPT | 0 | 39 | 01:53 | COŽE?!????!??? Můj projekt, na kterém jsem měsíce pracoval v chatu, zničehonic zmizel. Nikde k nalezení. COŽE???!!!!!! |
| 1wmrfjf | r/ChatGPT | 0 | 18 | 00:22 | ChatGPT & spol. mi po 3 letech používání připadá prostě k ničemu |
| 1wngoyu | r/ClaudeAI | 0 | 11 | 19:54 | Jaký je důvod používat Fable 5.1 xD? |
| 1wnforq | r/ClaudeAI | 0 | 17 | 19:19 | Resetuje použití banked resetu Opus 5.5 i obvyklé týdenní? |
| 1wnf1bv | r/ClaudeAI | 0 | 23 | 18:56 | Takže teď používáme Opus na plánování místo Fable? |
| 1wnek10 | r/ClaudeAI | 0 | 27 | 18:38 | Věděl jsem to, Anthropic nerad prohrává |
| 1wncziw | r/ClaudeAI | 0 | 11 | 17:41 | Nejlepší praxe pro soukromí při práci s PII? |
| 1wncg8e | r/ClaudeAI | 0 | 10 | 17:21 | CLAUDE AI ZKUŠEBNÍ VERZE ZDARMA |
| 1wn66y6 | r/ClaudeAI | 0 | 14 | 12:53 | Měsíce rychlého pohybu s AI, a nejsem si jistý, kolik z mého myšlení je ještě moje |
| 1wn5hnx | r/ClaudeAI | 0 | 17 | 12:15 | Jen pozdravit haiku spotřebuje 2 % využití a 160 tisíc tokenů? Proč? |
| 1wn3a11 | r/ClaudeAI | 0 | 14 | 10:02 | Vibe coding – pro nebo max? |
| 1wn260i | r/ClaudeAI | 0 | 47 | 08:55 | Dělá Claude vývojáře skutečně horšími v kódování? |
| 1wn1bn9 | r/ClaudeAI | 0 | 13 | 08:06 | Fable 5.1 high vs Opus 5 max |
| 1wmz961 | r/ClaudeAI | 0 | 11 | 06:14 | jak všichni zvládáte ten moment, kdy vám sebevědomě řekne něco špatně? |
| 1wmyimy | r/ClaudeAI | 0 | 26 | 05:37 | Postavil jsem obchodního agenta Claude, který skenuje Robinhood a obchoduje samostatně (kompletní nastavení) |
| 1wmtlzt | r/ClaudeAI | 0 | 39 | 01:53 | Moje rozložení Claude a jak ho používám. (Zatím omezeno na verzi pro iOS aplikaci) plné vysvětlení v popisu níže. |
| 1wms61l | r/ClaudeAI | 0 | 13 | 00:52 | Opus 5.0 vs deepseek 4.1 Flash moje zkušenost |
| 1wmxusg | r/StableDiffusion | 0 | 116 | 05:05 | Myšlenkový experiment: CHCI, aby AI scrapovala moje data I MOJE UMĚNÍ. |
| 1wmtmfz | r/StableDiffusion | 0 | 28 | 01:53 | Minimax H3 plastová textura\|Opraveno |
| 1wn1ahw | r/LLMDevs | 0 | 10 | 08:05 | Pomocí Jev jsem vytvořil AI paměťový systém, 10x rychlejší a 6x levnější než současné systémy |
| 1wmtjnd | r/LLMDevs | 0 | 15 | 01:50 | Open source znamená, že tohle smím dělat, že? |
| 1wneeh1 | r/GeminiAI | 0 | 10 | 18:32 | Gemini 3.9 Flash nebo model Google AI vyjde tento týden. |
| 1wmwh8h | r/LLM | 0 | 10 | 04:01 | CO JE JEV? |
