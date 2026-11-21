# 1y0vaey
**Tencent otevřel Hy4. Multimodální model má 770 miliard parametrů a kontext milion tokenů**

r/LocalLLaMA · u/ResearchCrafty1804 · 20. listopadu 2026, 06:27 · 365 bodů / 70 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y0vaey/)

Tencent zveřejnil váhy modelu Hy4, své nativně multimodální vlajkové lodi postavené na architektuře MoE. Model má celkem 770 miliard parametrů, z nichž je aktivních 49 miliard, a kontext až milion tokenů. Spolu s vahami vyšel repozitář na GitHubu, model na Hugging Face včetně GGUF varianty, licence i podrobná system card.

Komunitu nejvíc vystihuje nejvýše hodnocená reakce u/Bagelsarenakeddonuts: výkon je pěkný, ale na většinu lokálních sestav je model pořádně macatý. Přesně kolem toho se točí celé vlákno — papírově jde o špičku, prakticky o stroj, na který má doma málokdo. Uživatel u/Dense-Ad6315 to shrnuje stroze, že na provoz ani v nízké kvantizaci nemá peníze, a u/yanhua_lab se ptá, jestli by to utáhl 32GB MacBook.

Z věcnější části diskuse vyplývá, kam si lidé Hy4 zařazují. U/twack3r ho vidí jako ideálního nástupce místa, které v jeho sestavě drží GLM 5.3, a rovnou se ptá, zda je stejně omezený v kybernetických schopnostech jako Qwen 4 a Kimi K3.1. U/segmond připomíná, že už preview verze byla dost dobrá a novinka se v řadě testů drží modelu Kimi K3.1. Technicky nejzajímavější je postřeh u/IngwiePhoenix, podle kterého je právě 49 miliard aktivních parametrů nadějí pro dual-GPU sestavy se streamováním expertů MoE.

Nejobsáhlejší kontext přinesl u/Dolphin_research. Zajímavé je podle něj načasování: vedení Tencentu na hovoru k výsledkům za třetí čtvrtletí uvedlo, že Hy4 už má významný podíl využití ze zahraničí a firma ho chce globálně tlačit přes inferenční partnery, zatímco nová čipová pravidla mohou protáhnout další trénink. Levnější Hy4 Flash za dvacetinu ceny je podle něj už teď nejvytíženějším letošním modelem podle denních tokenů na OpenRouteru. Otevřené váhy tak čte jako distribuční plán: nechat model servírovat ostatní hosty v zahraničí, když je vlastní výpočetní kapacita napjatá, což zároveň znamená, že tahle verze tu s námi bude delší dobu.

Mezitím si vlákno dělá legraci samo ze sebe. Objevují se hned dvě otázky, jestli to poběží na Pentiu, konkrétně od u/rinmperdinck a u/Onkel-Thomas. Nováček u/Pogchumpinnitbruv se ptá, co vydání prakticky znamená, a u/Othun prosí jen o jediné, aby autor grafů příště zachoval stejné pořadí v benchmarcích.

Hy4 tak na r/LocalLLaMA působí jako model, který lidé chtějí zkoušet, ale většinou raději u někoho jiného na serveru.

---

**Další diskuse:**

- [r/LocalLLaMA – 275 bodů, 406 komentářů](https://www.reddit.com/r/LocalLLaMA/comments/1y15w4a/)
- [r/LocalLLaMA – 257 bodů, 80 komentářů](https://www.reddit.com/r/LocalLLaMA/comments/1y0ofce/)

[Zpět na index](00-index.md)
