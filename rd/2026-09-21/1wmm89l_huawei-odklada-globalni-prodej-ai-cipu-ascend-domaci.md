# 1wmm89l

**Huawei odkládá globální prodej AI čipů Ascend: domácí poptávka převyšuje kapacitu, Atlas škáluje na 15 488 čipů**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/fallingdowndizzyvr |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 320 / 59 |
| Článek | https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wmm89l/huawei_shelves_global_ai_chip_rollout/ |

## Co se stalo

Tom's Hardware (Anton Shilov, 21. 9. 2026) informuje, že **Huawei nebude nabízet AI akcelerátory řady Ascend 900 globálně**, ale prakticky jen v Číně. Důvod podle rotujícího předsedy **Erica Xu** (Huawei Connect): „nemáme dost kapacity ani uspokojit poptávku v Číně“, proto firma neplánuje plnohodnotnou mezinárodní expanzi — jen limitované objemy do několika zemí s velmi silnou poptávkou.

## Technický kontext z článku

- **Atlas SuperPoD/SuperCluster** škáluje až na **15 488 NPU Ascend 960**, s optickým propojením (NPO), které kompenzuje nižší výkon jednotlivých čipů.
- Uváděné hodnoty: až **30 FP8 EFLOPS** a **120 FP4 EFLOPS** v clusteru; pro Atlas 950 SuperCluster 524 FP8 ExaFLOPS (trénink) a 1 FP4 ZettaFLOPS (inference).
- Roadmapa: **960DT/960PR v roce 2027**, Ascend 970 (2028), Ascend 980 (2029) — s cíli 2/4/8 PFLOPS FP8/FP4 u 960 a 14, resp. 28 PFLOPS FP4 u 970/980.
- Srovnání: Nvidia H200 4 PFLOPS FP8, B300 10 PFLOPS FP8, R200 17,5 PFLOPS FP8 — Huawei dohání **škálováním systému**, ne výkonem čipu, a zaostává ve výkonu na watt; SMIC navíc tápe s 7nm/6nm výrobou.

## Citace

> „Protože nemáme dost kapacit ani na uspokojení poptávky v Číně, nemáme v plánu plnohodnotně expandovat na mezinárodní trh.“ (překlad) — Eric Xu, Huawei

> „AMD a Nvidia si už nemusí dělat starosti.“ (překlad) — Tom's Hardware

> „Stejně jako si západní konkurenti nemuseli dělat starosti s BYD nebo jinými čínskými elektromobily. Chvíli to tak bude a pak už ne.“ (překlad) — u/AGM_GM (skóre 110)

> „Formulace o „odložení globálního uvedení“ skrývá dobrou zprávu: domácí poptávka je tak vysoká, že jim nezbývají čipy na prodej do zahraničí. To je problém se zásobováním, který stojí za to mít.“ (překlad) — u/Elouakili_Flexy

> „Nvidia a AMD si starosti nedělají, my spotřebitelé ano.“ (překlad) — u/MotokoAGI

> „Jimi uváděné fp4 flops jsou na úrovni B200! I když předpokládám, že propustnost paměti je mnohem nižší.“ (překlad) — u/JustTellingUWatHapnd

## Hlavní linky diskuse

- **„Přijde to jako s EV.“** Nejsilnější linka: západní konkurence se nemusí bát, dokud se nemusí — a pak najednou ano (paralela BYD).
- **EUV a Tchaj-wan.** Komentující diskutují nezávislost Číny na ASML/EUV a geopolitické důsledky; jiní namítají, že sankce kvůli Tchaj-wanu by Čínu tvrdě zasáhly bez ohledu na čipy.
- **Je to dobrá zpráva.** Domácí poptávka tak vysoká, že nezbyde na export = kapacitní, ne poptávkový problém.
- **Spotřebitelé.** Obavy, že bez konkurence porostou ceny Nvidie/AMD; naděje na levnější GPU.

## Rozpory a neověřené informace

- **Rozpor:** odklad je jen kvůli domácí poptávce, nebo i proto, že o čipy v zahraničí nikdo nestál (u/throwawayacc201711)?
- **Rozpor:** dopad na ceny GPU — uvolnění trhu pro spotřebitele vs „jsme v háji, my spotřebitelé“.
- **Neověřené:** tvrzení, že čínský EUV prototyp už existuje (odkaz na Reuters); spekulace o zaplavení trhu čínskými čipy a o Tchaj-wanu.

## Proč to je důležité

Pro AI ekosystém je klíčové, že **čínská poptávka po vlastních čipech je tak velká, že pohlcuje celou produkci** — to je strukturální signál o velikosti tamního tréninkového úsilí. Současně článek ukazuje, že Huawei dohání Nvidii **architekturou clusterů a optikou**, ne výkonem čipu: to je jiná technologická cesta, jejíž limity (propustnost paměti, výkon/watt) zatím nejsou překonané.

---

*Zdroje: [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wmm89l/huawei_shelves_global_ai_chip_rollout/).*
