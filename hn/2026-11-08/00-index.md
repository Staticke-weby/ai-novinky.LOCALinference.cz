# Hacker News – denní AI/tech souhrn, 8. 11. 2026

## Metodika

- **Okno:** 8. 11. 2026, 00:00–24:00 Europe/Prague. Zdroj: Hacker News, sběr `scripts/hn-collect.py`.
- **Rozsah:** v datasetu bylo 700 story, 45 kandidátů mělo vlastní balíček a 52 story s alespoň 10 komentáři skončilo v `appendix.json`.
- **Výběr:** 14 článků pokrývá 16 HN story. Dvě další story o vyšetřování Nvidie jsou sloučené do jednoho článku (viz `dalsi_ids`).
- **Vyřazeno jako už vyšlá:** 0 témat. Žádný kandidát neopakoval konkrétní událost nebo produkt z přísného seznamu 5.–7. 11. Téma Nvidie z dnešního Redditu (id `1xr8moa`) je stejné jako článek 50418016, a proto je podle pravidel sloučené, nikoli vynechané. Obecné překryvy (např. paměť agentů) byly posouzeny jako nový text, ne jako opakování stejné události.
- **Vyřazeno mimo záběr:** zbytek kandidátů byly obecné story bez AI přesahu – politika, věda, retro hardware, klasické programování, doprava, kultura a podobně.
- **Příloha:** obsahuje 18 AI/tech story z 52 položek appendixu; zbytek appendixu tvoří ne-AI témata.
- **Co chybělo:** u části odkazů se externí článek nepodařilo načíst (HTTP 403/401/418/504), takže text vychází z titulku, selftextu a komentářů. Konkrétně se to týká zejména 50412591, 50415817, 50412760, 50409856 a 50414021.
- **Poznámka k HN:** veřejné skóre komentářů na HN neexistuje; v balíčcích je místo něj `-`, proto se skóre komentářů v článcích neuvádí. Časy jsou Europe/Prague.

## Články

| # | Téma | HN | Body | Komentáře | Čas |
|---:|---|---:|---:|---:|---|
| 1 | [Sbohem Claude, vítej Pi](50410107_goodbye-claude-hello-pi.md) | [50410107](https://news.ycombinator.com/item?id=50410107) | 725 | 447 | 04:11 |
| 2 | [Goldman Sachs omezil Claude Code](50415628_goldman-sachs-claude-code.md) | [50415628](https://news.ycombinator.com/item?id=50415628) | 688 | 384 | 19:16 |
| 3 | [Jensen Huang přiznal nevěru, Nvidia vyšetřuje](50418016_nvidia-huang-nevera-vysetrovani.md) | [50418016](https://news.ycombinator.com/item?id=50418016) | 480 | 514 | 23:20 |
| 4 | [284B DeepSeek na 64 GB RAM bez GPU](50411961_llama-modchip-deepseek-64gb.md) | [50411961](https://news.ycombinator.com/item?id=50411961) | 402 | 180 | 11:22 |
| 5 | [RAM Altman: skript posílá Altmanovi volnou RAM](50415172_ram-altman-linux-skript.md) | [50415172](https://news.ycombinator.com/item?id=50415172) | 220 | 113 | 18:20 |
| 6 | [AI brain fry a fronta úkolů v gitu](50416363_ai-brain-fry-fronta-ukolu.md) | [50416363](https://news.ycombinator.com/item?id=50416363) | 201 | 158 | 20:37 |
| 7 | [OpenAI vybrala 11 miliard dolarů](50413822_openai-11-miliard-valuace.md) | [50413822](https://news.ycombinator.com/item?id=50413822) | 185 | 204 | 15:49 |
| 8 | [Paměť agentů potřebuje OpenTelemetry moment](50411467_agent-memory-opentelemetry.md) | [50411467](https://news.ycombinator.com/item?id=50411467) | 177 | 105 | 09:40 |
| 9 | [Čelenky sbírají mozková data pro AI](50409856_mozkova-data-nausnice-ai.md) | [50409856](https://news.ycombinator.com/item?id=50409856) | 116 | 92 | 03:02 |
| 10 | [Proč jeden vývojář odmítá LLM v kódování](50412591_proc-odmitam-llm-kodovani.md) | [50412591](https://news.ycombinator.com/item?id=50412591) | 110 | 225 | 13:14 |
| 11 | [AI vyléčí nemoci? Farmaceuti jsou skeptičtí](50415817_ai-lecba-nemoci-farmaceuti.md) | [50415817](https://news.ycombinator.com/item?id=50415817) | 94 | 114 | 19:43 |
| 12 | [FuckCaptcha: průvodce typy CAPTCHA](50415078_fuckcaptcha-pruvodce.md) | [50415078](https://news.ycombinator.com/item?id=50415078) | 43 | 12 | 18:09 |
| 13 | [Anthropic dá 3,4 miliardy na plynové elektrárny](50412760_anthropic-plynova-elektrarna.md) | [50412760](https://news.ycombinator.com/item?id=50412760) | 40 | 28 | 13:41 |
| 14 | [Apple tlačí na ambicióznější AI a Siri](50414021_apple-siri-agentni-ai.md) | [50414021](https://news.ycombinator.com/item?id=50414021) | 35 | 60 | 16:19 |

## Příloha: všechny AI/tech story z appendixu

Tabulka obsahuje 18 AI/tech story s alespoň 10 komentáři. U sloučených story odkaz vede na článek, do kterého byly sloučené; u story bez samostatného článku vede odkaz na diskusi na HN.

| HN id | Skóre | Komentáře | Čas | Titulek | Odkaz |
|---:|---:|---:|---|---|---|
| 50410107 | 725 | 447 | 04:11 | Sbohem Claude, vítej Pi | [článek](50410107_goodbye-claude-hello-pi.md) |
| 50415628 | 688 | 384 | 19:16 | Goldman Sachs odebírá Claude Code bankéřům a traderům | [článek](50415628_goldman-sachs-claude-code.md) |
| 50418016 | 480 | 514 | 23:20 | Dopis CEO Nvidie Jensena Huanga zaměstnancům o aféře | [článek](50418016_nvidia-huang-nevera-vysetrovani.md) |
| 50416801 | 453 | 339 | 21:26 | Představenstvo Nvidia vyšetřuje Jensena Huanga | [článek](50418016_nvidia-huang-nevera-vysetrovani.md) |
| 50411961 | 402 | 180 | 11:22 | Llama-modchip: 284B DeepSeek na 64GB RAM, bez GPU | [článek](50411961_llama-modchip-deepseek-64gb.md) |
| 50415172 | 220 | 113 | 18:20 | RAM Altman: Linuxový skript denně e-mailem posílá Samu Altmanovi, kolik nevyužité RAM máš v PC | [článek](50415172_ram-altman-linux-skript.md) |
| 50416363 | 201 | 158 | 20:37 | Jak bojuji proti vyčerpání mozku z AI | [článek](50416363_ai-brain-fry-fronta-ukolu.md) |
| 50413822 | 185 | 204 | 15:49 | OpenAI získává $11B při valuaci $1.25T | [článek](50413822_openai-11-miliard-valuace.md) |
| 50411467 | 177 | 105 | 09:40 | Agentní paměť potřebuje svůj OpenTelemetry moment | [článek](50411467_agent-memory-opentelemetry.md) |
| 50409856 | 116 | 92 | 03:02 | Spotřebitelské headsets na mozkové vlny ohrožují soukromí | [článek](50409856_mozkova-data-nausnice-ai.md) |
| 50412591 | 110 | 225 | 13:14 | Proč při programování nebudu používat LLM | [článek](50412591_proc-odmitam-llm-kodovani.md) |
| 50415817 | 94 | 114 | 19:43 | Silicon Valley slibuje, že AI vyléčí nemoci. Šéfové farmaceutických firem tomu nevěří | [článek](50415817_ai-lecba-nemoci-farmaceuti.md) |
| 50415078 | 43 | 12 | 18:09 | Praktický průvodce typy CAPTCHA a tím, jak je prolomit | [článek](50415078_fuckcaptcha-pruvodce.md) |
| 50416679 | 41 | 12 | 21:14 | Představenstvo Nvidia prošetří špionážní kauzu poté, co CEO přiznal aféru | [článek](50418016_nvidia-huang-nevera-vysetrovani.md) |
| 50412760 | 40 | 28 | 13:41 | Anthropic uzavírá dohodu za $3.4B na výrobu plynové energie pro datová centra | [článek](50412760_anthropic-plynova-elektrarna.md) |
| 50414021 | 35 | 60 | 16:19 | CEO Apple tlačí na šéfa softwaru, aby prosazoval ambicióznější AI strategii | [článek](50414021_apple-siri-agentni-ai.md) |
| 50410796 | 7 | 11 | 06:58 | 70 % Britů říká AI prosím nebo děkuji, někteří se dokonce omlouvají | [diskuse](https://news.ycombinator.com/item?id=50410796) |
| 50409438 | 4 | 10 | 01:37 | Ask HN: Pokud bude reverzní inženýrství LLM považováno za nelegální, je to precedent pro OSS? | [diskuse](https://news.ycombinator.com/item?id=50409438) |
