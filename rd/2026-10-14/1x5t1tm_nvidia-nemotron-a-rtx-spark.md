# 1x5t1tm
**NVIDIA uvádí Nemotron Bolt 3.5 74B a superčip RTX Spark**

r/LocalLLaMA · u/CulturalKing5623 · 14. října 2026, 16:42 · 615 bodů / 167 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x5t1tm/)

Uživatel u/CulturalKing5623 přinesl do r/LocalLLaMA zprávu o novém lokálním modelu od Nvidie. Nemotron 3.5 Bolt 74B je směs expertů se 74 miliardami parametrů, z nichž se na jeden krok používá 9 miliard, a díky 2bitové kvantizaci s tréninkem vědomým kvantizace se má vejít do 24 GB. Podle popisu má být rychlejší než většina oblíbených hustých modelů a zároveň chytřejší než srovnatelně velká MoE.

Firemní blog ho představuje jako model stavěný na míru novému superčipu RTX Spark, který má spojit herní počítač, kreativní studio a osobní AI superpočítač s až 128 GB sjednocené paměti a výkonem 1 PFLOPS pro lokální agenty. Při startu má běžet přes llama.cpp, vLLM, Ollama, Unsloth a LM Studio i přímo v agentech Hermes a OpenClaw a jako ostatní Nemotrony má být plně otevřený včetně trénovacích dat, vah a receptů. Menší sourozenec E4B 4GB pro herní postavy v rámci NVIDIA ACE má následovat 23. října.

Diskuse se nese v opatrném tónu, protože Nvidia podle komunity zatím nevydala jeden užitečný model, jak píše v nejvýše hodnoceném komentáři u/Embarrassed_Adagio28. Na to navazuje u/laser50, podle kterého Nemotron Ultra patří k nejhorším funkčním modelům, jaké zkoušel, a kód i změny mu kazil víc než ostatní agenti dohromady, a u/Eyelbee si klade otázku, jestli tohle bude také propadák. Nízká očekávání shrnuje u/MrHumanist: pokud bude mít tři čtvrtiny kvality Qwen 3.8 27B, možná to zkusí.

Největší otazník visí nad výchozí 2bitovou kvantizací. u/atape_1 se ptá, jestli vyjdou i normální kvantizace, nebo je dvojka konečná, a u/n8mo se 16 GB grafické a 64 GB operační paměti přiznává, že ho právě dvojka odradila. Opačný pól drží u/ComplexType568 a u/MerePotato: prvního potěšilo, že velká laboratoř sází na nízko-bitové kvantizace, což by mohlo inspirovat i Qwen, DeepSeek nebo Google, druhý v úspěšném tréninku vědomém kvantizace vidí možný zlom. Věcně to rámuje u/GasSmooth7439 – když 2bit obstojí, bude to pro lokální uživatele ideální střed mezi kapacitou expertů a pamětí jedné spotřebitelské karty.

Právě velikost ale mnohé láká. u/Real_Ebb_7417 slaví, že po dlouhém čekání přichází 80B MoE, u/NickReese přiznává, že ho 74B těší víc, než čekal, protože tahle velikost byla dlouho zanedbávaná, a u/Long_comment_san tvrdí, že 80B modely jsou téměř ideální pro běžné 64GB sestavy, zatímco 120B nedávají smysl. Do toho zapadá i poznámka u/jacek2023, že nepřichází jeden, ale hned dva Nemotrony včetně 120B A12B, a praktické přání u/james_pic, aby menší E4B konečně překonal Gemma 4.

Čtenář si tak odnese jednoduchý vzkaz: papírově zajímavá kombinace velikosti a paměti, jejíž pověst rozhodne až to, jak přežije 2bit v reálných testech.
