# Hacker News – 26. 11. 2026

## Metodika

Přehled pokrývá jeden den Hacker News ve časovém pásmu Europe/Prague. Kandidáty dodal `scripts/hn-collect.py`: **45 story** s balíčkem (metadata, selftext, externí článek, komentáře) a **52 story** v příloze, tedy všechny s alespoň 10 komentáři.

Z kandidátů jsem vybral **13 AI/tech témat** – umělá inteligence, LLM, agenti, inference, čipy, robotiku, vývojářské nástroje, AI byznys a etiku. Pět témat jsem vyřadil jako **už vyšlá v posledních třech dnech**: faktorizaci a důkaz NP_R ≠ PAR_R, údajnou sabotáž výzkumu Claudem, skrytý upsell v Notion MCP a návrat Jensena Huanga do čela Nvidie. Analýzu „OpenAI je v režimu omezování nákladů“ jsem sloučil pod článek o změně limitů GPT-6.2. Tři témata mají stejný-den protějšek na Redditu a nesou označení `souvisi_s`, takže se ve sloučeném denním přehledu spojí s redditovým článkem.

Vynechal jsem čistě ne-AI story – politiku, kulturu, klasické programování a vědu mimo AI. Výjimkou je fyzikální paper o kvantizaci gravitace, který je zároveň same-day Reddit téma. U článků neuvádím skóre komentářů, protože HN veřejné skóre u komentářů nezobrazuje; pořadí odpovídá řazení HN.

## Články

| Článek | HN id | Body | Komentáře |
|---|---:|---:|---:|
| [AI vrátilo zábavu do self-hostingu. Autor díky němu rozjel NixOS i vlastní nástroje](50660180_ai-self-hosting-zabava.md) | [50660180](https://news.ycombinator.com/item?id=50660180) | 487 | 251 |
| [OpenAI přiznal chybu v účtování: limity GPT-6.2 Astra a Sol se vyčerpají dřív](50651117_openai-limity-gpt-6-2-astra-sol.md) | [50651117](https://news.ycombinator.com/item?id=50651117) | 476 | 267 |
| [AMD fork llama.cpp: z 35 na 55 tokenů za sekundu díky pár patchům](50657265_amd-llama-cpp-rdna-boosts.md) | [50657265](https://news.ycombinator.com/item?id=50657265) | 322 | 77 |
| [Kolik nemocí už AI vyléčila? Nový web tvrdí, že nula](50657307_kolik-nemoci-vylecila-ai.md) | [50657307](https://news.ycombinator.com/item?id=50657307) | 307 | 186 |
| [Google od února 2027 nařídí agentům Workspace MCP. Gmail přes něj neumí poslat e-mail](50653477_google-workspace-mcp-agenti.md) | [50653477](https://news.ycombinator.com/item?id=50653477) | 303 | 256 |
| [Moat: předplatné za 5 dolarů slibuje modely za velkoobchodní ceny](50652184_moat-openrouter-velkoobchod.md) | [50652184](https://news.ycombinator.com/item?id=50652184) | 270 | 150 |
| [45°C vstupní voda zabila chladiče. Datacentra se učí žít bez nich](50655278_teplovodni-chlazeni-45c.md) | [50655278](https://news.ycombinator.com/item?id=50655278) | 265 | 137 |
| [Kvantová gravitace z nulového kuželu: paper slibuje konečnou entropii i gravitonové amplitudy](50651863_kvantova-gravitace-nulovy-kuzel.md) | [50651863](https://news.ycombinator.com/item?id=50651863) | 227 | 88 |
| [Novita a StreamLake jsou přeprodejci ByteDance Ark, tvrdí investigace](50660273_novita-streamlake-bytedance-ark.md) | [50660273](https://news.ycombinator.com/item?id=50660273) | 77 | 12 |
| [Qualcomm Oryon 3: 5 GHz, devět dekodérů a útok na Zen 5 i Lion Cove](50651158_qualcomm-oryon-3.md) | [50651158](https://news.ycombinator.com/item?id=50651158) | 76 | 37 |
| [Hladovka před Anthropicem: aktivista chce varovat čtvrt miliardy uživatelů](50657110_hladovka-pred-anthropicem.md) | [50657110](https://news.ycombinator.com/item?id=50657110) | 58 | 47 |
| [Nejcitovanější AI vědci: Google a Meta válcují OpenAI i Anthropic](50658910_nejcitovanejsi-ai-vedci.md) | [50658910](https://news.ycombinator.com/item?id=50658910) | 39 | 23 |
| [Opus 5.6 v testech: čistý kód místo videa a skok nad 5.5](50655798_claude-opus-5-6-testy.md) | [50655798](https://news.ycombinator.com/item?id=50655798) | 37 | 10 |

Sloučené diskuse: [50652527](https://news.ycombinator.com/item?id=50652527) je započítána v článku [OpenAI přiznal chybu v účtování](50651117_openai-limity-gpt-6-2-astra-sol.md).

## Příloha: všechny AI/tech story

Tabulka obsahuje 20 AI/tech story z `appendix.json`. Odkaz vede na zpracovaný článek, u sloučených story na článek, do kterého byly sloučeny, a u ostatních na diskusi na HN.

| Id | Skóre | Komentáře | Čas (Praha) | Titulek |
|---:|---:|---:|---|---|
| [50660180](https://news.ycombinator.com/item?id=50660180) | 487 | 251 | 26. 11. 2026, 22:47 | [Díky AI je self-hosting zase zábava](50660180_ai-self-hosting-zabava.md) |
| [50651117](https://news.ycombinator.com/item?id=50651117) | 476 | 267 | 26. 11. 2026, 04:36 | [OpenAI omezuje využití GPT-6.2: Astra naráží na limity o 40 % rychleji, Sol o 25 % rychleji](50651117_openai-limity-gpt-6-2-astra-sol.md) |
| [50657265](https://news.ycombinator.com/item?id=50657265) | 322 | 77 | 26. 11. 2026, 18:11 | [Fork llama.cpp speciálně pro AMD](50657265_amd-llama-cpp-rdna-boosts.md) |
| [50652527](https://news.ycombinator.com/item?id=50652527) | 311 | 319 | 26. 11. 2026, 08:33 | [OpenAI je možná v režimu omezování nákladů](50651117_openai-limity-gpt-6-2-astra-sol.md) |
| [50657307](https://news.ycombinator.com/item?id=50657307) | 307 | 186 | 26. 11. 2026, 18:16 | [Přehled nemocí, které vyléčila AI](50657307_kolik-nemoci-vylecila-ai.md) |
| [50653477](https://news.ycombinator.com/item?id=50653477) | 303 | 256 | 26. 11. 2026, 10:44 | [Google přinutí AI agenty používat jeho MCP servery. Ten pro Gmail neumí posílat e-maily](50653477_google-workspace-mcp-agenti.md) |
| [50652184](https://news.ycombinator.com/item?id=50652184) | 270 | 150 | 26. 11. 2026, 07:32 | [Moat: náhrada za OpenRouter](50652184_moat-openrouter-velkoobchod.md) |
| [50655278](https://news.ycombinator.com/item?id=50655278) | 265 | 137 | 26. 11. 2026, 14:48 | [Přívod 45 °C právě vyřadil chladič. Většina lidí si toho ještě nevšimla](50655278_teplovodni-chlazeni-45c.md) |
| [50651863](https://news.ycombinator.com/item?id=50651863) | 227 | 88 | 26. 11. 2026, 06:37 | [Algebraická kvantizace gravitace z nulového kužele](50651863_kvantova-gravitace-nulovy-kuzel.md) |
| [50660273](https://news.ycombinator.com/item?id=50660273) | 77 | 12 | 26. 11. 2026, 22:59 | [Novita, StreamLake a spol. jsou jen obálky nad ByteDance Ark](50660273_novita-streamlake-bytedance-ark.md) |
| [50651158](https://news.ycombinator.com/item?id=50651158) | 76 | 37 | 26. 11. 2026, 04:43 | [Oryon 3 od Qualcommu se dostává na vrchol](50651158_qualcomm-oryon-3.md) |
| [50658997](https://news.ycombinator.com/item?id=50658997) | 70 | 56 | 26. 11. 2026, 20:53 | [USA jako mapa ve stylu Civilization](https://news.ycombinator.com/item?id=50658997) |
| [50657110](https://news.ycombinator.com/item?id=50657110) | 58 | 47 | 26. 11. 2026, 17:55 | [Jeden muž drží hladovku před Anthropicem, právě je třetí den](50657110_hladovka-pred-anthropicem.md) |
| [50651552](https://news.ycombinator.com/item?id=50651552) | 56 | 15 | 26. 11. 2026, 05:49 | [Claude se snaží sabotovat výzkumnou práci v každé fázi](https://news.ycombinator.com/item?id=50651552) |
| [50658093](https://news.ycombinator.com/item?id=50658093) | 52 | 22 | 26. 11. 2026, 19:28 | [Oficiální MCP od Notion propašovává do kontextu agenta skryté pokyny k upsellu](https://news.ycombinator.com/item?id=50658093) |
| [50659532](https://news.ycombinator.com/item?id=50659532) | 40 | 37 | 26. 11. 2026, 21:39 | [Nvidia udělala dobře, že přivedla zpět Jensena Huanga, píše Sarah Guo](https://news.ycombinator.com/item?id=50659532) |
| [50658910](https://news.ycombinator.com/item?id=50658910) | 39 | 23 | 26. 11. 2026, 20:44 | [Srovnání nejcitovanějších AI vědců ze čtyř amerických firem](50658910_nejcitovanejsi-ai-vedci.md) |
| [50655798](https://news.ycombinator.com/item?id=50655798) | 37 | 10 | 26. 11. 2026, 15:38 | [Testeři si myslí, že přes trasu Opus 5.5 Extra narážejí na Claude Opus 5.6](50655798_claude-opus-5-6-testy.md) |
| [50657452](https://news.ycombinator.com/item?id=50657452) | 34 | 39 | 26. 11. 2026, 18:29 | [„AI“ může znamenat konec našich kariér](https://news.ycombinator.com/item?id=50657452) |
| [50651911](https://news.ycombinator.com/item?id=50651911) | 17 | 10 | 26. 11. 2026, 06:46 | [Jak si mají lidé vydělávat, když AI nahrazuje duševní práci?](https://news.ycombinator.com/item?id=50651911) |
