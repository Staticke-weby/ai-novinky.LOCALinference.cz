# 1xjfuqh
**Unsloth vydal GGUF kvantizace DeepSeek-V4.1 Flash. Přesnost obhajuje 16 běhy AIME**

r/LocalLLaMA · u/danielhanchen · 30. října 2026, 14:48 · 346 bodů / 99 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xjfuqh/)

Unsloth zveřejnil nové GGUF kvantizace DeepSeek-V4.1-1017 Flash označené jako Dynamic V3.1 (preview) pro lokální běh. Tvrdí, že si ze všech srovnávaných variant drží nejvíc přesnosti na sedmi benchmarcích a téměř ve všech metrikách překonávají konkurenční kvantizace ISTA GSQ-RCO. Model se má vejít do 128 GB RAM nebo unified memory, s odkládáním n-gramů pak i na stroje se 64 GB.

Největší rozpor hlásí u AIME25, kde konkurence mluvila o stoprocentním zotavení přesnosti oproti základu, ale Unsloth v vlastních testech naměřil jen 91,88 procenta. Každý benchmark proto běžel nejméně třikrát a AIME25 dokonce šestnáctkrát, výsledky pak průměroval do tabulky od 508GB varianty Q8_K_XL až po 233GB variantu IQ1_S. Metodiku, data i grafy dal k dispozici na blogu a slibuje další výsledky příští týden, vedle toho vysvětluje KLD jako míru věrnosti logitů a přiznává, že nižší bity přemýšlejí o něco déle než nekvantovaný model.

Diskuse se nejdřív stočila k hardwaru a úlevnému humoru. u/NoFunk prosí, ať mu neberou tu tenkou výmluvu pro extravagantní nákupy železa, u/Frail_Waif hlásí vyhlášenou válku citátem o třikrát rychlejší inferenci a dodává, že teď jen potřebuje víc RAM. u/keepthepace to shrnuje střízlivěji, že za 128 až 145 GB paměti má člověk doma v podstatě frontier model, což by za jiných okolností mělo pro velké laboratoře hodnotu stovek miliard.

Jádro debaty ale patří číslům. u/RealFullMetal ukazuje na řádek Q2_K_XL, který má průměr 87,49 proti 87,68 u Q8, tedy o třetinu méně místa na disku za méně než pětinu bodu. Právě to, že menší Q2 na AIME poráží větší Q8, vrtá hlavou hned dvěma hlasům: u/Gullible_Implement36 se ptá, jestli je to jen rozptyl běhů, nebo kvantizace občas věci paradoxně uvolní, u/Chromix_ v tom vidí důkaz, že rozdíl dvou procent na přesycených a zašuměných benchmarcích bez opakování moc neznamená.

Nechybí ani konstruktivní rýpnutí do formy oznámení. u/keyboardhack by chtěl přímé srovnání nové verze 3.1 se starou 3.0, aby příspěvek stál víc na vlastním zlepšení než na souboji s GSQ-RCO. Podobně u/No_Weather8173 oceňuje práci, ale pro příště prosí o méně přesycené testy, protože kromě Aideru mu přijdou všechny dost nezajímavé. u/GodComplecs to uzavírá smířlivě, že náskok je v praxi tenký a běžný uživatel dobrý a výborný kvant sotva rozezná, o to víc se mu ale líbí, že konkurence nenechává Unsloth usnout na vavřínech.
