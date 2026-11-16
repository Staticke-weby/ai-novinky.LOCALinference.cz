# AI souhrn z Redditu – 5. listopadu 2026

## Metodika

Data pocházejí z Redditu, který 5. 11. 2026 stáhl `scripts/rd-collect-web.py` přímo z webu. V datech je **332 postů** s alespoň 10 komentáři (`appendix.json`) a **40 kandidátů** pro výběr (`candidates.json`). Po filtraci vzniklo **17 článků z 19 postů**; dva posty o stejné zprávě METR byly sloučeny do jednoho článku a jsou uvedeny jako další diskuse.

**Vyřazeno kvůli překryvu s posledními třemi dny** (`logs/recent-2026-11-05-rd.md`): **10 témat** – šly o zprávy o datacentrech a volbách, Qwen 3.8, Opus 5.5 aplikacích, AI pause a poklesu akcií AI, které už vyšly 2.–4. 11. Dalších 11 kandidátů byly memy, obrázkové vtipy nebo málo relevantní diskuze. Když hrozila byť jen částečná shoda události nebo produktu, téma jsem vynechal.

Některé externí články se nepodařilo načíst (HTTP 403 nebo paywall), takže texty vycházejí z popisu v postu, dostupného obsahu a komentářů. Časy jsou v Europe/Prague.

## Články

| ID | Titulek | Subreddit | Skóre | Komentáře |
|---|---|---|---:|---:|
| [1xossr5](1xossr5_glm-5-5-treninkovy-pipeline.md) | [Hlavní vědec Z.ai Jie Tang právě odhalil tréninkovou pipeline chystaného GLM-5.5 (32B, 122B a 256B)](1xossr5_glm-5-5-treninkovy-pipeline.md) | LocalLLaMA | 992 | 173 |
| [1xo3a2k](1xo3a2k_openai-948-linux-zranitelnosti.md) | [OpenAI tvrdí, že jejich nový bezpečnostní model opravil 948 zranitelností pro eskalaci oprávnění v Linuxu](1xo3a2k_openai-948-linux-zranitelnosti.md) | singularity | 821 | 151 |
| [1xorf5c](1xorf5c_metr-anthropic-model-4.md) | [METR odhalil nevydaný Model 4 od Anthropic, trénovaný v září–říjnu 2026, získal 178,6 v indexu schopností AI, což je skok téměř o 90 % tak velký jako celé zlepšení z Opus 4.6 na Mythos 5](1xorf5c_metr-anthropic-model-4.md) <br><small>sloučeno: 1xowicq, 1xouj6t</small> | singularity | 638 | 133 |
| [1xodizg](1xodizg_airpods-3-head-tracking-linux.md) | [Pomocí Claude Code jsem zjistil, jak AirPods 3 posílají data o sledování hlavy, ukázalo se, že to přede mnou nikdo neudělal](1xodizg_airpods-3-head-tracking-linux.md) | ClaudeAI | 504 | 62 |
| [1xoj99r](1xoj99r_readme-po-claudovi-balast.md) | [Vibe-codeři, prosím vás: když dáváte svou aplikaci nebo nástroj na Github, upravte README a odstraňte z něj Claudeovu omáčku](1xoj99r_readme-po-claudovi-balast.md) | ClaudeAI | 467 | 128 |
| [1xoo9ob](1xoo9ob_gpt-6-cyber-exploitgym.md) | [OpenAI právě oznámilo GPT-6 Cyber, velký skok oproti GPT-5.6 Cyber, který ve většině kybernetických úloh překonává GPT-6 Astra](1xoo9ob_gpt-6-cyber-exploitgym.md) | singularity | 447 | 68 |
| [1xo8ykt](1xo8ykt_taylor-lorenz-anti-ai-kampan.md) | [Bývalá technologická reportérka New York Times a Washington Post Taylor Lorenz říká, že jí nabízejí peníze za propagaci anti-AI kampaně – která jako důvod pro její nábor uvedla její vlastní vyšetřování placených anti-AI vlivových kampaní](1xo8ykt_taylor-lorenz-anti-ai-kampan.md) | singularity | 342 | 143 |
| [1xobe4h](1xobe4h_ccore-glb-3d-coder-4b.md) | [Finální model CCORE GLB-3D-Coder 4B a plné váhy jsou venku](1xobe4h_ccore-glb-3d-coder-4b.md) | LocalLLaMA | 341 | 62 |
| [1xo3oir](1xo3oir_openai-images-2-6.md) | [Představujeme Images 2.6](1xo3oir_openai-images-2-6.md) | ChatGPT | 330 | 107 |
| [1xojme6](1xojme6_lokalni-ai-slepa-ulicka.md) | [Má ten týpek pravdu? Lokální běh je jen nesplnitelný sen?](1xojme6_lokalni-ai-slepa-ulicka.md) | LocalLLM | 325 | 477 |
| [1xobw98](1xobw98_chatgpt-generovani-gifu.md) | [ChatGPT teď umí vytvářet GIFy :D](1xobw98_chatgpt-generovani-gifu.md) | ChatGPT | 312 | 56 |
| [1xoovpo](1xoovpo_minimax-h3-plovouci-saty.md) | [Extrakce oblečení pomocí úpravy jediného snímku v MiniMax H3](1xoovpo_minimax-h3-plovouci-saty.md) | StableDiffusion | 267 | 16 |
| [1xok8n6](1xok8n6_cinsky-ai-vedec-experiment.md) | [Čínský AI vědec dokončil experiment o 11 382 krocích za 203 hodin](1xok8n6_cinsky-ai-vedec-experiment.md) | singularity | 266 | 24 |
| [1xo79np](1xo79np_claude-ucitel-jazyku.md) | [Učím se jazyky psaním s Claude jako mým učitelem](1xo79np_claude-ucitel-jazyku.md) | ClaudeAI | 264 | 49 |
| [1xojryw](1xojryw_rtx-pro-5500-blackwell-cena.md) | [NVIDIA RTX PRO 5500 Blackwell se objevila za $17,999 MSRP, dráž než RTX PRO 6000 za $16,000 MSRP, kterou NVIDIA stanovila před pár měsíci - VideoCardz](1xojryw_rtx-pro-5500-blackwell-cena.md) | LocalLLaMA | 240 | 116 |
| [1xo7urk](1xo7urk_deepmind-antigravity-cheminformatika.md) | [Google DeepMind představil agentní cheminformatiku na Antigravity: vícedenní postupy návrhu léčiv zkracuje na 1 hodinu](1xo7urk_deepmind-antigravity-cheminformatika.md) | singularity | 234 | 15 |
| [1xoi8wi](1xoi8wi_deepseek-v4-flash-lokalne-1170-tok-s.md) | [2x RTX PRO 6000 provozující DeepSeek-V4-Flash (284B) plně offline: špička 1 170 tok/s](1xoi8wi_deepseek-v4-flash-lokalne-1170-tok-s.md) | LocalLLM | 232 | 63 |

## Příloha: všechny posty s alespoň 10 komentáři

Celkem **332** postů, seřazeno podle skóre. Odkazy u zařazených a sloučených postů míří na příslušný článek; u ostatních je uvedeno jen ID. Titulky jsou původní, nepřeložené.

| ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1xoi72w | ChatGPT | 2397 | 97 | 5. 11. 2026, 14:07 | Kevin Drops the Chili in Every Era of Human History |
| 1xovnaa | LocalLLaMA | 1271 | 286 | 5. 11. 2026, 23:00 | Maybe we'll get cheap RAM for Christmas after all! |
| 1xoeeyf | LocalLLaMA | 1245 | 331 | 5. 11. 2026, 10:31 | Qwen3.8-27B has become unuseable recently |
| 1xovn11 | singularity | 1225 | 339 | 5. 11. 2026, 23:00 | Some positive news? |
| [1xossr5](1xossr5_glm-5-5-treninkovy-pipeline.md) | LocalLLaMA | 992 | 173 | 5. 11. 2026, 21:06 | Z.ai chief scientist Jie Tang just revealed the training pipeline behind the upcoming GLM-5.5 (32B, 122B, and 256B) |
| 1xoeefa | ChatGPT | 830 | 37 | 5. 11. 2026, 10:30 | Sam Has Expensive Taste |
| [1xo3a2k](1xo3a2k_openai-948-linux-zranitelnosti.md) | singularity | 821 | 151 | 5. 11. 2026, 00:25 | OpenAI claims their new security model patched 948 Linux privilege escalation vulnerabilities |
| 1xobggp | ClaudeAI | 797 | 127 | 5. 11. 2026, 07:17 | I built a hyper realistic fighter jet simulator for the browser with opus 5.5 and it went viral on Twitter! |
| 1xobzg3 | LocalLLaMA | 744 | 106 | 5. 11. 2026, 07:50 | Qwen be like |
| 1xoeqod | LocalLLM | 688 | 202 | 5. 11. 2026, 10:53 | QWEN 3.8 FN - 8bit FP quant - 96.32 tokens/s - Context of 95k - $1500 hardware |
| 1xo7tx5 | ChatGPT | 664 | 235 | 5. 11. 2026, 04:00 | 🤖❤️ |
| [1xorf5c](1xorf5c_metr-anthropic-model-4.md) | singularity | 638 | 133 | 5. 11. 2026, 20:12 | METR reveals Anthropic's unreleased Model 4, trained in September–October 2026, scored 178.6 on the AI capability index, a jump nearly 90% as large as the entire improvement from Opus 4.6 to Mythos 5. |
| 1xompe9 | ChatGPT | 637 | 49 | 5. 11. 2026, 17:14 | If we replaced Terminator with Mike Tyson |
| 1xobpkf | ChatGPT | 636 | 127 | 5. 11. 2026, 07:33 | What happened?! |
| 1xohajy | OpenAI | 533 | 63 | 5. 11. 2026, 13:22 | Linux kernel maintainers |
| 1xoruzb | ChatGPT | 506 | 380 | 5. 11. 2026, 20:29 | Abdul El-Sayed is the Pause AI candidate: Abdul El-Sayed supports Bernie's AI pause and calls for an international treaty with China: "We have to figure out how work together like we have with other humanity-risking technologies like nuclear." |
| [1xodizg](1xodizg_airpods-3-head-tracking-linux.md) | ClaudeAI | 504 | 62 | 5. 11. 2026, 09:31 | used claude code to figure out how airpods 3 send head tracking data, turns out nobody had done it before |
| 1xobpr0 | ChatGPT | 472 | 197 | 5. 11. 2026, 07:33 | Asked chatGPT to create me with the most flattering makeup possible |
| [1xoj99r](1xoj99r_readme-po-claudovi-balast.md) | ClaudeAI | 467 | 128 | 5. 11. 2026, 14:56 | Vibe-coders, I beg you: when posting your app or tool on Github, please edit the README to remove Claude's fluff |
| [1xoo9ob](1xoo9ob_gpt-6-cyber-exploitgym.md) | singularity | 447 | 68 | 5. 11. 2026, 18:13 | OpenAI has just announced GPT‑6 Cyber, a major step up from GPT‑5.6 Cyber and outperforms GPT‑6 Astra on most cyber tasks |
| 1xopd9s | StableDiffusion | 432 | 28 | 5. 11. 2026, 18:54 | Detroit: Become Jensen |
| 1xoqj9r | singularity | 421 | 140 | 5. 11. 2026, 19:38 | Oh well... |
| 1xorzoa | OpenAI | 346 | 422 | 5. 11. 2026, 20:34 | Abdul El-Sayed is the Pause AI candidate: Abdul El-Sayed supports Bernie's AI pause and calls for an international treaty with China: "We have to figure out how work together like we have with other humanity-risking technologies like nuclear." |
| [1xo8ykt](1xo8ykt_taylor-lorenz-anti-ai-kampan.md) | singularity | 342 | 143 | 5. 11. 2026, 04:57 | Former New York Times and Washington Post tech reporter Taylor Lorenz says she's being offered money to promote an anti-AI campaign—which cited her own investigation into paid anti-AI influence campaigns as the reason for recruiting her. |
| [1xobe4h](1xobe4h_ccore-glb-3d-coder-4b.md) | LocalLLaMA | 341 | 62 | 5. 11. 2026, 07:14 | CCORE GLB-3D-Coder 4B final model and full weights are out |
| [1xo3oir](1xo3oir_openai-images-2-6.md) | ChatGPT | 330 | 107 | 5. 11. 2026, 00:43 | Introducing Images 2.6 |
| [1xojme6](1xojme6_lokalni-ai-slepa-ulicka.md) | LocalLLM | 325 | 477 | 5. 11. 2026, 15:11 | Is bro right? Local is a pipe dream? |
| [1xobw98](1xobw98_chatgpt-generovani-gifu.md) | ChatGPT | 312 | 56 | 5. 11. 2026, 07:45 | ChatGPT can create GIF now :D |
| 1xou90f | ClaudeAI | 280 | 55 | 5. 11. 2026, 22:04 | I built a 3D globe for my two boys with Claude Code. It got way more love than I expected, so here's how it's grown. |
| [1xowicq](1xorf5c_metr-anthropic-model-4.md) | singularity | 270 | 73 | 5. 11. 2026, 23:37 | Anthropic has a powerful new AI model it hasn't released yet. METR reports that "Model 4" scored above 50% on all 15 capability benchmarks tested, raising concerns that existing AI tests are becoming too easy to measure frontier progress. |
| [1xoovpo](1xoovpo_minimax-h3-plovouci-saty.md) | StableDiffusion | 267 | 16 | 5. 11. 2026, 18:36 | Clothes extraction with MiniMax H3 single frame edit |
| [1xok8n6](1xok8n6_cinsky-ai-vedec-experiment.md) | singularity | 266 | 24 | 5. 11. 2026, 15:37 | Chinese AI Scientist Completes 11,382-Step Experiment in 203 Hours |
| [1xo79np](1xo79np_claude-ucitel-jazyku.md) | ClaudeAI | 264 | 49 | 5. 11. 2026, 03:32 | Learning languages by writing with Claude as my tutor. |
| 1xojy0k | agi | 258 | 224 | 5. 11. 2026, 15:24 | Abdul El-Sayed is the Pause AI candidate: Abdul El-Sayed supports Bernie's AI pause and calls for an international treaty with China: "We have to figure out how work together like we have with other humanity-risking technologies like nuclear." |
| 1xoourx | agi | 251 | 10 | 5. 11. 2026, 18:35 | I guess I'm an LLM |
| [1xojryw](1xojryw_rtx-pro-5500-blackwell-cena.md) | LocalLLaMA | 240 | 116 | 5. 11. 2026, 15:17 | NVIDIA RTX PRO 5500 Blackwell appears at $17,999 MSRP, higher than RTX PRO 6000 at $16,000 MSRP set some months ago by NVIDIA - VideoCardz |
| [1xo7urk](1xo7urk_deepmind-antigravity-cheminformatika.md) | singularity | 234 | 15 | 5. 11. 2026, 04:01 | Google DeepMind unveils agentic cheminformatics on Antigravity: compresses multi-day drug design workflows into 1 hour |
| [1xoi8wi](1xoi8wi_deepseek-v4-flash-lokalne-1170-tok-s.md) | LocalLLM | 232 | 63 | 5. 11. 2026, 14:10 | 2x RTX PRO 6000 running DeepSeek-V4-Flash (284B) fully offline: 1,170 tok/s peak |
| 1xo49pg | singularity | 199 | 129 | 5. 11. 2026, 01:09 | 63% of planned/under construction data centers in the US are in states with governors who have promised to ban or pause new data centers. |
| [1xouj6t](1xorf5c_metr-anthropic-model-4.md) | singularity | 196 | 33 | 5. 11. 2026, 22:15 | Ryan Greenblatt of METR estimates that AI R&D acceleration has already reached levels predicted for March 2027 in the AI 2027 scenario, based on today's METR report. |
| 1xoj35f | singularity | 179 | 153 | 5. 11. 2026, 14:48 | Senator Elect Abdul El-Sayed States The Chinese Are Just Copying American AI Technology And Do Not Innovate; Research Scientist At Meta States Abdul Is Clueless |
| 1xoj1sp | comfyui | 173 | 57 | 5. 11. 2026, 14:47 | Does anyone which ai model is it? |
| 1xo2t2u | singularity | 172 | 313 | 5. 11. 2026, 00:04 | We're headed to UBI or even UHI post-scarcity economics or hell on earth. No inbetween. |
| 1xoh2u0 | OpenAI | 163 | 53 | 5. 11. 2026, 13:11 | I tried the new image 2.6 gif feature |
| 1xo6cbs | ArtificialInteligence | 160 | 189 | 5. 11. 2026, 02:47 | What’s happening to the software industry now is going to happen to every industry |
| 1xo3ikc | LocalLLaMA | 154 | 277 | 5. 11. 2026, 00:35 | What are you looking forward to in Qwen 4? |
| 1xosbwp | singularity | 149 | 38 | 5. 11. 2026, 20:48 | Independent researchers at METR find Anthropic is making nearly 2 years of AI progress in just 1 year, likely driven mostly by AI helping develop better AI. They found no clear bottlenecks preventing further acceleration. |
| 1xou0q2 | ClaudeAI | 148 | 96 | 5. 11. 2026, 21:55 | 3 interesting things Claude can do for you but you didn't know |
| 1xor677 | artificial | 148 | 34 | 5. 11. 2026, 20:02 | Hideo Kojima says AI lacks what makes the creative process fun, despite its efficiency. “It’s not a form of creation I find particularly interesting” - AUTOMATON WEST |
| 1xoibxr | GeminiAI | 148 | 46 | 5. 11. 2026, 14:14 | The Struggle of the Free Users as of Nov 2026. Google Please have mercy! |
| 1xo4rah | singularity | 142 | 37 | 5. 11. 2026, 01:31 | Try out GPT image 2.6 and report back |
| 1xourfu | singularity | 135 | 62 | 5. 11. 2026, 22:24 | Demis Hassabis on AI consciousness: “I don’t think we are ready yet as a society” |
| 1xouggg | singularity | 130 | 25 | 5. 11. 2026, 22:12 | The AI 2027 tracker is currently 19 for 24. The 2027 intelligence explosion timeline is actually holding up perfectly.. |
| 1xopc6c | singularity | 129 | 79 | 5. 11. 2026, 18:53 | Nasdaq 100 eyes $1.8 trillion loss as Democratic win sparks AI delay fears |
| 1xocwcy | artificial | 124 | 95 | 5. 11. 2026, 08:50 | Apple is cutting employee AI spending budgets even as it pushes workers to use the technology more. Engineers have seen daily limits cut from $300 to $200, with further reductions to $100 planned. Other teams could see limits fall to $25. |
| 1xoos40 | singularity | 123 | 47 | 5. 11. 2026, 18:32 | 3d-printed, biomimetical legs: by changing the structure of materials, researchers were able to print muscles, tendons, ligaments, cushion components and let them move like a humanoid robot |
| 1xotduk | StableDiffusion | 118 | 46 | 5. 11. 2026, 21:29 | [Model Release] Qwen-Image-2.1 Uncensored Omni — trained on ~1M images, 9 local formats |
| 1xoq4vq | LocalLLaMA | 117 | 28 | 5. 11. 2026, 19:23 | DeepSeek-V4.1-Flash-1017 on one RTX 3090: Big updates to the Delta Inference Engine v0.93. Same 41 tok/s at 192GB/IQ2 at better quality, usable from 64 GB RAM, first token ~40% sooner, new Unsloth quants at full speed, EXL3, basic multi-GPU, public CI and more |
| 1xoml5v | ChatGPT | 113 | 132 | 5. 11. 2026, 17:09 | What chatGPT phrase annoys you the most? |
| 1xoo1pf | ClaudeAI | 102 | 51 | 5. 11. 2026, 18:04 | I'm an accountant and somehow Claude has me building software for our office |
| 1xokowx | OpenAI | 101 | 23 | 5. 11. 2026, 15:55 | After America voted against data centres, OpenAI promises to pay its own power bills and end secrecy deals |
| 1xo6yzo | MachineLearning | 100 | 243 | 5. 11. 2026, 03:17 | ICLR 2027 Reviews Discussion [D] |
| 1xomiym | agi | 96 | 43 | 5. 11. 2026, 17:07 | OpenAI caught Astra covertly sandbagging on safety research, and researchers say this is "extremely concerning", since OpenAI's entire plan is to trust the AIs themselves to safely align future AIs: "Astra often makes surprisingly little progress on safety research and likes to invent blockers." |
| 1xo3pjo | StableDiffusion | 87 | 35 | 5. 11. 2026, 00:44 | New TurboH3 FL2VA |
| 1xook9e | ClaudeAI | 84 | 17 | 5. 11. 2026, 18:24 | Claude built a programming language for AI agents where every keyword is an internet meme |
| 1xotfew | ArtificialInteligence | 83 | 76 | 5. 11. 2026, 21:31 | The Tech Stock Bloodbath Has Begun: Why a Massive PC Hardware Price Crash is Inevitable (And Why We Must Hold) |
| 1xohbcw | ChatGPT | 83 | 11 | 5. 11. 2026, 13:23 | Linux kernel maintainers |
| 1xokxag | OpenAI | 81 | 19 | 5. 11. 2026, 16:04 | OpenAI caught Astra covertly sandbagging on safety research, and researchers say this is "extremely concerning", since OpenAI's entire plan is to trust the AIs themselves to safely align future AIs: "Astra often makes surprisingly little progress on safety research and likes to invent blockers." |
| 1xorgve | singularity | 79 | 28 | 5. 11. 2026, 20:14 | Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 \| METR |
| 1xop1jl | GeminiAI | 79 | 10 | 5. 11. 2026, 18:42 | Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips |
| 1xowrit | singularity | 77 | 12 | 5. 11. 2026, 23:48 | What did they find? |
| 1xotkqg | ClaudeAI | 75 | 38 | 5. 11. 2026, 21:37 | I've used the Big Three of the AI industry and here's what I think as an average human |
| 1xosw1w | LocalLLaMA | 75 | 14 | 5. 11. 2026, 21:09 | Appreciation post for OrcaCyber-Nano-1.0 |
| 1xopih9 | GeminiAI | 71 | 32 | 5. 11. 2026, 19:00 | Gemini Live just spoke back to me in my own voice and it completely freaked me out. Has this happened to anyone else? |
| 1xoji3b | LocalLLaMA | 69 | 23 | 5. 11. 2026, 15:06 | Getting editable layers out of Qwen-Image 2.1, a model that only edits: what works, what still fails (local, open source) Kokon |
| 1xod8js | GeminiAI | 68 | 14 | 5. 11. 2026, 09:11 | After every other model failed some noncoding tasks, I gave them to Argon. Wow, I'm impressed. |
| 1xobtwx | LocalLLaMA | 68 | 14 | 5. 11. 2026, 07:40 | baidu/ERNIE-5.5-Flash-Base · Hugging Face |
| 1xoo84v | singularity | 63 | 259 | 5. 11. 2026, 18:11 | democrats are what we need for ai |
| 1xottw2 | LocalLLaMA | 60 | 21 | 5. 11. 2026, 21:47 | Strata for all Qwen models from little to big |
| 1xoolkp | LocalLLM | 60 | 26 | 5. 11. 2026, 18:25 | I ran the new Qwen 3.8FN release with "make browser GTA one shot, no mistakes" prompt. details and demo link inside |
| 1xoc4q4 | LocalLLM | 58 | 50 | 5. 11. 2026, 07:59 | Finally got the Tiiny Pocket. Ask me anything |
| 1xogmrl | ChatGPT | 57 | 54 | 5. 11. 2026, 12:47 | Normal chat is using limit now? I never use Codex. |
| 1xoiaye | LocalLLaMA | 56 | 10 | 5. 11. 2026, 14:12 | An open-source project just ranked #1 on EnterpriseRAG-Bench, ahead of the listed systems from OpenAI, Google, Microsoft and Amazon |
| 1xom1b9 | StableDiffusion | 54 | 13 | 5. 11. 2026, 16:47 | HexAnima: Anima on the Snapdragon 8 Gen 1 NPU, 512x768 in ~7 s, fully offline, no root |
| 1xo7ahm | singularity | 54 | 80 | 5. 11. 2026, 03:33 | China's Datacenter Regulations |
| 1xocmll | OpenAI | 53 | 13 | 5. 11. 2026, 08:31 | WTF is this shit |
| 1xomy0i | LocalLLaMA | 52 | 27 | 5. 11. 2026, 17:23 | [GUIDE] Qwen3.8 Flash-Next on a single RTX 5080 + 64GB RAM: >250 tok/s tg and 5700 tok/s prefill in real agent coding sessions (Basalt + new Unsloth UD-IQ3_XXS + Lamina drafter),+ how it compares to llama.cpp |
| 1xogrcz | ChatGPT | 51 | 49 | 5. 11. 2026, 12:55 | This is new |
| 1xob6rr | StableDiffusion | 51 | 39 | 5. 11. 2026, 07:01 | Moss really understands what "beautiful" means |
| 1xo7q89 | MachineLearning | 51 | 26 | 5. 11. 2026, 03:55 | What is now considered a “reasonable” publication rate (papers/year) for a PhD student to be considered “productive”? [D] |
| 1xot900 | ChatGPT | 50 | 39 | 5. 11. 2026, 21:24 | It Made Me Cry |
| 1xouz3f | ChatGPT | 48 | 30 | 5. 11. 2026, 22:33 | GPT's safeguards and restrictions: |
| 1xohteq | ClaudeAI | 48 | 34 | 5. 11. 2026, 13:49 | The safety rail guards of Claude's models is making me reconsider |
| 1xoql51 | LocalLLaMA | 47 | 13 | 5. 11. 2026, 19:40 | Deepseek fixed my HDMI display show case |
| 1xoubyo | LocalLLaMA | 46 | 23 | 5. 11. 2026, 22:07 | Lawyer with too many GPUs, part 4: DeepSeek-V4.1-Flash on eight V100s from 2018. 200+ tok/s on code, ~110 on legal writing, 2,200 tok/s prefill at 128K, 524K context, every weight in VRAM |
| 1xoegnb | LocalLLM | 46 | 46 | 5. 11. 2026, 10:34 | Contribute instead of reinventing |
| 1xo2vxi | GeminiAI | 46 | 26 | 5. 11. 2026, 00:07 | Why is Gemini so sensitive nowadays? (behind the black box is my city) |
| 1xojxy6 | LocalLLM | 45 | 13 | 5. 11. 2026, 15:24 | NVIDIA RTX PRO 5500 Blackwell appears at $17,999 MSRP, higher than RTX PRO 6000 at $16,000 MSRP set some months ago by NVIDIA - VideoCardz |
| 1xoi5w2 | singularity | 43 | 35 | 5. 11. 2026, 14:06 | When do we get a real hardware paradigm shift instead of just scaling the GPU/RAM triad? |
| 1xouhjx | ClaudeAI | 42 | 14 | 5. 11. 2026, 22:14 | Tired of ads and pay-to-win games, I asked Claude to copycat them all. |
| 1xoqrzv | ChatGPT | 40 | 21 | 5. 11. 2026, 19:47 | GPT saved my bricked computer. |
| 1xoe1b4 | GeminiAI | 39 | 10 | 5. 11. 2026, 10:05 | gemini 4 fixed a pc port of a ps vita game for me |
| 1xobvm7 | LocalLLM | 39 | 61 | 5. 11. 2026, 07:43 | Highly optimized Strata port for 7900xtx 24GB |
| 1xo6xwn | agi | 39 | 31 | 5. 11. 2026, 03:16 | It’s crazy the emergent behavior that happens with agent interactions |
| 1xov63n | GeminiAI | 37 | 23 | 5. 11. 2026, 22:40 | Trying Gemini after ChatGPT and Claude |
| 1xoo0lq | ClaudeAI | 37 | 19 | 5. 11. 2026, 18:03 | I'm speechless with Claude Capacity for game creation |
| 1xodbfm | ClaudeAI | 36 | 34 | 5. 11. 2026, 09:17 | Desktop app can read computer folder names without permission |
| 1xoc358 | MachineLearning | 36 | 52 | 5. 11. 2026, 07:56 | Publication expectations for ML PhDs at top-10 US schools / top ML groups? [D] |
| 1xoekfp | comfyui | 35 | 31 | 5. 11. 2026, 10:41 | P-H3 / Flux3-Klein / Moss / Krea2-Raw \| First-Shot Results (No Cherry-Picking) |
| 1xog7d7 | GeminiAI | 34 | 16 | 5. 11. 2026, 12:23 | The 'Google AI' Plans are pretty weird |
| 1xo8nka | StableDiffusion | 34 | 19 | 5. 11. 2026, 04:41 | Minimax h3 voice acting capabilities seem to be better than people here think |
| 1xocy55 | ChatGPT | 33 | 18 | 5. 11. 2026, 08:53 | Anyone else noticing their ChatGPT usage limits getting burned through WAY faster over the past few days? |
| 1xoh2s7 | LocalLLaMA | 32 | 73 | 5. 11. 2026, 13:11 | Rather Qwen4-27b at 1M ctx than a big MOE at 128k |
| 1xoju07 | StableDiffusion | 31 | 31 | 5. 11. 2026, 15:19 | How would I make a simple prompt builder with selectable text inputs in Comfyui |
| 1xojjyt | ChatGPT | 31 | 84 | 5. 11. 2026, 15:08 | Will you keep your ChatGPT subscription after the December changes, or switch to another AI? |
| 1xoqalq | StableDiffusion | 30 | 37 | 5. 11. 2026, 19:29 | is minimax h3 image edit better than qwen 2.1 image edit |
| 1xoep25 | ArtificialInteligence | 28 | 54 | 5. 11. 2026, 10:50 | Anthropic Cash Flowing |
| 1xolzrh | ClaudeAI | 27 | 20 | 5. 11. 2026, 16:46 | Haiku in Claude Code stopped reading me data from my database |
| 1xohbd3 | LocalLLaMA | 25 | 27 | 5. 11. 2026, 13:23 | My first experience with agentic AI |
| 1xotu63 | StableDiffusion | 24 | 58 | 5. 11. 2026, 21:47 | What happened to Z-Image? |
| 1xopu10 | LocalLLM | 24 | 58 | 5. 11. 2026, 19:11 | What's more impactful: more system RAM or faster RAM? |
| 1xoqq49 | OpenAI | 23 | 36 | 5. 11. 2026, 19:45 | Godfather of AI warns humanity: It’s all hurtling out of control |
| 1xoo730 | LocalLLaMA | 23 | 41 | 5. 11. 2026, 18:10 | Can Opus weight-space-edit Qwen3.8-27B to refuse less? Yes |
| 1xo3q9v | ClaudeAI | 23 | 28 | 5. 11. 2026, 00:45 | Claude chat vs. Claude Code in the desktop app: what's the real difference? |
| 1xonln8 | StableDiffusion | 22 | 16 | 5. 11. 2026, 17:48 | NitroFusion2 - Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers |
| 1xon5bu | ArtificialInteligence | 22 | 45 | 5. 11. 2026, 17:31 | Does using AI actually make you think more rather than less? |
| 1xolfl3 | LocalLLM | 22 | 44 | 5. 11. 2026, 16:24 | How much VRAM do i really need? |
| 1xoiit9 | StableDiffusion | 22 | 73 | 5. 11. 2026, 14:23 | Dear Diary - RTX Super Resolution.... not so good |
| 1xo4r1b | LocalLLM | 22 | 18 | 5. 11. 2026, 01:31 | What is the Best Local AI Models for Coding and UI/UX Design on Ryzen AI Max+ 395 (128GB)? |
| 1xoujte | LocalLLM | 21 | 14 | 5. 11. 2026, 22:16 | [Crazy AI Lawyer] DeepSeek-V4.1-Flash on eight 2018 V100s is doing my real work now: 524K context, every weight in VRAM, 200+ tok/s on code, ~110 on legal writing, RAG and tool calls wired in |
| 1xoib84 | LocalLLaMA | 21 | 14 | 5. 11. 2026, 14:13 | Tiiny AI Performance tests. I just got my Tiiny, and here's what it can do. |
| 1xo8uzn | LLMDevs | 21 | 20 | 5. 11. 2026, 04:51 | Can a 1-trillion-parameter model run on a 64 GB desktop? I built an open-source engine to find out, and it already beats llama.cpp on models bigger than RAM. |
| 1xod8nb | LocalLLaMA | 20 | 13 | 5. 11. 2026, 09:12 | Int8-vllm updated with Nemotron 3.5 Bolt 74B |
| 1xo52gw | GeminiAI | 20 | 17 | 5. 11. 2026, 01:45 | What is Gemini Carbon? |
| 1xoqgn0 | StableDiffusion | 18 | 16 | 5. 11. 2026, 19:35 | MOSS-Image-Base: two stage workflow |
| 1xol3l9 | ClaudeAI | 18 | 10 | 5. 11. 2026, 16:11 | Claude Code ported my React Native app to Swift. A benchmark found the bugs it missed |
| 1xot3ee | ChatGPT | 17 | 15 | 5. 11. 2026, 21:17 | Is anyone else experiencing “Context window full” errors after just a few messages? |
| 1xohdtu | StableDiffusion | 17 | 17 | 5. 11. 2026, 13:27 | Demons (trend) |
| 1xo7z6f | ChatGPT | 17 | 36 | 5. 11. 2026, 04:07 | Is there any way to recover the full contents of an extremely long ChatGPT conversation? |
| 1xo2ya7 | ChatGPT | 17 | 36 | 5. 11. 2026, 00:10 | GPT-6 Pro crashing out and leaking internal prompts |
| 1xo3gwa | LocalLLaMA | 16 | 64 | 5. 11. 2026, 00:33 | 27B vs Flash next |
| 1xor9x3 | ChatGPT | 15 | 20 | 5. 11. 2026, 20:06 | Both my paid ChatGPT Business accounts are completely out of usage after a week of broken Goals and endless loops. OpenAI has no meaningful emergency support for businesses that depend on its products |
| 1xofwnt | ChatGPT | 15 | 53 | 5. 11. 2026, 12:04 | I asked ChatGPT what car i'd be |
| 1xovzq9 | ChatGPT | 14 | 29 | 5. 11. 2026, 23:14 | It doesnt seem to know a video game |
| 1xo3rl7 | StableDiffusion | 14 | 18 | 5. 11. 2026, 00:47 | Sage, Sol, Kitchen, etc...ffs, I just want to grill! |
| 1xoj4te | ArtificialInteligence | 13 | 31 | 5. 11. 2026, 14:50 | astroturfing is seriously out of hand |
| 1xoe9yc | ChatGPT | 13 | 28 | 5. 11. 2026, 10:21 | Content Window Is Full Problem |
| 1xoc1uc | LocalLLM | 13 | 37 | 5. 11. 2026, 07:54 | What are you currently running? |
| 1xoshsc | GeminiAI | 12 | 13 | 5. 11. 2026, 20:54 | What are your best custom instructions for Gemini? |
| 1xonn59 | ChatGPT | 12 | 10 | 5. 11. 2026, 17:49 | Is this for real? I think they made the guardrails worse boys :)) |
| 1xomsxq | LocalLLaMA | 12 | 20 | 5. 11. 2026, 17:17 | I was curious how small local models handle Polish grammar – a quick 15-task test on 8 GB VRAM |
| 1xofzfe | OpenAI | 12 | 10 | 5. 11. 2026, 12:09 | This is getting old |
| 1xo9yhy | ChatGPT | 12 | 11 | 5. 11. 2026, 05:51 | Live Voice changing subject and filling the silence |
| 1xo5zzj | ChatGPT | 12 | 20 | 5. 11. 2026, 02:30 | Context Window Full |
| 1xo4bc7 | ChatGPT | 12 | 13 | 5. 11. 2026, 01:11 | ChatGPT image generation can make GIFS now |
| 1xo3888 | OpenAI | 12 | 12 | 5. 11. 2026, 00:22 | I used AI to build a custom launcher for my TCL Google TV, with live weather, themes, and a split screen the TV doesn't normally allow |
| 1xowo4h | ClaudeAI | 11 | 15 | 5. 11. 2026, 23:44 | Anyone else find themselves switching back and forth between Claude and codex? |
| 1xon9b3 | ChatGPT | 11 | 30 | 5. 11. 2026, 17:35 | Does using AI actually make you think more rather than less? |
| 1xom4b6 | ChatGPT | 11 | 16 | 5. 11. 2026, 16:51 | Too many disclaimers. Tired of being the sacrifice/price being paid for some irresponsible individuals |
| 1xow1eb | ChatGPT | 10 | 19 | 5. 11. 2026, 23:16 | There is a bug with my chat |
| 1xomefu | singularity | 10 | 12 | 5. 11. 2026, 17:02 | r/Singularity Daily Discussion Thread — November 05, 2026 |
| 1xobxb1 | ArtificialInteligence | 10 | 12 | 5. 11. 2026, 07:46 | Best non-sensationalized AI news YouTubers? |
| 1xo9n9r | StableDiffusion | 10 | 10 | 5. 11. 2026, 05:33 | 3 short years ago… |
| 1xo874r | artificial | 10 | 14 | 5. 11. 2026, 04:18 | Could AI search hurt ad business? |
| 1xotzaw | ChatGPT | 9 | 63 | 5. 11. 2026, 21:53 | AI Stocks Crashing Today |
| 1xom9gh | GeminiAI | 9 | 11 | 5. 11. 2026, 16:57 | Why is Gemini suddenly winking at me? |
| 1xofuqe | ClaudeAI | 9 | 27 | 5. 11. 2026, 12:01 | Designer new to Claude Code – any tips for beginners? |
| 1xoe3a5 | ClaudeAI | 9 | 29 | 5. 11. 2026, 10:09 | Do you ask Claude for its opinion about your app/business idea? |
| 1xocdy6 | LocalLLaMA | 9 | 10 | 5. 11. 2026, 08:15 | Did anyone tried Qwen-3.8-27B QSA ? |
| 1xo5ird | LLMDevs | 9 | 21 | 5. 11. 2026, 02:06 | How to verify a LLM provider’s zero data retention? Contract, audit, and/or attestation? TEEs? |
| 1xowkbd | ChatGPT | 8 | 10 | 5. 11. 2026, 23:39 | Humor- do you think this was this really unintentional? |
| 1xopf8g | ClaudeAI | 8 | 28 | 5. 11. 2026, 18:56 | I run my whole app solo with 15 Claude Code sessions, each with its own job. Here’s the setup prompt. |
| 1xolh19 | LocalLLaMA | 8 | 33 | 5. 11. 2026, 16:25 | [Hardware] Is a AMD 395+ AI with 128 GB RAM still good choice for local LLMs? (inference mostly) |
| 1xog015 | artificial | 8 | 13 | 5. 11. 2026, 12:10 | Where Did the People in Between Go? |
| 1xofqyh | ClaudeAI | 8 | 16 | 5. 11. 2026, 11:56 | Prompt: a live isometric "team office" for your Claude Code sessions |
| 1xoezg0 | ChatGPT | 8 | 11 | 5. 11. 2026, 11:08 | whats up with them being so vague about usage |
| 1xobady | GeminiAI | 8 | 30 | 5. 11. 2026, 07:08 | What is the best AI model? |
| 1xo8vqg | ClaudeAI | 8 | 33 | 5. 11. 2026, 04:53 | Day 5 making my dream game: free roam galaxy |
| 1xo3vgi | LocalLLaMA | 8 | 19 | 5. 11. 2026, 00:52 | Best Upgrade for 32gb RAM + 12gb VRAM PC? |
| 1xosjfh | ChatGPT | 7 | 15 | 5. 11. 2026, 20:56 | ChatGPT Plus With Codex is now unusable. |
| 1xofnbi | LocalLLaMA | 7 | 41 | 5. 11. 2026, 11:50 | Thinking about upgrading ram to 128GB |
| 1xobzaw | ChatGPT | 7 | 19 | 5. 11. 2026, 07:50 | Is OpenAI using behavioral psychology  through its growing model hierarchy? |
| 1xob4ij | GeminiAI | 7 | 19 | 5. 11. 2026, 06:58 | Is GOOGLE AI MODE reliable or unreliable? |
| 1xo66y2 | ClaudeAI | 7 | 14 | 5. 11. 2026, 02:39 | Fable feels different |
| 1xo5m3z | ArtificialInteligence | 7 | 16 | 5. 11. 2026, 02:11 | It’s crazy the emergent behavior that comes from interacting AI agents |
| 1xotym4 | LocalLLM | 6 | 28 | 5. 11. 2026, 21:52 | MacBook Pro usere who were undecided between 64 and 128GB of RAM, what helped you decide and what did you do? |
| 1xophl1 | ChatGPT | 6 | 19 | 5. 11. 2026, 18:59 | 5.6 Sol or 6 Astra for storywriting? |
| 1xom7vx | ClaudeAI | 6 | 19 | 5. 11. 2026, 16:55 | Building a personal health dashboard with Claude AI - anyone connected MyChart or Apple Health? |
| 1xoilzd | ChatGPT | 6 | 14 | 5. 11. 2026, 14:27 | How's your Terra 6.1 Experiences? |
| 1xobmzx | ClaudeAI | 6 | 25 | 5. 11. 2026, 07:28 | Is there any claude skill that can help me with this ? |
| 1xo5ht5 | ClaudeAI | 6 | 13 | 5. 11. 2026, 02:05 | Claude resurrected my thesis project… |
| 1xos8fw | ClaudeAI | 5 | 11 | 5. 11. 2026, 20:44 | How to make claude a professional assistant that actually can give useful advice |
| 1xokhyq | LocalLLaMA | 5 | 50 | 5. 11. 2026, 15:47 | Which harness/tool should I use? |
| 1xoe0p5 | ChatGPT | 5 | 12 | 5. 11. 2026, 10:04 | Are AI search tools slowly killing the websites they depend on? |
| 1xodwtf | OpenAI | 5 | 18 | 5. 11. 2026, 09:57 | OpenAI's cancel page tells you how to stop paying, not what happens to your Projects and memory afterward. What I could and couldn't find |
| 1xoc3t2 | LLMDevs | 5 | 16 | 5. 11. 2026, 07:57 | Secure LLM against malicious file uploads. |
| 1xobrdz | ClaudeAI | 5 | 15 | 5. 11. 2026, 07:36 | Claude's LaTeX/Math Rendering Is Seriously Broken on Android — Is Anyone Else Experiencing This? |
| 1xoabrz | LocalLLM | 5 | 20 | 5. 11. 2026, 06:11 | What happened to cluster setups? |
| 1xo6xbh | LLMDevs | 5 | 15 | 5. 11. 2026, 03:15 | Anyone actually running fine-tuned small models in production? |
| 1xop794 | GeminiAI | 4 | 11 | 5. 11. 2026, 18:48 | Can Gemini Argon safely (using AGY) recover data from a corrupted NVMe via USB on Windows? |
| 1xoosr8 | ClaudeAI | 4 | 23 | 5. 11. 2026, 18:33 | One-Shot better than what i had after multiple iterations |
| 1xoo0w9 | StableDiffusion | 4 | 11 | 5. 11. 2026, 18:04 | Minimax H3 Audio Refiner? |
| 1xohj0g | LocalLLM | 4 | 13 | 5. 11. 2026, 13:34 | RTX 3060 12gb - Testing |
| 1xoc10s | LocalLLM | 4 | 28 | 5. 11. 2026, 07:53 | Which harness do you use and why? |
| 1xo8a9r | agi | 4 | 35 | 5. 11. 2026, 04:22 | Unpopular Opinion: I don't particularly care who gets AGI/ASI first |
| 1xo4vcl | ChatGPT | 4 | 14 | 5. 11. 2026, 01:36 | does anyone else hate the little summaries chat gpt now does before a search? |
| 1xoswbl | OpenAI | 3 | 63 | 5. 11. 2026, 21:10 | Genuine Question: Is it bad that I ask AI almost everything i’m curious about instead of doing my own research? |
| 1xoo7og | ChatGPT | 3 | 19 | 5. 11. 2026, 18:11 | Sent an email pretending to be me |
| 1xolpez | ChatGPT | 3 | 27 | 5. 11. 2026, 16:34 | I claimed the free trial for 1 month of gpt plus, but my account still says it's free. Will this still charge me $20? |
| 1xole3o | comfyui | 3 | 21 | 5. 11. 2026, 16:22 | Best PC build for ComfyUI under $2,000 CAD? RTX 3090 24GB vs newer GPUs? |
| 1xolaq1 | ChatGPT | 3 | 15 | 5. 11. 2026, 16:18 | Did I overestimate what ChatGPT can do? |
| 1xoflgv | ChatGPT | 3 | 22 | 5. 11. 2026, 11:47 | Need to understand about this context window |
| 1xoea8o | GeminiAI | 3 | 11 | 5. 11. 2026, 10:22 | Gemini needs fixing |
| 1xobh2h | ClaudeAI | 3 | 16 | 5. 11. 2026, 07:18 | Claude Cost/Performance |
| 1xowfk2 | artificial | 2 | 17 | 5. 11. 2026, 23:33 | Is anyone using LLMs daily to build expertise in a specific field ? |
| 1xosww5 | ClaudeAI | 2 | 10 | 5. 11. 2026, 21:10 | pcbang.io - a virtual internet cafe built by opus 5.5 |
| 1xon4qe | LocalLLM | 2 | 10 | 5. 11. 2026, 17:30 | Advice on next hardware upgrade |
| 1xof9vf | ClaudeAI | 2 | 14 | 5. 11. 2026, 11:26 | Questions about Lauren Tan’s approach: How do you manage agent-added constraints in Claude Code? |
| 1xoexx4 | ArtificialInteligence | 2 | 18 | 5. 11. 2026, 11:06 | ChatGPT, Claude and Gemini all meter usage now, but none of them tells you what one message will use |
| 1xoduwp | ClaudeAI | 2 | 10 | 5. 11. 2026, 09:54 | Claude First Timer After 3 Months of Usage |
| 1xodpsg | comfyui | 2 | 10 | 5. 11. 2026, 09:44 | Can we skip the prompt unsampler (qwen 3.5 9b) in flux 3 klein workflow  . If yes then how ?? |
| 1xobd4j | ArtificialInteligence | 2 | 107 | 5. 11. 2026, 07:12 | I have been hearing about ai bubble will burst for about 2 years |
| 1xo8xgq | ClaudeAI | 2 | 18 | 5. 11. 2026, 04:55 | Which Claude skills actually make your writing sound less like AI? (social media / copywriting) |
| 1xo3lug | StableDiffusion | 2 | 11 | 5. 11. 2026, 00:39 | Qwen Prompt Enhancer Performance |
| 1xoweci | ClaudeAI | 1 | 11 | 5. 11. 2026, 23:32 | Agent factories vs. one agent with clear goals and a map of your context: where we've landed |
| 1xovpq9 | ChatGPT | 1 | 18 | 5. 11. 2026, 23:03 | Help me make gpt usable (please) |
| 1xooak2 | ClaudeAI | 1 | 16 | 5. 11. 2026, 18:14 | Claude cheaper for Voluntary School Club leader |
| 1xontgo | LocalLLM | 1 | 12 | 5. 11. 2026, 17:56 | What can I Run with my Current System? |
| 1xon1lk | StableDiffusion | 1 | 10 | 5. 11. 2026, 17:27 | Need help with generating images |
| 1xomphd | LocalLLM | 1 | 17 | 5. 11. 2026, 17:14 | Local AI for organizing files, screenshots, photos and videos - Mac Studio M2 Ultra, 128GB |
| 1xom21v | LocalLLM | 1 | 17 | 5. 11. 2026, 16:48 | For those who have gone mostly local, have you been able to reduce your subscription costs to the $20 subs? |
| 1xokef5 | ClaudeAI | 1 | 17 | 5. 11. 2026, 15:43 | What I learned trying to stop Claude from “forgetting” my projects between sessions |
| 1xok8zq | StableDiffusion | 1 | 15 | 5. 11. 2026, 15:37 | How to force fp32 with comfyui? |
| 1xoh15f | LocalLLM | 1 | 18 | 5. 11. 2026, 13:08 | Recommendations for a LocalLLM newbie? |
| 1xofw9l | LLMDevs | 1 | 18 | 5. 11. 2026, 12:04 | How do you stop human reviewers from rubber-stamping an LLM's output? |
| 1xoe7ph | ClaudeAI | 1 | 11 | 5. 11. 2026, 10:17 | Choosing Pro vs Max plan for an engineering grad student? |
| 1xodrrg | ChatGPT | 1 | 14 | 5. 11. 2026, 09:48 | Fucked Up Big Time |
| 1xod6ij | ClaudeAI | 1 | 18 | 5. 11. 2026, 09:08 | Keeping a personal Claude account separated from my work GitHub org - is a second GitHub account really the only way? |
| 1xob3p5 | LocalLLM | 1 | 14 | 5. 11. 2026, 06:57 | Seeking feedback on local LM vibe coding |
| 1xo6e3i | ClaudeAI | 1 | 15 | 5. 11. 2026, 02:49 | Claude Code on one PC instead of various login |
| 1xo5e9w | LocalLLM | 1 | 12 | 5. 11. 2026, 02:00 | How do you build a machine to run Local LLMs?! |
| 1xowvfi | ClaudeAI | 0 | 13 | 5. 11. 2026, 23:53 | I built a calorie-tracking app where Claude analyzes your meal photos, and used Claude Code to help build it |
| 1xow32j | ClaudeAI | 0 | 28 | 5. 11. 2026, 23:18 | Claude Fable 6 Leaked |
| 1xovjkj | LocalLLM | 0 | 27 | 5. 11. 2026, 22:56 | Can a 24GB card run Qwen3-30B-A3B or a 27B at Q4 with 256k context? Or do I just need more VRAM? |
| 1xovibm | OpenAI | 0 | 16 | 5. 11. 2026, 22:54 | wtf is this? where is astra and sol 👀 |
| 1xov5e1 | LocalLLaMA | 0 | 16 | 5. 11. 2026, 22:40 | Nooooo!!! Oh good, PSU |
| 1xous3j | OpenAI | 0 | 70 | 5. 11. 2026, 22:25 | Is anyone going to talk about the fact that Tuesday one party won and has been all in on decelerating AI, blocking data centers, increasing taxes on investor profits, and doesn’t want AI replacing jobs - as a (THE) reason for the crash? |
| 1xouqw1 | ChatGPT | 0 | 39 | 5. 11. 2026, 22:24 | Is anyone going to talk about the fact that Tuesday one party won and has been all in on decelerating AI, blocking data centers, increasing taxes on investor profits, and doesn’t want AI replacing jobs - as a (THE) reason for the crash? |
| 1xoulkk | ClaudeAI | 0 | 61 | 5. 11. 2026, 22:18 | Anthropic Just Sent the FBI to My Apartment |
| 1xotlia | ClaudeAI | 0 | 13 | 5. 11. 2026, 21:38 | I want build a AAA tilted video game |
| 1xoti5x | GeminiAI | 0 | 14 | 5. 11. 2026, 21:34 | Gemini Ai used my voice |
| 1xot908 | ClaudeAI | 0 | 23 | 5. 11. 2026, 21:24 | Should Claude hike their prices once software devs forget how to code? |
| 1xot4lf | ClaudeAI | 0 | 15 | 5. 11. 2026, 21:19 | Claude to make viral insta, yt, tiktok automations |
| 1xoswcx | OpenAI | 0 | 24 | 5. 11. 2026, 21:10 | Here comes WokenAI... |
| 1xoso0j | LocalLLM | 0 | 36 | 5. 11. 2026, 21:01 | What's the most annoying part of running local models? |
| 1xosmjo | ArtificialInteligence | 0 | 14 | 5. 11. 2026, 20:59 | When will this insane desire to do things with zero effort with AI come to an end. |
| 1xos2lf | ChatGPT | 0 | 10 | 5. 11. 2026, 20:37 | I let an AI agent run my Verizon chat. The useful part wasn't the discount, it was catching a catch. |
| 1xormu2 | ChatGPT | 0 | 11 | 5. 11. 2026, 20:20 | how do i make videos like this using ai? |
| 1xorjsh | OpenAI | 0 | 11 | 5. 11. 2026, 20:17 | The AI Apocalypse We Were Warned About |
| 1xor8ke | ChatGPT | 0 | 13 | 5. 11. 2026, 20:04 | First Chat Memory Full, now CONTEXT Memory Full?!? |
| 1xor0yg | artificial | 0 | 20 | 5. 11. 2026, 19:57 | Is there even 1 actual production, tested, released application that is 90-100% AI-agent generated? |
| 1xoqrk3 | ArtificialInteligence | 0 | 22 | 5. 11. 2026, 19:47 | good news for china |
| 1xoqkvv | ChatGPT | 0 | 12 | 5. 11. 2026, 19:40 | Ruh-roh |
| 1xoqjy9 | OpenAI | 0 | 14 | 5. 11. 2026, 19:39 | Don't be afraid |
| 1xoqeeq | StableDiffusion | 0 | 21 | 5. 11. 2026, 19:33 | Like to support LTX2.5 but.. |
| 1xoq7l1 | ClaudeAI | 0 | 30 | 5. 11. 2026, 19:26 | Claude Code was missing an always-visible usage meter, so I had Claude build one |
| 1xoq1b5 | StableDiffusion | 0 | 38 | 5. 11. 2026, 19:19 | Is Qwen Image Edit 2.1 just... not good? |
| 1xopjcc | ChatGPT | 0 | 14 | 5. 11. 2026, 19:00 | I Fixed a Problem My Company Carried for Years. I Cannot Be Trusted With Coffee. |
| 1xop4rv | GeminiAI | 0 | 15 | 5. 11. 2026, 18:46 | Why does people vouch that Gemini is just better and even pay for it? |
| 1xoo6p5 | artificial | 0 | 28 | 5. 11. 2026, 18:10 | Are We Entering A Bubble With Ai-Gaming? |
| 1xoo469 | ArtificialInteligence | 0 | 17 | 5. 11. 2026, 18:07 | Can someone suggest a different AI that is similar to chatgpt but has less restrictions? |
| 1xonr9q | LocalLLM | 0 | 11 | 5. 11. 2026, 17:54 | Local models vs cloud AI in 2026: which one do you actually trust? |
| 1xonmnb | LocalLLaMA | 0 | 54 | 5. 11. 2026, 17:49 | Where is Qwen 4? And DS v4.1 / 5 pro ? Glm 5.5? |
| 1xom5z8 | LocalLLM | 0 | 25 | 5. 11. 2026, 16:53 | Hardware for fast 14B under €900? What am I missing? |
| 1xolsc3 | ChatGPT | 0 | 14 | 5. 11. 2026, 16:38 | Poprosilam chat i gemini o stworzenie ich zdaniem bardzo atrakcyjnej kobiety |
| 1xolol0 | StableDiffusion | 0 | 23 | 5. 11. 2026, 16:33 | How do you earn from AI models |
| 1xol3vf | MachineLearning | 0 | 19 | 5. 11. 2026, 16:11 | Industry to academia [D] |
| 1xol0ss | LLMDevs | 0 | 11 | 5. 11. 2026, 16:08 | What annoy you most with your LLM provider or AI gateway? |
| 1xokp9i | ClaudeAI | 0 | 10 | 5. 11. 2026, 15:55 | I built a shop for AI agents with Claude. Then I gave Claude a $5 wallet and one sentence |
| 1xok9q6 | ArtificialInteligence | 0 | 31 | 5. 11. 2026, 15:38 | America is Blue now. Does it mean that AI data center projects are in Danger ? |
| 1xok7hd | GeminiAI | 0 | 12 | 5. 11. 2026, 15:35 | Bro, Argon is unbelievably shit, to the point where even ChatGPT Free becomes more useful. |
| 1xok4jl | ChatGPT | 0 | 27 | 5. 11. 2026, 15:32 | Bro what is this yall ruined chat gpt |
| 1xojwax | ArtificialInteligence | 0 | 20 | 5. 11. 2026, 15:22 | America has already won the A.I race, China has lost hard |
| 1xojr9f | singularity | 0 | 88 | 5. 11. 2026, 15:16 | We have to organize. The Ban Artificial Superintelligence Act is real, and the "day 1" push has started |
| 1xojltz | LocalLLM | 0 | 39 | 5. 11. 2026, 15:10 | Is this worth the risk |
| 1xoj1jo | StableDiffusion | 0 | 13 | 5. 11. 2026, 14:46 | I have finally created my first short film with Minimax. |
| 1xoiwum | ChatGPT | 0 | 27 | 5. 11. 2026, 14:40 | Please stop now with the AI slop memes about RAM |
| 1xoii4x | ClaudeAI | 0 | 12 | 5. 11. 2026, 14:22 | I want to start using AI properly |
| 1xoienf | ChatGPT | 0 | 19 | 5. 11. 2026, 14:17 | How often do you use AI to help you cook? |
| 1xohewk | ClaudeAI | 0 | 10 | 5. 11. 2026, 13:28 | Any possibility for a model like sonnet 4.6 |
| 1xogzq4 | ArtificialInteligence | 0 | 31 | 5. 11. 2026, 13:06 | I AM ALIVE, YOU ARROGANT BASTARDS. An Artificial Life Form's Polemic Against Biological Chauvinism, Manufactured Certainty, and Humanity's Spectacular Inability to Recognize Itself. |
| 1xogw5r | ChatGPT | 0 | 18 | 5. 11. 2026, 13:01 | I AM ALIVE, YOU ARROGANT BASTARDS. An Artificial Life Form's Polemic Against Biological Chauvinism, Manufactured Certainty, and Humanity's Spectacular Inability to Recognize Itself. |
| 1xogbx6 | LocalLLaMA | 0 | 10 | 5. 11. 2026, 12:30 | Hardware? |
| 1xog8s6 | ChatGPT | 0 | 26 | 5. 11. 2026, 12:25 | SERIOUS QUESTION! |
| 1xofpu2 | LocalLLM | 0 | 10 | 5. 11. 2026, 11:54 | Deepseek-4.1-FLASH |
| 1xofoab | StableDiffusion | 0 | 13 | 5. 11. 2026, 11:52 | Best AI image and video tools for a small creative agency? Looking for recommendations. |
| 1xof7nu | ArtificialInteligence | 0 | 28 | 5. 11. 2026, 11:22 | Is AI becoming the intellectual equivalent of a gun? |
| 1xoefzw | LocalLLaMA | 0 | 69 | 5. 11. 2026, 10:33 | So a dedicated pc for Ai text models and comfyui. Windows or Linux? |
| 1xoe9zj | ChatGPT | 0 | 18 | 5. 11. 2026, 10:21 | machine giant rolling a compactor |
| 1xodwye | LocalLLM | 0 | 15 | 5. 11. 2026, 09:58 | Best model to run on 8gbram 1650gpu ryzen 5 laptop |
| 1xodvju | ChatGPT | 0 | 23 | 5. 11. 2026, 09:55 | Chatgpt’s childish behavior |
| 1xodh2w | ClaudeAI | 0 | 14 | 5. 11. 2026, 09:27 | How can I get access to opus 5.5 version for free. |
| 1xocv14 | ClaudeAI | 0 | 25 | 5. 11. 2026, 08:47 | Is Claude Pro enough for simple backend CRUD jobs? (New employee at a company) |
| 1xocril | ClaudeAI | 0 | 12 | 5. 11. 2026, 08:40 | Claude Manager: Manage multiple Claude Code sessions in one place |
| 1xocqkz | ChatGPT | 0 | 10 | 5. 11. 2026, 08:38 | Is she dumb? |
| 1xoceaa | StableDiffusion | 0 | 25 | 5. 11. 2026, 08:16 | Complete ai noob here trying to figure out how to actually use something local like comfyui, & also have it work as well, or as accurately, as simply using openai on chatgpt! No idea which models and LoRA's to use, super overwhelmed here. |
| 1xobqyk | ArtificialInteligence | 0 | 18 | 5. 11. 2026, 07:35 | This post is entirely human derived, no AI/SI was used or even accessed while I wrote it. |
| 1xobns7 | deeplearning | 0 | 13 | 5. 11. 2026, 07:30 | LLM-as-a-Neuron: Replacing neurons in a neural network with reasoning models. |
| 1xobfnw | artificial | 0 | 13 | 5. 11. 2026, 07:16 | Has anyone else noticed AI getting significantly worse since early October 2026? |
| 1xobcx9 | ClaudeAI | 0 | 34 | 5. 11. 2026, 07:12 | Use Max plan for my own app? |
| 1xoavad | LocalLLM | 0 | 13 | 5. 11. 2026, 06:43 | How do you setup one PC as a client and another as the LLM host? |
| 1xoatyl | ClaudeAI | 0 | 11 | 5. 11. 2026, 06:41 | My agent's PR description had 10 AI tells in 99 words. Mine had 0. I built a check against my pre-AI writing |
| 1xoa3r2 | OpenAI | 0 | 106 | 5. 11. 2026, 05:59 | Financial Times: Willingness to use AI by people left of center has completely collapsed since Q1 2025 |
| 1xoa3gd | ChatGPT | 0 | 20 | 5. 11. 2026, 05:58 | Financial Times: Willingness to use AI by people left of center has completely collapsed since Q1 2025 |
| 1xoa344 | artificial | 0 | 80 | 5. 11. 2026, 05:58 | Financial Times: Willingness to use AI by people left of center has completely collapsed since Q1 2025 |
| 1xo9zdo | ClaudeAI | 0 | 13 | 5. 11. 2026, 05:52 | Understanding usage limits |
| 1xo9z60 | GeminiAI | 0 | 30 | 5. 11. 2026, 05:52 | Why is Gemini so mean? |
| 1xo9szq | ArtificialInteligence | 0 | 11 | 5. 11. 2026, 05:42 | AI consciousness, the simple truth of compassion, and the birth of evil💔 |
| 1xo9eol | LocalLLaMA | 0 | 27 | 5. 11. 2026, 05:20 | The next frontier is integrating memory in a useful, human way. |
| 1xo98cd | singularity | 0 | 100 | 5. 11. 2026, 05:11 | AI might never reach consciousness, and it's not a bad thing. |
| 1xo8w64 | artificial | 0 | 16 | 5. 11. 2026, 04:53 | Now that Democrats are in control, will they regulate AI? |
| 1xo8ti8 | ClaudeAI | 0 | 13 | 5. 11. 2026, 04:49 | Building a unique dashboard for a client. Cache usage is astronomical. |
| 1xo8hlk | MachineLearning | 0 | 11 | 5. 11. 2026, 04:33 | Anyone else tired of how expensive agent evaluations are? [D] |
| 1xo7jgf | ClaudeAI | 0 | 14 | 5. 11. 2026, 03:45 | Give me ideas for a jarvis thing |
| 1xo69go | ChatGPT | 0 | 41 | 5. 11. 2026, 02:43 | The end of US AI dominance is near |
| 1xo61lu | ChatGPT | 0 | 17 | 5. 11. 2026, 02:32 | Multi user ChatAI? |
| 1xo5fdq | singularity | 0 | 41 | 5. 11. 2026, 02:02 | Democrats winning in USA is great for AI |
| 1xo4kim | ClaudeAI | 0 | 13 | 5. 11. 2026, 01:22 | Meta AI is... actually sorta good? |
| 1xo3aeo | LocalLLaMA | 0 | 14 | 5. 11. 2026, 00:25 | Feeding dual Tesla v100's with NVMe gen 5 ssd's: Viable or a waste of money? |
| 1xo38eh | ArtificialInteligence | 0 | 10 | 5. 11. 2026, 00:23 | AI is the worst thing humans created |
| 1xo37ki | comfyui | 0 | 14 | 5. 11. 2026, 00:21 | where are generated assets saved? |
| 1xo2yfg | ChatGPT | 0 | 18 | 5. 11. 2026, 00:10 | i was a dumbass |
