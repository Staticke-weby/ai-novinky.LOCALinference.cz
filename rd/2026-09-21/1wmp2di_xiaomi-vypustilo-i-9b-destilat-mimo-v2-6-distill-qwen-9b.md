# 1wmp2di

**Xiaomi vypustilo i 9B destilát: MiMo-V2.6-Distill-Qwen-9B zlepšuje Qwen3.5-9B hlavně v agentních úlohách**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/VoiceApprehensive893 |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 270 / 69 |
| Model card | https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmp2di/xiaomimimomimov26distillqwen9b/ |

## Co se stalo

Vedle velkých modelů MiMo-V2.6 vydalo Xiaomi i **9B model** vzniklý **doučením s učitelem (supervised fine-tuning) na Qwen3.5-9B a MiMo-generovaných datech**. Karta modelu uvádí pokrytí kódování, obecných agentních úloh, vizuálního kódování a kyberbezpečnosti; autoři ho popisují jako „výchozí bod pro otevřený výzkum agentního posilovaného učení“ (překlad).

Reakce komunity: překvapení z rychlosti oficiálního vydání („we're so back?!?“), okamžité dotazy na GGUF kvantizace a žádosti o 35B variantu.

## Čísla a zlepšení

- SFT datová směs: **77,4 B tokenů celkem, z toho 27,2 B „loss-bearing“** (Code 23,2 B / 29,9 %, Cyber 11,0 B / 14,2 %, General 22,0 B / 28,5 %).
- Proti Qwen3.5-9B: **SWE Pro avg@3 32,0 → 44,6**; **AutomationBench 5,0 → 30,3**; **Terminal Bench 2.1 27,0 → 37,1**; **MiMo Code (mini) 19,5 → 51,6**; **MiMo Cyber (mini) 5,7 → 31,3**; MiMo General (mini) 28,5 → 62,2.
- Licence MIT, úloha „image-text-to-text“, 804 stažení / 301 lajků v době sběru.
- Nasazení: SGLang s `--reasoning-parser mimo`, dotaz s `enable_thinking=True`.

## Citace

> „MiMo-V2.6-Distill-Qwen-9B je 9B agentický model vyvinutý Xiaomi MiMo pomocí supervizovaného doladění Qwen3.5-9B na datech vygenerovaných MiMo.“ (překlad) — Xiaomi MiMo Team

> „Tento SFT checkpoint vydáváme jako výchozí bod pro otevřený výzkum v agentickém posilovaném učení.“ (překlad) — Xiaomi MiMo Team

> „Tohle jsem nečekal lol můžeme dostat i 35B A3B?“ (překlad) — u/Atretador

> „Docela výrazné zlepšení. RL verze je na svou velikost teď pravděpodobně SOTA.“ (překlad) — u/ResearchCrafty1804

> „Tohle je jen sft, takže nebude moct konkurovat ornith (který má RL)“ (překlad) — u/Suspicious_Moment_87

> „model se při volání jakéhokoli nástroje neustále zacyklil. Možná problém se šablonou chatu, nevím“ (překlad) — uživatel v komentářích

## Hlavní linky diskuse

- **GGUF, prosím.** Nejčastější požadavek: lidé chtějí kvantizace pro lokální běh.
- **SFT vs RL.** Komentující upozorňují, že jde jen o SFT checkpoint a že bez RL verze model neporazí konkurenci trénovanou RL.
- **Problémy s tool-cally.** Dva uživatelé hlásí neustálé opakování (looping) při volání nástrojů; jeden to přičítá chat template, jiný tvrdí, že s alternativní šablonou nástroje fungují.
- **Chuť po 35B variantě.**

## Rozpory a neověřené informace

- **Reportovaný bug s loopingem nástrojů** je nekonzistentní: část uživatelů ho má, část ne — otevřená otázka kvality šablony.
- Neověřené: tvrzení, že RL verze je „SOTA pro svou velikost“, že RL verze SFT „drtí“, a že problémy s voláním nástrojů řeší alternativní šablona chatu.

## Proč to je důležité

Destilát je pro lokální scénu často praktičtější než 309B/1T modely: **9B model, který se dá reálně spustit, s MIT licencí a velkými skoky v agentních benchmarcích**. Zároveň ukazuje nový standard „open research“ release: firma pustí SFT checkpoint, aby komunita dotrénovala RL — což je zajímavý hybrid mezi open-source a vlastním výzkumem.

---

*Zdroje: [MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmp2di/xiaomimimomimov26distillqwen9b/).*
