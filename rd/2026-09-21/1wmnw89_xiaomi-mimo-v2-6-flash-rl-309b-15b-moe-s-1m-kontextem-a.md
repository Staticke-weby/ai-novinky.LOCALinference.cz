# 1wmnw89

**Xiaomi MiMo-V2.6-Flash-RL: 309B/15B MoE s 1M kontextem a licencí MIT — „nový lokální král“, ale 178 GB nativně**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Bestlife73 |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 471 / 120 |
| Model card | https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmnw89/xiaomimimomimov26flashrl_hugging_face/ |

## Co se stalo

Tým Xiaomi MiMo zveřejnil na Hugging Face **MiMo-V2.6-Flash-RL** pod licencí **MIT** — „efficiency-balanced checkpoint“ řady MiMo-V2.6, zaměřený na **škálování RL směrem k sebezdokonalování** (mixed RL, asynchronní GRPO, „groupwise agentic grading“).

Současně vyšel i vlajkový sibling **MiMo-V2.6-Pro-RL** a destilát **MiMo-V2.6-Distill-Qwen-9B**. Na Redditu to vyvolalo vlnu: „nový lokální král“, „open weight flash challenger“.

## Architektura a čísla

- **Sparse MoE: 309B total / 15B aktivovaných parametrů** (Pro: 1,02T total / 42B aktivních).
- **1M tokenů kontext**, multimodální vstup: text, obrázky, video, audio.
- Nativní velikost **178 GB**; komentující hlásí FP8/mixed kvantizaci, HF metadata jsou podle nich nespolehlivá.
- Trénink RL: **1 568 promptů × 16 rolloutů na krok**; vision encoder 681M, audio tokenizer 308M + audio patch encoder 127M, 5vrstvý spekulativní (MTP) dekodér.
- Benchmarky (Pro / Flash): DeepSWE v1.1 **71,9 / 67,9**, Terminal Bench 2.1 **89,9 / 87,6**, OSWorld-Verified **82,0 / 80,8**, CyberGym **94,0 / 95,1**, Toolathlon-Verified **76,9 / 73,6**.
- Nasazení: SGLang a vLLM, doporučené `temperature=1.0`, `top_p=0.95`; dostupné i v AI Studio, MiMo Code, Desktop, Open Platform API a na OpenRouteru.
- Komentující uvádějí API cenu: **$0,0028 cached / $0,14 / $0,28** (za milion tokenů).

## Citace

> „MiMo-V2.6-Flash-RL je efektivitou vyvážený checkpoint řady MiMo-V2.6.“ (překlad) — Xiaomi MiMo Team

> „1M kontext, text/obraz/video/audio na vstupu, SWA/GA 39/9, MTP/DFlash, 178GB nativní velikost. Mohl by se hodit pro 128GB zařízení – kvantovaný“ (překlad) — u/harpysichordist

> „Xiaomi přešlo od rýžovarů k reasoning modelům rychleji, než většina AI startupů přešla od pitch decku k produktu.“ (překlad) — u/FlightUsed648

> „Objevuje se nový open weight flash vyzyvatel! Vážně, čím víc, tím líp“ (překlad) — u/happycube

## Hlavní linky diskuse

- **Velikost vs lokální hardware.** 178 GB nativně znamená, že na 128GB strojích jde jen kvantizovaně — a část komentujících varuje, že model už je v mixed/4bit podobě a další tlak kvalitu srazí.
- **Sesterské modely.** Lidé okamžitě odkazují na Pro verzi a 9B destilát; objevuje se i odkaz na živě streamovaný RL dashboard Xiaomi.
- **Konkurenceschopnost.** „Některá skóre benchmarků jsou na úrovni Fable 5, wow“ (překlad); jinde tvrzení, že Pro vede nad Kimi K3 ve 14 z 15 benchmarků (komentář, nikoli ověřený fakt).
- **Nadšení z open weights** napříč vláknem.

## Rozpory a neověřené informace

- **Počet parametrů:** model card říká 309B total / 15B aktivních, jeden komentující tvrdí 159B — rozpor bez zdroje.
- **Kvantizace:** „půjde kvantizovat na 128 GB“ vs „už je kvantizovaný, další škrty ublíží“.
- **Neověřené:** Pro = 1,02T/42B a vede nad Kimi K3 v 14/15 benchmarků; API ceny od komentujícího; spekulace, že vydání načasovali na dokončení plánovaných RL kroků.

## Proč to je důležité

Je to **nejsilnější open-weight multimodální release dne** — a zároveň test hranice „lokálnosti“: model je otevřený (MIT), ale 178 GB znamená, že většina uživatelů ho reálně spustí jen přes API nebo agresivní kvantizaci. Pokud benchmarky drží, jde o přímý útok na pozici Qwen/DeepSeek v segmentu agentic coding modelů.

---

*Zdroje: [MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmnw89/xiaomimimomimov26flashrl_hugging_face/).*
