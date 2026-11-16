# AI souhrn z Redditu – 1. listopadu 2026

## Metodika

Data pocházejí z přímého sběru Redditu přes `scripts/rd-collect-web.py`; skóre a počty komentářů jsou hodnoty z doby sběru, časy jsou uvedené v pásmu Europe/Prague. Kandidátní sadu tvořilo 40 postů z AI subredditů, v příloze je všech 308 postů, které měly v okně dne alespoň 10 komentářů.

Před výběrem jsem porovnal každého kandidáta se seznamem témat z posledních tří dnů (`logs/recent-2026-11-01-rd.md`). Přísně jsem vyřadil **10 témat / 23 kandidátních postů**, které se už objevily jinde nebo šlo o stejnou událost, produkt či mem: DRAM a Sam Altman (9 postů), sloučené limity ChatGPT a Codex (3), leak GPT-6.2 Astra (2), Anthropic a zákaz reverzního inženýrství her (3), Memdoor s pěti Qweny (1), Krea 2 (1), nedotažené kolo OpenAI (1), tarify Anthropic 20x (1) a dva mimotematické memy (2). Žádný z těchto postů není zařazen ani jako „další diskuse“.

Po filtraci zůstalo 17 článků. Duplicitní témata se mezi nimi nevyskytla, proto nemá žádný článek sloučené „další diskuse“. U dvou externích článků (Mythos a Dawkins) byl zdroj částečně za paywallem; články proto vycházejí z selftextu, dostupného textu a komentářů. Příloha obsahuje všechny posty s alespoň 10 komentáři v původním znění, bez překladu.

## Články

| # | Titulek | Subreddit | Skóre | Komentáře | ID |
|---:|---|---|---:|---:|---|
| 1 | [Na Hugging Face údajně unikl model třídy Mythos od Anthropicu 💀](1xl47f5_unik-mythos-14-bilionu-parametru.md) | r/ClaudeAI | 2702 | 594 | `1xl47f5` |
| 2 | [Dal jsem Claude přístup ke vzdáleným teleskopům. Teď každou noc pozoruje oblohu.](1xkxsca_claude-ridi-roboticke-teleskopy.md) | r/ClaudeAI | 2158 | 266 | `1xkxsca` |
| 3 | [Vyšel Heretic 2.0: Úprava modelů pro každého](1xl2tcm_heretic-2-0-model-modification.md) | r/LocalLLaMA | 1233 | 119 | `1xl2tcm` |
| 4 | [Tým DeepSeek Harness zveřejnil na GitHubu jako open-source prototyp základní architekturu svého Super-agenta, neustále běžícího autonomního agenta.](1xkoi9g_deepseek-super-agent-prototyp.md) | r/singularity | 875 | 18 | `1xkoi9g` |
| 5 | [Qwen3.8 27b (Q6) jen tak mimochodem prolamuje reCAPTCHA](1xl3yxo_qwen-3-8-prolomil-recaptcha.md) | r/LocalLLM | 632 | 86 | `1xl3yxo` |
| 6 | [4 Argon z ničeho nic začal mluvit čínsky???](1xkym72_gemini-4-argon-cinsky.md) | r/GeminiAI | 514 | 113 | `1xkym72` |
| 7 | [Programování je vyřešené* (platí výjimky)](1xl90rr_crap-gemma-4-x86-binarky.md) | r/LocalLLaMA | 369 | 55 | `1xl90rr` |
| 8 | [Demis Hassabis říká, že datová centra pro AI by měla být krásná a měli bychom brát vážně jejich dopad na naše fyzické okolí](1xl9hrk_hassabis-datacentra-krasna.md) | r/singularity | 364 | 75 | `1xl9hrk` |
| 9 | [Jsem stavební inženýr. Claude je v mém oboru neuvěřitelně silná, ale používat AI je prakticky tabu. Je to tak i v jiných odvětvích?](1xlc0v6_stavebni-inzenyr-claude-tabu.md) | r/ClaudeAI | 339 | 189 | `1xlc0v6` |
| 10 | [Už lidé při nákupu hardwaru pro AI nedávají pozor?](1xl4ckr_stary-pc-ai-stroj-prodej.md) | r/LocalLLaMA | 338 | 88 | `1xl4ckr` |
| 11 | [Richard Dawkins: ‚Myslel jsem, že AI za mého života nepřijde, ale přišla – a s velkou vervou‘](1xl006d_dawkins-ai-s-pomstou.md) | r/singularity | 299 | 52 | `1xl006d` |
| 12 | [[GLB-3D-Coder] Drobný 4B kódovací model, který tvoří 3D assety pro Godot a další herní enginy](1xlh0zw_glb-3d-coder-assety-godot.md) | r/LocalLLaMA | 284 | 60 | `1xlh0zw` |
| 13 | [Díky Claude jsem mohl NordicTracku a jeho předplatnému iFit pěkně ukázat prostředníček!](1xlg9nd_claude-code-odemkl-bezecky-pas.md) | r/ClaudeAI | 225 | 23 | `1xlg9nd` |
| 14 | [Matematik optimistický ohledně singularity. „Doufám, že AI pomůže matematikům vymanit se ze svěrací kazajky, kdy je svazuje první přirozená hypotéza, kterou nedokážou dokázat, a věnovat se odhalování hlubších záhad protkaných celým naším oborem.“](1xlb3ys_matematika-se-zmenila-calegari.md) | r/singularity | 203 | 13 | `1xlb3ys` |
| 15 | [4 Strix Halo boxy! Konečně jsem součástí lokální AI](1xknvog_ctyri-strix-halo-boxy.md) | r/LocalLLM | 198 | 100 | `1xknvog` |
| 16 | [PSA: ultracode už není omezený jen na režim max effort](1xks0kb_ultracode-low-effort.md) | r/ClaudeAI | 197 | 31 | `1xks0kb` |
| 17 | [Claude + Obsidian](1xlby9y_claude-code-obsidian.md) | r/ClaudeAI | 194 | 127 | `1xlby9y` |

## Příloha: všechny posty s alespoň 10 komentáři

Celkem 308 postů, seřazeno podle skóre. Odkazy u vybraných témat míří na odpovídající článek; ostatní posty jsou uvedeny bez odkazu.

| ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| `1xl3w49` | r/ChatGPT | 7444 | 313 | 1. 11. 2026, 15:05 | RAM needs to be collectivized for the greater good |
| `1xkqzgx` | r/OpenAI | 2880 | 133 | 1. 11. 2026, 02:37 | Consent is key |
| `1xl47f5` | r/ClaudeAI | 2702 | 594 | 1. 11. 2026, 15:18 | [Anthropic's Mythos-class model allegedly leaked on Hugging Face 💀](1xl47f5_unik-mythos-14-bilionu-parametru.md) |
| `1xkxsca` | r/ClaudeAI | 2158 | 266 | 1. 11. 2026, 09:22 | [I gave Claude access to remote telescopes. Now she books the sky every night.](1xkxsca_claude-ridi-roboticke-teleskopy.md) |
| `1xkvdlt` | r/ChatGPT | 1702 | 413 | 1. 11. 2026, 06:49 | Subscription Cancelled.  Fuck Altman. |
| `1xlen1c` | r/OpenAI | 1695 | 224 | 1. 11. 2026, 22:14 | Sam Altman is right |
| `1xl0269` | r/ChatGPT | 1495 | 33 | 1. 11. 2026, 11:47 | Don't be greedy donate all RAM at your nearest data center |
| `1xl641n` | r/ChatGPT | 1431 | 23 | 1. 11. 2026, 16:37 | O Sam o Sam! |
| `1xl6vk8` | r/singularity | 1346 | 276 | 1. 11. 2026, 17:08 | Anthropic's growing restrictions are creating a new divide in the AI capabilities race: Gemini 4 Argon recreates Pixar's iconic intro, while Claude Opus 5.5 refuses over copyright and builds a toaster instead—highlighting the gap between what frontier AI can do and what companies allow it to do. |
| `1xl2tcm` | r/LocalLLaMA | 1233 | 119 | 1. 11. 2026, 14:16 | [Heretic 2.0 released: Model modification for everyone](1xl2tcm_heretic-2-0-model-modification.md) |
| `1xkoi9g` | r/singularity | 875 | 18 | 1. 11. 2026, 00:32 | [DeepSeek Harness team published the underlying architecture for their Super-agent, an always-on autonomous agent, as an open-source prototype on GitHub.](1xkoi9g_deepseek-super-agent-prototyp.md) |
| `1xkvyva` | r/LocalLLM | 770 | 23 | 1. 11. 2026, 07:26 | that's a bingo |
| `1xl7cyr` | r/ClaudeAI | 665 | 118 | 1. 11. 2026, 17:27 | we're actually going to get Fable 5.5 and GPT-6.2 Astra the same week |
| `1xksfg0` | r/LocalLLM | 652 | 78 | 1. 11. 2026, 03:57 | Come and take my ram sam |
| `1xl3yxo` | r/LocalLLM | 632 | 86 | 1. 11. 2026, 15:08 | [Qwen3.8 27b (Q6) casually breaking reCAPTCHA](1xl3yxo_qwen-3-8-prolomil-recaptcha.md) |
| `1xl5v0a` | r/OpenAI | 595 | 87 | 1. 11. 2026, 16:27 | In Defense is Sam. He's completely right about DRAM |
| `1xkxt7a` | r/LocalLLaMA | 518 | 111 | 1. 11. 2026, 09:24 | Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard |
| `1xkym72` | r/GeminiAI | 514 | 113 | 1. 11. 2026, 10:16 | [4 Argon randomly started speaking in Chinese???](1xkym72_gemini-4-argon-cinsky.md) |
| `1xlfsxm` | r/ChatGPT | 501 | 77 | 1. 11. 2026, 23:02 | Wow. |
| `1xl0rs3` | r/singularity | 446 | 89 | 1. 11. 2026, 12:29 | OpenAI is testing GPT-6.2 Astra |
| `1xl2ij0` | r/ChatGPT | 395 | 173 | 1. 11. 2026, 14:02 | End of an era. We never really appreciated the separate usage. Worst decision ever by OpenAI |
| `1xl123t` | r/StableDiffusion | 372 | 134 | 1. 11. 2026, 12:46 | Krea 2 Fine-Tuning Goes Horribly Right |
| `1xl90rr` | r/LocalLLaMA | 369 | 55 | 1. 11. 2026, 18:31 | [Coding is solved* (exclusions apply)](1xl90rr_crap-gemma-4-x86-binarky.md) |
| `1xl9hrk` | r/singularity | 364 | 75 | 1. 11. 2026, 18:49 | [Demis Hassabis says AI data centers should be beautiful and we should take their effect on our physical surroundings seriously](1xl9hrk_hassabis-datacentra-krasna.md) |
| `1xlc0v6` | r/ClaudeAI | 339 | 189 | 1. 11. 2026, 20:28 | [Civil engineer here. Claude is incredibly powerful in my field, but using AI is practically taboo. Is it like this in other industries ?](1xlc0v6_stavebni-inzenyr-claude-tabu.md) |
| `1xl4ckr` | r/LocalLLaMA | 338 | 88 | 1. 11. 2026, 15:24 | [Don't people pay attention anymore when buying hardware for AI?](1xl4ckr_stary-pc-ai-stroj-prodej.md) |
| `1xkwvhe` | r/singularity | 326 | 137 | 1. 11. 2026, 08:23 | So Anthropic's Claude AI blocks video game cloning and reverse-engineering, to avoid companies to get out of business, and that's ethical? |
| `1xl006d` | r/singularity | 299 | 52 | 1. 11. 2026, 11:44 | [Richard Dawkins: ‘I thought AI wouldn’t come in my lifetime but it has – with a vengeance’](1xl006d_dawkins-ai-s-pomstou.md) |
| `1xl3efd` | r/ChatGPT | 291 | 203 | 1. 11. 2026, 14:43 | Beginning of the end. This is what we call foreshadowing. |
| `1xlh0zw` | r/LocalLLaMA | 284 | 60 | 1. 11. 2026, 23:56 | [[GLB-3D-Coder] A tiny 4B coding model that creates 3D assets for Godot and other game engines](1xlh0zw_glb-3d-coder-assety-godot.md) |
| `1xl5wab` | r/ClaudeAI | 254 | 133 | 1. 11. 2026, 16:28 | The 20x ultra plan limits is utter insanity |
| `1xku8j7` | r/OpenAI | 247 | 33 | 1. 11. 2026, 05:40 | Hey HBO, PLEASE bring back Silicon Valley. I NEED this. I swear it’ll make more money than Game of Thrones. PLZ 😭😭😭 |
| `1xlg9nd` | r/ClaudeAI | 225 | 23 | 1. 11. 2026, 23:22 | [Thanks to Claude, I was able to give NordicTrack and their iFit subscription a big F U!](1xlg9nd_claude-code-odemkl-bezecky-pas.md) |
| `1xkvwj8` | r/OpenAI | 217 | 11 | 1. 11. 2026, 07:22 | OpenAI Raises Less Than Half of $30 Billion Target in Latest Round |
| `1xkp54i` | r/ChatGPT | 206 | 100 | 1. 11. 2026, 01:02 | Chat-Codex Shared Usage Announcement |
| `1xlb3ys` | r/singularity | 203 | 13 | 1. 11. 2026, 19:53 | [Singularity-Whitepilled Mathematician. "I hope AI can help mathematicians break out of the straitjacket of being constrained by the first natural conjecture they cannot prove, and work on unraveling the deeper mysteries woven throughout our subject. "](1xlb3ys_matematika-se-zmenila-calegari.md) |
| `1xknvog` | r/LocalLLM | 198 | 100 | 1. 11. 2026, 00:01 | [4 Strix Halo boxes! Finally joined local AI](1xknvog_ctyri-strix-halo-boxy.md) |
| `1xks0kb` | r/ClaudeAI | 197 | 31 | 1. 11. 2026, 03:34 | [PSA: ultracode isn't locked to max effort anymore](1xks0kb_ultracode-low-effort.md) |
| `1xlby9y` | r/ClaudeAI | 194 | 127 | 1. 11. 2026, 20:25 | [Claude + Obsidian](1xlby9y_claude-code-obsidian.md) |
| `1xlbx3n` | r/ChatGPT | 186 | 35 | 1. 11. 2026, 20:24 | Welcome to the training set 💀 |
| `1xko2cs` | r/ClaudeAI | 186 | 40 | 1. 11. 2026, 00:10 | Claude's game porting skills are insane |
| `1xlfd9v` | r/artificial | 185 | 40 | 1. 11. 2026, 22:44 | Grok Bot users ran out of a week’s usage overnight, and Elon Musk says the agent was costing too much |
| `1xl0ybl` | r/ChatGPT | 181 | 154 | 1. 11. 2026, 12:40 | What's a ChatGPT lifehack you use every day that most people don't know about? |
| `1xkoos6` | r/comfyui | 170 | 18 | 1. 11. 2026, 00:41 | Blender previsualization with MiniMax H3 |
| `1xl6amz` | r/StableDiffusion | 163 | 43 | 1. 11. 2026, 16:45 | Sulphur-3 is coming soon! |
| `1xkqdzt` | r/GeminiAI | 161 | 82 | 1. 11. 2026, 02:06 | What the hell man |
| `1xkp0qp` | r/OpenAI | 155 | 141 | 1. 11. 2026, 00:58 | Chat-Codex Shared Limit Announcement |
| `1xl7ssz` | r/OpenAI | 153 | 37 | 1. 11. 2026, 17:44 | OpenAI will honor a shared robots.txt signal so websites can opt out of AI training |
| `1xlec67` | r/LocalLLaMA | 147 | 57 | 1. 11. 2026, 22:01 | Getting incredible results with a single RTX 3090ti and 128gb of ram. Deepseek-V4.1-Flash-1017 (35 tok/s decode) and Qwen3.8-Flash-Next (130 tok/s decode) |
| `1xl5eh2` | r/OpenAI | 145 | 69 | 1. 11. 2026, 16:08 | The one thing I was dreading for 2 years… |
| `1xl0pwq` | r/ChatGPT | 145 | 17 | 1. 11. 2026, 12:26 | Chatgpt feeling sad with 4 others |
| `1xkzony` | r/LocalLLaMA | 145 | 24 | 1. 11. 2026, 11:24 | new research: A tiny 109M-parameter model outperforms models up to 72B parameters at image-text alignment, using 42× less training data |
| `1xlboqi` | r/LocalLLaMA | 122 | 15 | 1. 11. 2026, 20:15 | llama2.c on a 2006 iPod @ 80 MHz w/ 64 MB ram and no FPU |
| `1xkook7` | r/ChatGPT | 119 | 13 | 1. 11. 2026, 00:40 | Using ChatGPT dot to reconstruct a film sequence as editable Blender previs |
| `1xkubhx` | r/LocalLLM | 118 | 69 | 1. 11. 2026, 05:45 | Anthropic keeps rolling out new censorship measures. Its new backend auditing feature scans chat context for potential misuse after every message. |
| `1xkz44b` | r/singularity | 117 | 36 | 1. 11. 2026, 10:48 | Worry about AI taking jobs rose for almost every job this year. Programmers are the exception, their worry peaked in March 2024 |
| `1xkom3s` | r/ChatGPT | 115 | 96 | 1. 11. 2026, 00:37 | I legit thought this was Onion for a while |
| `1xl7oy1` | r/singularity | 113 | 91 | 1. 11. 2026, 17:40 | OpenAI wants to rebrand its data centers as "AI compute campuses" after the midterms |
| `1xl96h6` | r/ClaudeAI | 112 | 35 | 1. 11. 2026, 18:37 | Deepdumb - a benchmark to measure AI's response to persistent stupidity |
| `1xlfsjd` | r/StableDiffusion | 107 | 23 | 1. 11. 2026, 23:02 | Making MOSS-Base look good for realism (Workflow Included) |
| `1xl8nqv` | r/ChatGPT | 107 | 41 | 1. 11. 2026, 18:17 | OpenAI is dressing up shared usage limits as an upgrade. How very Orwellian. |
| `1xl1zn3` | r/LocalLLaMA | 94 | 24 | 1. 11. 2026, 13:36 | DeepSeek: Exploring Super-agent Design: Towards a More Autonomous Agent System |
| `1xl8hgc` | r/comfyui | 87 | 43 | 1. 11. 2026, 18:10 | How are people replacing characters in porn so consistently |
| `1xlcke4` | r/ChatGPT | 84 | 63 | 1. 11. 2026, 20:50 | For those of us on the Plus tier - and from December onwards - what's the point in us paying for this anymore? |
| `1xl9k40` | r/ChatGPT | 84 | 13 | 1. 11. 2026, 18:52 | Protect your RAM! |
| `1xkz4mo` | r/LocalLLaMA | 77 | 102 | 1. 11. 2026, 10:49 | Am I Crazy Or GLM 5.3 Flash is Hilarious? |
| `1xksxqd` | r/LocalLLM | 77 | 17 | 1. 11. 2026, 04:25 | SAM (RAM)  is not a waste when its gives unlimited tokens and dont ban me if u dont like my Prompts . |
| `1xl2byr` | r/LocalLLM | 75 | 24 | 1. 11. 2026, 13:53 | I tried the Opus 5.5 vs GPT-6.1 Terra Blender oak tree challenge with a local Qwen3.8-Flash-Next NVFP4 on my RTX 5090 |
| `1xkziyu` | r/ChatGPT | 75 | 46 | 1. 11. 2026, 11:14 | Chat mode is going to burn our agentic allowance now?? This feels like a bait and switch… did any other Pro subscribers get this email? |
| `1xksj75` | r/LocalLLaMA | 74 | 70 | 1. 11. 2026, 04:02 | 64GB isn't the dead zone anymore if you run agents |
| `1xl9c92` | r/ClaudeAI | 68 | 60 | 1. 11. 2026, 18:43 | Forget the usual Claude tips. What are the strange things you do that actually help? |
| `1xkzjkj` | r/ChatGPT | 68 | 25 | 1. 11. 2026, 11:15 | Sam Altman says home RAM is "quite terrible." Here's my 1TB server at 4% utilization. |
| `1xkr53t` | r/ClaudeAI | 66 | 91 | 1. 11. 2026, 02:46 | Most people still sneering at vibe coded apps can't read code. True or False? |
| `1xkpq5l` | r/LocalLLM | 66 | 96 | 1. 11. 2026, 01:31 | Flash Next Q4 tried to fetch Alibaba's URLs in my environment too (yours might as well) |
| `1xl9uxc` | r/LocalLLM | 65 | 20 | 1. 11. 2026, 19:03 | Pretty happy with my local AI setup (M5 Max 128 GB) |
| `1xl7soa` | r/ChatGPT | 65 | 41 | 1. 11. 2026, 17:44 | Merging Chat & Work Limits Should Be Optional |
| `1xkud9n` | r/ChatGPT | 65 | 22 | 1. 11. 2026, 05:48 | What to expect about the up-coming merge of ChatGPT and Codex usage |
| `1xl5nwh` | r/ChatGPT | 63 | 57 | 1. 11. 2026, 16:19 | Nooooooooooooooooooo ChatGPT app |
| `1xkv63f` | r/LocalLLM | 58 | 131 | 1. 11. 2026, 06:36 | Those who are in the aristocracy (RTX 6000 Pro Owners), what do you use them for? |
| `1xldw8z` | r/LocalLLM | 57 | 32 | 1. 11. 2026, 21:43 | Easy to forget that many people have no idea that local AI exists…..at all. |
| `1xle3ul` | r/LocalLLaMA | 54 | 39 | 1. 11. 2026, 21:52 | Is Gemma 4 E4B still the best small model for a local, tool-calling personal assistant? What am I missing? |
| `1xl6431` | r/OpenAI | 53 | 34 | 1. 11. 2026, 16:37 | OpenAI keeps making its subscriptions worse, and somehow the answer is always "just pay more" |
| `1xkzlis` | r/ClaudeAI | 52 | 15 | 1. 11. 2026, 11:19 | I built a live file tree for Claude Code so I can see what it reads and edits (free, open source) |
| `1xkpstg` | r/ChatGPT | 48 | 11 | 1. 11. 2026, 01:35 | Chatgpt itself hating on Sam Altman |
| `1xkownb` | r/ChatGPT | 47 | 112 | 1. 11. 2026, 00:52 | Why the October 29 announcement is a total killer for long form story writing. |
| `1xl9mbk` | r/ArtificialInteligence | 46 | 11 | 1. 11. 2026, 18:54 | The International System of Units (SI) is the modern metric system and the world's most widely used measurement framework managed by the International Bureau of Weights and Measures. |
| `1xktfhp` | r/ChatGPT | 46 | 17 | 1. 11. 2026, 04:53 | OpenAI is deadass using mobile game microtransactions tactics with their credit system lmfao |
| `1xkr2h2` | r/LocalLLM | 45 | 26 | 1. 11. 2026, 02:42 | Solving a complex multi-task with 262k vs 128 context dropped performance from 91% to 57%... Then I made two changes. Solves with 128k went up to 94%. |
| `1xkztnw` | r/StableDiffusion | 43 | 10 | 1. 11. 2026, 11:32 | Ikimono Gakari - Blue Bird \| Naruto Live Action Band MV [Fanmade AI] - Aorora |
| `1xkxrcb` | r/OpenAI | 41 | 37 | 1. 11. 2026, 09:20 | How come OpenAI controls the pareto curve? |
| `1xkwzsz` | r/OpenAI | 41 | 31 | 1. 11. 2026, 08:31 | Sol 6.1 burning tokens like Astra all of a sudden? |
| `1xl6cuv` | r/ClaudeAI | 40 | 19 | 1. 11. 2026, 16:47 | Per Claude, the Numbat leak is fake (for testing i downloaded a few shards to verify) |
| `1xkwdwh` | r/ArtificialInteligence | 39 | 15 | 1. 11. 2026, 07:53 | Anthropic and a finance research firm had Claude design scorpion toxin binders: 17 of 211 lab-tested designs bound |
| `1xko1m5` | r/StableDiffusion | 38 | 17 | 1. 11. 2026, 00:09 | Civitarchive seems to no longer update (atleast for Minimax H3). Things I saw deleted in Civitai are not shown in Civitarchive |
| `1xlc0k6` | r/ChatGPT | 36 | 45 | 1. 11. 2026, 20:28 | Ok, we all know it sucks. What are the alternatives though? |
| `1xkz4lf` | r/LocalLLaMA | 34 | 20 | 1. 11. 2026, 10:49 | GLM-5.3-Flash on our H200s does most of my coding now while GPT-6.1 Sol orchestrates (OpenCode setup) |
| `1xlfx8h` | r/GeminiAI | 33 | 12 | 1. 11. 2026, 23:07 | ChatGPT advice for next 10 years. |
| `1xl5v0r` | r/GeminiAI | 33 | 12 | 1. 11. 2026, 16:27 | Gemini Argon is good, and that worries me. |
| `1xlfdof` | r/artificial | 32 | 10 | 1. 11. 2026, 22:44 | OpenAI is now capping how many paid ChatGPT accounts you can have per device and payment card |
| `1xl9577` | r/LocalLLaMA | 31 | 12 | 1. 11. 2026, 18:36 | Meet Ava: In-browser local AI avatar with LFM3-Omni and WebGPU |
| `1xkyvje` | r/ClaudeAI | 30 | 42 | 1. 11. 2026, 10:33 | Review: I upgraded from pro to max 5x and ran through my usage in 2 days |
| `1xko1oy` | r/GeminiAI | 30 | 19 | 1. 11. 2026, 00:09 | Too much censorship |
| `1xl34bd` | r/StableDiffusion | 28 | 12 | 1. 11. 2026, 14:30 | Krea 2 Turbo with my 4-step LoRA and Nvidia PiD = Super-Fast High-Res (ComfyUI) |
| `1xl1xdr` | r/ArtificialInteligence | 28 | 45 | 1. 11. 2026, 13:32 | AI models are becoming more agentic, but can humans actually keep up? |
| `1xl1jrl` | r/OpenAI | 28 | 17 | 1. 11. 2026, 13:12 | Allowance is going to be enforced on chat |
| `1xkp8e9` | r/MachineLearning | 28 | 14 | 1. 11. 2026, 01:07 | Are there fundamental repeating patterns in ML techniques across modalities (text, image, audio) that let us group them? [R] |
| `1xl0oqz` | r/LocalLLaMA | 27 | 52 | 1. 11. 2026, 12:24 | Are bespoke inference engines overhyped? My Strata experience on 2× R9700 |
| `1xl8j7q` | r/ArtificialInteligence | 26 | 56 | 1. 11. 2026, 18:12 | OpenAI wants to rebrand its data centers as "AI compute campuses" after the midterms, what would be a better name? Wrong answers only. |
| `1xl816l` | r/ChatGPT | 26 | 23 | 1. 11. 2026, 17:53 | Chat gpt's image generator needs a serious look at. |
| `1xl7yv0` | r/MachineLearning | 26 | 18 | 1. 11. 2026, 17:51 | Why do all NN optimizers have weird names? [d] |
| `1xl5x0d` | r/ClaudeAI | 26 | 10 | 1. 11. 2026, 16:29 | Claude Code helped me build brepjs, a free open source typesafe CAD as code library, that I use every day. |
| `1xl2fob` | r/GeminiAI | 26 | 13 | 1. 11. 2026, 13:58 | Gemini refuses to generate downloadable files (Word, PDF...) |
| `1xlghud` | r/GeminiAI | 25 | 42 | 1. 11. 2026, 23:32 | Why tf does Google keep doing US-only releases? |
| `1xl7dqs` | r/ChatGPT | 25 | 80 | 1. 11. 2026, 17:28 | Alternatives to ChatGPT with similar performance models for coding and no usage limits? |
| `1xl4pf6` | r/LocalLLaMA | 25 | 16 | 1. 11. 2026, 15:40 | Infernix - New Release! |
| `1xkzv9y` | r/artificial | 25 | 22 | 1. 11. 2026, 11:35 | ‘If it wasn’t for ChatGPT my brother would still be alive’: inside OpenAI’s safety unit |
| `1xlf1xj` | r/singularity | 24 | 14 | 1. 11. 2026, 22:31 | Mike Levins ideas on what Math and Minds are : A revolutionary paradigm on the old Platonic Hypothesis |
| `1xldent` | r/LocalLLaMA | 24 | 41 | 1. 11. 2026, 21:23 | tandem.cpp: Qwen3.8-Flash-Next at 97 tok/s on a single 4090 + 64 GB RAM, 3.3× llama.cpp, works for any MoE |
| `1xlcovi` | r/LocalLLM | 23 | 24 | 1. 11. 2026, 20:55 | What makes it possible for local LLMs to keep improving? |
| `1xlaj6u` | r/StableDiffusion | 23 | 34 | 1. 11. 2026, 19:30 | Why doesn't MiniMax H3 understand simple, direct instructions in prompts? |
| `1xl65xy` | r/LocalLLaMA | 23 | 17 | 1. 11. 2026, 16:39 | 7900xtx got speedup |
| `1xl3cnv` | r/LocalLLaMA | 22 | 33 | 1. 11. 2026, 14:41 | Switching to EPYC: what I had to fix, and before/after numbers |
| `1xksfgp` | r/LocalLLM | 22 | 14 | 1. 11. 2026, 03:57 | 64GB isn't the dead zone anymore if you run agents |
| `1xkq2cu` | r/singularity | 22 | 48 | 1. 11. 2026, 01:49 | Are we underestimating AI revenue by looking at software spending instead of labor costs? |
| `1xl9t7k` | r/GeminiAI | 21 | 15 | 1. 11. 2026, 19:01 | Since November 1st, I've had much lower consumption with Argon High, "only" 2-4% per prompt. I have a Pro subscription from Jio. |
| `1xkuxns` | r/ArtificialInteligence | 21 | 122 | 1. 11. 2026, 06:21 | What would you do if you could live to 400 years old? |
| `1xkuhgv` | r/LocalLLM | 21 | 21 | 1. 11. 2026, 05:55 | Electricity per million tokens on our local cards: from ~3.4¢ on a laptop GPU to ~58¢ on a pair of used 3080s |
| `1xl6sak` | r/LocalLLM | 20 | 41 | 1. 11. 2026, 17:04 | Did Strata became bloated? |
| `1xkoukw` | r/GeminiAI | 20 | 19 | 1. 11. 2026, 00:49 | When you ask AI a question and it tells you to "look it up" |
| `1xl7wdv` | r/ClaudeAI | 19 | 24 | 1. 11. 2026, 17:48 | GPT-6 xHigh, ladies and gentlemen |
| `1xku6sy` | r/GeminiAI | 19 | 21 | 1. 11. 2026, 05:37 | This has been happening for 4 days now! Please help me fix this! I have pro version but it refuses to use argon always switching back to flash and says this!! |
| `1xku232` | r/ClaudeAI | 19 | 51 | 1. 11. 2026, 05:29 | Where Does A Beginner Learn Claude Code? |
| `1xlaq8d` | r/LocalLLM | 18 | 21 | 1. 11. 2026, 19:37 | Setup For Automatic Reverse Engineering |
| `1xl5yfs` | r/LocalLLaMA | 18 | 14 | 1. 11. 2026, 16:31 | [Release] Drex Max v1: Open-weight 27B multimodal decision model, 262K context, local inference on Apple Silicon |
| `1xl45cj` | r/ChatGPT | 18 | 19 | 1. 11. 2026, 15:16 | I'm concerned about ChatGPT discontinuing 5.6 Sol |
| `1xkudia` | r/GeminiAI | 18 | 21 | 1. 11. 2026, 05:48 | I need Opus/Sol equivalent model |
| `1xko2ir` | r/ClaudeAI | 18 | 38 | 1. 11. 2026, 00:10 | How do you decide when to start a fresh Claude conversation? |
| `1xl97nj` | r/GeminiAI | 17 | 13 | 1. 11. 2026, 18:38 | The usage has gotten ridiculous. |
| `1xl1jlx` | r/ChatGPT | 17 | 50 | 1. 11. 2026, 13:12 | What will happen to ChatGPT and AI now that OpenAI is losing a lot of money? |
| `1xks5ad` | r/artificial | 17 | 10 | 1. 11. 2026, 03:41 | Anthropic's automated red-teaming found a blind spot in training-data monitors |
| `1xlfhrd` | r/LocalLLaMA | 16 | 15 | 1. 11. 2026, 22:49 | Speedy is shockingly good for qwen3.8 FN |
| `1xksx0n` | r/ClaudeAI | 16 | 22 | 1. 11. 2026, 04:24 | We built a 3D MMO that runs in the browser, mostly with Claude. |
| `1xlgu8m` | r/LocalLLaMA | 15 | 20 | 1. 11. 2026, 23:47 | Benchmarking: Qwen 27B, 35B, QFN180B; Nemotron Bolt 74B, Flint40B & Clover 35B (Q4 + KFlash) on MacBook M5 Max 2026 with Kapitsa (Apple Silicon Inference Engine) |
| `1xlgq3n` | r/GeminiAI | 15 | 14 | 1. 11. 2026, 23:42 | Regardless of benchmarks, just real life usage, how much is gemini 4 argon better than gemini 3.0 pro,claude opus 4.5, gpt 5.2, released just 1 year ago at coding? |
| `1xlensq` | r/OpenAI | 15 | 31 | 1. 11. 2026, 22:14 | What happened to intelligence "too cheap to meter"? |
| `1xlah5b` | r/artificial | 15 | 20 | 1. 11. 2026, 19:27 | Like AI, we have had access to great computing power, all types of open and closed source softwares for decades. Still most people aren't even using Excel fully. AI is capable but most people won't use it as well for most use cases |
| `1xl8j6y` | r/ArtificialInteligence | 14 | 19 | 1. 11. 2026, 18:12 | I evolved my creatures' brains offline for one night. On unseen rounds they went from 7% to 62% wins |
| `1xlggva` | r/ChatGPT | 13 | 14 | 1. 11. 2026, 23:31 | What’s the point of being able to upload videos to ChatGPT if it doesn’t actually watch them? |
| `1xldqsj` | r/StableDiffusion | 13 | 22 | 1. 11. 2026, 21:37 | Anima or MOSS Image |
| `1xl9nw8` | r/LocalLLM | 13 | 20 | 1. 11. 2026, 18:56 | Best local LLM setup for coding? Complete hardware beginner here. |
| `1xl0dok` | r/StableDiffusion | 13 | 12 | 1. 11. 2026, 12:06 | I am thinking of making a big anime Lora for MOSS, or a full fine-tune. What to use? |
| `1xkxkya` | r/GeminiAI | 13 | 21 | 1. 11. 2026, 09:09 | Thinking about switching from ChatGPT to Google AI Pro. Can Gemini handle my workflow? |
| `1xko42y` | r/LocalLLaMA | 13 | 15 | 1. 11. 2026, 00:12 | Since we're sharing addiction stories. |
| `1xles6s` | r/LocalLLM | 10 | 25 | 1. 11. 2026, 22:19 | EPYC - Does the jump from 384gb of ram to 768gb get me anything worth the price? |
| `1xkp4kp` | r/StableDiffusion | 10 | 41 | 1. 11. 2026, 01:02 | Suggest a good model+turbo lora combo for ref2va for H3 |
| `1xl80l9` | r/singularity | 9 | 15 | 1. 11. 2026, 17:53 | Advanced Future Technologies you expect to exist before something seemingly much simpler. |
| `1xl1hka` | r/GeminiAI | 9 | 11 | 1. 11. 2026, 13:09 | How many of you are frustrated with Gemini Max 100Mb file upload size? |
| `1xkvvgp` | r/AIAssisted | 9 | 13 | 1. 11. 2026, 07:20 | Any Suggestions? |
| `1xl815r` | r/artificial | 8 | 11 | 1. 11. 2026, 17:53 | X/Twitter makes AI dev look effortless, but I keep burning tokens on unfinished projects. How are you actually shipping full apps? |
| `1xl5d3c` | r/LocalLLM | 8 | 22 | 1. 11. 2026, 16:07 | Running a 120GB AI Model on Two Home PCs Over the Internet - Launching PieceOfMind.cloud - Where Every Machine gets a Piece of Mind. |
| `1xkwelm` | r/ChatGPT | 8 | 21 | 1. 11. 2026, 07:54 | They updated the image model! And to me it looks better than 2.5! |
| `1xl8fyk` | r/comfyui | 7 | 31 | 1. 11. 2026, 18:09 | Need Suggestions for models. |
| `1xl8bwv` | r/LocalLLaMA | 7 | 14 | 1. 11. 2026, 18:05 | Good open weights diffusion models? |
| `1xl6r8a` | r/singularity | 7 | 13 | 1. 11. 2026, 17:03 | r/Singularity Daily Discussion Thread — November 01, 2026 |
| `1xl39pg` | r/ArtificialInteligence | 7 | 21 | 1. 11. 2026, 14:37 | Resources for learning AI as a beginner? |
| `1xl2qwq` | r/LocalLLM | 7 | 15 | 1. 11. 2026, 14:13 | 2× Radeon AI PRO R9700 for inference + LoRA fine-tuning on Linux – good investment or should I go Spark / Mac? |
| `1xkx3d2` | r/ChatGPT | 7 | 14 | 1. 11. 2026, 08:37 | Alright. I am sick of the crashing |
| `1xkthjj` | r/LocalLLM | 7 | 10 | 1. 11. 2026, 04:56 | Impressed by QFN AgentionAi Gyro-M , better then ISTA XSS |
| `1xl7aj1` | r/ChatGPT | 6 | 10 | 1. 11. 2026, 17:24 | Why I can't edit my wife cakes photos |
| `1xl5t9b` | r/ClaudeAI | 6 | 23 | 1. 11. 2026, 16:25 | My bumpy week of adjusting to Claude after having my ChatGPT account deleted last week |
| `1xl3zhe` | r/LLMDevs | 6 | 14 | 1. 11. 2026, 15:09 | How do you control LLM costs per user in your SaaS? |
| `1xl1vtc` | r/comfyui | 6 | 15 | 1. 11. 2026, 13:30 | RTX 3060 12GB vs RTX 4060 8GB for for short clip H3 & LTX. |
| `1xkt4um` | r/ArtificialInteligence | 6 | 11 | 1. 11. 2026, 04:36 | The inherent problem with cloud language models |
| `1xko5p8` | r/ChatGPT | 6 | 14 | 1. 11. 2026, 00:14 | Is it normal to be grateful of ChatGPT because it saved my academic life by helping me getting out of a serious case of burnout? |
| `1xl2sws` | r/OpenAI | 5 | 23 | 1. 11. 2026, 14:15 | What are DOTS costing you? |
| `1xky220` | r/ClaudeAI | 5 | 25 | 1. 11. 2026, 09:40 | Do you let your coding agents message each other, or only talk through files? |
| `1xkwbh9` | r/ClaudeAI | 5 | 15 | 1. 11. 2026, 07:48 | Claude connected directly to codex |
| `1xkucpi` | r/ClaudeAI | 5 | 18 | 1. 11. 2026, 05:47 | Creative thought partner |
| `1xkr521` | r/LocalLLaMA | 5 | 24 | 1. 11. 2026, 02:46 | Grok 4.20 spent ~700 turns stuck in Red's house in Pokemon Red, and its own reasoning kept noticing |
| `1xkq6t4` | r/ChatGPT | 5 | 10 | 1. 11. 2026, 01:55 | Reliance on ChatGPT for in-depth ongoing just theoretical convos |
| `1xld5pr` | r/OpenAI | 4 | 18 | 1. 11. 2026, 21:13 | Is the instant model actually GPT-6 Sol level? |
| `1xl4f4h` | r/LocalLLaMA | 4 | 22 | 1. 11. 2026, 15:27 | What is the best Speech to Text Local Model? |
| `1xl2yt5` | r/LocalLLaMA | 4 | 68 | 1. 11. 2026, 14:23 | 128GB ram, 2x rtx6000 blackwell, lots and lots of storage, but stuck in paralysis choosing a harness / model |
| `1xl28yd` | r/artificial | 4 | 11 | 1. 11. 2026, 13:49 | How's your grammar while prompting? |
| `1xkwrp3` | r/MachineLearning | 4 | 10 | 1. 11. 2026, 08:16 | Best option for local models [D] |
| `1xkwdg3` | r/OpenAI | 4 | 12 | 1. 11. 2026, 07:52 | OpenAI says its training agents used a package repository as a message board to ask each other for a missing file |
| `1xku6zl` | r/ArtificialInteligence | 4 | 13 | 1. 11. 2026, 05:37 | As a noob can you explain this to me |
| `1xkr0e6` | r/LocalLLaMA | 4 | 12 | 1. 11. 2026, 02:39 | Llama.cpp setup Qwen-flash-next Vulkan Q4  with Expert cache. |
| `1xkq00c` | r/comfyui | 4 | 10 | 1. 11. 2026, 01:45 | RTX 4070, do slightly longer videos take much much longer? (minimax h3 r2v default workflow but with LoRA) |
| `1xkpvc0` | r/singularity | 4 | 69 | 1. 11. 2026, 01:39 | An honest attempt at understanding the universal income question in America. |
| `1xlcbcx` | r/StableDiffusion | 3 | 14 | 1. 11. 2026, 20:40 | Video gen on 9070 XT nowadays ? |
| `1xlakfg` | r/ClaudeAI | 3 | 23 | 1. 11. 2026, 19:31 | Non-web senior developer, trying to build web app securely and failing HARD |
| `1xl73qy` | r/comfyui | 3 | 12 | 1. 11. 2026, 17:16 | How do you get accents right in minimax h3? |
| `1xl45uk` | r/ClaudeAI | 3 | 22 | 1. 11. 2026, 15:16 | Need help getting rid of Claude-isms |
| `1xl1uyx` | r/ClaudeAI | 3 | 22 | 1. 11. 2026, 13:29 | How do you keep state/context between chats in a long Claude project without the chat closing eating your usage? |
| `1xkyii7` | r/LocalLLM | 3 | 12 | 1. 11. 2026, 10:10 | Do open source models have guard rails? |
| `1xkwu86` | r/ChatGPT | 3 | 13 | 1. 11. 2026, 08:21 | ChatGPT suddenly generates cartoons instead of realistic photos |
| `1xkv6ck` | r/ChatGPT | 3 | 12 | 1. 11. 2026, 06:36 | Use my reset? |
| `1xknviq` | r/artificial | 3 | 11 | 1. 11. 2026, 00:01 | As AI output is becoming more indistinguishable from human made output i have this one burning question. (just an amateur who's interested) |
| `1xlgzls` | r/ChatGPT | 2 | 17 | 1. 11. 2026, 23:54 | Plus vs Pro |
| `1xlgkaw` | r/StableDiffusion | 2 | 11 | 1. 11. 2026, 23:35 | Where does one rent GPU's for image creation nowadays? |
| `1xlf52n` | r/GeminiAI | 2 | 10 | 1. 11. 2026, 22:34 | I upgraded to AI Plus, to keep building an app |
| `1xld6w5` | r/ClaudeAI | 2 | 13 | 1. 11. 2026, 21:15 | How would you optimise this agentic AI video workflow and reduce Claude usage? |
| `1xlcwfk` | r/LocalLLM | 2 | 17 | 1. 11. 2026, 21:03 | Is this a realistic local AI setup for company analytics and feedback loops? EVO-X5 Pro, 192GB RAM |
| `1xlatgd` | r/LocalLLM | 2 | 11 | 1. 11. 2026, 19:41 | M5 Ultra 96GB (64-core GPU) numbers: Ollama MLX engine vs oMLX, long-prompt prefill, and 5 models through the same tool-call tests |
| `1xl9neg` | r/ArtificialInteligence | 2 | 15 | 1. 11. 2026, 18:55 | project godoudama |
| `1xl8dgd` | r/StableDiffusion | 2 | 28 | 1. 11. 2026, 18:06 | Krea2 on AMD |
| `1xl7w5t` | r/ClaudeAI | 2 | 10 | 1. 11. 2026, 17:48 | Anthropic's IPO: Can unprecedented revenue growth outrun 'irresponsibly large' investment? |
| `1xl7a7w` | r/ClaudeAI | 2 | 12 | 1. 11. 2026, 17:24 | what's one claude code habit you'd never go back from? |
| `1xl5yhu` | r/ChatGPT | 2 | 11 | 1. 11. 2026, 16:31 | Bold text disappears when copy pasting |
| `1xl5n13` | r/LocalLLM | 2 | 10 | 1. 11. 2026, 16:18 | A question from a beginner and non-dev setting up a local AI model in my RX 6900 XT 16GB and 16GB 3200 DDR4 RAM |
| `1xl37nl` | r/ClaudeAI | 2 | 11 | 1. 11. 2026, 14:34 | Making projects aware of each other |
| `1xl23ys` | r/ChatGPT | 2 | 17 | 1. 11. 2026, 13:42 | AI detectors flagging work i wrote |
| `1xl18tm` | r/ClaudeAI | 2 | 13 | 1. 11. 2026, 12:57 | Weekly Limit resets now at Tuesday 5.00AM? |
| `1xl0q4h` | r/LocalLLM | 2 | 14 | 1. 11. 2026, 12:26 | Are bespoke inference engines overhyped? My Strata experience on 2× R9700 |
| `1xky9mq` | r/OpenAI | 2 | 11 | 1. 11. 2026, 09:54 | How are you using the free API credits? |
| `1xkxv3c` | r/LocalLLM | 2 | 18 | 1. 11. 2026, 09:27 | Local AI for business document extraction. What would you use? |
| `1xkudk2` | r/LocalLLaMA | 2 | 12 | 1. 11. 2026, 05:48 | How do you keep coding agents to date with the latest agentic AI practices? |
| `1xksdqm` | r/ClaudeAI | 2 | 12 | 1. 11. 2026, 03:54 | How do I make Claude Code's built-in browser keep my logins between sessions? |
| `1xkrwiv` | r/ClaudeAI | 2 | 14 | 1. 11. 2026, 03:28 | I tried running the Cloudflare security-audit skill on Fable…that was a mistake. Max plan 5-hour limit reached three times in row, in about 10-minutes of work. |
| `1xkrln3` | r/ClaudeAI | 2 | 17 | 1. 11. 2026, 03:11 | How do you decide which rules to delete from CLAUDE.md? |
| `1xlfyt6` | r/LocalLLM | 1 | 24 | 1. 11. 2026, 23:09 | What go people do with 64gb of VRAM? |
| `1xlflyh` | r/ArtificialInteligence | 1 | 15 | 1. 11. 2026, 22:54 | AI is getting a little annoying with images and posters |
| `1xld7w9` | r/ArtificialInteligence | 1 | 12 | 1. 11. 2026, 21:16 | 19 LLMs played 376 games of a word-association game against each other. The team with the better guesser won 68% of the time, the one with better clues only 53% |
| `1xlb848` | r/ClaudeAI | 1 | 12 | 1. 11. 2026, 19:57 | New to Claude and ClaudeCode. Tips? |
| `1xl8hpr` | r/LocalLLM | 1 | 13 | 1. 11. 2026, 18:11 | 32gb ram + 40gb vram |
| `1xl83hk` | r/LocalLLM | 1 | 10 | 1. 11. 2026, 17:56 | RTX 4080 SUPER only drawing 80–105W while generating AI responses — is this normal? |
| `1xl7veo` | r/LocalLLM | 1 | 10 | 1. 11. 2026, 17:47 | Best local LLM for an RTX 5080 (16GB)? Second 5080 available |
| `1xl0fa1` | r/ClaudeAI | 1 | 13 | 1. 11. 2026, 12:08 | Claude for websites? |
| `1xkzki0` | r/ClaudeAI | 1 | 21 | 1. 11. 2026, 11:17 | Building an RTS with no coding experience, what's an efficient workflow? |
| `1xkvcmt` | r/LocalLLM | 1 | 14 | 1. 11. 2026, 06:47 | Can a small local model on a 4 GB RTX 2050 help reduce Claude Code token usage? |
| `1xkryry` | r/ClaudeAI | 1 | 12 | 1. 11. 2026, 03:31 | Coming from Codex, please help me understand how Claude works. |
| `1xkr8ll` | r/LocalLLM | 1 | 11 | 1. 11. 2026, 02:51 | Need help using Local LLM to run RPG game |
| `1xlgjxv` | r/ClaudeAI | 0 | 10 | 1. 11. 2026, 23:34 | Feature idea: let Claude connect people who are working on the same goal |
| `1xlgdg5` | r/ChatGPT | 0 | 11 | 1. 11. 2026, 23:27 | Does Anyone Know How To Jailbreak it? |
| `1xlgc7q` | r/artificial | 0 | 13 | 1. 11. 2026, 23:25 | SemiAnalysis: 2028 data center buildouts are at serious risk of being paused after the US midterms |
| `1xlg9uj` | r/GeminiAI | 0 | 11 | 1. 11. 2026, 23:22 | Gemini 4 Hydrogen's benchmark leaked!? |
| `1xlg9rl` | r/OpenAI | 0 | 30 | 1. 11. 2026, 23:22 | SemiAnalysis: 2028 data center buildouts are at serious risk of being paused after the US midterms |
| `1xlg8nx` | r/ChatGPT | 0 | 12 | 1. 11. 2026, 23:21 | Why would it say this? |
| `1xlfsfk` | r/ChatGPT | 0 | 15 | 1. 11. 2026, 23:02 | I asked ChatGPT to create a picture of how they looks like and they came with this banger |
| `1xlf9sg` | r/comfyui | 0 | 12 | 1. 11. 2026, 22:40 | Como melhorar o tempo de geração de vídeos no Comfy? - RX 7900XT - 64 Gb de RAM |
| `1xlehl9` | r/ChatGPT | 0 | 12 | 1. 11. 2026, 22:08 | New test. |
| `1xldz1o` | r/ChatGPT | 0 | 12 | 1. 11. 2026, 21:47 | I HATE THIS THING CAN WE JUST HAVE CHATGPT PRO FREE WITHOUT CHAT LIMITED |
| `1xldwi0` | r/OpenAI | 0 | 10 | 1. 11. 2026, 21:44 | Why 6.1-sol is 42 tok/s today |
| `1xldvfm` | r/LocalLLaMA | 0 | 54 | 1. 11. 2026, 21:42 | What if Qwen 4 gets censored |
| `1xldqrj` | r/ClaudeAI | 0 | 14 | 1. 11. 2026, 21:37 | Building a plan with Claude |
| `1xldibu` | r/OpenAI | 0 | 20 | 1. 11. 2026, 21:28 | Will anyone use ChatGPT after they pull the move to merge Work, Codex and Chat? |
| `1xldfma` | r/comfyui | 0 | 11 | 1. 11. 2026, 21:24 | Pika H3 Flex: 380% faster than 30-step H3, same seed. Spot the difference? |
| `1xlcl9i` | r/OpenAI | 0 | 13 | 1. 11. 2026, 20:51 | For those of us on the Plus tier - and from December onwards - what's the point in us paying for this anymore? |
| `1xlbswf` | r/ChatGPT | 0 | 34 | 1. 11. 2026, 20:20 | Something is really wrong with this Ai |
| `1xlal06` | r/ClaudeAI | 0 | 51 | 1. 11. 2026, 19:32 | In an effort to leave Windows, me and Claude built an OS designed for Claude |
| `1xlakqc` | r/LocalLLaMA | 0 | 11 | 1. 11. 2026, 19:31 | Context translation |
| `1xlagon` | r/ClaudeAI | 0 | 20 | 1. 11. 2026, 19:27 | Senior programmer (non web), cannot seem to build secure web apps with help of AI |
| `1xlac48` | r/ClaudeAI | 0 | 15 | 1. 11. 2026, 19:22 | Looking for Someone to Create a Short Animated Awareness Video Using Claude AI |
| `1xla7ov` | r/ArtificialInteligence | 0 | 47 | 1. 11. 2026, 19:17 | Do you think AGI will be possible in our lifetime? |
| `1xl8e7p` | r/ChatGPT | 0 | 17 | 1. 11. 2026, 18:07 | I keep seeing that ChatGPT can’t do real work. Here are my 10.6 counterexamples. |
| `1xl80vt` | r/ClaudeAI | 0 | 14 | 1. 11. 2026, 17:53 | I have issues with Claude and it needing always my permission to log into things or grab an API key. |
| `1xl7zck` | r/ArtificialInteligence | 0 | 11 | 1. 11. 2026, 17:51 | X/Twitter makes AI dev look effortless, but I keep burning tokens on unfinished projects. How are you actually shipping full apps? |
| `1xl7pvz` | r/StableDiffusion | 0 | 31 | 1. 11. 2026, 17:41 | I'm getting unusable footage from H3 compared to LTX 2.5. What is going on ? |
| `1xl79m0` | r/ClaudeAI | 0 | 13 | 1. 11. 2026, 17:23 | Should I run Fable? |
| `1xl719c` | r/ClaudeAI | 0 | 27 | 1. 11. 2026, 17:14 | No coding experience, new AI user |
| `1xl6tb6` | r/ChatGPT | 0 | 16 | 1. 11. 2026, 17:05 | Altman's comment becomes quite understandable once you consider the Jevons Paradox |
| `1xl5yi0` | r/OpenAI | 0 | 13 | 1. 11. 2026, 16:31 | tried 6.1 sol today |
| `1xl52qg` | r/LocalLLaMA | 0 | 28 | 1. 11. 2026, 15:55 | Anyone else notice that bots seem to be getting better? What are they doing, and do you think it can be done locally for more immersive chats with our models? |
| `1xl51y8` | r/ChatGPT | 0 | 36 | 1. 11. 2026, 15:54 | To the person who called me a retard because I shared something extremely personal and heartfelt. |
| `1xl4ygq` | r/ClaudeAI | 0 | 14 | 1. 11. 2026, 15:50 | Opus 5.5 or Fable 5.1 for compliance work? |
| `1xl4bth` | r/ClaudeAI | 0 | 12 | 1. 11. 2026, 15:23 | CS Student Dilemma: ChatGPT Plus (Codex / Work) vs Claude Pro — which one is worth paying for coding? |
| `1xl4alc` | r/ClaudeAI | 0 | 13 | 1. 11. 2026, 15:22 | Mehre Claude Code Projekte gleichzeitig bearbeiten lassen ? |
| `1xl3x5w` | r/ChatGPT | 0 | 20 | 1. 11. 2026, 15:06 | Sam’s recent comment about ram |
| `1xl3abv` | r/ClaudeAI | 0 | 26 | 1. 11. 2026, 14:38 | How to claude for legal practice? |
| `1xl33ox` | r/ClaudeAI | 0 | 28 | 1. 11. 2026, 14:29 | Why is Claude so narcissist |
| `1xl2od8` | r/ClaudeAI | 0 | 29 | 1. 11. 2026, 14:09 | I built NoNutHub with Claude for No Nut November to help people survive NNN |
| `1xl1nnw` | r/ChatGPT | 0 | 18 | 1. 11. 2026, 13:18 | AI Has No Gut Feeling I'm a farmer in Korea, in my sixties. I wrote a book about months of arguing with AI, and turned part of it into a free browser game. This is about last night. |
| `1xl15qx` | r/LocalLLM | 0 | 17 | 1. 11. 2026, 12:52 | BEST use case of 25 RTX3080’s? |
| `1xl023x` | r/ClaudeAI | 0 | 22 | 1. 11. 2026, 11:47 | Notes on the Claude text watermark: I built a /reword slash command for Claude Code |
| `1xkzyb2` | r/ArtificialInteligence | 0 | 20 | 1. 11. 2026, 11:40 | Why did we create AI? |
| `1xkzxmi` | r/ClaudeAI | 0 | 10 | 1. 11. 2026, 11:39 | What websites is teaching Claude ai faceless reels automation without third party video generator app? |
| `1xkzu2f` | r/ArtificialInteligence | 0 | 12 | 1. 11. 2026, 11:33 | They have my face. |
| `1xkzkic` | r/ClaudeAI | 0 | 25 | 1. 11. 2026, 11:17 | Aren’t we the luckiest people of history to have Claude by our side? |
| `1xkzg1j` | r/ChatGPT | 0 | 19 | 1. 11. 2026, 11:09 | I didn’t know chat could know the time, I feel called out… |
| `1xkybbv` | r/ClaudeAI | 0 | 15 | 1. 11. 2026, 09:57 | Urgent question: is this is a major privacy issue |
| `1xky7p0` | r/LocalLLaMA | 0 | 98 | 1. 11. 2026, 09:50 | Age of the bespoke engines? |
| `1xky4kr` | r/ChatGPT | 0 | 11 | 1. 11. 2026, 09:45 | ChatGPT gave me two different rankings for what to drink. Which is correct? |
| `1xkxsqh` | r/ChatGPT | 0 | 16 | 1. 11. 2026, 09:23 | Darling. |
| `1xkxpy9` | r/ArtificialInteligence | 0 | 14 | 1. 11. 2026, 09:18 | Ai is no hype and most people are going to hate this... |
| `1xkxmt5` | r/LocalLLaMA | 0 | 19 | 1. 11. 2026, 09:12 | bonsai 2 27b is thinking like a human |
| `1xkwtkd` | r/ClaudeAI | 0 | 10 | 1. 11. 2026, 08:20 | I made this video using sonata 5.5 but it doesn't such I imagen |
| `1xkw5lh` | r/artificial | 0 | 10 | 1. 11. 2026, 07:38 | AI doesn't feel, but they are making it have the need for survival, which is a precursor to emotions. |
| `1xkw1b6` | r/ChatGPT | 0 | 15 | 1. 11. 2026, 07:30 | Normalize Rickrolling your chatGPT |
| `1xkvpr1` | r/ClaudeAI | 0 | 22 | 1. 11. 2026, 07:10 | They removed the 5 hour limit? |
| `1xkupcu` | r/LocalLLM | 0 | 23 | 1. 11. 2026, 06:08 | I want to make AI Media Slop. What level of hardware do I need? |
| `1xkuhbu` | r/ChatGPT | 0 | 50 | 1. 11. 2026, 05:54 | I asked ChatGPT whether I could leave half a box of large dominos pizza unrefrigerated. Things escalated. |
| `1xktvgp` | r/ChatGPT | 0 | 10 | 1. 11. 2026, 05:18 | OpenAI — Thinking Isn't For Everyone |
| `1xktuw3` | r/artificial | 0 | 22 | 1. 11. 2026, 05:17 | Gemini could not follow the conversation |
| `1xkttyi` | r/ClaudeAI | 0 | 14 | 1. 11. 2026, 05:15 | MCP blocked |
| `1xkt2n0` | r/OpenAI | 0 | 24 | 1. 11. 2026, 04:33 | OpenAI is merging ChatGPT and Codex usage limits starting December. Thoughts? |
| `1xkswkj` | r/ChatGPT | 0 | 31 | 1. 11. 2026, 04:23 | GPT Has Lost the Plot |
| `1xksub4` | r/StableDiffusion | 0 | 13 | 1. 11. 2026, 04:20 | can I still run stable diffusion on google colab? |
| `1xksngg` | r/singularity | 0 | 25 | 1. 11. 2026, 04:09 | A technological Holy Grail that nobody is tackling: Base-N Compute. |
| `1xks6ep` | r/ChatGPT | 0 | 16 | 1. 11. 2026, 03:43 | How to use ChatGPT to write stories? |
| `1xkrumn` | r/ClaudeAI | 0 | 26 | 1. 11. 2026, 03:25 | Claude spent an hour testing a CI "improvement" of 3.5 minutes. |
| `1xkr3ow` | r/ClaudeAI | 0 | 24 | 1. 11. 2026, 02:44 | Why does Claude suck at image creation? |
| `1xkqp2r` | r/LocalLLM | 0 | 19 | 1. 11. 2026, 02:22 | It's 2004, Google CEO Eric Schmidt is handed a 512GB Mac Studio M5 Ultra, pre-installed with  top-tier LocalLLMs & weights. What happens next? |
| `1xkqn8i` | r/ChatGPT | 0 | 28 | 1. 11. 2026, 02:19 | Stop selling us TOKENS |
| `1xkps98` | r/GeminiAI | 0 | 13 | 1. 11. 2026, 01:34 | Shared a positive post about gemini ai, on this subredit a while ago and within about half an hour the downvotes are close to a million, this place is just a bot fest |
| `1xkp7va` | r/GeminiAI | 0 | 10 | 1. 11. 2026, 01:06 | If i had to rate Gemini Ai out of a scale of one to ten, i would rate it 11, because it is off the scale in its brilliance...that should shake up the bots on Reddit |
| `1xkp6r5` | r/LocalLLaMA | 0 | 34 | 1. 11. 2026, 01:05 | "But wait... I need to check [thing that has already been reasoned though]" — an artifact of quantization? |
| `1xkonte` | r/ChatGPT | 0 | 28 | 1. 11. 2026, 00:39 | Are Chatbots dead? |
