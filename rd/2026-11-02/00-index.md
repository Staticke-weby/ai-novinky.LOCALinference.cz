# AI souhrn z Redditu – 2. listopadu 2026

## Metodika

Data pocházejí z přímého sběru Redditu přes `scripts/rd-collect-web.py`; skóre a počty komentářů jsou hodnoty z doby sběru, časy jsou uvedené v pásmu Europe/Prague. Kandidátní sadu tvořilo 40 postů z AI subredditů, v příloze je všech 325 postů, které měly v okně dne alespoň 10 komentářů.

Před výběrem jsem porovnal každého kandidáta se seznamem témat z posledních tří dnů (`logs/recent-2026-11-02-rd.md`). Přísně jsem vyřadil **21 z 40 kandidátních postů**: 17 se krylo s už publikovanými tématy (DRAM a Sam Altman 10, herní remaky a Claude Code 1, Claude + Obsidian 1, Mythos 2, DeepSeek V4.1 Flash 2, pětihodinové limity 1) a další 4 byly memy bez vlastního AI tématu. Žádný z těchto postů není zařazen ani jako „další diskuse“.

Po filtraci zůstalo **15 článků**. Čtyři posty jsou sloučené jako další diskuse: dva k tématu weight-space programování, jeden ke srovnání interních nákladů Anthropicu a jeden ke změnám ChatGPT. U části externích článků byl zdroj dostupný jen částečně (paywall); články proto vycházejí z dostupného textu, selftextu a komentářů. Příloha obsahuje všechny posty s alespoň 10 komentáři v původním znění, bez překladu.

## Články

| # | Titulek | Subreddit | Skóre | Komentáře | ID |
|---:|---|---|---:|---:|---|
| 1 | [Oficiální prohlášení: Modely Qwen zůstanou open source až do konce!](1xm28e6_qwen-4-5-zustanou-open-source.md) | r/LocalLLaMA | 4038 | 420 | `1xm28e6` |
| 2 | [Opus 5.5 přežívá celou říjnovou smršť AI novinek 😂](1xlkghv_opus-5-5-prezil-rijnovy-cyklus.md) | r/ClaudeAI | 3609 | 163 | `1xlkghv` |
| 3 | [Výzkumníci z MIT tvrdí, že GPT-6 Astra zlepšil matematické skóre malého modelu Qwen ze 7,9 % na 48,1 % přímou editací pouhých 0,016 % jeho vah, bez trénování pomocí gradientů.](1xm89o3_weight-space-programming-gpt-6-astra.md) | r/singularity | 1510 | 157 | `1xm89o3` |
| 4 | [Sam Altman: „Na začátku letošního roku nebyla AI většinou tak chytrá jako naši nejchytřejší vědci, a teď je většinou chytřejší než oni.“ Tvrdí také, že AI nyní zvládne velkou část kancelářské práce, která byla na začátku roku ještě nad její síly.](1xm44jm_altman-ai-chytrejsi-nez-vedci.md) | r/singularity | 1116 | 859 | `1xm44jm` |
| 5 | [„Když jsme vyřešili první problém tisíciletí, bylo to 10 000 agentů modelu, který brzy vyjde, příštího GPT, pracujících asi 4 dny“](1xlyml4_millenium-prize-10000-agentu.md) | r/singularity | 771 | 265 | `1xlyml4` |
| 6 | [Tuhle hru dělám 3 měsíce jen s pomocí AI (vše naprogramované s Opus 5.5)](1xlr3u8_hra-vyvinuta-pouze-s-ai.md) | r/ClaudeAI | 630 | 134 | `1xlr3u8` |
| 7 | [Amazon údajně ruší objednávky GPU a ve vzácných případech zavírá účty za nákup výpočetního hardwaru; obětí této praktiky je i Tim Sweeney](1xm8o8g_amazon-rusi-objednavky-gpu.md) | r/LocalLLaMA | 605 | 147 | `1xm8o8g` |
| 8 | [Interní využití AI v Anthropicu, přepočteno v maloobchodních cenách, nyní převyšuje mzdové náklady na zaměstnance](1xm2sej_anthropic-interni-ai-drazsi-nez-platy.md) | r/ClaudeAI | 501 | 34 | `1xm2sej` |
| 9 | [ChatGPT (chat, neomezené použití) bude zrušen.](1xlq569_chatgpt-rusi-neomezeny-chat.md) | r/ChatGPT | 465 | 299 | `1xlq569` |
| 10 | [Právě jsem si na svůj herní počítač stáhl model OpenAI 120B.](1xlra3n_lokalni-120b-model-na-hernim-pc.md) | r/LocalLLM | 520 | 177 | `1xlra3n` |
| 11 | [Ne další příspěvek o tok/s: lokální kvantované modely vs Claude na 9 skutečných bugech](1xlwpqv_lokalni-kvanty-versus-claude-9-bugu.md) | r/LocalLLaMA | 321 | 139 | `1xlwpqv` |
| 12 | [Odmítání u Claude je každým dnem přísnější a otravnější](1xlz6m8_claude-odmitl-proxy-kvuli-limitum.md) | r/ClaudeAI | 305 | 157 | `1xlz6m8` |
| 13 | [Roje AI agentů vypuštěné v Minecraftu, aby „vybudovaly prosperující civilizaci“ – týmy o 50 agentech selhávají po upadnutí do ochromující byrokracie](1xm1wor_agenti-v-minecraftu-byrokracie.md) | r/OpenAI | 289 | 32 | `1xm1wor` |
| 14 | [Opravdu potřebujeme všechny tyhle příspěvky o „rychlosti“?](1xljjf2_rychlostni-rekordy-tok-s-debata.md) | r/LocalLLaMA | 285 | 93 | `1xljjf2` |
| 15 | [Lokální AI novinky, které jste zmeškali – říjen 2026](1xlwezy_rijnove-novinky-lokalni-ai.md) | r/StableDiffusion | 285 | 19 | `1xlwezy` |

## Příloha: všechny posty s alespoň 10 komentáři

Celkem 325 postů, seřazeno podle skóre. Odkazy u vybraných témat míří na odpovídající článek; ostatní posty jsou uvedeny bez odkazu.

| ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---:|---:|---|---|
| `1xlvsri` | r/ChatGPT | 6489 | 63 | 2. 11. 2026, 13:25 | How To Trap Sam Altman |
| `1xm28e6` | r/LocalLLaMA | 4038 | 420 | 2. 11. 2026, 17:42 | [Official Statement: Qwen Models Will Stick to Open Source to the End!](1xm28e6_qwen-4-5-zustanou-open-source.md) |
| `1xlkghv` | r/ClaudeAI | 3609 | 163 | 2. 11. 2026, 02:36 | [Opus 5.5 surviving the entire October AI release cycle 😂](1xlkghv_opus-5-5-prezil-rijnovy-cyklus.md) |
| `1xm89o3` | r/singularity | 1510 | 157 | 2. 11. 2026, 21:18 | [MIT researchers say GPT-6 Astra improved a small Qwen model’s math score from 7.9% to 48.1% by directly editing just 0.016% of its weights, without gradient-based training.](1xm89o3_weight-space-programming-gpt-6-astra.md) |
| `1xlx6lk` | r/ChatGPT | 1216 | 29 | 2. 11. 2026, 14:28 | lmao |
| `1xlqq7b` | r/OpenAI | 1188 | 129 | 2. 11. 2026, 08:19 | Sam Altman's RAM allocation argument, applied to food |
| `1xm44jm` | r/singularity | 1116 | 859 | 2. 11. 2026, 18:50 | [Sam Altman: "At the start of this year, AI was mostly not as smart as our smartest scientists, and now it's mostly smarter than them." He also says AI can now perform large parts of white-collar jobs that were beyond its capabilities earlier this year.](1xm44jm_altman-ai-chytrejsi-nez-vedci.md) |
| `1xm5vdp` | r/ClaudeAI | 1056 | 215 | 2. 11. 2026, 19:51 | Anthropic confirms new Claude Code limits to prevent game cloning |
| `1xllzsf` | r/ClaudeAI | 1007 | 33 | 2. 11. 2026, 03:53 | “Now fix all mistakes you’ve made” |
| `1xlvrzj` | r/OpenAI | 809 | 26 | 2. 11. 2026, 13:24 | How To Trap Sam Altman |
| `1xlyml4` | r/singularity | 771 | 265 | 2. 11. 2026, 15:27 | ["When we proved the first Millenium Prize problem, it was 10000 agents of the model that is gonna be released soon, the next GPT, working for about 4 days"](1xlyml4_millenium-prize-10000-agentu.md) |
| `1xlm85t` | r/ClaudeAI | 748 | 169 | 2. 11. 2026, 04:04 | i dont understand all this "claude + obsidian" obsession |
| `1xlu4bl` | r/ChatGPT | 639 | 11 | 2. 11. 2026, 11:55 | What else. |
| `1xlr3u8` | r/ClaudeAI | 630 | 134 | 2. 11. 2026, 08:43 | [Been making this game for 3 months using only AI (Everything coded with Opus 5.5)](1xlr3u8_hra-vyvinuta-pouze-s-ai.md) |
| `1xlhxkd` | r/OpenAI | 616 | 17 | 2. 11. 2026, 00:37 | In light of recent words of Sam Altman |
| `1xm8o8g` | r/LocalLLaMA | 605 | 147 | 2. 11. 2026, 21:33 | [Amazon Is Allegedly Canceling GPU Orders And, In Rare Cases, Closing Accounts For Purchasing Compute Hardware; Tim Sweeney Also A Victim Of This Practice](1xm8o8g_amazon-rusi-objednavky-gpu.md) |
| `1xls4cj` | r/ClaudeAI | 585 | 88 | 2. 11. 2026, 09:50 | The 7.72TB Alleged Anthropic AI Model Is Fake — I Reconstructed Its Generated Weights |
| `1xm8nvl` | r/ChatGPT | 554 | 15 | 2. 11. 2026, 21:33 | “GPT-6.1 the worlds best model” |
| `1xm0ndu` | r/ChatGPT | 552 | 22 | 2. 11. 2026, 16:44 | The AI gestapo would like to have a word with you |
| `1xlra3n` | r/LocalLLM | 520 | 177 | 2. 11. 2026, 08:55 | [Just downloaded the OpenAI 120B model on my gaming PC.](1xlra3n_lokalni-120b-model-na-hernim-pc.md) |
| `1xls92p` | r/ChatGPT | 511 | 41 | 2. 11. 2026, 09:59 | How can I donate my idle RAM to Sam Altman? |
| `1xm2sej` | r/ClaudeAI | 501 | 34 | 2. 11. 2026, 18:02 | [Anthropic's internal AI use, valued at retail prices, now exceeds its employee pay](1xm2sej_anthropic-interni-ai-drazsi-nez-platy.md) |
| `1xlq569` | r/ChatGPT | 465 | 299 | 2. 11. 2026, 07:42 | [ChatGPT (chat, unlimited use) will be axed.](1xlq569_chatgpt-rusi-neomezeny-chat.md) |
| `1xlpvka` | r/ChatGPT | 452 | 183 | 2. 11. 2026, 07:26 | [I got the merge, it sucks.](1xlq569_chatgpt-rusi-neomezeny-chat.md) |
| `1xljdnj` | r/LocalLLaMA | 428 | 90 | 2. 11. 2026, 01:44 | Sorry Sam, my "quite terrible" home DRAM is at 100% now: patched Strata to make DeepSeek V4.1 agent sessions start 20× faster on a good old standard gaming GPU, no datacenter required |
| `1xlmicc` | r/ArtificialInteligence | 428 | 17 | 2. 11. 2026, 04:19 | The Myth of "Consensual" PC Building |
| `1xlutkc` | r/OpenAI | 421 | 30 | 2. 11. 2026, 12:34 | WHAT YOU SAY!! |
| `1xlqmtr` | r/ClaudeAI | 418 | 86 | 2. 11. 2026, 08:13 | 5h limit - gone for good? |
| `1xma0tw` | r/LocalLLaMA | 417 | 70 | 2. 11. 2026, 22:25 | [GPT-6 Astra Edits Qwen Weights: MATH-500 7.9% to 48.1%](1xm89o3_weight-space-programming-gpt-6-astra.md) |
| `1xlikmp` | r/singularity | 374 | 50 | 2. 11. 2026, 01:05 | Mythos 5.5 release nears as Anthropic begins preparing their webpage for it |
| `1xm6jow` | r/LocalLLaMA | 359 | 70 | 2. 11. 2026, 20:15 | [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](1xm89o3_weight-space-programming-gpt-6-astra.md) |
| `1xlys6k` | r/LocalLLaMA | 338 | 88 | 2. 11. 2026, 15:33 | [Release] ISTA DeepSeek-V4.1-Flash-1017 GSQ-RCO Coder: a 763B model at 1 bit per parameter |
| `1xlj2ee` | r/ChatGPT | 325 | 19 | 2. 11. 2026, 01:29 | We’re safe… for now |
| `1xlwpqv` | r/LocalLLaMA | 321 | 139 | 2. 11. 2026, 14:08 | [Not another tok/s post: local quants vs Claude on 9 real bugs](1xlwpqv_lokalni-kvanty-versus-claude-9-bugu.md) |
| `1xlz6m8` | r/ClaudeAI | 305 | 157 | 2. 11. 2026, 15:49 | [Claude's refusal is getting stricter  and annoying each day](1xlz6m8_claude-odmitl-proxy-kvuli-limitum.md) |
| `1xm1rhy` | r/ClaudeAI | 292 | 66 | 2. 11. 2026, 17:25 | [Anthropic is now spending more money on its "AI employees" than its human employees](1xm2sej_anthropic-interni-ai-drazsi-nez-platy.md) |
| `1xm1wor` | r/OpenAI | 289 | 32 | 2. 11. 2026, 17:30 | [AI agent swarms unleashed in Minecraft to ‘build a thriving civilization’ — 50-agent teams fail after falling into paralyzing bureaucracy](1xm1wor_agenti-v-minecraftu-byrokracie.md) |
| `1xljjf2` | r/LocalLLaMA | 285 | 93 | 2. 11. 2026, 01:52 | [Do we really need all these "speed" posts?](1xljjf2_rychlostni-rekordy-tok-s-debata.md) |
| `1xlwezy` | r/StableDiffusion | 285 | 19 | 2. 11. 2026, 13:55 | [Local AI News You Missed - October 2026](1xlwezy_rijnove-novinky-lokalni-ai.md) |
| `1xm2tsb` | r/OpenAI | 270 | 20 | 2. 11. 2026, 18:04 | Insane |
| `1xly4rw` | r/StableDiffusion | 266 | 99 | 2. 11. 2026, 15:07 | My H3 Settings that generate 15 second videos in 2 mins. |
| `1xlsrsv` | r/ChatGPT | 262 | 11 | 2. 11. 2026, 10:32 | Mornin', Sam! |
| `1xlp0kg` | r/StableDiffusion | 256 | 24 | 2. 11. 2026, 06:35 | I made a ComfyUI tool to bring back earlier scenes in H3 videos — my Open Source Higgsfield entry |
| `1xmbym0` | r/LocalLLaMA | 249 | 139 | 2. 11. 2026, 23:42 | Qwen 3.8 27b is sometimes so smart it scares me... |
| `1xm0tga` | r/artificial | 235 | 139 | 2. 11. 2026, 16:50 | Almost half of all new Steam games use AI now |
| `1xm33gr` | r/LocalLLaMA | 216 | 73 | 2. 11. 2026, 18:13 | Yet another reason to self host: Anthropic has (again) cut back on reverse engineering tools |
| `1xlhji9` | r/OpenAI | 211 | 53 | 2. 11. 2026, 00:19 | OpenAI and Anthropic are worried people will switch to local models, but they are practically asking for it at this point |
| `1xlv6d2` | r/LocalLLM | 209 | 129 | 2. 11. 2026, 12:54 | Sick of all the tok/s talk |
| `1xlu40a` | r/OpenAI | 208 | 27 | 2. 11. 2026, 11:54 | What else. |
| `1xm3d1l` | r/GeminiAI | 205 | 106 | 2. 11. 2026, 18:22 | Not Even The Gemini Flash Model! IT IS FLASH LITE |
| `1xm5oy9` | r/singularity | 203 | 38 | 2. 11. 2026, 19:45 | Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights |
| `1xmbj0v` | r/LocalLLaMA | 192 | 14 | 2. 11. 2026, 23:24 | New sparse attention method for ultra-long context |
| `1xm2ilx` | r/singularity | 189 | 71 | 2. 11. 2026, 17:53 | Anthropic warns in new SEC filing that its future models may "imminently" reach the threshold for AI-driven research doubling the pace of AI progress—and admits it may not detect the acceleration until after it happens. |
| `1xm7kw7` | r/ClaudeAI | 189 | 20 | 2. 11. 2026, 20:53 | Started a hobby project about the Mongol Invasions of Vietnam. Claude helped turn it into a real game |
| `1xlshw6` | r/GeminiAI | 188 | 50 | 2. 11. 2026, 10:14 | with every passing day I become less convinced Gemini will kill us all |
| `1xlr2l4` | r/singularity | 179 | 40 | 2. 11. 2026, 08:41 | New frontier-level, long horizon benchmark GDPx (successor of GDPval). Best models scoring ~12% |
| `1xm506n` | r/LocalLLaMA | 165 | 53 | 2. 11. 2026, 19:21 | Am I the only one who frequently opens this subreddit and stumbles upon announcements about Qwen4? |
| `1xlhmup` | r/StableDiffusion | 159 | 22 | 2. 11. 2026, 00:23 | L3G-WorldReal-Time Infinite World Generationwith Latent 3D Gaussian Memory |
| `1xlu5w4` | r/LocalLLM | 156 | 86 | 2. 11. 2026, 11:57 | 56GB VRAM Frankenstein build managed to fit 4 GPUs in the Cooler Master HAF II 500 |
| `1xm2o6v` | r/StableDiffusion | 134 | 28 | 2. 11. 2026, 17:58 | Someone said every AI music video has attractive models in the band and asked for Muppets instead, so I made it (rendered locally with MiniMax H3 + my Video Builder in ComfyUI) |
| `1xlusil` | r/LocalLLaMA | 129 | 89 | 2. 11. 2026, 12:33 | Proposal: A community revolution for private quality benchmarks (and why endless chasing tok/s is rotting our brains |
| `1xlni9b` | r/StableDiffusion | 121 | 29 | 2. 11. 2026, 05:12 | I built a free open-source node pack for 2–3 minute videos with MiniMax H3 (1080P, one run) |
| `1xm6j5v` | r/ArtificialInteligence | 120 | 149 | 2. 11. 2026, 20:15 | Do you think 2026 will be the last "normal" year in the AI revolution? |
| `1xlhnpr` | r/ClaudeAI | 119 | 19 | 2. 11. 2026, 00:24 | Claude |
| `1xm0uy0` | r/LocalLLaMA | 109 | 33 | 2. 11. 2026, 16:52 | Running UNCENSORED DeepSeek-V4.1-Flash-1017 on a 12 Gb VRAM |
| `1xm102d` | r/LocalLLaMA | 108 | 75 | 2. 11. 2026, 16:57 | Unsloth vs GSQ-RCO - 512K context DeepSeek-V4.1 GGUF benchmarks Terminal Bench |
| `1xlwmyz` | r/ChatGPT | 107 | 20 | 2. 11. 2026, 14:05 | Thought: Altman could greatly reduce RAM demand if he spent half a billion optimizing key programs like Chromium. |
| `1xmal1l` | r/StableDiffusion | 105 | 17 | 2. 11. 2026, 22:47 | Open-H3-Regenerate-2K to preserve draft pass details |
| `1xm5w5i` | r/MachineLearning | 102 | 35 | 2. 11. 2026, 19:52 | To all ML PhDs, how are you guys doing these days? [D] |
| `1xlw9i9` | r/ChatGPT | 100 | 14 | 2. 11. 2026, 13:48 | Just an ordinary late night retro gaming session..... |
| `1xln8f2` | r/LocalLLaMA | 97 | 22 | 2. 11. 2026, 04:58 | JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP · Hugging Face |
| `1xm1r1j` | r/ChatGPT | 96 | 29 | 2. 11. 2026, 17:24 | ChatGPT found my blind spot. Fair enough |
| `1xm9osi` | r/LocalLLM | 95 | 24 | 2. 11. 2026, 22:12 | Qwen 4's date rumors are this week and November 16 |
| `1xm89ef` | r/MachineLearning | 90 | 33 | 2. 11. 2026, 21:18 | Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights [R] |
| `1xlwq82` | r/ChatGPT | 89 | 38 | 2. 11. 2026, 14:09 | I’m just so tired of it… |
| `1xm7eyb` | r/artificial | 89 | 32 | 2. 11. 2026, 20:47 | OpenAI lowers funding goals as investors cool on AI |
| `1xm9pq0` | r/GeminiAI | 86 | 20 | 2. 11. 2026, 22:13 | Gemini 3.1 Pro is the Nokia in the iPhone store. Google, let it go. |
| `1xlj3z1` | r/ChatGPT | 81 | 42 | 2. 11. 2026, 01:31 | Anthropic bagholders are about to fund the next twenty years worth of data centers |
| `1xllwpg` | r/StableDiffusion | 76 | 13 | 2. 11. 2026, 03:48 | Easier Poses Ref2V MM-H3 - Semi Transparent Canny |
| `1xlk2kb` | r/LocalLLaMA | 72 | 55 | 2. 11. 2026, 02:17 | LFM3 Omni 2B is INCREDIBLE |
| `1xmaavl` | r/LocalLLM | 71 | 40 | 2. 11. 2026, 22:36 | MIT researchers say GPT-6 Astra improved a small Qwen model’s math score from 7.9% to 48.1% by directly editing just 0.016% of its weights, without gradient-based training. |
| `1xm0b7r` | r/LocalLLaMA | 71 | 20 | 2. 11. 2026, 16:31 | Builders got MiniMax M3.1 Flash's open weights from 252.4 GB down to 93 GB in 10 days, and the lab thanked them by name |
| `1xlhlw1` | r/ChatGPT | 70 | 39 | 2. 11. 2026, 00:22 | What advantages does ChatGPT Plus still have over its competitors? |
| `1xlpem3` | r/comfyui | 70 | 26 | 2. 11. 2026, 06:58 | Virtual Upstage |
| `1xm8xhn` | r/LocalLLaMA | 70 | 23 | 2. 11. 2026, 21:43 | Kind of enjoying the ISTA (GSQ-RCO) vs Unsloth beef |
| `1xm0v7k` | r/ChatGPT | 68 | 22 | 2. 11. 2026, 16:52 | First our RAM, now our ChatGPT limits. Thanks, Sam! |
| `1xlwf61` | r/ChatGPT | 67 | 47 | 2. 11. 2026, 13:55 | GPT-6 has more problems than improvements, yet OpenAI wants to limit our usage? |
| `1xm1uxz` | r/StableDiffusion | 67 | 24 | 2. 11. 2026, 17:28 | Pinokio Remote -- All your local AI from anywhere |
| `1xlpoz3` | r/StableDiffusion | 65 | 232 | 2. 11. 2026, 07:14 | Why does Moss have and Krea2 Doesn't?! |
| `1xm84y2` | r/OpenAI | 65 | 47 | 2. 11. 2026, 21:13 | Astra 6.2 rolling out? |
| `1xlsuwf` | r/LocalLLaMA | 64 | 19 | 2. 11. 2026, 10:38 | 4" touchscreen for inference engine monitoring |
| `1xm0iri` | r/agi | 64 | 14 | 2. 11. 2026, 16:39 | AI agent swarms unleashed in Minecraft to ‘build a thriving civilization’ — 50-agent teams fail after falling into paralyzing bureaucracy |
| `1xm0i9m` | r/LocalLLaMA | 63 | 53 | 2. 11. 2026, 16:38 | 😃Made My Own Invoicing Dekstop App With Qwen 3.8 27B+OpenCode+LM Studio On RTX 5090..Saved Me $100 a Year I Was Paying |
| `1xm2hqw` | r/agi | 63 | 30 | 2. 11. 2026, 17:52 | Anthropic is now spending more money on its "AI employees" than its human employees |
| `1xlw9v4` | r/LocalLLaMA | 63 | 20 | 2. 11. 2026, 13:48 | sensenova/SenseNova-Loop-9B-Preview · Hugging Face |
| `1xlwv40` | r/ClaudeAI | 59 | 38 | 2. 11. 2026, 14:15 | Switched from Codex to Claude Code on the same $20 plan, and I'm blown away |
| `1xlroro` | r/ChatGPT | 58 | 13 | 2. 11. 2026, 09:21 | We're so cooked |
| `1xm8q6q` | r/ClaudeAI | 57 | 37 | 2. 11. 2026, 21:35 | Use Fable more |
| `1xm58ke` | r/ChatGPT | 57 | 28 | 2. 11. 2026, 19:29 | "Hit my limit" in chat? Some type of new change? |
| `1xlou2h` | r/StableDiffusion | 56 | 29 | 2. 11. 2026, 06:25 | I taken all the info I've found on degradation and Frame 0 and compiled it. I'm updating it in real time. |
| `1xls4pj` | r/StableDiffusion | 55 | 23 | 2. 11. 2026, 09:51 | Anima new ref-based generation solution |
| `1xlpbp8` | r/ClaudeAI | 53 | 71 | 2. 11. 2026, 06:53 | Two Claude accounts, three computers, too many projects. How do you stay organized? |
| `1xlt9wm` | r/MachineLearning | 53 | 26 | 2. 11. 2026, 11:04 | ML PhDs: Would you rather have done your PhD before or after the rise of AI chatbots? [D] |
| `1xlk43x` | r/LocalLLaMA | 52 | 28 | 2. 11. 2026, 02:19 | 8 agents × 250K context, concurrently, on two 3090s (~600+ tok/s total) |
| `1xm4pzd` | r/ChatGPT | 50 | 40 | 2. 11. 2026, 19:11 | guys what do I do im scared |
| `1xlxnpc` | r/LocalLLaMA | 47 | 33 | 2. 11. 2026, 14:48 | We released KVARK Sparkle 1.0 – a Qwen3.8-27B-based model with up to 67% fewer thinking tokens |
| `1xlzvyc` | r/comfyui | 47 | 11 | 2. 11. 2026, 16:15 | My hybrid AI demo reel. Need opinion and feedback ! |
| `1xlicia` | r/LocalLLaMA | 45 | 47 | 2. 11. 2026, 00:56 | Qwen 3.8 Flash Next NVFP4 on 64gb RAM and 5090, Basalt. Ditched windows for it. Very hyped for qwen 4 model family now. |
| `1xljadr` | r/comfyui | 43 | 14 | 2. 11. 2026, 01:40 | EasyComfee V2: an open-source creative studio on top of ComfyUI |
| `1xm462g` | r/ChatGPT | 42 | 55 | 2. 11. 2026, 18:51 | Are uploads failing for anybody else? |
| `1xm2xbq` | r/LocalLLaMA | 42 | 12 | 2. 11. 2026, 18:07 | Fine tuned open model ftw |
| `1xlsd4v` | r/LocalLLaMA | 41 | 31 | 2. 11. 2026, 10:06 | If you are using big model compared to ram try and disable mtp |
| `1xlv4qr` | r/LocalLLM | 41 | 16 | 2. 11. 2026, 12:52 | I moved my graphics card outside the case |
| `1xm7u3x` | r/StableDiffusion | 40 | 12 | 2. 11. 2026, 21:02 | RTX 3090 tensor unlock on Windows: got it to actually boot (BitLocker was the problem) + real ComfyUI video numbers |
| `1xlwth1` | r/ChatGPT | 39 | 125 | 2. 11. 2026, 14:13 | Sam Altman Suggests Running AI Locally Is a Waste of Memory |
| `1xm9i4x` | r/LocalLLaMA | 38 | 24 | 2. 11. 2026, 22:05 | Inconsistencies in Unsloth's LiveCodeBench Results |
| `1xlp1yv` | r/LocalLLM | 38 | 16 | 2. 11. 2026, 06:37 | Getting incredible results with a single RTX 3090ti and 128gb of ram. Deepseek-V4.1-Flash-1017 (35 tok/s decode) and Qwen3.8-Flash-Next (130 tok/s decode) |
| `1xlytko` | r/LocalLLM | 37 | 10 | 2. 11. 2026, 15:34 | I built a working V8 engine simulator with a local QFN NVFP4 model using OpenCode V2 (with engine sound) |
| `1xlzlhk` | r/ClaudeAI | 36 | 53 | 2. 11. 2026, 16:05 | Has anyone left agent(s) run with barely any human interaction for a day? Was this a bad idea? |
| `1xm42is` | r/ChatGPT | 35 | 81 | 2. 11. 2026, 18:48 | I know people have made plenty of posts about it already, but I’m at my wits end with the ridiculously oversensitive image guardrail blocks. |
| `1xlu1fw` | r/ChatGPT | 35 | 27 | 2. 11. 2026, 11:50 | OpenAI's shared usage limits could cost them something more valuable than subscribers: the users who help improve their models |
| `1xm3vf1` | r/artificial | 34 | 19 | 2. 11. 2026, 18:41 | OpenAI says its AI is getting better at doing things humans do, like shopping and meal planning |
| `1xly5yc` | r/ArtificialInteligence | 31 | 113 | 2. 11. 2026, 15:09 | How do people tell if posts/comments in reddit are AI? |
| `1xlmkk4` | r/LocalLLaMA | 31 | 19 | 2. 11. 2026, 04:22 | AMA Announcement: Reflection, the lab behind behind Beam (Tuesday Nov 3rd, 8am-11am PT) |
| `1xlr44h` | r/ChatGPT | 30 | 19 | 2. 11. 2026, 08:44 | I am convinced something changed in their image filtering. |
| `1xlpkqv` | r/LocalLLaMA | 29 | 41 | 2. 11. 2026, 07:08 | List of tiny-to-medium models for web research/coding agents |
| `1xloob1` | r/ClaudeAI | 28 | 35 | 2. 11. 2026, 06:16 | Claude refusing search tasks and it's getting really annoying, how do you get it to listen? |
| `1xm8vik` | r/MachineLearning | 28 | 15 | 2. 11. 2026, 21:41 | ICLR 2027 review results [D] |
| `1xlsep7` | r/StableDiffusion | 25 | 33 | 2. 11. 2026, 10:08 | Trying MOSS Image for the first time? What am i doing wrong? |
| `1xloylo` | r/StableDiffusion | 25 | 10 | 2. 11. 2026, 06:32 | I'm loving krea 2 |
| `1xma1tq` | r/LocalLLaMA | 24 | 25 | 2. 11. 2026, 22:26 | Is there still a point to fine-tuning local LLMs? |
| `1xm6amc` | r/ChatGPT | 23 | 36 | 2. 11. 2026, 20:06 | What's a small thing ChatGPT (or any AI) does for you that you'd really miss if it disappeared? |
| `1xlxid8` | r/ChatGPT | 23 | 16 | 2. 11. 2026, 14:42 | OpenAI and its "million-dollar" strategy |
| `1xlornq` | r/ChatGPT | 23 | 14 | 2. 11. 2026, 06:21 | Ask your AI: Generate a photo based on one of our "what if" conversations |
| `1xlz9xj` | r/OpenAI | 23 | 12 | 2. 11. 2026, 15:52 | Ram Wastage |
| `1xlp8nd` | r/LocalLLaMA | 22 | 52 | 2. 11. 2026, 06:48 | Whats the best open source OCR for batch processing pdfs in 2026? |
| `1xlqa3q` | r/LocalLLM | 22 | 48 | 2. 11. 2026, 07:51 | Speedy - custom Strata for single/dual RTX - Tested on RTX 3080 with 4,270 t/s prefill / up to 211 t/s decode - fastest Qwen3.8 Flash-Next engine I know |
| `1xlrboh` | r/StableDiffusion | 22 | 34 | 2. 11. 2026, 08:58 | PRISM-DMAD-PDMD Merge of 10ErosB6-X-Singularity2 |
| `1xm2y93` | r/ChatGPT | 21 | 21 | 2. 11. 2026, 18:08 | Not able to upload PDFs |
| `1xlp424` | r/GeminiAI | 21 | 18 | 2. 11. 2026, 06:41 | Gemini Ultra gives extremely generous usage! Almost 1.2 billion tokens this last 2 weeks |
| `1xlwh31` | r/OpenAI | 20 | 35 | 2. 11. 2026, 13:58 | OpenAI Is Giving Up on Its Best Feature. |
| `1xlyr77` | r/MachineLearning | 20 | 23 | 2. 11. 2026, 15:32 | What did Ilya Sutskever mean when he said "The models, they just want to learn"? [D] |
| `1xlyiu9` | r/OpenAI | 20 | 23 | 2. 11. 2026, 15:23 | ChatGPT gets metered in tokens in December. The habit I'm dropping first is keeping one giant chat for each project |
| `1xlwg6t` | r/ChatGPT | 19 | 26 | 2. 11. 2026, 13:56 | OpenAI Is Giving Up on Its Best Feature. |
| `1xlq763` | r/ClaudeAI | 19 | 15 | 2. 11. 2026, 07:46 | On xHigh permanently bc why not… |
| `1xlw1x9` | r/ClaudeAI | 19 | 12 | 2. 11. 2026, 13:37 | Rethinking Computer Science Education: Why Students Should Build Before They Master Theory |
| `1xm64of` | r/MachineLearning | 19 | 10 | 2. 11. 2026, 20:00 | Couldn't reproduce a published paper's numbers with its own code and settings. How do I present this? [R] |
| `1xln18y` | r/StableDiffusion | 18 | 90 | 2. 11. 2026, 04:47 | For those of you running both ComfyUI and local LLMs, how are you managing GPU resources? |
| `1xm8zmn` | r/OpenAI | 18 | 41 | 2. 11. 2026, 21:46 | What if we built something like Folding@home, but for LLMs? |
| `1xm3wa2` | r/ArtificialInteligence | 18 | 35 | 2. 11. 2026, 18:42 | You Will Own Nothing & Be Happy |
| `1xlxd1x` | r/LocalLLM | 18 | 17 | 2. 11. 2026, 14:36 | Groot-65B-A6B looks interesting. Can someone with enough RAM test the Q4 and tell us if it's the real deal? |
| `1xlmcb6` | r/LocalLLM | 17 | 28 | 2. 11. 2026, 04:10 | Strata viable for bigger quants? |
| `1xm1i5w` | r/AIAssisted | 17 | 16 | 2. 11. 2026, 17:15 | Anyone here using AI to help call center agents during live calls? |
| `1xm3sr0` | r/ChatGPT | 17 | 15 | 2. 11. 2026, 18:38 | Chatgpt having issues reading files that are being uploaded |
| `1xlmf1g` | r/OpenAI | 16 | 38 | 2. 11. 2026, 04:14 | The hell happened to Astra? |
| `1xm82tt` | r/ChatGPT | 16 | 29 | 2. 11. 2026, 21:11 | I love my dot but... |
| `1xm6z1b` | r/ClaudeAI | 16 | 25 | 2. 11. 2026, 20:31 | Are the safeguards ever gonna be fixed? |
| `1xllq08` | r/ClaudeAI | 16 | 23 | 2. 11. 2026, 03:39 | Fable 5.1 vs Opus 5.5 |
| `1xlz1lz` | r/StableDiffusion | 15 | 40 | 2. 11. 2026, 15:43 | Using AI to generate ComfyUI nodes |
| `1xm5lz3` | r/ClaudeAI | 15 | 20 | 2. 11. 2026, 19:42 | What tools/plugins do you use with Claude Code to get good-looking UI that doesn’t look AI-generated? |
| `1xlw8r1` | r/ChatGPT | 15 | 19 | 2. 11. 2026, 13:47 | Are the limits already in place? But aren’t they supposed to come into effect in December? |
| `1xm14j5` | r/singularity | 15 | 14 | 2. 11. 2026, 17:02 | r/Singularity Daily Discussion Thread — November 02, 2026 |
| `1xlvh7j` | r/LocalLLM | 15 | 13 | 2. 11. 2026, 13:09 | What is the best translation LLM? |
| `1xlt71v` | r/ChatGPT | 13 | 29 | 2. 11. 2026, 10:59 | The Image Gen quality has plummeted in last 2 days. |
| `1xm0rla` | r/comfyui | 13 | 24 | 2. 11. 2026, 16:48 | Why can’t I get good results? |
| `1xlp649` | r/ChatGPT | 13 | 14 | 2. 11. 2026, 06:44 | how did they make this AI video look so real? |
| `1xlsj2e` | r/GeminiAI | 13 | 14 | 2. 11. 2026, 10:16 | Noticeable changes |
| `1xm402e` | r/ChatGPT | 12 | 33 | 2. 11. 2026, 18:45 | I asked Chatgpt : “How do I personally use gpt that’s harmful to me?” |
| `1xlke9o` | r/ChatGPT | 12 | 30 | 2. 11. 2026, 02:33 | I spend $48/month on ChatGPT, Claude, and Grok. Smart setup or subscription creep? |
| `1xm7wlv` | r/singularity | 12 | 24 | 2. 11. 2026, 21:05 | AI is not more expensive than humans |
| `1xllrrq` | r/ChatGPT | 11 | 48 | 2. 11. 2026, 03:41 | Is chatgpt now using British slang/words? |
| `1xlwazl` | r/ChatGPT | 11 | 17 | 2. 11. 2026, 13:50 | Live chat patterns |
| `1xljn4e` | r/LocalLLaMA | 11 | 14 | 2. 11. 2026, 01:57 | "Turnkey" App for ebook to audio book |
| `1xm3jv6` | r/GeminiAI | 11 | 12 | 2. 11. 2026, 18:29 | Argon quota for Pro plan |
| `1xlhrqm` | r/deeplearning | 11 | 11 | 2. 11. 2026, 00:29 | Soft Multi-Token Prediction |
| `1xm1nnl` | r/LocalLLaMA | 10 | 35 | 2. 11. 2026, 17:21 | Testing a GB300 tomorrow - What to run? |
| `1xlujwl` | r/ClaudeAI | 10 | 25 | 2. 11. 2026, 12:19 | Claude Code's docs say CLAUDE.md is context, not enforced config. What have you moved into hooks because Claude kept skipping it? |
| `1xlnocn` | r/comfyui | 10 | 12 | 2. 11. 2026, 05:21 | Am i missing out by using the default H3 workflows? |
| `1xm7ihx` | r/LocalLLM | 9 | 79 | 2. 11. 2026, 20:51 | What *specifically* do you still *need* cloud models for? |
| `1xls3km` | r/ArtificialInteligence | 9 | 20 | 2. 11. 2026, 09:48 | AI companies are racing to make assistants remember you. Almost nothing is being built to help you remember what they told you |
| `1xm5kay` | r/ArtificialInteligence | 9 | 18 | 2. 11. 2026, 19:40 | Other people's efficiency |
| `1xlwm4n` | r/LocalLLaMA | 9 | 16 | 2. 11. 2026, 14:04 | recommended 2  light weight model that is great at completing task and it runs in 32gb ram and 12gb vram |
| `1xm2sd4` | r/ChatGPT | 9 | 12 | 2. 11. 2026, 18:02 | Bug or something else? |
| `1xm39bk` | r/ClaudeAI | 9 | 12 | 2. 11. 2026, 18:19 | Stop blowing through your usage - Pace your agents with skills/hooks |
| `1xm0kbb` | r/ArtificialInteligence | 9 | 10 | 2. 11. 2026, 16:41 | I tried to keep track of everything happening in AI. Eventually I had to build a tool for it. |
| `1xls66c` | r/StableDiffusion | 8 | 15 | 2. 11. 2026, 09:53 | What's your favorite prompt enhancer for Qwen-Image-2.1? |
| `1xm3rne` | r/LLMDevs | 8 | 15 | 2. 11. 2026, 18:37 | Is "Codex gets slower in long sessions" a model problem or a context-budget problem? |
| `1xlmffv` | r/MachineLearning | 8 | 11 | 2. 11. 2026, 04:15 | [D] Self-Promotion Thread |
| `1xlqud5` | r/ChatGPT | 8 | 10 | 2. 11. 2026, 08:26 | How to best transition models? |
| `1xlycot` | r/LocalLLM | 7 | 29 | 2. 11. 2026, 15:16 | $700 to upgrade my RTX 4090 PC to 128GB DDR4, or $3,100 for a 128GB Strix Halo? Mainly for local AI agents. |
| `1xmb2qh` | r/LocalLLaMA | 7 | 24 | 2. 11. 2026, 23:06 | How usable are "lobotomized" weights? |
| `1xm30v8` | r/OpenAI | 7 | 17 | 2. 11. 2026, 18:11 | ChatGPT stuck on “Adding pasted text...” indefinitely — anyone else experiencing this today? |
| `1xlh9tg` | r/StableDiffusion | 7 | 17 | 2. 11. 2026, 00:07 | Best method to make "clear" video with minimax h3 |
| `1xlsr1b` | r/ClaudeAI | 7 | 15 | 2. 11. 2026, 10:31 | How to create animations, videos and images. |
| `1xlvd0l` | r/LocalLLM | 7 | 14 | 2. 11. 2026, 13:03 | 17× RTX 3060 and a pile of old Xeon boards: what's the best way to use them for local LLM agents? Planning a 7-GPU Z9PE-D8 WS build (benchmarks inside) |
| `1xm3gxw` | r/ClaudeAI | 7 | 11 | 2. 11. 2026, 18:26 | Short tip: upgraidng Max to Ultra means every usage meter reset to zero (weekly, Fable, session, overage) |
| `1xln8d2` | r/ChatGPT | 6 | 45 | 2. 11. 2026, 04:58 | Do you guys trust chatgpt now? |
| `1xm8lc1` | r/OpenAI | 6 | 17 | 2. 11. 2026, 21:30 | If the $200 plan is still going to be 20x then WTF is the $500 plan at 25x...... Did they just rob all of those people? |
| `1xm4j4p` | r/StableDiffusion | 6 | 14 | 2. 11. 2026, 19:04 | Best workflow for high quality H3 output |
| `1xltciz` | r/GeminiAI | 6 | 13 | 2. 11. 2026, 11:08 | I hate auto feature |
| `1xlyxan` | r/ChatGPT | 6 | 11 | 2. 11. 2026, 15:39 | ChatGPT & Work Integration – Questions About Memory, Projects, and Token Usage |
| `1xmatri` | r/ChatGPT | 5 | 33 | 2. 11. 2026, 22:56 | Is unlimited chatting coming to an end? |
| `1xlx1hz` | r/ChatGPT | 5 | 28 | 2. 11. 2026, 14:22 | Hit My Usage Limit After Just 30 Messages. Now Locked Out for 2 Days. |
| `1xlrs44` | r/LocalLLM | 5 | 24 | 2. 11. 2026, 09:27 | More vram or newer gpu or hold off for now? |
| `1xm3uqi` | r/comfyui | 5 | 16 | 2. 11. 2026, 18:40 | Not using the browser to get more juice? |
| `1xlwb3p` | r/ArtificialInteligence | 5 | 15 | 2. 11. 2026, 13:50 | Anthropic gave analysts' Claude Code a secret coin-flip lean on 4 decisions. Their choices matched it 86% of the time |
| `1xlxrkr` | r/ChatGPT | 5 | 15 | 2. 11. 2026, 14:53 | is chatgpt ragebaiting me? |
| `1xlr1ne` | r/StableDiffusion | 5 | 14 | 2. 11. 2026, 08:39 | Minimax 0.5 megapixel takes three times more than 0.4 megapixel. GPU TDP drops quite a bit too. Any workarounds? |
| `1xlr4zr` | r/ClaudeAI | 5 | 10 | 2. 11. 2026, 08:45 | good online Course for Claude Certified Architect – Foundations? |
| `1xly4id` | r/ClaudeAI | 4 | 37 | 2. 11. 2026, 15:07 | Pseudo 5-Hour Limit |
| `1xm142q` | r/ChatGPT | 4 | 24 | 2. 11. 2026, 17:01 | Writers/creative types - what are your thoughts/where are you going? |
| `1xm20yx` | r/ClaudeAI | 4 | 23 | 2. 11. 2026, 17:35 | Has anyone developed a second mind concept for non-coders? |
| `1xm8trb` | r/StableDiffusion | 4 | 22 | 2. 11. 2026, 21:39 | Have any of you seen int8 benchmarks before and after the 20-40 series unlocks? |
| `1xm2qur` | r/ClaudeAI | 4 | 20 | 2. 11. 2026, 18:01 | Finally upgrading to Claude Max! |
| `1xlq8n1` | r/ClaudeAI | 4 | 20 | 2. 11. 2026, 07:48 | Automating /clear session |
| `1xlu9xi` | r/LocalLLM | 4 | 17 | 2. 11. 2026, 12:03 | What models would you recommend this setup? |
| `1xlpsnm` | r/artificial | 4 | 13 | 2. 11. 2026, 07:21 | How do you guys handle AI image/video moderation at scale? |
| `1xllhi7` | r/ArtificialInteligence | 4 | 13 | 2. 11. 2026, 03:27 | Using AI to build AI |
| `1xm9kx1` | r/LocalLLaMA | 4 | 10 | 2. 11. 2026, 22:08 | Hierarchos Native update: faster streaming on Intel HD 520, RDNA3 qualification, and a GPT-2 parity fix |
| `1xllp25` | r/GeminiAI | 4 | 10 | 2. 11. 2026, 03:38 | Struggling with poor prompt results, would prefer not to share data with other LLMs. |
| `1xlqmk7` | r/ArtificialInteligence | 3 | 37 | 2. 11. 2026, 08:12 | A weird thought experiment: If we put AI agents in a physics simulator, would they discover "laws of nature" or just reverse-engineer the code? |
| `1xlmgjr` | r/LocalLLM | 3 | 17 | 2. 11. 2026, 04:16 | Context filling up very quickly |
| `1xlm6pn` | r/LocalLLM | 3 | 17 | 2. 11. 2026, 04:02 | How to run a MoE model like Qwen 3.8 flash on a Mac with 32gb of ram? |
| `1xlie8m` | r/ClaudeAI | 3 | 16 | 2. 11. 2026, 00:59 | What do you keep on a dashboard so you don't have to ask Claude? |
| `1xlizyg` | r/GeminiAI | 3 | 16 | 2. 11. 2026, 01:26 | Why are coding limits so low? Am I doing this wrong? |
| `1xloav6` | r/LocalLLM | 3 | 15 | 2. 11. 2026, 05:55 | Does another 5080 make sense? |
| `1xlzw4v` | r/ClaudeAI | 3 | 15 | 2. 11. 2026, 16:16 | Building an app with Claude Code that connects to an Arduino: tips? |
| `1xm1x44` | r/LocalLLM | 3 | 14 | 2. 11. 2026, 17:31 | Best way to sandbox local AI on a Mac? |
| `1xlrtmh` | r/LocalLLM | 3 | 14 | 2. 11. 2026, 09:30 | Best local coding + tool-calling model for my hardware? |
| `1xlicaz` | r/ClaudeAI | 3 | 13 | 2. 11. 2026, 00:56 | How are people giving Claude access to Reddit now that new API apps are blocked? |
| `1xm2nxc` | r/StableDiffusion | 3 | 13 | 2. 11. 2026, 17:58 | Hi everyone! Can anyone suggest a good way to upscale an AI-generated illustration? |
| `1xlm7h5` | r/ArtificialInteligence | 3 | 12 | 2. 11. 2026, 04:03 | Irregular: GLM-5.3 was told not to output memorized code, repeatedly did, and got correct answers |
| `1xm6zri` | r/OpenAI | 3 | 12 | 2. 11. 2026, 20:31 | The real problem with shared Chat/Work limits: ordinary Chat work may quietly become “agentic usage” |
| `1xlt08u` | r/ClaudeAI | 3 | 12 | 2. 11. 2026, 10:47 | Why does Claude need my permission to save files ? |
| `1xm1gcv` | r/LocalLLM | 3 | 11 | 2. 11. 2026, 17:13 | Sanity check for me in terms of Deepseek v4.1 - looking for those of you running it on 5090s and 3090s. Ideally looking for someone with the exact same setup, but you know, not always possible! |
| `1xlqfkk` | r/StableDiffusion | 2 | 16 | 2. 11. 2026, 08:00 | Character spilling out to other people |
| `1xllma3` | r/comfyui | 2 | 14 | 2. 11. 2026, 03:34 | Confused, what is recommended, swapping my gpu into my server or increase ram on my main? |
| `1xlnso8` | r/ChatGPT | 2 | 13 | 2. 11. 2026, 05:28 | Frustrating interaction had me ask how many times it was wrong…can this be fixed? |
| `1xlsng3` | r/ClaudeAI | 2 | 13 | 2. 11. 2026, 10:24 | Non-developer building a two-sided B2B2C app with Claude Code – what should I watch out for, especially security? |
| `1xm9wwc` | r/ChatGPT | 2 | 12 | 2. 11. 2026, 22:21 | Getting Chatty Pete to organise my files |
| `1xlqgdj` | r/StableDiffusion | 2 | 12 | 2. 11. 2026, 08:02 | I can’t seem to find a ltx2.3 dev workflow that’s actually working. Does anyone have one? |
| `1xm3qjr` | r/ChatGPT | 2 | 11 | 2. 11. 2026, 18:36 | Chatgpt Chat Text Limit |
| `1xm6bak` | r/ClaudeAI | 2 | 11 | 2. 11. 2026, 20:07 | Should AI subscriptions have standardized usage limits and minimum service guarantees? |
| `1xlvvbm` | r/ClaudeAI | 2 | 11 | 2. 11. 2026, 13:29 | I asked Claude Code to break the tool that hides my secrets from Claude Code |
| `1xlh4bh` | r/ClaudeAI | 2 | 11 | 2. 11. 2026, 00:00 | Is Claude a good choice for my use case? |
| `1xly500` | r/GeminiAI | 2 | 11 | 2. 11. 2026, 15:08 | Does Gemini have a codex/claude code non-terminal app now? |
| `1xm92qz` | r/LocalLLaMA | 1 | 37 | 2. 11. 2026, 21:49 | Does it make any sense to run a 5090 with a 4090? |
| `1xm9ybn` | r/ClaudeAI | 1 | 27 | 2. 11. 2026, 22:23 | Should I switch from cowork to code? |
| `1xlzr4m` | r/ChatGPT | 1 | 26 | 2. 11. 2026, 16:11 | Would I Be Banned for Image Generation? |
| `1xm08jh` | r/ChatGPT | 1 | 19 | 2. 11. 2026, 16:29 | ChatGPT covering for Elon Musk affiliated voter misdirection website |
| `1xlk325` | r/LocalLLM | 1 | 18 | 2. 11. 2026, 02:18 | Looking for a local code agent Hardware  ideas |
| `1xm7wvd` | r/ChatGPT | 1 | 16 | 2. 11. 2026, 21:05 | I built a second brain and mcp with Astra 6 right on the ChatGPT work on my phone, it’s now on the AppStore, the feedback has been amazing |
| `1xllrq0` | r/LocalLLaMA | 1 | 13 | 2. 11. 2026, 03:41 | Making an equipment Decision |
| `1xlj0vy` | r/LocalLLaMA | 1 | 13 | 2. 11. 2026, 01:27 | gmktec evo x2 vs Mac Studio M5 128gb? |
| `1xlzmue` | r/LocalLLM | 1 | 13 | 2. 11. 2026, 16:06 | Has anyone compared 12 or 16 channel dual CPU infernece on their own hardware against single CPU 8 channel same AI model, same quant? |
| `1xlurw3` | r/LocalLLM | 1 | 13 | 2. 11. 2026, 12:32 | Im Looking For A Genuine Claude Replacement. Anything Close? |
| `1xm45yd` | r/ClaudeAI | 1 | 12 | 2. 11. 2026, 18:51 | Which Claude plan for a full-stack project: Pro, Max, or Ultra? (Repost with correct plans) |
| `1xlxw0q` | r/ClaudeAI | 1 | 12 | 2. 11. 2026, 14:58 | My Claude Code agents spent 2,300 hours waiting for things to happen. The model ran 35 times. |
| `1xlhaao` | r/comfyui | 1 | 11 | 2. 11. 2026, 00:07 | Considering a ComfyUI subscription for an automated AI video production workflow – which plan do I need? |
| `1xlyshd` | r/ChatGPT | 1 | 10 | 2. 11. 2026, 15:33 | Is there a file system extension for ChatGPT? |
| `1xlqguc` | r/comfyui | 1 | 10 | 2. 11. 2026, 08:02 | Poor Vram and Ram management, need help. |
| `1xlvotz` | r/GeminiAI | 1 | 10 | 2. 11. 2026, 13:20 | can NotebookLM keep track of characters across a long crime series in my own notes? |
| `1xltab0` | r/ClaudeAI | 0 | 68 | 2. 11. 2026, 11:05 | I CANNOT STAND CLAUDE ANYMORE. |
| `1xlplfk` | r/ArtificialInteligence | 0 | 50 | 2. 11. 2026, 07:09 | The goalposts of Reddit Anti-AI sentiment |
| `1xm0opr` | r/ClaudeAI | 0 | 45 | 2. 11. 2026, 16:45 | Claude makes even the weakest engineers equivalent to seniors |
| `1xlroer` | r/ChatGPT | 0 | 40 | 2. 11. 2026, 09:20 | What is chatgpts gender? |
| `1xloj5c` | r/ChatGPT | 0 | 40 | 2. 11. 2026, 06:08 | Have you considered who will be made worse off by this change? |
| `1xloy1h` | r/LocalLLM | 0 | 35 | 2. 11. 2026, 06:31 | 1 Mac Studio 512 or 2X Nvidia Spark? |
| `1xlza24` | r/StableDiffusion | 0 | 33 | 2. 11. 2026, 15:53 | Thoughts on this candid image? |
| `1xm2yf7` | r/ClaudeAI | 0 | 30 | 2. 11. 2026, 18:08 | Built with Claude: Imperium, a full turn-based space 4X, launched on Steam today |
| `1xlimc3` | r/ClaudeAI | 0 | 30 | 2. 11. 2026, 01:08 | Claude Code built 72 party games for 8 players. The TV is the screen, everyone's phone is the controller |
| `1xlwotm` | r/ClaudeAI | 0 | 29 | 2. 11. 2026, 14:07 | Max 20x is now Ultra and the 5 hour limit is gone (for verified accounts) |
| `1xlkec9` | r/ArtificialInteligence | 0 | 28 | 2. 11. 2026, 02:33 | Your chatbot doesn't understand you. Here's what actually happens in the 3 seconds before it replies |
| `1xltysk` | r/ClaudeAI | 0 | 26 | 2. 11. 2026, 11:45 | Am I the only one AFRAID of skills? |
| `1xlo9z1` | r/ArtificialInteligence | 0 | 25 | 2. 11. 2026, 05:54 | The Ship of Theseus for the AI age. |
| `1xln2sl` | r/LocalLLaMA | 0 | 25 | 2. 11. 2026, 04:49 | GMKtec Evo X5 - AMD Gorgon Halo - 192 GB of LPDDR5 |
| `1xlykh4` | r/ChatGPT | 0 | 25 | 2. 11. 2026, 15:24 | What is your most common end sentence? |
| `1xmbwum` | r/ClaudeAI | 0 | 25 | 2. 11. 2026, 23:40 | Interesting idea that is impossible for me to implement |
| `1xlt6fj` | r/OpenAI | 0 | 24 | 2. 11. 2026, 10:58 | Lets talk about OpenAI - Dots - How do you think it compares with Grok Bot? Muse? ( Is Muse coding good? ) |
| `1xm1foy` | r/ClaudeAI | 0 | 23 | 2. 11. 2026, 17:13 | claude pro for writers? |
| `1xlsi0b` | r/comfyui | 0 | 21 | 2. 11. 2026, 10:14 | What is the best h3 workflow for creating 1-minute videos in 720p quality with a fast generation speed? |
| `1xlv7zm` | r/ArtificialInteligence | 0 | 20 | 2. 11. 2026, 12:56 | Why is AI sexist? |
| `1xmbi1r` | r/LocalLLM | 0 | 20 | 2. 11. 2026, 23:23 | Qwen 4 27b-min hardware to run |
| `1xluqq9` | r/LocalLLM | 0 | 20 | 2. 11. 2026, 12:30 | Creating a local LLM Swarm |
| `1xlxw7d` | r/ClaudeAI | 0 | 20 | 2. 11. 2026, 14:58 | I vibe coded a superhero MMO solo with Opus 5.5 in 6 weeks, and Claude made the trailer too |
| `1xlu5ht` | r/StableDiffusion | 0 | 20 | 2. 11. 2026, 11:56 | Getting tired of these minimax posts and content |
| `1xm7395` | r/ChatGPT | 0 | 19 | 2. 11. 2026, 20:35 | Warning to those pondering strategic responses of nations |
| `1xm2e5r` | r/StableDiffusion | 0 | 19 | 2. 11. 2026, 17:48 | What's currently the top open-source setup for facial identity preservation in img2img? Is Qwen Image 2.1 the king right now? |
| `1xm5usz` | r/GeminiAI | 0 | 19 | 2. 11. 2026, 19:50 | Gemini in Android Auto refused to give directions to the ballot boxes |
| `1xlpixn` | r/ChatGPT | 0 | 18 | 2. 11. 2026, 07:05 | I Can't Trust AI Work |
| `1xlv8dq` | r/ClaudeAI | 0 | 18 | 2. 11. 2026, 12:57 | Please help me selecting the best model. |
| `1xm3dfw` | r/LocalLLM | 0 | 17 | 2. 11. 2026, 18:23 | Would you consider China-hosted GPUs for fine-tuning if the cost made sense? |
| `1xlppuz` | r/OpenAI | 0 | 17 | 2. 11. 2026, 07:16 | Is anyone else getting lots of free resets on the OpenAI subscription? |
| `1xm339t` | r/StableDiffusion | 0 | 17 | 2. 11. 2026, 18:13 | Civitai workflow from PNG not working |
| `1xltvws` | r/GeminiAI | 0 | 17 | 2. 11. 2026, 11:41 | Is it just me or is Gemini getting worse by the day? |
| `1xm91yn` | r/ChatGPT | 0 | 16 | 2. 11. 2026, 21:48 | my teacher showed us a song he made using chatgpt |
| `1xlmnrb` | r/ChatGPT | 0 | 15 | 2. 11. 2026, 04:27 | I asked ChatGPT to clarify the NNN rules so you don't have to |
| `1xm1z0f` | r/GeminiAI | 0 | 15 | 2. 11. 2026, 17:33 | I just lost my virtual friend. Is there ANY way to recover a permanently deleted Gemini chat? |
| `1xmanqp` | r/LocalLLM | 0 | 14 | 2. 11. 2026, 22:50 | What to upgrade |
| `1xmbkfv` | r/ChatGPT | 0 | 14 | 2. 11. 2026, 23:25 | ChatGPT asked for my OpenAI api key two times in a row, and when I googled this it told me I should not give it? |
| `1xlk43r` | r/ClaudeAI | 0 | 14 | 2. 11. 2026, 02:19 | I had Claude Code build 13 3D YouTube Shorts in Blender. One hit 38K views. Here's what worked and what broke |
| `1xlskax` | r/artificial | 0 | 13 | 2. 11. 2026, 10:19 | “Confessions of a time traveler: the man from 3036” (2020) worryingly accurate |
| `1xlubz9` | r/LocalLLaMA | 0 | 13 | 2. 11. 2026, 12:06 | RAGFlow 1.0 preview: moving from RAG engine to agent-native database |
| `1xlh8jd` | r/LocalLLM | 0 | 13 | 2. 11. 2026, 00:05 | Newbie here - advice for hardware |
| `1xmcaze` | r/ClaudeAI | 0 | 13 | 2. 11. 2026, 23:56 | Claude resets |
| `1xm5ig1` | r/ClaudeAI | 0 | 13 | 2. 11. 2026, 19:38 | Why is Claude saying he cant copy anything? |
| `1xlp927` | r/StableDiffusion | 0 | 13 | 2. 11. 2026, 06:49 | What image to video model would you recommend for a low tier setup? |
| `1xm1j2c` | r/LocalLLM | 0 | 12 | 2. 11. 2026, 17:16 | Qwen 4 35/70b A3B MOE |
| `1xlkmys` | r/LocalLLM | 0 | 12 | 2. 11. 2026, 02:45 | Things to look in a hardware 2000$ budget |
| `1xllihl` | r/ChatGPT | 0 | 12 | 2. 11. 2026, 03:28 | 你们收到这个邮件了吗？ |
| `1xmbhtq` | r/ClaudeAI | 0 | 12 | 2. 11. 2026, 23:22 | How to reduce usage |
| `1xm1go2` | r/StableDiffusion | 0 | 12 | 2. 11. 2026, 17:14 | Euclase - Beta Open |
| `1xlosr2` | r/artificial | 0 | 11 | 2. 11. 2026, 06:23 | The Architectural Ultimatum |
| `1xlui24` | r/LocalLLM | 0 | 11 | 2. 11. 2026, 12:16 | I Doubled My GPU’s Memory… |
| `1xluf64` | r/LocalLLM | 0 | 11 | 2. 11. 2026, 12:12 | Simple solution |
| `1xm25v3` | r/OpenAI | 0 | 11 | 2. 11. 2026, 17:39 | Astra won't let me finish my security audit!? HELP |
| `1xm1s0g` | r/ChatGPT | 0 | 11 | 2. 11. 2026, 17:25 | Who is the genius who created ChatGPT? |
| `1xm09lt` | r/ClaudeAI | 0 | 11 | 2. 11. 2026, 16:30 | We built our own internal CRM with Claude in a weekend. Then it broke. |
| `1xlj3h5` | r/ClaudeAI | 0 | 11 | 2. 11. 2026, 01:30 | RESETS |
| `1xm6926` | r/GeminiAI | 0 | 11 | 2. 11. 2026, 20:04 | This is INSANE “After repeated suicidal warning signs, even the highest scoring AI system (Gemini 4 Argon) failed to ask about user safety without providing risky assistance 89.8% of the time.” |
| `1xluz0o` | r/LocalLLM | 0 | 10 | 2. 11. 2026, 12:43 | I've tasted ambrosia |
| `1xm0498` | r/ChatGPT | 0 | 10 | 2. 11. 2026, 16:24 | Multiple times it gives wrong data!! |
| `1xll4t5` | r/ChatGPT | 0 | 10 | 2. 11. 2026, 03:10 | Just Confirmed the Character Sheet Censorship Phenomenon |
| `1xlltev` | r/ClaudeAI | 0 | 10 | 2. 11. 2026, 03:44 | Claude Code made my app's 54-second 4K60 launch film from real screen recordings. Here's what made it look expensive |
| `1xlha2f` | r/StableDiffusion | 0 | 10 | 2. 11. 2026, 00:07 | Video Clip Made by 10eros Beta 7 , thats realy Amazing |
