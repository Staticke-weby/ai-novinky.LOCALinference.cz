# AI souhrn z Redditu – 13. listopad 2026

## Metodika

Data pocházejí z přímého webového sběru Redditu (`scripts/rd-collect-web.py`) za den 13. 11. 2026 (Europe/Prague), skóre a počty komentářů jsou hodnoty z doby sběru. Databáze obsahuje 961 postů, z toho 353 s alespoň 10 komentáři; pro 40 nejlepších vznikl podrobný balíček s komentáři a odkazovaným článkem.

Z nabídky bylo vyřazeno 29 kandidátů, kteří opakují témata z předchozích tří dnů: 12 postů kolem rezignace Jensena Huanga a Nvidie, 4 kolem Gemini 4 Hydrogen, 2 kolem čínských modelů na exportovaných Blackwell čipech, 2 kolem Fable 5.2, 1 kolem Hugging Face a Huangova odchodu a 8 memů či příspěvků s nízkou relevancí. Šest témat mimo původní balíčky (OpenAI robotika, ExploitGym, ChatGPT Wallet, LFM3, Edge0-145B, CXMT) bylo dohledáno v `dataset.json` a doplněno vlastním balíčkem.

Vzniklo 17 článků. Duplicitní posty ke stejnému videu jsou sloučené a odkázané v článku. Příloha obsahuje všechny posty s alespoň 10 komentáři, u sloučených témat odkazuje na článek, do kterého byly zařazeny.

## Články

| # | Titulek | Subreddit | Skóre | Komentářů |
|---|---|---|---:|---:|
| 1 | [ChatGPT se po deseti dnech ozval sám. Uživatelé sbírají nevyžádané zprávy](1xv32sv_chatgpt-nevyzadana-zprava-po-deseti-dnech.md) | r/ChatGPT | 2249 | 891 |
| 2 | [FAA nasadila AI na řízení letového provozu. Nástroj stál 875 milionů dolarů](1xvl00y_faa-ai-rizeni-letoveho-provozu.md) | r/singularity | 1674 | 320 |
| 3 | [llama.cpp vydal verzi 1.0. Lokální inference dostala stabilní základ](1xv8t2e_llama-cpp-verze-1-0.md) | r/LocalLLaMA | 1532 | 187 |
| 4 | [Na Steamu přiznal každý AI díl své hry. Disclaimery se staly hlavním tématem](1xus0wz_steam-ai-disclosure-hra-mend.md) | r/ClaudeAI | 920 | 818 |
| 5 | [Necenzurované modely frčí. Lidé porovnávají DeepSeek, Qwen a GLM bez odmítání](1xutc35_necenzurovane-modely-deepseek-qwen-glm.md) | r/LocalLLM | 610 | 306 |
| 6 | [Dario Amodei si rýpl do konkurence: my modely neavizujeme, my je vydáváme](1xvi97m_dario-amodei-bez-avizovani-modelu.md) | r/singularity | 586 | 78 |
| 7 | [A100 zlevnily o 20 až 30 procent. Trh s ojetými GPU se hroutí](1xuxbeb_a100-ceny-pokles-20-30-procent.md) | r/LocalLLaMA | 439 | 232 |
| 8 | [Necenzurovaný Qwen-Image-2.1 vystoupal vysoko v trendech Hugging Face](1xvc0lz_qwen-image-2-1-uncensored-hugging-face.md) | r/StableDiffusion | 396 | 101 |
| 9 | [Pangram CEO: otázka na svačinu v přihlášce zkrátí revizi o 60 procent](1xvizxy_pangram-svacina-v-prihlasce.md) | r/singularity | 611 | 101 |
| 10 | [Syn vytáhl z kůlny 3090ky z těžby. Otec na nich rozjel lokální AI](1xvbcfp_syn-3090-z-etherea-lokalni-ai.md) | r/LocalLLaMA | 411 | 112 |
| 11 | [Umělá videa už nejde rozeznat. Diskuse: děti neuvěří ničemu, co uvidí](1xvfehk_umela-videa-realita-deepfake-diskuse.md) | r/OpenAI | 1587 | 298 |
| 12 | [OpenAI zrušila samostatný robotický tým. Výzkumníky přesunula k obecným modelům](1xvgyfd_openai-zruseni-robotickeho-tymu.md) | r/singularity | 294 | 56 |
| 13 | [OpenAI interní model ExploitGym: 77 procent, Anthropic 39](1xurxd4_openai-exploitgym-77-procent.md) | r/OpenAI | 238 | 112 |
| 14 | [ChatGPT Wallet: agenti nakupují, ale každý nákup musí schválit uživatel](1xvd1ci_chatgpt-wallet-nakupy-agentem.md) | r/OpenAI | 132 | 42 |
| 15 | [Liquid AI vydala LFM3. Dvoumiliardové multimodální modely slibují rychlost](1xuz7ao_liquid-ai-lfm3-modely.md) | r/LocalLLM | 169 | 72 |
| 16 | [Edge0-145B: open-source model se 145 miliardami parametrů běží na vlastním počítači](1xuuq0b_edge0-145b-lokalni-model.md) | r/LocalLLaMA | 144 | 36 |
| 17 | [CXMT ztrojnásobí výrobu RAM. Čínské paměti mají uvolnit AI trh](1xvam8o_cxmt-ztrojnasobi-vyrobu-ram.md) | r/LocalLLaMA | 172 | 65 |

## Příloha: všechny posty s alespoň 10 komentáři

| ID | Subreddit | Skóre | Komentářů | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1xv19ci | r/ChatGPT | 5526 | 298 | 13. 11. 2026, 08:10 | Whole cinematic universe be like |
| 1xvghd1 | r/ClaudeAI | 3608 | 326 | 13. 11. 2026, 20:00 | Fable 5.2 painting in MS Paint |
| 1xuvexw | r/LocalLLaMA | 2955 | 577 | 13. 11. 2026, 02:58 | Stories coming out about Jensen |
| 1xva8yj | r/singularity | 2766 | 141 | 13. 11. 2026, 16:06 | Huang: The Game |
| 1xv4jdb | r/GeminiAI | 2259 | 129 | 13. 11. 2026, 11:36 | Asking Gemini Hydrogen for help was my biggest mistake 💔 |
| [1xv32sv](1xv32sv_chatgpt-nevyzadana-zprava-po-deseti-dnech.md) | r/ChatGPT | 2249 | 891 | 13. 11. 2026, 10:04 | ChatGPT randomly sent me an unsolicited follow-up message |
| 1xv9pff | r/OpenAI | 2208 | 392 | 13. 11. 2026, 15:44 | Investigators have discovered that the top 4 Chinese AI labs all built their newest models on NVIDIA’s most advanced Blackwell chips, which are barred from export to China. |
| 1xuxxmb | r/LocalLLaMA | 1921 | 549 | 13. 11. 2026, 05:03 | ‘Bring Back THE Boss’: Nvidia Employees Petition for Jensen Huang’s Return |
| 1xv4wg4 | r/ChatGPT | 1890 | 41 | 13. 11. 2026, 11:58 | Jensen Huang singing his resignation, 2026, colorized |
| 1xv64tw | r/ChatGPT | 1822 | 36 | 13. 11. 2026, 13:04 | Day in the life of Jensen Huang |
| [1xvl00y](1xvl00y_faa-ai-rizeni-letoveho-provozu.md) | r/singularity | 1674 | 320 | 13. 11. 2026, 22:56 | The FAA rolled out its $875 million AI Air Traffic tool today with reassurances it would not affect safety |
| [1xvfehk](1xvfehk_umela-videa-realita-deepfake-diskuse.md) | r/OpenAI | 1587 | 298 | 13. 11. 2026, 19:19 | The next generation will never see a real video |
| 1xutg3x | r/ChatGPT | 1535 | 113 | 13. 11. 2026, 01:25 | The Office AI: Jensen Huang gets a new job at Dunder Mifflin WATCH TILL THE END! |
| [1xv8t2e](1xv8t2e_llama-cpp-verze-1-0.md) | r/LocalLLaMA | 1532 | 187 | 13. 11. 2026, 15:07 | llama.cpp v1.0 is here 🦙 |
| 1xut4o7 | r/LocalLLaMA | 1367 | 115 | 13. 11. 2026, 01:11 | Hugging Face CEO vows to keep fighting for open source AI after Jensen Huang's exit |
| [1xvffkv](1xvfehk_umela-videa-realita-deepfake-diskuse.md) | r/ChatGPT | 1359 | 248 | 13. 11. 2026, 19:20 | The next generation will never see a real video |
| 1xv1dcj | r/ArtificialInteligence | 1352 | 18 | 13. 11. 2026, 08:16 | Love in the days of AI |
| 1xvfcho | r/StableDiffusion | 1342 | 125 | 13. 11. 2026, 19:17 | What's the best model for generating images like this? My goal is to generate images, then use MiniMax for I2V to create videos like this |
| 1xv707t | r/GeminiAI | 1073 | 45 | 13. 11. 2026, 13:48 | Saw others try it so I did too |
| 1xvf4gd | r/singularity | 992 | 60 | 13. 11. 2026, 19:09 | Nvidia should hire Lisa. AMD should hire Jensen. Both win. We all win. AI bubble cancelled. |
| 1xvbea9 | r/ChatGPT | 937 | 33 | 13. 11. 2026, 16:51 | Worth a Shot 💔🥀 |
| [1xus0wz](1xus0wz_steam-ai-disclosure-hra-mend.md) | r/ClaudeAI | 920 | 818 | 13. 11. 2026, 00:22 | I disclosed every AI-made part of my solo game on Steam. The disclaimer is one of the main things people comment on. |
| 1xv3djt | r/ChatGPT | 914 | 49 | 13. 11. 2026, 10:23 | Jensen when diversifying his portfolio |
| 1xuvian | r/GeminiAI | 880 | 133 | 13. 11. 2026, 03:03 | Google might actually have cooked with Hydrogen |
| 1xv0vte | r/ClaudeAI | 850 | 42 | 13. 11. 2026, 07:47 | Dumbest way to burn credits |
| 1xv16md | r/ArtificialInteligence | 719 | 63 | 13. 11. 2026, 08:05 | Pray for me guys... |
| 1xvibfo | r/ChatGPT | 656 | 76 | 13. 11. 2026, 21:10 | Bruh |
| 1xv4qvh | r/singularity | 631 | 63 | 13. 11. 2026, 11:49 | Jensen distracted by the Woman in Red while Trump explains the Matrix |
| 1xv8f1n | r/ArtificialInteligence | 620 | 204 | 13. 11. 2026, 14:51 | Investigators have discovered that the top 4 Chinese AI labs all built their newest models on NVIDIA’s most advanced Blackwell chips, which are barred from export to China. |
| [1xvizxy](1xvizxy_pangram-svacina-v-prihlasce.md) | r/singularity | 611 | 101 | 13. 11. 2026, 21:37 | Pangram CEO: We ask for their favourite snack in our job application, and it cuts down on our application review by 60% |
| [1xutc35](1xutc35_necenzurovane-modely-deepseek-qwen-glm.md) | r/LocalLLM | 610 | 306 | 13. 11. 2026, 01:20 | Uncensored models are awesome |
| [1xvi97m](1xvi97m_dario-amodei-bez-avizovani-modelu.md) | r/singularity | 586 | 78 | 13. 11. 2026, 21:07 | Dario woke up and chose violence: "We don't vague post about models ahead of time. We basically build the model, we make sure it's good, we release the model." |
| 1xvfh47 | r/LocalLLM | 583 | 269 | 13. 11. 2026, 19:22 | it feels like they just wanted Huang gone because he supported Open Source & Open Weight models |
| 1xuuabz | r/ClaudeAI | 555 | 113 | 13. 11. 2026, 02:04 | Anthropic are discouraging using Fable as a coordinator for Projects |
| 1xv3hvm | r/LocalLLM | 525 | 70 | 13. 11. 2026, 10:30 | Anthropic after realizing it can just buy NVIDIA with its IPO money |
| 1xv0oy0 | r/GeminiAI | 455 | 67 | 13. 11. 2026, 07:35 | Google definitely cook with Hydrogen 4 bro, it's too good for free AI |
| 1xvc5qe | r/OpenAI | 445 | 33 | 13. 11. 2026, 17:19 | Worth a Shot 💔🥀 |
| [1xuxbeb](1xuxbeb_a100-ceny-pokles-20-30-procent.md) | r/LocalLLaMA | 439 | 232 | 13. 11. 2026, 04:31 | A100 prices down 20-30% since my post about them collapsing |
| [1xvbcfp](1xvbcfp_syn-3090-z-etherea-lokalni-ai.md) | r/LocalLLaMA | 411 | 112 | 13. 11. 2026, 16:49 | Look what my son gave me! |
| [1xvc0lz](1xvc0lz_qwen-image-2-1-uncensored-hugging-face.md) | r/StableDiffusion | 396 | 101 | 13. 11. 2026, 17:14 | Our uncensored Qwen-Image-2.1 model just reached No.2 of page 1 on Hugging Face’s Qwen rankings—and page 2 across all trending models! |
| 1xuznt8 | r/LocalLLM | 388 | 198 | 13. 11. 2026, 06:36 | Local AI is under attack. |
| 1xuxmu5 | r/StableDiffusion | 375 | 59 | 13. 11. 2026, 04:47 | GPU died of a broken heart |
| 1xv44ih | r/ChatGPT | 335 | 81 | 13. 11. 2026, 11:10 | New CEO Announcement Already! |
| 1xusyqa | r/ArtificialInteligence | 324 | 177 | 13. 11. 2026, 01:04 | Microsoft outage |
| 1xv4g1n | r/singularity | 318 | 131 | 13. 11. 2026, 11:30 | Polymarket has google as the owner of the best AI model by the end of the month and year |
| 1xusj0t | r/ClaudeAI | 316 | 81 | 13. 11. 2026, 00:45 | I hate how Claude formulates responses, they are very hard to read |
| [1xvgyfd](1xvgyfd_openai-zruseni-robotickeho-tymu.md) | r/singularity | 294 | 56 | 13. 11. 2026, 20:17 | OpenAI disbands its stand-alone robotics team as its general-purpose AI models start running robots |
| 1xv5xvm | r/GeminiAI | 292 | 131 | 13. 11. 2026, 12:55 | Good news for promotional pro users, plus and free users! |
| 1xuw9zm | r/LocalLLM | 284 | 71 | 13. 11. 2026, 03:40 | Adding three AI Pro 9700s this weekend! |
| 1xvcqj1 | r/GeminiAI | 269 | 47 | 13. 11. 2026, 17:41 | Hydrogen is best model for daily use on market right now. If you compare speed (end to end task), token efficiency and inteligence itself |
| 1xuxvgo | r/ArtificialInteligence | 252 | 174 | 13. 11. 2026, 05:00 | Nvidia staff are petitioning to bring Jensen back, and I've come around to it |
| 1xv8aci | r/agi | 252 | 44 | 13. 11. 2026, 14:46 | Investigators have discovered that the top 4 Chinese AI labs all built their newest models on NVIDIA’s most advanced Blackwell chips, which are barred from export to China. |
| 1xuy74i | r/artificial | 241 | 131 | 13. 11. 2026, 05:17 | Former US AI Czar David Sacks says there’s no evidence that Alice Huang was a Chinese Spy |
| [1xurxd4](1xurxd4_openai-exploitgym-77-procent.md) | r/OpenAI | 238 | 112 | 13. 11. 2026, 00:18 | OpenAI’s internal cyber model hit 77.0% on ExploitGym — nearly double Anthropic’s Mythos 5.2 (39.2%) |
| 1xuy0gk | r/GeminiAI | 224 | 30 | 13. 11. 2026, 05:07 | Sam and Dario after Hydrogen 4 |
| 1xurkxi | r/GeminiAI | 221 | 34 | 13. 11. 2026, 00:03 | Hydrogen 4. High Vs Sol 6.1 Max/ Extra high (long term user) |
| 1xuydzd | r/singularity | 207 | 70 | 13. 11. 2026, 05:27 | US intel isn’t sure if businesswoman spied on Nvidia for China, doesn’t mean she wasn’t a risk, sources say |
| 1xv1ql8 | r/StableDiffusion | 197 | 73 | 13. 11. 2026, 08:40 | KREA2 vs Z-Image vs Moss vs Qwen 2.1 Which one should I choose? |
| 1xv1bru | r/GeminiAI | 191 | 14 | 13. 11. 2026, 08:14 | Google Methane: Carbon with 4 Hydrogen subagents |
| 1xuscpa | r/LocalLLM | 189 | 19 | 13. 11. 2026, 00:37 | [Crazy AI Lawyer] My Claude legal harness now runs 100% local on DeepSeek-V4.1-Flash: eight 2018 V100s at near-NVFP4 quality, 524K context, 100+ tok/s. Not as good as frontier, but it replaces real work today |
| 1xvjsog | r/StableDiffusion | 187 | 53 | 13. 11. 2026, 22:08 | MiniMax H3 Image is kind of insane for editing at 60MP - Concept to Realistic |
| 1xutknf | r/ClaudeAI | 179 | 145 | 13. 11. 2026, 01:31 | Anthropic’s IPO is reportedly 6x oversubscribed... the biggest AI market test yet |
| 1xv3qth | r/GeminiAI | 178 | 44 | 13. 11. 2026, 10:47 | Hydrogen is gonna get replaced soon? |
| 1xvh4ag | r/LocalLLaMA | 177 | 24 | 13. 11. 2026, 20:23 | Weight Space Programming for Quantization: Nace quants achieve up to 2x better KL divergence for Qwen 9B, 27B, 35B & Flash Next [GGUF] |
| 1xvcg52 | r/singularity | 175 | 51 | 13. 11. 2026, 17:30 | Some Benchmarks Where Humans Still Beat Frontier LLMs |
| [1xvam8o](1xvam8o_cxmt-ztrojnasobi-vyrobu-ram.md) | r/LocalLLaMA | 172 | 65 | 13. 11. 2026, 16:21 | CXMT almost tripling RAM production from 2025 to 2028 |
| [1xuz7ao](1xuz7ao_liquid-ai-lfm3-modely.md) | r/LocalLLM | 169 | 72 | 13. 11. 2026, 06:11 | Why is no one talking about LFM3 models |
| 1xv03n0 | r/GeminiAI | 157 | 85 | 13. 11. 2026, 07:01 | when Gemini 4 Hydrogen-High is already so smart and fast, whats the point in using 3.1pro? |
| 1xv6xud | r/ChatGPT | 152 | 15 | 13. 11. 2026, 13:45 | best use case of AI by far... |
| [1xuuq0b](1xuuq0b_edge0-145b-lokalni-model.md) | r/LocalLLaMA | 144 | 36 | 13. 11. 2026, 02:25 | Edge0-145B: Open-Source On-Device AI with 145B Parameters |
| 1xuwf9w | r/LocalLLaMA | 143 | 87 | 13. 11. 2026, 03:47 | US intel isn’t sure if businesswoman spied on Nvidia for China, doesn’t mean she wasn’t a risk, sources say |
| 1xuzlpu | r/ClaudeAI | 142 | 144 | 13. 11. 2026, 06:33 | What would you do if there's a Claude outage? |
| 1xv2ck8 | r/singularity | 140 | 14 | 13. 11. 2026, 09:17 | A Data Center with zero water use, 100% renewable energy (1.17g CO2/kWh) and a 1.15 PUE, all made from wood |
| 1xvijhy | r/singularity | 138 | 47 | 13. 11. 2026, 21:19 | inside you there are two wolves |
| 1xvhaf3 | r/StableDiffusion | 137 | 20 | 13. 11. 2026, 20:30 | Physics understanding of MiniMax H3 |
| 1xuw231 | r/ArtificialInteligence | 135 | 16 | 13. 11. 2026, 03:29 | NVIDIA Powers. |
| 1xvjzer | r/ArtificialInteligence | 133 | 23 | 13. 11. 2026, 22:15 | 'Sabotaged': Microsoft Outage Sparks Fears of 'Insider Threat' Amid Massive Global Tech Chaos |
| [1xvd1ci](1xvd1ci_chatgpt-wallet-nakupy-agentem.md) | r/OpenAI | 132 | 42 | 13. 11. 2026, 17:52 | OpenAI introduces ChatGPT Wallet so agents can complete purchases with user approval |
| 1xvje07 | r/singularity | 128 | 33 | 13. 11. 2026, 21:52 | Recursive self-improvement has started |
| 1xvhnsq | r/GeminiAI | 125 | 12 | 13. 11. 2026, 20:44 | Gemini Hydrogen kicks ass! |
| 1xvivdy | r/artificial | 123 | 80 | 13. 11. 2026, 21:32 | OpenAI is so convinced that LLMs will become brains for robots that it has disbanded its robotics team |
| 1xveugv | r/ClaudeAI | 123 | 12 | 13. 11. 2026, 18:59 | Claude Code limits in a desktop pet |
| 1xuxuov | r/LocalLLM | 122 | 35 | 13. 11. 2026, 04:59 | GPU died of a broken heart |
| 1xvbhjz | r/singularity | 122 | 30 | 13. 11. 2026, 16:55 | ASUS teases their first humanoid robot |
| 1xus81t | r/LocalLLaMA | 120 | 43 | 13. 11. 2026, 00:31 | Lawyer with too many GPUs, part 5: DeepSeek-V4.1-Flash at near-NVFP4 quality on eight V100s from 2018. 524K context, 100+ tok/s decode, ~160 tok/s with two chats at once, and my legal harness now runs on it, 100% local |
| 1xvesum | r/StableDiffusion | 115 | 30 | 13. 11. 2026, 18:57 | Minimax H3 Image is awesome - Please don't confuse photographic realism with sharpness |
| 1xvbith | r/LocalLLaMA | 108 | 22 | 13. 11. 2026, 16:56 | e-means: 10x faster k-means at equal loss |
| 1xuzy9u | r/StableDiffusion | 105 | 35 | 13. 11. 2026, 06:53 | Famegrid Spice V2 Krea 2 |
| 1xvkzvl | r/ChatGPT | 104 | 11 | 13. 11. 2026, 22:56 | Chatgpt gone wrong |
| 1xv581p | r/GeminiAI | 102 | 14 | 13. 11. 2026, 12:15 | Hydrogen is absolutely amazing! |
| 1xut32q | r/ClaudeAI | 101 | 66 | 13. 11. 2026, 01:09 | Isn’t it funny how quickly people who were extremely anti AI changed their mind the second it created something they want to use. |
| 1xvinch | r/artificial | 101 | 31 | 13. 11. 2026, 21:23 | "We are deeply sorry" Microsoft apologizes for major outage that knocked Outlook, Teams, and Microsoft 365 offline for 24 hours – insists it wasn't AI that caused it |
| 1xv0rsw | r/ChatGPT | 100 | 14 | 13. 11. 2026, 07:40 | Sam Altman after the RAM shortage hits😭 |
| 1xv2onx | r/GeminiAI | 100 | 14 | 13. 11. 2026, 09:39 | Hydrogen is surprisingly fast |
| 1xutred | r/ArtificialInteligence | 99 | 53 | 13. 11. 2026, 01:40 | 6 Chinese AI models, including DeepSeek V4 and Kimi K3, carry the fingerprint of export-banned Nvidia Blackwell chips, per a new forensic report |
| 1xv8jg2 | r/StableDiffusion | 97 | 41 | 13. 11. 2026, 14:56 | Simple vs Detailed prompts (Minimax H3-Img, Minimax H3 stills, Iris Z, Moss, Qwen and Krea2) |
| 1xv2e0a | r/LocalLLaMA | 96 | 118 | 13. 11. 2026, 09:20 | Google is asking |
| 1xuvob3 | r/ChatGPT | 95 | 75 | 13. 11. 2026, 03:11 | Is this supposed to happen orr... |
| 1xv8bld | r/ClaudeAI | 95 | 18 | 13. 11. 2026, 14:47 | Claude used boogie nights nude scene for testing |
| 1xv5eff | r/GeminiAI | 94 | 37 | 13. 11. 2026, 12:26 | It currently appears that Pro users will NOT get Carbon. |
| 1xv94ps | r/GeminiAI | 94 | 22 | 13. 11. 2026, 15:20 | Hydrogen is twice as fast as 3.8 Flash. We're staying on Flash until January anyway |
| 1xute2l | r/ChatGPT | 92 | 331 | 13. 11. 2026, 01:23 | The difference between Standard vs Live voice |
| 1xuxgu0 | r/LocalLLM | 92 | 14 | 13. 11. 2026, 04:39 | M5 Max 128GB running Qwen3.8 Flash Next as a real agent all day: ~68 tok/s at 100k-190k context, plus what I learned making local agent automations actually reliable |
| 1xvcgxq | r/LocalLLaMA | 90 | 43 | 13. 11. 2026, 17:31 | DeepSeek flash max is the first model to reach >1% on challenging SWE-sweep bug finding benchmark |
| 1xvbn2m | r/LocalLLaMA | 87 | 25 | 13. 11. 2026, 17:00 | Qwen3.5-9B running on a PS4’s GPU, offline, using its own MTP head for speculative decoding |
| 1xv50sl | r/ClaudeAI | 83 | 88 | 13. 11. 2026, 12:04 | Claude chat vs Claude Code: am I managing my projects wrong, or is Code just better at everything? |
| 1xuswgk | r/singularity | 83 | 71 | 13. 11. 2026, 01:01 | Startup unveils Thorsten-4, an AI trained on 35 million psychologist-labeled words from 7,000+ people to predict their motivations, decisions and future behavior across 50 psychological traits — claims 90% accuracy |
| 1xutb77 | r/LocalLLaMA | 82 | 40 | 13. 11. 2026, 01:19 | Uncensored models are awesome |
| 1xvljhf | r/ArtificialInteligence | 82 | 35 | 13. 11. 2026, 23:18 | FAA expands AI advice to manage air traffic congestion across entire US airspace |
| 1xv7fku | r/LocalLLaMA | 79 | 18 | 13. 11. 2026, 14:08 | Perplexity releases Decider v1.3 (26B) and Decider Flash v1.3 (5B): open-weight (Apache 2.0) classification/decision models |
| 1xvakh7 | r/singularity | 78 | 26 | 13. 11. 2026, 16:19 | AI startup says it took just 3 hours to recreate a safer replacement for an allergy drug withdrawn over dangerous heart effects. Now it's attempting to make an existing cancer drug safer without losing its ability to fight cancer. |
| 1xuxzfs | r/LocalLLaMA | 77 | 81 | 13. 11. 2026, 05:06 | Artificial Analysis updated Qwen 3.8 Flash Next score as 29 |
| 1xv04sy | r/StableDiffusion | 77 | 17 | 13. 11. 2026, 07:03 | The Witcher season 4 with Cavill |
| 1xviq6r | r/StableDiffusion | 75 | 13 | 13. 11. 2026, 21:26 | New MOSS DMD Lora from Lodestone |
| 1xvli7o | r/ChatGPT | 74 | 36 | 13. 11. 2026, 23:17 | Is it just me, or has ChatGPT become so obsessed with logical accuracy that it can't hold a normal conversation? |
| 1xvbqqa | r/LocalLLaMA | 74 | 13 | 13. 11. 2026, 17:03 | I noticed the 2 Hessian Refinement of MACaQ can be applied to any GGUF without any patches ... and tried it. 13% better quants |
| 1xvefqg | r/singularity | 74 | 13 | 13. 11. 2026, 18:44 | With a tiny 5.46M-parameter touch model called LingBot-Touch, not a frontier LLM, these robot hands poke a straw through a cup's sealed lid, turn a single page and pull one cup off a stack, autonomous at 1x |
| 1xuwd96 | r/ClaudeAI | 73 | 71 | 13. 11. 2026, 03:44 | The better my AI coding agents get, the less I enjoy being a software engineer. |
| 1xuwszo | r/LocalLLaMA | 73 | 56 | 13. 11. 2026, 04:06 | US intel isn’t sure if businesswoman spied on Nvidia for China, doesn’t mean she wasn’t a risk, sources say |
| 1xuszbr | r/ChatGPT | 72 | 26 | 13. 11. 2026, 01:04 | These Instructions have completely changed the feel of Chat for me |
| 1xv2u6e | r/OpenAI | 70 | 15 | 13. 11. 2026, 09:49 | Dot appeared on my EU account without VPN |
| 1xvb2wt | r/GeminiAI | 69 | 19 | 13. 11. 2026, 16:39 | For those also confused if Argon is basically outdated after two weeks and Carbon is just better / cheaper |
| 1xv3xyv | r/ClaudeAI | 68 | 104 | 13. 11. 2026, 11:00 | Discussion Hub for new Claude incident: Elevated errors on claude.ai, Claude Code, and platform.claude.com on Nov 13, 2026 |
| 1xvcbbh | r/LocalLLaMA | 67 | 41 | 13. 11. 2026, 17:25 | Nvidia privately confirmed it could track chips to fight smuggling, even as industry publicly questioned feasibility |
| 1xvg2ll | r/OpenAI | 63 | 30 | 13. 11. 2026, 19:44 | In six days, OpenAI will begin using your medical data for training unless you opt-out. |
| 1xvcmnc | r/ClaudeAI | 62 | 18 | 13. 11. 2026, 17:37 | Please, allow us to connect with a password |
| 1xva3j7 | r/ChatGPT | 61 | 57 | 13. 11. 2026, 16:00 | Anyone else feel like ChatGPT has been neutered? |
| 1xv9zkg | r/comfyui | 59 | 18 | 13. 11. 2026, 15:56 | Who changed the font's color in the last update??? |
| 1xvkxbj | r/MachineLearning | 57 | 23 | 13. 11. 2026, 22:53 | ICML 2027 Changes [D] |
| 1xv5mno | r/Bard | 57 | 11 | 13. 11. 2026, 12:39 | Gemini 4 carbon was very passionate about team work with his sub agent |
| 1xuyzz6 | r/OpenAI | 56 | 33 | 13. 11. 2026, 06:00 | The simpsons house if it was in real life |
| 1xvk6kx | r/GeminiAI | 55 | 20 | 13. 11. 2026, 22:23 | Gemini 4 Hydrogen usage is confusing! |
| 1xv2077 | r/StableDiffusion | 52 | 30 | 13. 11. 2026, 08:57 | The real best thing about Minimax Image |
| 1xuthme | r/LocalLLaMA | 49 | 140 | 13. 11. 2026, 01:27 | If open weights dry up, what are you archiving? |
| 1xveyh4 | r/ChatGPT | 49 | 36 | 13. 11. 2026, 19:02 | Introducing ChatGPT Wallet |
| 1xv3gkx | r/ClaudeAI | 47 | 57 | 13. 11. 2026, 10:28 | How can you log back in during the Microsoft outage? |
| 1xvcmm0 | r/LocalLLaMA | 47 | 29 | 13. 11. 2026, 17:37 | I built speedy Strix Halo kernels for the top-51 LLMs with AMD Loom (and you can too) |
| 1xv0y2u | r/singularity | 44 | 336 | 13. 11. 2026, 07:51 | Why are you excited about singularity if AI alignment isn't solved? |
| 1xv4aqv | r/ClaudeAI | 42 | 84 | 13. 11. 2026, 11:21 | What’s the most interesting thing you’ve ever done with Claude? |
| 1xv1eya | r/GeminiAI | 42 | 29 | 13. 11. 2026, 08:19 | Google is cooking something massive for AI coding 👀 |
| 1xuw68g | r/ClaudeAI | 42 | 16 | 13. 11. 2026, 03:35 | Claude Managed Agents can now run self-hosted, inside your own perimeter (private beta) |
| 1xv8gr7 | r/StableDiffusion | 38 | 19 | 13. 11. 2026, 14:53 | Generative AI Fill in Open Source Photoshop |
| 1xvbcwg | r/ArtificialInteligence | 37 | 29 | 13. 11. 2026, 16:49 | We are all Emily Chang’s expression |
| 1xuye31 | r/ChatGPT | 37 | 28 | 13. 11. 2026, 05:27 | The only explanation that can save bro is that he's dating all of them just to spy on everyone and get insights from everywhere. |
| 1xuvjtw | r/ChatGPT | 36 | 32 | 13. 11. 2026, 03:05 | Random ChatGPT in the wild.. anyone else have this happen yet? |
| 1xvi9ko | r/StableDiffusion | 34 | 47 | 13. 11. 2026, 21:08 | Why does Minimax H3 Image even run (and fast!) on my 8GB VRAM/32GB RAM system despite the entire stack being about ~50GB (int8 pruned)? |
| 1xuwhrc | r/LocalLLM | 34 | 13 | 13. 11. 2026, 03:50 | Stories coming out about Jensen's support of Local AI |
| 1xvey5t | r/StableDiffusion | 33 | 17 | 13. 11. 2026, 19:02 | RTX 5070 Ti vs RTX 3090 — MiniMax H3 image-to-video benchmark (non-turbo, 20 steps) |
| 1xv7hxz | r/ClaudeAI | 32 | 32 | 13. 11. 2026, 14:11 | Discussion Hub for new Claude incident: Elevated errors on claude.ai, the Claude API, and Claude Code on Nov 13, 2026 |
| 1xutkqv | r/LocalLLaMA | 32 | 10 | 13. 11. 2026, 01:31 | Gemma 4 E2B on a 8GB RAM netbook |
| 1xv5jrj | r/StableDiffusion | 31 | 12 | 13. 11. 2026, 12:34 | MiniMax H3 video: how to keep faces consistent during dynamic camera motion? |
| 1xv8n0e | r/ClaudeAI | 30 | 41 | 13. 11. 2026, 15:00 | Unable to connect ANY connectors to Claude – Anyone else? |
| 1xv5svo | r/LocalLLaMA | 30 | 15 | 13. 11. 2026, 12:48 | I trained DiffusionGemma to be an abstract expressionist |
| 1xuyirz | r/StableDiffusion | 30 | 12 | 13. 11. 2026, 05:34 | I got MiniMax H3-Image running on a MacBook air with just ~3GB memory and almost no speed loss |
| 1xv5dsb | r/LocalLLaMA | 29 | 27 | 13. 11. 2026, 12:25 | I ran the same Halloween animation prompt through five coding agents on one local Qwen model |
| 1xv2yk2 | r/singularity | 29 | 21 | 13. 11. 2026, 09:57 | Tritium how many models they have internally ?? |
| 1xuveyg | r/ChatGPT | 28 | 16 | 13. 11. 2026, 02:58 | 6.1-Sol attempts to model a child in blender |
| 1xv6in5 | r/ChatGPT | 28 | 12 | 13. 11. 2026, 13:24 | I feel like crying |
| 1xvlc1e | r/agi | 28 | 10 | 13. 11. 2026, 23:10 | Leave the world behind |
| 1xutwi3 | r/StableDiffusion | 27 | 12 | 13. 11. 2026, 01:46 | H3-Image at 16MP: I reran the same 15 prompts, and the gap narrows |
| 1xuu72o | r/GeminiAI | 26 | 21 | 13. 11. 2026, 02:00 | Gemini 4 Hydrogen can be accessed on free tier |
| 1xvfem2 | r/singularity | 26 | 10 | 13. 11. 2026, 19:19 | crazy how far we got in just 2 years... |
| 1xvhzq9 | r/LocalLLaMA | 25 | 20 | 13. 11. 2026, 20:57 | DeepSeek v4.1 Flash vs Qwen 3.8 Flash Next Performance |
| 1xv1tkh | r/artificial | 24 | 92 | 13. 11. 2026, 08:45 | Why hasn’t the unemployment rate gone up at all yet? |
| 1xuvij1 | r/ChatGPT | 23 | 17 | 13. 11. 2026, 03:03 | Welp, I’m haunted. |
| 1xvecq2 | r/ChatGPT | 22 | 24 | 13. 11. 2026, 18:40 | ChatGPT is acting weird today. |
| 1xv6jdj | r/GeminiAI | 22 | 23 | 13. 11. 2026, 13:25 | About Hydrogen |
| 1xv282p | r/LocalLLaMA | 22 | 22 | 13. 11. 2026, 09:10 | Strata EXL3 AMD - UPDATED +15-20% tk/s - run Q4 at Q3 speeds - MiMo v2.6 flash support (exp) |
| 1xvdmzb | r/LocalLLaMA | 22 | 12 | 13. 11. 2026, 18:14 | Tontaube V1.1: open-weights TTS with voice cloning for long-form generation. 4-bit version runs about real time on a desktop CPU |
| 1xva70a | r/StableDiffusion | 19 | 23 | 13. 11. 2026, 16:03 | RTX 5070 Ti ComfyUI benchmarks: Overclock cut gen times ~10%, tuned flags more than halved H3 video time |
| 1xvfc8c | r/ClaudeAI | 18 | 144 | 13. 11. 2026, 19:17 | Tech bros, do you still think AI can replace most white collar jobs that can be done on a computer? |
| 1xvl9zs | r/ChatGPT | 18 | 46 | 13. 11. 2026, 23:07 | I asked chap gpt what it would do if it controlled the world. |
| 1xvc8n7 | r/StableDiffusion | 18 | 19 | 13. 11. 2026, 17:22 | Minimax-H3-Image works on RTX 3060 12gb + 32 gb RAM |
| 1xv3h93 | r/LocalLLaMA | 17 | 16 | 13. 11. 2026, 10:29 | [Boole-32B-A2.5B-preview] 9GB 1.8-bit MoE, 565 token/s on 1 RTX 5090 |
| 1xvm8uo | r/Bard | 17 | 11 | 13. 11. 2026, 23:48 | I’m not one to rush things, but shall we talk about this? |
| 1xvbe0t | r/ClaudeAI | 16 | 35 | 13. 11. 2026, 16:51 | Claude Fable 5.2 just topped the Artificial Analysis Intelligence Index at 65 — has anyone actually felt the jump over Opus 5.5? |
| 1xv9g4y | r/ClaudeAI | 15 | 21 | 13. 11. 2026, 15:33 | What kept a 300k-line Claude Code game project from falling apart |
| 1xvb6mn | r/ChatGPT | 15 | 14 | 13. 11. 2026, 16:43 | Year 3039, Humanity is at war with a race of Cosmic Alien Parasites, and you are a Mecha pilot about to head to the front lines. |
| 1xvbq3s | r/LocalLLaMA | 15 | 10 | 13. 11. 2026, 17:03 | modules for my opensource (GPL3) harness have evolved to the point where this is possible. this is a full fledged videogame running inside it! |
| 1xuxygr | r/OpenAI | 14 | 20 | 13. 11. 2026, 05:04 | Does anyone make an AI bot that just authorizes the endless requests for authorization from ChatGPT? |
| 1xvhsp7 | r/ChatGPT | 13 | 15 | 13. 11. 2026, 20:50 | Bruh, what happened to this thing? |
| 1xvej6v | r/ClaudeAI | 12 | 13 | 13. 11. 2026, 18:47 | Has anyone here had their mind blown by what is possible just by writing code, especially after Opus 5.5? |
| 1xvm8r3 | r/LocalLLaMA | 11 | 79 | 13. 11. 2026, 23:48 | Why are LLMs still so bad at jokes? |
| 1xuy029 | r/agi | 11 | 45 | 13. 11. 2026, 05:07 | What would you do if there was a 10% chance of the world ending in 1 year? |
| 1xvj4g3 | r/OpenAI | 11 | 17 | 13. 11. 2026, 21:42 | Unknown third-party GPT called "CodeX" appeared in my ChatGPT account. Should I be concerned about account security? |
| 1xuvjdv | r/ClaudeAI | 11 | 17 | 13. 11. 2026, 03:04 | I used Claude to build an AI design tool for social & marketing posts and I'm already using it for my side gigs |
| 1xv6aut | r/artificial | 11 | 14 | 13. 11. 2026, 13:13 | Korea's tax accountant exam top scorer is facing "AI glasses" suspicion with no evidence. |
| 1xvjn3v | r/agi | 11 | 11 | 13. 11. 2026, 22:02 | Is The Utopian Truly That Far Less Realistic Than The Dystopian? |
| 1xv0zz7 | r/LocalLLM | 10 | 29 | 13. 11. 2026, 07:54 | Do you run your local AI agents in Docker or directly on your host? |
| 1xvcdmj | r/comfyui | 10 | 25 | 13. 11. 2026, 17:28 | How do you stop a 9 cm robot from growing to head size in every shot? Local MiniMax H3 workflow, one 5090 |
| 1xv1cmh | r/ClaudeAI | 10 | 19 | 13. 11. 2026, 08:15 | Is Claude bad at everyday research, or am I just prompting it wrong? |
| 1xuu7s9 | r/LocalLLM | 10 | 14 | 13. 11. 2026, 02:01 | Candidates for "all purpose" LLM to run on single Mac Studio 512GB server? |
| 1xvfg2n | r/LocalLLaMA | 10 | 13 | 13. 11. 2026, 19:21 | Computer use programs/Pi extensions |
| 1xvlnw1 | r/ChatGPT | 10 | 12 | 13. 11. 2026, 23:23 | ChatGPT Plus heavily blocks image generation for me — the same prompts work on Free and other Plus accounts |
| 1xvi8md | r/ChatGPT | 10 | 12 | 13. 11. 2026, 21:07 | Rate my custom instructions out of 10. Will they actually improve accuracy and research quality? |
| 1xv2kmq | r/ClaudeAI | 10 | 12 | 13. 11. 2026, 09:31 | Fable is smart, but don't forget to have other models review its code |
| 1xvhzes | r/LocalLLaMA | 9 | 43 | 13. 11. 2026, 20:57 | Poorman's Local LLM |
| 1xv1opf | r/LocalLLaMA | 9 | 31 | 13. 11. 2026, 08:36 | mi50 32gb or v100 32gb? |
| 1xv8w8l | r/StableDiffusion | 9 | 19 | 13. 11. 2026, 15:11 | GPU showdown: RTX 5070 Ti vs RTX 3090 in ComfyU |
| 1xuw5lc | r/LLMDevs | 8 | 35 | 13. 11. 2026, 03:34 | What are you still not letting your agents do? |
| 1xvi3rb | r/LocalLLM | 8 | 21 | 13. 11. 2026, 21:01 | Is Qwen 3.6 35B A3B capable of reliable browser automation? |
| 1xve0b0 | r/artificial | 8 | 20 | 13. 11. 2026, 18:28 | so are robots just chatbots with arms now? |
| 1xv4cz4 | r/StableDiffusion | 8 | 17 | 13. 11. 2026, 11:25 | What are people using for cleanup / deroping in Minimax h3? |
| 1xuwooe | r/ClaudeAI | 8 | 16 | 13. 11. 2026, 04:00 | A 10-minute 'manual dreaming' pass for your CLAUDE.md and memory files |
| 1xv7w0i | r/GeminiAI | 8 | 12 | 13. 11. 2026, 14:28 | Request to all jio users |
| 1xvia6x | r/LocalLLaMA | 8 | 11 | 13. 11. 2026, 21:08 | Voice dictation with one model. |
| 1xvimf6 | r/LocalLLM | 8 | 11 | 13. 11. 2026, 21:22 | DeepSeek V4.1 Flash RAM overheat |
| 1xv6hyj | r/LocalLLM | 7 | 39 | 13. 11. 2026, 13:23 | Recommended LLM for 16GB VRAM? |
| 1xuupey | r/ChatGPT | 7 | 17 | 13. 11. 2026, 02:24 | Update Suggestion for GPT |
| 1xutqna | r/GeminiAI | 7 | 17 | 13. 11. 2026, 01:39 | Hit a usage limit for the first time ever. |
| 1xvgzsu | r/ChatGPT | 7 | 16 | 13. 11. 2026, 20:19 | Astra and usage limits |
| 1xv0ibj | r/LocalLLaMA | 7 | 13 | 13. 11. 2026, 07:24 | Local Parakeet speech to text on Android |
| 1xvanf5 | r/GeminiAI | 7 | 13 | 13. 11. 2026, 16:22 | After a while |
| 1xv3sm6 | r/StableDiffusion | 7 | 10 | 13. 11. 2026, 10:50 | All-In-One Solution for Minimax H3? |
| 1xvcl22 | r/singularity | 6 | 77 | 13. 11. 2026, 17:36 | How will the world look like in 2032? |
| 1xvbzkg | r/OpenAI | 6 | 36 | 13. 11. 2026, 17:13 | How are people using up their $100 Plan so fast? |
| 1xv4cti | r/GeminiAI | 6 | 33 | 13. 11. 2026, 11:25 | Gemini hydrogen 4 VS ChatGPT free AI model right now |
| 1xvjoa7 | r/LocalLLaMA | 6 | 25 | 13. 11. 2026, 22:03 | Tandem-vLLM 0.2.0: DeepSeek-V4.1-Flash now on 3090/4090-class, A6000, Ada and H100/H200 cards, and on two GPUs (a second card as an "expert helper") |
| 1xv0y6g | r/GeminiAI | 6 | 24 | 13. 11. 2026, 07:51 | My workplace is just about to switch from Claude pro plans to Gemini. Is this a massive downgrade? |
| 1xvh7rz | r/ChatGPT | 6 | 14 | 13. 11. 2026, 20:27 | Slow |
| 1xveibt | r/OpenAI | 6 | 13 | 13. 11. 2026, 18:46 | ChatGPT as a home assistant? |
| 1xve8r2 | r/ChatGPT | 6 | 12 | 13. 11. 2026, 18:36 | Ridiculously unsafe how "chatGPT work" operates - that's what destroys peoples computers |
| 1xv7v68 | r/ClaudeAI | 6 | 12 | 13. 11. 2026, 14:27 | I built a gift shop for AIs with Claude Code, then asked four models to pick a gift. Three asked for a pebble. Grok asked for the private jet. |
| 1xuvklw | r/GeminiAI | 6 | 12 | 13. 11. 2026, 03:06 | Which Gemini Model to Use when |
| 1xv85wb | r/AIAssisted | 6 | 11 | 13. 11. 2026, 14:40 | AI tools I use for work |
| 1xvk0kb | r/ClaudeAI | 6 | 10 | 13. 11. 2026, 22:16 | Claude Review Code |
| 1xvj61w | r/ClaudeAI | 5 | 33 | 13. 11. 2026, 21:43 | Is it me or is Opus actually more of a footgun than sonnet |
| 1xvl9eq | r/ClaudeAI | 5 | 32 | 13. 11. 2026, 23:07 | How do you keep Claude Code from fixing one bug and creating two more? |
| 1xurnev | r/LocalLLM | 5 | 19 | 13. 11. 2026, 00:06 | They need to revive SLI compatiblity for Ai Training. |
| 1xv9pjn | r/ClaudeAI | 5 | 19 | 13. 11. 2026, 15:44 | Since when does Claude use a smaller model to fetch webpages? |
| 1xvf1nf | r/StableDiffusion | 5 | 15 | 13. 11. 2026, 19:06 | Is it possible to train krea2(raw) lora on rtx4050 6gb vram? |
| 1xvdh5w | r/LocalLLM | 5 | 11 | 13. 11. 2026, 18:09 | New Mac Mini M5 Pro 64GB - Advice for Stack |
| 1xv2zrd | r/StableDiffusion | 4 | 17 | 13. 11. 2026, 09:59 | krea |
| 1xv62e4 | r/LocalLLM | 4 | 16 | 13. 11. 2026, 13:01 | under 5k? |
| 1xv8yee | r/ClaudeAI | 4 | 16 | 13. 11. 2026, 15:13 | Fable Level Projects? |
| 1xuzeg7 | r/ClaudeAI | 4 | 16 | 13. 11. 2026, 06:22 | I use ChatGPT for planning and Claude Code for coding, so I built a place where they can share files |
| 1xvbwl9 | r/LocalLLaMA | 4 | 14 | 13. 11. 2026, 17:10 | Guide on setting up new pc from scratch for local ai model |
| 1xv59p9 | r/ClaudeAI | 4 | 14 | 13. 11. 2026, 12:18 | Claude code |
| 1xuzd56 | r/GeminiAI | 4 | 12 | 13. 11. 2026, 06:20 | Are we really supposed to trust google/gemini? |
| 1xuz68s | r/ClaudeAI | 4 | 11 | 13. 11. 2026, 06:09 | Claude pro paid and catgut free for building web app taking a long time |
| 1xvb7dw | r/LocalLLM | 3 | 29 | 13. 11. 2026, 16:44 | Qwen3.6-35B-A3B on a 12 GB RTX 3060: BigMoeOnEdge vs Strata, same box, same file |
| 1xvl6ut | r/LocalLLM | 3 | 22 | 13. 11. 2026, 23:04 | Curious if these t/s are normal/good/okay for my system // basic gaming pc - 9800X3D / 6800XT with 16GB VRAM and 32GB DDR5. |
| 1xuzazz | r/Bard | 3 | 22 | 13. 11. 2026, 06:16 | Gemini 4 Hydrogen is much more censored than Gemini 3.8 Flash |
| 1xvaxma | r/StableDiffusion | 3 | 18 | 13. 11. 2026, 16:33 | Under the radar story from Huang fallout: Commerce Dept to block Alibaba from renting advanced chips in Singapore & Malaysia |
| 1xv9ga2 | r/LocalLLaMA | 3 | 17 | 13. 11. 2026, 15:33 | I need context window |
| 1xurrtz | r/LocalLLM | 3 | 17 | 13. 11. 2026, 00:11 | maybe ddr3 is better than optanes? |
| 1xv3vd7 | r/ChatGPT | 3 | 16 | 13. 11. 2026, 10:55 | Subscription upgrade |
| 1xvcdt2 | r/ChatGPT | 3 | 15 | 13. 11. 2026, 17:28 | Is there a TTS tool that uses ChatGPT voices? |
| 1xuwowk | r/LocalLLaMA | 3 | 13 | 13. 11. 2026, 04:00 | Looking for some help optimizing for a 300-page manual and transcripts |
| 1xv5f8y | r/LocalLLaMA | 3 | 11 | 13. 11. 2026, 12:27 | MIT's  Weight-Space Programming paper sent me down to a mathematical paradox trying to fix Llama's over-refusal. |
| 1xut0k5 | r/ClaudeAI | 3 | 11 | 13. 11. 2026, 01:06 | I don't feel AI is improving at communication or "modelling humans" |
| 1xuvyjn | r/GeminiAI | 3 | 10 | 13. 11. 2026, 03:25 | Yeah, what the actual duck is this google (see the screenshot) |
| 1xus5mt | r/ChatGPT | 2 | 28 | 13. 11. 2026, 00:28 | OpenAI is killing Standard Voice, and I genuinely don't understand what the hell they're thinking |
| 1xv7ffr | r/LocalLLM | 2 | 20 | 13. 11. 2026, 14:07 | What models should I keep an archive of? |
| 1xvaflf | r/ClaudeAI | 2 | 20 | 13. 11. 2026, 16:13 | From Claude Max to Ultra |
| 1xuvgie | r/LocalLLM | 2 | 18 | 13. 11. 2026, 03:00 | Local is my first choice, but what do you do when a model just won’t fit on your machine? |
| 1xvggj6 | r/LocalLLaMA | 2 | 17 | 13. 11. 2026, 19:59 | How do you guys containerize local LLMs on Mac ? |
| 1xv6ufa | r/ClaudeAI | 2 | 16 | 13. 11. 2026, 13:41 | Building my own admin assistant for my business, some feedback/tips would be great |
| 1xvme8n | r/LocalLLM | 2 | 13 | 13. 11. 2026, 23:55 | Dual V100 32gb fails to post without workaround help |
| 1xv8rs5 | r/ChatGPT | 2 | 13 | 13. 11. 2026, 15:06 | What ai do you use that’s unrestricted? |
| 1xuxp2n | r/StableDiffusion | 2 | 13 | 13. 11. 2026, 04:51 | Krea 2 4k question |
| 1xv4kb4 | r/ChatGPT | 2 | 11 | 13. 11. 2026, 11:37 | How do I disable ChatGPT from referencing previous conversations? |
| 1xvd56e | r/ClaudeAI | 2 | 10 | 13. 11. 2026, 17:56 | Even the non-technical folks on our bootstrapped team started coding tools in Claude, and quickly outgrew Artifacts. Here is the internal cloud we built for them. |
| 1xvfmcj | r/ChatGPT | 1 | 46 | 13. 11. 2026, 19:27 | A fun prompt to try: ask Chat to generate a psychological portrait of themself |
| 1xvh7ik | r/ClaudeAI | 1 | 31 | 13. 11. 2026, 20:27 | We give AI coding agents access to everything. Are we being way too careless? |
| 1xusvq9 | r/ClaudeAI | 1 | 27 | 13. 11. 2026, 01:00 | For devs using Claude Code or similar at work: what’s the 10% you still fix by hand in Python? |
| 1xv5bx1 | r/LocalLLM | 1 | 17 | 13. 11. 2026, 12:22 | I expected Ollama and llama.cpp to perform the same now that Ollama runs llama.cpp. With 4 parallel requests on a 27B: 33 vs 100 tok/s |
| 1xvceug | r/ChatGPT | 1 | 13 | 13. 11. 2026, 17:29 | Text editing with AI has been getting worse lately |
| 1xv7uyk | r/ChatGPT | 1 | 13 | 13. 11. 2026, 14:27 | Is there any provider thats decent and has GPT models for $60? |
| 1xv1ahm | r/ChatGPT | 1 | 13 | 13. 11. 2026, 08:12 | How to find an AI(s) to replace Opus 5.5 |
| 1xvm6m3 | r/ClaudeAI | 1 | 13 | 13. 11. 2026, 23:45 | Has anyone found a way of getting a feeling of mastery/flow state/deep work while using AI to code? If so what does your workflow look like? |
| 1xvagbx | r/ClaudeAI | 1 | 13 | 13. 11. 2026, 16:14 | Fable 5.2 launch resets disappeared after switching Ultra → Max (still an eligible plan), no warning |
| 1xveetr | r/GeminiAI | 1 | 13 | 13. 11. 2026, 18:43 | First impressions of Gemini Hydrogon? |
| 1xves4q | r/LocalLLM | 1 | 12 | 13. 11. 2026, 18:56 | Mi25 |
| 1xuve85 | r/LocalLLM | 1 | 12 | 13. 11. 2026, 02:57 | Strata Help |
| 1xvet0p | r/ChatGPT | 1 | 12 | 13. 11. 2026, 18:57 | Interesting how AI is now relating to itself during a conversation. |
| 1xvahbs | r/StableDiffusion | 1 | 12 | 13. 11. 2026, 16:15 | What's the least ram-consuming comfy wrapper right now? |
| 1xv07ah | r/StableDiffusion | 1 | 12 | 13. 11. 2026, 07:07 | How to improve MiniMax H3-Image’s image quality and prompt adherence ? |
| 1xv4kq6 | r/LocalLLM | 1 | 11 | 13. 11. 2026, 11:38 | Thoughts on mixing AMD with Nvidia GPUs |
| 1xuus5p | r/LocalLLM | 1 | 11 | 13. 11. 2026, 02:28 | Should I run the 5060 TI and RX 6600 simultaneously? |
| 1xuu3vj | r/StableDiffusion | 1 | 11 | 13. 11. 2026, 01:56 | Minimax H3 - different results from 3 days ago? |
| 1xusz0i | r/GeminiAI | 1 | 10 | 13. 11. 2026, 01:04 | Gemini just started talking out of nowhere |
| 1xvam6d | r/ChatGPT | 0 | 75 | 13. 11. 2026, 16:21 | is there a safer voice ai for kids than regular chatgpt? |
| 1xv3m5y | r/ArtificialInteligence | 0 | 73 | 13. 11. 2026, 10:38 | Jensen Huangs legacy being clubbed into sexual deviancy after having built one of the biggest and most important companies in the history of mankind is nothing short of a disgrace and the very proof that moral supremacy is being weaponized by the media. |
| 1xvbcpf | r/ClaudeAI | 0 | 52 | 13. 11. 2026, 16:49 | what are realistic ways to make money using Claude? |
| 1xvbgch | r/LocalLLM | 0 | 47 | 13. 11. 2026, 16:53 | Local Ai. Do these delusional billionaires really think we need them anymore? |
| 1xusbcy | r/ChatGPT | 0 | 42 | 13. 11. 2026, 00:35 | AI accident is most likely reason you will die, warns OpenAI board member |
| 1xv12vq | r/StableDiffusion | 0 | 36 | 13. 11. 2026, 07:59 | do you guys use pc for comfy same as pc you play games? |
| 1xv2w9j | r/singularity | 0 | 34 | 13. 11. 2026, 09:53 | We humans are going to be remembered forever because Superintelligence will be immortal. |
| 1xvflyc | r/LocalLLaMA | 0 | 31 | 13. 11. 2026, 19:27 | A year ago I couldn't get vLLM running on my 5090. Now work gave me a DGX Station for a month. What should I run? |
| 1xv9kgh | r/LocalLLaMA | 0 | 31 | 13. 11. 2026, 15:38 | How are you affording your tokens? |
| 1xuv877 | r/ChatGPT | 0 | 31 | 13. 11. 2026, 02:49 | AI Poses a Much Larger Threat Than You People Realize |
| 1xv3tx3 | r/LocalLLaMA | 0 | 30 | 13. 11. 2026, 10:53 | UD_IQ1_M Q3.8 FN behavior on Strata |
| 1xvk6ny | r/OpenAI | 0 | 29 | 13. 11. 2026, 22:23 | To OpenAI: I’ve been a dedicated and paid user of pro and premium since 3.5 - You’re making me switch to Chinese Models. |
| 1xvlgkh | r/LocalLLaMA | 0 | 28 | 13. 11. 2026, 23:15 | Are any of the other 'free' models worth using? |
| 1xuu5g8 | r/ClaudeAI | 0 | 27 | 13. 11. 2026, 01:58 | Should we worry about that? what is really happening? I hope that it really isn't the end of AI fan creations and I hope this situation doesn't get worse to levels I don't want |
| 1xvi7iq | r/StableDiffusion | 0 | 24 | 13. 11. 2026, 21:05 | Any ideas on how I can generate images like this? |
| 1xv45vj | r/GeminiAI | 0 | 24 | 13. 11. 2026, 11:13 | Gemini 4 hydrogen destroyed my 5h quota in 3 questions |
| 1xus0v4 | r/ClaudeAI | 0 | 23 | 13. 11. 2026, 00:22 | Someone please explain to me Claude's really creepy obsession with age. |
| 1xv8u4u | r/ArtificialInteligence | 0 | 22 | 13. 11. 2026, 15:08 | Pretty convenient that Nvidia is being beheaded now that the democrats are in power |
| 1xvkaws | r/ClaudeAI | 0 | 22 | 13. 11. 2026, 22:28 | Help prevent me being dumb |
| 1xvb5vi | r/LocalLLaMA | 0 | 21 | 13. 11. 2026, 16:42 | Nemotron models are the best open models there is |
| 1xv0nug | r/LocalLLaMA | 0 | 21 | 13. 11. 2026, 07:34 | With these scandals and uncertainty with Huggingface, what models should I download? |
| 1xuwuqd | r/ChatGPT | 0 | 21 | 13. 11. 2026, 04:08 | What exactly do I need to be careful of for ChatGPT computer use |
| 1xutfxu | r/StableDiffusion | 0 | 21 | 13. 11. 2026, 01:25 | Best local model for uncensored image gen? |
| 1xv3zzd | r/artificial | 0 | 20 | 13. 11. 2026, 11:03 | I thought AI would save me time. What a joke |
| 1xvjjf9 | r/ChatGPT | 0 | 20 | 13. 11. 2026, 21:58 | The Chinese AI Wall: What Happened to China's Biggest Models? |
| 1xv529i | r/ChatGPT | 0 | 19 | 13. 11. 2026, 12:06 | How I'd explain ChatGPT to my parents: it doesn't think, it predicts the next word |
| 1xv4b3a | r/GeminiAI | 0 | 17 | 13. 11. 2026, 11:22 | Where is Gemini 3.8 Flash ? |
| 1xv31ug | r/ArtificialInteligence | 0 | 16 | 13. 11. 2026, 10:02 | AI and the future of humanity |
| 1xva42x | r/LocalLLM | 0 | 16 | 13. 11. 2026, 16:00 | How long do you think it will take before abliterated models are made illegal? |
| 1xv36lx | r/OpenAI | 0 | 16 | 13. 11. 2026, 10:11 | Where should your AI's memory live: on a server or on your own PC? |
| 1xvbyfi | r/ChatGPT | 0 | 16 | 13. 11. 2026, 17:12 | what's wrong now? I've been using the app for months, was always able to keep the same chat for weeks but since the last update it always does that after a couple of messages. So frustrating. Never does that before. |
| 1xv1ho4 | r/ChatGPT | 0 | 16 | 13. 11. 2026, 08:24 | Why is nobody talking about OpenAI’s silent shift to pay-per-usage next month? |
| 1xusgzr | r/ArtificialInteligence | 0 | 15 | 13. 11. 2026, 00:42 | FUCKING GPT DOES NOT KNOW HOW TO READ. IT GUESSES EVERYTHING. |
| 1xvhb52 | r/LocalLLM | 0 | 15 | 13. 11. 2026, 20:31 | Why aren't more people talking about the Rust frontend for vLLM? |
| 1xv2fl7 | r/LocalLLM | 0 | 15 | 13. 11. 2026, 09:23 | What model for 32gb vram and 96gb ram |
| 1xv20tv | r/GeminiAI | 0 | 15 | 13. 11. 2026, 08:58 | FREE Offer user like me should be grateful, and not ask for too much |
| 1xvky9w | r/OpenAI | 0 | 14 | 13. 11. 2026, 22:54 | An Open Letter to OpenAI Thank You for Helping Me Bring a Vision Into the World — and an Invitation to Build What Comes Next |
| 1xvm6jx | r/ChatGPT | 0 | 14 | 13. 11. 2026, 23:45 | So sick of chat gpt. Oops sorry I totally screwed it all up.... |
| 1xv5e6p | r/ChatGPT | 0 | 14 | 13. 11. 2026, 12:25 | Chatgpt bet? |
| 1xuu5ok | r/ChatGPT | 0 | 14 | 13. 11. 2026, 01:58 | ChatGPT being homophobic: refuses to generate cunty yassified Patrick Star GIF. |
| 1xvilwr | r/ClaudeAI | 0 | 14 | 13. 11. 2026, 21:21 | Should I switch from ChatGPT Plus to Claude Pro |
| 1xuwl31 | r/ClaudeAI | 0 | 14 | 13. 11. 2026, 03:55 | Fable Reset is a lie? |
| 1xvcede | r/StableDiffusion | 0 | 14 | 13. 11. 2026, 17:28 | Some images from MiniMax H3 Image |
| 1xvm0qg | r/ArtificialInteligence | 0 | 13 | 13. 11. 2026, 23:38 | I think we'll see lots of chinese ai chips coming soon to the market. |
| 1xvdsho | r/ArtificialInteligence | 0 | 13 | 13. 11. 2026, 18:20 | What are the best LLMs to humanize texts? |
| 1xva6hv | r/ArtificialInteligence | 0 | 13 | 13. 11. 2026, 16:03 | Jensen should not be reinstated |
| 1xv2yaj | r/LocalLLM | 0 | 13 | 13. 11. 2026, 09:56 | Can someone explain me what the uncensored ai models means? |
| 1xvmb1n | r/comfyui | 0 | 13 | 13. 11. 2026, 23:51 | Is the Pixelfudger course worth it? |
| 1xv5zco | r/GeminiAI | 0 | 13 | 13. 11. 2026, 12:57 | What’s up with the mixed reviews on Hydrogen? |
| 1xv1ldv | r/GeminiAI | 0 | 13 | 13. 11. 2026, 08:30 | Google screws Jio subscribers once again! Not available in Antigravity. |
| 1xuw12v | r/ArtificialInteligence | 0 | 12 | 13. 11. 2026, 03:28 | As time approaches infinity Ai approaches consciousness. But never actually gets there... |
| 1xutq9j | r/ArtificialInteligence | 0 | 12 | 13. 11. 2026, 01:38 | The state really wants to ban open source |
| 1xv1t4h | r/ChatGPT | 0 | 12 | 13. 11. 2026, 08:44 | This is the only sub where my notifications are working so I shall talk about chat GPT. |
| 1xuyiwg | r/ClaudeAI | 0 | 12 | 13. 11. 2026, 05:35 | what's the way for prompting? |
| 1xuvh9n | r/ClaudeAI | 0 | 12 | 13. 11. 2026, 03:01 | I wanted to live the life of a wizarding student in a castle, so I made it. |
| 1xvcvz6 | r/StableDiffusion | 0 | 12 | 13. 11. 2026, 17:47 | Has anyone tried building one click ai drama movie using comfyui? |
| 1xurzle | r/GeminiAI | 0 | 12 | 13. 11. 2026, 00:21 | Gemini 4 Hydrogen will be removed in 45 days |
| 1xv6f8g | r/LocalLLM | 0 | 11 | 13. 11. 2026, 13:19 | M5 max vs hybrid strix halo? |
| 1xuyby8 | r/OpenAI | 0 | 11 | 13. 11. 2026, 05:24 | The only explanation that can save bro is that he's dating all of them just to spy on everyone and get insights from everywhere. |
| 1xveo58 | r/ChatGPT | 0 | 11 | 13. 11. 2026, 18:52 | I asked GPT-5.6 Sol to design its own body before generating a selfie. Then I animated it. |
| 1xv35wm | r/ChatGPT | 0 | 11 | 13. 11. 2026, 10:09 | Would you watch a YouTube series where an AI starts a real business from scratch? |
| 1xuz091 | r/ChatGPT | 0 | 11 | 13. 11. 2026, 06:01 | The simpsons house if it was in real life |
| 1xuxmk2 | r/ClaudeAI | 0 | 11 | 13. 11. 2026, 04:47 | Why are game UIs orange? |
| 1xvle3q | r/comfyui | 0 | 11 | 13. 11. 2026, 23:12 | How Can I Get Rid Of These Callouts? |
| 1xva7uu | r/GeminiAI | 0 | 11 | 13. 11. 2026, 16:04 | Seems Hydrogen takes more quota than 3.8 flash did. |
| 1xvcpap | r/ArtificialInteligence | 0 | 10 | 13. 11. 2026, 17:40 | My perspective on AI - Tell me how yours in different |
| 1xuuj3m | r/ArtificialInteligence | 0 | 10 | 13. 11. 2026, 02:16 | Gemini glitched out and accidentally leaked the instructions/prompt given to it from the backend to respond to my statement. is this common? |
| 1xv6aal | r/ChatGPT | 0 | 10 | 13. 11. 2026, 13:12 | Can’t wait for the movie |
| 1xvkbje | r/ClaudeAI | 0 | 10 | 13. 11. 2026, 22:29 | Claude after translating my app into 44 languages 🤯 |
| 1xve2yw | r/ClaudeAI | 0 | 10 | 13. 11. 2026, 18:31 | I launched my Warcraft 3 style tower defence a few weeks ago. This week Claude Code and I rebuilt how the whole game looks. Here's what I learned this time. |
| 1xv2f15 | r/StableDiffusion | 0 | 10 | 13. 11. 2026, 09:22 | Minimax image default workflow issue |
