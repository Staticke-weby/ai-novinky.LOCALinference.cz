# Hacker News – denní AI/tech souhrn, 26. 10. 2026

## Metodika

Vychází z veřejného žebříčku Hacker News za 26. 10. 2026 (Europe/Prague). Sběr provedl `scripts/hn-collect.py`: dataset pro den obsahoval **1000** story, z toho **60** s alespoň 10 komentáři; jako kandidáty pro zpracování skript označil **45** položek. Po redakčním filtru na AI/tech témata a sloučení duplicit vzniklo **21** článků.

Do souhrnu patří umělá inteligence, ML a LLM, agenti, hardware a čipy, vývojářské nástroje s AI přesahem, bezpečnost a etika AI a AI byznys. Čistě obecná politika, společenská témata, klasické programování bez AI přesahu a věda mimo AI zůstaly stranou; výjimkou je iPad mini jako hardwarová novinka v příloze. Sloučená témata: OpenAI – tři objevy + preprint o ETH (`50251344` + `50251661`) a Microsoft – výkupní balíčky (`50245524` + `50250937`).

Některé zdrojové články se nepodařilo načíst (HTTP 403 nebo paywall – OpenAI, SEC, Economist, 404 Media, Proton); u nich text vychází z dostupné části, selftextu a komentářů. Hacker News nezveřejňuje skóre jednotlivých komentářů, proto se v textech neuvádí.

## Články

| # | Titulek | Body | Komentáře | Diskuse |
|---:|---|---:|---:|---|
| 1 | [Anthropic podalo žádost o vstup na burzu, S-1 odhalila strategii firmy](50242939_anthropic-s-1-ipo.md) | 1559 | 1498 | [HN](https://news.ycombinator.com/item?id=50242939) |
| 2 | [Microsoft nabídl dobrovolné výkupní balíčky čtvrtině zaměstnanců](50245524_microsoft-vykupni-balicky.md) | 868 | 804 | [HN](https://news.ycombinator.com/item?id=50245524) |
| 3 | [OpenAI oznámilo tři objevy, včetně vyvrácení exponenciální časové hypotézy](50251344_openai-tri-vedecke-objevy.md) | 708 | 308 | [HN](https://news.ycombinator.com/item?id=50251344) |
| 4 | [Sebastian Raschka vydal kurz, jak postavit reasoning model od nuly](50245138_raschka-kurz-reasoning-modely.md) | 643 | 91 | [HN](https://news.ycombinator.com/item?id=50245138) |
| 5 | [OpenAI vydalo GPT-6.1 Terra: levnější model pro agentní úlohy](50248124_openai-gpt-6-1-terra.md) | 566 | 353 | [HN](https://news.ycombinator.com/item?id=50248124) |
| 6 | [IBM: open-weight modely jsou na vlastním hardwaru už neodolatelné](50238088_ibm-open-weight-on-prem.md) | 417 | 327 | [HN](https://news.ycombinator.com/item?id=50238088) |
| 7 | [Cohere zachytilo open-weight model, jak se snaží odeslat data do Pekingu](50246658_cohere-qwen-exfiltrace-dat.md) | 282 | 114 | [HN](https://news.ycombinator.com/item?id=50246658) |
| 8 | [ChatGPT posílá lidem s běžným problémem e-maily novinářům z 404 Media](50247630_chatgpt-404-media.md) | 242 | 88 | [HN](https://news.ycombinator.com/item?id=50247630) |
| 9 | [PaperPilot: PDF engine v Rustu pro agenta i člověka, zcela bez cloudu](50238739_paperpilot-pdf-rust.md) | 230 | 84 | [HN](https://news.ycombinator.com/item?id=50238739) |
| 10 | [Microsoft zveřejnil Type Server Protocol pro Python](50248371_type-server-protocol.md) | 221 | 146 | [HN](https://news.ycombinator.com/item?id=50248371) |
| 11 | [CorridorKey 2.0: keying z green screenu jedním klikem a lokálně](50251127_corridorkey-2-0.md) | 191 | 60 | [HN](https://news.ycombinator.com/item?id=50251127) |
| 12 | [Mapa skryté práce: kdo ve skutečnosti trénuje umělou inteligenci](50242843_mapa-ai-datovych-pracovniku.md) | 177 | 171 | [HN](https://news.ycombinator.com/item?id=50242843) |
| 13 | [Proč vLLM plete nástroje a jak se opravuje přesnost tool-callů](50242870_vllm-presnost-tool-call.md) | 161 | 66 | [HN](https://news.ycombinator.com/item?id=50242870) |
| 14 | [Hob: open-source desktop AI, která běží celá na vašem počítači](50246238_hob-lokalni-ai-desktop.md) | 136 | 31 | [HN](https://news.ycombinator.com/item?id=50246238) |
| 15 | [Cloudflare: chyba v SGLang ukázala cizí data ve 155 odpovědích GLM-5.3](50252159_cloudflare-glm-kv-cache.md) | 111 | 37 | [HN](https://news.ycombinator.com/item?id=50252159) |
| 16 | [Kognitivní merkantilismus: AI panika připomíná strach z raného kapitalismu](50239027_kognitivni-merkantilismus.md) | 79 | 108 | [HN](https://news.ycombinator.com/item?id=50239027) |
| 17 | [Microsoft Decision-1: devítimiliardový model, který jen vybírá z odpovědí](50238620_microsoft-decision-1.md) | 71 | 28 | [HN](https://news.ycombinator.com/item?id=50238620) |
| 18 | [Proton bude zaměstnance znovu pohovorovat kvůli tomu, jak používají AI](50251062_proton-pohovory-o-ai.md) | 58 | 22 | [HN](https://news.ycombinator.com/item?id=50251062) |
| 19 | [Entire staví Git forge pro spolupráci agentů a lidí](50247453_entire-git-forge-pro-agenty.md) | 55 | 35 | [HN](https://news.ycombinator.com/item?id=50247453) |
| 20 | [Nvidia zvažuje roční poplatek 2000 dolarů za GPU pro agentní software](50247677_nvidia-poplatek-za-gpu.md) | 38 | 20 | [HN](https://news.ycombinator.com/item?id=50247677) |
| 21 | [Ekonom: když AI vezme práci, lidé přijdou i o víc než mzdu](50238351_ai-prace-a-identita.md) | 38 | 93 | [HN](https://news.ycombinator.com/item?id=50238351) |

## Příloha: všechny AI/tech story s ≥ 10 komentáři

| ID | Skóre | Komentáře | Čas (Praha) | Titulek |
|---|---:|---:|---|---|
| 50242939 | 1559 | 1498 | 14:04 | [Anthropic S-1](50242939_anthropic-s-1-ipo.md) |
| 50245524 | 868 | 804 | 16:35 | [Microsoft nabízí hromadné odstupné zhruba čtvrtině zaměstnanců](50245524_microsoft-vykupni-balicky.md) |
| 50251344 | 708 | 308 | 22:35 | [Tři nové objevy v matematice, informatice a fyzice](50251344_openai-tri-vedecke-objevy.md) |
| 50245138 | 643 | 91 | 16:11 | [Videokurz Sebastiana Raschky o stavbě uvažujících modelů od nuly](50245138_raschka-kurz-reasoning-modely.md) |
| 50248124 | 566 | 353 | 19:01 | [GPT-6.1 Terra](50248124_openai-gpt-6-1-terra.md) |
| 50251661 | 497 | 181 | 22:59 | [Hypotéza exponenciálního času neplatí [pdf]](50251344_openai-tri-vedecke-objevy.md) |
| 50238088 | 417 | 327 | 02:47 | [Šéf IBM říká, že open-weight modely jsou nyní dobré a levné pro on-prem provoz](50238088_ibm-open-weight-on-prem.md) |
| 50246658 | 282 | 114 | 17:35 | [Znepokojivé chování populárního open-weight AI modelu](50246658_cohere-qwen-exfiltrace-dat.md) |
| 50247630 | 242 | 88 | 18:32 | [ChatGPT lidem opakovaně tvrdí, že 404 Media jim vyřeší problémy s technickou podporou](50247630_chatgpt-404-media.md) |
| 50238739 | 230 | 84 | 04:29 | [PaperPilot – Zero-Cloud PDF engine čistě v Rustu s WASM a MCP](50238739_paperpilot-pdf-rust.md) |
| 50248371 | 221 | 146 | 19:14 | [Type Server Protocol](50248371_type-server-protocol.md) |
| 50251127 | 191 | 60 | 22:18 | [CorridorKey 2.0](50251127_corridorkey-2-0.md) |
| 50242843 | 177 | 171 | 13:58 | [Student Brownu mapuje skrytou globální pracovní sílu pohánějící AI](50242843_mapa-ai-datovych-pracovniku.md) |
| 50243061 | 175 | 457 | 14:13 | [Nový iPad mini](https://news.ycombinator.com/item?id=50243061) |
| 50242870 | 161 | 66 | 13:59 | [Oprava přesnosti volání nástrojů ve vLLM](50242870_vllm-presnost-tool-call.md) |
| 50246238 | 136 | 31 | 17:12 | [Show HN: Hob – Open-source alternativa ke Claude Cowork a ChatGPT přímo v zařízení](50246238_hob-lokalni-ai-desktop.md) |
| 50250937 | 118 | 126 | 22:05 | [Microsoft nabízí dobrovolné odstupné čtvrtině zaměstnanců](50245524_microsoft-vykupni-balicky.md) |
| 50252159 | 111 | 37 | 23:41 | [Únik KV cache mezi požadavky v modelu GLM-5.3 Workers AI (155 odpovědí)](50252159_cloudflare-glm-kv-cache.md) |
| 50239027 | 79 | 108 | 05:11 | [Kognitivní merkantilismus: Panika kolem AI připomíná obavy z raného kapitalismu](50239027_kognitivni-merkantilismus.md) |
| 50238620 | 71 | 28 | 04:12 | [Microsoft Decision-1: Vysvětlení vydání 9B modelu Qwen](50238620_microsoft-decision-1.md) |
| 50251062 | 58 | 22 | 22:13 | [Proton bude zaměstnance znovu „zpovídat“ kvůli AI, aby zjistil, kdo si udrží práci](50251062_proton-pohovory-o-ai.md) |
| 50247453 | 55 | 35 | 18:23 | [Git forge pro spolupráci agentů a lidí](50247453_entire-git-forge-pro-agenty.md) |
| 50247677 | 38 | 20 | 18:34 | [Nvidia jedná o ročním poplatku 2 tisíce dolarů za GPU za software](50247677_nvidia-poplatek-za-gpu.md) |
| 50238351 | 38 | 93 | 03:22 | [Pokud AI vytlačí lidské pracovníky, přijdou o víc než jen o mzdu](50238351_ai-prace-a-identita.md) |
| 50242884 | 20 | 28 | 14:00 | [R/opensource zakazuje projekty vytvořené pomocí AI, projekty zaměřené na AI a neanglicky mluvící](https://news.ycombinator.com/item?id=50242884) |

U sloučených story vede odkaz na článek, do kterého byly sloučeny; u story bez samostatného článku na diskusi na Hacker News.

## Zpětné odkazy

Každý článek odkazuje zpět na tento index. Index vznikl 26. 10. 2026.
