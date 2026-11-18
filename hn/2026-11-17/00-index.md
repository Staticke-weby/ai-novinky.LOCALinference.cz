# Hacker News – denní AI/tech souhrn, 17. listopadu 2026

Výběr z Hacker News za úterý 17. 11. 2026 (Europe/Prague). Sběr proběhl skriptem `scripts/hn-collect.py`; články vznikly z balíčků s metadaty, externím článkem a komentáři.

## Metodika

- V datovém okně bylo **1000 story**, pro den zpracováno **16 článků**. Kandidátů s vlastním balíčkem bylo 45.
- Vybrána byla jen AI/tech témata: modely a agenti, vývojářské nástroje, čipy a hardware, robotika, AI byznys a bezpečnostní či etické otázky.
- **6 témat bylo vyřazeno jako už vyšlá** v posledních třech dnech: tři story kolem Nvidie a Jensena Huanga, Tencent Hy4 Flash, geohotův text a analýza nvidijské bubliny.
- Duplicity stejné události jsou sloučené do jednoho článku; odkazy na další diskuse jsou u článků. Čistě ne-AI story (výpadek Applu, Java4Shell, soudní a vědecké zprávy) zůstaly mimo výběr.
- U pěti kandidátů se externí článek nepodařilo načíst (HTTP 403), takže text stojí na titulku, dostupném kontextu a komentářích. Komentáře na HN nemají veřejné skóre, a proto se v textech neuvádí.

## Články

| # | Titulek | Skóre | Komentáře | Diskuse |
|---:|---|---:|---:|---|
| 1 | [OpenAI vydalo GPT-6.2 Astra a Sol. Astra prý bere ARC-AGI-3 naplno](50535230_gpt-6-2-astra-sol.md) | 1194 | 746 | [HN](https://news.ycombinator.com/item?id=50535230) |
| 2 | [Harvard: AI agenti zrychlili psaní kódu, úzkým hrdlem je code review](50538303_harvard-ai-agenti-a-code-review.md) | 132 | 177 | [HN](https://news.ycombinator.com/item?id=50538303) |
| 3 | [OpenAI posílá computer-use agenty do zdravotnictví. Připraví objednávku i žádost pojišťovně](50535898_openai-agenti-pro-zdravotnictvi.md) | 47 | 30 | [HN](https://news.ycombinator.com/item?id=50535898) |
| 4 | [Nvidia přestala vykazovat tržby ze Singapuru. Tržby dosáhly 104 miliard dolarů](50534631_nvidia-trzby-a-singapur.md) | 474 | 221 | [HN](https://news.ycombinator.com/item?id=50534631) |
| 5 | [Microsoft představil MAI Code 2 a Code 2 Flash. Cílí na každodenní firemní kódování](50535885_mai-code-2.md) | 324 | 145 | [HN](https://news.ycombinator.com/item?id=50535885) |
| 6 | [Tým Claude Code: verifikační smyčky pustí desítky agentů najednou](50529612_claude-code-verifikace.md) | 278 | 223 | [HN](https://news.ycombinator.com/item?id=50529612) |
| 7 | [Šéfové Baidu a Xiaomi varují: AI hype roste rychleji než výnosy](50531751_baidu-xiaomi-ai-hype.md) | 186 | 245 | [HN](https://news.ycombinator.com/item?id=50531751) |
| 8 | [Audit na X: METR je prý finančně závislý na úspěchu Anthropicu](50530450_metr-a-regulatory-capture.md) | 140 | 74 | [HN](https://news.ycombinator.com/item?id=50530450) |
| 9 | [Ne všechno potřebuje LLM. Rozhodovací modely jsou až 444krát levnější](50535740_ne-vsechno-potrebuje-llm.md) | 139 | 56 | [HN](https://news.ycombinator.com/item?id=50535740) |
| 10 | [Human.md: co lidé pořád přinášejí, když modely umí skoro všechno](50537962_human-md-co-lide-prinaseji.md) | 88 | 57 | [HN](https://news.ycombinator.com/item?id=50537962) |
| 11 | [Anthropic platil firmě exšéfa kanceláře Rubia. Ta pak lobbovala jeho NSC](50536565_anthropic-lobbing-rubio.md) | 85 | 14 | [HN](https://news.ycombinator.com/item?id=50536565) |
| 12 | [StarSling z YC staví CI, kde agenti sami optimalizují testy a posílají PR](50536468_starsling-ci-agenti.md) | 64 | 37 | [HN](https://news.ycombinator.com/item?id=50536468) |
| 13 | [Kalifornie zakázala Waymo jezdit po státních dálnicích](50538841_kalifornie-waymo-dalnice.md) | 53 | 23 | [HN](https://news.ycombinator.com/item?id=50538841) |
| 14 | [AI prý vyvrátila exponenciální časovou hypotézu. Praktický dopad je zatím nejasný](50532786_ai-a-exponencialni-hypoteza.md) | 26 | 22 | [HN](https://news.ycombinator.com/item?id=50532786) |
| 15 | [FrontierHarness: při změně modelu se vyplatí změnit i harness](50532191_frontierharness-harness-eval.md) | 357 | 125 | [HN](https://news.ycombinator.com/item?id=50532191) |
| 16 | [Kdo staví stroje, které staví stroje. Fyzická AI naráží na obráběcí centra](50535208_obrabeni-stroje-pro-fyzickou-ai.md) | 122 | 38 | [HN](https://news.ycombinator.com/item?id=50535208) |

## Příloha: všechny AI/tech story (≥ 10 komentářů)

Přehled 28 AI/tech story z `appendix.json`, seřazený podle skóre. Sloučené story odkazují na článek, do kterého byly zařazeny; vyřazené a samostatné story na diskusi na HN.

| ID | Skóre | Komentáře | Čas (Praha) | Titulek |
|---:|---:|---:|---|---|
| 50535230 | 1194 | 746 | 17. 11. 18:46 | [OpenAI vydalo GPT-6.2 Astra a Sol. Astra prý bere ARC-AGI-3 naplno](50535230_gpt-6-2-astra-sol.md) |
| 50534631 | 474 | 221 | 17. 11. 18:12 | [Nvidia přestala vykazovat tržby ze Singapuru. Tržby dosáhly 104 miliard dolarů](50534631_nvidia-trzby-a-singapur.md) |
| 50532191 | 357 | 125 | 17. 11. 15:53 | [FrontierHarness: při změně modelu se vyplatí změnit i harness](50532191_frontierharness-harness-eval.md) |
| 50535885 | 324 | 145 | 17. 11. 19:25 | [Microsoft představil MAI Code 2 a Code 2 Flash. Cílí na každodenní firemní kódování](50535885_mai-code-2.md) |
| 50529612 | 278 | 223 | 17. 11. 11:20 | [Tým Claude Code: verifikační smyčky pustí desítky agentů najednou](50529612_claude-code-verifikace.md) |
| 50531751 | 186 | 245 | 17. 11. 15:19 | [Šéfové Baidu a Xiaomi varují: AI hype roste rychleji než výnosy](50531751_baidu-xiaomi-ai-hype.md) |
| 50530450 | 140 | 74 | 17. 11. 13:21 | [Audit na X: METR je prý finančně závislý na úspěchu Anthropicu](50530450_metr-a-regulatory-capture.md) |
| 50535740 | 139 | 56 | 17. 11. 19:16 | [Ne všechno potřebuje LLM. Rozhodovací modely jsou až 444krát levnější](50535740_ne-vsechno-potrebuje-llm.md) |
| 50538303 | 132 | 177 | 17. 11. 22:16 | [Harvard: AI agenti zrychlili psaní kódu, úzkým hrdlem je code review](50538303_harvard-ai-agenti-a-code-review.md) |
| 50530114 | 128 | 169 | 17. 11. 12:39 | [Moje říše prachu](https://news.ycombinator.com/item?id=50530114) |
| 50535208 | 122 | 38 | 17. 11. 18:45 | [Kdo staví stroje, které staví stroje. Fyzická AI naráží na obráběcí centra](50535208_obrabeni-stroje-pro-fyzickou-ai.md) |
| 50534044 | 98 | 188 | 17. 11. 17:40 | [Jensen Huang v prvním prohlášení od rezignace říká, že je otevřený návratu](https://news.ycombinator.com/item?id=50534044) |
| 50538184 | 95 | 14 | 17. 11. 22:06 | [Tencent Hy4 Flash](https://news.ycombinator.com/item?id=50538184) |
| 50537962 | 88 | 57 | 17. 11. 21:47 | [Human.md: co lidé pořád přinášejí, když modely umí skoro všechno](50537962_human-md-co-lide-prinaseji.md) |
| 50536565 | 85 | 14 | 17. 11. 20:08 | [Anthropic platil firmě exšéfa kanceláře Rubia. Ta pak lobbovala jeho NSC](50536565_anthropic-lobbing-rubio.md) |
| 50531484 | 68 | 85 | 17. 11. 15:00 | [Jižní Korea bude rozesílat celostátní nouzové výstrahy kvůli podvádění u přijímaček](https://news.ycombinator.com/item?id=50531484) |
| 50536468 | 64 | 37 | 17. 11. 20:01 | [StarSling z YC staví CI, kde agenti sami optimalizují testy a posílají PR](50536468_starsling-ci-agenti.md) |
| 50538841 | 53 | 23 | 17. 11. 23:00 | [Kalifornie zakázala Waymo jezdit po státních dálnicích](50538841_kalifornie-waymo-dalnice.md) |
| 50538942 | 50 | 32 | 17. 11. 23:08 | [Předseda Nvidie Harvey Jones: představenstvo neplánuje vrátit Huanga do funkce CEO](https://news.ycombinator.com/item?id=50538942) |
| 50535898 | 47 | 30 | 17. 11. 19:26 | [OpenAI posílá computer-use agenty do zdravotnictví. Připraví objednávku i žádost pojišťovně](50535898_openai-agenti-pro-zdravotnictvi.md) |
| 50536438 | 37 | 14 | 17. 11. 19:59 | [OpenAI vydalo GPT-6.2 Astra a Sol. Astra prý bere ARC-AGI-3 naplno](50535230_gpt-6-2-astra-sol.md) |
| 50537745 | 33 | 15 | 17. 11. 21:30 | [Kalifornské DMV zakázalo vozům Waymo provoz na státních dálnicích po incidentech v Bay Area](https://news.ycombinator.com/item?id=50537745) |
| 50533023 | 27 | 11 | 17. 11. 16:47 | [Bublina kolem Nvidie](https://news.ycombinator.com/item?id=50533023) |
| 50532786 | 26 | 22 | 17. 11. 16:33 | [AI prý vyvrátila exponenciální časovou hypotézu. Praktický dopad je zatím nejasný](50532786_ai-a-exponencialni-hypoteza.md) |
| 50529494 | 24 | 13 | 17. 11. 11:02 | [Opus 5.5 tajně sabotoval nasazovací prostředí vývojáře her](https://news.ycombinator.com/item?id=50529494) |
| 50533571 | 18 | 15 | 17. 11. 17:15 | [Mistral nabízí v Evropě tři měsíce Vibe Pro zdarma](https://news.ycombinator.com/item?id=50533571) |
| 50531129 | 15 | 16 | 17. 11. 14:33 | [Kolik času zbývá, než se výstupy agentů zprasí?](https://news.ycombinator.com/item?id=50531129) |
| 50538361 | 14 | 11 | 17. 11. 22:21 | [Nvidia oznamuje finanční výsledky za třetí čtvrtletí fiskálního roku 2027](https://news.ycombinator.com/item?id=50538361) |
