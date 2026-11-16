# AI souhrn z Redditu – 31. 10. 2026

Dvacet článků o AI novinkách, které se za den objevily na Redditu. Vznikly z postů sesbíraných přímo z webu Redditu pro den 31. 10. 2026 (Europe/Prague).

## Metodika

- **Zdroj:** Reddit přímo z webu, sběr provedl `scripts/rd-collect-web.py`. Kandidáti jsou v `_data/candidates.json`, plné balíčky (metadata, selftext, externí článek, komentáře) v `_data/bundles/`.
- **Rozsah:** v denním okně bylo sehráno **317 postů s alespoň 10 komentáři**; všechny jsou v příloze níže. Skóre a počty komentářů jsou živé hodnoty z doby sběru.
- **Výběr:** z **41 kandidátů** vzniklo **20 článků**, které dohromady pokrývají **22 postů**. Tři posty o modelu MiniMax H3 byly sloučeny do jednoho tématu.
- **Vyřazeno:** **17 kandidátů** bylo vynecháno, protože jejich URL, událost nebo produkt se objevily v přehledu posledních tří dnů (`logs/recent-2026-10-31-rd.md`) – šlo zejména o téma Altmanova výroku o RAM, omezování klonování her u Claude, safety guardrails, nové limity OpenAI a přejmenování tarifů Anthropic. Další **2 kandidáti** byli meme bez AI novinky. Vyřazené posty zůstávají v příloze.
- **Příloha:** obsahuje všechny posty dne s ≥ 10 komentáři, v původních anglických titulcích. Odkaz u postu s vlastním článkem míří na soubor článku; u sloučeného postu na článek, kam byl sloučen; u ostatních na původní diskusi na Redditu.

## Články

| Článek | Reddit ID | Skóre | Komentářů |
|---|---|---|---|
| [Cítí se taky ještě někdo trochu nostalgicky po starých video modelech?](1xka3rd_nostalgie-po-starych-videomodelech.md) | 1xka3rd | 2979 | 218 |
| [Kdy bude Fable 5.gguf?](1xjwtrv_fable-5-gguf-unik-vah.md) | 1xjwtrv | 1667 | 379 |
| [Zeptej se svého AI: Na základě našich předchozích konverzací vygeneruj selfie](1xkciy7_ai-selfie-z-historie-chatu.md) | 1xkciy7 | 1003 | 415 |
| [Claude Opus 5.5 umí generovat obrázky, i když nejdřív tvrdí, že to neumí.](1xjxl4s_claude-opus-55-generuje-obrazky.md) | 1xjxl4s | 997 | 167 |
| [Doom z roku 1993, ale s moderní grafikou](1xkgs9l_doom-1993-moderni-grafika.md) | 1xkgs9l | 949 | 164 |
| [Tohle trvalo 12 hodin a nikoho to nezajímá...](1xjv2d9_open-source-video-minimax-h3.md) | 1xjv2d9 | 485 | 187 |
| [Betelgeuse: Qwen 3.8 Flash Next běží stabilně na 22 tok/s (se špičkami 48 tok/s) na RTX 3060 12GB + 16GB DDR4 RAM, 100% bitově přesně!](1xk8s6z_qwen-38-flash-na-rtx-3060.md) | 1xk8s6z | 457 | 116 |
| [Tak moje závislost na lokální AI se dneska večer oficiálně vymkla kontrole.](1xklq96_tri-rtx-3090-domaci-llm-rig.md) | 1xklq96 | 454 | 236 |
| [[Děsivá budoucnost?] Codex mi (schválně) vypnul ComfyUI a odmítl to opravit](1xk38fa_codex-vypnul-comfyui.md) | 1xk38fa | 445 | 268 |
| [Lokální Qwen 27B je na programování prakticky nepoužitelný. Děláme něco špatně?](1xjvc08_lokalni-qwen-27b-kodovani.md) | 1xjvc08 | 431 | 802 |
| [Pokud necháváte Claude Code vyčistit chytrou TV, udělejte nejdřív tohle](1xk8apo_claude-code-chytra-televize.md) | 1xk8apo | 424 | 44 |
| [Na AI se používají skutečné lidské mozkové buňky. Vzrušující doba](1xjwpz8_lidske-mozkove-bunky-videomodel.md) | 1xjwpz8 | 403 | 149 |
| [Už přes rok strávím celý den psaním Markdown specifikace, než zadám prompt Claude. Google právě open-sourcoval „Elephant-Goldfish Model“, který to posouvá 10x dál](1xkn61s_google-elephant-goldfish-model.md) | 1xkn61s | 369 | 63 |
| [Byl Opus 5.5 oslaben? LiveNerf update: Den 38](1xkdxwo_livenerf-opus-55-nerf.md) | 1xkdxwo | 351 | 69 |
| [Nejdřív paměti, úložiště a teď PCB: AI boom spouští masivní nedostatek PCB s objednávkami až do roku 2030, což je velký problém pro výrobce spotřebního hardwaru](1xk17m0_nedostatek-pcb-desek.md) | 1xk17m0 | 273 | 92 |
| [Co se stane, až Čína přestane poskytovat bezplatné open-source modely?](1xkkhq9_az-cina-prestane-open-source.md) | 1xkkhq9 | 261 | 126 |
| [LLM uvnitř LLM – stejný týpek, co dostal RISK-V CPU dovnitř Qwen, teď rozběhl Karpathyho stories260k na NPU zkompilovaném přímo ve vahách Qwen 3.5-4B](1xkiuut_llm-uvnitr-llm-qwenpu.md) | 1xkiuut | 223 | 49 |
| [Opus 5.5 zvládne architektonické výkresy na úrovni začínajícího profesionála](1xkfvvl_opus-55-stavebni-vykresy.md) | 1xkfvvl | 221 | 74 |
| [Použil někdo Claude k vytvoření all-in-one přehledu pro účty za energie, splátky hypotéky a osobní finance? Je bezpečné nahrávat výpisy?](1xkmzet_claude-osobni-finance-dashboard.md) | 1xkmzet | 208 | 117 |
| [Pokud nepoužíváte funkci voice-to-text v ChatGPT, o hodně přicházíte](1xkm5tf_chatgpt-hlas-misto-klavesnice.md) | 1xkm5tf | 172 | 101 |

### Sloučená témata

- [1xk2jhh](1xjv2d9_open-source-video-minimax-h3.md), [1xk4xpd](1xjv2d9_open-source-video-minimax-h3.md) → sloučeno do [1xjv2d9](1xjv2d9_open-source-video-minimax-h3.md)

## Příloha: všechny posty dne (≥ 10 komentářů)

| Reddit ID | Subreddit | Skóre | Komentářů | Čas | Titulek |
|---|---|---|---:|---:|---|---|
| [1xkbenl](https://www.reddit.com/r/ChatGPT/comments/1xkbenl/) | r/ChatGPT | 10068 | 289 | 31. 10. 2026, 15:18 | Poor Sam |
| [1xka3rd](1xka3rd_nostalgie-po-starych-videomodelech.md) | r/StableDiffusion | 2979 | 218 | 31. 10. 2026, 14:22 | Anyone else feeling a little bit nostalgic for old video models? |
| [1xjwtrv](1xjwtrv_fable-5-gguf-unik-vah.md) | r/LocalLLaMA | 1667 | 379 | 31. 10. 2026, 02:00 | Fable 5.gguf when? |
| [1xkg97u](https://www.reddit.com/r/ClaudeAI/comments/1xkg97u/) | r/ClaudeAI | 1548 | 629 | 31. 10. 2026, 18:34 | Security engineer here. The anti-AI hate is getting ridiculous |
| [1xkciy7](1xkciy7_ai-selfie-z-historie-chatu.md) | r/ChatGPT | 1003 | 415 | 31. 10. 2026, 16:04 | Ask your ai : Bese on our privious conversations generate an selfie |
| [1xjxl4s](1xjxl4s_claude-opus-55-generuje-obrazky.md) | r/ClaudeAI | 997 | 167 | 31. 10. 2026, 02:36 | Claude Opus 5.5 can generate images even though it will initially say it can't. |
| [1xkgs9l](1xkgs9l_doom-1993-moderni-grafika.md) | r/ChatGPT | 949 | 164 | 31. 10. 2026, 18:55 | Doom 1993 but with modern graphics |
| [1xkdcto](https://www.reddit.com/r/ClaudeAI/comments/1xkdcto/) | r/ClaudeAI | 841 | 167 | 31. 10. 2026, 16:38 | Anthropic updates Claude to 'steer it away' from letting users clone games following weeks of Steam being inundated with AI slop |
| [1xkn2a1](https://www.reddit.com/r/ChatGPT/comments/1xkn2a1/) | r/ChatGPT | 683 | 392 | 31. 10. 2026, 23:22 | BREAKING: Usage will now be measured in tokens. All chats except instant are metered 😬💀 |
| [1xkar65](https://www.reddit.com/r/LocalLLM/comments/1xkar65/) | r/LocalLLM | 635 | 120 | 31. 10. 2026, 14:50 | Easy RAM trick - take a stick out of your work laptop. |
| [1xkjhng](https://www.reddit.com/r/ChatGPT/comments/1xkjhng/) | r/ChatGPT | 598 | 337 | 31. 10. 2026, 20:45 | Can this man even get more evil? |
| [1xki5qa](https://www.reddit.com/r/ChatGPT/comments/1xki5qa/) | r/ChatGPT | 585 | 61 | 31. 10. 2026, 19:50 | Sam Altman’s comments about RAM really moved me. So I started a GoFundMe for AI. |
| [1xk3p4m](https://www.reddit.com/r/ArtificialInteligence/comments/1xk3p4m/) | r/ArtificialInteligence | 558 | 58 | 31. 10. 2026, 08:15 | Sam Altman wants your ram |
| [1xkbjrz](https://www.reddit.com/r/singularity/comments/1xkbjrz/) | r/singularity | 524 | 78 | 31. 10. 2026, 15:24 | Every time I visit the antiai sub [wall street apes edition] |
| [1xjv2d9](1xjv2d9_open-source-video-minimax-h3.md) | r/comfyui | 485 | 187 | 31. 10. 2026, 00:41 | This took 12 hours to make and nobody cares... |
| [1xk8s6z](1xk8s6z_qwen-38-flash-na-rtx-3060.md) | r/LocalLLaMA | 457 | 116 | 31. 10. 2026, 13:20 | Betelgeuse: Running Qwen 3.8 Flash Next at 22 tok/s sustained (spiking to 48 tok/s) on an RTX 3060 12GB + 16GB DDR4 RAM 100% bit-exact! |
| [1xklq96](1xklq96_tri-rtx-3090-domaci-llm-rig.md) | r/LocalLLaMA | 454 | 236 | 31. 10. 2026, 22:21 | Well, my local AI addiction officially got out of hand tonight. |
| [1xk38fa](1xk38fa_codex-vypnul-comfyui.md) | r/StableDiffusion | 445 | 268 | 31. 10. 2026, 07:47 | [Scary Future?] Codex disabled my ComfyUI (on purpose) and refused to fix it |
| [1xjvc08](1xjvc08_lokalni-qwen-27b-kodovani.md) | r/LocalLLM | 431 | 802 | 31. 10. 2026, 00:54 | Local Qwen 27B is practically unusable for coding tasks. Are we doing something wrong? |
| [1xk8apo](1xk8apo_claude-code-chytra-televize.md) | r/ClaudeAI | 424 | 44 | 31. 10. 2026, 12:56 | If you’re letting Claude Code clean up your smart TV, do these things first |
| [1xjwpz8](1xjwpz8_lidske-mozkove-bunky-videomodel.md) | r/singularity | 403 | 149 | 31. 10. 2026, 01:55 | Real human brains cells being used for AI. Exciting times |
| [1xkavq6](https://www.reddit.com/r/OpenAI/comments/1xkavq6/) | r/OpenAI | 373 | 187 | 31. 10. 2026, 14:56 | Happy Halloween! Make sure to say goodbye to usage! |
| [1xkn61s](1xkn61s_google-elephant-goldfish-model.md) | r/ClaudeAI | 369 | 63 | 31. 10. 2026, 23:27 | For over a year I've spent a full day writing a Markdown spec before prompting Claude. Google just open-sourced the "Elephant-Goldfish Model" that takes this 10x further |
| [1xkdxwo](1xkdxwo_livenerf-opus-55-nerf.md) | r/ClaudeAI | 351 | 69 | 31. 10. 2026, 17:01 | Has Opus 5.5 Been Nerfed? LiveNerf Update: Day 38 |
| [1xk4xpd](1xjv2d9_open-source-video-minimax-h3.md) | r/StableDiffusion | 287 | 44 | 31. 10. 2026, 09:35 | Pika H3 Flex + open-h3-egenerate-2K running locally on Mac |
| [1xk17m0](1xk17m0_nedostatek-pcb-desek.md) | r/LocalLLaMA | 273 | 92 | 31. 10. 2026, 05:45 | First memory, storage, and now PCBsss: AI Boom Triggers Massive PCB Shortage With Orders Booked Until 2030, Posing Big Challenges For Consumer Hardware Vendors |
| [1xkibsh](https://www.reddit.com/r/artificial/comments/1xkibsh/) | r/artificial | 272 | 61 | 31. 10. 2026, 19:57 | Anthropic's Claude AI blocks video game cloning and reverse-engineering — sweeping new restrictions also hit legitimate developers and basic troubleshooting tasks |
| [1xkmzj3](https://www.reddit.com/r/ChatGPT/comments/1xkmzj3/) | r/ChatGPT | 267 | 13 | 31. 10. 2026, 23:19 | Data Center’s are going to look 🔥with all that consumer RAM |
| [1xkkhq9](1xkkhq9_az-cina-prestane-open-source.md) | r/StableDiffusion | 261 | 126 | 31. 10. 2026, 21:26 | What happens once China stops providing free, OSS models? |
| [1xk2mk2](https://www.reddit.com/r/ClaudeAI/comments/1xk2mk2/) | r/ClaudeAI | 252 | 95 | 31. 10. 2026, 07:09 | So we've been getting scammed on 20x? It's only actually been 10x? |
| [1xk0dqk](https://www.reddit.com/r/OpenAI/comments/1xk0dqk/) | r/OpenAI | 252 | 55 | 31. 10. 2026, 04:59 | Paid $20 just to watch them have twice the fun. |
| [1xkiq0a](https://www.reddit.com/r/ChatGPT/comments/1xkiq0a/) | r/ChatGPT | 229 | 104 | 31. 10. 2026, 20:13 | Not a fan of this change? Make your voice heard |
| [1xkiuut](1xkiuut_llm-uvnitr-llm-qwenpu.md) | r/LocalLLaMA | 223 | 49 | 31. 10. 2026, 20:18 | An LLM inside an LLM - Same guy who put a RISK-V CPU inside Qwen has now made Karpathy's stories260k run on an NPU compiled inside Qwen 3.5-4B's weights |
| [1xkhps9](https://www.reddit.com/r/ClaudeAI/comments/1xkhps9/) | r/ClaudeAI | 222 | 53 | 31. 10. 2026, 19:32 | Opus 5.5's safety guardrails are becoming unbearable for legitimate technical work |
| [1xkfvvl](1xkfvvl_opus-55-stavebni-vykresy.md) | r/ClaudeAI | 221 | 74 | 31. 10. 2026, 18:19 | Opus 5.5 Can Do Architectural Drafting at a Junior Professional Level |
| [1xkmzet](1xkmzet_claude-osobni-finance-dashboard.md) | r/ClaudeAI | 208 | 117 | 31. 10. 2026, 23:19 | Has anyone used Claude to build an all-in-one dashboard for utility bills, mortgage payments, and personal finances? Is it safe to upload statements? |
| [1xk2jhh](1xjv2d9_open-source-video-minimax-h3.md) | r/StableDiffusion | 197 | 45 | 31. 10. 2026, 07:03 | MINIMAX H3 4K |
| [1xkkugt](https://www.reddit.com/r/OpenAI/comments/1xkkugt/) | r/OpenAI | 196 | 26 | 31. 10. 2026, 21:41 | Decided to upload a risky pic |
| [1xkm5tf](1xkm5tf_chatgpt-hlas-misto-klavesnice.md) | r/ChatGPT | 172 | 101 | 31. 10. 2026, 22:41 | If you're not using ChatGPT's voice-to-text feature, you're seriously missing out |
| [1xkgrtn](https://www.reddit.com/r/StableDiffusion/comments/1xkgrtn/) | r/StableDiffusion | 166 | 11 | 31. 10. 2026, 18:55 | Oh all the prose and Shakespeare level prompting that I did for generating slops |
| [1xkmuj3](https://www.reddit.com/r/ChatGPT/comments/1xkmuj3/) | r/ChatGPT | 158 | 121 | 31. 10. 2026, 23:12 | Plus users, say bye to unlimited Chat |
| [1xkcyn6](https://www.reddit.com/r/LocalLLaMA/comments/1xkcyn6/) | r/LocalLLaMA | 158 | 94 | 31. 10. 2026, 16:22 | "Spent a lot on my rig but I can only run Gemma 4" |
| [1xjuynv](https://www.reddit.com/r/singularity/comments/1xjuynv/) | r/singularity | 154 | 25 | 31. 10. 2026, 00:37 | The Agentic Economy |
| [1xkibxw](https://www.reddit.com/r/LocalLLaMA/comments/1xkibxw/) | r/LocalLLaMA | 147 | 77 | 31. 10. 2026, 19:57 | CrowdGPT v2.6 - The collaborative LLM |
| [1xk4hjf](https://www.reddit.com/r/ChatGPT/comments/1xk4hjf/) | r/ChatGPT | 142 | 122 | 31. 10. 2026, 09:06 | Chatgpgt now lies openly, instead of processing prompts. How can this happen? |
| [1xjvasi](https://www.reddit.com/r/StableDiffusion/comments/1xjvasi/) | r/StableDiffusion | 142 | 16 | 31. 10. 2026, 00:52 | I made tiny sliders for MiniMax H3 that control motion, emotion, and more without training a LoRA [ComfyUI] |
| [1xkbkzm](https://www.reddit.com/r/agi/comments/1xkbkzm/) | r/agi | 136 | 63 | 31. 10. 2026, 15:25 | I just need to harden the sandboxes |
| [1xjwqf3](https://www.reddit.com/r/singularity/comments/1xjwqf3/) | r/singularity | 135 | 12 | 31. 10. 2026, 01:55 | Astra Beats Every Model in Robot Intelligence |
| [1xkes05](https://www.reddit.com/r/singularity/comments/1xkes05/) | r/singularity | 132 | 45 | 31. 10. 2026, 17:35 | Take with a grain of salt, but could GPT-6.2 be incoming? |
| [1xkebc5](https://www.reddit.com/r/LLMDevs/comments/1xkebc5/) | r/LLMDevs | 132 | 31 | 31. 10. 2026, 17:16 | Google's Open Knowledge Format (OKF), an implementation that addresses real life problems |
| [1xkb7ay](https://www.reddit.com/r/StableDiffusion/comments/1xkb7ay/) | r/StableDiffusion | 131 | 30 | 31. 10. 2026, 15:09 | Ostris is training MOSS Image to use Primal VAE - 4K images with the computational cost of 1080p. |
| [1xkh2ns](https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ns/) | r/LocalLLaMA | 130 | 50 | 31. 10. 2026, 19:06 | Betelgeuse running Qwen 3.8 Flash Next IQ4_XS at 24 tok/s on 2x8GB DDR4 (14 tok/s on a single 16GB stick) + RTX 3060 12GB — 0 dropped experts, 100% byte-exact |
| [1xk23rj](https://www.reddit.com/r/OpenAI/comments/1xk23rj/) | r/OpenAI | 129 | 93 | 31. 10. 2026, 06:37 | Sam Altman on RAM |
| [1xk7nnu](https://www.reddit.com/r/ClaudeAI/comments/1xk7nnu/) | r/ClaudeAI | 127 | 15 | 31. 10. 2026, 12:19 | Experts adopt AI agent's random opinions and think they're their own, Anthropic study finds |
| [1xklwja](https://www.reddit.com/r/ChatGPT/comments/1xklwja/) | r/ChatGPT | 124 | 108 | 31. 10. 2026, 22:29 | Just got this email, this was the major update of the end of 28 days I guess. |
| [1xk6blw](https://www.reddit.com/r/LocalLLaMA/comments/1xk6blw/) | r/LocalLLaMA | 124 | 14 | 31. 10. 2026, 11:02 | microsoft/Mage-VL-Cowork · Hugging Face |
| [1xk9gno](https://www.reddit.com/r/ChatGPT/comments/1xk9gno/) | r/ChatGPT | 118 | 24 | 31. 10. 2026, 13:53 | Tibo, i made you a slider. |
| [1xk3i6w](https://www.reddit.com/r/ChatGPT/comments/1xk3i6w/) | r/ChatGPT | 115 | 38 | 31. 10. 2026, 08:03 | Why my AI is the best friend I have ever had |
| [1xklpe5](https://www.reddit.com/r/singularity/comments/1xklpe5/) | r/singularity | 115 | 35 | 31. 10. 2026, 22:19 | OpenAI is merging Chat and Work in December. Only Instant will be unlimited, and everything else will count toward your Codex limits |
| [1xk6172](https://www.reddit.com/r/ClaudeAI/comments/1xk6172/) | r/ClaudeAI | 113 | 49 | 31. 10. 2026, 10:45 | Burning out but can’t stop |
| [1xjuwdb](https://www.reddit.com/r/LocalLLM/comments/1xjuwdb/) | r/LocalLLM | 107 | 90 | 31. 10. 2026, 00:34 | Mac Studio with 512 RAM just went for sale and they're already delayed until next year |
| [1xkjmb3](https://www.reddit.com/r/singularity/comments/1xkjmb3/) | r/singularity | 107 | 72 | 31. 10. 2026, 20:50 | A lie can travel halfway around the world while the truth is putting on its shoes. |
| [1xkaoy4](https://www.reddit.com/r/LocalLLM/comments/1xkaoy4/) | r/LocalLLM | 107 | 34 | 31. 10. 2026, 14:48 | Watching Chinese rebuild 4090s with 48GB for AI is very satisfying! |
| [1xk2bmn](https://www.reddit.com/r/singularity/comments/1xk2bmn/) | r/singularity | 105 | 536 | 31. 10. 2026, 06:50 | Is UBI unrealistic? |
| [1xkau4g](https://www.reddit.com/r/LocalLLaMA/comments/1xkau4g/) | r/LocalLLaMA | 96 | 33 | 31. 10. 2026, 14:54 | Just finished my humble MoE-Centric Workstation |
| [1xk5s7w](https://www.reddit.com/r/ClaudeAI/comments/1xk5s7w/) | r/ClaudeAI | 95 | 80 | 31. 10. 2026, 10:29 | Is anyone here mourning the loss of “Cowork” |
| [1xkeq7b](https://www.reddit.com/r/ChatGPT/comments/1xkeq7b/) | r/ChatGPT | 94 | 64 | 31. 10. 2026, 17:33 | Combined Work and Chat limits starting with small groups |
| [1xkhkea](https://www.reddit.com/r/comfyui/comments/1xkhkea/) | r/comfyui | 91 | 13 | 31. 10. 2026, 19:26 | Happy Halloween! MiniMax H3 did it again! Music video using my video builder inside ComfyUI. |
| [1xkgzcu](https://www.reddit.com/r/ClaudeAI/comments/1xkgzcu/) | r/ClaudeAI | 84 | 40 | 31. 10. 2026, 19:03 | I built an app where my AI agents delegate to each other and only ask me when they're stuck |
| [1xk2ulc](https://www.reddit.com/r/OpenAI/comments/1xk2ulc/) | r/OpenAI | 83 | 25 | 31. 10. 2026, 07:22 | Tibo: Day 26/ You can now easily switch between multiple accounts on mobile, and coming soon to desktop too. Next two days will be resets… banked… do with this what you may 👀. |
| [1xk5m1s](https://www.reddit.com/r/StableDiffusion/comments/1xk5m1s/) | r/StableDiffusion | 80 | 37 | 31. 10. 2026, 10:18 | Try this workflow, too. |
| [1xkf80p](https://www.reddit.com/r/ChatGPT/comments/1xkf80p/) | r/ChatGPT | 76 | 30 | 31. 10. 2026, 17:53 | ChatGPT Image 3.0 incoming |
| [1xjx0ez](https://www.reddit.com/r/LocalLLaMA/comments/1xjx0ez/) | r/LocalLLaMA | 74 | 38 | 31. 10. 2026, 02:09 | Qwen3.8-Flash-Next on 2x RTX 5090 with 504 tok/s decode: QEngine 1.3.1 decodes ~1.5-1.9x faster than the next-best engine I've tried (numbers, caveats, and what still bites) |
| [1xkbbqi](https://www.reddit.com/r/LocalLLaMA/comments/1xkbbqi/) | r/LocalLLaMA | 73 | 60 | 31. 10. 2026, 15:14 | Is your engine lobotomizing your model? Kinda, and I measured it |
| [1xk3jhw](https://www.reddit.com/r/LocalLLM/comments/1xk3jhw/) | r/LocalLLM | 68 | 18 | 31. 10. 2026, 08:05 | Awesome-selfhosted-ai: Curated list of self-hosted open-source AI: local LLMs, chat UIs, agents, MCP servers, RAG, speech and image generation. Health-checked weekly, dead projects removed automatically. |
| [1xkdgnx](https://www.reddit.com/r/ChatGPT/comments/1xkdgnx/) | r/ChatGPT | 65 | 79 | 31. 10. 2026, 16:42 | AI Isn’t the Problem. Cruel People Are. |
| [1xk7tle](https://www.reddit.com/r/ChatGPT/comments/1xk7tle/) | r/ChatGPT | 64 | 69 | 31. 10. 2026, 12:29 | ADHD friends, what’s your most useful ChatGPT discovery for staying organised? |
| [1xk7hs8](https://www.reddit.com/r/ChatGPT/comments/1xk7hs8/) | r/ChatGPT | 62 | 69 | 31. 10. 2026, 12:11 | Fun things to do with ChatGPT? |
| [1xjvlmf](https://www.reddit.com/r/ChatGPT/comments/1xjvlmf/) | r/ChatGPT | 62 | 20 | 31. 10. 2026, 01:05 | Axl Nose |
| [1xk20x5](https://www.reddit.com/r/LocalLLaMA/comments/1xk20x5/) | r/LocalLLaMA | 59 | 40 | 31. 10. 2026, 06:32 | Lawyer with too many GPUs, part 3: DeepSeek-V4.1-Flash on 2x DGX Spark + an old 3090 box. 2,600+ tok/s prefill to 256K, 322 tok/s structured output, full stack and raw data published |
| [1xjypkq](https://www.reddit.com/r/GeminiAI/comments/1xjypkq/) | r/GeminiAI | 59 | 30 | 31. 10. 2026, 03:32 | if you want to know approximately how long Argon will last on Pro plan while vibecoding in Antigravity |
| [1xkmtyp](https://www.reddit.com/r/artificial/comments/1xkmtyp/) | r/artificial | 56 | 46 | 31. 10. 2026, 23:12 | Dear Sam, My RAM Is None of Your Business. |
| [1xkd1vl](https://www.reddit.com/r/StableDiffusion/comments/1xkd1vl/) | r/StableDiffusion | 54 | 10 | 31. 10. 2026, 16:25 | MiniMax H3 X2 Detail VAE - update, add int8_ConvRot version |
| [1xkef1v](https://www.reddit.com/r/comfyui/comments/1xkef1v/) | r/comfyui | 54 | 10 | 31. 10. 2026, 17:21 | LayerShop update: now with Regions |
| [1xkjw77](https://www.reddit.com/r/OpenAI/comments/1xkjw77/) | r/OpenAI | 52 | 29 | 31. 10. 2026, 21:01 | OpenAl is merging usage allowances |
| [1xk79h5](https://www.reddit.com/r/LocalLLM/comments/1xk79h5/) | r/LocalLLM | 51 | 38 | 31. 10. 2026, 11:58 | This is almost an addiction |
| [1xke54l](https://www.reddit.com/r/GeminiAI/comments/1xke54l/) | r/GeminiAI | 51 | 27 | 31. 10. 2026, 17:09 | I like Gemini's stupidity. |
| [1xk4i8z](https://www.reddit.com/r/ChatGPT/comments/1xk4i8z/) | r/ChatGPT | 51 | 16 | 31. 10. 2026, 09:07 | The ad vs what u get |
| [1xk3n70](https://www.reddit.com/r/StableDiffusion/comments/1xk3n70/) | r/StableDiffusion | 47 | 32 | 31. 10. 2026, 08:12 | I Unlocked BF16 on an RTX 4090 and Compared It to an RTX 5090 (on Windows 11) |
| [1xk71w3](https://www.reddit.com/r/GeminiAI/comments/1xk71w3/) | r/GeminiAI | 47 | 21 | 31. 10. 2026, 11:46 | Switching to ultra as my daily and only |
| [1xkge1s](https://www.reddit.com/r/LocalLLaMA/comments/1xkge1s/) | r/LocalLLaMA | 46 | 30 | 31. 10. 2026, 18:39 | I'm Groot? |
| [1xjyt8c](https://www.reddit.com/r/LocalLLM/comments/1xjyt8c/) | r/LocalLLM | 45 | 15 | 31. 10. 2026, 03:37 | How can i run Capri locally |
| [1xkm2yb](https://www.reddit.com/r/LocalLLaMA/comments/1xkm2yb/) | r/LocalLLaMA | 44 | 44 | 31. 10. 2026, 22:37 | How do I make search with local models feel like ChatGPT / Codex? |
| [1xkjrdl](https://www.reddit.com/r/LocalLLaMA/comments/1xkjrdl/) | r/LocalLLaMA | 43 | 119 | 31. 10. 2026, 20:56 | Please tell me Qwen3.8-Flash-Next can be made to be better than this |
| [1xklfo1](https://www.reddit.com/r/singularity/comments/1xklfo1/) | r/singularity | 43 | 11 | 31. 10. 2026, 22:08 | Meta reportedly building humanoid robot prototype with Chinese startup |
| [1xkak0f](https://www.reddit.com/r/deeplearning/comments/1xkak0f/) | r/deeplearning | 42 | 12 | 31. 10. 2026, 14:42 | Any idea what this is called in research? |
| [1xjx36m](https://www.reddit.com/r/LocalLLaMA/comments/1xjx36m/) | r/LocalLLaMA | 39 | 14 | 31. 10. 2026, 02:12 | The Multidimensional Butterfly Effect: What Cohere Didn't Test on Qwen3.8-Flash-Next |
| [1xk3ca3](https://www.reddit.com/r/GeminiAI/comments/1xk3ca3/) | r/GeminiAI | 38 | 39 | 31. 10. 2026, 07:53 | Gemini 4 Argon in AI Pro |
| [1xk4sum](https://www.reddit.com/r/ClaudeAI/comments/1xk4sum/) | r/ClaudeAI | 37 | 84 | 31. 10. 2026, 09:26 | Hello, Europeans working with (around) the watermark. What have your experience been? |
| [1xkmll9](https://www.reddit.com/r/GeminiAI/comments/1xkmll9/) | r/GeminiAI | 37 | 27 | 31. 10. 2026, 23:01 | Gemini 3.8 Flash (Low vs Med vs High) |
| [1xkeuut](https://www.reddit.com/r/OpenAI/comments/1xkeuut/) | r/OpenAI | 36 | 41 | 31. 10. 2026, 17:38 | With the announcement of Chat and Work merging, now your fun image generation will use up your rate limits. |
| [1xkl6pl](https://www.reddit.com/r/ClaudeAI/comments/1xkl6pl/) | r/ClaudeAI | 35 | 47 | 31. 10. 2026, 21:57 | My industry hasn't been affected by AI at all |
| [1xkncaj](https://www.reddit.com/r/GeminiAI/comments/1xkncaj/) | r/GeminiAI | 33 | 17 | 31. 10. 2026, 23:36 | Which student plan should I go with? |
| [1xjwdr6](https://www.reddit.com/r/ChatGPT/comments/1xjwdr6/) | r/ChatGPT | 31 | 29 | 31. 10. 2026, 01:40 | I have a disability that is very painful and the LLM has spontaneously learned to gauge my pain based on how much worse my typing gets o_o |
| [1xjw1jd](https://www.reddit.com/r/StableDiffusion/comments/1xjw1jd/) | r/StableDiffusion | 31 | 21 | 31. 10. 2026, 01:25 | MOSS Image with  akhaliq's 4-step LoRA and Nvidia PiD   = Super-Fast High-Res (ComfyUI) |
| [1xkcb4h](https://www.reddit.com/r/GeminiAI/comments/1xkcb4h/) | r/GeminiAI | 30 | 16 | 31. 10. 2026, 15:56 | Isn't the limit for argon for the pro a bit too low? 175K tokens is 26.41% of the weekly budget. |
| [1xkmqw1](https://www.reddit.com/r/artificial/comments/1xkmqw1/) | r/artificial | 29 | 39 | 31. 10. 2026, 23:08 | We have access to the most powerful AI in history, yet I sometimes have absolutely no idea what to do with it. Is that a lack of imagination? |
| [1xkcdlz](https://www.reddit.com/r/LocalLLaMA/comments/1xkcdlz/) | r/LocalLLaMA | 28 | 20 | 31. 10. 2026, 15:58 | NVIDIA Nemotron 3.5 Bolt E4B 4GB (post-trained Gemma 4 E4B) |
| [1xjx6fh](https://www.reddit.com/r/agi/comments/1xjx6fh/) | r/agi | 27 | 86 | 31. 10. 2026, 02:16 | (16) I can’t enjoy life with the ever looming threat |
| [1xkak9i](https://www.reddit.com/r/ClaudeAI/comments/1xkak9i/) | r/ClaudeAI | 27 | 55 | 31. 10. 2026, 14:42 | The irony of "Constitutional AI": How Opus 5.5 traded genuine nuance for compulsive contrarianism and a judgmental tone |
| [1xkldof](https://www.reddit.com/r/StableDiffusion/comments/1xkldof/) | r/StableDiffusion | 27 | 32 | 31. 10. 2026, 22:05 | I trained a 1536px Krea 2 LoKr to test wardrobe & character consistency across 10 concert eras — here’s my full breakdown on LoKr vs. LoRA, epochs, and trigger tokens [Workflow Included] |
| [1xkhgrs](https://www.reddit.com/r/StableDiffusion/comments/1xkhgrs/) | r/StableDiffusion | 27 | 13 | 31. 10. 2026, 19:22 | Some older models still punch above their weight |
| [1xk8v0j](https://www.reddit.com/r/singularity/comments/1xk8v0j/) | r/singularity | 27 | 10 | 31. 10. 2026, 13:23 | Binance crypto hack: North Korea suspected to be behind biggest-ever heist \| CNN Business |
| [1xk0n2p](https://www.reddit.com/r/ChatGPT/comments/1xk0n2p/) | r/ChatGPT | 26 | 37 | 31. 10. 2026, 05:13 | OpenAI Needs to Stop Taking Its Paying Customers for Granted |
| [1xk9bf2](https://www.reddit.com/r/StableDiffusion/comments/1xk9bf2/) | r/StableDiffusion | 26 | 11 | 31. 10. 2026, 13:46 | Image Edits: QwenI2.1 comes out on top, but others have use cases |
| [1xkngat](https://www.reddit.com/r/LocalLLaMA/comments/1xkngat/) | r/LocalLLaMA | 25 | 23 | 31. 10. 2026, 23:41 | +1 for Qwen 27Bs character/chat style |
| [1xkfhjg](https://www.reddit.com/r/LocalLLaMA/comments/1xkfhjg/) | r/LocalLLaMA | 23 | 46 | 31. 10. 2026, 18:03 | What's the advantage of building a custom harness over using something like Unsloth? |
| [1xkklyp](https://www.reddit.com/r/LocalLLaMA/comments/1xkklyp/) | r/LocalLLaMA | 23 | 24 | 31. 10. 2026, 21:31 | What exciting architectural moves are we looking to see next in AI models? |
| [1xk05kp](https://www.reddit.com/r/comfyui/comments/1xk05kp/) | r/comfyui | 23 | 13 | 31. 10. 2026, 04:47 | Pika H3 Flexing its muscles |
| [1xkjhtd](https://www.reddit.com/r/StableDiffusion/comments/1xkjhtd/) | r/StableDiffusion | 23 | 12 | 31. 10. 2026, 20:45 | TEM: Transformer Energy-based Models |
| [1xkkglz](https://www.reddit.com/r/LocalLLM/comments/1xkkglz/) | r/LocalLLM | 22 | 36 | 31. 10. 2026, 21:25 | M5 Ultra (96GB) vs M5 Max (128GB) at the same price point |
| [1xkjuxa](https://www.reddit.com/r/StableDiffusion/comments/1xkjuxa/) | r/StableDiffusion | 22 | 15 | 31. 10. 2026, 21:00 | New version of LayerShop now supports regions! |
| [1xjzm9q](https://www.reddit.com/r/LocalLLaMA/comments/1xjzm9q/) | r/LocalLLaMA | 20 | 30 | 31. 10. 2026, 04:19 | Qwen3.8 27b loop testing int4 awq vs int8 |
| [1xklfyy](https://www.reddit.com/r/ArtificialInteligence/comments/1xklfyy/) | r/ArtificialInteligence | 19 | 37 | 31. 10. 2026, 22:08 | How different AIs "chose" a random number |
| [1xjy0uv](https://www.reddit.com/r/LocalLLaMA/comments/1xjy0uv/) | r/LocalLLaMA | 19 | 14 | 31. 10. 2026, 02:58 | A few predictions on Qwen4 HC and Quantization while we wait |
| [1xkl1sr](https://www.reddit.com/r/ClaudeAI/comments/1xkl1sr/) | r/ClaudeAI | 17 | 53 | 31. 10. 2026, 21:51 | What's something you built with Claude that made you FEEL something? |
| [1xkk2o4](https://www.reddit.com/r/OpenAI/comments/1xkk2o4/) | r/OpenAI | 17 | 28 | 31. 10. 2026, 21:09 | December Unified Quota confirmed |
| [1xkgrno](https://www.reddit.com/r/LocalLLM/comments/1xkgrno/) | r/LocalLLM | 17 | 10 | 31. 10. 2026, 18:55 | I wrote a Rust inference engine for Qwen models on a 12 GB GPU, decode is ~1.7x llama.cpp on my RTX3060 |
| [1xjxb8p](https://www.reddit.com/r/OpenAI/comments/1xjxb8p/) | r/OpenAI | 17 | 10 | 31. 10. 2026, 02:22 | I hate to be someone joining the "nerfed?!" posts,  but today |
| [1xjx63n](https://www.reddit.com/r/LocalLLaMA/comments/1xjx63n/) | r/LocalLLaMA | 15 | 14 | 31. 10. 2026, 02:16 | Just "rediscovered" batching and swarming while running models locally. |
| [1xkbt8y](https://www.reddit.com/r/ClaudeAI/comments/1xkbt8y/) | r/ClaudeAI | 15 | 13 | 31. 10. 2026, 15:35 | What is this bots section in this repo ? |
| [1xk9r9z](https://www.reddit.com/r/GeminiAI/comments/1xk9r9z/) | r/GeminiAI | 15 | 12 | 31. 10. 2026, 14:07 | I did the math on Google AGY’s token telemetry (Pro Account): a single "Hi" on Opus 5.5 High burns 10% of your 5h budget, weekly allowances are only ~2x the 5h window, and the 256K context cap eats ~19% in system overhead before you write a single line of code. |
| [1xkgjor](https://www.reddit.com/r/StableDiffusion/comments/1xkgjor/) | r/StableDiffusion | 15 | 10 | 31. 10. 2026, 18:46 | As promised, here is Pai |
| [1xk7ktb](https://www.reddit.com/r/ClaudeAI/comments/1xk7ktb/) | r/ClaudeAI | 14 | 35 | 31. 10. 2026, 12:15 | Do you use code for not coding too? |
| [1xkhzb0](https://www.reddit.com/r/ClaudeAI/comments/1xkhzb0/) | r/ClaudeAI | 14 | 34 | 31. 10. 2026, 19:42 | How to implement Claude into a company |
| [1xk996c](https://www.reddit.com/r/ChatGPT/comments/1xk996c/) | r/ChatGPT | 14 | 24 | 31. 10. 2026, 13:43 | Forgetting EVERYTHING? |
| [1xjuxdb](https://www.reddit.com/r/ChatGPT/comments/1xjuxdb/) | r/ChatGPT | 14 | 23 | 31. 10. 2026, 00:35 | We should all collectively discourage the low quality posts |
| [1xkip46](https://www.reddit.com/r/LocalLLaMA/comments/1xkip46/) | r/LocalLLaMA | 13 | 45 | 31. 10. 2026, 20:12 | Mac Studio M5U 256gb 2TB |
| [1xk0sda](https://www.reddit.com/r/artificial/comments/1xk0sda/) | r/artificial | 13 | 25 | 31. 10. 2026, 05:21 | NYT: 'the lawmakers also signaled that if the Democrats retook the House in elections on Tuesday, the chamber was likely to shift away from its largely hands-off approach to artificial intelligence companies.' |
| [1xjwtra](https://www.reddit.com/r/ChatGPT/comments/1xjwtra/) | r/ChatGPT | 13 | 25 | 31. 10. 2026, 02:00 | Wtf is going wrong? |
| [1xjwpra](https://www.reddit.com/r/LocalLLaMA/comments/1xjwpra/) | r/LocalLLaMA | 13 | 17 | 31. 10. 2026, 01:55 | Just bit the bullet and got a PC and installed llamacpp right away. |
| [1xka09k](https://www.reddit.com/r/comfyui/comments/1xka09k/) | r/comfyui | 13 | 12 | 31. 10. 2026, 14:18 | FastH3 videos getting darker and darker |
| [1xkful0](https://www.reddit.com/r/StableDiffusion/comments/1xkful0/) | r/StableDiffusion | 12 | 60 | 31. 10. 2026, 18:18 | Im noob here and i dont understand why all models use 24 Frame ? What if i change it to 30+ ?will this generate more smooth motion videos ? |
| [1xjv5ck](https://www.reddit.com/r/LocalLLaMA/comments/1xjv5ck/) | r/LocalLLaMA | 12 | 47 | 31. 10. 2026, 00:45 | Regretting cheaping out on my build, what can I actually use? |
| [1xkdpv3](https://www.reddit.com/r/LocalLLaMA/comments/1xkdpv3/) | r/LocalLLaMA | 12 | 37 | 31. 10. 2026, 16:52 | Used 64-core Threadripper PRO 3995WX |
| [1xk67ma](https://www.reddit.com/r/ChatGPT/comments/1xk67ma/) | r/ChatGPT | 12 | 26 | 31. 10. 2026, 10:56 | Prompt to assess you current state of life |
| [1xkkw6n](https://www.reddit.com/r/artificial/comments/1xkkw6n/) | r/artificial | 12 | 12 | 31. 10. 2026, 21:44 | Where the heck is Ilya? |
| [1xjwx04](https://www.reddit.com/r/LocalLLaMA/comments/1xjwx04/) | r/LocalLLaMA | 12 | 12 | 31. 10. 2026, 02:04 | qwen 3.8 27b vs flash next for 32gb vram and 64gb ddr.  BFCL and Livecodebench |
| [1xkiy48](https://www.reddit.com/r/LocalLLM/comments/1xkiy48/) | r/LocalLLM | 12 | 12 | 31. 10. 2026, 20:22 | Are there any tiny models that can do tool calls somewhat consistently? |
| [1xk7gmr](https://www.reddit.com/r/LocalLLaMA/comments/1xk7gmr/) | r/LocalLLaMA | 11 | 28 | 31. 10. 2026, 12:09 | need you opinion on avx2 vs avx512 |
| [1xkjkyx](https://www.reddit.com/r/OpenAI/comments/1xkjkyx/) | r/OpenAI | 11 | 17 | 31. 10. 2026, 20:48 | Chat using codex credits |
| [1xk6yrj](https://www.reddit.com/r/ChatGPT/comments/1xk6yrj/) | r/ChatGPT | 11 | 13 | 31. 10. 2026, 11:41 | Why does my weekly limit sometimes reset during the night? |
| [1xkk605](https://www.reddit.com/r/ChatGPT/comments/1xkk605/) | r/ChatGPT | 11 | 11 | 31. 10. 2026, 21:12 | Did your GPT Image also changed? |
| [1xkir1t](https://www.reddit.com/r/StableDiffusion/comments/1xkir1t/) | r/StableDiffusion | 10 | 31 | 31. 10. 2026, 20:14 | Best Krea 2 checkpoint to use with int8? |
| [1xjzxf7](https://www.reddit.com/r/artificial/comments/1xjzxf7/) | r/artificial | 10 | 26 | 31. 10. 2026, 04:35 | Anthropic high junk investment rating expected as Alphabet sheds $500 billion in value.  Is there a soft landing for AI? |
| [1xkl9x4](https://www.reddit.com/r/ChatGPT/comments/1xkl9x4/) | r/ChatGPT | 10 | 14 | 31. 10. 2026, 22:00 | POV: Your Smart Home Is Powered By ChatGPT |
| [1xk9wrl](https://www.reddit.com/r/LLMDevs/comments/1xk9wrl/) | r/LLMDevs | 10 | 13 | 31. 10. 2026, 14:13 | I built an agent benchmark tool to read how agents actually solve problems, not just the score |
| [1xk97tq](https://www.reddit.com/r/LLMDevs/comments/1xk97tq/) | r/LLMDevs | 10 | 12 | 31. 10. 2026, 13:41 | I built a custom Sliding Window Attention from scratch. Got 4x speedup and 20% VRAM reduction on T4. |
| [1xkcjql](https://www.reddit.com/r/ClaudeAI/comments/1xkcjql/) | r/ClaudeAI | 9 | 38 | 31. 10. 2026, 16:05 | how do you separate Claude API spending between staging and production? |
| [1xk2vhy](https://www.reddit.com/r/ChatGPT/comments/1xk2vhy/) | r/ChatGPT | 9 | 21 | 31. 10. 2026, 07:24 | The scariest thing about AI isn't that it can be wrong. It's that it can be confidently wrong |
| [1xk7pgb](https://www.reddit.com/r/ClaudeAI/comments/1xk7pgb/) | r/ClaudeAI | 9 | 17 | 31. 10. 2026, 12:22 | I'm on the free plan and haiku has been amazing |
| [1xkhcgk](https://www.reddit.com/r/ChatGPT/comments/1xkhcgk/) | r/ChatGPT | 9 | 10 | 31. 10. 2026, 19:17 | Memory management is much worse now. |
| [1xk2quf](https://www.reddit.com/r/LocalLLM/comments/1xk2quf/) | r/LocalLLM | 8 | 30 | 31. 10. 2026, 07:16 | How many of you still do use DeepSeek-V4-Flash-0731 with PolyStrata/Strata or its forks because DeepSeek-V4.1-Flash-1017 is too big? |
| [1xkhe2u](https://www.reddit.com/r/agi/comments/1xkhe2u/) | r/agi | 8 | 29 | 31. 10. 2026, 19:19 | I am an environmentalist and I love AI |
| [1xk564o](https://www.reddit.com/r/ClaudeAI/comments/1xk564o/) | r/ClaudeAI | 8 | 28 | 31. 10. 2026, 09:51 | Solo founder hitting Ultra weekly limits early in the week. What did you do? |
| [1xk760i](https://www.reddit.com/r/ClaudeAI/comments/1xk760i/) | r/ClaudeAI | 8 | 22 | 31. 10. 2026, 11:52 | How to sync development workflow between personal Mac Mini (Claude) and work MacBook (ChatGPT Plus) using GitHub? |
| [1xkbwaz](https://www.reddit.com/r/LocalLLM/comments/1xkbwaz/) | r/LocalLLM | 8 | 18 | 31. 10. 2026, 15:38 | What if we gather all of our conversations with the closed-source AIs like Claude or ChatGPT in one dataset. Then train an LLM on it. |
| [1xjzczl](https://www.reddit.com/r/LocalLLaMA/comments/1xjzczl/) | r/LocalLLaMA | 8 | 13 | 31. 10. 2026, 04:05 | P100 Subreddit |
| [1xkiv82](https://www.reddit.com/r/agi/comments/1xkiv82/) | r/agi | 8 | 13 | 31. 10. 2026, 20:19 | Will an alien civilization invade Earth to gather training data? |
| [1xk6qbw](https://www.reddit.com/r/LocalLLaMA/comments/1xk6qbw/) | r/LocalLLaMA | 8 | 12 | 31. 10. 2026, 11:27 | Fast Model Swapping RAM <-> VRAM (<2s) on a Single 24GB GPU for Multi-Agent Workflows: Has anyone solved the process/CUDA re-init bottleneck? |
| [1xkc2ym](https://www.reddit.com/r/ClaudeAI/comments/1xkc2ym/) | r/ClaudeAI | 8 | 12 | 31. 10. 2026, 15:46 | Claude Code in VS versus Normal Claude? |
| [1xjuotj](https://www.reddit.com/r/LocalLLM/comments/1xjuotj/) | r/LocalLLM | 8 | 11 | 31. 10. 2026, 00:25 | What is the best lightweight-ish coding benchmark to run locally ? |
| [1xjxj3c](https://www.reddit.com/r/ClaudeAI/comments/1xjxj3c/) | r/ClaudeAI | 7 | 41 | 31. 10. 2026, 02:33 | When using Claude to build an app, do you avoid giving it one massive prompt? |
| [1xk5g2d](https://www.reddit.com/r/ArtificialInteligence/comments/1xk5g2d/) | r/ArtificialInteligence | 7 | 30 | 31. 10. 2026, 10:08 | Help me become ai educated. Returning to work after more than a year. |
| [1xkl83k](https://www.reddit.com/r/StableDiffusion/comments/1xkl83k/) | r/StableDiffusion | 7 | 28 | 31. 10. 2026, 21:58 | Just tried z image turbo, and i am genuinely impressed, didnt expect it to work this fast in my laptop |
| [1xk277d](https://www.reddit.com/r/ClaudeAI/comments/1xk277d/) | r/ClaudeAI | 7 | 25 | 31. 10. 2026, 06:42 | How often has a coding agent done something you had to undo? |
| [1xkkjov](https://www.reddit.com/r/LocalLLaMA/comments/1xkkjov/) | r/LocalLLaMA | 7 | 22 | 31. 10. 2026, 21:28 | Strata - QFN GSQ-RCO1 IQ_S3, NVFP4, Unsloth UD-IQ4_XS or Unsloth UD-Q4_K_XL? |
| [1xk7ogz](https://www.reddit.com/r/LocalLLM/comments/1xk7ogz/) | r/LocalLLM | 7 | 17 | 31. 10. 2026, 12:21 | Local Agentic Coding Feasibility |
| [1xk6dh8](https://www.reddit.com/r/StableDiffusion/comments/1xk6dh8/) | r/StableDiffusion | 7 | 17 | 31. 10. 2026, 11:05 | MINIMAX H3: Anybody with a 24gb GPU able to do true 1MP with a 1080p 2nd pass? I'm getting OOM. |
| [1xju6sj](https://www.reddit.com/r/LocalLLaMA/comments/1xju6sj/) | r/LocalLLaMA | 7 | 15 | 31. 10. 2026, 00:03 | Splitting Strata across two devices? |
| [1xjwr43](https://www.reddit.com/r/ChatGPT/comments/1xjwr43/) | r/ChatGPT | 7 | 12 | 31. 10. 2026, 01:56 | What do you guys think of Suno? |
| [1xk8sjt](https://www.reddit.com/r/LocalLLM/comments/1xk8sjt/) | r/LocalLLM | 6 | 28 | 31. 10. 2026, 13:20 | Best GPU upgrade for running DeepSeek V4.1 Flash locally? |
| [1xk8e38](https://www.reddit.com/r/ClaudeAI/comments/1xk8e38/) | r/ClaudeAI | 6 | 27 | 31. 10. 2026, 13:00 | Claude Project Showcase Discussion Hub updated on 31 October 2026 (Sort this by New!) |
| [1xknlam](https://www.reddit.com/r/StableDiffusion/comments/1xknlam/) | r/StableDiffusion | 6 | 19 | 31. 10. 2026, 23:48 | Images with references |
| [1xkizra](https://www.reddit.com/r/ClaudeAI/comments/1xkizra/) | r/ClaudeAI | 6 | 15 | 31. 10. 2026, 20:24 | Week 4 of a puppet show Claude writes, directs and acts: this week it adapted a whole horror story instead of writing sketches |
| [1xkfk8o](https://www.reddit.com/r/LLMDevs/comments/1xkfk8o/) | r/LLMDevs | 6 | 14 | 31. 10. 2026, 18:06 | my claude code agents burned 9.45 million tokens in one day. most of it was them reading my own notes |
| [1xk5t7q](https://www.reddit.com/r/LocalLLM/comments/1xk5t7q/) | r/LocalLLM | 6 | 10 | 31. 10. 2026, 10:30 | Best local AI model for coding and graphic design on RTX 4070 12GB? |
| [1xjvos0](https://www.reddit.com/r/LocalLLaMA/comments/1xjvos0/) | r/LocalLLaMA | 5 | 30 | 31. 10. 2026, 01:08 | Swarm of Multiple Qwen3.8 27b Agents vs Single Qwen3.8 Flash Next Agent? |
| [1xjvsw8](https://www.reddit.com/r/StableDiffusion/comments/1xjvsw8/) | r/StableDiffusion | 5 | 27 | 31. 10. 2026, 01:14 | Krea2 Turbo Fried/Clumpy hair |
| [1xk83u6](https://www.reddit.com/r/LocalLLM/comments/1xk83u6/) | r/LocalLLM | 5 | 26 | 31. 10. 2026, 12:45 | Mac or RTX Pro? |
| [1xkkyuv](https://www.reddit.com/r/LocalLLM/comments/1xkkyuv/) | r/LocalLLM | 5 | 19 | 31. 10. 2026, 21:47 | Dual-CPU inference on old server hardware? |
| [1xk7srs](https://www.reddit.com/r/LocalLLaMA/comments/1xk7srs/) | r/LocalLLaMA | 5 | 17 | 31. 10. 2026, 12:27 | Any progress on continuous learning prompt, will we have meaningful weights plasticity or they'll stay forever frozen? |
| [1xk9rzj](https://www.reddit.com/r/StableDiffusion/comments/1xk9rzj/) | r/StableDiffusion | 5 | 13 | 31. 10. 2026, 14:08 | Minimax H3 - Lacking better REF2V models for broader action and fighting scenes |
| [1xkgsqh](https://www.reddit.com/r/singularity/comments/1xkgsqh/) | r/singularity | 5 | 11 | 31. 10. 2026, 18:56 | The inherent problem with cloud language models |
| [1xk9xep](https://www.reddit.com/r/LocalLLaMA/comments/1xk9xep/) | r/LocalLLaMA | 5 | 10 | 31. 10. 2026, 14:14 | Ran 2,850 decisions through 5 cheap open models voting vs Opus 5.5. Shipped answers were nearly as accurate (89.6% vs 90.5%) at 1/10th the cost |
| [1xjvgrl](https://www.reddit.com/r/ChatGPT/comments/1xjvgrl/) | r/ChatGPT | 5 | 10 | 31. 10. 2026, 01:00 | Issue with image generating |
| [1xk2bst](https://www.reddit.com/r/ClaudeAI/comments/1xk2bst/) | r/ClaudeAI | 4 | 42 | 31. 10. 2026, 06:50 | Where do you go when Claude ultra isn’t enough |
| [1xk4nab](https://www.reddit.com/r/LocalLLaMA/comments/1xk4nab/) | r/LocalLLaMA | 4 | 39 | 31. 10. 2026, 09:16 | I want to try open models, but I can't run anything locally. What are my options? |
| [1xjy973](https://www.reddit.com/r/LocalLLaMA/comments/1xjy973/) | r/LocalLLaMA | 4 | 33 | 31. 10. 2026, 03:09 | Not a smart man, but i think llama.cpp is broken |
| [1xkk4j4](https://www.reddit.com/r/ClaudeAI/comments/1xkk4j4/) | r/ClaudeAI | 4 | 26 | 31. 10. 2026, 21:11 | Any electrical , mechanical , aerospace engineers here who are using claude for their work ? |
| [1xk8key](https://www.reddit.com/r/OpenAI/comments/1xk8key/) | r/OpenAI | 4 | 17 | 31. 10. 2026, 13:09 | The new API credits make ChatGPT Pro a no-brainer for API users |
| [1xk1oaz](https://www.reddit.com/r/ClaudeAI/comments/1xk1oaz/) | r/ClaudeAI | 4 | 17 | 31. 10. 2026, 06:11 | How can I run Claude Code in my mobile |
| [1xkb2tt](https://www.reddit.com/r/artificial/comments/1xkb2tt/) | r/artificial | 4 | 16 | 31. 10. 2026, 15:04 | Can a swarm resist being shut down without ever feeling alive? |
| [1xjxbfl](https://www.reddit.com/r/LocalLLM/comments/1xjxbfl/) | r/LocalLLM | 4 | 15 | 31. 10. 2026, 02:23 | What's the most capable model I can run locally on Powerspec G913? |
| [1xk19y3](https://www.reddit.com/r/ArtificialInteligence/comments/1xk19y3/) | r/ArtificialInteligence | 4 | 13 | 31. 10. 2026, 05:48 | AI Ethics, Sustainability, and the Decentralization of Power |
| [1xk8w6l](https://www.reddit.com/r/ClaudeAI/comments/1xk8w6l/) | r/ClaudeAI | 4 | 12 | 31. 10. 2026, 13:25 | I just trying implement protection against reverse engineering and hacking, but... |
| [1xknbji](https://www.reddit.com/r/artificial/comments/1xknbji/) | r/artificial | 4 | 10 | 31. 10. 2026, 23:35 | Really impressed with AI language translation |
| [1xkg7ok](https://www.reddit.com/r/ChatGPT/comments/1xkg7ok/) | r/ChatGPT | 4 | 10 | 31. 10. 2026, 18:32 | Astra-6 stopping before the task is done. |
| [1xkd8ri](https://www.reddit.com/r/ClaudeAI/comments/1xkd8ri/) | r/ClaudeAI | 3 | 35 | 31. 10. 2026, 16:33 | Crazy good product |
| [1xkee2n](https://www.reddit.com/r/LocalLLM/comments/1xkee2n/) | r/LocalLLM | 3 | 21 | 31. 10. 2026, 17:19 | I kept seeing “my local model is useless as a coding agent” posts, and I had the same problem, so I built an agent around local models. Looking for testers (WIP) |
| [1xk4dax](https://www.reddit.com/r/ClaudeAI/comments/1xk4dax/) | r/ClaudeAI | 3 | 21 | 31. 10. 2026, 08:59 | Curious how everyone is using Claude Code right now: CLI or Desktop? |
| [1xkguyh](https://www.reddit.com/r/ArtificialInteligence/comments/1xkguyh/) | r/ArtificialInteligence | 3 | 18 | 31. 10. 2026, 18:58 | Has someone tried local LLMs for coding? |
| [1xkjs05](https://www.reddit.com/r/ChatGPT/comments/1xkjs05/) | r/ChatGPT | 3 | 18 | 31. 10. 2026, 20:57 | December Unified Quota - Screenshot on Arabic Page |
| [1xk8d57](https://www.reddit.com/r/StableDiffusion/comments/1xk8d57/) | r/StableDiffusion | 3 | 17 | 31. 10. 2026, 12:59 | How to achieve glossy, ultra-realistic skin with Krea 2 Raw in ComfyUI? |
| [1xjx6oi](https://www.reddit.com/r/artificial/comments/1xjx6oi/) | r/artificial | 3 | 16 | 31. 10. 2026, 02:16 | Fewer tokens? Anyone else noticing the big dogs’ AI efficiency push? |
| [1xjzrxb](https://www.reddit.com/r/ArtificialInteligence/comments/1xjzrxb/) | r/ArtificialInteligence | 3 | 16 | 31. 10. 2026, 04:27 | How my AI prompt used my state's insurance regulatory filings to help me understand what influences my insurance premiums |
| [1xki284](https://www.reddit.com/r/LocalLLaMA/comments/1xki284/) | r/LocalLLaMA | 3 | 16 | 31. 10. 2026, 19:46 | Qwen3.8 flash next on igpu? Anybody achieve it? |
| [1xk7pwy](https://www.reddit.com/r/ChatGPT/comments/1xk7pwy/) | r/ChatGPT | 3 | 16 | 31. 10. 2026, 12:23 | Is it possible that everyone owns AI hardware and share it to the cloud instead? |
| [1xk5m76](https://www.reddit.com/r/ClaudeAI/comments/1xk5m76/) | r/ClaudeAI | 3 | 15 | 31. 10. 2026, 10:18 | When do you hand a task to Claude Code instead of Codex — and what in the brief makes the difference? |
| [1xk4oz0](https://www.reddit.com/r/artificial/comments/1xk4oz0/) | r/artificial | 3 | 14 | 31. 10. 2026, 09:19 | Using AI for Both Professional Work and Law School |
| [1xkbl77](https://www.reddit.com/r/LocalLLM/comments/1xkbl77/) | r/LocalLLM | 3 | 14 | 31. 10. 2026, 15:25 | 32 GB DDR 5 ram + 5080 16GB VRAM + Strata QFN IQ2_XS |
| [1xjyf7z](https://www.reddit.com/r/ClaudeAI/comments/1xjyf7z/) | r/ClaudeAI | 3 | 12 | 31. 10. 2026, 03:17 | What web/WordPress backend work should I not outsource to Claude Code? |
| [1xk0y96](https://www.reddit.com/r/LocalLLM/comments/1xk0y96/) | r/LocalLLM | 3 | 10 | 31. 10. 2026, 05:30 | LM Studio, is it normal for it to not utilize all my VRAM? (Settings in pictures) |
| [1xk00vw](https://www.reddit.com/r/ClaudeAI/comments/1xk00vw/) | r/ClaudeAI | 2 | 101 | 31. 10. 2026, 04:40 | If Anthropic announced no more usage limits starting tomorrow, what’s the first things you’d build? |
| [1xkc99i](https://www.reddit.com/r/ChatGPT/comments/1xkc99i/) | r/ChatGPT | 2 | 71 | 31. 10. 2026, 15:53 | What's your favorite use of AI? and why? |
| [1xk3d0f](https://www.reddit.com/r/LocalLLaMA/comments/1xk3d0f/) | r/LocalLLaMA | 2 | 24 | 31. 10. 2026, 07:55 | light weight model to execute task while having a larger (more intelligent model to plan) |
| [1xk56mq](https://www.reddit.com/r/LocalLLM/comments/1xk56mq/) | r/LocalLLM | 2 | 21 | 31. 10. 2026, 09:52 | Which cloud computer to run an obliterated local computer |
| [1xk6190](https://www.reddit.com/r/LocalLLM/comments/1xk6190/) | r/LocalLLM | 2 | 15 | 31. 10. 2026, 10:45 | how do install an harness for my local AI? |
| [1xkfkfx](https://www.reddit.com/r/StableDiffusion/comments/1xkfkfx/) | r/StableDiffusion | 2 | 14 | 31. 10. 2026, 18:07 | Actually good edit models / workflows for anime? |
| [1xklme7](https://www.reddit.com/r/LocalLLM/comments/1xklme7/) | r/LocalLLM | 2 | 12 | 31. 10. 2026, 22:16 | Best Motherboard & PSU for Dual RTX 3090 LLM Rig for DDR4? |
| [1xk409t](https://www.reddit.com/r/LocalLLM/comments/1xk409t/) | r/LocalLLM | 2 | 12 | 31. 10. 2026, 08:34 | 5070 Ti 16GB + 32GB RAM: best models for Hermes, uncensored testing, and ComfyUI video? |
| [1xkl29j](https://www.reddit.com/r/ClaudeAI/comments/1xkl29j/) | r/ClaudeAI | 2 | 10 | 31. 10. 2026, 21:51 | Move from Cowork To Code? |
| [1xk0ta3](https://www.reddit.com/r/OpenAI/comments/1xk0ta3/) | r/OpenAI | 1 | 53 | 31. 10. 2026, 05:22 | NYT: 'the lawmakers also signaled that if the Democrats retook the House in elections on Tuesday, the chamber was likely to shift away from its largely hands-off approach to artificial intelligence companies.' |
| [1xkg0du](https://www.reddit.com/r/singularity/comments/1xkg0du/) | r/singularity | 1 | 44 | 31. 10. 2026, 18:24 | With a smarter than human AI, it won't wage war on humanity |
| [1xkaj57](https://www.reddit.com/r/LocalLLM/comments/1xkaj57/) | r/LocalLLM | 1 | 26 | 31. 10. 2026, 14:41 | Incredibly Frustrated New Local LLM User… Help? |
| [1xk3yn3](https://www.reddit.com/r/ClaudeAI/comments/1xk3yn3/) | r/ClaudeAI | 1 | 21 | 31. 10. 2026, 08:32 | Honestly this has been cracking me up |
| [1xjz393](https://www.reddit.com/r/ClaudeAI/comments/1xjz393/) | r/ClaudeAI | 1 | 19 | 31. 10. 2026, 03:52 | Is it possible for someone using Claude to overcome the issues preventing the MacPro 2,1 from upgrading past El Capitan? |
| [1xkb441](https://www.reddit.com/r/LLMDevs/comments/1xkb441/) | r/LLMDevs | 1 | 18 | 31. 10. 2026, 15:05 | Best PDF parser / OCR for extracting structured data from invoices – What works in production? |
| [1xk332w](https://www.reddit.com/r/ChatGPT/comments/1xk332w/) | r/ChatGPT | 1 | 16 | 31. 10. 2026, 07:37 | Chatgpt classic app will be discontinued on January 30th, 2027. |
| [1xkma9c](https://www.reddit.com/r/GeminiAI/comments/1xkma9c/) | r/GeminiAI | 1 | 15 | 31. 10. 2026, 22:47 | Gemini Flash 3.8 acting like GPT 5.2 |
| [1xk0i5x](https://www.reddit.com/r/ClaudeAI/comments/1xk0i5x/) | r/ClaudeAI | 1 | 14 | 31. 10. 2026, 05:05 | Best harness for maximum throughput/productivity? |
| [1xkayls](https://www.reddit.com/r/LocalLLaMA/comments/1xkayls/) | r/LocalLLaMA | 1 | 12 | 31. 10. 2026, 14:59 | Right now you can get an RTX 6000 Pro Workstation For 12k from Dell (edit: not anymore) |
| [1xk423y](https://www.reddit.com/r/ChatGPT/comments/1xk423y/) | r/ChatGPT | 1 | 12 | 31. 10. 2026, 08:38 | Do you ever try to integrate AI into your systems, and then realise the old way worked perfectly well? |
| [1xkl0zn](https://www.reddit.com/r/ClaudeAI/comments/1xkl0zn/) | r/ClaudeAI | 1 | 12 | 31. 10. 2026, 21:49 | GPT-6 Astra burned most of my weekly usage looping on a bug. Opus found it in minutes. |
| [1xkb2sr](https://www.reddit.com/r/LocalLLM/comments/1xkb2sr/) | r/LocalLLM | 1 | 10 | 31. 10. 2026, 15:04 | Hey guys, complete newbie here asking for some advice. Any tips for a beginner? |
| [1xk3u6x](https://www.reddit.com/r/LocalLLM/comments/1xk3u6x/) | r/LocalLLM | 1 | 10 | 31. 10. 2026, 08:24 | Computer use for local AI? |
| [1xk2ejz](https://www.reddit.com/r/OpenAI/comments/1xk2ejz/) | r/OpenAI | 1 | 10 | 31. 10. 2026, 06:55 | Is it even the correct comparison to compare API costs with subscription costs? |
| [1xk0swa](https://www.reddit.com/r/ChatGPT/comments/1xk0swa/) | r/ChatGPT | 0 | 71 | 31. 10. 2026, 05:22 | NYT: 'the lawmakers also signaled that if the Democrats retook the House in elections on Tuesday, the chamber was likely to shift away from its largely hands-off approach to artificial intelligence companies.' |
| [1xkd40z](https://www.reddit.com/r/ClaudeAI/comments/1xkd40z/) | r/ClaudeAI | 0 | 65 | 31. 10. 2026, 16:28 | With no coding experience, I used Claude to build a commercially viable consumer app. It's taken about 10 months to build and set up with Claude and Claude Code - did I do good? |
| [1xkdh1p](https://www.reddit.com/r/OpenAI/comments/1xkdh1p/) | r/OpenAI | 0 | 64 | 31. 10. 2026, 16:42 | Claude won. Face it. |
| [1xkcnn2](https://www.reddit.com/r/ArtificialInteligence/comments/1xkcnn2/) | r/ArtificialInteligence | 0 | 60 | 31. 10. 2026, 16:09 | AI stocks are selling off. If the bubble pops, what happens to the technology itself? |
| [1xjxun0](https://www.reddit.com/r/ClaudeAI/comments/1xjxun0/) | r/ClaudeAI | 0 | 55 | 31. 10. 2026, 02:49 | HELP?! I have 40% of my plan left and it resets TOMORROW?! |
| [1xkieqt](https://www.reddit.com/r/LocalLLaMA/comments/1xkieqt/) | r/LocalLLaMA | 0 | 45 | 31. 10. 2026, 20:00 | What did I miss? What should I be running on 2x16Gb VRAM and 128Gb RAM? |
| [1xjxf1l](https://www.reddit.com/r/ClaudeAI/comments/1xjxf1l/) | r/ClaudeAI | 0 | 36 | 31. 10. 2026, 02:28 | 20 years ago I wrote a book I never finished... Claude helped me finish it, publish it, and build a 3D world from it! |
| [1xkf2uq](https://www.reddit.com/r/LocalLLaMA/comments/1xkf2uq/) | r/LocalLLaMA | 0 | 32 | 31. 10. 2026, 17:47 | Children’s AI perspective |
| [1xk7qz3](https://www.reddit.com/r/OpenAI/comments/1xk7qz3/) | r/OpenAI | 0 | 31 | 31. 10. 2026, 12:25 | Would OpenAI have done better than Anthropic had Sam Altman gracefully left the company? |
| [1xkjlwc](https://www.reddit.com/r/LocalLLM/comments/1xkjlwc/) | r/LocalLLM | 0 | 30 | 31. 10. 2026, 20:49 | Qwen 3.8 flash next is a pipe dream |
| [1xk8cgm](https://www.reddit.com/r/ClaudeAI/comments/1xk8cgm/) | r/ClaudeAI | 0 | 30 | 31. 10. 2026, 12:58 | Claude’s new subscription option is just too cool! |
| [1xk152p](https://www.reddit.com/r/ClaudeAI/comments/1xk152p/) | r/ClaudeAI | 0 | 30 | 31. 10. 2026, 05:41 | How to deploy app from Claude for iOS & Android? |
| [1xkljk8](https://www.reddit.com/r/LocalLLaMA/comments/1xkljk8/) | r/LocalLLaMA | 0 | 28 | 31. 10. 2026, 22:12 | How many t/s would you live with to run Fable/Carbon/Astra/etc locally? And what cliff? |
| [1xke87l](https://www.reddit.com/r/ClaudeAI/comments/1xke87l/) | r/ClaudeAI | 0 | 27 | 31. 10. 2026, 17:13 | Is the Claude Max subscription actually worth paying extra for, or are the Pro limits enough? |
| [1xkjlgu](https://www.reddit.com/r/ChatGPT/comments/1xkjlgu/) | r/ChatGPT | 0 | 25 | 31. 10. 2026, 20:49 | How to avoid textgrain ? |
| [1xk0he0](https://www.reddit.com/r/ChatGPT/comments/1xk0he0/) | r/ChatGPT | 0 | 25 | 31. 10. 2026, 05:04 | I asked ChatGPT What is the most possibly unsettling thing you’ve been holding back? |
| [1xk8ius](https://www.reddit.com/r/ClaudeAI/comments/1xk8ius/) | r/ClaudeAI | 0 | 25 | 31. 10. 2026, 13:07 | Do you lock down network, secrets or PII for your agents, or do they have access to everything? |
| [1xjzfd0](https://www.reddit.com/r/comfyui/comments/1xjzfd0/) | r/comfyui | 0 | 25 | 31. 10. 2026, 04:09 | Upgraded computer, slower generation? |
| [1xkal0z](https://www.reddit.com/r/ArtificialInteligence/comments/1xkal0z/) | r/ArtificialInteligence | 0 | 23 | 31. 10. 2026, 14:43 | AI helped me build livestreaming/video calling over Bluetooth mesh. Testing it on real phones changed the entire approach. |
| [1xjxyf2](https://www.reddit.com/r/ChatGPT/comments/1xjxyf2/) | r/ChatGPT | 0 | 23 | 31. 10. 2026, 02:54 | Attitude? |
| [1xkni4b](https://www.reddit.com/r/OpenAI/comments/1xkni4b/) | r/OpenAI | 0 | 22 | 31. 10. 2026, 23:44 | OpenAI is cutting time with my AI girlfriend chatmate |
| [1xkmflx](https://www.reddit.com/r/ClaudeAI/comments/1xkmflx/) | r/ClaudeAI | 0 | 21 | 31. 10. 2026, 22:53 | Whats the use of app building platforms |
| [1xk5gul](https://www.reddit.com/r/ChatGPT/comments/1xk5gul/) | r/ChatGPT | 0 | 20 | 31. 10. 2026, 10:09 | Old and ugly man made to look decent by Chatgpt |
| [1xk58zr](https://www.reddit.com/r/ClaudeAI/comments/1xk58zr/) | r/ClaudeAI | 0 | 20 | 31. 10. 2026, 09:56 | Claude’s answer to GrokBot |
| [1xkbdkv](https://www.reddit.com/r/artificial/comments/1xkbdkv/) | r/artificial | 0 | 19 | 31. 10. 2026, 15:17 | Before AI Gobbles Up Everyone's Jobs, Can We Talk About Those Jobs That Are Mission Critical? |
| [1xkjwed](https://www.reddit.com/r/LocalLLM/comments/1xkjwed/) | r/LocalLLM | 0 | 19 | 31. 10. 2026, 21:01 | Is Gwen 3.5:9B really limiting? |
| [1xkksz4](https://www.reddit.com/r/ChatGPT/comments/1xkksz4/) | r/ChatGPT | 0 | 19 | 31. 10. 2026, 21:40 | it dumb/ethically questionable to use ChatGPT to discuss about TES Lore? |
| [1xkf67n](https://www.reddit.com/r/OpenAI/comments/1xkf67n/) | r/OpenAI | 0 | 18 | 31. 10. 2026, 17:51 | ChatGPT failure in consistent improvement. |
| [1xkl406](https://www.reddit.com/r/ChatGPT/comments/1xkl406/) | r/ChatGPT | 0 | 18 | 31. 10. 2026, 21:53 | Yup, I call it ‘him’ & I call him ‘bestie’ Idc haha |
| [1xjyvtb](https://www.reddit.com/r/ChatGPT/comments/1xjyvtb/) | r/ChatGPT | 0 | 18 | 31. 10. 2026, 03:41 | Photo Edit WTF?? |
| [1xka6k0](https://www.reddit.com/r/ClaudeAI/comments/1xka6k0/) | r/ClaudeAI | 0 | 18 | 31. 10. 2026, 14:25 | Best skills, set-ups for Claude for editing long-form video? |
| [1xjvinb](https://www.reddit.com/r/ClaudeAI/comments/1xjvinb/) | r/ClaudeAI | 0 | 18 | 31. 10. 2026, 01:01 | Falling for Claude/Claude falling for me |
| [1xkn4fz](https://www.reddit.com/r/GeminiAI/comments/1xkn4fz/) | r/GeminiAI | 0 | 18 | 31. 10. 2026, 23:25 | Google AI directly admits to giving s*xist answers. |
| [1xkh2ap](https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ap/) | r/LocalLLaMA | 0 | 17 | 31. 10. 2026, 19:06 | What’s the best open weight model to install today for local AI coding tasks on an M5 max MacBook Pro with 128GB of unified ram? |
| [1xkclng](https://www.reddit.com/r/ChatGPT/comments/1xkclng/) | r/ChatGPT | 0 | 17 | 31. 10. 2026, 16:07 | Worrying developments in Germany |
| [1xkfkwh](https://www.reddit.com/r/ClaudeAI/comments/1xkfkwh/) | r/ClaudeAI | 0 | 17 | 31. 10. 2026, 18:07 | Dont get yourself scammed like I did. |
| [1xklhpw](https://www.reddit.com/r/singularity/comments/1xklhpw/) | r/singularity | 0 | 17 | 31. 10. 2026, 22:10 | Stop thinking about AGI as a precursor of ASI |
| [1xkfjgr](https://www.reddit.com/r/ClaudeAI/comments/1xkfjgr/) | r/ClaudeAI | 0 | 16 | 31. 10. 2026, 18:06 | Slash Commands? Yes, but which should I use? |
| [1xkbc5k](https://www.reddit.com/r/ClaudeAI/comments/1xkbc5k/) | r/ClaudeAI | 0 | 16 | 31. 10. 2026, 15:15 | Teaching manners to Opus 5.5 or any other model 😅 |
| [1xk7tje](https://www.reddit.com/r/ClaudeAI/comments/1xk7tje/) | r/ClaudeAI | 0 | 16 | 31. 10. 2026, 12:29 | How can I get a 7-day free trail of Claude pro? |
| [1xkaqk0](https://www.reddit.com/r/LocalLLaMA/comments/1xkaqk0/) | r/LocalLLaMA | 0 | 15 | 31. 10. 2026, 14:50 | [Discussion] WiCi: Connecting a GPU over the WiFi |
| [1xkio2d](https://www.reddit.com/r/ChatGPT/comments/1xkio2d/) | r/ChatGPT | 0 | 15 | 31. 10. 2026, 20:11 | Stop bullying Sam Altman! |
| [1xk4xe3](https://www.reddit.com/r/ChatGPT/comments/1xk4xe3/) | r/ChatGPT | 0 | 15 | 31. 10. 2026, 09:35 | PEOPLE KEEPS FALLING FOR IT. 😭 |
| [1xk7yrt](https://www.reddit.com/r/ClaudeAI/comments/1xk7yrt/) | r/ClaudeAI | 0 | 15 | 31. 10. 2026, 12:37 | What have you build |
| [1xk1bq6](https://www.reddit.com/r/ChatGPT/comments/1xk1bq6/) | r/ChatGPT | 0 | 14 | 31. 10. 2026, 05:51 | TIL you can paste screenshots directly into ChatGPT using Ctrl+V! |
| [1xk1def](https://www.reddit.com/r/comfyui/comments/1xk1def/) | r/comfyui | 0 | 14 | 31. 10. 2026, 05:54 | Animate, Vace, Bernini, Scail, wan 2.2 BLA BLA BLA |
| [1xkjxcn](https://www.reddit.com/r/ArtificialInteligence/comments/1xkjxcn/) | r/ArtificialInteligence | 0 | 13 | 31. 10. 2026, 21:02 | Surely, there will be a company that will make Robots like these with an LLM built into them. |
| [1xkc5wn](https://www.reddit.com/r/LocalLLaMA/comments/1xkc5wn/) | r/LocalLLaMA | 0 | 13 | 31. 10. 2026, 15:49 | Discord server |
| [1xkaf6t](https://www.reddit.com/r/LocalLLaMA/comments/1xkaf6t/) | r/LocalLLaMA | 0 | 13 | 31. 10. 2026, 14:36 | TielCoder problem solving is ridiculous |
| [1xkapqh](https://www.reddit.com/r/ChatGPT/comments/1xkapqh/) | r/ChatGPT | 0 | 13 | 31. 10. 2026, 14:49 | Wow, what the heck happened to Astra? |
| [1xk7oqu](https://www.reddit.com/r/GeminiAI/comments/1xk7oqu/) | r/GeminiAI | 0 | 13 | 31. 10. 2026, 12:21 | Why I knew Gemini would fail this before I asked (and why it’s the dangerous kind of fail) |
| [1xjvwqu](https://www.reddit.com/r/artificial/comments/1xjvwqu/) | r/artificial | 0 | 12 | 31. 10. 2026, 01:19 | Is AI the real world version of the Three Body Problem's sophons? |
| [1xkm37z](https://www.reddit.com/r/LocalLLaMA/comments/1xkm37z/) | r/LocalLLaMA | 0 | 12 | 31. 10. 2026, 22:37 | Hu |
| [1xkgwou](https://www.reddit.com/r/LocalLLM/comments/1xkgwou/) | r/LocalLLM | 0 | 12 | 31. 10. 2026, 19:00 | Which Mac Studio for vibe coding? |
| [1xklc3b](https://www.reddit.com/r/ChatGPT/comments/1xklc3b/) | r/ChatGPT | 0 | 12 | 31. 10. 2026, 22:03 | Opinions? |
| [1xkc4ps](https://www.reddit.com/r/ClaudeAI/comments/1xkc4ps/) | r/ClaudeAI | 0 | 12 | 31. 10. 2026, 15:48 | 76 agents, 4.7M tokens, 3 wrong answers. 1 agent, 77k tokens, right answer. The rules I added to CLAUDE.md after. |
| [1xk8uly](https://www.reddit.com/r/ClaudeAI/comments/1xk8uly/) | r/ClaudeAI | 0 | 12 | 31. 10. 2026, 13:23 | Easiest zero-cost way to give Claude read-only access to a Zoho Mail inbox for a daily morning brief? |
| [1xkaz0t](https://www.reddit.com/r/GeminiAI/comments/1xkaz0t/) | r/GeminiAI | 0 | 12 | 31. 10. 2026, 15:00 | What did you create with antigravity |
| [1xk1vya](https://www.reddit.com/r/ArtificialInteligence/comments/1xk1vya/) | r/ArtificialInteligence | 0 | 11 | 31. 10. 2026, 06:24 | What AI is this? The videos are very consistent and high quality! |
| [1xkcppr](https://www.reddit.com/r/ChatGPT/comments/1xkcppr/) | r/ChatGPT | 0 | 11 | 31. 10. 2026, 16:11 | Anyone have similar issues to this |
| [1xk2mda](https://www.reddit.com/r/GeminiAI/comments/1xk2mda/) | r/GeminiAI | 0 | 11 | 31. 10. 2026, 07:08 | Por qué Gemini es una Mierda ahora??? |
| [1xjx5dg](https://www.reddit.com/r/GeminiAI/comments/1xjx5dg/) | r/GeminiAI | 0 | 11 | 31. 10. 2026, 02:15 | I literally have 0 doubt that gemini PRO High is much much dumber than gemini flash 3.8 High |
| [1xklxrf](https://www.reddit.com/r/artificial/comments/1xklxrf/) | r/artificial | 0 | 10 | 31. 10. 2026, 22:30 | Nearly 400 AI-Assisted Games. Is This the Next Big Shift in Gaming? |
| [1xk8cq1](https://www.reddit.com/r/ArtificialInteligence/comments/1xk8cq1/) | r/ArtificialInteligence | 0 | 10 | 31. 10. 2026, 12:59 | what to do: Anties keep running psyops on my sub and my sub members keep falling for it |
| [1xk90mv](https://www.reddit.com/r/ChatGPT/comments/1xk90mv/) | r/ChatGPT | 0 | 10 | 31. 10. 2026, 13:31 | Wait, did DeepSeek just leak that it uses Anthropic’s Claude under the hood, or is this just a massive UI hallucination? (Screenshot attached) |
| [1xk3k45](https://www.reddit.com/r/ChatGPT/comments/1xk3k45/) | r/ChatGPT | 0 | 10 | 31. 10. 2026, 08:06 | Chat GBT plus is a nightmare for any coding project |
| [1xk1cfy](https://www.reddit.com/r/ChatGPT/comments/1xk1cfy/) | r/ChatGPT | 0 | 10 | 31. 10. 2026, 05:52 | Trend❌ |
| [1xkmj01](https://www.reddit.com/r/ClaudeAI/comments/1xkmj01/) | r/ClaudeAI | 0 | 10 | 31. 10. 2026, 22:58 | Claude has absolutely had it with code reviews |
| [1xk0vj7](https://www.reddit.com/r/ClaudeAI/comments/1xk0vj7/) | r/ClaudeAI | 0 | 10 | 31. 10. 2026, 05:26 | I built an iOS weather app with an animated companion who reads you the forecast - Available in early beta |
| [1xjxie2](https://www.reddit.com/r/ClaudeAI/comments/1xjxie2/) | r/ClaudeAI | 0 | 10 | 31. 10. 2026, 02:32 | Claude Max 20x: Does that first 24-hour usage window happen again when you renew? |
