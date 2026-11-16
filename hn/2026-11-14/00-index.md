# Hacker News – AI/tech souhrn, 14. 11. 2026

Denní přehled AI/tech novinek z Hacker News za **14. listopadu 2026** (časové pásmo Europe/Prague). Výběr se soustředí na umělou inteligenci, modely a agenty, čipy a hardware, vývojářské nástroje, bezpečnost a byznys kolem AI.

## Metodika

Sběr proběhl skriptem `scripts/hn-collect.py`; v denním okně bylo 55 story s alespoň 10 komentáři a 45 kandidátů s vlastním balíčkem (metadata, selftext, externí článek, komentáře). Z nich vzniklo **16 článků**. Dvě témata byla sloučena, protože šlo o stejnou událost z více zdrojů: kruhové financování Nvidie (50493251 + 50501631) a italská pokuta Metě (50497009 + 50498063).

**Vyřazeno jako už vyšlá témata: 7.** Šest kandidátů opakovalo události z 11.–13. listopadu, které už vyšly v předchozích přehledech: kvantizace Unsloth Qwen3.8-27B (11. 11.), ggml/llama.cpp v1.0 (13. 11.), formalizace amerického daňového zákoníku v Lean (11. 11.) a tři příspěvky k aféře Jensena Huanga – pašování GPU (50498051), prodej akcií člena představenstva (50492993) a otevřený dopis boardu (50491690); sedmým vyřazeným byl Denny's a odstraněná cedule Nvidie (50492407), což je tatáž kauza. Zbytek kandidátů byly obecné story mimo AI/tech (politika, kosmonautika, retrocomputing, hry).

Komentáře na Hacker News nemají veřejné skóre, proto se v textech neuvádí; pořadí odpovídá řazení HN. Odkazy v tabulce míří na soubory článků, odkaz `HN` na původní diskusi. U několika balíčků se externí článek nenačetl celý (paywall nebo bot check, například TechPowerUp a Reuters), takže texty vycházejí z dostupné části a z diskuse.

## Články

| # | Článek | Skóre | Komentáře | HN |
|---:|---|---:|---:|---|
| 1 | [Claude Code Projects umí řídit paralelní agenty](50492141_claude-code-projects-paralelni-agenti.md) | 98 | 91 | [diskuse](https://news.ycombinator.com/item?id=50492141) |
| 2 | [Claude smazal profesorovi sylabus i roční poznámky](50499114_claude-smazal-sylabus.md) | 45 | 63 | [diskuse](https://news.ycombinator.com/item?id=50499114) |
| 3 | [Nvidia prý uměle držela ceny GPU přes kruhové financování](50493251_nvidia-kruhove-financovani-gpu.md) | 1064 | 630 | [diskuse](https://news.ycombinator.com/item?id=50493251) |
| 4 | [GLM-5.3 na dvou DGX stanicích: 607 tokenů za sekundu](50497155_glm-5-3-dve-dgx-vllm.md) | 133 | 65 | [diskuse](https://news.ycombinator.com/item?id=50497155) |
| 5 | [DeepSeek V3 ve 200 řádcích čistého JAX](50497589_deepseek-v3-jax.md) | 219 | 20 | [diskuse](https://news.ycombinator.com/item?id=50497589) |
| 6 | [The Claude Delusion: esej o iluzi všemocné AI](50496921_claude-delusion-esej.md) | 146 | 191 | [diskuse](https://news.ycombinator.com/item?id=50496921) |
| 7 | [agweb: prohlížeč pro agenty, který nekrade fokus](50497147_agweb-prohlizec-pro-agenty.md) | 93 | 27 | [diskuse](https://news.ycombinator.com/item?id=50497147) |
| 8 | [Ask HN: které AI dovednosti se vyplatí naučit](50494696_ask-hn-ai-dovednosti.md) | 82 | 51 | [diskuse](https://news.ycombinator.com/item?id=50494696) |
| 9 | [Lovable aplikace odhalily pasy a 200 tisíc zpráv](50499017_lovable-unik-dat.md) | 761 | 302 | [diskuse](https://news.ycombinator.com/item?id=50499017) |
| 10 | [Antigravity /teamwork: agenti vyřešili otevřené vědecké problémy](50496811_antigravity-teamwork-veda.md) | 192 | 40 | [diskuse](https://news.ycombinator.com/item?id=50496811) |
| 11 | [Budou datacentra ve vesmíru? Ekonomika orbitálního computu](50498945_datacentra-ve-vesmiru.md) | 62 | 186 | [diskuse](https://news.ycombinator.com/item?id=50498945) |
| 12 | [geohot: první úder, ASI a slepá ulička AI závodu](50491944_geohot-first-strike-ai-zavod.md) | 62 | 48 | [diskuse](https://news.ycombinator.com/item?id=50491944) |
| 13 | [Fursoy Slice-1: out-of-order RISC-V jádro bootuje Linux](50497137_fursoy-riscv-core-linux.md) | 74 | 26 | [diskuse](https://news.ycombinator.com/item?id=50497137) |
| 14 | [Project Zero zkracuje lhůtu na 90 dní kvůli AI](50496051_project-zero-90-dni.md) | 226 | 88 | [diskuse](https://news.ycombinator.com/item?id=50496051) |
| 15 | [PyPI má nové stránky s jasnějšími bezpečnostními signály](50497892_pypi-bezpecnostni-signaly.md) | 230 | 99 | [diskuse](https://news.ycombinator.com/item?id=50497892) |
| 16 | [Itálie pokutovala Metu 805 milionů eur kvůli fotkám](50497009_italie-pokuta-meta-fotky.md) | 362 | 253 | [diskuse](https://news.ycombinator.com/item?id=50497009) |

## Příloha: všechny AI/tech story s ≥ 10 komentáři

| ID | Skóre | Komentáře | Čas (Praha) | Titulek |
|---:|---:|---:|---|---|
| 50492141 | 98 | 91 | 14. 11. 2026, 01:28 | [Claude Code Projects umí řídit paralelní agenty](50492141_claude-code-projects-paralelni-agenti.md) |
| 50498051 | 53 | 38 | 14. 11. 2026, 16:58 | [Pašování 1,5 milionu AI GPU může být důvodem Huangova odchodu](https://news.ycombinator.com/item?id=50498051) |
| 50499114 | 45 | 63 | 14. 11. 2026, 18:51 | [Claude smazal profesorovi sylabus i roční poznámky](50499114_claude-smazal-sylabus.md) |
| 50493251 | 1064 | 630 | 14. 11. 2026, 03:52 | [Nvidia prý uměle držela ceny GPU přes kruhové financování](50493251_nvidia-kruhove-financovani-gpu.md) |
| 50501631 | 415 | 207 | 14. 11. 2026, 23:26 | [Nvidia prý uměle držela ceny GPU přes kruhové financování](50493251_nvidia-kruhove-financovani-gpu.md) |
| 50497155 | 133 | 65 | 14. 11. 2026, 15:09 | [GLM-5.3 na dvou DGX stanicích: 607 tokenů za sekundu](50497155_glm-5-3-dve-dgx-vllm.md) |
| 50491980 | 246 | 82 | 14. 11. 2026, 01:06 | [Kvantizace Unsloth Qwen3.8-27B – aktualizace Dynamic v3.1](https://news.ycombinator.com/item?id=50491980) |
| 50497589 | 219 | 20 | 14. 11. 2026, 16:04 | [DeepSeek V3 ve 200 řádcích čistého JAX](50497589_deepseek-v3-jax.md) |
| 50492993 | 217 | 53 | 14. 11. 2026, 03:21 | [Člen představenstva Nvidie prodal akcie za téměř miliardu dolarů před skandálem](https://news.ycombinator.com/item?id=50492993) |
| 50496921 | 146 | 191 | 14. 11. 2026, 14:36 | [The Claude Delusion: esej o iluzi všemocné AI](50496921_claude-delusion-esej.md) |
| 50497147 | 93 | 27 | 14. 11. 2026, 15:08 | [agweb: prohlížeč pro agenty, který nekrade fokus](50497147_agweb-prohlizec-pro-agenty.md) |
| 50494696 | 82 | 51 | 14. 11. 2026, 07:56 | [Ask HN: které AI dovednosti se vyplatí naučit](50494696_ask-hn-ai-dovednosti.md) |
| 50491690 | 48 | 44 | 14. 11. 2026, 00:34 | [Otevřený dopis představenstvu Nvidie](https://news.ycombinator.com/item?id=50491690) |
| 50492407 | 15 | 11 | 14. 11. 2026, 02:04 | [Denny's, kde vznikla Nvidia, odstranil ceduli oslavující firmu](https://news.ycombinator.com/item?id=50492407) |
| 50499017 | 761 | 302 | 14. 11. 2026, 18:43 | [Lovable aplikace odhalily pasy a 200 tisíc zpráv](50499017_lovable-unik-dat.md) |
| 50496811 | 192 | 40 | 14. 11. 2026, 14:20 | [Antigravity /teamwork: agenti vyřešili otevřené vědecké problémy](50496811_antigravity-teamwork-veda.md) |
| 50497009 | 362 | 253 | 14. 11. 2026, 14:48 | [Itálie pokutovala Metu 805 milionů eur kvůli fotkám](50497009_italie-pokuta-meta-fotky.md) |
| 50498063 | 133 | 63 | 14. 11. 2026, 17:00 | [Itálie pokutovala Metu 805 milionů eur kvůli fotkám](50497009_italie-pokuta-meta-fotky.md) |
| 50497892 | 230 | 99 | 14. 11. 2026, 16:40 | [PyPI má nové stránky s jasnějšími bezpečnostními signály](50497892_pypi-bezpecnostni-signaly.md) |
| 50496051 | 226 | 88 | 14. 11. 2026, 12:13 | [Project Zero zkracuje lhůtu na 90 dní kvůli AI](50496051_project-zero-90-dni.md) |
| 50497137 | 74 | 26 | 14. 11. 2026, 15:06 | [Fursoy Slice-1: out-of-order RISC-V jádro bootuje Linux](50497137_fursoy-riscv-core-linux.md) |
| 50493062 | 402 | 68 | 14. 11. 2026, 03:28 | [Ggml v1.0.0](https://news.ycombinator.com/item?id=50493062) |
| 50498945 | 62 | 186 | 14. 11. 2026, 18:35 | [Budou datacentra ve vesmíru? Ekonomika orbitálního computu](50498945_datacentra-ve-vesmiru.md) |
| 50491944 | 62 | 48 | 14. 11. 2026, 01:00 | [geohot: první úder, ASI a slepá ulička AI závodu](50491944_geohot-first-strike-ai-zavod.md) |
