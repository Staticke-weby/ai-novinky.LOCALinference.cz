# 1wmntwv

**MiMo-V2.6-Pro-RL: 1,02T MoE s 42B aktivními parametry, 1M kontextem a omnimodálním vstupem**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Bestlife73 |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 140 / 29 (později 137/29 v jiném vlákně) |
| Model card | https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmntwv/xiaomimimomimov26prorl_hugging_face/ |

## Co se stalo

Xiaomi MiMo vydalo **vlajkový checkpoint řady MiMo-V2.6** — Pro-RL. Nejde o lokálně provozovatelný model v běžném smyslu: jde o **1,02 bilionu parametrů** (MoE) s **42B aktivními**, určený pro vLLM/SGLang nasazení a API.

## Architektura a čísla

- Sparse MoE **1,02T total / 42B activated**, **1M tokenů kontext**.
- Modality: text, obrázek, video, audio; MiMo ViT 681M; audio tokenizer 308M + 127M patch encoder; 5vrstvý spekulativní dekodér; 70/60/10 vrstev (Total/SWA/GA), hidden 6144, 384 routed expertů / 8 aktivních.
- RL: asynchronní GRPO, **1 568 promptů × 16 rolloutů na krok**, „Groupwise Reward Synthesis“ a „Groupwise Advantage Redistribution“, multi-prefix multi-teacher distillation.
- Benchmarky Pro: DeepSWE v1.1 **71,9**, Terminal Bench 2.1 **89,9**, OSWorld-Verified **82,0**, CyberGym **94,0**, GDPval-AA 2.1 **1673**, MiMo VisualCoding **72,3**, ExploitBench **47,9**, SEC Bench Pro **66,3**.
- Licence MIT, jazyky en/zh, dostupné i přes AI Studio, MiMo Code, Desktop, Open Platform API a OpenRouter.

## Citace

> „MiMo-V2.6-Pro-RL je vlajkový checkpoint řady MiMo-V2.6.“ (překlad) — Xiaomi MiMo Team

> „Text, obraz, video a zvuk v jednom modelu; 1M tokenů pro dlouhé repozitáře, stopy nástrojů a více relační běhy agentů.“ (překlad) — Xiaomi MiMo Team

> „Sakra, soudě podle jejich benchů, postavili prostě něco úžasného? MiMo-V2.5 Pro se mi líbil jako kritický sub-agent, ale Flash a Pro mohou být nové agentické kódovací kombo.“ (překlad) — u/cleversmoke

> „1T model s pouhými 156B trénovacích tokenů může být upřímně podtrénovaný. Bude zajímavé, jak si povedou pozdější checkpointy.“ (překlad) — u/fgk55555

> „Poběží mi to na 4GB VRAM a 8GB DDR4 (samozřejmě s offloadingem do systémové RAM)“ (překlad) — u/circumcised_hobbit

## Hlavní linky diskuse

- **Nejde o lokální model.** Otázky typu „poběží na 4 GB VRAM“ kontrastují s velikostí 1T; vlákno je spíš o benchmarkách a API.
- **Chvála benchmarků** — „new king“ nálada, kombinace Flash+Pro jako „agentic coding combo“.
- **Podezření na undertraining** — 1T parametrů při relativně malém počtu trénovacích tokenů.
- **OpenRouter a rychlost:** komentář o Flash verzi, která prý překonává DeepSeek Flash a nabízí 190 tk/s „ultraspeed“ za $9.

## Rozpory a neověřené informace

- Hugging Face metadata hlásí jinou velikost (500B) než komentující (1T) — rozpor v metadatech, nikoli v model card.
- Neověřené: srovnání výkonu Flash vs DeepSeek Flash, cena/rychlost na OpenRouteru, tvrzení o undertrainingu.

## Proč to je důležité

MiMo-V2.6-Pro-RL ukazuje, že **čínské modely už nebojují jen v segmentu „malých lokálních“ modelů** — Xiaomi staví 1T MoE s multimodálním vstupem a RL zaměřeným na sebezdokonalování. Pro ekosystém je klíčové, že licence je MIT: pokud se výsledky potvrdí, jde o vážného konkurenta pro uzavřené frontier modely v agentních úlohách.

---

*Zdroje: [MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmntwv/xiaomimimomimov26prorl_hugging_face/).*
