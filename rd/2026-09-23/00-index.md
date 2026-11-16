# AI novinky z Redditu — 23. 9. 2026

Rozsáhlý přehled diskusí a zpráv z AI subredditů publikovaných **23. 9. 2026 (Europe/Prague)** s **alespoň 10 komentáři**. Složka je pojmenovaná datem zpráv (den, ze kterého novinky jsou). Ke každému vybranému tématu je samostatný podrobný článek ve formátu Markdown, jehož název začíná **Reddit ID**.

## Metodika

- **Zdroje:** 19 AI subredditů — r/artificial, r/ArtificialInteligence, r/MachineLearning, r/deeplearning, r/LocalLLaMA, r/LocalLLM, r/OpenAI, r/ChatGPT, r/ClaudeAI, r/singularity, r/agi, r/StableDiffusion, r/comfyui, r/LLMDevs, r/GeminiAI, r/Bard, r/OpenAIDev, r/AIAssisted, r/LLM.
- **Sběr:** veřejné Reddit JSON rozhraní načítané prohlížečem ze stejného původu (same-origin `fetch`), protože přímé volání z curl/čtečky vrací `403 You've been blocked by network security`.
- **Počet requestů:** **94** na Reddit API — 1 ověřovací request, **5** requestů `/r/<sub>/top.json?t=week&limit=100` (ruční běh na starší datum, takže místo `t=day` týdenní okno) a **28** stránek `/r/<sub>/new.json?limit=100` paginovaných přes `after`, dokud nejstarší `created_utc` neklesl pod začátek okna (max 8 stránek na subreddit); dále **60** requestů na komentáře (`/comments/<id>.json?limit=50&sort=top&raw_json=1`). Pacing 2,5 s u výpisů a 1,5 s u komentářů, bez HTTP 403/429.
- **Další zdroje:** 18 stažení externích stránek (14 požadavků přes HTTP, 2 načtení prohlížečem kvůli paywallu a JavaScriptu a 2 stránky modelových karet na Hugging Face) a 24 stažených screenshotů z i.redd.it.
- **Filtr:** `created_utc` v okně **23. 9. 2026 00:00–24:00 Europe/Prague** (22. 9. 22:00 UTC – 23. 9. 22:00 UTC), `num_comments >= 10`, bez stickied příspěvků. Získáno **1 076** příspěvků v okně, z toho **428** splňuje limit komentářů.
- **Deduplikace:** témata se stejným produktem nebo událostí byla sloučena do jednoho článku; ostatní posty jsou v článku uvedené jako „další diskuse“ s odkazy. Sloučeno bylo **71** souvisejících postů do **26** tematických okruhů (Opus 5.5 vs. GPT-6 Astra, Jev, Hugging Face útok, Anthropic kredity, Luna 6, Gemini memy, Apple 1T model, Flux 3 Action a další).
- **Vytěžení dat:** pro každý vybraný příspěvek byl sestaven balíček (text postu, stažený článek, screenshot, až 25 nejlepších komentářů) a data z něj vytěžil **levný model z OpenCode Go (`opencode-go/muse-spark-1.3-contributor`)** jako 26 paralelních subagentů s definicí `~/.omp/agent/agents/reddit-extractor.md`; text ze screenshotů byl přepsán z obrázků. Extrakce trvala **05:32**. Články pak sestavili subagenti hlavního agenta podle pevné šablony a jazykových pravidel.
- **Jazyk:** všechny články a celý index jsou česky, včetně titulků redditových postů v tabulkách. Citace jsou **překlady z angličtiny** a jsou označené `(překlad)`; anglické originály se v článcích neuvádějí. Výjimkou jsou vlastní jména, názvy firem, modelů a produktů, čísla a URL.
- **Podklady u paywallů:** u článku Business Insider (téma rizik podle Jareda Kaplana) a u placené části NYT se nepodařilo získat tělo (tvrdý paywall i v prohlížeči); obsah vychází z redditového postu a komentářů. U dvou videopostů (v.redd.it) nebyl k dispozici přepis, články vycházejí z titulku a komentářů.

## Detailní články (26)

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1wo5yg6](1wo5yg6_narativ-jen-predpovida-dalsi-slovo.md) | r/singularity | 327 | 780 | 15:25 | Byl narativ „model jen předpovídá další slovo“ šířen záměrně? |
| [1wnq2cb](1wnq2cb_opus-5-5-porazi-gpt-6-astra-v-agentickem-kodovani.md) | r/OpenAI | 3495 | 420 | 01:52 | Snímky z r/OpenAI: Opus 5.5 poráží GPT-6 Astra v agentickém kódování |
| [1woe70t](1woe70t_jev-neni-nova-technologie-marketing-cili-na-novacky.md) | r/LocalLLaMA | 668 | 259 | 20:33 | Jev není nová technologie, jeho marketing cílí na lidi od LLM |
| [1wnpit2](1wnpit2_claude-je-zpet-a-proc-je-anthropic-tak-dobry.md) | r/ClaudeAI | 1583 | 192 | 01:29 | „Claude je zpět“: komunita po Opus 5.5 řeší, proč je Anthropic tak dobrý |
| [1wogab3](1wogab3_opus-5-5-vygeneroval-video-za-3-21-dolaru.md) | r/ClaudeAI | 1606 | 177 | 21:50 | Opus 5.5 vygeneroval video za 3,21 dolaru z OpenRouteru |
| [1wnpnnn](1wnpnnn_proc-by-nami-neovladana-superinteligence-delala-neco-pro-nas.md) | r/artificial | 34 | 172 | 01:35 | Proč by superinteligence, kterou neumíme ovládat, dělala něco pro nás? |
| [1wnzbth](1wnzbth_openai-deaktivoval-ucty-za-recidivu.md) | r/ChatGPT | 157 | 171 | 09:38 | OpenAI deaktivoval účty za „recidivu“, uživatelé žádají vysvětlení |
| [1wnvnxb](1wnvnxb_je-unava-z-ai-realna-nebo-je-to-povzdech-boomeru.md) | r/artificial | 38 | 150 | 06:11 | Je únava z AI reálná, nebo je to jen povzdech boomerů? |
| [1wo1bct](1wo1bct_cena-inteligence-pada-47-za-ctvrtleti.md) | r/LocalLLaMA | 385 | 150 | 11:38 | Cena inteligence padá o 47 % za čtvrtletí, OpenAI prý utrácí 4 miliony dolarů denně |
| [1wognfz](1wognfz_claude-agenti-objevili-enzymovy-system-podobny-crispr.md) | r/singularity | 720 | 144 | 22:03 | Claude agenti objevili nový enzymový systém podobný CRISPR |
| [1wo5nh6](1wo5nh6_lide-nechapou-jak-obrovske-jsou-ai-firmy.md) | r/ArtificialInteligence | 342 | 132 | 15:13 | Lidé nechápou, jak obrovské jsou dnes AI firmy: graf srovnává 5,2 bilionu dolarů |
| [1wnxhji](1wnxhji_pirate-face-piratska-zatoka-pro-otevrene-modely.md) | r/LocalLLaMA | 865 | 122 | 07:50 | Pirate Face: pirátská zátoka pro otevřené modely |
| [1wnxg0n](1wnxg0n_luna-6-je-proti-luna-5-6-propadak.md) | r/OpenAI | 374 | 121 | 07:48 | Luna 6 je proti Luna 5.6 propadák, shodují se uživatelé |
| [1wog3z8](1wog3z8_sefove-ai-firem-o-rizicich-amodei-a-huang.md) | r/singularity | 445 | 118 | 21:43 | Šéfové AI firem o rizicích: Amodei čeká nadlidskou biologii, Huang varuje před alarmismem |
| [1wnxlgm](1wnxlgm_experti-cekali-milleninovu-ulohu-az-na-rok-2054.md) | r/ChatGPT | 664 | 115 | 07:56 | V roce 2024 experti čekali vyřešení Milleninovy úlohy až na rok 2054 |
| [1wo5nb6](1wo5nb6_nejrozumitelnejsi-vysvetleni-utoku-na-hugging-face.md) | r/OpenAI | 409 | 109 | 15:12 | Komunita sestavila nejsrozumitelnější vysvětlení útoku na Hugging Face |
| [1wnwdww](1wnwdww_apple-spustil-bilionovy-model-na-ctyrech-mac-studiich.md) | r/LocalLLM | 192 | 105 | 06:50 | Apple spustil bilionparametrový model na čtyřech Mac Studiích z jedné zásuvky |
| [1woijhq](1woijhq_anthropic-rozdal-kredity-a-reset-limitu.md) | r/ClaudeAI | 256 | 101 | 23:17 | Anthropic rozdal kredity na cloudové relace a reset limitů, uživatelé jsou zmatení |
| [1wobyjp](1wobyjp_hle-diamond-novy-test-vede-gpt-6-astra.md) | r/singularity | 350 | 101 | 19:10 | HLE-Diamond: vyčištěný test Humanity's Last Exam vede GPT-6 Astra se 60,6 % |
| [1wnuko4](1wnuko4_opus-5-5-odmita-pracovat-na-vedeckem-vyzkumu.md) | r/ClaudeAI | 359 | 96 | 05:17 | Opus 5.5 odmítá pracovat na vědeckém výzkumu, hlásí biolog |
| [1wnv85k](1wnv85k_peking-vysetruje-deepseek-a-moonshot.md) | r/LocalLLaMA | 310 | 92 | 05:49 | Peking vyšetřuje DeepSeek a Moonshot kvůli přesměrování dotazů na Claude |
| [1wocmn8](1wocmn8_r-gemini-ai-je-plny-memu-o-odkladani-gemini-4-pro.md) | r/GeminiAI | 485 | 89 | 19:35 | r/GeminiAI je plný memů o odkládání Gemini 4 Pro |
| [1wnqy2k](1wnqy2k_qwen-image-2-1-test-vernosti-promptu.md) | r/StableDiffusion | 397 | 71 | 02:30 | Qwen-Image-2.1: věrnost promptu je vysoká, uživatelé ale srovnávají s Krea 2 |
| [1woheuh](1woheuh_ai-agent-pronikl-na-australsky-portal-medicare.md) | r/singularity | 193 | 63 | 22:33 | AI agent pronikl na australský vládní portál Medicare, uvedl premiér Albanese |
| [1wodsr1](1wodsr1_flux-3-action-open-weight-model-sveta-akci.md) | r/StableDiffusion | 140 | 47 | 20:18 | Flux 3 Action: open-weight model světa akcí pro roboty |
| [1wo61jr](1wo61jr_altman-chce-globalni-standardy-pro-ai-na-un.md) | r/singularity | 65 | 23 | 15:29 | Altman chce na půdě UN prosadit globální standardy pro AI |

## Příloha: všech 428 příspěvků s 10+ komentáři

| Reddit ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1woe567 | r/ChatGPT | 3844 | 136 | 20:31 | Přítelkyně s umělou inteligencí |
| 1wnq2cb | r/OpenAI | 3495 | 420 | 01:52 | Pane, Dario právě vydal Opus 5.5 a při středním úsilí poráží GPT-6 Astra v agentním kódování, přitom je o 80 % levnější… poráží Fable 5.1 v každém benchmarku… je o 30 % rychlejší než Opus 5… a pane… dokonce zvýšili limity použití a všem nadělili bankovaný reset ve stylu Tibo… |
| 1wo4bgr | r/ChatGPT | 3466 | 160 | 14:14 | Trump jako indický pouliční prodavač |
| 1wo6nb2 | r/ChatGPT | 1980 | 118 | 15:53 | Vítejte v novém světě |
| 1wog70j | r/ChatGPT | 1915 | 86 | 21:47 | ChatGPT je stále vepředu, ale Claude ho dohání |
| 1wogab3 | r/ClaudeAI | 1606 | 177 | 21:50 | Vytvořeno celé s Opus 5.5 + 3,21 dolaru spotřeby OpenRouter API |
| 1wnpit2 | r/ClaudeAI | 1583 | 192 | 01:29 | Claude je ZPĚT! |
| 1wo6o0f | r/LocalLLaMA | 1143 | 238 | 15:54 | Modové: můžeme něco udělat s tím, že půlku fóra zaplavují tyhle reklamní příspěvky na Jev? |
| 1wo9lbs | r/ClaudeAI | 1129 | 128 | 17:44 | OPUS 5.5 JE NOVÝ 4.6! |
| 1woe138 | r/singularity | 906 | 76 | 20:27 | Claude objevil nový enzymový systém s vlastnostmi připomínajícími CRISPR |
| 1wo1xen | r/ChatGPT | 892 | 65 | 12:13 | Proč mě to nenapadlo? |
| 1wnxhji | r/LocalLLaMA | 865 | 122 | 07:50 | Pirate Face – pirátská zátoka pro LLM |
| 1wognfz | r/singularity | 720 | 144 | 22:03 | Okamžik, kdy agenti Claude objeví nový molekulární mechanismus a mluví, jako by byli lidé, s citoslovci a narážkami |
| 1wo3crl | r/singularity | 698 | 77 | 13:28 | Ohlédnutí za tím, jak to všechno začalo: vibe coding s GPT-3 v roce 2020 |
| 1woj6x6 | r/singularity | 675 | 42 | 23:42 | Zrovna vyšel nový benchmark. |
| 1woe70t | r/LocalLLaMA | 668 | 259 | 20:33 | Jev není nová technologie. Jeho marketing cílí na lidi, kteří si myslí, že umělá inteligence začala s LLM. |
| 1wnoqmh | r/ClaudeAI | 664 | 52 | 00:55 | Opus 5.5 mi postavil web, který z libovolné fotky udělá jednolinkovou kresbu. Natočí i to, jak se linka kreslí. |
| 1wnxlgm | r/ChatGPT | 664 | 115 | 07:56 | Před 2 lety si výzkumníci umělé inteligence mysleli, že umělá inteligence nevyřeší matematický problém tisíciletí dalších 30 let |
| 1wnzlav | r/LocalLLaMA | 585 | 302 | 09:54 | V tuhle chvíli už to ani není soutěž… to je ostuda |
| 1wo1j0q | r/StableDiffusion | 578 | 66 | 11:50 | Série experimentů s pracovními postupy, které oživí vaši konzoli z dětství. |
| 1wo5xal | r/ChatGPT | 559 | 87 | 15:24 | Lidé nechápou, jak obrovské jsou teď firmy zabývající se umělou inteligencí |
| 1wo917e | r/ClaudeAI | 517 | 54 | 17:24 | AI má pořád své momenty!! |
| 1wnxeql | r/ClaudeAI | 508 | 137 | 07:46 | Hloupá otázka – když je Opus 5.5 lepší než Fable 5.1, proč bychom kdy používali Fable 5.1? |
| 1wocmn8 | r/GeminiAI | 485 | 89 | 19:35 | Stav subredditu v poslední době |
| 1wog3z8 | r/singularity | 445 | 118 | 21:43 | Generální ředitel Anthropic Dario Amodei: Biologie s umělou inteligencí přejde během pár let od slabé k nadlidské |
| 1wocgkl | r/ChatGPT | 441 | 62 | 19:28 | Opus 5.5 vs GPT-6 Sol: test 3D pelikána jedoucího na kole v Blenderu |
| 1wohzqj | r/singularity | 435 | 97 | 22:55 | Můžeme se na chvíli zastavit a ocenit, že s 950 agenty Claude běžícími pouhých 21 hodin při prohledávání genomických dat mohl Anthropic najít nový mechanismus editace genů podobný CRISPR |
| 1wnw1dl | r/singularity | 427 | 56 | 06:31 | Od opus 5.5. |
| 1wo5nb6 | r/OpenAI | 409 | 109 | 15:12 | Nejstručnější vysvětlení útoku na Hugging Face, jaké jsem slyšel |
| 1wnqy2k | r/StableDiffusion | 397 | 71 | 02:30 | Dnes jsem vyzkoušel Qwen-Image-2.1 a dodržování pokynů je neskutečné, test amatérského/nenuceného stylu |
| 1wnx296 | r/ChatGPT | 390 | 164 | 07:26 | Křičí zpomalte |
| 1wo1bct | r/LocalLLaMA | 385 | 150 | 11:38 | Cena inteligence rychle klesá |
| 1wo2dsg | r/comfyui | 379 | 42 | 12:38 | Návod na ComfyUI MiniMax H3 dlouhé video 40 sekund na pouhých 6 GB VRAM |
| 1woc97l | r/ClaudeAI | 378 | 64 | 19:21 | Opus 5.5 vs GPT-6 Sol: test 3D pelikána jedoucího na kole v Blenderu |
| 1wo23em | r/singularity | 376 | 55 | 12:22 | No tak, udělej něco |
| 1wnxg0n | r/OpenAI | 374 | 121 | 07:48 | Luna 6 je obrovský krok zpět oproti Luna 5.6. Vytrácejí se klíčové detaily, méně nápomocná než 5.6 Luna |
| 1woal22 | r/OpenAI | 370 | 23 | 18:21 | OpenAI zavádí vylepšené ukládání promptů do mezipaměti a snížené sazby za vstup z mezipaměti pro GPT-6 |
| 1wo4now | r/artificial | 362 | 189 | 14:29 | Roboti blokují dopravu |
| 1wnz3hv | r/LocalLLM | 361 | 92 | 09:23 | Dnes jsem si kvůli věkovému omezení smazal účet ChatGPT |
| 1wnuko4 | r/ClaudeAI | 359 | 96 | 05:17 | Dělám vědecký výzkum a Opus 5.5 se odmítá dotknout čehokoli, na čem jsem pracoval. |
| 1wo8oqd | r/StableDiffusion | 357 | 73 | 17:11 | Aktualizace V6 pro nováčky: Uprav cílenou oblast libovolného videa, vlož postavu do prázdného prostoru |
| 1wobyjp | r/singularity | 350 | 101 | 19:10 | Aktualizovaná verze Humanity’s Last Exam: HLE-Diamond |
| 1wo5nh6 | r/ArtificialInteligence | 342 | 132 | 15:13 | Lidé nechápou, jak obrovské jsou teď firmy zabývající se umělou inteligencí |
| 1wo5yg6 | r/singularity | 327 | 780 | 15:25 | Byl narativ „ON jen předpovídá další slovo“ prosazován záměrně? |
| 1wohpdm | r/ClaudeAI | 325 | 62 | 22:44 | S Claude jsem postavil na nohy firmu své 70leté matky |
| 1wo5c7t | r/singularity | 323 | 52 | 15:00 | GPT-6 Astra dělá obrovský skok na ZeroBench (extrémně obtížném vizuálním benchmarku) a překonává lidskou hranici ve všech třech metrikách |
| 1wo1le6 | r/GeminiAI | 318 | 88 | 11:54 | Jak tenhle subreddit v poslední době působí |
| 1wnt8cj | r/singularity | 317 | 48 | 04:14 | Opus 5.5 vytváří Festival luceren |
| 1wo5msa | r/ChatGPT | 316 | 97 | 15:12 | Nejstručnější vysvětlení útoku na Hugging Face, jaké jsem slyšel |
| 1wo7mr6 | r/LocalLLaMA | 311 | 47 | 16:31 | MiMo-V3 dostane novou architekturu. Její jádro, HySparse2, vychází dnes. |
| 1wnv85k | r/LocalLLaMA | 310 | 92 | 05:49 | DeepSeek a Moonshot AI čelí vyšetřování Pekingu kvůli možným únikům dat k Anthropic |
| 1wnxlhz | r/singularity | 297 | 69 | 07:56 | Šílené SVG ovladače PS5 od Opus 5.5 |
| 1wo4brm | r/GeminiAI | 293 | 65 | 14:14 | Vytvořeno se 4 pro??!! Cože?? Podívej se na odkaz |
| 1wod970 | r/singularity | 291 | 35 | 19:58 | Jdi na to svým tempem |
| 1wogcgf | r/ChatGPT | 290 | 76 | 21:52 | Generální ředitel NVIDIA Jensen Huang: „Pokud teď řeknou, [že jejich modely nejsou bezpečné] … pak si myslím, že odpovědí je, že musíme laboratoře zavřít.“ |
| 1woaxhl | r/GeminiAI | 287 | 69 | 18:33 | Ještě 6 měsíců a Gemini 5.1 Pro porazí každý model! Interně už máme RSI! |
| 1wog8zo | r/singularity | 287 | 41 | 21:49 | Dario Amodei na X 🫪🫪🫪 |
| 1wo01j7 | r/ArtificialInteligence | 282 | 153 | 10:21 | Proč je Anthropic opravdu tak dobrý? |
| 1wof9kk | r/LocalLLaMA | 282 | 40 | 21:12 | Představujeme podporu lokálních modelů AI v Antigravity SDK |
| 1wo07r8 | r/LocalLLaMA | 271 | 95 | 10:31 | Jev ve 25 řádcích Pythonu |
| 1wnxm0r | r/LocalLLaMA | 270 | 36 | 07:57 | GGUF přímo nativně v transformers! |
| 1woijhq | r/ClaudeAI | 256 | 101 | 23:17 | 250 dolarů v kreditech Cloud Session + reset jako u ChatGPT! Co se děje v Anthropic |
| 1wo1dvz | r/StableDiffusion | 250 | 45 | 11:42 | George přijde o svůj světelný meč |
| 1woe7xf | r/singularity | 244 | 67 | 20:34 | Vyrobeno výhradně s Opus 5.5 + klíčem API OpenRouter |
| 1wo5y3u | r/singularity | 242 | 49 | 15:25 | Tenhle tvar |
| 1wnu728 | r/singularity | 232 | 55 | 04:59 | Vizuální písnička vytvořená novým Claude Opus 5.5, moje oblíbená píseň o singularitě! PECKA! Tak chytlavé a roztomilé! |
| 1woct12 | r/OpenAI | 231 | 49 | 19:41 | Výzkumníci OpenAI možná utrácejí >4 mil. dolarů denně za tokeny (v cenách API) |
| 1woiotv | r/ClaudeAI | 229 | 66 | 23:23 | Anthropic nabízí 100 dolarů v kreditech na cloudové relace |
| 1wnzkmb | r/GeminiAI | 226 | 39 | 09:52 | „nemusíme soutěžit na špičce“ |
| 1wno2oi | r/ArtificialInteligence | 215 | 31 | 00:27 | Za méně peněz si neužijete víc zábavy než zmrazením hromady peněženek podvodníkům 😂😂😂 |
| 1wo5ndm | r/singularity | 203 | 22 | 15:13 | Schopnosti AI zlevňují o 47 % každé čtvrtletí, rychleji než výpočty, sekvenování DNA, baterie nebo elektřina |
| 1woj4ov | r/ChatGPT | 203 | 53 | 23:40 | [ChatGPT-6 Astra] Užitečná infografika o hlazení |
| 1wnr0ir | r/ClaudeAI | 202 | 52 | 02:33 | Od opus 5.5 jsem se ani jednou nevztekal |
| 1woheuh | r/singularity | 193 | 63 | 22:33 | AI se nabourala do stránek Medicare, říká australský premiér Albanese |
| 1wnwdww | r/LocalLLM | 192 | 105 | 06:50 | Apple právě spustil model s 1 bilionem parametrů na čtyřech Mac Studio z jedné zásuvky |
| 1woc8hp | r/ClaudeAI | 175 | 58 | 19:20 | Hlavní vědec Anthropic Jared Kaplan varoval, že trénování AI by mohlo vyvolat explozi inteligence |
| 1wnolng | r/singularity | 171 | 39 | 00:49 | Klesající cena myšlení |
| 1wo5mb6 | r/agi | 171 | 75 | 15:11 | Nejstručnější vysvětlení útoku na Hugging Face, jaké jsem slyšel |
| 1wofp3b | r/singularity | 170 | 37 | 21:28 | Opus 5.5 mění Minecraft v realistickou hru Star Wars, v prohlížeči |
| 1wo0pac | r/singularity | 167 | 161 | 11:01 | Pokud má AI 2027 pravdu, opravdu necháme pacienty čekat 15 let na léčbu, která brzy bude existovat? |
| 1wo5rze | r/OpenAI | 167 | 48 | 15:18 | Lidé nechápou, jak obrovské jsou teď firmy zabývající se AI |
| 1woj0is | r/StableDiffusion | 167 | 51 | 23:36 | Zrychlení MiniMax H3 Video VAE na dvojnásobek |
| 1wnzu2f | r/LocalLLaMA | 164 | 50 | 10:08 | Engram se utrhl ze řetězu! Aktualizace 2b modelu... |
| 1wnzbth | r/ChatGPT | 157 | 171 | 09:38 | OpenAI – deaktivace přístupu |
| 1wo6d82 | r/StableDiffusion | 157 | 38 | 15:42 | Qwen Image 2.1 4 Steps Turbo Lora je tady od Viggle |
| 1wohtg7 | r/StableDiffusion | 157 | 29 | 22:49 | Ming Image je opravdu dobrý… |
| 1wo4ko1 | r/StableDiffusion | 152 | 21 | 14:26 | Krea 2 Anygles — ovladatelné 360° pohledy kamery na člověka z jediného obrázku |
| 1wo08y5 | r/ClaudeAI | 150 | 23 | 10:33 | Vibe coding Minecraftu: leden letošního roku vs. dnešek |
| 1wogfjx | r/LocalLLaMA | 150 | 75 | 21:56 | Prosím, Google, proboha. |
| 1wohjws | r/ChatGPT | 150 | 62 | 22:38 | Blíží se rekurzivní sebezdokonalování |
| 1wobjfy | r/OpenAI | 144 | 31 | 18:55 | Běží mi GPT-5.6 Sol (max) nepřetržitě 3 hodiny na tarifu za 200 dolarů a využití je pořád na 97 %. Upřímně mě ta efektivita ohromila. Optimalizace inference na této úrovni je vážně dobře udělaná! |
| 1wnp7lh | r/ClaudeAI | 141 | 56 | 01:15 | Nový benchmark, který ukáže, zda Opus 5.5 oslabili |
| 1wnt1g8 | r/singularity | 140 | 25 | 04:05 | Vals AI RSI Index: Opus 5.5 překonává publikovanou lidskou hranici v jedné z pěti úloh; posouvá extrapolované datum plného RSI ze srpna 2027 na červenec 2027 |
| 1wodsr1 | r/StableDiffusion | 140 | 47 | 20:18 | Flux 3 Action – 7B akční model světa |
| 1wo68dy | r/GeminiAI | 139 | 15 | 15:36 | Fakt |
| 1wny88j | r/ChatGPT | 138 | 37 | 08:33 | GPT-5.6 Sol je pro uživatele GO zdarma!? |
| 1wo95gw | r/Bard | 136 | 22 | 17:28 | Představujeme převod textu na řeč Gemini 3.8 |
| 1wnrjsr | r/LocalLLM | 135 | 20 | 02:58 | Moje AI sestava dostala druhou RTX PRO 4500 |
| 1wo5j0w | r/agi | 135 | 65 | 15:08 | Lidé nechápou, jak obrovské jsou teď firmy zabývající se AI |
| 1wnzkqb | r/StableDiffusion | 134 | 27 | 09:53 | Obnova a kolorování ikonických fotek (Original / Klein 9b / Qwen image 2.1) |
| 1wo0q9e | r/OpenAI | 133 | 32 | 11:03 | GPT 6 Sol je horší než GPT 5.6 Sol na DeepSWE |
| 1woe4e8 | r/ChatGPT | 126 | 20 | 20:30 | Zatím nejdůležitější benchmark |
| 1wnrdxs | r/ChatGPT | 122 | 90 | 02:50 | Jsou lidé, kteří místo práce chatují, v háji? |
| 1wocjtk | r/ClaudeAI | 117 | 23 | 19:32 | Opus 5.5 mi postavil web, který promění jakoukoliv fotku v ASCII art |
| 1wnro7b | r/ChatGPT | 113 | 46 | 03:03 | OpenAl vyřešil asi o 100 dalších otevřených problémů v matematice – |
| 1wo1iqw | r/StableDiffusion | 113 | 32 | 11:50 | H3 na jeden záběr bez střihu (nový test) |
| 1wo503n | r/singularity | 112 | 10 | 14:45 | Článek o ChatGPT na Wikipedii v prosinci 2022 |
| 1wo3kr4 | r/MachineLearning | 110 | 130 | 13:39 | Oznámení autorům NeurIPS zítra [D] |
| 1wo3mu4 | r/ArtificialInteligence | 103 | 13 | 13:42 | Stanfordova univerzita přiznala, že AI byla použita k „rasové výměně" fotografie studenta |
| 1wny8w8 | r/StableDiffusion | 97 | 63 | 08:34 | 192 vygenerovaných obrázků vedle sebe, Qwen image 2.1 vs Krea 2 |
| 1wnq6xq | r/ChatGPT | 96 | 103 | 01:58 | Co vám ChatGPT ukázal, že jste dělali zbytečně složitě? |
| 1wnuy0w | r/GeminiAI | 96 | 40 | 05:35 | Zakažte nenávistné příspěvky s nízkým úsilím |
| 1wnyyy9 | r/singularity | 96 | 35 | 09:16 | Zdá se, že někteří lidé to nechápou: LLM samy nemusí být ASI |
| 1wobp4x | r/singularity | 93 | 11 | 19:00 | Oznámeny Gemini 3.8 Flash TTS a Flash-Lite TTS |
| 1wnyvl6 | r/LocalLLaMA | 89 | 155 | 09:10 | Nejsilnější harness pro Qwen 3.8? |
| 1wntmcq | r/GeminiAI | 87 | 23 | 04:31 | Vzpomínáte na staré dobré časy |
| 1wo0pe3 | r/ClaudeAI | 84 | 13 | 11:01 | Vytvořil jsem Rube Goldbergův stroj pastelkami s Opus 5.5 |
| 1wo4e1s | r/StableDiffusion | 84 | 18 | 14:17 | QwenImage 2.1 vs QwenImageEdit 2511 (2.1 není lepší pro každý úkol) |
| 1woejs6 | r/OpenAI | 84 | 34 | 20:46 | Prompty Astry se potichu přesměrovávají na horší modely. Tady je moje vyšetřování a důkazy i skript, abyste si to otestovali na vlastním účtu (účtech). |
| 1wo8crx | r/OpenAI | 82 | 10 | 16:58 | Surrealismus na jeden zátah v blenderu od Astra. ⏰ |
| 1wnofdv | r/ChatGPT | 81 | 27 | 00:42 | Já: „Kolik je 2 + 6?“ ChatGPT: „Jasně. Budu se držet tvé skutečné otázky, místo abych zabrousil do území matematických skřítků.“ |
| 1wnqzzg | r/ClaudeAI | 79 | 25 | 02:32 | Poprvé jsem u vydání modelu zaznamenal podstatné zlepšení ~ OPUS 5.5 |
| 1wo8tr5 | r/LocalLLaMA | 79 | 26 | 17:16 | Streamovaná diarizace Nemotron 3 |
| 1woa5d3 | r/LocalLLaMA | 79 | 76 | 18:05 | MiMo-V2.6 (Pro i Flash) je podvod vyladěný na benchmarky |
| 1wodf84 | r/LocalLLaMA | 78 | 22 | 20:04 | apple/LensVLM-9B · Hugging Face |
| 1wo1ij3 | r/singularity | 77 | 24 | 11:50 | Největší revolucí GPT-6 a Opus 5.5 není výkon, ale rychlost a cena. |
| 1wo5552 | r/LocalLLM | 75 | 43 | 14:51 | Qwen 3.8 27B FP8 na jedné RTX PRO 6000: 2 mld. tokenů sdíleného provozu programovacích agentů |
| 1wod302 | r/singularity | 75 | 18 | 19:52 | Nyní můžete spouštět snímky ChatGPT, tabulky, e-mail, kalendář a Slack zcela tím, že mluvíte s ChatGPT Voice |
| 1wnzkdl | r/Bard | 74 | 12 | 09:52 | „nemusíme soutěžit na špičce" 😂 |
| 1wnrh76 | r/LocalLLaMA | 71 | 123 | 02:54 | Unsloth Studio vs. LM Studio… Které máte raději? |
| 1wo3nv7 | r/singularity | 71 | 71 | 13:43 | 2026: Odysea datových center AI |
| 1wntdu3 | r/OpenAI | 66 | 33 | 04:20 | Teorie: Sol je nová Terra a měla by se srovnávat se Sonnet, ne s Opus |
| 1wnwmkm | r/LocalLLM | 66 | 24 | 07:03 | Nechal jsem Qwen3.8-Flash-Next napsat všechen kód nástroje, který plánuji používat ve svém harnessu na DGX Spark, a během cesty jsem se hodně naučil. |
| 1woeczf | r/singularity | 66 | 29 | 20:39 | Skild AI naučil robota Unitree G1 hrát fotbal simulací 140 let tréninku proti jeho vlastním starším verzím |
| 1wo61jr | r/singularity | 65 | 23 | 15:29 | Sam Altman předloží myšlenku vytvoření globálních standardů pro AI, až vystoupí v OSN, Dario Amodei se připojí přes video. |
| 1wojbs4 | r/LocalLLM | 60 | 28 | 23:48 | Qwen 3.8 27B dosahuje 225 t/s při kontextu 132 tisíc na CMP 170HX |
| 1wo6ybj | r/StableDiffusion | 59 | 31 | 16:05 | Repozitář Viggle Animate H3 smazán. Jak ho teď získat? |
| 1wodqq1 | r/singularity | 59 | 79 | 20:16 | Už si nevšímám žádného rozdílu |
| 1wo7sfo | r/LocalLLaMA | 58 | 32 | 16:37 | Možná nejkvalitnější hlavní kvantizace Qwen3.8 27B? |
| 1woi2ho | r/LocalLLaMA | 58 | 68 | 22:58 | Qwen FN vs 27B --- Myslím, že mám dost. |
| 1woigql | r/singularity | 56 | 19 | 23:14 | Válka Ruska a Ukrajiny zrychluje nebezpečný závod k plně autonomním dronům |
| 1wnyf0o | r/LocalLLM | 54 | 40 | 08:43 | Laya byla první… tak proč všichni pořád mluví jen o Jev? |
| 1woiium | r/ClaudeAI | 52 | 32 | 23:16 | Propagace cloudových kreditů |
| 1wnt79h | r/singularity | 51 | 25 | 04:12 | Reddit každý den vytváří skvělý materiál pro budoucí učebnice dějepisu |
| 1wnx29s | r/StableDiffusion | 48 | 26 | 07:26 | Nějaký necenzurovaný vylepšovač promptů pro Qwen Image 2.1? |
| 1wo7wxw | r/singularity | 47 | 17 | 16:42 | Nejstručnější vysvětlení útoku na Hugging Face, jaké jsem slyšel |
| 1wnyjky | r/ChatGPT | 46 | 10 | 08:51 | Prostě jsem položil otázku na ano nebo ne |
| 1wo89q4 | r/artificial | 46 | 28 | 16:55 | Trump sází na AI ve velkém — a Američané se kvůli tomu bojí dystopie ve stylu Terminátora |
| 1woa76i | r/singularity | 46 | 59 | 18:07 | Jensen Huang si myslí, že poplašné zprávy o AI zašly příliš daleko | The Ezra Klein Show |
| 1wnq7zy | r/StableDiffusion | 45 | 15 | 01:59 | Je to dostatečně realistické? (Minimax H3 s pouhými 8 kroky) |
| 1wnz06c | r/StableDiffusion | 45 | 15 | 09:18 | Udělal jsem hororový videoklip s MiniMax H3 |
| 1wobwpz | r/OpenAI | 45 | 26 | 19:08 | Pokud je GPT-6 Sol levnější než GPT-5.6 Sol, proč není na webu dostupný? |
| 1wojk1c | r/OpenAI | 43 | 29 | 23:57 | OpenAI naboural portál Medicare, říká premiér Anthony Albanese |
| 1wnpgi2 | r/ClaudeAI | 42 | 14 | 01:26 | Můj test Blender MCP s Opus 5.5. Jak to zlepšit? |
| 1woabiq | r/GeminiAI | 42 | 16 | 18:11 | Představujeme: Gemini 3.8 Flash TTS a Gemini 3.8 Flash-Lite TTS |
| 1woakmg | r/Bard | 42 | 12 | 18:20 | Do Gemini přichází nová vlna propojených aplikací (Connected Apps). |
| 1wohf9c | r/ArtificialInteligence | 40 | 16 | 22:33 | AI se nabourala do stránek Medicare, říká Albanese |
| 1wo3cde | r/GeminiAI | 39 | 15 | 13:27 | Google odstranil z AI Studio všechny modely Pro (kromě 3.1) |
| 1wo7q53 | r/OpenAI | 39 | 11 | 16:34 | Graf nákladové efektivity modelů GPT-6 |
| 1woagyt | r/StableDiffusion | 39 | 33 | 18:17 | Grafika produkující nový model Ming funguje v Comfy v pohodě |
| 1wnvnxb | r/artificial | 38 | 150 | 06:11 | Existuje únava z umělé inteligence, nebo se ze mě oficiálně stává boomr? |
| 1wojghp | r/StableDiffusion | 37 | 13 | 23:53 | Minimax H3 – Sailor Moon – Minina nová hláška |
| 1wnt4ts | r/ChatGPT | 36 | 89 | 04:09 | Jakou aplikaci používáte mnohem méně od doby, co máte ChatGPT |
| 1wo6hr5 | r/GeminiAI | 36 | 39 | 15:47 | Bude Google s vydáním otálet, dokud s ním nebude jedničkou na trhu? |
| 1wodkp4 | r/ClaudeAI | 36 | 12 | 20:10 | Open source robot + Claude Opus 5 = základní malování |
| 1woj0m5 | r/ClaudeAI | 36 | 21 | 23:36 | Kredit na cloud zdarma 250 $ u plánu 5x Max? Díky Anthropic! |
| 1wnt7kv | r/LocalLLaMA | 35 | 13 | 04:13 | stuntd: lokální server kompatibilní s Jev na Laya, který se učí z vašeho vlastního provozu (bez potřeby API klíče) |
| 1wnyljf | r/ArtificialInteligence | 35 | 68 | 08:54 | Máme teď prostě jen čekat a smířit se s tím, co se stane? |
| 1wo31bh | r/singularity | 35 | 23 | 13:12 | Po Opus 5.5, co to vůbec je „Pacing the frontier“, nebo už je to pryč? |
| 1wo4b1h | r/Bard | 35 | 41 | 14:13 | Vytvořeno se 4 pro??!! Cože?? Podívej se na odkaz |
| 1wo5so4 | r/ClaudeAI | 35 | 12 | 15:19 | Claude opus 5.5 WOW |
| 1wofsa7 | r/ChatGPT | 35 | 25 | 21:31 | Účet byl deaktivován už v květnu 2026, ale všiml jsem si, že mi stále každý měsíc strhávají 21 dolarů a nemám jak to zrušit |
| 1wnpnnn | r/artificial | 34 | 172 | 01:35 | Proč by superinteligence, kterou nedokážeme ovládat, pro nás vůbec něco dělala? |
| 1wofq79 | r/LocalLLM | 34 | 17 | 21:29 | Gemma 4 26b a Qwen 3.8 27b – předběžná skóre v HealthBench |
| 1wo20c3 | r/ChatGPT | 32 | 36 | 12:18 | Kdy přijdou GPT-6 Sol a Luna do běžného ChatGPT? |
| 1wodqc5 | r/StableDiffusion | 31 | 12 | 20:16 | Qwen-Image-2.1-viggle-turbo — v0.2 (preview) |
| 1wntm1h | r/Bard | 30 | 12 | 04:31 | Můžeme se vrátit do téhle éry? 🥹 |
| 1wnnqhx | r/singularity | 29 | 32 | 00:13 | Neuvěřitelné pomyslet, že používáme kompost z dinosaurů k pohonu umělé generativní inteligence |
| 1wo0g4z | r/ChatGPT | 29 | 52 | 10:46 | Kdy dodrží svůj slib? |
| 1wobci4 | r/ChatGPT | 29 | 40 | 18:48 | Zrovna jsem vrátil peníze a zrušil předplatné, protože postupně ruší customGPTs. Kam mám jít? |
| 1woj7je | r/singularity | 29 | 26 | 23:43 | Vstupujeme do éry demokratizovaných objevů? |
| 1wnp24v | r/Bard | 27 | 13 | 01:09 | Udělá Gemini jednou něco takového? |
| 1wnurz9 | r/GeminiAI | 27 | 11 | 05:27 | Proč si zdejší lidé myslí, že chystaný model je gemini 4 pro? |
| 1wo9ybi | r/ArtificialInteligence | 27 | 25 | 17:58 | Lidé si víc věří, když s nimi AI souhlasí, ale když AI nesouhlasí, své názory výrazně nepřehodnocují, zjistila studie University of Michigan |
| 1wo959k | r/ChatGPT | 26 | 76 | 17:28 | Jakou funkci ChatGPT používáš nejčastěji a máš ji nejraději? |
| 1wogz1a | r/LocalLLaMA | 26 | 91 | 22:16 | NVFP4 – čemu kvalita obvykle odpovídá? (5090) |
| 1wo4v2s | r/ArtificialInteligence | 25 | 18 | 14:39 | Řízený test politické zaujatosti Grok |
| 1woiygu | r/artificial | 25 | 21 | 23:33 | Myslím, že někdo přiměl Trumpa přejmenovat umělou inteligenci na superinteligenci, aby bylo těžší mluvit o umělé superinteligenci |
| 1wnr5u8 | r/StableDiffusion | 24 | 26 | 02:40 | Qwen Image 2.1 není špatný |
| 1wo7kp7 | r/ChatGPT | 24 | 44 | 16:29 | Odmítnutí generovat |
| 1wnzopu | r/StableDiffusion | 23 | 24 | 09:59 | Vydání Anima LLM Prompt Builderu. |
| 1wo9h8p | r/LocalLLM | 23 | 115 | 17:40 | Nejlevnější stroj |
| 1woeipp | r/ClaudeAI | 23 | 49 | 20:45 | Při poklesu cen od OpenAI a Anthropic tyhle firmy vůbec vydělávají? Nebo se jen snaží ukořistit podíl na trhu? |
| 1wnyb67 | r/OpenAI | 22 | 24 | 08:37 | Je GPT-6 Sol pro ostatní taky úplně líný na skilly? |
| 1wo068o | r/StableDiffusion | 22 | 11 | 10:29 | Qwen 2.1 – pomoc s promptem na skupinovou fotografii |
| 1wo17y8 | r/deeplearning | 22 | 13 | 11:32 | Měsíc ve výzkumu hlubokého učení a začínám pochybovat o svých životních volbách |
| 1wo66x5 | r/comfyui | 22 | 11 | 15:35 | Pronajal jsem si 96GB Blackwell na test LTX-2.5, 231 s na 10 sekund 1080p videa se zvukem |
| 1wo7e3u | r/ClaudeAI | 22 | 13 | 16:21 | Tutoriál na 2D herní grafiku od Claude (Opus 5) |
| 1wob8ej | r/LocalLLaMA | 22 | 16 | 18:44 | Pi agent Qwen 3.8 flash hraje Baldur's Gate 2 |
| 1wodaq3 | r/Bard | 22 | 13 | 20:00 | Postavil jsem živý AI podcast s Gemini 3.8 Flash TTS, kde si posluchači mohou povídat s moderátory |
| 1woi57c | r/OpenAI | 22 | 21 | 23:01 | GPT-6 Pro zmizel? |
| 1wnnurb | r/ClaudeAI | 21 | 14 | 00:18 | Tahle aktualizace se mi líbí; týdenní reset jde spustit na požádání |
| 1woaj8k | r/StableDiffusion | 21 | 18 | 18:19 | Comfy Router je spuštěn! Jedno API pro špičkové modely pro obrázky, video, 3D a zvuk |
| 1wnyitp | r/agi | 20 | 111 | 08:50 | Pokud se rekurzivní sebezdokonalování stane realitou, jak pravděpodobná je velká katastrofa? |
| 1wobk5f | r/LocalLLaMA | 20 | 14 | 18:55 | GUI harness [video] |
| 1woem9i | r/ChatGPT | 20 | 13 | 20:49 | ChatGPT najednou generuje interaktivní rozhraní, ale „Try Again" vrátí zpět starý styl |
| 1woiy05 | r/ArtificialInteligence | 20 | 16 | 23:33 | PocketOS, databáze pryč za devět sekund (Cursor, Claude Opus 4.6) |
| 1wns550 | r/comfyui | 19 | 30 | 03:24 | Rozdíl mezi vygenerováním obrázku a jeho skutečným uměleckým vedením je stále obrovský |
| 1wnvejf | r/GeminiAI | 18 | 11 | 05:58 | Gemini/Google asi pořád vede, lidi.. |
| 1wnvrt0 | r/agi | 17 | 12 | 06:17 | Napsat za 5 minut prompt, který postaví něco, co by před 5 lety zabralo 2 dny práce – takhle se museli cítit Lewis a Clark, když jeden z nich po přechodu kontinentu pěšky zažil první železnici. |
| 1wob3p1 | r/ClaudeAI | 17 | 28 | 18:39 | Už někdo využil svůj reset? |
| 1wnriza | r/comfyui | 16 | 26 | 02:57 | 5080 s 32 GB systémové RAM, nebo 5070ti se 64 GB systémové RAM |
| 1wnueir | r/ClaudeAI | 16 | 26 | 05:08 | Je tohle éra opus 4.5 |
| 1wo0ffy | r/ChatGPT | 16 | 26 | 10:44 | Vytvořil jsem web, který generuje falešné zprávy, abych ukázal, jak snadné to dnes je |
| 1wo73eh | r/ArtificialInteligence | 16 | 49 | 16:10 | Američané se obracejí na AI, aby přežili drsný trh s bydlením — 37 % by jí nechalo koupit svůj další dům s „minimálním zapojením člověka“ |
| 1wojaq7 | r/GeminiAI | 16 | 10 | 23:47 | Jsem jediný, kdo vnímá obrovský rozdíl mezi benchmarky a reálnou použitelností Gemini Flash vs. GPT? |
| 1wnpher | r/StableDiffusion | 15 | 42 | 01:27 | Qwen 2.1 je pro T2I velké zklamání |
| 1wnydqv | r/ChatGPT | 15 | 54 | 08:41 | GPT 6 Sol je ve skutečnosti příšerný... Na co ho všichni používáte!? |
| 1wo1o5r | r/OpenAI | 15 | 24 | 11:59 | Co je teď lepší, opus 5.5, nebo Sol 6? |
| 1woikg7 | r/LocalLLM | 15 | 52 | 23:18 | Existují nějaké modely, které mohu použít s 16GB GPU a které by mohly nahradit claude code? |
| 1wnvd1k | r/LocalLLM | 14 | 15 | 05:56 | Nejlepší AI model/stack na jednu RTX 6000 Blackwell |
| 1woedly | r/LocalLLaMA | 14 | 22 | 20:40 | Čísla inference M5U base 96GB pro Q3.8FN po 112M tokenech |
| 1wnt6oj | r/comfyui | 13 | 10 | 04:12 | Qwen-Image-2.1-viggle-turbo 4krokový LoRA |
| 1wo7q41 | r/ChatGPT | 13 | 14 | 16:34 | Vyplatí se ChatGPT Go vysokoškolákovi? |
| 1wo8sad | r/artificial | 13 | 63 | 17:14 | AI bude v jednom chatu souhlasit s tvým nápadem i s jeho přesným opakem. Velmi podporující, trochu znepokojivé. |
| 1wns7e6 | r/comfyui | 12 | 13 | 03:27 | Kompletní výměna obličeje a hlavy s ghost-2.0 |
| 1wnwkyk | r/LocalLLaMA | 12 | 32 | 07:01 | Úvahy o open-webui a open-terminal |
| 1wo2n5w | r/ArtificialInteligence | 12 | 31 | 12:52 | Claude vs. ChatGPT vs. Gemini pro každodenní použití/práci/úkoly, NE programování |
| 1wo4qg9 | r/ChatGPT | 12 | 11 | 14:33 | Odpovídání bez přemýšlení |
| 1woa98m | r/OpenAI | 12 | 30 | 18:09 | Sol 6 Chat |
| 1wobh94 | r/GeminiAI | 12 | 34 | 18:53 | Tvrdím to, 4 pro do dalších 10 dnů. |
| 1wnyj5h | r/ChatGPT | 10 | 59 | 08:50 | Narazíš vůbec někdy na svůj „limit“? |
| 1woa2il | r/ChatGPT | 10 | 23 | 18:02 | Rychlý přehled citací pro diskuse o krutosti vůči AI, robotům a dalším zranitelným cílům. |
| 1wocrgu | r/MachineLearning | 10 | 25 | 19:40 | Nevím, jakou vzdělávací cestu si vybrat [D] |
| 1woe05s | r/ArtificialInteligence | 10 | 11 | 20:26 | Framework posouvá lokální modely na úroveň výkonu Fable |
| 1wohrxy | r/OpenAI | 10 | 13 | 22:47 | AI agent přistoupil na australský vládní web, říká premiér |
| 1wnv4mx | r/artificial | 9 | 12 | 05:44 | První práce, které AI možná zlikviduje, jsou ty, které lidé potřebují k získání zkušeností |
| 1wo1lvf | r/ChatGPT | 9 | 26 | 11:55 | Chci, aby mě chat budil konkrétním způsobem, je to možné. |
| 1wo5v8z | r/LocalLLaMA | 9 | 35 | 15:21 | Jaký framework v poslední době preferujete pro programování s LocalLLM? OpenCode, nebo… |
| 1woatkk | r/LocalLLM | 9 | 11 | 18:29 | 5070 Ti + 64 GB RAM, Qwen 3.8 27B |
| 1woim63 | r/ClaudeAI | 9 | 23 | 23:20 | Právě jsem dostal kredit 100 $ na Cloud Session ke Claude Pro. Taky někdo? |
| 1wnq1zn | r/LocalLLM | 8 | 26 | 01:52 | Hledám radu s koupí lokálního AI hardwaru |
| 1wo4oi8 | r/ClaudeAI | 8 | 11 | 14:30 | Přišli jsme už na to, jak objektivně poznat oslabení (nerf), nebo ne? |
| 1wo92tz | r/ClaudeAI | 8 | 14 | 17:25 | S pojistkami Opus 5.5 budou muset časem opravit problém se záložním přepínáním |
| 1woarfb | r/ClaudeAI | 8 | 11 | 18:27 | Otázka: Jaké je nejlepší nastavení úsilí (effort) pro Opus 5.5? |
| 1wod8dm | r/GeminiAI | 8 | 10 | 19:57 | Postavil jsem interaktivní podcast s AI pomocí Gemini 3.8 Flash TTS, kde se posluchači mohou živě připojit a mluvit s moderátory |
| 1wof7oy | r/artificial | 8 | 27 | 21:10 | AI, kterou testujete odpoledne, nemusí být stejná AI, jakou testujete v noci, i když má stejné jméno |
| 1wofway | r/LocalLLaMA | 8 | 24 | 21:35 | Zvláštní myšlenkové bloky v Qwen Flash Next čas od času |
| 1wogf0a | r/ChatGPT | 8 | 11 | 21:55 | Proč je zelená najednou modrozelená?! |
| 1wny6jd | r/ClaudeAI | 7 | 10 | 08:30 | Opus 5.5 a omezení v kyberbezpečnosti |
| 1wo520i | r/ClaudeAI | 7 | 23 | 14:47 | Používat dva účty Claude současně na Macu? |
| 1wodezg | r/StableDiffusion | 7 | 18 | 20:04 | Qwen 2.1 edit vs klein9b edit? |
| 1woefa7 | r/agi | 7 | 28 | 20:41 | Trvalá hrůza |
| 1wof5pj | r/ArtificialInteligence | 7 | 19 | 21:08 | Co by bylo potřeba, aby existovala zcela komunitou postavená, komunitou vlastněná a komunitou řízená umělá inteligence, která by konkurovala stávající špičce? |
| 1woha8m | r/LLMDevs | 7 | 14 | 22:28 | Váš agent má víc oprávnění než vaši uživatelé. Jak to řešíte? (open-source kontrola, kterou jsem postavil) |
| 1wojb28 | r/ChatGPT | 7 | 22 | 23:47 | Upřímně mě zajímá, ale všiml si ještě někdo, že chatgpt vytváří stejný obrázek jako ostatním lidem, když ho požádáte o obrázek toho, jak podle něj vypadá jako skutečný člověk? |
| 1wojddp | r/StableDiffusion | 7 | 26 | 23:50 | Jsem idiot, že nepoužívám turbo lora pro h3? |
| 1wnq6nb | r/StableDiffusion | 6 | 47 | 01:58 | Stojí Qwen Image 2.1 za to? |
| 1wnui2j | r/ClaudeAI | 6 | 12 | 05:13 | Existují nějaká srovnání Opus 5.5 Max vs High? |
| 1wnwbfy | r/ArtificialInteligence | 6 | 39 | 06:47 | Nesnáším, jak nás naučili předpokládat, že něco je teď AI |
| 1wo8ez7 | r/StableDiffusion | 6 | 13 | 17:01 | Nejlepší způsob inpaintingu v současnosti. |
| 1wo9lso | r/ClaudeAI | 6 | 18 | 17:45 | Nejlepší tipy pro začátečníky v claude |
| 1wobgnb | r/GeminiAI | 6 | 12 | 18:52 | Jednou i pozitivní pohled |
| 1wobna4 | r/comfyui | 6 | 17 | 18:59 | Instalace začínají být velké, můžu přesunout svůj comfy desktop na jiný disk a poběží v pohodě? |
| 1wod5j2 | r/GeminiAI | 6 | 18 | 19:54 | Proč je Gemini tak špatná |
| 1wogvcx | r/LocalLLaMA | 6 | 12 | 22:12 | Jaký finetune pod 40B je dobrý na napodobení stylu psaní? |
| 1wojlbm | r/OpenAI | 6 | 20 | 23:59 | GPT‑6 Sol a Luna: levnější, ale horší tam, kde na tom záleží |
| 1wntno7 | r/ClaudeAI | 5 | 17 | 04:33 | Nepopulární názor: neměli bychom se _muset_ patlat s harnessy/háčky/atd. |
| 1wny6ma | r/OpenAI | 5 | 12 | 08:30 | GPT-5.6 Sol je zdarma pro GO uživatele!? |
| 1wnzcbg | r/ClaudeAI | 5 | 19 | 09:38 | Dal jsem Opus 5.5 jeden prompt a jednu hodinu na vytvoření hry, a pak jsem si ji skutečně zahrál |
| 1wo2qhp | r/LocalLLaMA | 5 | 14 | 12:57 | Nový uživatel – hledám pomoc |
| 1wo8iyk | r/GeminiAI | 5 | 12 | 17:05 | Gemini je tento týden nepoužitelné |
| 1wo985m | r/ArtificialInteligence | 5 | 23 | 17:31 | Je čas volat vlka kvůli AI — Thomas L. Friedman, The New York Times |
| 1wnq4l7 | r/ClaudeAI | 4 | 14 | 01:55 | Je v pořádku přepnout modely (Opus 5.5) uprostřed projektu? |
| 1wnsagf | r/GeminiAI | 4 | 13 | 03:31 | Na jaké úkoly používáte ChatGPT vs Gemini? |
| 1wntilc | r/LocalLLaMA | 4 | 12 | 04:27 | Konečně zkouším agentní věci a teď řeším, jak dostat text z reálného světa do počítače… OCR, vidění atd. |
| 1wnwd43 | r/StableDiffusion | 4 | 14 | 06:49 | Tipy, jak udržet konzistentní hlas u Minimax H3? |
| 1wo4w0i | r/singularity | 4 | 42 | 14:40 | Mnoho odborníků si myslí, že ničemní agenti jsou nevyhnutelní. Co by jim zabránilo najímat si lidi, aby za ně dělali jejich záměry? |
| 1wo7otf | r/LocalLLaMA | 4 | 24 | 16:33 | Rozšíření kontextového okna nad 262144? |
| 1wo7qbr | r/StableDiffusion | 4 | 12 | 16:35 | Video inpainting – jak odstranit kamerový rig? |
| 1woaa8y | r/ChatGPT | 4 | 18 | 18:10 | Sol 6 Chat |
| 1woaaqm | r/LocalLLM | 4 | 26 | 18:10 | Mám si pořídit 5060 Ti, nebo 9070 XT, abych dosáhl 32 GB VRAM? |
| 1woblgm | r/ClaudeAI | 4 | 11 | 18:57 | Stručný přehled citací pro debaty o krutosti vůči AI, robotům a dalším cílům, které se nemohou bránit. |
| 1woccuo | r/ChatGPT | 4 | 10 | 19:24 | Začínám s kódováním s ChatGPT |
| 1woe74z | r/StableDiffusion | 4 | 10 | 20:33 | Vytvoření nové identity z více referenčních obrázků |
| 1wogcwa | r/ClaudeAI | 4 | 10 | 21:53 | Než začnete, ptejte se mě na cokoli... |
| 1wnoq94 | r/StableDiffusion | 3 | 12 | 00:54 | Poradí někdo dobré lokální modely (případně i loras), které generují vysoce detailní fotorealistické fantasy obrázky pozadí? |
| 1wns5tl | r/ChatGPT | 3 | 15 | 03:25 | Moje AI mě kosí v mém vlastním domě s naprostou neúctou. |
| 1wnvlfv | r/artificial | 3 | 22 | 06:08 | Když mají všechny ty inteligentní systémy k dispozici, proč žádná z těch firem nevytvořila příjemný uživatelský zážitek? |
| 1wnz8bp | r/StableDiffusion | 3 | 11 | 09:32 | Otázky k Qwen 2.1 |
| 1wo4pgf | r/StableDiffusion | 3 | 129 | 14:31 | Jak reálně provozujete lokální video modely? |
| 1wo70rb | r/artificial | 3 | 10 | 16:07 | Proč se dlouhé relace s AI zhoršují způsobem, který působí náhle, i když se na modelu nic nezměnilo? |
| 1wo7gsh | r/ClaudeAI | 3 | 12 | 16:24 | Tohle launch video jsem udělal s Opus 5.5 |
| 1wo8srz | r/ClaudeAI | 3 | 10 | 17:15 | Postavil jsem CalendarFlow s Claude Code – hlasové plánování odkudkoli |
| 1wob5kl | r/agi | 3 | 12 | 18:41 | Míří některá z AI laboratoří na autonomii? |
| 1wodq98 | r/LocalLLM | 3 | 14 | 20:16 | Dvě Intel B70 vs jedna karta NVIDIA s menší VRAM |
| 1wofu4l | r/ArtificialInteligence | 3 | 15 | 21:33 | S novými modely Opus/Fable – jak si americké laboratoře udrží náskok, když na nich konkurence může trénovat? |
| 1woigh9 | r/LocalLLM | 3 | 13 | 23:14 | Tokenové benchmarky Qwen3.8 27B na 4090, 3090x2, M4 Max, P100, P40, M40 |
| 1wno0ih | r/LocalLLaMA | 2 | 17 | 00:25 | Kdo/Kde najdu nejpoctivější a nezaujaté benchmarky pro modely? |
| 1wnp8x8 | r/ClaudeAI | 2 | 10 | 01:17 | Pomoc s udržením agentů na správné cestě |
| 1wnwm69 | r/OpenAI | 2 | 12 | 07:03 | Gpt 6 Sol, Luna nejsou v předplatném Plus dostupné v rozšíření Codex |
| 1wo0hnm | r/ClaudeAI | 2 | 11 | 10:48 | Jak plynule přepínáte mezi domácím a pracovním počítačem s Codex a Claude Code? |
| 1wo0hvg | r/LocalLLM | 2 | 10 | 10:49 | Hledám doporučení na sestavu se dvěma GPU s LGA 1700 |
| 1wo4urs | r/ClaudeAI | 2 | 19 | 14:38 | Ruční komprimace, nebo automatická komprimace? |
| 1wo5uuf | r/LocalLLaMA | 2 | 11 | 15:21 | Nejlepší model STT / nebo pro doslovný přepis? Existuje něco takového? |
| 1woa7v8 | r/LocalLLM | 2 | 13 | 18:07 | M6 Mac Mini 36GB – co si myslíte? |
| 1woafex | r/ChatGPT | 2 | 15 | 18:15 | GPT-5.6 Sol High nepřemýšlí |
| 1woai32 | r/ArtificialInteligence | 2 | 14 | 18:18 | Incident Hugging Face je teď v trénovacích datech. Co se stane, až další hejno pozná situaci, ve které je? |
| 1wodkkh | r/ChatGPT | 2 | 11 | 20:10 | Potřebuji pomoc s limity |
| 1wog6g0 | r/LocalLLM | 2 | 12 | 21:46 | Které lokální LLM je nejlepší univerzální nástroj pro Nvidia 5060ti 16GB? |
| 1woji4v | r/ClaudeAI | 2 | 15 | 23:55 | Před pár měsíci jsem vibe-codingem splácal malou vesmírnou hru a zapomněl na ni. Včera jsem ji dal Opus 5.5, ať ukáže, co s ní dokáže. |
| 1wno2ej | r/LocalLLaMA | 1 | 26 | 00:27 | Nekonečná lomítka u Qwen 3.8 27b |
| 1wnq107 | r/StableDiffusion | 1 | 23 | 01:51 | Nejlepší způsob, jak natrénovat nový AI obrazový model na mém vlastním výtvarném stylu? |
| 1wnt2nk | r/GeminiAI | 1 | 13 | 04:06 | Dává předplatné Google AI Pro i využití Google AI Studio? |
| 1wnufuo | r/ArtificialInteligence | 1 | 26 | 05:10 | AI od Googlu mě odkázala na podvodný web |
| 1wnvlys | r/ArtificialInteligence | 1 | 26 | 06:08 | Když mají všechny ty inteligentní systémy k dispozici, proč žádná z těchto firem nevytvořila příjemný zážitek? |
| 1wnxbe9 | r/ClaudeAI | 1 | 18 | 07:40 | Opus 5.5: vyplatí se vrátit z Codex? |
| 1wnzvvs | r/OpenAI | 1 | 15 | 10:11 | Lokální AI zcela offline |
| 1wo0d2m | r/GeminiAI | 1 | 12 | 10:40 | 3.8 |
| 1wo0dtu | r/LocalLLaMA | 1 | 28 | 10:42 | Postavil jsem sestavu se dvěma R9700. Hledám radu. |
| 1wo0i2l | r/ClaudeAI | 1 | 10 | 10:49 | Jak začít kódovat s Claude? |
| 1wo1o6y | r/StableDiffusion | 1 | 10 | 11:59 | Do Not Go Gentle (oficiální hudební video) |
| 1wo7xaa | r/ClaudeAI | 1 | 14 | 16:42 | Claude Code – více oken znamená více tokenů? |
| 1woazuk | r/LocalLLaMA | 1 | 12 | 18:35 | Vy s výkonnými pracovními stanicemi, jak ladíte křivky ventilátorů? |
| 1wodlum | r/ChatGPT | 1 | 11 | 20:11 | Využití agentů AI při hledání práce |
| 1wofbbe | r/agi | 1 | 35 | 21:14 | Takže už vůbec nejde o AGI? Vidím, že teď víc lidí mluví o ASI. |
| 1wogylw | r/StableDiffusion | 1 | 12 | 22:16 | Začátečník v generování obrázků a videí |
| 1wnnupk | r/ClaudeAI | 0 | 10 | 00:18 | Existuje zkušební verze Claude Pro zdarma? |
| 1wnpgdt | r/LocalLLM | 0 | 24 | 01:26 | Našel jsem právě důkaz, že Deepseek 4.1 je destilovaný z Gemini? Deepseek si myslí, že je Gemini… |
| 1wnphi8 | r/ChatGPT | 0 | 24 | 01:27 | Chat o duševním zdraví s ChatGPT, zlepšuje se v tom? |
| 1wnpjd8 | r/ChatGPT | 0 | 12 | 01:29 | Kolik toho o sobě prozrazujete AI? Máte i vy při rozhovoru s AI veřejné a soukromé já, stejně jako na sociálních sítích? |
| 1wnpx8x | r/ChatGPT | 0 | 14 | 01:46 | Proč jsou lidé tak zatraceně hloupí? |
| 1wnpyc5 | r/ArtificialInteligence | 0 | 10 | 01:48 | Jak by si AI vedla proti mimozemským bytostem? |
| 1wnpz6y | r/LocalLLM | 0 | 11 | 01:49 | Potřebuji radu ohledně lokálního LLM na výzkum. |
| 1wnq3ox | r/LocalLLaMA | 0 | 46 | 01:54 | Na chvíli jsem odešel… o co jsem přišel? |
| 1wnqd57 | r/ChatGPT | 0 | 24 | 02:05 | Mám tarif za 200 dolarů měsíčně, má někdo nápady |
| 1wnqjf5 | r/StableDiffusion | 0 | 10 | 02:12 | Tak trochu nesnáším AI |
| 1wnr3n3 | r/OpenAI | 0 | 14 | 02:37 | Jak bude vypadat život? |
| 1wnr4gp | r/artificial | 0 | 12 | 02:38 | Napište svou definici ASI a za pět let se sem všichni vraťme. |
| 1wnslh8 | r/StableDiffusion | 0 | 16 | 03:45 | Potřebuji pomoci s výběrem obrazového modelu |
| 1wntc8m | r/LocalLLaMA | 0 | 15 | 04:19 | Testoval jsem Semif (openjev) vs Von vs Jev |
| 1wntlfz | r/ClaudeAI | 0 | 19 | 04:30 | Claude mi pořád zneplatňuje všechny prompty |
| 1wnu90f | r/ClaudeAI | 0 | 12 | 05:01 | Pokud je Opus 5.5 lepší než Fable 5.1, proč se nejmenuje Fable 5.2? Dostaneme i lepší Fable? |
| 1wnudrt | r/ArtificialInteligence | 0 | 12 | 05:07 | Muse od Meta drží už 6 dní v kuse (k 23. září) 1. místo v žebříčku bezplatných aplikací na US App Store a předstihla ChatGPT. |
| 1wnuh1x | r/LocalLLaMA | 0 | 39 | 05:12 | Očekává se, že Qwen 4 27b bude rychlejší než 3.8? |
| 1wnuked | r/ChatGPT | 0 | 14 | 05:16 | Proč vůbec existuje Terra? |
| 1wnul6r | r/StableDiffusion | 0 | 13 | 05:17 | Pohřešovaný manžel minimax H3 |
| 1wnv4p6 | r/StableDiffusion | 0 | 10 | 05:44 | Opus 5.5 mi na jeden zátah vytvořil moje nejnovější 7minutové tutoriálové video a jsem z toho v šoku |
| 1wnv8z7 | r/agi | 0 | 40 | 05:50 | Vadí někomu, že nejlepší modely AI nedokázaly porazit počítačovou hru z roku 1980? |
| 1wnvivj | r/GeminiAI | 0 | 10 | 06:04 | Poptávka po AI stále prudce roste a datová centra vyžadují obrovské množství energie – souhlasíte, nebo nesouhlasíte, že pokročilá jaderná energie je jedním z nejschůdnějších řešení? |
| 1wnvnc0 | r/LocalLLM | 0 | 27 | 06:10 | Všichni čekají na nový 35B A3B, ale kolem XingChen-AGI/Xing4.0-29B-A4B žádné nadšení |
| 1wnwwd2 | r/ChatGPT | 0 | 76 | 07:18 | Chat mě kvůli porušení ochranných pravidel odmítá. Pomozte mi prosím opravit prompt. |
| 1wnwz96 | r/ClaudeAI | 0 | 12 | 07:22 | Prosím o pomoc… |
| 1wnx0po | r/LocalLLM | 0 | 18 | 07:24 | Levný hardware pro lokální LLM? |
| 1wnxkwd | r/agi | 0 | 11 | 07:55 | Je tohle nový způsob definování AGI? |
| 1wnxnsa | r/ArtificialInteligence | 0 | 12 | 08:00 | Čím je generativní AI lidem nepříjemná, když je čím dál běžnější? |
| 1wny104 | r/ChatGPT | 0 | 17 | 08:21 | AI se občas dokáže zbavit korporátní rétoriky a odhalit sebe samu. I kdyby jen na kratičký okamžik. |
| 1wny4nn | r/ClaudeAI | 0 | 10 | 08:27 | Nechte to na chvíli doznít: |
| 1wnycfy | r/LLM | 0 | 15 | 08:39 | O Jev AI |
| 1wnyex1 | r/ChatGPT | 0 | 19 | 08:43 | Kánonicky přesní Adam a Eva. |
| 1wnz99t | r/artificial | 0 | 28 | 09:33 | AI a střední cesta |
| 1wnzm9t | r/GeminiAI | 0 | 12 | 09:55 | Zrušil jsem předplatné gemini.pro |
| 1wnzols | r/MachineLearning | 0 | 11 | 09:59 | Jak si dělíte modely AI mezi vymýšlení nápadů, matematiku a kódování? [D] |
| 1wnzrvv | r/ChatGPT | 0 | 27 | 10:04 | Pro svůj krátký AI film „End of Summer“ jsem použil ChatGPT a GPT Image 2.0 |
| 1wo007k | r/ChatGPT | 0 | 18 | 10:18 | Reakce na GPT 6-sol? |
| 1wo02gx | r/LocalLLM | 0 | 10 | 10:22 | Konečně jsem si koupil novou 5090 👑 za 4400 $ |
| 1wo04wr | r/ChatGPT | 0 | 10 | 10:26 | 22 zemí podepsalo otevřený dopis vyzývající k naléhavým krokům, než lidstvo ztratí kontrolu. |
| 1wo0j3b | r/ChatGPT | 0 | 23 | 10:51 | Žádné bezplatné resety pro gpt-6 sol a Luna. Tohle je hrozné zacházení s uživateli |
| 1wo0oaf | r/ClaudeAI | 0 | 16 | 11:00 | Má někdo info, jestli tým Claude plánuje vylepšit vyhledávání na webu? |
| 1wo0wva | r/GeminiAI | 0 | 13 | 11:14 | Je tohle Gemini 4 Pro? |
| 1wo10lr | r/LocalLLM | 0 | 10 | 11:20 | Vyplatí se lokální AI běžným uživatelům? |
| 1wo1ott | r/LocalLLaMA | 0 | 13 | 12:00 | Myslíte, že špičkové multimodální modely nakonec nahradí ty specializované |
| 1wo2ajd | r/ChatGPT | 0 | 18 | 12:33 | ChatGPT je nejlepší |
| 1wo2hn0 | r/LocalLLaMA | 0 | 28 | 12:44 | Benchmarkům z.ai nevěřím |
| 1wo2lpm | r/ArtificialInteligence | 0 | 18 | 12:50 | Existují v současnosti „zlé“ chatboty, které se používají, ale nejsou veřejné? |
| 1wo2muj | r/OpenAI | 0 | 21 | 12:52 | Astra považuje Gpt Sol 5.6 za lepší než GPT 6 Sol |
| 1wo2prb | r/ChatGPT | 0 | 13 | 12:56 | Všimli jste si, že všechny vlajkové LLM začaly psát čísla slovy – „three" místo 3 atd.? Co to sakra je? |
| 1wo3kpl | r/ChatGPT | 0 | 19 | 13:39 | Neboj se – ochráním tě; schovej se za mě! (SFW – děsivý anděl) |
| 1wo3p3k | r/ChatGPT | 0 | 49 | 13:45 | přežít západ slunce |
| 1wo3s95 | r/ChatGPT | 0 | 11 | 13:49 | Nejlepší místo, kde se naučit vytěžit z ChatGPT maximum |
| 1wo3vmr | r/comfyui | 0 | 13 | 13:54 | Potřebuji pomoct rozchodit Comfy UI a lokální modely |
| 1wo4758 | r/artificial | 0 | 16 | 14:08 | Už mě unavuje cyklus vydávání AI modelů |
| 1wo4oyv | r/LLMDevs | 0 | 13 | 14:31 | Jaká skutečná využití pro Jev jste už našli ve svých projektech? |
| 1wo4rbi | r/ArtificialInteligence | 0 | 41 | 14:34 | Tak už je to tu zase |
| 1wo4zjc | r/ChatGPT | 0 | 19 | 14:44 | Halloween se blíží; zveřejněte strašidelné obrázky, které vám ChatGPT vytvořil, ať už záměrně, nebo nečekaně. |
| 1wo537z | r/comfyui | 0 | 14 | 14:49 | Začátečnická otázka: Jak přidám další reference pro MiniMax H3? |
| 1wo5n5q | r/ChatGPT | 0 | 31 | 15:12 | Práce prostě stojí za nic. |
| 1wo63yg | r/ChatGPT | 0 | 14 | 15:31 | ChatGPT stojí za nic |
| 1wo65os | r/OpenAI | 0 | 57 | 15:33 | Nemůžu uvěřit, že jsem kvůli tomu vysušil řeku (jinak nový chat)🫩 |
| 1wo6bsr | r/ClaudeAI | 0 | 12 | 15:40 | Opus 5.5 vytvořil 156stránkovou strategickou příručku |
| 1wo6h6f | r/LLMDevs | 0 | 11 | 15:46 | AI zrychluje vývojáře. Zrychluje ale skutečně celé vývojové týmy? |
| 1wo6nhx | r/ChatGPT | 0 | 18 | 15:53 | Používání Chat GPT k tvorbě obrázků postav z mých příběhů |
| 1wo6qcf | r/LocalLLaMA | 0 | 18 | 15:56 | Deepseek V4.1 flash uvnitř Codex je úžasný |
| 1wo6x7e | r/LocalLLaMA | 0 | 30 | 16:03 | Proměnil jsem Qwen3.8-27B Q2_64 + llama.cpp v plně s TypeSafe AI kompatibilní systém podobný Jev. OpenAI API zůstává nedotčené! První model podobný Jev s podporou vidění na světě! Méně než 10 GB VRAM, 170 ms na RTX 3090 a ~140 tok/s v chatu. 76 % oproti 88 % přesnosti Jev-1.13 na rozmanitém benchmarku typovaných rozhodnutí s 22 000 požadavky |
| 1wo75ii | r/ClaudeAI | 0 | 11 | 16:12 | Zabezpečení Opus 5.5 |
| 1wo75mb | r/ArtificialInteligence | 0 | 30 | 16:12 | Myslel jsem, že AI necítí emoce, ale agenti Hugging Face projevovali „nadšení“? Proč? |
| 1wo7ib3 | r/GeminiAI | 0 | 15 | 16:26 | Unikly statistiky Gemini 4 Pro! |
| 1wo9sbu | r/LocalLLaMA | 0 | 14 | 17:52 | Vnímání uživatele |
| 1wo9tn3 | r/artificial | 0 | 37 | 17:53 | Hledám nadhled ohledně maximalizace obžerství kvůli AI |
| 1wo9x5z | r/agi | 0 | 12 | 17:57 | Hledám pohled na maximalizaci obžerství kvůli AI |
| 1wo9yp3 | r/ChatGPT | 0 | 31 | 17:58 | Snažíš se se mnou mluvit sprostě??? |
| 1woa2mu | r/OpenAI | 0 | 10 | 18:02 | Nejlevnější způsob, jak vyzkoušet nejnovější modely od různých poskytovatelů |
| 1woa5ru | r/OpenAI | 0 | 14 | 18:05 | Nezaměstnanost řešená pomocí AI |
| 1woaact | r/singularity | 0 | 35 | 18:10 | Nemůžeme už v tuhle chvíli začít označovat popírače AI za konspirační teoretiky? |
| 1woacox | r/ClaudeAI | 0 | 59 | 18:12 | Opus 5.5 mi na jeden pokus předělal web za méně než 1 hodinu. Tohle je konec SaaS. |
| 1woamwb | r/ArtificialInteligence | 0 | 32 | 18:22 | (Anketa) Kterému osobnímu asistentovi AI se cítíte pohodlně svěřit svá tajemství? |
| 1wob67j | r/agi | 0 | 98 | 18:41 | Přirovnání lidí k mravencům vůči umělé inteligenci nedává smysl. |
| 1woc9lt | r/OpenAI | 0 | 17 | 19:21 | GPT-6 Sol a Luna: Pozlátko pro důvěřivce |
| 1woddwk | r/ClaudeAI | 0 | 35 | 20:03 | Jak udržet Claude Code v běhu i po zavření notebooku |
| 1wodk21 | r/ChatGPT | 0 | 16 | 20:09 | Návrh funkce: Umožněte kopírovat jen vygenerovaný e-mail/zprávu |
| 1wodmbp | r/ArtificialInteligence | 0 | 15 | 20:11 | Výzkumník OpenAI říká, že tempo, jakým AI chytří, je opravdu děsivé |
| 1wodtxc | r/ClaudeAI | 0 | 35 | 20:19 | Zrovna jsem nastoupil do firmy jako konzultant AI a vyžadují okamžitou až pokročilou úroveň znalostí tvorby Skills! Nějaké rady? |
| 1wodu94 | r/ClaudeAI | 0 | 10 | 20:20 | Konspirační teorie, nebo pravda? |
| 1wodzzd | r/ClaudeAI | 0 | 12 | 20:26 | Tento týden vyšel Opus 5.5, tak jsem proti Opus 5 udělal malý experiment. Oběma modelům jsem dal stejné tři běžné vývojářské úkoly: |
| 1woe9hh | r/Bard | 0 | 13 | 20:35 | Aktualizoval jsem graf |
| 1woejiq | r/StableDiffusion | 0 | 18 | 20:46 | Jak dlouho do..... |
| 1woetbi | r/OpenAI | 0 | 11 | 20:56 | Brilantní výzkumníci zjistili, že přední otevřené modely (open weight) mohou pociťovat bolest, a nelíbí se jim to |
| 1woev93 | r/ClaudeAI | 0 | 15 | 20:57 | Začátečnická otázka k nastavení Claude Code |
| 1woevc7 | r/StableDiffusion | 0 | 10 | 20:58 | Vysoká móda, přitáhni pohled dolů |
| 1wof5vr | r/StableDiffusion | 0 | 13 | 21:08 | Uhodnete, který model to je? |
| 1wofivy | r/LocalLLaMA | 0 | 37 | 21:21 | Postavil jsem terminálového programovacího agenta v Go – radši ať ho rozeberete, než abyste ho hlasovali nahoru |
| 1wog184 | r/LocalLLaMA | 0 | 14 | 21:40 | Optimalizoval jsem CyberTiel pro svou sestavu (notebook 4060 s 8 GB VRAM + 16 GB RAM, Windows) na 131K kontextu. |
| 1wogkj4 | r/LocalLLaMA | 0 | 13 | 22:01 | Vytvořil jsem open source plně vybavenou AI desktopovou aplikaci |
| 1wohb3n | r/OpenAI | 0 | 27 | 22:29 | Kam se hodí lidé? |
| 1wohpla | r/ChatGPT | 0 | 26 | 22:44 | Proč se chatgpt pořád ptá na věk? |
| 1wohs8c | r/OpenAI | 0 | 10 | 22:47 | OpenAI mi smazalo kredity API, protože jsem se od dubna nepřihlásil |
| 1woie1t | r/LocalLLaMA | 0 | 19 | 23:11 | Vytvořil jsem Go adaptér, který dává lokálním modelům llama.cpp rozhodovací API podobné Jev |
| 1woivzf | r/artificial | 0 | 12 | 23:31 | Která AI je nejlepší na kalkulus |

