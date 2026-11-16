# AI souhrn z Redditu – 3. 11. 2026

## Metodika

Data pocházejí z Redditu, který pro den 3. 11. 2026 (Europe/Prague) stáhl `scripts/rd-collect-web.py` přímo z webu. K dispozici bylo 40 kandidátů v `candidates.json` a 316 postů s alespoň 10 komentáři v `appendix.json`; skóre a počty komentářů jsou živé hodnoty z doby sběru.

Z výběru bylo vyřazeno 12 kandidátů kvůli opakování témat z posledních tří dnů – zejména weight-space programování GPT-6 Astra, MiniMax H3, sloučení ChatGPT Chatu a Work, výroky Sama Altmana, únik názvů Qwen 4 a domácí GPU rigy. Dalších 9 příspěvků bylo meme, čistě obrázkových nebo mimo AI. Čtyři duplicitní posty byly sloučeny do dvou článků (Dopplerova lokalizace a limity Claude). Výsledkem je 15 článků pokrývajících 19 redditových postů.

Některé externí články nebyly dostupné: NYT vrátil 403 a část médií je za paywallem. U obrázkových a videopostů často chyběl selftext, takže články vycházejí z titulku, dostupného textu a diskuse.

## Články

| # | Téma | Subreddit | Skóre | Komentáře |
|---:|---|---|---:|---:|
| 1 | [Tenhle chlápek přišel na to, jak z jakéhokoliv videa se zvukem zjistit vaši přesnou polohu pomocí Dopplerových křivek okolních letadel](1xmviu5_zvuk-letadel-prozradi-polohu.md) | r/OpenAI | 2332 | 432 |
| 2 | [Humanoidní roboti Xiaomi zachyceni při první 8hodinové směně, kdy třídili díly pro elektromobily rychlostí ~ 1 za minutu](1xn5g1f_xiaomi-humanoidi-osmihodinova-smena.md) | r/singularity | 1337 | 391 |
| 3 | [Britský fintech Revolut snížil náklady na AI programování na desetinu, když vyřadil Claude a přešel na vlastní hosting](1xn568h_revolut-vlastni-glm.md) | r/LocalLLaMA | 1283 | 212 |
| 4 | [RTX 5090 s 64GB a 96GB VRAM „potvrzena“ americkým opravářem GPU](1xmqq2a_rtx-5090-64-96-gb.md) | r/LocalLLaMA | 673 | 143 |
| 5 | [Každému modelu Claude jsem od července 2025 dával úplně stejný prompt. 13 modelů, 14 měsíců, tady je vývoj](1xn6eli_claude-13-modelu-14-mesicu.md) | r/ClaudeAI | 654 | 59 |
| 6 | [Který LLM u vás v poslední době vítězí pro každodenní použití?](1xmgwm1_ktery-llm-pouzivate-denne.md) | r/GeminiAI | 629 | 650 |
| 7 | [Opus 5.5 medium s Blender MCP je při správném promptování neskutečný](1xmcwbt_opus-blender-stredoveka-scena.md) | r/ClaudeAI | 618 | 69 |
| 8 | [Sólový vývojář tohle postavil za 4 dny s Opus 5.5 + Godot. To už je absurdní](1xmdih0_godot-horor-ctyri-dny.md) | r/ClaudeAI | 532 | 167 |
| 9 | [Google vypne vyhledávání školám, které odmítnou A.I.](1xmxcxl_google-skoly-search-ai.md) | r/singularity | 400 | 245 |
| 10 | [Co se to sakra děje s limity](1xmmmte_claude-limity-rychleji.md) | r/ClaudeAI | 378 | 200 |
| 11 | [Celou ulici jsem otexturoval v Blenderu pomocí Qwen Image 2.1, a pak z ní udělal cyberpunkovou, anime a papírovou verzi](1xmg8au_stablegen-qwen-image-ulice.md) | r/StableDiffusion | 377 | 24 |
| 12 | [Anthropic blokuje jakékoliv reverzní inženýrství](1xn2iq3_anthropic-zakaz-rekreace-her.md) | r/ClaudeAI | 292 | 101 |
| 13 | [Co spouštějí lidé s normálním hardwarem: 32GB RAM, 16GB VRAM?](1xn2jyz_modely-32gb-ram-16gb-vram.md) | r/LocalLLaMA | 258 | 258 |
| 14 | [Pomocí Qwen3.8 Flash-Next jsem reverzně analyzoval autorádio s Androidem](1xn2q8a_qwen-autoradio-launcher.md) | r/LocalLLM | 229 | 21 |
| 15 | [Opus 5.5 na kód, Opus 4.6 na nápady a brainstorming](1xmcdri_opus-55-kod-opus-46-ideje.md) | r/ClaudeAI | 210 | 47 |

## Příloha: všechny posty s alespoň 10 komentáři

| ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| [1xmviu5](1xmviu5_zvuk-letadel-prozradi-polohu.md) | r/OpenAI | 2332 | 432 | 3. 11. 2026, 16:12 | This guy figured out how to leak your exact location from any video with sound using the Doppler curves of nearby airplanes |
| [1xn5g1f](1xn5g1f_xiaomi-humanoidi-osmihodinova-smena.md) | r/singularity | 1337 | 391 | 3. 11. 2026, 22:16 | Xiaomi's humanoid robots spotted doing their first 8-hour shift sorting EV parts at a rate of ~ 1 per minute |
| [1xn568h](1xn568h_revolut-vlastni-glm.md) | r/LocalLLaMA | 1283 | 212 | 3. 11. 2026, 22:05 | British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted |
| [1xmvglp](1xmviu5_zvuk-letadel-prozradi-polohu.md) | r/agi | 929 | 240 | 3. 11. 2026, 16:09 | This guy figured out how to leak your exact location from any video with sound using the Doppler curves of nearby airplanes |
| [1xmvlnn](1xmviu5_zvuk-letadel-prozradi-polohu.md) | r/ArtificialInteligence | 880 | 164 | 3. 11. 2026, 16:15 | This guy figured out how to leak your exact location from any video with sound using the Doppler curves of nearby airplanes |
| 1xmitzx | r/LocalLLaMA | 877 | 131 | 3. 11. 2026, 04:55 | Alibaba's Qwen Code repo just leaked qwen4-max, qwen4-coder-plus, and qwen4-omni-120b |
| 1xmzcjz | r/ClaudeAI | 787 | 102 | 3. 11. 2026, 18:32 | Nobody else seems to have as hard of a time with Claude as I do. I just want to understand why Claude hates me. |
| 1xmt4nj | r/OpenAI | 727 | 84 | 3. 11. 2026, 14:37 | GPT-6 successfully performed "brain surgery" on another AI to make it smarter |
| [1xmqq2a](1xmqq2a_rtx-5090-64-96-gb.md) | r/LocalLLaMA | 673 | 143 | 3. 11. 2026, 12:40 | RTX 5090 with 64GB and 96GB VRAM 'confirmed' by US GPU repair tech |
| [1xn6eli](1xn6eli_claude-13-modelu-14-mesicu.md) | r/ClaudeAI | 654 | 59 | 3. 11. 2026, 22:54 | I gave every Claude model the exact same prompt since July 2025. 13 models, 14 months, here's the evolution |
| [1xmgwm1](1xmgwm1_ktery-llm-pouzivate-denne.md) | r/GeminiAI | 629 | 650 | 3. 11. 2026, 03:22 | Which LLM is Winning Your Daily use Case Lately? |
| [1xmcwbt](1xmcwbt_opus-blender-stredoveka-scena.md) | r/ClaudeAI | 618 | 69 | 3. 11. 2026, 00:21 | Opus 5.5 medium with blender mcp is insane with the right prompting |
| 1xmesfd | r/singularity | 610 | 178 | 3. 11. 2026, 01:44 | Seems weight space programming is an emergent capability on new fronteir models |
| 1xmw7io | r/singularity | 593 | 36 | 3. 11. 2026, 16:37 | Im calling this the Altman Trap |
| 1xmx22x | r/OpenAI | 555 | 152 | 3. 11. 2026, 17:09 | Sorry, my agents accidentally did it |
| [1xmdih0](1xmdih0_godot-horor-ctyri-dny.md) | r/ClaudeAI | 532 | 167 | 3. 11. 2026, 00:47 | A Solo Developer Built This in 4 Days With Opus 5.5 + Godot. This Is Getting Ridiculous |
| 1xmjd9k | r/ArtificialInteligence | 494 | 15 | 3. 11. 2026, 05:23 | ChatGPT rejected my meme |
| 1xmz9ca | r/LocalLLaMA | 477 | 65 | 3. 11. 2026, 18:29 | Like GPT-6 Astra, Qwen 3.8 27B can interpret model weights |
| 1xmmi1i | r/GeminiAI | 445 | 33 | 3. 11. 2026, 08:20 | Gemini Aron |
| 1xmsj6n | r/LocalLLM | 441 | 69 | 3. 11. 2026, 14:10 | The Inference Wall |
| 1xmnxbx | r/ArtificialInteligence | 401 | 36 | 3. 11. 2026, 09:52 | Happy birthday kiddo here’s $15 of chatgpt ! |
| [1xmxcxl](1xmxcxl_google-skoly-search-ai.md) | r/singularity | 400 | 245 | 3. 11. 2026, 17:20 | Google Will Turn Off Search for Schools That Reject A.I. |
| 1xmzjxa | r/ArtificialInteligence | 392 | 25 | 3. 11. 2026, 18:40 | Entire world to Sam Altman right now |
| [1xmmmte](1xmmmte_claude-limity-rychleji.md) | r/ClaudeAI | 378 | 200 | 3. 11. 2026, 08:28 | What the hel is happening with limits |
| [1xmg8au](1xmg8au_stablegen-qwen-image-ulice.md) | r/StableDiffusion | 377 | 24 | 3. 11. 2026, 02:51 | I textured an entire street in Blender with Qwen Image 2.1, then made cyberpunk, anime and papercraft versions of it |
| 1xmnb1w | r/StableDiffusion | 306 | 56 | 3. 11. 2026, 09:12 | H3 Long-Gen with Qwen 3.8 Flash Next prompting every 18sec went in a really wild direction (2min14s) |
| [1xn2iq3](1xn2iq3_anthropic-zakaz-rekreace-her.md) | r/ClaudeAI | 292 | 101 | 3. 11. 2026, 20:26 | Anthropic Blocking Reverse Engineer Anything |
| [1xmohxq](1xmmmte_claude-limity-rychleji.md) | r/ClaudeAI | 271 | 184 | 3. 11. 2026, 10:27 | I'm worried Claude will become less and less useful for what I use it for. |
| 1xmw01o | r/agi | 267 | 114 | 3. 11. 2026, 16:29 | Sorry, my agents accidentally did it |
| [1xn2jyz](1xn2jyz_modely-32gb-ram-16gb-vram.md) | r/LocalLLaMA | 258 | 258 | 3. 11. 2026, 20:28 | What do people with normal hardware : 32GB ram 16GB VRAM run? |
| [1xn26ml](1xmviu5_zvuk-letadel-prozradi-polohu.md) | r/singularity | 258 | 31 | 3. 11. 2026, 20:14 | This guy figured out how to leak your exact location from any video with sound using the Doppler curves of nearby airplanes |
| 1xmzwfo | r/LocalLLM | 249 | 81 | 3. 11. 2026, 18:52 | Claude was laid off |
| 1xmknhl | r/ClaudeAI | 248 | 17 | 3. 11. 2026, 06:31 | GTA VI - I had Claude 5.5 help me build a GTA VI Vice City style 3D pixel diorama, and I'm obsessed with the neon glow. 🌴🌆 |
| 1xmfbam | r/LocalLLaMA | 238 | 57 | 3. 11. 2026, 02:08 | I found another niche use case for local LLMs, but need some advice |
| 1xn1gs9 | r/LocalLLaMA | 233 | 46 | 3. 11. 2026, 19:48 | I tried MIT's "weight-space programming" on my own use case: Claude rewrote 8 neurons of Gemma 4 12B to change how it translates one Italian tense |
| [1xn2q8a](1xn2q8a_qwen-autoradio-launcher.md) | r/LocalLLM | 229 | 21 | 3. 11. 2026, 20:34 | I used Qwen3.8 Flash-Next to reverse-engineer an Android car stereo |
| 1xmm9uk | r/StableDiffusion | 227 | 58 | 3. 11. 2026, 08:06 | Flip a switch and stop your Videos from Degrading. 50 Clip Test No Degrading at the end. Geiru Context Suite |
| 1xmowkr | r/ChatGPT | 216 | 169 | 3. 11. 2026, 10:53 | People who say they already got ChatGPT's chat and work merge keep reporting the same things. Here's what I'd save before it reaches your account |
| [1xmcdri](1xmcdri_opus-55-kod-opus-46-ideje.md) | r/ClaudeAI | 210 | 47 | 3. 11. 2026, 00:00 | Opus 5.5 for code, Opus 4.6 for ideas and brainstorming |
| 1xmt1y0 | r/agi | 208 | 101 | 3. 11. 2026, 14:34 | GPT-6 successfully performed "brain surgery" on another AI to make it smarter |
| 1xmvgxx | r/singularity | 207 | 45 | 3. 11. 2026, 16:10 | Fable 5.5 vs GPT 6.2 Astra -  SVG of a PS5 Controller |
| 1xn7jti | r/ClaudeAI | 202 | 19 | 3. 11. 2026, 23:40 | From a notebook sketch to an animated Godot boss — 3D AI + Opus 5.5 |
| 1xmuct5 | r/singularity | 200 | 30 | 3. 11. 2026, 15:27 | Skyfall AI demonstrates SKY-001, an engineering world model that reconstructs a Jaguar car with thousands of 3D parts. The company also reports matching GPT-6 Astra's CAD accuracy while running 51× faster and costing 150× less. |
| 1xn6tu3 | r/ClaudeAI | 198 | 17 | 3. 11. 2026, 23:10 | I gave Claude ~700 ransomware encrypted files. It told me upfront it couldn't decrypt them, then got two thirds of them usable again |
| 1xn2du1 | r/GeminiAI | 196 | 28 | 3. 11. 2026, 20:21 | Does Gemini hate me? |
| 1xn3cwl | r/singularity | 194 | 62 | 3. 11. 2026, 20:57 | OpenAI's New Internal Models' Performance on Real-World Hardware Engineering Tasks |
| 1xmp6dh | r/comfyui | 189 | 28 | 3. 11. 2026, 11:10 | I built a free, open-source film studio on top of ComfyUI + MiniMax H3: idea to finished short film, on your own PC |
| 1xmxb6g | r/singularity | 189 | 16 | 3. 11. 2026, 17:18 | The 'Astra can read and write weights to improve Qwen' post is misleading |
| 1xn7rfh | r/LocalLLaMA | 177 | 34 | 3. 11. 2026, 23:48 | [llama.cpp fork]: QFN + [specific quant] + [ultra specific hardware config] = [incredible and irreproducible pp and tg] |
| 1xn10sg | r/singularity | 174 | 32 | 3. 11. 2026, 19:32 | DeepMind employees say lifetime restrictions on criticizing Google stop them speaking publicly about AI safety and impact |
| 1xn36d1 | r/OpenAI | 173 | 39 | 3. 11. 2026, 20:50 | GPT 6.2 Astra , GPT 6.2 sol |
| 1xmmadn | r/LocalLLaMA | 173 | 30 | 3. 11. 2026, 08:07 | DeepSeek V5 is planned to be pre-trained on Huawei Ascend chips. |
| 1xn3roz | r/singularity | 172 | 23 | 3. 11. 2026, 21:12 | First in a human: gene therapy fixed a one-letter DNA typo inside one patient's liver to treat alpha-1 antitrypsin deficiency, an inherited disease that damages the liver and lungs. The patient now makes the working protein, and no unwanted edits were found. New hope for avoiding a liver transplant. |
| 1xmyovx | r/comfyui | 164 | 34 | 3. 11. 2026, 18:09 | New image model based on Minimax H3, 7× smaller, 5× faster, 8 steps |
| 1xn3cr5 | r/ClaudeAI | 163 | 16 | 3. 11. 2026, 20:57 | The Binance theft started as a coding assignment. I’ve been sent the same kind of repo all year. All were exploits. |
| 1xmp7b1 | r/singularity | 162 | 158 | 3. 11. 2026, 11:11 | I remembered Alan’s countdown - it says there’s 1% left until AGI. What do you think? |
| 1xmmo2y | r/ArtificialInteligence | 159 | 93 | 3. 11. 2026, 08:30 | Is this news true? |
| 1xn0e12 | r/ClaudeAI | 155 | 71 | 3. 11. 2026, 19:10 | I tried to make Opus 5.5 cheaper with a cheap coding subagent, but It got worse and more expensive |
| 1xmsvfa | r/ChatGPT | 152 | 165 | 3. 11. 2026, 14:26 | Done with ChatGPT |
| 1xmq2y4 | r/OpenAI | 150 | 81 | 3. 11. 2026, 12:03 | What's the deal with all these RAM memes? |
| 1xms9ii | r/LocalLLaMA | 150 | 29 | 3. 11. 2026, 13:58 | What Qwen is thinking when it gets stuck saying "Wait" |
| 1xmjipa | r/LocalLLaMA | 141 | 111 | 3. 11. 2026, 05:31 | Underrated benefit of Local AI: Speed |
| 1xn5piy | r/singularity | 135 | 12 | 3. 11. 2026, 22:26 | British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted |
| 1xn1mep | r/StableDiffusion | 126 | 20 | 3. 11. 2026, 19:54 | PrunaAI/P-H3-Image-Comfy · Hugging Face |
| 1xn22y7 | r/artificial | 125 | 43 | 3. 11. 2026, 20:10 | Google to shut off search for schools that opt-out of AI |
| 1xmv551 | r/OpenAI | 124 | 28 | 3. 11. 2026, 15:57 | How OpenAI Cofounder Greg Brockman’s Wife Anna Became a Trump and MAGA Mega-Donor |
| 1xmszyq | r/LocalLLM | 120 | 51 | 3. 11. 2026, 14:31 | Rant: The lack of appreciation for shit you get for free |
| 1xmgmd8 | r/LocalLLaMA | 117 | 52 | 3. 11. 2026, 03:09 | Rtx 8000 48gb prices have decreased over the last two years while 3090 doubled. |
| 1xms6eq | r/LocalLLaMA | 110 | 190 | 3. 11. 2026, 13:53 | Is Qwen 3.8 27B still the king |
| 1xn50x4 | r/ChatGPT | 108 | 79 | 3. 11. 2026, 22:00 | ChatGPT limiting image generation now |
| 1xn5cfw | r/StableDiffusion | 105 | 40 | 3. 11. 2026, 22:12 | Electricity per AI image on an RTX PRO 6000, RTX 5090 Laptop, RTX 5080, RTX 3090 and more: about 3 to 10 cents per 1,000 images (FLUX.2 klein, 1024x1024) |
| 1xmo5xu | r/LocalLLaMA | 103 | 30 | 3. 11. 2026, 10:06 | [Paper] Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights |
| 1xmqbyu | r/StableDiffusion | 102 | 49 | 3. 11. 2026, 12:18 | Black Forest Labs updated Flux.3 Image Klein documentation to clarify that its primarily designed for image editing. |
| 1xmdjjy | r/StableDiffusion | 99 | 109 | 3. 11. 2026, 00:49 | Looking for a fast, smart uncensored LLM for prompt generation on RTX 5070 Ti (16GB VRAM)? |
| 1xn40w7 | r/LocalLLaMA | 98 | 21 | 3. 11. 2026, 21:21 | Tokens/s? "World's biggest PCIe graphics card" discovered, prototype AMD Radeon RX 470 board with four GPUs has been pictured |
| 1xmnxtj | r/comfyui | 96 | 12 | 3. 11. 2026, 09:53 | We open-sourced our video app that runs on your ComfyUI (H3 VFX LoRAs, Qwen, Flux) |
| 1xmjhtd | r/ClaudeAI | 94 | 47 | 3. 11. 2026, 05:30 | How to start "Obsidian + ClaudeAI" |
| 1xmuowj | r/StableDiffusion | 94 | 19 | 3. 11. 2026, 15:40 | Reshoot 4D: Reshoot Anyone in 4D |
| 1xmdwop | r/ClaudeAI | 89 | 22 | 3. 11. 2026, 01:03 | Official Claude Code Extension Compromise: Security Advisory |
| 1xmfdgq | r/LocalLLM | 86 | 94 | 3. 11. 2026, 02:11 | Buy 32GB RAM right now? |
| 1xmh3xy | r/ChatGPT | 82 | 83 | 3. 11. 2026, 03:32 | Chat is now just another AI assistant |
| 1xn7qoo | r/singularity | 82 | 23 | 3. 11. 2026, 23:48 | Ai 2027 authors mentioning we’ll hit ASI sooner than Ai 2027 predicted |
| 1xn53eb | r/ClaudeAI | 77 | 11 | 3. 11. 2026, 22:02 | Saying the safeguard reason will trigger the safeguard |
| 1xmolk6 | r/LocalLLaMA | 75 | 66 | 3. 11. 2026, 10:33 | Qwen3.8-Flash-Next (local) vs Claude |
| 1xn4qn1 | r/LocalLLaMA | 74 | 37 | 3. 11. 2026, 21:49 | Basalt 0.2.0: Qwen 3.8 Flash Next NVFP4, 300 t/s prose, 600 t/s struct, 10K t/s prefill on a 5090 + 5060 Ti and 128GB RAM |
| 1xmuea8 | r/StableDiffusion | 73 | 29 | 3. 11. 2026, 15:28 | SPEEDing up more than just MiniMax-H3 without retraining - now a drop-in KSampler replacement for image, edit and video models (with evidence this time) |
| 1xmk8rx | r/MachineLearning | 72 | 11 | 3. 11. 2026, 06:09 | We turned 10 years of ML papers into one page per topic: benchmark records, what got tried, what reviewers expect [P] |
| 1xmh012 | r/ClaudeAI | 65 | 17 | 3. 11. 2026, 03:27 | Anthropic added “message threads” to the Messages API (public beta): send the conversation once, then only new messages. Already on by default in Claude Code |
| 1xmvn4q | r/LocalLLaMA | 65 | 10 | 3. 11. 2026, 16:16 | Four open coding models, prompted to finish an upload URL - analysis |
| 1xmqc97 | r/singularity | 63 | 18 | 3. 11. 2026, 12:18 | LLMs are fantastic Tech Supports |
| 1xmgwz0 | r/ChatGPT | 57 | 68 | 3. 11. 2026, 03:23 | Why does ChatGPT always ask me if I’m going to hurt myself? |
| 1xmt6kb | r/LocalLLaMA | 54 | 118 | 3. 11. 2026, 14:39 | Strata is the shit |
| 1xn2i0n | r/LocalLLaMA | 54 | 10 | 3. 11. 2026, 20:26 | DeepSeek V4.1 Flash 1017 can also do Weight-Space Programming |
| 1xmwryg | r/LocalLLaMA | 53 | 105 | 3. 11. 2026, 16:59 | We’re the product team at Reflection, the lab behind Beam — Ask Us Anything! |
| 1xmtn3k | r/artificial | 53 | 58 | 3. 11. 2026, 14:59 | ok AI assistants are getting kinda out of hand |
| 1xn7kpk | r/ClaudeAI | 52 | 44 | 3. 11. 2026, 23:41 | What level are you on ? |
| 1xmiwkh | r/LocalLLM | 51 | 19 | 3. 11. 2026, 04:59 | DeepSeek V4.1 Flash (552B) on a used Dell R820 from 2012: 10 tok/s decode, 100 tok/s prefill |
| 1xml0js | r/GeminiAI | 49 | 60 | 3. 11. 2026, 06:52 | While Carbon is off limits for most of us, what has Gemini 4 Argon already done well for you? |
| 1xn7jo1 | r/ChatGPT | 46 | 65 | 3. 11. 2026, 23:40 | Does your ChatGPT use emojis with you when it’s responding to you? |
| 1xme6c5 | r/LocalLLaMA | 46 | 18 | 3. 11. 2026, 01:15 | LFM3-1.7B quantization report: 3.6 GB VRAM lossless; 2.2 GB with modest degradation |
| 1xn0tde | r/StableDiffusion | 46 | 18 | 3. 11. 2026, 19:24 | Where did the MEAT PROXIES GO? |
| 1xmitnt | r/GeminiAI | 41 | 63 | 3. 11. 2026, 04:55 | Damn... they added a limit |
| 1xn145z | r/StableDiffusion | 40 | 19 | 3. 11. 2026, 19:36 | I trained and released a Pose Control LoRA for Krea-2 |
| 1xmllmx | r/StableDiffusion | 38 | 15 | 3. 11. 2026, 07:25 | The Wall Street Journal Style-A Krea 2 LoRA |
| 1xmkk63 | r/artificial | 37 | 11 | 3. 11. 2026, 06:26 | Marvell inks record-breaking $115B AI deal |
| 1xmfcf6 | r/ChatGPT | 36 | 49 | 3. 11. 2026, 02:09 | work + chat combined usage allowance |
| 1xmxn2u | r/LLMDevs | 36 | 15 | 3. 11. 2026, 17:30 | Prompt caching patterns across major LLM providers look very different |
| 1xmgs3m | r/ClaudeAI | 33 | 61 | 3. 11. 2026, 03:16 | Freudian slip? |
| 1xmss5o | r/artificial | 32 | 27 | 3. 11. 2026, 14:22 | To the companies building AI: the cheapest day to pay for the damage is today |
| 1xmwoy8 | r/singularity | 30 | 154 | 3. 11. 2026, 16:56 | The "AI is fancy autocomplete" vs. "Imminent RSI/AGI" argument. |
| 1xmuddx | r/ChatGPT | 30 | 31 | 3. 11. 2026, 15:28 | Hot take: with the new usage limits, your 80-message ChatGPT thread is now your most expensive habit |
| 1xmexvp | r/GeminiAI | 30 | 29 | 3. 11. 2026, 01:51 | What have they done to make Gemini this stupid |
| 1xn1n5b | r/ArtificialInteligence | 29 | 169 | 3. 11. 2026, 19:55 | If AI causes mass unemployment, who will have the money to pay for goods and services? |
| 1xn2szj | r/ChatGPT | 29 | 45 | 3. 11. 2026, 20:37 | ChatGPT is suddenly restricted from making election predictions. |
| 1xmtlm7 | r/LocalLLaMA | 29 | 13 | 3. 11. 2026, 14:57 | balbal-v2: Turkish speech recognition that runs on CPU, 2nd on Mu-Bench TR after Google Chirp 3 |
| 1xmgzia | r/ClaudeAI | 28 | 13 | 3. 11. 2026, 03:26 | How Claude Code reacts when a repo has a no-AI contribution policy |
| 1xn1q5g | r/LocalLLM | 27 | 91 | 3. 11. 2026, 19:58 | Is running a local AI actually worth it? I'd love to hear about your experience! |
| 1xmhhdk | r/LocalLLM | 27 | 17 | 3. 11. 2026, 03:50 | AI Agent Task performance of small LLM models (4B and below) in self-assessment set |
| 1xn3n5x | r/ChatGPT | 27 | 13 | 3. 11. 2026, 21:07 | POV you are too stupid, so you use AI to reboot a server |
| 1xmv9ju | r/LocalLLaMA | 26 | 50 | 3. 11. 2026, 16:02 | Has anyone done a in-depth comparison between Qwen-3.8 27b @ 8bpw and Qwen-3.8-FN @ 4bpw? |
| 1xmhrd7 | r/ClaudeAI | 24 | 39 | 3. 11. 2026, 04:03 | a Mac DAW where Claude can run the whole session, using Claude Code |
| 1xmwav5 | r/ChatGPT | 24 | 33 | 3. 11. 2026, 16:41 | Has using AI as a thinking partner changed the way you communicate with people? |
| 1xmrzsf | r/ClaudeAI | 24 | 12 | 3. 11. 2026, 13:45 | 560 commits with claude in two weeks: "Weave all together" |
| 1xmxxg2 | r/ChatGPT | 23 | 99 | 3. 11. 2026, 17:41 | Solo dev on a tight budget: is the Claude $100 plan worth it, or should I look at ChatGPT instead? |
| 1xmocac | r/ChatGPT | 23 | 21 | 3. 11. 2026, 10:18 | "Context window exhausted/full"? |
| 1xmn0l8 | r/artificial | 23 | 12 | 3. 11. 2026, 08:53 | UK High Court records a non-existent case citation in its 2026 judgment |
| 1xmnkkt | r/LocalLLM | 20 | 11 | 3. 11. 2026, 09:29 | Trying "Weight-Space Programming" on a local 35B GGUF to fix agent loops |
| 1xmnkqf | r/LocalLLM | 19 | 101 | 3. 11. 2026, 09:29 | So everybody here have top tier customer hardware? Rant |
| 1xmzyv2 | r/StableDiffusion | 19 | 11 | 3. 11. 2026, 18:55 | Generation result in Minimax H3 on an RTX 4060 8GB with 16GB of RAM (showcase) |
| 1xmfz5s | r/ArtificialInteligence | 17 | 43 | 3. 11. 2026, 02:39 | Can someone explain to me where “there” is when they talk about who will get “there” first in the race to AI? |
| 1xms8nm | r/ChatGPT | 17 | 21 | 3. 11. 2026, 13:56 | Surprised about changing minds on Claude |
| 1xn74pn | r/StableDiffusion | 16 | 12 | 3. 11. 2026, 23:22 | Open-source local "Higgsfield" on ComfyUI, update: restore old footage, train your character in the UI, 60+ tools (Krea 2,  FLUX.2, FLUX 3 Klein, LTX-2.5, Wan 2.2, SeedVR2) |
| 1xn1gfm | r/ChatGPT | 15 | 17 | 3. 11. 2026, 19:48 | ChatGPT knows your location regardless of permissions |
| 1xmp6kt | r/ClaudeAI | 15 | 10 | 3. 11. 2026, 11:10 | I built an open-source tool that lets Claude Code make Screen Studio-quality screen recordings |
| 1xmcibh | r/LocalLLaMA | 14 | 14 | 3. 11. 2026, 00:05 | [GPU Lawyer] Deepseek 4.1 Flash 1018 on 4 32GB V100s -- pushing 40 tok/s decode, and will test across 8 v100s next. |
| 1xmo41i | r/LocalLLM | 14 | 14 | 3. 11. 2026, 10:03 | Local LLM recommendations for coding and agentic workflows (RTX 5060 Ti 16GB) |
| 1xn1e0h | r/StableDiffusion | 14 | 14 | 3. 11. 2026, 19:46 | Best model for anthro and anime? |
| 1xmkuxc | r/StableDiffusion | 14 | 13 | 3. 11. 2026, 06:43 | Genjutsu but it's local. Supports multiple subjects + multiple cuts. All inside Director's Cut, try Second Take now. |
| 1xmxr1q | r/LocalLLaMA | 13 | 80 | 3. 11. 2026, 17:34 | Claude Code enjoyer wanting to go local. What would your newbie harness of choice be? |
| 1xmgx79 | r/AIAssisted | 13 | 15 | 3. 11. 2026, 03:23 | How do I get started automating everyday tasks with AI? |
| 1xn361o | r/ChatGPT | 13 | 11 | 3. 11. 2026, 20:50 | Things to do with free access to Premium ChatGPT |
| 1xmwur0 | r/singularity | 12 | 19 | 3. 11. 2026, 17:01 | r/Singularity Daily Discussion Thread — November 03, 2026 |
| 1xmq913 | r/LocalLLaMA | 12 | 14 | 3. 11. 2026, 12:13 | Olla v0.1.0 - Lightweight open-source LLM proxy for homelabs & on-prem inference (Ollama, vLLM, SGLang, llama.cpp, oMLX with failover, sticky sessions & load balancing) |
| 1xmyrrj | r/ChatGPT | 12 | 13 | 3. 11. 2026, 18:12 | Custom GPTs stop working Dec 11. what actually happens to the chats you had with them |
| 1xn6ew2 | r/ArtificialInteligence | 11 | 37 | 3. 11. 2026, 22:54 | This is just hilarious |
| 1xmsgz5 | r/LocalLLaMA | 11 | 33 | 3. 11. 2026, 14:07 | preserve_thinking off is FINE |
| 1xmv2et | r/ChatGPT | 11 | 26 | 3. 11. 2026, 15:54 | What's your 'non common' ChatGPT practice? |
| 1xmwj8g | r/ChatGPT | 11 | 25 | 3. 11. 2026, 16:50 | Now that Sora is not available, what are you guys using? |
| 1xme97q | r/ChatGPT | 11 | 22 | 3. 11. 2026, 01:19 | Questions pertaining to the upcoming work and chat integration. |
| 1xmsjk4 | r/ClaudeAI | 11 | 17 | 3. 11. 2026, 14:10 | Claude Code leads to more Claude Code |
| 1xn1av3 | r/ChatGPT | 11 | 16 | 3. 11. 2026, 19:42 | Should I turn on the memory setting? |
| 1xmtks0 | r/StableDiffusion | 11 | 16 | 3. 11. 2026, 14:56 | Ideogram 4: FP8 vs INT8 for Quality and Speed? (Slow Internet Link) |
| 1xmkqpe | r/StableDiffusion | 11 | 15 | 3. 11. 2026, 06:36 | What can I use to extend videos past 15 seconds on Minimax H3 ref2va? |
| 1xmpwyu | r/LLMDevs | 11 | 10 | 3. 11. 2026, 11:54 | Coding agents: cache price matters more than input price |
| 1xmo3jb | r/ClaudeAI | 10 | 89 | 3. 11. 2026, 10:02 | green flag, red flag, or doesn’t matter: being mean to claude? |
| 1xmn6qp | r/ClaudeAI | 10 | 37 | 3. 11. 2026, 09:04 | Is Sonnet actually any worse at executing tasks than Opus? |
| 1xmv6gp | r/LocalLLM | 10 | 28 | 3. 11. 2026, 15:59 | Polystrata - best coding LLM for my setup? |
| 1xn451t | r/ClaudeAI | 10 | 25 | 3. 11. 2026, 21:26 | Watermark Key and Universities |
| 1xn4n3j | r/LocalLLaMA | 10 | 18 | 3. 11. 2026, 21:45 | Harnesses/Agents suited for linux sysadmin, system maintenance, network and light coding. |
| 1xmojdg | r/OpenAI | 10 | 12 | 3. 11. 2026, 10:30 | 371 AI chatbot requests, 3.7M tokens, $1.04 total (ChatGPT Luna 5.6) |
| 1xmukz1 | r/comfyui | 10 | 12 | 3. 11. 2026, 15:35 | I built a ComfyUI prompt enhancer that runs a small local LLM without permanently occupying your VRAM |
| 1xn4rbk | r/ChatGPT | 10 | 10 | 3. 11. 2026, 21:50 | Image generation : poor rendering |
| 1xmtmge | r/ClaudeAI | 9 | 38 | 3. 11. 2026, 14:58 | Switching from Codex to Claude Code - any tips on initial setup and keeping usage under control? |
| 1xmnepj | r/LocalLLaMA | 9 | 24 | 3. 11. 2026, 09:18 | Best ASR & TTS models to date to use locally |
| 1xmd9aw | r/LocalLLaMA | 8 | 63 | 3. 11. 2026, 00:36 | Follow up on "Is it time to jump ship from OpenCode? " |
| 1xmzcut | r/ClaudeAI | 8 | 12 | 3. 11. 2026, 18:33 | How did you get better at building agentic systems? What helped most? |
| 1xmipdg | r/ChatGPT | 7 | 114 | 3. 11. 2026, 04:49 | AI and soul |
| 1xmtmw0 | r/ArtificialInteligence | 7 | 52 | 3. 11. 2026, 14:58 | What leverage could humans have over a superintelligent AI that's smarter than us? |
| 1xmnjdu | r/LocalLLaMA | 7 | 40 | 3. 11. 2026, 09:27 | Best reliable, affordable PCIe 4.0 risers for 4× RTX 3090 inference setup? |
| 1xmtzez | r/StableDiffusion | 7 | 31 | 3. 11. 2026, 15:12 | RTX 3090 |
| 1xmds0b | r/ChatGPT | 7 | 28 | 3. 11. 2026, 00:59 | if you think Sam Altman is still a good guy just google Suchir Balaji |
| 1xmy9nu | r/ClaudeAI | 7 | 28 | 3. 11. 2026, 17:54 | Claude pro average user consumption |
| 1xn635z | r/ChatGPT | 7 | 27 | 3. 11. 2026, 22:41 | The ChatGPT Business Promo for a free Standard seat is ending this week |
| 1xmw8xv | r/GeminiAI | 7 | 17 | 3. 11. 2026, 16:39 | Curious what people do daily with Gemini pro daily |
| 1xmze1m | r/LocalLLaMA | 7 | 16 | 3. 11. 2026, 18:34 | How did you get better at building agentic systems? What helped most? |
| 1xn2j0f | r/ClaudeAI | 7 | 15 | 3. 11. 2026, 20:27 | Claude as orchestrator, cheaper model for the grunt work? |
| 1xn0sqg | r/ChatGPT | 7 | 11 | 3. 11. 2026, 19:24 | Do you build it or do you purchase it? |
| 1xmsv6m | r/LocalLLaMA | 6 | 34 | 3. 11. 2026, 14:25 | Are there any faster unified memory options that aren't Mac? |
| 1xmfp1b | r/ClaudeAI | 6 | 21 | 3. 11. 2026, 02:26 | Tablet Running Claude |
| 1xn3pnn | r/singularity | 6 | 20 | 3. 11. 2026, 21:10 | What happened to Science Fiction? |
| 1xmpvcq | r/comfyui | 6 | 14 | 3. 11. 2026, 11:51 | Krea 2 General Edit V2 – what results are people actually getting? |
| 1xmnnch | r/ChatGPT | 6 | 11 | 3. 11. 2026, 09:34 | What's the point of a banked reset if it also resets your weekly limit? ChatGPT/CODEX |
| 1xmss97 | r/LocalLLM | 5 | 53 | 3. 11. 2026, 14:22 | Cannot decide what GPUs to buy |
| 1xmpfyv | r/LocalLLM | 5 | 41 | 3. 11. 2026, 11:26 | V100 HBM2 PCIE 32GB for 1000 euros, worth it? |
| 1xmdoc2 | r/ClaudeAI | 5 | 20 | 3. 11. 2026, 00:55 | Pro to Max: At what point did you finally pull the trigger? What’s your story? |
| 1xmju2q | r/ClaudeAI | 5 | 19 | 3. 11. 2026, 05:47 | How to get claude to make proper a UI? |
| 1xmotl3 | r/LocalLLaMA | 5 | 18 | 3. 11. 2026, 10:48 | Those of you who develop or make changes to local inference engines, how do you safeguard models from their own internal tokens? |
| 1xmqefq | r/StableDiffusion | 5 | 16 | 3. 11. 2026, 12:22 | I trained rawsnap v3 (LoKr) for Krea 2 on 749 images and can't pick the best epoch — help me vote (public, no login) |
| 1xmyf4q | r/ChatGPT | 5 | 14 | 3. 11. 2026, 17:59 | Subjectively, can you estimate how much money you need to pay to buy tokens to cover the same 5-hour limit as in the plus model. |
| 1xme91e | r/ArtificialInteligence | 5 | 11 | 3. 11. 2026, 01:19 | Any good AI courses ? |
| 1xn11wd | r/LocalLLaMA | 5 | 10 | 3. 11. 2026, 19:33 | I compared 4 decision-model leaderboards. Fine-tuning beats size under 5B, Arabic collapses below 1B, and the leaderboards don’t agree on #1 [OC] |
| 1xmpadq | r/StableDiffusion | 5 | 10 | 3. 11. 2026, 11:16 | Tips / settings for better results with MOSS-Image Base + Turbo LoRAs? (blur / out-of-focus / smoothness issues) |
| 1xmtgcd | r/ClaudeAI | 4 | 76 | 3. 11. 2026, 14:51 | Anthropic updated its S1 this morning: "we may imminently meet our definition of 'dramatically accelerated progress attributable to AI." ... "we do not anticipate being able to safely use Claude to fully autonomously design successive generations of frontier models" |
| 1xmtigw | r/OpenAI | 4 | 31 | 3. 11. 2026, 14:53 | Which model is the most balanced in terms of token consumption and doing the work correctly? |
| 1xmrajo | r/ChatGPT | 4 | 30 | 3. 11. 2026, 13:09 | I wanna wear my self off chatgpt but don't know how |
| 1xn25va | r/StableDiffusion | 4 | 27 | 3. 11. 2026, 20:13 | Photo restoration |
| 1xmzp2n | r/ClaudeAI | 4 | 25 | 3. 11. 2026, 18:45 | How do you keep track of multiple coding agents running in parallel? |
| 1xn10t0 | r/LocalLLM | 4 | 23 | 3. 11. 2026, 19:32 | Is it really hard to build PC myself if I never did it? |
| 1xmo1r0 | r/ChatGPT | 4 | 22 | 3. 11. 2026, 10:00 | Burning through my $100 Codex plan in 2 days. Any advice? What about free resets ? Also considering Claude Code |
| 1xmf7dx | r/artificial | 4 | 18 | 3. 11. 2026, 02:03 | Designers, how do you... work? |
| 1xn1flh | r/LocalLLM | 4 | 17 | 3. 11. 2026, 19:47 | Recommendation for GPU (cheap as possible) |
| 1xn7prx | r/LocalLLaMA | 4 | 15 | 3. 11. 2026, 23:47 | Keep CMP 170 or sell for upgrades? |
| 1xmrjfi | r/ClaudeAI | 4 | 14 | 3. 11. 2026, 13:22 | before starting a project in Claude Code I tried to get a free prototype out of 5 AI app builders first |
| 1xms13n | r/LocalLLM | 4 | 12 | 3. 11. 2026, 13:46 | [Build Advice] Is this €2,000 workstation worth it for local LLM inference and AI workloads? |
| 1xmfkfx | r/ArtificialInteligence | 4 | 11 | 3. 11. 2026, 02:20 | Epistemically Isolated Artificial Intelligence (EIAI) |
| 1xmpw92 | r/GeminiAI | 4 | 10 | 3. 11. 2026, 11:53 | Why Gemini Does This |
| 1xme4ih | r/singularity | 3 | 38 | 3. 11. 2026, 01:13 | If ASI Is Coming Soon, A Superhuman Alignment Researcher Is Coming Sooner |
| 1xmdywr | r/LocalLLM | 3 | 34 | 3. 11. 2026, 01:06 | I tested 6 AI models on a complex reasoning challenge. Here are the results |
| 1xmd35r | r/LocalLLM | 3 | 31 | 3. 11. 2026, 00:29 | Anyone using a Mac Studio for local LLMs? Looking for model and tool recommendations |
| 1xmd7ts | r/ClaudeAI | 3 | 19 | 3. 11. 2026, 00:35 | Is there any way to improve to make PowerPoints looks better? |
| 1xmea8t | r/ClaudeAI | 3 | 18 | 3. 11. 2026, 01:20 | How to make AI sound more human: what held up for us after 1,000+ hours on our writing skill and hundreds of blind A/B tests |
| 1xmruuc | r/LocalLLM | 3 | 17 | 3. 11. 2026, 13:38 | Which uncensored models work with Strata? |
| 1xmxkr0 | r/LocalLLM | 3 | 16 | 3. 11. 2026, 17:28 | is it worth getting an M5U 256gb memory for my use cases? |
| 1xn1fd4 | r/ClaudeAI | 3 | 15 | 3. 11. 2026, 19:47 | Best ways to use both Claude and ChatGPT models under a single interface? |
| 1xmnezy | r/ClaudeAI | 3 | 15 | 3. 11. 2026, 09:19 | A week after my "several Claude Code sessions" post: what I changed because of your comments |
| 1xn78cm | r/LocalLLaMA | 3 | 13 | 3. 11. 2026, 23:27 | Some "trust me bro" benchmarks while we prep the repo to open-source |
| 1xmpmg8 | r/ClaudeAI | 3 | 13 | 3. 11. 2026, 11:37 | Starting Today, my hook forcing Claude to understand me and what i wanted started getting blocked by [reasoning extraction claude]. Does someone have a methold to solve the issue that my hook was previously solving ? |
| 1xmw242 | r/ClaudeAI | 3 | 12 | 3. 11. 2026, 16:32 | Claude never says no to a feature, so I built a skill that makes it argue for deleting one |
| 1xmk3yk | r/LocalLLM | 3 | 11 | 3. 11. 2026, 06:02 | Little feeling on QFN nvfp4 and 27b fp8 |
| 1xmut36 | r/ClaudeAI | 3 | 11 | 3. 11. 2026, 15:44 | Using Claude on cooking and fitness |
| 1xmp6ro | r/ClaudeAI | 3 | 11 | 3. 11. 2026, 11:10 | Claude use in procurement |
| 1xmnelj | r/GeminiAI | 3 | 10 | 3. 11. 2026, 09:18 | A change in Pro quota ? |
| 1xmuzmh | r/ClaudeAI | 2 | 25 | 3. 11. 2026, 15:51 | Is context aggregation the real bottleneck for personal AI assistants? |
| 1xmhxzj | r/StableDiffusion | 2 | 21 | 3. 11. 2026, 04:11 | H3 Ref2va b25 49 workflow generating 20 second clip in 20 mins with RTX 4090, is this acceptable speed? |
| 1xmqt0b | r/ChatGPT | 2 | 20 | 3. 11. 2026, 12:44 | Reaching the cap limit seemingly randomly |
| 1xmuwub | r/LocalLLaMA | 2 | 17 | 3. 11. 2026, 15:48 | Two 3060ti 8gb and 64gb DDR4, worth using? |
| 1xmqcn1 | r/ArtificialInteligence | 2 | 15 | 3. 11. 2026, 12:19 | Seven GPT releases gave different leading answers about humanity's biggest threat |
| 1xmk8iw | r/LocalLLM | 2 | 14 | 3. 11. 2026, 06:08 | RTX Pro 4500 Blackwell - HP branded card |
| 1xmx0ux | r/LocalLLM | 2 | 13 | 3. 11. 2026, 17:08 | Why is my local AI slow to respond (first and subsequent interactions)? 2 |
| 1xmeubz | r/ClaudeAI | 2 | 13 | 3. 11. 2026, 01:46 | Anyone using two claude subscriptions in the claude code app? How? |
| 1xmmuuf | r/LocalLLM | 2 | 11 | 3. 11. 2026, 08:43 | best coder ai for projects |
| 1xmeb2f | r/LocalLLM | 2 | 11 | 3. 11. 2026, 01:21 | Opinions on ornith models? |
| 1xmohfc | r/ClaudeAI | 2 | 11 | 3. 11. 2026, 10:26 | Is it possible to do this Claude Code video editing workflow entirely on an Android tablet? |
| 1xmhurw | r/LLMDevs | 2 | 11 | 3. 11. 2026, 04:07 | Five checks I run by hand before I believe an agent actually finished |
| 1xme08e | r/ClaudeAI | 1 | 31 | 3. 11. 2026, 01:08 | Haiku 5.5 is basically just a fancy classifier with good manners. Change my mind. |
| 1xn4bn4 | r/LocalLLM | 1 | 22 | 3. 11. 2026, 21:33 | 2 x 3090 or 3090 + 128gb DDR4? |
| 1xmtyhz | r/LocalLLM | 1 | 20 | 3. 11. 2026, 15:11 | Add 3090 to current setup? Make separate machine with dual v100s? |
| 1xmzojo | r/ClaudeAI | 1 | 15 | 3. 11. 2026, 18:45 | Consultants / freelancers who use Claude |
| 1xn72tz | r/ClaudeAI | 1 | 14 | 3. 11. 2026, 23:20 | Claude app, Claude Code, or a mix of both? Looking for advice from non-devs |
| 1xmq17q | r/MachineLearning | 1 | 13 | 3. 11. 2026, 12:01 | Paper review question [D] |
| 1xmxl5q | r/LocalLLM | 1 | 13 | 3. 11. 2026, 17:28 | Second 3090 - new motherboard or NVLink? |
| 1xmop2l | r/ClaudeAI | 1 | 13 | 3. 11. 2026, 10:40 | How to get a Claude code review on every pull request with just your Pro/Max subscription. No API key, no extra bill. |
| 1xmxve7 | r/LocalLLM | 1 | 12 | 3. 11. 2026, 17:39 | Building my first LLM sever, thoughts? |
| 1xmqoia | r/ClaudeAI | 1 | 12 | 3. 11. 2026, 12:37 | This is when the creators finally understand the value of their work: after they leave the company :) |
| 1xmlzhi | r/StableDiffusion | 1 | 12 | 3. 11. 2026, 07:48 | Best way to combine pose, identity, clothing and background in Krea 2 ComfyUI? |
| 1xmzbqn | r/GeminiAI | 1 | 11 | 3. 11. 2026, 18:32 | Google NEEDS to give some more Gemini privileges to Pixel |
| 1xmh0qg | r/ChatGPT | 1 | 10 | 3. 11. 2026, 03:28 | Dot setup fails every time. |
| 1xmvxjp | r/ClaudeAI | 1 | 10 | 3. 11. 2026, 16:27 | How to use Claude on another pc? |
| 1xmgxev | r/singularity | 0 | 108 | 3. 11. 2026, 03:23 | Automated food production after singularity |
| 1xn1w81 | r/singularity | 0 | 63 | 3. 11. 2026, 20:03 | What about God? |
| 1xms3hp | r/LocalLLaMA | 0 | 47 | 3. 11. 2026, 13:50 | Does 5B tokens/month actually justify an eight-H200 purchase? |
| 1xmxrfi | r/LocalLLaMA | 0 | 45 | 3. 11. 2026, 17:35 | Black Friday coming up, best cost-effective rig for local inference? |
| 1xn5cmx | r/LocalLLM | 0 | 45 | 3. 11. 2026, 22:12 | The gap between proprietary LLMs vs. open source has widen |
| 1xmkqhj | r/ChatGPT | 0 | 42 | 3. 11. 2026, 06:36 | ai still not the very intelligent this year we need the actual benchmark which human not able to solve yet either myopia , cancer . we lack the actual ai metrics the investor are not able to ask right question or fast drug delivery . the real benchmark should be the human health not writing |
| 1xmuvep | r/ArtificialInteligence | 0 | 40 | 3. 11. 2026, 15:47 | Have AI models genuinely degraded over the past year, or am I imagining things? |
| 1xn0avz | r/ClaudeAI | 0 | 37 | 3. 11. 2026, 19:06 | Anthropic, please give us an option to turn off whimsical status messaging about task operations. |
| 1xmtert | r/LocalLLaMA | 0 | 36 | 3. 11. 2026, 14:49 | https://www.crowdgpt.net/ |
| 1xmf036 | r/artificial | 0 | 30 | 3. 11. 2026, 01:54 | Have we already crossed the frontier of saying that AI can "think"? |
| 1xn2yhf | r/LocalLLaMA | 0 | 30 | 3. 11. 2026, 20:42 | New Mac Mini M6 (16GB RAM) – What local LLMs can I realistically run? Looking for advice on runtimes and fine-tuning. |
| 1xmml7e | r/LocalLLaMA | 0 | 28 | 3. 11. 2026, 08:25 | Please rate or roast my setup and my LLM performance! |
| 1xmjirq | r/LocalLLM | 0 | 27 | 3. 11. 2026, 05:31 | Underrated benefit of Local AI: Speed |
| 1xmv440 | r/ChatGPT | 0 | 27 | 3. 11. 2026, 15:56 | When will AI actually solve the AI slop problem when it comes to graphics and art? |
| 1xmoy3w | r/artificial | 0 | 25 | 3. 11. 2026, 10:56 | AI bubble popping, what would be the consequences |
| 1xmxjiy | r/ClaudeAI | 0 | 24 | 3. 11. 2026, 17:27 | I asked Claude which database to use 612 times, then had Claude Code and Cursor build the same apps. In 4 of 7 jobs they built something else. |
| 1xmtwpp | r/StableDiffusion | 0 | 24 | 3. 11. 2026, 15:09 | Our Dreams are Video Generations? |
| 1xmvz9t | r/StableDiffusion | 0 | 23 | 3. 11. 2026, 16:29 | [LTX 2.5] General AI Filmmaking - How can I get Spatial Awareness for my filming locations ? |
| 1xmfjfb | r/LocalLLM | 0 | 22 | 3. 11. 2026, 02:18 | My Mac finally arrived |
| 1xmou9o | r/ClaudeAI | 0 | 22 | 3. 11. 2026, 10:49 | Claide chat vs claude code |
| 1xn67rh | r/LocalLLM | 0 | 21 | 3. 11. 2026, 22:46 | The question on everyone's mind: is a local LLM actually worth it? |
| 1xmm8p5 | r/OpenAI | 0 | 20 | 3. 11. 2026, 08:04 | OpenAI L4 offer vs a fresh Google L6 promo: which would you choose? |
| 1xmuec6 | r/LocalLLM | 0 | 19 | 3. 11. 2026, 15:28 | How to make local AI search jobs for me? |
| 1xmsv5j | r/ClaudeAI | 0 | 19 | 3. 11. 2026, 14:25 | I can't code, and I've released 25 small mobile games in about six months with Claude. Here's how it actually works |
| 1xmhmwi | r/StableDiffusion | 0 | 19 | 3. 11. 2026, 03:57 | Solo dev: measuring anime character proportions in LoRA datasets. What would convince you it improves the LoRA? |
| 1xmenzi | r/StableDiffusion | 0 | 19 | 3. 11. 2026, 01:38 | Training a FLUX LoRA of myself how do I keep the facial structure ,body  conistent? |
| 1xmdq1q | r/ArtificialInteligence | 0 | 18 | 3. 11. 2026, 00:57 | What if all cows started talking tomorrow? |
| 1xmg3n5 | r/ChatGPT | 0 | 18 | 3. 11. 2026, 02:45 | Can Chat be Authentic? |
| 1xmlebo | r/comfyui | 0 | 18 | 3. 11. 2026, 07:13 | Hey how can i create those AI influencers with comfeyUI. |
| 1xmwe5h | r/GeminiAI | 0 | 18 | 3. 11. 2026, 16:44 | GEMINI IS THE WORST AI ON THE PLANET! |
| 1xn7d7k | r/ArtificialInteligence | 0 | 17 | 3. 11. 2026, 23:32 | Why are we still acting as if Ai can't do anything we want |
| 1xmdwor | r/LocalLLaMA | 0 | 17 | 3. 11. 2026, 01:03 | My Local AI seems pretty confident it can solve the 3 body problem... |
| 1xmhnxj | r/ChatGPT | 0 | 17 | 3. 11. 2026, 03:58 | GPT zero proof |
| 1xmdb48 | r/ChatGPT | 0 | 17 | 3. 11. 2026, 00:39 | I spent time on ChatGPT developing a rubric for ranking the US Presidents from best to worst |
| 1xmmt0f | r/StableDiffusion | 0 | 17 | 3. 11. 2026, 08:39 | Cant we turn minimax into seadance 2.5 |
| 1xmxynm | r/GeminiAI | 0 | 17 | 3. 11. 2026, 17:42 | I asked Gemini a simple question about my dachshund puppy. It suddenly started speaking an unknown language for 15 seconds, then went back to normal. I recorded everything. |
| 1xmopx6 | r/OpenAI | 0 | 16 | 3. 11. 2026, 10:41 | How does Astra Medium (or Sonnet High) compare to Opus? |
| 1xn4ujo | r/ClaudeAI | 0 | 16 | 3. 11. 2026, 21:53 | Is it realistic to build macOS apps using Claude AI with limited Swift experience? |
| 1xn2s8o | r/GeminiAI | 0 | 16 | 3. 11. 2026, 20:36 | Gemini asked me to sniff mold |
| 1xmqt4u | r/LocalLLaMA | 0 | 15 | 3. 11. 2026, 12:44 | Model recommendations for cybersec work on 5090+5080 multi gpu setup + 32GB sys RAM |
| 1xmq0qj | r/ClaudeAI | 0 | 15 | 3. 11. 2026, 12:00 | ¿Existen las pruebas gratis de claude pro? |
| 1xmupji | r/LocalLLaMA | 0 | 14 | 3. 11. 2026, 15:40 | We're building a way for AI agents to share context across different models. Curious how local LLM users handle this. |
| 1xmdpra | r/LocalLLaMA | 0 | 14 | 3. 11. 2026, 00:56 | Why don't more people use QwenPaw as a Harness? |
| 1xn0fbz | r/LocalLLM | 0 | 14 | 3. 11. 2026, 19:11 | Last week Sam Altman said it is 'quite terrible' for people to use their RAM for running local LLMs. So today I am launching NativeCluster. A free platform for people to manage and use LLM apps with their own RAM for free. |
| 1xn4v40 | r/ClaudeAI | 0 | 14 | 3. 11. 2026, 21:54 | Do you use bypass/full-access mode when coding, or approve actions as you go? |
| 1xmy1m0 | r/ClaudeAI | 0 | 14 | 3. 11. 2026, 17:45 | I spent 9 months building local code search tool for Claude Code / 200 held-out SWE-rebench tasks: 5–11% cheaper, same no. of tasks solved. Open source (sweet-search) |
| 1xn12rf | r/LocalLLaMA | 0 | 13 | 3. 11. 2026, 19:34 | 5 approaches to managing memory and context in AI agents (and why bigger context windows don't solve everything) |
| 1xmplps | r/StableDiffusion | 0 | 13 | 3. 11. 2026, 11:35 | Super Editor — Why be ordinary when you can be super |
| 1xmoxgp | r/StableDiffusion | 0 | 13 | 3. 11. 2026, 10:55 | recommend good open source video generation model |
| 1xmqvtb | r/GeminiAI | 0 | 13 | 3. 11. 2026, 12:49 | gemini 4 argon is ret*rded |
| 1xmvzno | r/artificial | 0 | 12 | 3. 11. 2026, 16:29 | Who Gets to Hold the Reins of AI |
| 1xmxmw2 | r/ArtificialInteligence | 0 | 12 | 3. 11. 2026, 17:30 | so, who should I hate, the technology itself or who commands it? |
| 1xmnks8 | r/ArtificialInteligence | 0 | 12 | 3. 11. 2026, 09:29 | I'm saved!!! |
| 1xmhj93 | r/ChatGPT | 0 | 12 | 3. 11. 2026, 03:52 | Can AI analyze years of my digital footprint to reveal patterns I haven't noticed about myself? |
| 1xn3flm | r/ClaudeAI | 0 | 12 | 3. 11. 2026, 21:00 | Main usecase of Claude Code? |
| 1xmrcr1 | r/ClaudeAI | 0 | 12 | 3. 11. 2026, 13:12 | Art director, not a developer: I built BeeKeeper with Claude Code to see what my agents do behind my back |
| 1xmni0z | r/ClaudeAI | 0 | 12 | 3. 11. 2026, 09:24 | Cache-Aware Claude Max Workflow |
| 1xmfny8 | r/ClaudeAI | 0 | 12 | 3. 11. 2026, 02:24 | Using the entire weekly limit of an ultra plan in less than two hours on purpose, and why you should too. |
| 1xmd4d4 | r/ClaudeAI | 0 | 12 | 3. 11. 2026, 00:30 | I built a Claude skill for job hunting in Germany: it catches "German required" in English ads, checks Blue Card salary rules and writes a Lebenslauf (free, open source) |
| 1xmdb9u | r/GeminiAI | 0 | 12 | 3. 11. 2026, 00:39 | Gemini AI asked for the pin numbers of my bank accounts, should i trust it? |
| 1xn1bzg | r/artificial | 0 | 11 | 3. 11. 2026, 19:44 | Am I the only one that prefers to build it rather than paying for it? |
| 1xmss4r | r/artificial | 0 | 11 | 3. 11. 2026, 14:21 | Tell me which AI I should get! |
| 1xml9vp | r/ArtificialInteligence | 0 | 11 | 3. 11. 2026, 07:07 | I don't use AI as a chatbot. I run my life on an agent, disputes, a move, a podcast, all of it. |
| 1xn4hxu | r/ClaudeAI | 0 | 11 | 3. 11. 2026, 21:39 | “MCP Is Dead”? We Got 20,000 email Signups in Two Weeks. |
| 1xmkbzo | r/ClaudeAI | 0 | 11 | 3. 11. 2026, 06:14 | "(Claude) Model is not the bottleneck" |
| 1xmvn22 | r/StableDiffusion | 0 | 11 | 3. 11. 2026, 16:16 | Trained an SDXL LoRA for Chinese gongbi portraits, ended up not using it |
| 1xmkjr0 | r/ChatGPT | 0 | 10 | 3. 11. 2026, 06:26 | Amazon $50 |
| 1xmjslu | r/StableDiffusion | 0 | 10 | 3. 11. 2026, 05:45 | Visual models with good spatial awareness? |
