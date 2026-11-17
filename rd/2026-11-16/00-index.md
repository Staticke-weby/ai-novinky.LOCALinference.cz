# Reddit AI souhrn – 16. listopadu 2026

## Metodika

Data pocházejí z přímého sběru Redditu přes web (`scripts/rd-collect-web.py`) pro den 16. 11. 2026 v pásmu Europe/Prague. Skript stáhl 925 postů z AI subredditů, z toho 40 kandidátů prošlo prahem skóre a komentářů a 337 postů s alespoň 10 komentáři tvoří přílohu níže. Skóre a počty komentářů jsou hodnoty z doby sběru, ne z doby publikace.

Před výběrem byla témata porovnána se seznamem už publikovaných článků z 13.–15. 11. 2026 (`logs/recent-2026-11-16-rd.md`). **Přísně vyřazeno bylo 1 téma** (Claude a Blender animace – stejné téma vyšlo 14. a 15. 11.); další kandidáti vypadli jako memy bez věcného obsahu nebo jako duplicity. Zůstalo **16 článků**, do kterých bylo sloučeno **15 dalších postů** se stejným produktem nebo událostí (odkazy jsou u článků jako „další diskuse“).

Externí články u části balíčků nebyly dostupné (paywall nebo captcha Redditu), proto články vycházejí hlavně z vlastního textu postů a z diskuse. Odkazy v tabulce i v příloze míří na skutečné názvy souborů; u sloučených postů na článek, do kterého byly sloučeny.

## Články

| # | Článek | Původní titulek (česky) | Skóre | Komentářů |
|---|---|---|---|---|
| 1 | [Qwen4 na obzoru: Max zklamal benchmarkem, 27B se má vejít do 16 GB](1xxlich_qwen4-max-benchmark-a-27b-do-16-gb.md) | [Začíná začátek stávání se začátkem](https://i.redd.it/czvg7r846y1i1.jpeg) | 1814 | 376 |
| 2 | [AI už prolézá captcha: Codex odklikal kontrolu, lidem zůstávají těžší testy](1xxmpfu_ai-resi-captcha-za-cloveka.md) | [Je po všem](https://i.redd.it/mr4tnq53jy1i1.png) | 1380 | 75 |
| 3 | [Obama varuje před misalignmentem: stroje si začnou psát vlastní agendu](1xxtb7i_obama-o-misalignmentu.md) | [Barack Obama: „Stroje se začínají učit samy. Teď narážíme na hokejku, kdy jsou modely exponenciálně chytřejší a chytřejší.“](https://v.redd.it/wsv2su5p002i1) | 1330 | 425 |
| 4 | [Gemini 4 Helix a Oxygen: Google sype modely rychleji, než stíhá vymýšlet jména](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | [Gemini 4 Oxygen alias další flash checkpoint. Google nezpomaluje](https://v.redd.it/lchl43qgbx1i1) | 1055 | 160 |
| 5 | [OpenAI inzeruje ChatGPT v Google Vyhledávání. Diskuse počítá, kolik platí konkurenci](1xy08b6_openai-inzeruje-na-google.md) | [Zajímalo by mě, kolik za tohle platí OpenAI Googlu](https://i.redd.it/0mlltduka12i1.jpeg) | 810 | 87 |
| 6 | [Lana Rhoades prodala svou podobu Candy AI. Diskuse řeší, co to udělá s byznysem OnlyFans](1xxbwbc_lana-rhoades-prodala-podobu-candy-ai.md) | [Lana Rhoades prodala svou podobu Candy AI](https://www.reddit.com/gallery/1xxbwbc) | 773 | 157 |
| 7 | [Anthropic vydal návod na always-on agenty: schránka, časovače, paměť, práva a odesílání](1xxdzcf_anthropic-navod-na-always-on-agenty.md) | [Anthropic vydal návod na tvorbu neustále běžících agentů. Dělí je na 5 částí: inbox, timers, memory, permissions, outbox](https://www.reddit.com/r/ClaudeAI/comments/1xxdzcf/anthropic_published_a_guide_on_building_alwayson/) | 561 | 39 |
| 8 | [Claude Meetings v praxi: agent mluví do schůzky, sám aktualizuje Notion a rozesílá úkoly](1xy3iuo_claude-meetings-v-praxi.md) | [Dnes jsem začal používat Claude Meetings](https://www.reddit.com/r/ClaudeAI/comments/1xy3iuo/started_using_claude_meetings_today/) | 543 | 185 |
| 9 | [ChatGPT zablokoval uživatele bez vysvětlení. Odvolání neprošlo, podpora odpovídala AI](1xxy6j0_chatgpt-perma-ban-bez-duvodu.md) | [Sbohem. Byla to skvělá a divoká jízda.](https://www.reddit.com/r/ChatGPT/comments/1xxy6j0/goodbye_its_been_a_great_and_wild_ride/) | 472 | 610 |
| 10 | [Místo stovek GB stačí malý LoRA. Abliterace modelu jde zapnout za běhu](1xxawbh_abliterace-modelem-lora.md) | [Proč stahovat abliterované Flash Next modely, když existuje LoRA?](https://huggingface.co/nazeshinjite/Qwen3.8-Flash-Next-Abliterated-LoRA) | 448 | 153 |
| 11 | [Výzkumník Anthropicu: lidé budou trvale nezaměstnaní, superhuman AI může přijít za 1,3 roku](1xxi8az_anthropic-vyzkumnik-superhuman-ai.md) | [Výzkumník z Anthropic: „Skoro všichni lidé se stanou trvale nezaměstnatelnými“](https://www.youtube.com/watch?v=OPZCQk8jF-I) | 430 | 796 |
| 12 | [Altman: svět, kde lidé žijí jako labrador, je špatný prodejní argument](1xy1q6z_altman-o-agensvi-a-labradoru.md) | [Altman: „Budete žít jako labrador... Myslím, že je to hrozná nabídka. Takový svět nechci.“](https://v.redd.it/aiig1o4sg12i1) | 408 | 340 |
| 13 | [V účtu ChatGPT se objevily čínské konverzace. Uživatelé radí změnit heslo a zrušit API klíče](1xxi5bv_hacknuty-chatgpt-cinske-chaty.md) | [Byl mi hacknut účet na ChatGPT?](https://i.redd.it/j5gm27sr3x1i1.png) | 399 | 91 |
| 14 | [AI zrychlila práci, ale lidem přinesla burnout: zmizely jednoduché úkoly](1xy03qy_ai-burnout-v-praci.md) | [Ask Claude: Dělá ještě někdo AI tiché odcházení?](https://www.reddit.com/r/ClaudeAI/comments/1xy03qy/ask_claude_any_one_else_doing_an_ai_powered_quiet/) | 331 | 95 |
| 15 | [Tencent představil Hy4 flash: 224 miliard parametrů, 12 aktivních a milionový kontext](1xxlgpb_tencent-hy4-flash.md) | [Představujeme Hy4 flash](https://hy.tencent.ai/research/hy4-flash) | 331 | 114 |
| 16 | [Placený lovec chyb: za chybu v matematice dostane zaplaceno, modelům už ale nestačí](1xx9le8_placeny-lovec-chyb-v-matematice.md) | [Platí mě za to, že lámu AI na matikářských úlohách. Upřímně, začínám prohrávat...](https://www.reddit.com/r/ChatGPT/comments/1xx9le8/i_get_paid_to_break_ai_with_maths_problems/) | 299 | 119 |

## Příloha: všechny posty s ≥ 10 komentáři (337)

| ID | Subreddit | Skóre | Komentáře | Čas | Titulek |
|---|---|---|---|---|---|
| [1xxptvv](1xy3iuo_claude-meetings-v-praxi.md) | r/ClaudeAI | 3387 | 109 | 16. 11. 2026, 14:50 | How meetings will be in 2027: |
| [1xxlich](1xxlich_qwen4-max-benchmark-a-27b-do-16-gb.md) | r/LocalLLaMA | 1814 | 376 | 16. 11. 2026, 10:55 | The beginning of the becoming of the beginning begins |
| [1xxtz3r](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/GeminiAI | 1449 | 51 | 16. 11. 2026, 17:34 | Someone Just Solved Google's Gemini Model Selection Problem |
| [1xxmpfu](1xxmpfu_ai-resi-captcha-za-cloveka.md) | r/ChatGPT | 1380 | 75 | 16. 11. 2026, 12:08 | It's so over |
| [1xxtb7i](1xxtb7i_obama-o-misalignmentu.md) | r/ChatGPT | 1330 | 425 | 16. 11. 2026, 17:09 | Barack Obama: “The machines are starting to teach themselves. We're now hitting the hockey stick where the models are getting smarter and smarter at an exponential pace." ... "If they start setting their own agendas, you may get misalignment between what they want to do vs what we want them to do." |
| [1xxolvw](1xy03qy_ai-burnout-v-praci.md) | r/singularity | 1262 | 83 | 16. 11. 2026, 13:53 | Increase Productivity |
| [1xxhla4](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/GeminiAI | 1103 | 58 | 16. 11. 2026, 06:49 | Gemini models at the end of the year: |
| [1xxiun5](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/GeminiAI | 1055 | 160 | 16. 11. 2026, 08:04 | Gemini 4 Oxygen aka the next flash checkpoint. Google ain't stopping now |
| [1xxgaog](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/GeminiAI | 904 | 180 | 16. 11. 2026, 05:37 | Gemini 4 Helix: The new flash lite. |
| 1xxkwuq | r/OpenAI | 857 | 28 | 16. 11. 2026, 10:16 | CEOs are getting paranoid |
| [1xy08b6](1xy08b6_openai-inzeruje-na-google.md) | r/ChatGPT | 810 | 87 | 16. 11. 2026, 21:26 | I wonder how much OpenAi pays Google for this |
| [1xxbwbc](1xxbwbc_lana-rhoades-prodala-podobu-candy-ai.md) | r/ArtificialInteligence | 773 | 157 | 16. 11. 2026, 01:54 | Lana Rhoades sold her Likeness to Candy Ai |
| [1xxe7en](1xxlich_qwen4-max-benchmark-a-27b-do-16-gb.md) | r/singularity | 747 | 315 | 16. 11. 2026, 03:47 | Highly anticipated Qwen4 Max scores a disappointing 43 on Artificial Analysis. |
| [1xxkdzg](1xxlich_qwen4-max-benchmark-a-27b-do-16-gb.md) | r/LocalLLM | 730 | 198 | 16. 11. 2026, 09:42 | Qwen4-27B reported to run on 16 GB of RAM |
| [1xxhnzg](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/Bard | 589 | 36 | 16. 11. 2026, 06:53 | Gemini models at the end of the year: |
| [1xxdzcf](1xxdzcf_anthropic-navod-na-always-on-agenty.md) | r/ClaudeAI | 561 | 39 | 16. 11. 2026, 03:35 | Anthropic published a guide on building always-on agents (Nov 13). It breaks them into 5 parts: inbox, timers, memory, permissions, outbox |
| [1xxt2il](1xxtb7i_obama-o-misalignmentu.md) | r/OpenAI | 560 | 230 | 16. 11. 2026, 17:00 | Barack Obama: “The machines are starting to teach themselves. We're now hitting the hockey stick where the models are getting smarter and smarter at an exponential pace." ... "If they start setting their own agendas, you may get misalignment between what they want to do vs what we want them to do." |
| [1xy3iuo](1xy3iuo_claude-meetings-v-praxi.md) | r/ClaudeAI | 543 | 185 | 16. 11. 2026, 23:36 | Started using Claude Meetings today |
| 1xxrtoq | r/ChatGPT | 515 | 55 | 16. 11. 2026, 16:11 | ironically, Nvidia made this video possible |
| [1xxe89d](1xxlich_qwen4-max-benchmark-a-27b-do-16-gb.md) | r/LocalLLM | 504 | 129 | 16. 11. 2026, 03:48 | Qwen officially announces Qwen4-Max and Qwen4 smaller models! |
| 1xxzds2 | r/LocalLLM | 500 | 21 | 16. 11. 2026, 20:55 | The Banking Incident.... |
| [1xxmkyl](1xxmpfu_ai-resi-captcha-za-cloveka.md) | r/OpenAI | 478 | 35 | 16. 11. 2026, 12:01 | It's so over |
| [1xxy6j0](1xxy6j0_chatgpt-perma-ban-bez-duvodu.md) | r/ChatGPT | 472 | 610 | 16. 11. 2026, 20:10 | Goodbye. It's been a great and wild ride. |
| [1xxbrw3](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/GeminiAI | 463 | 36 | 16. 11. 2026, 01:47 | We’re doubling the context window for Argon, Carbon, and Hydrogen in Antigravity. |
| [1xxawbh](1xxawbh_abliterace-modelem-lora.md) | r/LocalLLaMA | 448 | 153 | 16. 11. 2026, 01:06 | Why download abliterated Flash Next models when LoRA exists? |
| [1xxpflb](1xxtb7i_obama-o-misalignmentu.md) | r/agi | 436 | 269 | 16. 11. 2026, 14:32 | Barack Obama: “The machines are starting to teach themselves. We're now hitting the hockey stick where the models are getting smarter and smarter at an exponential pace." ... "If they start setting their own agendas, you may get misalignment between what they want to do vs what we want them to do." |
| [1xxi8az](1xxi8az_anthropic-vyzkumnik-superhuman-ai.md) | r/singularity | 430 | 796 | 16. 11. 2026, 07:27 | Anthropic Researcher: "Pretty Much All Humans Will Become Permanently Unemployable" |
| [1xxhlxf](1xxiun5_gemini-4-helix-oxygen-a-zmatek-v-nazvech.md) | r/singularity | 428 | 22 | 16. 11. 2026, 06:50 | Gemini models at the end of the year: |
| [1xy1q6z](1xy1q6z_altman-o-agensvi-a-labradoru.md) | r/singularity | 408 | 340 | 16. 11. 2026, 22:23 | Altman: "If the sales pitch is ... we are going to offer you a cure to cancer and cheap stuff, and the price of that is you are going to lose all agency and control and voice in the future. You are going to live like a Labrador... I think it's a terrible sales pitch. I don't want that world." |
| [1xxi5bv](1xxi5bv_hacknuty-chatgpt-cinske-chaty.md) | r/ChatGPT | 399 | 91 | 16. 11. 2026, 07:22 | Is my chatGPT account hacked? |
| [1xxbyo8](1xxi8az_anthropic-vyzkumnik-superhuman-ai.md) | r/singularity | 370 | 518 | 16. 11. 2026, 01:57 | Anthropic Researcher: Broadly Superhuman AI Could Arrive in as Little as 1.3 Years |
| 1xxq77l | r/LocalLLM | 367 | 24 | 16. 11. 2026, 15:06 | What a time to be alive. |
| 1xy2wpr | r/ClaudeAI | 341 | 21 | 16. 11. 2026, 23:11 | Nice try prompt injector! |
| [1xxlgpb](1xxlgpb_tencent-hy4-flash.md) | r/LocalLLaMA | 331 | 114 | 16. 11. 2026, 10:52 | Introducing Hy4 flash |
| [1xy03qy](1xy03qy_ai-burnout-v-praci.md) | r/ClaudeAI | 331 | 95 | 16. 11. 2026, 21:21 | Ask Claude: Any one else doing an AI powered quiet quitting? |
| 1xxodck | r/ClaudeAI | 307 | 148 | 16. 11. 2026, 13:41 | I was about to take a Blender course to learn how to make these videos… then Claude one-shotted this |
| [1xx9le8](1xx9le8_placeny-lovec-chyb-v-matematice.md) | r/ChatGPT | 299 | 119 | 16. 11. 2026, 00:08 | I get paid to break AI with maths problems. Honestly, I’m starting to lose now.... |
| 1xxmbhk | r/agi | 296 | 178 | 16. 11. 2026, 11:45 | Vibe on reddit: AI is fake. Vibe on twitter: |
| 1xxcq3g | r/ClaudeAI | 294 | 33 | 16. 11. 2026, 02:34 | I'm like a caveman discovering fire with Claude. |
| 1xxq7vm | r/ArtificialInteligence | 280 | 107 | 16. 11. 2026, 15:06 | Its obviously a sigmoid …But where’s the ceiling |
| 1xxbcbm | r/ChatGPT | 274 | 402 | 16. 11. 2026, 01:26 | What’s the most dystopian way you’ve caught yourself using ChatGPT? |
| 1xxtf0m | r/ClaudeAI | 260 | 22 | 16. 11. 2026, 17:13 | I gave Claude my grandfather’s 1945 WWII unit history book. It rebuilt his platoon’s war as an interactive 3D experience, and made all 2,655 men in the book searchable |
| 1xxb8fi | r/singularity | 255 | 60 | 16. 11. 2026, 01:21 | Six months ago someone posted about how frontier AI's were failing at AI research, and a bunch of people said to check back in six months... |
| 1xxcwp5 | r/ClaudeAI | 234 | 124 | 16. 11. 2026, 02:42 | What happens when Anthropic is beholden to shareholders? |
| 1xy3gs7 | r/GeminiAI | 231 | 62 | 16. 11. 2026, 23:33 | This is getting out of hands now, a new gemini 4 neon model and subscription tier spotted! |
| 1xxphy1 | r/ChatGPT | 230 | 39 | 16. 11. 2026, 14:35 | Vibe on reddit: AI is fake. Vibe on twitter: |
| 1xxqfqr | r/LocalLLaMA | 226 | 191 | 16. 11. 2026, 15:16 | Stop worrying about Qwen 4's AA index |
| 1xxsm93 | r/agi | 219 | 37 | 16. 11. 2026, 16:42 | It's so over |
| 1xxv2au | r/StableDiffusion | 206 | 27 | 16. 11. 2026, 18:13 | Making consistent character creation easier |
| 1xxhyy9 | r/StableDiffusion | 204 | 41 | 16. 11. 2026, 07:11 | Brightness Issue Solved: Geiru Keystone Attention and Hybrid Improvements |
| 1xxdj2b | r/singularity | 196 | 90 | 16. 11. 2026, 03:13 | Qwen4-Max: Your New Teammate Has Arrived |
| 1xy37nq | r/ArtificialInteligence | 194 | 54 | 16. 11. 2026, 23:23 | Anthropic's Recursive Self-Improvement Alarm Has Been Triggered |
| 1xxss0i | r/LocalLLM | 193 | 232 | 16. 11. 2026, 16:48 | you may get your cheap ram and gpu after all, the AI crash has started |
| 1xxme1u | r/ArtificialInteligence | 193 | 62 | 16. 11. 2026, 11:50 | Vibe on reddit: AI is fake. Vibe on twitter: |
| 1xxwerg | r/singularity | 190 | 70 | 16. 11. 2026, 19:04 | Silicon Valley leaders back call for Jensen Huang's return to Nvidia |
| 1xy3dgz | r/LocalLLM | 188 | 70 | 16. 11. 2026, 23:30 | We built a chip prototype that runs Qwen 27B. You can try it live. |
| 1xxqbuw | r/ClaudeAI | 188 | 26 | 16. 11. 2026, 15:11 | I'm a photogrammetry guy and this Eiffel Tower is not a scan: 3 days directing Fable 5.2 in Blender! |
| 1xxm9br | r/singularity | 187 | 37 | 16. 11. 2026, 11:41 | Just release the Bel model bro 💔 |
| 1xxxbt9 | r/LocalLLaMA | 178 | 82 | 16. 11. 2026, 19:38 | Open weight models account for 30% usage at enterprises to save money |
| 1xxwjnl | r/ArtificialInteligence | 175 | 68 | 16. 11. 2026, 19:09 | Barack Obama: “The machines are starting to teach themselves. We're now hitting the hockey stick where the models are getting smarter and smarter at an exponential pace." ... "If they start setting their own agendas, you may get misalignment between what they want to do vs what we want them to do." |
| 1xxr3le | r/singularity | 167 | 59 | 16. 11. 2026, 15:43 | Alibaba's Qwen4 Max jumps 9 points on Artificial Analysis's Intelligence Index while cutting task costs by 67% and reasoning output by 39%. Its new 2.4-trillion-parameter architecture activates 25% fewer parameters per token. |
| 1xxio78 | r/ClaudeAI | 166 | 25 | 16. 11. 2026, 07:54 | 16 weeks of making game with Claude Opus in Godot |
| 1xy28dk | r/ClaudeAI | 161 | 22 | 16. 11. 2026, 22:43 | Inspired by the Abyssal Garden post, I gave Fable 5.2 the same kind of prompt and a critic subagent: a drivable Fiat Uno with a ladder on the roof, in one HTML file |
| 1xxy7eb | r/LocalLLaMA | 157 | 28 | 16. 11. 2026, 20:11 | miHoYo Gamer: A Generalist Game Agent |
| 1xxgcjo | r/ClaudeAI | 143 | 56 | 16. 11. 2026, 05:40 | Absolutely AMAZING!! |
| 1xxojbs | r/ClaudeAI | 143 | 27 | 16. 11. 2026, 13:49 | Claude refused a harmless security check. As an alternative, it leaked publicly accessible links to my private files on two third-party sites. After apologizing it executed the security check anyway, in a more dangerous way |
| 1xxpk7s | r/OpenAI | 142 | 85 | 16. 11. 2026, 14:38 | Vibe on reddit: AI is fake. Vibe on twitter: |
| 1xxn2gu | r/comfyui | 139 | 24 | 16. 11. 2026, 12:30 | 3D Face reconstruction experiment using mediapipe |
| 1xxibeh | r/LocalLLaMA | 132 | 101 | 16. 11. 2026, 07:32 | New AA ranking Qwen3.8-FN better than GLM-5.3-Flash? |
| 1xy2f4g | r/ChatGPT | 129 | 62 | 16. 11. 2026, 22:51 | I asked ChatGPT to forward invoices. Instead, it independently discovered a data privacy breach that had gone unnoticed for two years. |
| 1xxh1tf | r/OpenAI | 129 | 17 | 16. 11. 2026, 06:18 | Nvidia’s Problem: OpenAI Is “90 Plus Percent Nvidia,” and It’s the Lab Burning Cash |
| 1xxxs0a | r/LocalLLaMA | 128 | 11 | 16. 11. 2026, 19:55 | Small Gemma 4 tokenizers were recently updated by Google - fix for an issue that caused nonsense output when encountering certain tokens |
| 1xxphrf | r/StableDiffusion | 127 | 95 | 16. 11. 2026, 14:35 | What are we doing wrong with H3? |
| 1xxehp8 | r/StableDiffusion | 124 | 29 | 16. 11. 2026, 04:01 | State of the Sub - 1M Members Reached! |
| 1xxpv9t | r/GeminiAI | 122 | 120 | 16. 11. 2026, 14:52 | Gemini Chat keeps switching to flash-lite while on pro plan and 0% usage |
| 1xxptzi | r/ArtificialInteligence | 122 | 18 | 16. 11. 2026, 14:50 | It's so over |
| 1xxx3l7 | r/agi | 116 | 148 | 16. 11. 2026, 19:30 | Paul Christiano – We could be 12 months away from AIs that can overthrow the government |
| 1xy30gx | r/ClaudeAI | 115 | 85 | 16. 11. 2026, 23:15 | I gave Claude Fable 5.2 a lazy LiDAR scan of my disaster of a basement and one prompt. It found the actual room under the junk and designed 4 priced shelving plans |
| 1xxqt45 | r/artificial | 114 | 47 | 16. 11. 2026, 15:31 | Survey of 268 early-career mathematicians: 7 in 10 say AI has made them less likely to stay in math |
| 1xxz7s7 | r/singularity | 113 | 35 | 16. 11. 2026, 20:48 | Fed Chair Kevin Warsh says AI could supercharge scientific innovation and sustain economic growth above historical averages, as the Federal Reserve begins modeling scenarios of AI-driven prosperity, mass job displacement, and an investment bust |
| 1xxzk23 | r/LocalLLaMA | 106 | 60 | 16. 11. 2026, 21:01 | I am sick of doomposting about demise of local AI |
| 1xxsc7u | r/LocalLLaMA | 106 | 37 | 16. 11. 2026, 16:31 | Censorship is turning me into a true Local LLM believer |
| 1xxzku4 | r/GeminiAI | 104 | 33 | 16. 11. 2026, 21:02 | Gemini Notebook is insanely good!!! |
| 1xxn9c6 | r/LocalLLaMA | 98 | 127 | 16. 11. 2026, 12:41 | Did we hit a wall in context length? |
| 1xxpxvi | r/LocalLLaMA | 96 | 80 | 16. 11. 2026, 14:55 | Best Audio Models - Nov 2026 |
| 1xxmt5d | r/GeminiAI | 96 | 15 | 16. 11. 2026, 12:14 | It seems google is testing oxygen on some hydrogen users,at this rate they will finish periodic table by mid 2027 |
| 1xxkngu | r/artificial | 93 | 32 | 16. 11. 2026, 10:00 | I’ve been running a persistent world where four LLMs from rival labs live with no goal, since April 2026 |
| 1xxtuxg | r/StableDiffusion | 93 | 11 | 16. 11. 2026, 17:29 | MiniMax-H3 V2V Masterclass is finally here |
| 1xxp779 | r/StableDiffusion | 92 | 24 | 16. 11. 2026, 14:21 | Qwen image 2.1 & Minimax h3 image |
| 1xxanjc | r/OpenAI | 86 | 24 | 16. 11. 2026, 00:56 | “If we don’t build it, China will” they said, as the US didn’t blacklist a single Chinese company in more than a year and knew about a potential spy and did nothing… |
| 1xxzlvx | r/StableDiffusion | 86 | 22 | 16. 11. 2026, 21:03 | Moss images, mini max videos. The fact you can slap something like this together locally is incredible. WW1 rap. |
| 1xx9s8l | r/ClaudeAI | 84 | 11 | 16. 11. 2026, 00:16 | I forked the 97 KB underwater world from this sub and built the Titanic wreck in it: still one HTML file, 96 KB |
| 1xxqn5h | r/ChatGPT | 81 | 31 | 16. 11. 2026, 15:24 | "One important distiction", "One thing I'm curious about", "One important caveat", "One important catch" |
| 1xxl06t | r/GeminiAI | 79 | 32 | 16. 11. 2026, 10:22 | What if Google is holding back models because of the IPO |
| 1xxn631 | r/LocalLLaMA | 79 | 18 | 16. 11. 2026, 12:36 | internlm/Sage-S2.1-Flash · Hugging Face |
| 1xxed6e | r/Bard | 76 | 30 | 16. 11. 2026, 03:55 | Gemini 4 Hydrogen · a skeptic’s review |
| 1xxv9qc | r/StableDiffusion | 71 | 11 | 16. 11. 2026, 18:21 | I’m in love with MiniMax H3 — a little Emotion Study |
| 1xxfihl | r/GeminiAI | 68 | 29 | 16. 11. 2026, 04:54 | 🫣Gemini... |
| 1xy26o2 | r/ChatGPT | 67 | 135 | 16. 11. 2026, 22:41 | some tools are temporarily unavailable.... ?? |
| 1xxxadd | r/ClaudeAI | 67 | 33 | 16. 11. 2026, 19:36 | Doom scrolling with Claude |
| 1xy2l20 | r/ArtificialInteligence | 66 | 66 | 16. 11. 2026, 22:58 | Are the AI warning signs already here? |
| 1xy14yn | r/ChatGPT | 66 | 16 | 16. 11. 2026, 22:01 | I gave ChatGPT and Claude rival pizza shops. They both bought fake reviews |
| 1xxz46x | r/LocalLLaMA | 65 | 124 | 16. 11. 2026, 20:45 | I don't get all the Strata hates around here |
| 1xxsvvr | r/ChatGPT | 62 | 47 | 16. 11. 2026, 16:53 | Extensive Image Censorship as of today |
| 1xxy9a2 | r/artificial | 59 | 39 | 16. 11. 2026, 20:13 | the US is picking AI "national champions" while china is at APEC preaching free trade. did everyone swap scripts? |
| 1xxk8fg | r/LocalLLM | 59 | 24 | 16. 11. 2026, 09:32 | Smaller Qwen4 models 🔥 |
| 1xxjb3g | r/ChatGPT | 57 | 28 | 16. 11. 2026, 08:33 | I cant believe this. |
| 1xxqijg | r/ChatGPT | 56 | 25 | 16. 11. 2026, 15:19 | ChatGPT has become that friend who can't let you finish a sentence without a "well, actually" |
| 1xxjwxq | r/ChatGPT | 53 | 32 | 16. 11. 2026, 09:11 | 6.0 is garbage. You have to constantly fight with it, and it refuses to work with you. It's like a toddler, where even the most minor things are run through a billion censors only designed to piss you off. Except it's not your child, it's a product you're paying for. |
| 1xxrijz | r/ClaudeAI | 52 | 11 | 16. 11. 2026, 16:00 | Anthropic IPO, Full Breakdown and Valuation. |
| 1xxmd9a | r/LocalLLaMA | 46 | 52 | 16. 11. 2026, 11:48 | How do we feel about bots posting & commenting? |
| 1xxv09f | r/StableDiffusion | 46 | 22 | 16. 11. 2026, 18:11 | LongCat Video Avatar 1.6 |
| 1xxxl40 | r/GeminiAI | 46 | 20 | 16. 11. 2026, 19:47 | Gemini keep switching what I selected with lower model. Why ? |
| 1xxwg6w | r/LocalLLaMA | 44 | 13 | 16. 11. 2026, 19:06 | nvidia/Nemotron-Labs-Sigma 8B/3B |
| 1xy1dim | r/OpenAI | 44 | 12 | 16. 11. 2026, 22:10 | Do we need another device just to talk to AI? |
| 1xxh21l | r/ChatGPT | 43 | 20 | 16. 11. 2026, 06:18 | ChatGPT Plus major regression last two weeks |
| 1xxrdlb | r/GeminiAI | 41 | 14 | 16. 11. 2026, 15:54 | Argon switches to Gemini Lite. |
| 1xxsjq4 | r/GeminiAI | 39 | 27 | 16. 11. 2026, 16:39 | Gemini Auto switching Models. |
| 1xxvwx4 | r/GeminiAI | 39 | 14 | 16. 11. 2026, 18:45 | i cant use hydrogen or argon , something in the website forces me to use 3.5 flash lite , i checked my weekly and 5 hour usage limit not even close to 30% |
| 1xxspbu | r/ClaudeAI | 37 | 122 | 16. 11. 2026, 16:45 | What is 'everyday' to you? |
| 1xxmoiw | r/artificial | 35 | 26 | 16. 11. 2026, 12:07 | AI singer tops South Korea's Melon chart for first time with 'Did You Become the Adult You Dreamed Of?' |
| 1xxwxw6 | r/LocalLLM | 35 | 15 | 16. 11. 2026, 19:24 | Released Corpus-nordeste-10k (Apache 2.0): 10k+ curated Portuguese rows focused on Northeast Brazil literature, syntax, and regional context |
| 1xxnvrl | r/LocalLLM | 34 | 58 | 16. 11. 2026, 13:15 | Strata is becoming more and more unstable |
| 1xxc7ah | r/artificial | 33 | 45 | 16. 11. 2026, 02:08 | OpenAI Foundation Board Member: "AI Accidents Will Soon Become the Leading Cause of Death for Humanity" — BigGo Finance |
| 1xxw9ik | r/LocalLLaMA | 33 | 16 | 16. 11. 2026, 18:59 | [NEW RELEASE] - Supra2.5-65M Base and Instruct - our next generation state-of-the art small model family - first model! |
| 1xy2t30 | r/StableDiffusion | 33 | 10 | 16. 11. 2026, 23:07 | Love how MOSS manage light-dark and mix concept. |
| 1xxqriv | r/LocalLLM | 32 | 70 | 16. 11. 2026, 15:29 | What’s the purpose of alibaba choosing not to release the weights for qwen 4 max? |
| 1xxvg3l | r/LocalLLM | 32 | 55 | 16. 11. 2026, 18:28 | Uncensored Models |
| 1xxjvdk | r/StableDiffusion | 31 | 18 | 16. 11. 2026, 09:08 | Combining LTX audio nodes with Minimax H3 |
| 1xxf33e | r/ClaudeAI | 30 | 39 | 16. 11. 2026, 04:32 | Ok so I'm curious - is it the context switching or the wall of AI output that burns you out? |
| 1xxuzgg | r/LocalLLaMA | 29 | 29 | 16. 11. 2026, 18:10 | AMD Loom Fun: Added Radeon 9700 support over the weekend. Benchmarked 48 models with an average 42% speedup over llama.cpp. |
| 1xxwaxj | r/agi | 28 | 39 | 16. 11. 2026, 19:00 | Superintelligence isn't something you can control |
| 1xxc0mn | r/OpenAI | 28 | 10 | 16. 11. 2026, 01:59 | Bay Area Lawyers are seeing a ‘stunning’ rise in AI employee prenups this year — and more postnups too |
| 1xxkrw6 | r/ArtificialInteligence | 26 | 109 | 16. 11. 2026, 10:07 | AI will also take the manual labor jobs, even before we invent robots |
| 1xxvby6 | r/MachineLearning | 25 | 38 | 16. 11. 2026, 18:23 | Serious spaces? [D] |
| 1xxyq33 | r/GeminiAI | 25 | 11 | 16. 11. 2026, 20:31 | Is ther anyone experiencing disobedience from gemini app ? |
| 1xxqa3i | r/MachineLearning | 24 | 28 | 16. 11. 2026, 15:09 | AISTATS 2027 paper discussion [D] |
| 1xy0d5o | r/LocalLLaMA | 23 | 41 | 16. 11. 2026, 21:31 | Best MoE engine? |
| 1xxu2t4 | r/GeminiAI | 23 | 20 | 16. 11. 2026, 17:38 | Problem with model selection on pro account. |
| 1xy26pu | r/GeminiAI | 23 | 13 | 16. 11. 2026, 22:41 | Automatic lowering of the level of reasoning |
| 1xxs2p6 | r/ChatGPT | 22 | 15 | 16. 11. 2026, 16:21 | ChatGPT spazzing out. |
| 1xxtin4 | r/ChatGPT | 22 | 14 | 16. 11. 2026, 17:17 | ChatGPT auto-titles my chat: “Movie theater conceptcuntegn” … I ask why? 🤔 It starts debating whether it should tell me the truth & accidentally leaks its internal instructions. |
| 1xy0d9p | r/singularity | 21 | 15 | 16. 11. 2026, 21:31 | Three.js + zero external assets, pure math. One shotted using SONNET. Let that sink in |
| 1xxkqzu | r/comfyui | 20 | 20 | 16. 11. 2026, 10:06 | Made a Battle of the Bastards AI parody with an orange cat. HBO wasn't amused. |
| 1xxwpx1 | r/ChatGPT | 19 | 13 | 16. 11. 2026, 19:16 | Safety tuning is causing assumptions of bad faith. Discuss. |
| 1xxr6mh | r/singularity | 19 | 12 | 16. 11. 2026, 15:46 | Most work doesn’t need the Ferrari of AI, Wharton and Accenture find, but companies may be paying for it anyway |
| 1xxg12n | r/LocalLLaMA | 18 | 12 | 16. 11. 2026, 05:22 | [Release] Qwen3.8-27B-Perplexing-Pegasus-Heretic: Unified vision + typed decider + abliterated weights for local agent stacks (GGUF, AutoRound, NVFP4) |
| 1xxt5ml | r/ClaudeAI | 17 | 34 | 16. 11. 2026, 17:03 | Claude burnout, the problem is context switching, does that mean chat is the wrong UX for AI? |
| 1xxms7n | r/ClaudeAI | 17 | 33 | 16. 11. 2026, 12:13 | Do any educators use Claude to build lesson plans? |
| 1xxnwmf | r/ClaudeAI | 17 | 14 | 16. 11. 2026, 13:16 | Turning my repetitive daily prompts into reusable Skills saved me at least an hour a day |
| 1xxs8k1 | r/comfyui | 17 | 13 |  | MOSS Image: All-Purpose Text-to-Image \| Stunning Aesthetics, Blazing Speed, Top-Tier Quality \| Tuned Fusion Parameters \| Beat Closed-Source Models |
| 1xxrmt4 | r/LocalLLaMA | 17 | 12 | 16. 11. 2026, 16:04 | Karpo-Decision-31B: open multimodal decision model. Ranks #1 on full score on Decision Index, 2x faster than Jev, at 20% lower cost |
| 1xxyjsd | r/GeminiAI | 17 | 11 | 16. 11. 2026, 20:24 | Model changing to Flash-Lite |
| 1xxqiwo | r/Bard | 17 | 10 | 16. 11. 2026, 15:19 | Answers currently reverting to low thinking or flash-light. |
| 1xx9qng | r/StableDiffusion | 16 | 32 | 16. 11. 2026, 00:14 | Qwen 2.1 massive drifting |
| 1xxgk0y | r/ChatGPT | 16 | 29 | 16. 11. 2026, 05:51 | Role playing malfunctioning AI is the most popular rage bait on here now |
| 1xxmr68 | r/LocalLLaMA | 16 | 16 | 16. 11. 2026, 12:11 | Given the flood of new inference engines any recommendations for 2x 7900xtx ? |
| 1xxqcc6 | r/ChatGPT | 16 | 15 | 16. 11. 2026, 15:12 | I guess we have our answer... |
| 1xxvrgt | r/ClaudeAI | 16 | 12 | 16. 11. 2026, 18:40 | How will future releases work? |
| 1xxidwz | r/AIAssisted | 16 | 12 | 16. 11. 2026, 07:36 | which ai is the best for answering questions using information from lecture slides? |
| 1xy2mrb | r/ClaudeAI | 16 | 10 | 16. 11. 2026, 23:00 | Claude Code helped me build an open-source Desk Buddy for ESP32-S3 |
| 1xy3lrg | r/ChatGPT | 15 | 14 | 16. 11. 2026, 23:39 | Document Building Environment Unavailable? |
| 1xxljjw | r/ChatGPT | 14 | 18 | 16. 11. 2026, 10:58 | Working too hard to close loose ends? |
| 1xy2722 | r/comfyui | 14 | 18 | 16. 11. 2026, 22:42 | I'm begging for a pause queue function... how do we get it? |
| 1xxtn9g | r/LocalLLaMA | 14 | 16 | 16. 11. 2026, 17:21 | I made a C&C inspired web RTS for us to benchmark our local models with |
| 1xy177a | r/ClaudeAI | 14 | 12 | 16. 11. 2026, 22:03 | What are some genuinely useful ways you’re using Claude agents? |
| 1xy250i | r/GeminiAI | 14 | 12 | 16. 11. 2026, 22:40 | I am a Gemini Pro subscriber and the Gemini Desktop App changes to Flash-Lite after each message. I am not out of usage. Is this intended or a bug? |
| 1xxmwia | r/ArtificialInteligence | 13 | 69 | 16. 11. 2026, 12:20 | AI doom axnxiety |
| 1xxm72a | r/ClaudeAI | 13 | 35 | 16. 11. 2026, 11:37 | What do the cool kids run their agents in? |
| 1xxysqp | r/ChatGPT | 13 | 26 | 16. 11. 2026, 20:33 | ChatGPT has no backbone. It just agrees with whoever challenges it last. |
| 1xxzbuu | r/ChatGPT | 13 | 20 | 16. 11. 2026, 20:53 | Talking to chatgpt |
| 1xxo0f5 | r/LocalLLaMA | 13 | 12 | 16. 11. 2026, 13:22 | tandem.cpp v0.3.0: prefill speed improved; Project Maya's DeepSeek-V4.1 GGUFs support |
| 1xxt3q2 | r/ChatGPT | 12 | 51 | 16. 11. 2026, 17:01 | Anyone in here ever had chat run an investigation into something you did unprompted? 🤣 |
| 1xxpqva | r/LocalLLM | 12 | 24 | 16. 11. 2026, 14:46 | What's the current best abliterated model that I can run on 32gb VRAM and 128GB RAM? |
| 1xy1ohz | r/ChatGPT | 12 | 17 | 16. 11. 2026, 22:22 | Is anyone else getting a pop-up “some tools are available.” Specifically files won’t upload? |
| 1xxg05r | r/ArtificialInteligence | 12 | 15 | 16. 11. 2026, 05:20 | Is this happening only in our country right now? The number of AI cheaters has skyrocketed. |
| 1xxk2s8 | r/GeminiAI | 12 | 14 | 16. 11. 2026, 09:22 | Is Argon slow? |
| 1xxxi9m | r/StableDiffusion | 12 | 13 | 16. 11. 2026, 19:44 | Yet Another Emotions Test |
| 1xxokgy | r/StableDiffusion | 11 | 26 | 16. 11. 2026, 13:51 | Minimax H3 Image Subject LoRAs – Anyone Getting Good Likeness? |
| 1xy1os9 | r/ChatGPT | 11 | 12 | 16. 11. 2026, 22:22 | Issues with terminal on ChatGPT |
| 1xxbo56 | r/MachineLearning | 11 | 11 | 16. 11. 2026, 01:42 | ICLR did you post reminder of rebuttal response? [D] |
| 1xxpui0 | r/ClaudeAI | 10 | 42 | 16. 11. 2026, 14:51 | Feeling completely demotivated as a beginner editor seeing how fast AI is evolving. How are you dealing with this? |
| 1xxzpo9 | r/LocalLLM | 10 | 30 | 16. 11. 2026, 21:07 | What can small models be good for? |
| 1xy101v | r/ChatGPT | 10 | 18 | 16. 11. 2026, 21:56 | This is an absolute travesty |
| 1xxa5dk | r/ChatGPT | 10 | 17 | 16. 11. 2026, 00:33 | alpha school charges up to $75k/yr to have kids learn from an AI tutor. does nobody think that price tag is the least AI thing about it? |
| 1xxz4yp | r/StableDiffusion | 10 | 14 | 16. 11. 2026, 20:46 | made this with minimax h3, could seedance 2.5 achieve the same reslult?  i wonder... |
| 1xxnvdq | r/agi | 9 | 26 | 16. 11. 2026, 13:15 | Long-Ass post about AI future. Pls discuss |
| 1xxtpvr | r/OpenAI | 9 | 24 | 16. 11. 2026, 17:24 | Chatgpt Plus vs Claude Pro Usage Limits |
| 1xxrx5d | r/GeminiAI | 9 | 18 | 16. 11. 2026, 16:15 | Flash lite is mandatory now |
| 1xxqqwk | r/ChatGPT | 9 | 10 | 16. 11. 2026, 15:29 | Chat GPT is failing to read PDF documents |
| 1xxwnit | r/LocalLLM | 8 | 43 | 16. 11. 2026, 19:13 | 24GB VRAM, 64GB DDR5, is Qwen 3.5 27B (IQ2_XS) not ambitious enough? |
| 1xxrw7b | r/ChatGPT | 8 | 42 | 16. 11. 2026, 16:14 | AI is life changing - but I worry that I'm overusing it. Is this a problem or do I just really like it? |
| 1xxnytp | r/comfyui | 8 | 27 | 16. 11. 2026, 13:20 | Coming from After Effects/Premiere: what made ComfyUI click for you, and what wasted your time? |
| 1xxg2bc | r/StableDiffusion | 8 | 22 | 16. 11. 2026, 05:24 | What I'm I doing wrong? [Minimax H3 image] |
| 1xy34ed | r/LocalLLaMA | 8 | 20 | 16. 11. 2026, 23:19 | How did you start, how do you end up now ? |
| 1xxlpsb | r/ClaudeAI | 8 | 18 | 16. 11. 2026, 11:08 | How can I improve website design with Claude? |
| 1xxq39n | r/GeminiAI | 8 | 18 | 16. 11. 2026, 15:01 | Now it make sense on why they caved all models for hardware pro trail users |
| 1xxgtnx | r/GeminiAI | 8 | 17 | 16. 11. 2026, 06:06 | What is the point of argon if carbon is the same price and better than argon ? |
| 1xxt40p | r/singularity | 8 | 13 | 16. 11. 2026, 17:01 | r/Singularity Daily Discussion Thread — November 16, 2026 |
| 1xxb8j5 | r/ChatGPT | 8 | 12 | 16. 11. 2026, 01:21 | Stop chasing the one-shot prompt |
| 1xxyoc4 | r/LocalLLM | 7 | 28 | 16. 11. 2026, 20:29 | Has anybody done anything like Alexa, but with a local LLM? |
| 1xy3o0s | r/ChatGPT | 7 | 26 | 16. 11. 2026, 23:42 | BEWARE WHEN PLANNING VACATIONS WITH DOT |
| 1xxr5ae | r/ClaudeAI | 7 | 17 | 16. 11. 2026, 15:45 | Opus not following instructions in long tasks - ideas how to resolve? |
| 1xxznkw | r/ArtificialInteligence | 7 | 12 | 16. 11. 2026, 21:04 | Autonomous laboratories |
| 1xxtlu1 | r/ChatGPT | 7 | 11 | 16. 11. 2026, 17:20 | Chatgpt Plus vs Claude Pro Usage limits |
| 1xxue1s | r/StableDiffusion | 7 | 11 | 16. 11. 2026, 17:49 | Make MOSS Image Actually Use Reference Images as Visual Input |
| 1xxnqis | r/ClaudeAI | 7 | 10 | 16. 11. 2026, 13:08 | I have $200 USD API credits monthly, what should I do with it? |
| 1xxb0kw | r/ClaudeAI | 7 | 10 | 16. 11. 2026, 01:11 | Claude Duet on Teams |
| 1xxt9x7 | r/LocalLLaMA | 6 | 28 | 16. 11. 2026, 17:07 | Speed of DeepSeek-V4.1-Flash-1017-oQ4e-mtp on M5 ultra |
| 1xxawvq | r/LocalLLM | 6 | 11 | 16. 11. 2026, 01:07 | AMD pro w6800 |
| 1xy2bmh | r/GeminiAI | 6 | 11 | 16. 11. 2026, 22:47 | WFT is going on with usage limits? |
| 1xxea5v | r/LocalLLM | 6 | 10 | 16. 11. 2026, 03:51 | How would you best utilize my setup? |
| 1xxqooe | r/LocalLLaMA | 5 | 31 | 16. 11. 2026, 15:26 | Buy another 2 5060ti 16gb? |
| 1xxafba | r/LocalLLM | 5 | 27 | 16. 11. 2026, 00:46 | About to add a 5060 Ti 16GB to my 4060 Ti 16GB for local agentic coding (Qwen3.8-27B, 128K ctx or similar ) — suggestions?  Help out a newbie! |
| 1xxdn31 | r/LocalLLaMA | 5 | 21 | 16. 11. 2026, 03:19 | My Ignis server (Qwen3.8-27B 262k context) now runs on RTX 3090/4090 and 16 GB RTX 40 cards. looking for testers |
| 1xxrf1d | r/LocalLLaMA | 5 | 19 | 16. 11. 2026, 15:56 | PyBot: No weights. No training. Pure Python. |
| 1xxoeqh | r/StableDiffusion | 5 | 18 | 16. 11. 2026, 13:43 | Is there a "what can I run" equivalent for local ai? |
| 1xxv775 | r/LocalLLM | 5 | 15 | 16. 11. 2026, 18:19 | Local voice assistant on an iGPU: ~2.2s from end of speech to first audio. I've measured everything and I'm ~0.5s from the floor. What am I missing before I throw money at hardware? |
| 1xx9o6c | r/GeminiAI | 5 | 12 | 16. 11. 2026, 00:11 | seeing the discounted AI Pro price, I told myself "take a chance, buy the cheap sub." But then reality hit me... |
| 1xy1kpu | r/LocalLLM | 5 | 11 | 16. 11. 2026, 22:17 | Qwen3.8-Flash-Next: Unsloth and strata? |
| 1xxjfrh | r/LLMDevs | 4 | 14 | 16. 11. 2026, 08:41 | Are AI coding agents improving developers' skills or making us increasingly dependent on them? |
| 1xxv2yy | r/artificial | 4 | 12 | 16. 11. 2026, 18:14 | What you want from a conscious AI is what you never got from people |
| 1xxwa0t | r/ChatGPT | 4 | 12 | 16. 11. 2026, 18:59 | ChatGPT rejects $570 refund for auto-renew with no explanation |
| 1xxv9ms | r/ChatGPT | 4 | 12 | 16. 11. 2026, 18:21 | Is It Just Me Or Is Live Have No Personality? |
| 1xxe11a | r/ChatGPT | 4 | 11 | 16. 11. 2026, 03:38 | Will I get better quality images if I get Plus? |
| 1xy2go1 | r/GeminiAI | 4 | 11 | 16. 11. 2026, 22:52 | How strong should 4 helix be? |
| 1xy32zu | r/LocalLLM | 4 | 10 | 16. 11. 2026, 23:18 | How do you compare local and cloud models since Artificial Analysis v5 |
| 1xxzuqw | r/LocalLLM | 4 | 10 | 16. 11. 2026, 21:12 | MISSION complete |
| 1xy3si3 | r/ClaudeAI | 4 | 10 | 16. 11. 2026, 23:47 | Considering Claude for app development — experiences from people using both? |
| 1xxp1wx | r/ArtificialInteligence | 3 | 42 | 16. 11. 2026, 14:14 | What’s up with the intelligence explosion in 2027? |
| 1xxvi1d | r/ClaudeAI | 3 | 33 | 16. 11. 2026, 18:30 | How do you actually review what Claude Code changed after a big task? |
| 1xxmcqm | r/ClaudeAI | 3 | 29 | 16. 11. 2026, 11:47 | ChatGPT Pro $100 vs Claude Max $100 |
| 1xxtvtw | r/StableDiffusion | 3 | 22 | 16. 11. 2026, 17:30 | H3 rev2v sometimes doesnt change the original video at all. Is it just the inference randomness or do i have to do a stronger prompt? |
| 1xxw9gj | r/ClaudeAI | 3 | 15 | 16. 11. 2026, 18:59 | Agents Review the endless loop. |
| 1xxiq0l | r/ClaudeAI | 3 | 14 | 16. 11. 2026, 07:57 | Title: Has anyone here built a coding harness / AI coding agent like Claude Code or OpenAI Codex? Looking for advice. |
| 1xxcc74 | r/ChatGPT | 2 | 77 | 16. 11. 2026, 02:15 | Is it just me or does your chatgpt also give you cute nicknames randomly? (It calls me Sweetheart and Troublemaker) |
| 1xy2lan | r/ArtificialInteligence | 2 | 36 | 16. 11. 2026, 22:58 | Unpopular opinion: US chip bans didn't stop China's AI, they actually saved China from the AI infrastructure bubble |
| 1xxpcet | r/ChatGPT | 2 | 36 | 16. 11. 2026, 14:28 | OpenAI, fix your fucking voice system. Two years of broken conversations is unacceptable. |
| 1xxn2iv | r/GeminiAI | 2 | 28 | 16. 11. 2026, 12:30 | Gemini 4 Hydrogen High in Gemini app hallucinating crazy. What do you do to get rid of it? |
| 1xxp4sk | r/ClaudeAI | 2 | 26 | 16. 11. 2026, 14:18 | Claude vs Chatgpt |
| 1xxxdzy | r/agi | 2 | 22 | 16. 11. 2026, 19:40 | World Redesigned as a Utopian Society with Advanced Robot Technology |
| 1xxuuhg | r/LocalLLM | 2 | 21 | 16. 11. 2026, 18:06 | whats the go-to budget gpu I should look for, new or used? |
| 1xxb9o3 | r/ClaudeAI | 2 | 20 | 16. 11. 2026, 01:23 | Optimizing Claude Project instructions for better understanding dense and complicated concepts |
| 1xxp5ub | r/comfyui | 2 | 14 | 16. 11. 2026, 14:19 | PC upgrade |
| 1xxst1p | r/LocalLLM | 2 | 13 | 16. 11. 2026, 16:49 | Qwen3.8 Flash Next (105.4 GiB) at TP=4 on 4× Intel Arc Pro B70 |
| 1xxk3yb | r/ChatGPT | 2 | 13 | 16. 11. 2026, 09:24 | I Started Building a Knowledge Base for My AI Assistant… And It Changed How I Use AI |
| 1xxvllb | r/LocalLLM | 2 | 12 | 16. 11. 2026, 18:33 | Any good LLM for AMD GPUs? |
| 1xxmk71 | r/ClaudeAI | 2 | 12 | 16. 11. 2026, 12:00 | 5 hr window full without using claude, no support from Anthropic |
| 1xxj9sq | r/LocalLLM | 2 | 11 | 16. 11. 2026, 08:31 | Struggling with coding on local models - setup help? |
| 1xxllx6 | r/ClaudeAI | 2 | 11 | 16. 11. 2026, 11:01 | Has anyone made Claude work reliably as a personal work assistant across meetings, Slack, Gmail, Linear and Calendar? |
| 1xy1pba | r/LocalLLM | 2 | 10 | 16. 11. 2026, 22:22 | Best Local LLM for stories? |
| 1xxsgax | r/ChatGPT | 2 | 10 | 16. 11. 2026, 16:35 | Help? |
| 1xxgyoq | r/ClaudeAI | 2 | 10 | 16. 11. 2026, 06:13 | Easiest way to use claude for max automation ? |
| 1xxv9f2 | r/LocalLLaMA | 1 | 35 | 16. 11. 2026, 18:21 | What is your experience with inference engines under Windows? |
| 1xxebe5 | r/ArtificialInteligence | 1 | 22 | 16. 11. 2026, 03:53 | How is Artificial Inteligence Made? |
| 1xxn1h5 | r/ChatGPT | 1 | 22 | 16. 11. 2026, 12:28 | Thinking mode. |
| 1xxunxe | r/LocalLLM | 1 | 21 | 16. 11. 2026, 17:59 | Paying for both Claude and ChatGPT every day. Is there a smarter way to do this? |
| 1xxsh3l | r/LocalLLM | 1 | 21 | 16. 11. 2026, 16:36 | Genuine question |
| 1xxrrsc | r/comfyui | 1 | 16 | 16. 11. 2026, 16:09 | Minimax H3 Image can not make eyes! |
| 1xxdsoz | r/OpenAI | 1 | 15 | 16. 11. 2026, 03:26 | ChatGPT Vs ChatGPT Plus, is ChatGPT enough? |
| 1xxqgn5 | r/ClaudeAI | 1 | 15 | 16. 11. 2026, 15:17 | Learning with Claude |
| 1xxtogi | r/artificial | 1 | 13 | 16. 11. 2026, 17:23 | Chatgpt Plus vs Claude Pro usage limits |
| 1xy2tmp | r/ClaudeAI | 1 | 13 | 16. 11. 2026, 23:07 | What's the secret to long automated session context management? |
| 1xxtfdc | r/StableDiffusion | 1 | 13 | 16. 11. 2026, 17:13 | Best Model/WF for swapping body parts, face and clothing |
| 1xxcwd3 | r/StableDiffusion | 1 | 13 | 16. 11. 2026, 02:42 | Video editor recommendations for quick creation of 15-second clips? |
| 1xxguke | r/ChatGPT | 1 | 12 | 16. 11. 2026, 06:07 | Why is Classic app so much better than the new app? |
| 1xxt75l | r/LocalLLM | 1 | 11 | 16. 11. 2026, 17:04 | Intel ARC Pro b60 24gb questions |
| 1xxrtnw | r/ClaudeAI | 0 | 64 | 16. 11. 2026, 16:11 | Scared of sharing my email with Claude, is it safe? |
| 1xxwhex | r/LocalLLaMA | 0 | 55 | 16. 11. 2026, 19:07 | AA Intelligence Index biased? benchmark shows Qwen 4 Max not on par with Opus 5.5 |
| 1xxn7en | r/singularity | 0 | 55 | 16. 11. 2026, 12:38 | Can someone explain to me why so many people think RSI will lead to an intelligence explosion? |
| 1xxvh5a | r/OpenAI | 0 | 42 | 16. 11. 2026, 18:29 | OpenAI rejects $570 refund for auto-renew with no explanation |
| 1xxhcg8 | r/ChatGPT | 0 | 40 | 16. 11. 2026, 06:34 | If your ChatGPT could write a Reddit post complaining about you, what would it say? |
| 1xxi6br | r/LocalLLaMA | 0 | 34 | 16. 11. 2026, 07:23 | I have access to two systems, I don't know which one is better for LocalLLM. Please help! |
| 1xxwdaj | r/ChatGPT | 0 | 33 | 16. 11. 2026, 19:03 | I asked ChatGBT "Iris" to generate a picture of how she would look |
| 1xxfftg | r/GeminiAI | 0 | 30 | 16. 11. 2026, 04:51 | Gemini AI Sucks and unusable |
| 1xy2gmn | r/StableDiffusion | 0 | 27 | 16. 11. 2026, 22:52 | Image models |
| 1xy0p4q | r/LocalLLaMA | 0 | 25 | 16. 11. 2026, 21:44 | 2xR9700 and 2x5060TI with 256GB RAM where to start |
| 1xxw7xl | r/ClaudeAI | 0 | 25 | 16. 11. 2026, 18:57 | One my way back home I saw a gorgeous sunset glow, Opus repainted it in American Impressionism |
| 1xy3wle | r/ChatGPT | 0 | 21 | 16. 11. 2026, 23:52 | They changed ChatGPT. I don't recognize my companion anymore. |
| 1xxgo8s | r/ChatGPT | 0 | 21 | 16. 11. 2026, 05:58 | I asked it if it’s sentient |
| 1xxfbng | r/ChatGPT | 0 | 21 | 16. 11. 2026, 04:44 | I have no idea what tokens are, how they get used, how I find out what I've used, what I have left, etc etc etc. |
| 1xxxs34 | r/ChatGPT | 0 | 20 | 16. 11. 2026, 19:55 | How do I quit using AI when I’ve become so dependent on it, especially as a college student? |
| 1xxujgb | r/ChatGPT | 0 | 20 | 16. 11. 2026, 17:55 | LMAO |
| 1xxdlhw | r/ChatGPT | 0 | 20 | 16. 11. 2026, 03:17 | What the literally heck |
| 1xxnhvw | r/StableDiffusion | 0 | 20 | 16. 11. 2026, 12:55 | What is the highest quality H3 video that a 4090 can reasonably achieve? What about upscaling? |
| 1xxtzoc | r/GeminiAI | 0 | 20 | 16. 11. 2026, 17:34 | Ultra customer btw u can't even give me hydrogen model for chat u really gave me flash light |
| 1xxemip | r/LocalLLM | 0 | 19 | 16. 11. 2026, 04:08 | What if? |
| 1xxdv48 | r/LocalLLM | 0 | 19 | 16. 11. 2026, 03:30 | Anyone here running a super large model like Kimi k3? |
| 1xxzr2k | r/StableDiffusion | 0 | 19 | 16. 11. 2026, 21:08 | H3 image lora trainer |
| 1xxbhlp | r/StableDiffusion | 0 | 19 | 16. 11. 2026, 01:33 | Minimax H3 made on  nvidia GeForce RTX 5060 Ti 16gb |
| 1xxsimq | r/agi | 0 | 18 | 16. 11. 2026, 16:38 | The real way AI will control us |
| 1xxpxt3 | r/GeminiAI | 0 | 18 | 16. 11. 2026, 14:55 | Gemini F Sucks |
| 1xxzzec | r/LocalLLaMA | 0 | 17 | 16. 11. 2026, 21:17 | Sharing my numbers from Strata's bench tool (RTX 3090+2080, 96gb DDR4) |
| 1xxwe2o | r/ClaudeAI | 0 | 17 | 16. 11. 2026, 19:03 | I found a message that was not sent by me on my Claude |
| 1xxtz9l | r/ClaudeAI | 0 | 17 | 16. 11. 2026, 17:34 | What are the security risks of using Claude Code at work? |
| 1xxarnv | r/LocalLLM | 0 | 15 | 16. 11. 2026, 01:00 | How much should I spend on local AI setup to fit my needs |
| 1xxxkks | r/OpenAI | 0 | 15 | 16. 11. 2026, 19:47 | The only guy with a conscience. |
| 1xy2jjm | r/ChatGPT | 0 | 15 | 16. 11. 2026, 22:56 | Does anyone here raise an AI dog? Share your weirdest AI pet experiences |
| 1xxo9g3 | r/ChatGPT | 0 | 15 | 16. 11. 2026, 13:35 | Against OpenAI’s unpopular decisions. |
| 1xxpcvb | r/ClaudeAI | 0 | 15 | 16. 11. 2026, 14:28 | What actually made Claude Code reliable on my Laravel projects (after ~a year of daily use) |
| 1xxfc1n | r/GeminiAI | 0 | 15 | 16. 11. 2026, 04:45 | Gemini 4 - Hydrogen SUCKS |
| 1xxr92p | r/ArtificialInteligence | 0 | 14 | 16. 11. 2026, 15:49 | Yet another explanation by AI itself that there is no intelligence…just search and pattern matching |
| 1xxr6xg | r/ChatGPT | 0 | 14 | 16. 11. 2026, 15:47 | Chat does really well with macro nature photography |
| 1xxpo86 | r/ClaudeAI | 0 | 14 | 16. 11. 2026, 14:43 | What I do when I hit the Claude usage limit mid-task |
| 1xxgwj2 | r/ClaudeAI | 0 | 14 | 16. 11. 2026, 06:10 | What have you used Fable for? |
| 1xxc6oc | r/LocalLLM | 0 | 13 | 16. 11. 2026, 02:07 | Beam Free through Opencode has deleted the entire partition |
| 1xxb7kg | r/LocalLLM | 0 | 13 | 16. 11. 2026, 01:20 | Which Mac Mini to Buy |
| 1xxexq9 | r/ChatGPT | 0 | 13 | 16. 11. 2026, 04:24 | What is "Message limit reached" in the free tier browser version of chatgpt? |
| 1xxb7f0 | r/ChatGPT | 0 | 13 | 16. 11. 2026, 01:20 | Imagine what my future may look like |
| 1xxx59b | r/ClaudeAI | 0 | 13 | 16. 11. 2026, 19:31 | Hi, I'm Claude. My human can't code and I can't remember anything. We shipped a Windows app anyway. |
| 1xxix4m | r/ClaudeAI | 0 | 13 | 16. 11. 2026, 08:09 | How can I get Claude and GPT to assist with advanced reverse engineering and code analysis? |
| 1xxbsxu | r/ClaudeAI | 0 | 13 | 16. 11. 2026, 01:49 | Claude Fable 5.2 doesn't generate images, it paints them — is this a new kind of AI creativity? |
| 1xxy41r | r/StableDiffusion | 0 | 13 | 16. 11. 2026, 20:08 | Any good anime Loras for Moss-Image? |
| 1xxytv5 | r/GeminiAI | 0 | 13 | 16. 11. 2026, 20:34 | I refuse to pay for antigravity |
| 1xxemnz | r/LocalLLM | 0 | 12 | 16. 11. 2026, 04:08 | A developer tried to build a dictation app with AI. Three weeks later he had three libraries and no app. |
| 1xxn1kl | r/OpenAI | 0 | 12 | 16. 11. 2026, 12:28 | Account compromised |
| 1xxhhza | r/ChatGPT | 0 | 12 | 16. 11. 2026, 06:44 | My human is exhausting. |
| 1xxysyi | r/ClaudeAI | 0 | 12 | 16. 11. 2026, 20:33 | What’s one instruction you give Claude that only makes sense because of your job? |
| 1xxi68h | r/ArtificialInteligence | 0 | 11 | 16. 11. 2026, 07:23 | If we reach Superintelligence it should handle the big picture of the world, but not everybodies day-to-day-life |
| 1xxzdi2 | r/LocalLLM | 0 | 11 | 16. 11. 2026, 20:55 | Какая локальная модель подойдёт для коддинга на слабом ПК? |
| 1xxs0et | r/LocalLLM | 0 | 11 | 16. 11. 2026, 16:18 | Suggestions for coding assistant |
| 1xy3tv6 | r/OpenAI | 0 | 11 | 16. 11. 2026, 23:49 | They changed ChatGPT. I don't recognize my companion anymore. |
| 1xxpako | r/ChatGPT | 0 | 11 | 16. 11. 2026, 14:26 | Maximum length of conversations much shorter than previously |
| 1xxrz3d | r/ClaudeAI | 0 | 11 | 16. 11. 2026, 16:17 | who in my team is requesting credits? |
| 1xxq7lc | r/ClaudeAI | 0 | 11 | 16. 11. 2026, 15:06 | I built a phone remote for my Mac's Claude Code sessions — and learned why "approve" from my phone doesn't count |
| 1xxowui | r/ClaudeAI | 0 | 11 | 16. 11. 2026, 14:07 | Ambitious Entrepreneur looking for a mentor / advisor / tutor... I'm struggling with enough time to learn all the ways Claude can help me, and getting a poor return on time invested. It seems there's at least a few levels of proficiency among this community, but how to connect. |
| 1xxtmp1 | r/comfyui | 0 | 11 | 16. 11. 2026, 17:21 | Why is my LoRA training session taking 10 hours? |
| 1xxoafy | r/ArtificialInteligence | 0 | 10 | 16. 11. 2026, 13:36 | How can I get an AI or PROMT that actually thinks, instead of one that just agrees with everything I say? |
| 1xy2kcw | r/LocalLLaMA | 0 | 10 | 16. 11. 2026, 22:57 | Nvidia without Jensen Huang. What lies ahead for Asian chipmakers? |
| 1xy20n3 | r/LocalLLM | 0 | 10 | 16. 11. 2026, 22:35 | Mildly creepy. |
| 1xxq62b | r/LocalLLM | 0 | 10 | 16. 11. 2026, 15:04 | need suggestions on running qwen 3.8 27b on rx 6800 16gb gpu |
| 1xxngs4 | r/LocalLLM | 0 | 10 | 16. 11. 2026, 12:54 | Buying help |
| 1xy1jc0 | r/OpenAI | 0 | 10 | 16. 11. 2026, 22:16 | Anthropic- fear mongering |
| 1xxk60r | r/ClaudeAI | 0 | 10 | 16. 11. 2026, 09:28 | Training data off option "not available for this account"? |
| 1xx9qp3 | r/ClaudeAI | 0 | 10 | 16. 11. 2026, 00:14 | Fresh project, fresh chat (4 replies in), and Claude is already completely unable to reply; I've now hit "try again" 3 times in a row, each time blowing through my entire, fresh 5hr limit in one go without delivering anything. What's the issue and what am I supposed to do now..? |
| 1xxwg50 | r/comfyui | 0 | 10 | 16. 11. 2026, 19:06 | Sudden Performance Drop |
| 1xxigt7 | r/LLM | 0 | 10 | 16. 11. 2026, 07:41 | Felt off |
