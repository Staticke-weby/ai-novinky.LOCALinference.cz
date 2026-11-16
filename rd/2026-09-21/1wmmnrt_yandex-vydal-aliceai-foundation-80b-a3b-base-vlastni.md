# 1wmmnrt

**Yandex vydal AliceAI-Foundation-80B-A3B-Base: vlastní architektura bez dodatečného doučování, ruští konkurenti Qwenu**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Iwaku_Real |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 218 / 181 |
| Model | https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmmnrt/yandexaliceaifoundation80ba3bbase/ |

## Co se stalo

Yandex publikoval **AliceAI-Foundation-80B-A3B-Base** — podle autora postu „**není to Qwen3 finetune**, je to vlastní architektura“ a jde o **base model bez post-trainingu**. Model je prezentován jako ruský konkurent Qwenu 35B a DeepSeeku V4 Flash na úrovni base modelů. **llama.cpp zatím nemá podporu**, takže lokální vyzkoušení znamená vLLM a podobné sestavy.

## Klíčová fakta

- 80B-A3B (aktivní 3B) — podle komentujících architektura ve stylu Qwen3-Next s Kimi Delta Attention.
- **Není dodatečně doučený** (jde o základní model) — tedy nepoužitelný pro chat nebo agentní workflow bez dalšího tréninku.
- Srovnáván s **Qwen 3.5 35B-A3B base**; Qwen 3.6 base checkpoint podle komentujících neexistuje.
- Detaily v článku na Habru: https://habr.com/ru/companies/yandex/articles/1083300/
- Diskuse: 218 skóre, 181 komentář (93 v balíčku).

## Citace

> „Není to finetune Qwen3, je to vlastně vlastní plně zakázková architektura. Zatím bohužel bez podpory Llama.cpp“ (překlad) — u/Iwaku_Real (OP)

> „(Všimněte si také, že **tento model NENÍ post-trénovaný** jako Qwen3.5/3.6)“ (překlad) — u/Iwaku_Real (OP)

> „Na první base model, který natrénovali od nuly, to vypadá docela slušně.“ (překlad) — u/Unhappy_Project_3723

> „Na Habru vysvětlili, že 3.5 zvolili, protože Qwen nezveřejnil base checkpoint pro 3.6.“ (překlad) — u/pand5461

> „Base model bez post-trénování, který poráží post-trénované modely v matematice IMO, je skutečně působivý.“ (překlad) — u/SquareBat780

> „Tohle je base model. Nemůžete ho používat v chatovém režimu ani v agentických workflow.“ (překlad) — u/quivering_palm

## Hlavní linky diskuse

- **Benchmarky base modelu vypadají dobře.** Několik lidí tvrdí, že i bez post-trainingu překonává starší DeepSeek V4 Flash s menším počtem parametrů.
- **Ale je to jen „papoušek“.** Hlavní protiargument: skutečná inteligence vzniká až v post-trainingu; base model se nedá použít jako produkt.
- **Metodologie srovnání.** Část diskuse obviňuje Yandex z nefér srovnání s Qwen 3.5 místo 3.6; jiní vysvětlují, že Qwen base pro 3.6 vůbec nepublikoval.
- **Bezpečnost a původ.** Několik komentářů doporučuje spouštět ruský model jen v uzavřeném sandboxu; jiní to odmítají jako předsudek.
- **Optimismus ohledně budoucí post-trénované verze.**

## Rozpory a neověřené informace

- **Rozpor:** je srovnání s Qwen 3.5 místo 3.6 klamavé, nebo jediné možné?
- **Rozpor:** predikuje silný base model i silný finální model? Příklad GigaChat 3.5 (dobrý pre-train, slabý po post-trainingu) je uváděn jako protiargument — neověřeno v balíčku.
- **Neověřené:** architektonické detaily (Kimi Delta Attention), výkon vs DeepSeek V4 Flash, tvrzení o nedostatku RL specialistů v Rusku.

## Proč to je důležité

Jde o **první vlastní base model Yandexu trénovaný od nuly** — tedy o signál, že se geopoliticky fragmentovaný AI trh posouvá od „finetunujeme čínské modely“ k vlastním pre-trainům. Pro praktické použití je dnes model nezajímavý (base, bez llama.cpp), ale jako indikátor schopností a jako základ pro budoucí post-training je to relevantní datový bod.

---

*Zdroje: [AliceAI-Foundation-80B-A3B-Base](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base), [Habr článek](https://habr.com/ru/companies/yandex/articles/1083300/), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmmnrt/yandexaliceaifoundation80ba3bbase/).*
