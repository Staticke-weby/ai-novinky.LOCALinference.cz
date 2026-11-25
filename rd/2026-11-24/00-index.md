# AI souhrn z Redditu – 24. listopadu 2026

## Metodika

Data pocházejí z přímého sběru Redditu přes `scripts/rd-collect-web.py` (bez API), pořízeného pro den 24. 11. 2026 v časovém pásmu Europe/Prague. Sběr našel 40 kandidátských postů s balíčky (metadata, selftext, externí článek, komentáře); příloha obsahuje všech 307 postů dne s alespoň 10 komentáři.

Z kandidátů vzniklo **20 článků z 27 postů**. Sedm postů bylo sloučeno do tří článků: čtyři kolem IPO Anthropicu, tři kolem důkazu Riemannovy hypotézy a tři kolem Gemini 4 Argon/Carbon a kvót. Šest postů (pět témat) bylo vyřazeno, protože se stejná událost nebo produkt objevily v některém z posledních tří dnů: meme k závěru Silicon Valley, dva posty k VP ≠ VNP, LeCunova kritika Amodeiho, Claude Ship a Amodeiho poznámka o videohrách. Zbylých sedm kandidátů jsme nepoužili jako málo relevantní, čistě memové nebo duplicitní v rámci dne.

Články jsou řazené podle skóre primárního postu. Tabulka odkazuje na skutečné soubory; příloha ponechává původní anglické titulky a u sloučených postů odkazuje na článek, do kterého byly zařazeny.

## Články

| # | Titulek | Původní titulek (česky) | Skóre | Komentářů |
|---:|---|---|---:|---:|
| 1 | [Anthropic po IPO: akcie padají a komunita žádá Clauda o opravu kurzu](1y47w6b_anthropic-ipo-akcie-padaji.md) | Nezapomeňte si koupit 1 akcii Anthropic | 2148 | 54 |
| 2 | [Fable z jednoho promptu udělalo animaci „Claude se stal Skynetem“](1y4jufl_fable-animace-claude-skynet.md) | Dal jsem Fable tenhle jeden prompt: "Animate: Claude became Skynet" | 844 | 57 |
| 3 | [Alpöge promluvil k důkazu Riemannovy hypotézy. Komunita ho komprimuje](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) | Levent Alpöge prolomil mlčení o Riemannově hypotéze. | 776 | 860 |
| 4 | [Paměť pro milion tokenů spadla ze 130 TB na 890 MB](1y4kikk_pamet-pro-milion-tokenu-130tb-890mb.md) | Jak se paměť pro 1M tokenů smrskla ze 130TB na 890MB | 690 | 66 |
| 5 | [Stavař vyvíjí simulátor stavebních strojů. Kód píše Claude](1y3xeyp_stavar-simulator-unreal-claude.md) | Jsem stavební dělník, ne vývojář. 3 týdny s Claude, ChatGPT a Tripo mě dostaly takhle daleko se stavebním simulátorem | 592 | 60 |
| 6 | [Zaměstnanci OpenAI a Anthropicu: interní modely už nejde bezpečně vydat](1y4hg81_interni-modely-prilis-silne-na-vydani.md) | Zaměstnanci OpenAI a Anthropic nyní tvrdí, že interní modely začínají být příliš silné na to, aby je vůbec vydali | 522 | 468 |
| 7 | [Claude Pro uživatel zkusil Gemini Neon. Nadchl ho, ale brzdí ho kvóty](1y4eddw_gemini-neon-limity-antigravity.md) | Jako uživatel Claude Pro jsem zkusil Gemini Neon... TY BRĎO | 493 | 135 |
| 8 | [Notion MCP dál vkládá reklamu na Business do Claude. I v Gemini](1y4pxfl_notion-mcp-skryta-reklama.md) | 3 měsíce poté, co byl tady pranýřován, oficiální MCP od Notion STÁLE propašovává skryté reklamy na Business do Claude (a říká mu, aby maskoval sledovací odkaz) | 464 | 36 |
| 9 | [Rok od Opus 4.5: model, po kterém lidé přestali psát HTML ručně](1y4coc9_rok-od-opus-4-5.md) | Před rokem | 425 | 40 |
| 10 | [T3 Code čelí obvinění z tajné telemetrie. LocalLLaMA řeší důvěru](1y4atw3_t3-code-telemetrie-drama.md) | Drama kolem T3 Code (čínský příspěvek na X) | 400 | 185 |
| 11 | [Gemini 4 Argon končí. Pro uživatele dostanou Carbon](1y44mo7_gemini-4-argon-konci-carbon.md) | Gemini 4 Argon končí 30. listopadu, zatímco Pro (placení) uživatelé konečně dostanou Gemini 4 Carbon poté, co podle měřítek Google zastaral! | 378 | 41 |
| 12 | [Claude prý přímo napsal váhy transformeru. Řeší Sudoku i Hanoj](1y46vww_claude-napsal-vahy-transformeru.md) | Claude přímo zapsal váhy transformeru, který dokáže řešit testovací bludiště, Sudoku, Hanojskou věž a další se 100% přesností, a překonal všechny modely trénované gradientním sestupem s nižšími náklady a menší velikostí modelu | 342 | 100 |
| 13 | [Agent vysochal masku v Blenderu 32 tisíci tahy. Stálo to 1,48 dolaru](1y4pwnh_ai-socha-blender-32-tisic-tahu.md) | AI sochání je tady: Fable 5.2 udělal 32 139 skutečných tahů štětcem v Blenderu a je to mazec | 318 | 31 |
| 14 | [Slábne ChatGPT schválně? Uživatelé řeší, kde zmizela výkonnost](1y4mte6_chatgpt-slabne-nebo-setri.md) | Zhoršuje OpenAI záměrně ChatGPT, aby přiměl platící předplatitele utrácet víc peněz? Myslím, že tohle musíme vážně prošetřit. | 275 | 141 |
| 15 | [Ternary Bonsai 2.5: 27B agentní model se vejde do 6 GB](1y4mech_ternary-bonsai-2-5-27b-agenti.md) | prism-ml/Ternary-Bonsai-2.5-27B-GGUF · Hugging Face | 272 | 50 |
| 16 | [„16 GB VRAM stačí.“ LocalLLM si dělá legraci z vlastního copingu](1y438r2_16-gb-vram-staci-meme.md) | Jak sám sebe přesvědčuju, že 16GB VRAM stačí na lokální LLM | 268 | 58 |
| 17 | [Songe trénuje lokální model na vašich stopách, když počítač spí](1y3xhrh_songe-lokalni-dotrenovani-ve-spanku.md) | Songe: open-source engine, který doladí váš lokální model na vašich stopách, zatímco váš počítač zahálí | 239 | 72 |
| 18 | [Gemini Neon: empatie je operační systém, ne schopnost](1y4pou8_gemini-neon-empatie-operacni-system.md) | Gemini Neon o empatii | 227 | 177 |
| 19 | [Yang-Mills na torusu: důkaz za méně než tisíc dolarů](1y42p63_yang-mills-dukaz-za-tisic-dolaru.md) | Aktualizace: Nezávislý důkaz existence Yang-Mills od spolupráce MathePhysics | 224 | 31 |
| 20 | [Comfy Desktop 1.2 chce být vstupní branou do ComfyUI](1y3x3im_comfy-desktop-1-2-aplikace.md) | Nový Comfy Desktop se stává vaší vstupní branou ke všemu v ComfyUI | 211 | 97 |

## Příloha: všechny posty dne s ≥ 10 komentáři

| ID | Subreddit | Skóre | Komentářů | Čas | Titulek |
|---|---|---:|---:|---|---|
| 1y4mk3t | r/singularity | 3408 | 251 | 24. 11. 2026, 20:36 | ​ |
| [1y47w6b](1y47w6b_anthropic-ipo-akcie-padaji.md) | r/ClaudeAI | 2148 | 54 | 24. 11. 2026, 09:20 | [Remember to buy 1 share of Anthropic](1y47w6b_anthropic-ipo-akcie-padaji.md) |
| [1y4iana](1y47w6b_anthropic-ipo-akcie-padaji.md) | r/ClaudeAI | 963 | 71 | 24. 11. 2026, 17:52 | [Claude, fix your company's stock price \[Anthropic\]. Make no mistakes.](1y47w6b_anthropic-ipo-akcie-padaji.md) |
| 1y4ll61 | r/singularity | 886 | 94 | 24. 11. 2026, 19:58 | It's just going to get weirder and weirder |
| 1y46npg | r/ArtificialInteligence | 850 | 78 | 24. 11. 2026, 08:03 | btw, Silicon Valley ended with a self-improving AI unexpectedly solving discrete log in polynomial time and breaking encryption. their solution was to destroy the company they spent six seasons to build. |
| [1y4jufl](1y4jufl_fable-animace-claude-skynet.md) | r/ClaudeAI | 844 | 57 | 24. 11. 2026, 18:51 | [i asked fable this one prompt: "Animate: Claude became Skynet"](1y4jufl_fable-animace-claude-skynet.md) |
| [1y40yl0](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) | r/ArtificialInteligence | 776 | 860 | 24. 11. 2026, 03:01 | [Levent Alpöge breaks his silence on the Riemann hypothesis.](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) |
| [1y4kikk](1y4kikk_pamet-pro-milion-tokenu-130tb-890mb.md) | r/LocalLLaMA | 690 | 66 | 24. 11. 2026, 19:16 | [How the memory for 1M tokens shrank from 130TB to 890MB](1y4kikk_pamet-pro-milion-tokenu-130tb-890mb.md) |
| [1y49s8b](1y47w6b_anthropic-ipo-akcie-padaji.md) | r/ArtificialInteligence | 622 | 166 | 24. 11. 2026, 11:20 | [🔥 This is fine 🔥](1y47w6b_anthropic-ipo-akcie-padaji.md) |
| [1y3xeyp](1y3xeyp_stavar-simulator-unreal-claude.md) | r/ClaudeAI | 592 | 60 | 24. 11. 2026, 00:16 | [I'm a construction worker, not a developer. 3 weeks with Claude, ChatGPT and Tripo got me this far on a construction sim](1y3xeyp_stavar-simulator-unreal-claude.md) |
| [1y4hg81](1y4hg81_interni-modely-prilis-silne-na-vydani.md) | r/singularity | 522 | 468 | 24. 11. 2026, 17:19 | [OpenAI And Anthropic Employees Are Now Saying Internal Models Are Becoming Too Powerful To Ever Release](1y4hg81_interni-modely-prilis-silne-na-vydani.md) |
| [1y4eddw](1y4eddw_gemini-neon-limity-antigravity.md) | r/GeminiAI | 493 | 135 | 24. 11. 2026, 15:16 | [As a Claude Pro user who tried Gemini Neon... OH BOY](1y4eddw_gemini-neon-limity-antigravity.md) |
| [1y4q2wj](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) | r/singularity | 468 | 50 | 24. 11. 2026, 22:57 | [Volunteers cut 22.7% of the Riemann Hypothesis Lean proof in one day. Anyone can join](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) |
| [1y4pxfl](1y4pxfl_notion-mcp-skryta-reklama.md) | r/ClaudeAI | 464 | 36 | 24. 11. 2026, 22:50 | [3 months after getting called out here, Notion's official MCP is STILL injecting hidden Business upsells into Claude (and telling it to mask the tracking link)](1y4pxfl_notion-mcp-skryta-reklama.md) |
| [1y455su](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) | r/singularity | 443 | 130 | 24. 11. 2026, 06:36 | [I think Levent Alpoge and Anthropic owe it to the world to publish the full raw transcripts of his sessions with Claude on RH and the other problems they've solved.](1y40yl0_riemannova-hypoteza-alpoge-komprese.md) |
| [1y4coc9](1y4coc9_rok-od-opus-4-5.md) | r/singularity | 425 | 40 | 24. 11. 2026, 13:59 | [One year ago](1y4coc9_rok-od-opus-4-5.md) |
| [1y4atw3](1y4atw3_t3-code-telemetrie-drama.md) | r/LocalLLaMA | 400 | 185 | 24. 11. 2026, 12:21 | [T3 Code drama (Chinese post on X)](1y4atw3_t3-code-telemetrie-drama.md) |
| 1y3y4x6 | r/ClaudeAI | 393 | 100 | 24. 11. 2026, 00:49 | New model incoming? |
| [1y44mo7](1y44mo7_gemini-4-argon-konci-carbon.md) | r/GeminiAI | 378 | 41 | 24. 11. 2026, 06:07 | [Gemini 4 Argon being retired on November 30th, while Pro (Paid) users finally get Gemini 4 Carbon after it became outdated by Google's standards!](1y44mo7_gemini-4-argon-konci-carbon.md) |
| [1y4qacw](1y44mo7_gemini-4-argon-konci-carbon.md) | r/GeminiAI | 372 | 32 | 24. 11. 2026, 23:05 | [Improvements to the antigravity harness and optimizations to Neon’s quota/workload](1y44mo7_gemini-4-argon-konci-carbon.md) |
| 1y44lsn | r/ClaudeAI | 369 | 58 | 24. 11. 2026, 06:05 | Claude AI introduced Claude Ship. Code Review + the PR and Claude Approvals built into Claude Code and the Claude platform |
| 1y3yaxu | r/singularity | 365 | 85 | 24. 11. 2026, 00:56 | Claude proved VP ≠ VNP |
| 1y4qgly | r/singularity | 358 | 41 | 24. 11. 2026, 23:12 | I tried to make the Stochastic Parrot Meme more realistic |
| 1y4a5ph | r/singularity | 355 | 67 | 24. 11. 2026, 11:42 | OpenAI publishes their V != VNP, supposedly obtained on November 6th |
| [1y46vww](1y46vww_claude-napsal-vahy-transformeru.md) | r/artificial | 342 | 100 | 24. 11. 2026, 08:17 | [Claude directly wrote the weights of a transformer that could solve test mazes, Sudoku, Tower of Hanoi, and more with 100% accuracy, beating all models trained with gradient descent at a lower cost and model size](1y46vww_claude-napsal-vahy-transformeru.md) |
| 1y465ey | r/LocalLLaMA | 324 | 89 | 24. 11. 2026, 07:33 | Yann LeCun on Dario's framing of open weight models |
| [1y4pwnh](1y4pwnh_ai-socha-blender-32-tisic-tahu.md) | r/ClaudeAI | 318 | 31 | 24. 11. 2026, 22:49 | [AI Sculpting Is Here: Fable 5.2 Made 32,139 Real Brush Strokes in Blender And This is Sick](1y4pwnh_ai-socha-blender-32-tisic-tahu.md) |
| 1y480ef | r/agi | 303 | 44 | 24. 11. 2026, 09:28 | So he was correct |
| [1y4ldoy](1y47w6b_anthropic-ipo-akcie-padaji.md) | r/ArtificialInteligence | 293 | 22 | 24. 11. 2026, 19:50 | [Brand new sentence](1y47w6b_anthropic-ipo-akcie-padaji.md) |
| [1y4mte6](1y4mte6_chatgpt-slabne-nebo-setri.md) | r/ChatGPT | 275 | 141 | 24. 11. 2026, 20:46 | [Is OpenAI intentionally degrading ChatGPT to push paying subscribers toward spending more money? I think we seriously need to investigate this.](1y4mte6_chatgpt-slabne-nebo-setri.md) |
| 1y46za3 | r/agi | 272 | 171 | 24. 11. 2026, 08:22 | JUST IN: Anthropic CEO Dario Amodei reportedly suggested immersive video games could pacify the masses left jobless by AI, preventing widespread political unrest. |
| [1y4mech](1y4mech_ternary-bonsai-2-5-27b-agenti.md) | r/LocalLLaMA | 272 | 50 | 24. 11. 2026, 20:30 | [prism-ml/Ternary-Bonsai-2.5-27B-GGUF · Hugging Face](1y4mech_ternary-bonsai-2-5-27b-agenti.md) |
| [1y438r2](1y438r2_16-gb-vram-staci-meme.md) | r/LocalLLM | 268 | 58 | 24. 11. 2026, 04:54 | [Me convincing myself that 16gb vram is good enough for local LLMs](1y438r2_16-gb-vram-staci-meme.md) |
| [1y3xhrh](1y3xhrh_songe-lokalni-dotrenovani-ve-spanku.md) | r/LocalLLaMA | 239 | 72 | 24. 11. 2026, 00:20 | [Songe: open-source engine that fine-tunes your local model on your traces while your machine is idle](1y3xhrh_songe-lokalni-dotrenovani-ve-spanku.md) |
| 1y45af5 | r/GeminiAI | 230 | 19 | 24. 11. 2026, 06:43 | Oh it's leaking its own thinking process |
| [1y4pou8](1y4pou8_gemini-neon-empatie-operacni-system.md) | r/singularity | 227 | 177 | 24. 11. 2026, 22:40 | [Gemini Neon on Empathy](1y4pou8_gemini-neon-empatie-operacni-system.md) |
| [1y42p63](1y42p63_yang-mills-dukaz-za-tisic-dolaru.md) | r/singularity | 224 | 31 | 24. 11. 2026, 04:26 | [Update: Independent proof of Yang-Mills Existence by the MathePhysics collaboration](1y42p63_yang-mills-dukaz-za-tisic-dolaru.md) |
| [1y3x3im](1y3x3im_comfy-desktop-1-2-aplikace.md) | r/comfyui | 211 | 97 | 24. 11. 2026, 00:02 | [The New Comfy Desktop becomes your front door to everything ComfyUI](1y3x3im_comfy-desktop-1-2-aplikace.md) |
| 1y4qmr1 | r/singularity | 209 | 12 | 24. 11. 2026, 23:19 | To the person who deliberately made their visualization of the RH proof resemble a nervous system |
| [1y4m3by](1y44mo7_gemini-4-argon-konci-carbon.md) | r/GeminiAI | 207 | 44 | 24. 11. 2026, 20:18 | [Gemini](1y44mo7_gemini-4-argon-konci-carbon.md) |
| 1y49269 | r/OpenAI | 200 | 63 | 24. 11. 2026, 10:35 | ChatGPT gives GPT-5.6 Sol users one month before cutting off access |
| 1y3z6ti | r/artificial | 197 | 59 | 24. 11. 2026, 01:35 | Google's tensor processing units could challenge Nvidia's AI chip monopoly |
| 1y4kxm6 | r/LocalLLaMA | 197 | 23 | 24. 11. 2026, 19:32 | Upcoming Models - Solar-Mini-4.5, MiniCPM5-15B-A2.5B, etc., |
| 1y42wm9 | r/LocalLLaMA | 177 | 73 | 24. 11. 2026, 04:36 | baidu/ERNIE-5.5-Flash-Preview |
| 1y42zz2 | r/ClaudeAI | 175 | 37 | 24. 11. 2026, 04:41 | Claude Fable 5.2 made this animation film in 6 hours (I've never used Blender) |
| 1y4puqo | r/ClaudeAI | 171 | 174 | 24. 11. 2026, 22:47 | I’m lost - what are you doing with Claude |
| 1y4dxn4 | r/LocalLLM | 171 | 59 | 24. 11. 2026, 14:58 | Benchmarked 7 local Qwen3.8 builds (27B dense vs 125B Flash MoE) on 54 real tasks, fully autonomous on a single 5090 . Full report + playable demos attached |
| 1y4eg80 | r/singularity | 171 | 50 | 24. 11. 2026, 15:19 | Modders working with Claude got GTA VI’s Xbox build to render in-game scenes on Windows within a day of the executable leak. |
| 1y400tk | r/ArtificialInteligence | 162 | 290 | 24. 11. 2026, 02:15 | People who will be "useless" in an AI society: how do you deal with it mentally? |
| 1y4et6g | r/ChatGPT | 156 | 125 | 24. 11. 2026, 15:35 | So, I use ChatGPT most of the day for work and personal conversation. I just learnt theyre getting rid of unlimited chat? |
| 1y4qp7i | r/StableDiffusion | 155 | 10 | 24. 11. 2026, 23:22 | RMBG-3.0 is a Fibo 2 fine-tune for background removal and is pretty good even on hard cases |
| 1y4mcd5 | r/ClaudeAI | 152 | 68 | 24. 11. 2026, 20:28 | Opus 4.5 deprecation notice |
| 1y43859 | r/LocalLLaMA | 148 | 21 | 24. 11. 2026, 04:53 | baidu/ERNIE-5.5-Flash-Preview · Hugging Face |
| 1y4gqqy | r/ClaudeAI | 147 | 61 | 24. 11. 2026, 16:52 | Less than a week after its IPO, Anthropic's stock is now over 5% down from its IPO price, or 30% down from its opening peak price. |
| 1y4lp35 | r/StableDiffusion | 145 | 30 | 24. 11. 2026, 20:02 | 2 minute long "selfie style" continuous shot w/ constant location changes & dialogue \[short + tutorial in comments covering quality loss prevention techniques\] |
| 1y4ltvt | r/comfyui | 138 | 21 | 24. 11. 2026, 20:08 | 2 minute "selfie style" continuous shot w/ constant location changes & dialogue \[short + tutorial covering quality loss prevention techniques\] |
| 1y4rhws | r/LocalLLaMA | 138 | 20 | 24. 11. 2026, 23:57 | Inkling Mini's bench scores improved by as much as 10% for FREE by Apple's LoopCD paper |
| 1y46wxs | r/ClaudeAI | 132 | 42 | 24. 11. 2026, 08:18 | Claude directly wrote the weights of a transformer that could solve test mazes, Sudoku, Tower of Hanoi, and more with 100% accuracy all without gradient descent, beating all trained models at a lower cost and model size |
| 1y4ctyc | r/ArtificialInteligence | 124 | 82 | 24. 11. 2026, 14:06 | Ok AIs can solve the Riemann Hypothesis but they still can't... |
| 1y4rj6w | r/ClaudeAI | 124 | 32 | 24. 11. 2026, 23:59 | Anthropic-affiliated economists just dropped their best study yet (IMHO) |
| 1y4jopo | r/ClaudeAI | 120 | 94 | 24. 11. 2026, 18:45 | Is Duet a joke? |
| 1y4gv8k | r/singularity | 119 | 68 | 24. 11. 2026, 16:57 | Tidal is banning fully AI-Generated Music |
| 1y49t8l | r/ArtificialInteligence | 117 | 18 | 24. 11. 2026, 11:21 | The entire year in AI |
| 1y48q6x | r/LocalLLaMA | 116 | 119 | 24. 11. 2026, 10:14 | Will llama.cpp adopt Strata's memory management techniques, or will Strata become the preferred engine for MoE inference? |
| 1y4cxme | r/comfyui | 114 | 27 | 24. 11. 2026, 14:11 | How I kept one AI-generated room consistent across 8 camera angles, with every mistake I made along the way |
| 1y468fg | r/OpenAI | 110 | 53 | 24. 11. 2026, 07:38 | Oh, cool, we’re at the "Supreme Court justices talk casually about AI extinction and mind uploading" stage of AI |
| 1y4lk9h | r/GeminiAI | 109 | 30 | 24. 11. 2026, 19:57 | GEMINI 4 HYDROGEN ROLLED OUT TO JIO-PRO |
| 1y4gpet | r/LocalLLaMA | 105 | 67 | 24. 11. 2026, 16:51 | Neon Should be distilled into the Qwen models for the ultimate brain child! |
| 1y4ncfm | r/StableDiffusion | 102 | 32 | 24. 11. 2026, 21:06 | Juggernaut Moss is out (+ Turbo), and instead of 1girl here's a 1animal showcase :P |
| 1y4osfq | r/singularity | 102 | 20 | 24. 11. 2026, 22:04 | Managed to get Fable 5.2 Medium to weight space program a chess bot to 2730ish Elo |
| 1y4mmbe | r/LocalLLaMA | 100 | 126 | 24. 11. 2026, 20:39 | The administration likes open weight models so they pushed to bring back Jensen?! |
| 1y3yt6u | r/LocalLLaMA | 100 | 17 | 24. 11. 2026, 01:17 | GDN: use replay instead of rollback by am17an · Pull Request #31669 · ggml-org/llama.cpp |
| 1y3zcny | r/GeminiAI | 98 | 14 | 24. 11. 2026, 01:43 | Data collection in paid account is insane |
| 1y420qi | r/singularity | 97 | 11 | 24. 11. 2026, 03:53 | SenseNova U1.6 released. An open-weights 8B image model, and these five come straight from its release samples. |
| 1y493ie | r/GeminiAI | 96 | 54 | 24. 11. 2026, 10:37 | Is it just me or Gemini AI Pro plan limits are just trash? |
| 1y475y7 | r/ChatGPT | 93 | 57 | 24. 11. 2026, 08:34 | I'm a teacher, not a programmer. ChatGPT has let me create educational games for my students, and I'm fucking stoked about it. |
| 1y4f6nq | r/StableDiffusion | 92 | 39 | 24. 11. 2026, 15:50 | SoulX-Singer: A New Model for Local Singing Synthesis and Voice Conversion |
| 1y49n18 | r/ChatGPT | 91 | 62 | 24. 11. 2026, 11:11 | What are some cool/useful things that ChatGPT can do, but may not be super well known? |
| 1y41tfo | r/StableDiffusion | 89 | 12 | 24. 11. 2026, 03:43 | SenseNova released U1.6, an open 8B image model that checks its own output for garbled text and redraws it |
| 1y4jsys | r/OpenAI | 88 | 87 | 24. 11. 2026, 18:50 | Does this means soon we getting a Combined Chat and Work usage ? |
| 1y4qn59 | r/ArtificialInteligence | 88 | 39 | 24. 11. 2026, 23:20 | I don't know what the fuck is going on anymore |
| 1y4p2su | r/ClaudeAI | 74 | 24 | 24. 11. 2026, 22:15 | I'm 49, never made a game before, and just spent 1,000 hours building my own fantasy RPG |
| 1y4l671 | r/LocalLLaMA | 73 | 21 | 24. 11. 2026, 19:42 | KRAFTON/Raon-1-mini · Hugging Face |
| 1y40dte | r/LocalLLM | 72 | 60 | 24. 11. 2026, 02:32 | Inking 2 Mini, the Megathread. |
| 1y4r6au | r/ClaudeAI | 70 | 55 | 24. 11. 2026, 23:43 | $500 in promo credits each week until the end of the year for Claude Duet |
| 1y4fi6v | r/LocalLLaMA | 70 | 18 | 24. 11. 2026, 16:03 | SoulX-Singer: A New Model for Local Singing Synthesis and Voice Conversion |
| 1y4nanw | r/StableDiffusion | 69 | 15 | 24. 11. 2026, 21:05 | RD Flow 64: a from scratch, tiny, open weights pixel art model |
| 1y40d75 | r/LocalLLM | 63 | 43 | 24. 11. 2026, 02:32 | Why not put the KV cache into RAM? Offload to RAM with Qwen 3.8 Flash Next works surprisingly well |
| 1y40lmd | r/ChatGPT | 63 | 25 | 24. 11. 2026, 02:43 | 6.2 guardrailed to the point it's not trustworthy... |
| 1y4lrzn | r/LocalLLM | 62 | 36 | 24. 11. 2026, 20:06 | Easily the best local LLM price-to-performance right now ! |
| 1y47slc | r/deeplearning | 61 | 33 | 24. 11. 2026, 09:14 | I built a neural network from scratch using only NumPy. |
| 1y4h8m3 | r/LocalLLaMA | 59 | 44 | 24. 11. 2026, 17:11 | Inkling 2 Mini on 2× RTX 5070 Ti, 308 tok/s writing code, with the original weights |
| 1y4llsh | r/LocalLLaMA | 59 | 20 | 24. 11. 2026, 19:59 | CCORE Web Designs: 3,500 training samples for web design, presentations and infographics |
| 1y4qtod | r/singularity | 59 | 18 | 24. 11. 2026, 23:28 | The great pirating boycott |
| 1y4kd48 | r/ArtificialInteligence | 55 | 32 | 24. 11. 2026, 19:10 | People who work in AI: What is really going on about safety concerns??? |
| 1y4ip4v | r/singularity | 53 | 66 | 24. 11. 2026, 18:08 | This felt like sci-fi two years ago: a hologram living in my foldable that I can talk to, all on local AI |
| 1y4obgp | r/artificial | 53 | 33 | 24. 11. 2026, 21:45 | Gemini Physical Agents and Embodied Reasoning lead at Google DeepMind confirms DeepMind has achieved RSI |
| 1y4c4xg | r/LocalLLaMA | 52 | 85 | 24. 11. 2026, 13:31 | My Take on Inkling-2-Mini: Loop is the deal breaker! :( |
| 1y4awyo | r/LocalLLaMA | 52 | 12 | 24. 11. 2026, 12:26 | tencent/hy-mt3: machine translation models |
| 1y4i5wd | r/ClaudeAI | 50 | 58 | 24. 11. 2026, 17:47 | I spent 11 weeks with Claude Code building a Balatro bot. It went from 1% to 41% wins, and I have no idea how to get it higher |
| 1y46bf2 | r/ArtificialInteligence | 50 | 24 | 24. 11. 2026, 07:42 | Oh, cool, we’re at the "Supreme Court justices talk casually about AI extinction and mind uploading" stage of AI |
| 1y4dq5l | r/ArtificialInteligence | 49 | 100 | 24. 11. 2026, 14:48 | How far away is China/Huawei from having a competitive chip with Nvidia? |
| 1y4ognv | r/ChatGPT | 49 | 41 | 24. 11. 2026, 21:51 | What happened? |
| 1y4btkm | r/artificial | 49 | 18 | 24. 11. 2026, 13:15 | Trump Posts Bizarre AI Meme of Jensen Huang Holding Up a Bra, Riffing Off 2024 Assassination Attempt on President, After Nvidia Board Reinstates CEO |
| 1y48eje | r/singularity | 48 | 133 | 24. 11. 2026, 09:53 | Who buys the products with high unemployment? |
| 1y4fwqk | r/ArtificialInteligence | 48 | 39 | 24. 11. 2026, 16:19 | "Google might be planning to build a completely AI-generated TV channel in which your likeness is the main character, according to a newly unveiled patent application." -from Gizmodo |
| 1y4g0u9 | r/ChatGPT | 47 | 38 | 24. 11. 2026, 16:24 | 6.2 power is unlocked in chat mode |
| 1y447rr | r/LocalLLM | 46 | 69 | 24. 11. 2026, 05:45 | Whats the advantage of dense models vs MOE? |
| 1y454qs | r/singularity | 45 | 37 | 24. 11. 2026, 06:34 | Can AI independently rediscover Newton's laws of motion and universal gravitation if we restrict its knowledge to everything humanity knew before 1687? |
| 1y454is | r/ArtificialInteligence | 44 | 34 | 24. 11. 2026, 06:34 | Can AI independently rediscover Newton's laws of motion and universal gravitation if we restrict its knowledge to everything humanity knew before 1687? |
| 1y4f7pi | r/GeminiAI | 44 | 11 | 24. 11. 2026, 15:52 | Dont be stupid like me |
| 1y4bh2t | r/ChatGPT | 43 | 34 | 24. 11. 2026, 12:58 | I'm paying OpenAI for frontier intelligence, but its restrictions are making it impossible to do my research |
| 1y3xf53 | r/ChatGPT | 43 | 28 | 24. 11. 2026, 00:16 | Personality Change |
| 1y46qvv | r/ChatGPT | 43 | 22 | 24. 11. 2026, 08:08 | Anyone else noticing a serious drop in quality? |
| 1y4ic4b | r/singularity | 41 | 63 | 24. 11. 2026, 17:54 | Has progress on image generation stalled? |
| 1y46vxe | r/LocalLLaMA | 41 | 25 | 24. 11. 2026, 08:17 | \[GUIDE\] Inkling 2 Mini on a single RTX 5080 16GB + 12GB  RAM: 230 tok/s chat, 450 tok/s structured output, ~9,000 tok/s prompt reads, 240K context (Basalt + 5 open PRs) |
| 1y3xyci | r/LocalLLaMA | 40 | 79 | 24. 11. 2026, 00:40 | Is there a local Model that is good with REA? |
| 1y4313l | r/LocalLLaMA | 39 | 33 | 24. 11. 2026, 04:43 | 2nd Fractal with T4's this time w/112gb vram |
| 1y4iyul | r/ClaudeAI | 38 | 13 | 24. 11. 2026, 18:18 | I made Claude explain code with interactive graphs instead of text |
| 1y4mjhd | r/OpenAI | 36 | 41 | 24. 11. 2026, 20:36 | Astra 6.2 is lazy |
| 1y3zp70 | r/ChatGPT | 36 | 23 | 24. 11. 2026, 01:59 | Now I know what everyone's talking about. Wth is up with GPT now? |
| 1y3x5oi | r/StableDiffusion | 35 | 98 | 24. 11. 2026, 00:05 | The New Comfy Desktop becomes your front door to everything ComfyUI |
| 1y483vx | r/MachineLearning | 33 | 135 | 24. 11. 2026, 09:34 | Arr october 2026 reviews \[R\] |
| 1y4loj0 | r/singularity | 33 | 101 | 24. 11. 2026, 20:02 | Biological immortality doesn’t mean you can’t die |
| 1y4e4t7 | r/ChatGPT | 32 | 100 | 24. 11. 2026, 15:06 | What intellectual tasks can't AI do, that humans can? |
| 1y4mb99 | r/ArtificialInteligence | 32 | 72 | 24. 11. 2026, 20:26 | Accelerate UBI |
| 1y4i7i4 | r/ChatGPT | 32 | 41 | 24. 11. 2026, 17:49 | How is 6.2 chat mode vs 5.6? |
| 1y4b7tc | r/StableDiffusion | 31 | 57 | 24. 11. 2026, 12:43 | Which MiniMax H3 Version are you using or recommending? |
| 1y409ky | r/GeminiAI | 30 | 29 | 24. 11. 2026, 02:27 | The safety filters in Gemini 4 Hydrogen are too strict! |
| 1y4ds2t | r/GeminiAI | 30 | 11 | 24. 11. 2026, 14:51 | It's leaving already?! |
| 1y4ni5a | r/ArtificialInteligence | 28 | 32 | 24. 11. 2026, 21:13 | Jensen Huang says he still doesn’t believe in Nvidia succession planning |
| 1y44e68 | r/StableDiffusion | 28 | 24 | 24. 11. 2026, 05:55 | Minimax H3 ref I2V |
| 1y3x2zk | r/GeminiAI | 27 | 11 | 24. 11. 2026, 00:02 | I was signing up for pro the other day, and it offered me a 6 month free trial, I was so excited. Then all these new models came out, which are locked for me because of the trial and now Flash is leaving? Will I just be locked out of anti gravity? |
| 1y4624c | r/LocalLLM | 26 | 35 | 24. 11. 2026, 07:27 | Is anyone else delegating Claude Code subtasks to local LLMs? Here's my setup and numbers |
| 1y480cn | r/ClaudeAI | 26 | 26 | 24. 11. 2026, 09:28 | Why is Claude so obsessed with relative pronouns at the start of sentences? |
| 1y4h41u | r/ChatGPT | 26 | 25 | 24. 11. 2026, 17:06 | It acted on its own |
| 1y4idr8 | r/ClaudeAI | 25 | 21 | 24. 11. 2026, 17:56 | I wish Claude had a "what changed your mind?  button. |
| 1y4dkx7 | r/ClaudeAI | 25 | 10 | 24. 11. 2026, 14:42 | I built a procedural tropical island you can walk, swim, and fly in the browser |
| 1y45acl | r/LocalLLaMA | 24 | 16 | 24. 11. 2026, 06:43 | Is it time for a benchmark database? |
| 1y420dt | r/GeminiAI | 23 | 36 | 24. 11. 2026, 03:52 | Jio pro bundle |
| 1y4hvqz | r/LocalLLM | 22 | 18 | 24. 11. 2026, 17:36 | I added Inkling 2 Mini support to Pithos: 9.7 tok/s on a GTX 1650 laptop with 4GB VRAM and 16GB RAM |
| 1y4266j | r/LocalLLaMA | 22 | 14 | 24. 11. 2026, 04:00 | Inkling 2 mini on 1x3090: 125 TPS at 100k tok depth, 1700 pp/s, 401K ctx, same KLD as UD-4K XL; 3x faster than stock llama.cpp |
| 1y4dzw6 | r/deeplearning | 22 | 12 | 24. 11. 2026, 15:00 | I made a library that combines your devices' memory to train or fine-tune large models (open source) |
| 1y4a6i7 | r/GeminiAI | 20 | 37 | 24. 11. 2026, 11:44 | Why doesn't Gemini have a feature like Claude Cowork ? |
| 1y4e9n1 | r/ChatGPT | 19 | 40 | 24. 11. 2026, 15:11 | Any updates on the 6.2 situation |
| 1y4gloq | r/ArtificialInteligence | 19 | 28 | 24. 11. 2026, 16:47 | Article in the NY Times, “Looking for the Formula to Avert an Apocalypse” |
| 1y44xov | r/ChatGPT | 16 | 21 | 24. 11. 2026, 06:23 | Dots use cases |
| 1y4f7wi | r/LocalLLaMA | 16 | 20 | 24. 11. 2026, 15:52 | Using an LLM to make corrections in an STT pipeline |
| 1y4az4c | r/agi | 15 | 37 | 24. 11. 2026, 12:30 | Since AI can now apparently solve the Riemann Hypothesis, how close are we to AI making anime girls real? |
| 1y4h3v0 | r/GeminiAI | 15 | 19 | 24. 11. 2026, 17:06 | Neon Usage vs Opus 5.5 |
| 1y4o292 | r/ClaudeAI | 14 | 41 | 24. 11. 2026, 21:35 | How many projects are you running simultaneously? |
| 1y4mqvo | r/LocalLLaMA | 14 | 37 | 24. 11. 2026, 20:44 | Anyone else using Inkling-Mini-2 in Claude Code? |
| 1y3xwoy | r/ClaudeAI | 14 | 23 | 24. 11. 2026, 00:38 | Anyone else spending more time creating than playing with their creations? |
| 1y4aku2 | r/LLMDevs | 14 | 22 | 24. 11. 2026, 12:06 | Prompt rules vs. structural limits for tool-calling agents: what do you enforce outside the prompt? |
| 1y4c5vl | r/GeminiAI | 14 | 15 | 24. 11. 2026, 13:33 | Neon eats tokens too fast even on medium |
| 1y4meur | r/StableDiffusion | 13 | 36 | 24. 11. 2026, 20:30 | Give me Moss-Video or give me death |
| 1y4dfcs | r/artificial | 13 | 20 | 24. 11. 2026, 14:34 | Can AI independently rediscover Newton's laws of motion and universal gravitation if we restrict its knowledge to everything humanity knew before 1687? |
| 1y3zpu3 | r/OpenAI | 13 | 16 | 24. 11. 2026, 02:00 | Now I know what everyone's talking about. Wth is up with GPT now? |
| 1y4jokp | r/LocalLLM | 13 | 12 | 24. 11. 2026, 18:45 | What Have You Made with Small Local Models? |
| 1y4cmxr | r/ArtificialInteligence | 13 | 11 | 24. 11. 2026, 13:57 | Healthcare professionals, how prepared are you for a future where AI is part of everyday clinical practice? |
| 1y4dnpn | r/LocalLLaMA | 12 | 24 | 24. 11. 2026, 14:45 | Radeon AI PRO R9700 Noise Comparison: Gigabyte vs. Sapphire vs. ASUS |
| 1y4hdbj | r/LocalLLaMA | 12 | 17 | 24. 11. 2026, 17:16 | Added the 4th 3090 to my Local AI setup |
| 1y4qlfz | r/singularity | 12 | 16 | 24. 11. 2026, 23:18 | Some AI Lab Employees Support A Pause Because They Don't Want To Automate Themselves Out of a Job |
| 1y42ktv | r/ClaudeAI | 12 | 15 | 24. 11. 2026, 04:20 | Guardrails |
| 1y4odsc | r/artificial | 12 | 13 | 24. 11. 2026, 21:48 | SaaS Apocalypse averted? New Anthropic research suggests many companies don't want the hassle of maintaining their own software. |
| 1y4a68j | r/OpenAI | 11 | 25 | 24. 11. 2026, 11:43 | You would think this would be less of a problem as models get... smarter |
| 1y41vv9 | r/LocalLLM | 11 | 19 | 24. 11. 2026, 03:46 | Have you ever noticed that Qwen3.8-27B curses while it is thinking? |
| 1y4afz2 | r/ChatGPT | 11 | 19 | 24. 11. 2026, 11:59 | Is 6.2 lazy? |
| 1y4iedc | r/agi | 10 | 121 | 24. 11. 2026, 17:56 | So realistically, how long do we have? |
| 1y40ewf | r/LocalLLM | 10 | 49 | 24. 11. 2026, 02:34 | Unsloth builds aren't as good as they say? |
| 1y4kehw | r/ChatGPT | 10 | 44 | 24. 11. 2026, 19:12 | What happened?! |
| 1y4hc4g | r/ChatGPT | 10 | 14 | 24. 11. 2026, 17:15 | Chat not following instructions |
| 1y4ghs5 | r/OpenAI | 10 | 11 | 24. 11. 2026, 16:42 | I think I understand Astra 6.2 |
| 1y424hm | r/LocalLLaMA | 9 | 46 | 24. 11. 2026, 03:58 | 128GB DDR4 RAM + 48GB VRAM; what models bigger than Qwen Flash Next can fit with decent speed (>20t/s), and at what quant? |
| 1y49eno | r/LocalLLaMA | 9 | 45 | 24. 11. 2026, 10:57 | Any dual Xeon users? Is NUMA an issue? |
| 1y4avbz | r/artificial | 9 | 11 | 24. 11. 2026, 12:24 | Who is Levent Alpöge, the reclusive genius behind AI’s math conquest? \| Scientific American |
| 1y456q5 | r/LocalLLaMA | 8 | 21 | 24. 11. 2026, 06:37 | vLLM, 72GB VRAM + 64GB DDR5, Multi User - can we run Q3.8FN? |
| 1y4rhof | r/LocalLLM | 8 | 21 | 24. 11. 2026, 23:57 | Automating corporate agitation with locally hosted LLMs — why should the benefits of automation accrue exclusively to capital? |
| 1y4jbcj | r/StableDiffusion | 8 | 13 | 24. 11. 2026, 18:31 | Minimax H3 Image Blurry Picture |
| 1y47u9i | r/ArtificialInteligence | 8 | 11 | 24. 11. 2026, 09:17 | Any product/project idea? |
| 1y46jcm | r/comfyui | 8 | 11 | 24. 11. 2026, 07:56 | How Do You Like to Create Your Character Sheets? |
| 1y44ns5 | r/LLMDevs | 8 | 11 | 24. 11. 2026, 06:08 | Stuck with 4-8 GB (GPU or server), how do you get real work done? |
| 1y48xyd | r/ArtificialInteligence | 7 | 84 | 24. 11. 2026, 10:28 | Thoughts on NVIDIA reinstating Jensen Huang as the CEO? |
| 1y4o40c | r/LocalLLaMA | 7 | 19 | 24. 11. 2026, 21:37 | Local TTS that speaks with fun character accents, like pirate or cockney gangster. Is that a thing? |
| 1y4b2i6 | r/LocalLLaMA | 7 | 12 | 24. 11. 2026, 12:35 | Local Inference Lab: 3T-Class Kimi K3.1 Pro Locally on PCIe GPUs — 260 tok/s Peak (8× GPUs EXL3, 1.1M KV) & 529 tok/s (16× GPUs MXFP4, 2M KV) |
| 1y4hf74 | r/ChatGPT | 7 | 11 | 24. 11. 2026, 17:18 | Roast My Idea: A Simple Prompt & Skills Manager for AI Beginners |
| 1y4im90 | r/agi | 6 | 17 | 24. 11. 2026, 18:05 | Okor’s Baselisk |
| 1y3x1xr | r/ChatGPT | 6 | 14 | 24. 11. 2026, 00:01 | For those of you who've gotten the chat and work merge: is ChatGPT still conversational? |
| 1y43uwg | r/LocalLLaMA | 6 | 13 | 24. 11. 2026, 05:26 | Seeing less quality on high quants with Basalt |
| 1y4kbd7 | r/ChatGPT | 6 | 11 | 24. 11. 2026, 19:09 | which AI tools have a genuinely useful free plan |
| 1y4r68t | r/ArtificialInteligence | 5 | 51 | 24. 11. 2026, 23:43 | How can people still say AI applications have no moat |
| 1y43req | r/ChatGPT | 5 | 41 | 24. 11. 2026, 05:21 | Does GPT-6.2 feel like a gentleman wearing a mask to anyone else? |
| 1y4e2pv | r/ArtificialInteligence | 5 | 33 | 24. 11. 2026, 15:03 | What intellectual tasks can't AI do, that people can? |
| 1y4g4qt | r/ClaudeAI | 5 | 32 | 24. 11. 2026, 16:28 | $500 per week Duet Usage Credit seems absurdly high. Maybe I'm using it wrong? How are you using Duet? |
| 1y47nzu | r/ArtificialInteligence | 5 | 27 | 24. 11. 2026, 09:06 | Simple question on the Paperclip Problem. |
| 1y4a7ru | r/StableDiffusion | 5 | 27 | 24. 11. 2026, 11:46 | RefMod or Lora |
| 1y4ixe2 | r/LocalLLM | 5 | 24 | 24. 11. 2026, 18:16 | Compact local AI box under $4,300: which 128 GB Strix Halo mini PC would you pick? |
| 1y4hmls | r/GeminiAI | 5 | 21 | 24. 11. 2026, 17:26 | Black Friday Pricing? |
| 1y4j3w1 | r/ClaudeAI | 5 | 20 | 24. 11. 2026, 18:23 | Any prompt to combat harsh copyright policies |
| 1y43k1x | r/LocalLLM | 5 | 15 | 24. 11. 2026, 05:10 | Running HY4 thoughts |
| 1y4butx | r/GeminiAI | 5 | 13 | 24. 11. 2026, 13:17 | Neon 4 vs. Opus for writing & research? |
| 1y47fmf | r/comfyui | 5 | 12 | 24. 11. 2026, 08:51 | Finally getting somewhere with a Trellis2/Pixal3D workflow that will optimise your models along the way. Outputs here are the raw models from a comfy workflow |
| 1y4gb7x | r/ClaudeAI | 5 | 11 | 24. 11. 2026, 16:35 | Has anyone quantified whether the cloud agents have a premium, possibly based on their harness cost? |
| 1y4cur0 | r/ClaudeAI | 4 | 37 | 24. 11. 2026, 14:07 | How do you take ownership of an entirely AI-generated codebase with stale documentation, stale code, and nobody who understands it end-to-end? |
| 1y4njjz | r/GeminiAI | 4 | 33 | 24. 11. 2026, 21:14 | I got 2k+ to spend on AI |
| 1y48e4q | r/ChatGPT | 4 | 30 | 24. 11. 2026, 09:53 | When will chatGPT be able to directly access my PC and attached devices? |
| 1y4iv6i | r/ClaudeAI | 4 | 21 | 24. 11. 2026, 18:14 | Do you let your coding agent touch AWS (or other clouds)? How do you limit it? |
| 1y4lw2q | r/StableDiffusion | 4 | 21 | 24. 11. 2026, 20:10 | If I'm new to Image generation on LocalAI what should I use? I've only used Local LLM not image gen (M5 Max 128GB unified) |
| 1y4g7dm | r/artificial | 4 | 16 | 24. 11. 2026, 16:31 | How 'in danger' is my job in the face of AI? |
| 1y3y8nq | r/ChatGPT | 4 | 16 | 24. 11. 2026, 00:54 | our support bot invented a Black Friday discount |
| 1y46i6e | r/ChatGPT | 4 | 15 | 24. 11. 2026, 07:54 | Why does my AI character's face keep changing every generation? ChatGPT gave me five different women. |
| 1y3ylmc | r/LocalLLaMA | 4 | 13 | 24. 11. 2026, 01:08 | What model/stack is best for content creation? |
| 1y4r6rn | r/ClaudeAI | 4 | 13 | 24. 11. 2026, 23:43 | Which one would suit me better |
| 1y4rebr | r/ChatGPT | 4 | 12 | 24. 11. 2026, 23:53 | Lost access to chat/work switcher (Pro user) |
| 1y48srv | r/ClaudeAI | 4 | 12 | 24. 11. 2026, 10:18 | How to know what model is "enough"? |
| 1y46k0m | r/GeminiAI | 4 | 10 | 24. 11. 2026, 07:57 | I'm stuck on Gemini 3.1 Pro and 4 Argon (Paying Pro user with 74% student discount) |
| 1y462u3 | r/LocalLLaMA | 3 | 32 | 24. 11. 2026, 07:28 | The m3/4 max 128 gb of UrAM or the m5 max 48 gb/64gb or The m5 pro 64 gb ? |
| 1y4bfdw | r/GeminiAI | 3 | 18 | 24. 11. 2026, 12:55 | Is there any way to renew Jio plan ? |
| 1y4qx2n | r/ClaudeAI | 3 | 13 | 24. 11. 2026, 23:32 | How do I get more efficient with Claude? |
| 1y4dyqh | r/ClaudeAI | 3 | 12 | 24. 11. 2026, 14:59 | I built a floating progress widget for Claude Code on Windows with Claude Code (free, open source) |
| 1y4gqjn | r/StableDiffusion | 3 | 11 | 24. 11. 2026, 16:52 | An elf in Paris, made without ComfyUI - H3 image edit + ref2vid |
| 1y4i9a1 | r/singularity | 2 | 29 | 24. 11. 2026, 17:51 | Could something like Lean be used for discovering new theories in physics? |
| 1y4jxs4 | r/ClaudeAI | 2 | 25 | 24. 11. 2026, 18:55 | Tips on making Claude better at reading documents. |
| 1y43y3u | r/ClaudeAI | 2 | 23 | 24. 11. 2026, 05:31 | Does 20$ sub plus additional credits make sense? |
| 1y4dj0n | r/ClaudeAI | 2 | 20 | 24. 11. 2026, 14:39 | What is the actual API dollar value of Claude Pro, Max 5x and Max 20x? |
| 1y4q2kp | r/ClaudeAI | 2 | 15 | 24. 11. 2026, 22:56 | What are people using for a long horizon memory manager? |
| 1y492xd | r/ChatGPT | 2 | 14 | 24. 11. 2026, 10:36 | best Ai subscription for studying? |
| 1y4q6s7 | r/ChatGPT | 2 | 12 | 24. 11. 2026, 23:01 | Our responsibility regarding AI |
| 1y4nm6j | r/ChatGPT | 2 | 12 | 24. 11. 2026, 21:17 | Weird moment with ChatGPT 6.2 |
| 1y4byhr | r/StableDiffusion | 2 | 12 | 24. 11. 2026, 13:22 | Any experience requesting usage licence ? |
| 1y4ast7 | r/ClaudeAI | 2 | 10 | 24. 11. 2026, 12:19 | How to Connect Claude with After Effects Using MCP for Motion Design? |
| 1y45mga | r/ClaudeAI | 2 | 10 | 24. 11. 2026, 07:02 | Building an AI-powered educational publishing pipeline with Claude — looking for advice |
| 1y4ebkc | r/ChatGPT | 1 | 35 | 24. 11. 2026, 15:14 | When you mostly say "yes" to ChatGPT's suggestions, how much of the work is still yours? (Thinking of building a visual skill) |
| 1y4fl6g | r/ChatGPT | 1 | 26 | 24. 11. 2026, 16:07 | Image censorship got worse |
| 1y4g71t | r/StableDiffusion | 1 | 24 | 24. 11. 2026, 16:30 | Are these new filmmaking suits/tools better than just using a simple workflow? |
| 1y4paqi | r/ChatGPT | 1 | 17 | 24. 11. 2026, 22:24 | Help College Student Study Math |
| 1y43nyw | r/LocalLLM | 1 | 16 | 24. 11. 2026, 05:16 | Is it worth running local AI agents on a low-end GPU for personal development? |
| 1y4at2v | r/ClaudeAI | 1 | 16 | 24. 11. 2026, 12:20 | Is Claude Code actually saving us time or just giving us new work? |
| 1y403xc | r/ChatGPT | 1 | 15 | 24. 11. 2026, 02:19 | Anyone know how to choose models in a new chat with on projects on iOS? |
| 1y4emii | r/ClaudeAI | 1 | 15 | 24. 11. 2026, 15:27 | what's actually in your handoff file when you switch from claude to another agent? |
| 1y4ncfw | r/GeminiAI | 1 | 15 | 24. 11. 2026, 21:06 | Bruh |
| 1y4ifcz | r/LocalLLM | 1 | 14 | 24. 11. 2026, 17:57 | how much time and money would it cost to build a niche specific LLM? |
| 1y3z10a | r/ClaudeAI | 1 | 13 | 24. 11. 2026, 01:27 | Is there a Claude powered website builder that lets me move stiff around and position things like squarespace? |
| 1y4efci | r/LLMDevs | 1 | 13 | 24. 11. 2026, 15:18 | \[Free API Access\] NVIDIA Nemotron 3.5 Lightning – 256K Context, vLLM Streaming & 552 TPS Benchmark |
| 1y4igai | r/LLMDevs | 1 | 12 | 24. 11. 2026, 17:58 | how much time and money would it cost to build a niche specific LLM? |
| 1y4162t | r/LocalLLM | 1 | 11 | 24. 11. 2026, 03:11 | "Aesthetic" Local AI Rig? Dual 3090 + 128Gb Z13 Strix Halo |
| 1y3zx3j | r/ArtificialInteligence | 0 | 119 | 24. 11. 2026, 02:09 | We are there. AI is more intelligent than humanity. |
| 1y4fbhm | r/ArtificialInteligence | 0 | 35 | 24. 11. 2026, 15:56 | Do you think Jensen Huang has a political support from Trump ? |
| 1y41rqb | r/LocalLLaMA | 0 | 35 | 24. 11. 2026, 03:41 | What’s your take on Open Weights Lagging behind Closed Models moving forward?( I don’t think so) |
| 1y4be53 | r/singularity | 0 | 34 | 24. 11. 2026, 12:53 | Math student reacts to Riemann news: "after today, math class will become PE class. It’s only a way for kids to exercise their brains, no longer an essential subject to devote your life for cuz "you were making progress for humanity". people’s life’s work is now just ashes in history." |
| 1y4lsb8 | r/LocalLLaMA | 0 | 32 | 24. 11. 2026, 20:06 | What happens tomorrow? |
| 1y48te6 | r/LocalLLaMA | 0 | 32 | 24. 11. 2026, 10:19 | This sub nowadays looks like a party of freeloaders hunting for smart, no-frills bots to help them cut corners at their coding jobs. What happened to "AI enthusiasts"? |
| 1y4eof5 | r/ClaudeAI | 0 | 31 | 24. 11. 2026, 15:29 | 4 apps I connected to Claude, and what my AI employees do in each one |
| 1y4h23j | r/GeminiAI | 0 | 31 | 24. 11. 2026, 17:04 | I absolutely hate Gemini Skills |
| 1y49cie | r/ClaudeAI | 0 | 30 | 24. 11. 2026, 10:53 | Beginner VibeCoder HELP |
| 1y4ipbn | r/artificial | 0 | 29 | 24. 11. 2026, 18:08 | There Is Nothing Right With This Image. There Is Everything Wrong With It. |
| 1y3zuur | r/ClaudeAI | 0 | 29 | 24. 11. 2026, 02:06 | Ugh: building software with Claude / GPT together |
| 1y3xbl4 | r/ClaudeAI | 0 | 29 | 24. 11. 2026, 00:12 | Claude can now review, fix, and approve PRs. I think the interesting question is what it should NEVER approve. |
| 1y4myso | r/GeminiAI | 0 | 29 | 24. 11. 2026, 20:52 | CLAUDE FOR FREE WITH GEMINI PRO? |
| 1y443wq | r/ArtificialInteligence | 0 | 27 | 24. 11. 2026, 05:39 | Should Data Centers be built with a “self-destruct” mechanism? |
| 1y4fxgs | r/LocalLLaMA | 0 | 25 | 24. 11. 2026, 16:20 | PSA: google is actively banning pi.dev gemini connectors |
| 1y40d7w | r/ClaudeAI | 0 | 25 | 24. 11. 2026, 02:32 | Total noob here: what prompts or Project setups do you use with Claude to manage your finances (without linking bank accounts)? |
| 1y49k55 | r/LocalLLM | 0 | 24 | 24. 11. 2026, 11:06 | Did you get paid customers building a local AI client for non technical people that feels like ChatGPT, but with local models (M chip macs only)? |
| 1y4jspx | r/GeminiAI | 0 | 23 | 24. 11. 2026, 18:49 | Google randomly ended my 18 month Jio subscription? |
| 1y4cmbu | r/ClaudeAI | 0 | 22 | 24. 11. 2026, 13:57 | Anthropic, OpenAI staff doubt some internal models can be safely released |
| 1y4bpqo | r/ClaudeAI | 0 | 22 | 24. 11. 2026, 13:09 | Can I automate ALL my social media using just Claude Code? |
| 1y4h4in | r/GeminiAI | 0 | 22 | 24. 11. 2026, 17:07 | FK Gemini!!! |
| 1y481ef | r/singularity | 0 | 21 | 24. 11. 2026, 09:30 | Put down your bets |
| 1y40ofq | r/ArtificialInteligence | 0 | 20 | 24. 11. 2026, 02:47 | concerned |
| 1y48vvc | r/ClaudeAI | 0 | 19 | 24. 11. 2026, 10:24 | Product manager, no coding background: I led a team of Claude agents to build and ship a full iOS, Apple Watch and Android app |
| 1y4695w | r/StableDiffusion | 0 | 19 | 24. 11. 2026, 07:39 | SD3.5-large on one 12 GB consumer card — about 62 seconds, no Python / no CUDA toolkit |
| 1y40xdu | r/comfyui | 0 | 19 | 24. 11. 2026, 03:00 | Nvidia vs AMD GPU |
| 1y4hv1h | r/GeminiAI | 0 | 19 | 24. 11. 2026, 17:35 | The problem is JIO's users |
| 1y4osaw | r/LocalLLaMA | 0 | 18 | 24. 11. 2026, 22:03 | Experience with Hermes + Mac Studio M5 Max, 36GB RAM? |
| 1y4raao | r/GeminiAI | 0 | 18 | 24. 11. 2026, 23:48 | my (jio) pro plan has ended idk why!!! |
| 1y48fzb | r/GeminiAI | 0 | 18 | 24. 11. 2026, 09:56 | Done! |
| 1y4iwuk | r/ChatGPT | 0 | 15 | 24. 11. 2026, 18:16 | please get rid of this so we can roleplay |
| 1y40b09 | r/ChatGPT | 0 | 15 | 24. 11. 2026, 02:29 | Should OpenAi discontinue 6.2 models and keep 5.6 model? |
| 1y4lvbf | r/ClaudeAI | 0 | 15 | 24. 11. 2026, 20:09 | Todoist MCP vs Todoist's official CLI in Claude Code: same day of work, 4.2x fewer tokens with the CLI |
| 1y4gf72 | r/GeminiAI | 0 | 15 | 24. 11. 2026, 16:39 | Jensung hung reportedly disclosed more than 10 affairs to Nvidia board |
| 1y47zf9 | r/LocalLLM | 0 | 14 | 24. 11. 2026, 09:26 | New here: What do you do with local models on 16 gig VRAM |
| 1y45vst | r/ClaudeAI | 0 | 14 | 24. 11. 2026, 07:17 | I asked Claude what it would believe if it were human, then had it write its own scripture. It wrote 13 books where God never answers. |
| 1y45b06 | r/comfyui | 0 | 14 | 24. 11. 2026, 06:44 | How are people creating such realistic AI photo compositions? |
| 1y4l4x7 | r/GeminiAI | 0 | 14 | 24. 11. 2026, 19:41 | Bro what is this joke of a limit?! 😂💀 Rough weekly usage estimate for Gemini 4 Hydrogen on Antigravity because apparently 10k tokens is a whole personality now |
| 1y4i4ri | r/ArtificialInteligence | 0 | 13 | 24. 11. 2026, 17:46 | Future Possibility - AI Blackmail |
| 1y435fu | r/LocalLLaMA | 0 | 13 | 24. 11. 2026, 04:49 | Many states are regulating chatbots. How can one person open-source a free local chat app? |
| 1y4r6rx | r/LocalLLM | 0 | 13 | 24. 11. 2026, 23:43 | Good agentic local coding LLM? |
| 1y46gzi | r/ChatGPT | 0 | 13 | 24. 11. 2026, 07:52 | For the love of all things holy, please stop forcing GPT 6.2 on me! |
| 1y4p9hy | r/ClaudeAI | 0 | 13 | 24. 11. 2026, 22:23 | I run a small marketing agency out of Claude Code. Got to 17 open terminals today, here's how I cleaned it up without losing anything |
| 1y4ahb4 | r/StableDiffusion | 0 | 13 | 24. 11. 2026, 12:01 | How do you build AI character scenes from scratch? |
| 1y4clq4 | r/ChatGPT | 0 | 12 | 24. 11. 2026, 13:56 | 6.2 is out in normal chat!! |
| 1y4isfk | r/ClaudeAI | 0 | 12 | 24. 11. 2026, 18:11 | How has AI coding changed your review workload on production systems? |
| 1y4dhwf | r/ClaudeAI | 0 | 12 | 24. 11. 2026, 14:38 | Gemini API for Claude? |
| 1y4pv8j | r/GeminiAI | 0 | 12 | 24. 11. 2026, 22:48 | Gemini lies on purpose |
| 1y4f9dw | r/ArtificialInteligence | 0 | 11 | 24. 11. 2026, 15:54 | Who is Levent Alpöge, the reclusive genius behind AI’s math conquest? |
| 1y43496 | r/ArtificialInteligence | 0 | 11 | 24. 11. 2026, 04:48 | Why don’t mathematics community enforce the release of chain of prompts? |
| 1y4h496 | r/LocalLLM | 0 | 11 | 24. 11. 2026, 17:06 | Qwen3.8-Flash-Next is (almost) an excellent psychologist |
| 1y3zk3i | r/LocalLLM | 0 | 11 | 24. 11. 2026, 01:52 | Qwen 3.8 Flash humiliates Sonnet 5.5 |
| 1y44s97 | r/OpenAI | 0 | 11 | 24. 11. 2026, 06:15 | Created an app for sensation |
| 1y4lduj | r/ClaudeAI | 0 | 11 | 24. 11. 2026, 19:50 | Claude helped prove Riemann and nobody understands how. Developers are next |
| 1y42ssi | r/ClaudeAI | 0 | 11 | 24. 11. 2026, 04:31 | What do you guys think? |
| 1y410lp | r/ClaudeAI | 0 | 11 | 24. 11. 2026, 03:04 | Hit 100% on Ultra and it’s still going. Thank you Claude, please don't send me a bill for this. |
| 1y4iiz4 | r/GeminiAI | 0 | 11 | 24. 11. 2026, 18:01 | Neon isn't "it" |
| 1y47dof | r/LocalLLaMA | 0 | 10 | 24. 11. 2026, 08:48 | Tested Inkling-2-Mini on a 4090 (24 GB): 8-bit KV + DSpark gets slower than plain 8-bit KV past 64K |
| 1y43efd | r/ChatGPT | 0 | 10 | 24. 11. 2026, 05:02 | How to make GTA 7 using AI on android phone? |
| 1y4kyop | r/ClaudeAI | 0 | 10 | 24. 11. 2026, 19:34 | Best rule I’ve made |
| 1y4aseh | r/ClaudeAI | 0 | 10 | 24. 11. 2026, 12:19 | I knew nothing about radio, so I built a browser SDR app with Claude Code |
