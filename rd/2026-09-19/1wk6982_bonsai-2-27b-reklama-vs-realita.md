# 1wk6982

**Bonsai 2 27B: reklama slibuje 98 % výkonu FP16 modelu, komunita ji odmítá jako vybírání třešniček**

| | |
|---|---|
| Subreddit | r/LocalLLM |
| Autor | u/AB172234 |
| Publikováno (Europe/Prague) | 19. 9. 2026, 01:43 |
| Skóre / komentáře | 152 / 140 |
| Odkaz | https://www.reddit.com/r/LocalLLM/comments/1wk6982/bonsai_2_27b_quantized_38_27b_98_intelligence_of/ |
| Další diskuse | [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1wkorli/i_tested_qwen38_27b_iq3_xxs_1018gib_vs_bonsai/) (81/96) · [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1wkwz69/ternarybonsai227bpq2_0_is_not_completely/) (71/40) |

## Co se stalo

Uživatel u/AB172234 zveřejnil na r/LocalLLM **screenshot reklamy na Ternary Bonsai 2 27B** a zeptal se, zda je pravda, že model dosahuje **98 % a více inteligence** plnohodnotné (FP16) verze. Reklama tvrdí, že Bonsai 2 27B si drží **98,2 % výkonu** plnopřesného protějšku při **9× menší velikosti** a **5,9 GB**, postavený na Qwen3.8 27B.

Odpověď komunity byla rychlá a jednoznačná — nejhlasitější komentáře zněly prostě **„Ne“** a „Nope“. Diskutující tvrdí, že číslo vzniklo **vybíráním vhodných testů** („benchmaxxing“) a že se v reálném nasazení nepotvrzuje. Objevují se konkrétní zkušenosti: rozbitá volání nástrojů, selhání skriptu v PowerShellu po pěti pokusech, zacyklení, ignorované instrukce a vynechané „jehly v kupce sena“ při testu dlouhého kontextu. Jeden z podrobnějších příspěvků nicméně uznává, že Bonsai 2 je na svou velikost velmi dobrý a překonává Qwen 3.6 27B — jen ne Qwen 3.8 27B v kvantizaci Q4 a výše.

## Klíčová fakta

- **Produkt:** Ternary Bonsai 2 27B, kvantizovaný (ternární) Qwen3.8 27B.
- **Marketingové tvrzení:** 98,2 % výkonu plné přesnosti, 9× menší nároky, 5,9 GB.
- **Reakce komunity:** tvrzení odmítnuto jako vybírání vhodných testů; horní komentáře odpovídají „ne“.
- **Nezávislé zkušenosti:** vynechané „jehly“ v testu dlouhého kontextu, selhání generování kódu, zacyklení, ignorované instrukce.
- **Reálné místo na trhu:** podle diskuse dobrá volba pro stroje s 8–12 GB VRAM, ale nikoli náhrada plného modelu.
- **Doplnění autora:** později přidal testovací video na YouTube a sám napsal, že 98,2 % je nejspíš hype.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Uváděná retence výkonu (reklama) | 98,2 % |
| Uváděná úspora velikosti (reklama) | 9× |
| Velikost modelu (reklama) | 5,9 GB |
| Parametry | 27 B |
| Retence podle whitepaperu (komentář) | 75 % („83 % v dobrý den“) |
| Test kontextu (komentář) | 2048 jehel, ~30 % vynecháno |
| Doporučená VRAM (diskuse) | 8–12 GB |
| Rychlost (komentář) | 30–40 tok/s |
| Skóre / komentáře postu | 152 / 140 |
| Komentářů v balíčku | 25 |

## Citace

> „… dosahuje 98,2% retence výkonu plnopřesného protějšku při 9× menší velikosti. Při pouhých 5,9 GB přináší silnější agentní kódování, multimodální uvažování a dlouhodobé používání nástrojů do lokálních zařízení. Postaveno na Qwen3.8 27B…“ (překlad) — reklama v přiloženém obrázku

> „Zajímalo by mě, jestli je tvrzení o 98 %+ inteligence modelu FP16 pravdivé, a jestli s tím má někdo zkušenost.“ (překlad) — u/AB172234, vlastní text postu

> „Ne, ty testy vyšperkují, jak se jim hodí. Spusťte si je sami a uvidíte.“ (překlad) — u/DataGOGO

> „Ale pokud dokážete spustit 3.8 27B v Q4 nebo výše, Bonsai 2 není v žádném ohledu náhrada.“ (překlad) — u/Old_Restaurant_2216

> „To 98,2 % se zatím jeví jako hype.“ (překlad) — u/AB172234, dodatečný komentář autora

> „Požádal jsem ho, ať napíše skript v PowerShellu, který spočítá všechna prvočísla mezi 1 a 1000. Nedokázal vygenerovat syntakticky správný kód.“ (překlad) — u/AlanBarber

## Co říkají komentáře

Vlákno je pozoruhodné **jednomyslností**: tvrzení o 98 % odmítá drtivá většina diskutujících a nejlépe hodnocené odpovědi jsou jednoslovné. Argumenty se opírají o tři věci: číslo pochází z **vybraných testů**, nezávislé testy ukazují nižší retenci (jeden komentující odkazuje na whitepaper s 75 %), a v praxi se objevují konkrétní selhání — kód, volání nástrojů, dlouhý kontext. Menšinový, ale věcný hlas uznává, že jde o **dobrý model pro malé VRAM** a že překonává starší generaci Qwen 3.6 27B; spor tedy není o kvalitě modelu, ale o **reklamním čísle**.

## Rozpory a neověřené informace

- **Neověřené tvrzení (reklama):** 98,2% retence výkonu plné přesnosti při 9× menší velikosti a 5,9 GB.
- **Neověřené tvrzení:** u/Purple-Subject1568 uvádí, že zveřejněný whitepaper ukazuje 75 % zachované schopnosti — v podkladu není doloženo.
- **Neověřené tvrzení:** u/ireallydontcare00 ironicky tvrdí, že z modelu odstranili všechna data kromě těch potřebných k projití benchmarků.
- **Neshoda:** u/Old_Restaurant_2216 považuje Bonsai 2 za výborný na svou velikost a lepší než Qwen 3.6 27B, většina ostatních ho označuje za slabý nebo přeceňovaný.
- **Neshoda:** reklama tvrdí 98,2 %, komentující uvádějí 75 % (resp. „83 % v dobrý den“) a vynechané jehly v kontextovém testu.

## Proč to je důležité

Případ je učebnicová ukázka toho, **jak se dnes marketing kvantizovaných modelů ověřuje**. U lokálních modelů je klíčové číslo „kolik procent výkonu plné přesnosti zůstalo“ — a právě to je metrika, kterou lze snadno nafouknout volbou testů. Komunita na to reagovala rychle a konkrétně, což je pro uživatele s malou VRAM praktičtější než samotná reklama: model je použitelný, ale **rozhoduje velikost paměti, ne procento z reklamy**.

## Zdroje

- https://www.reddit.com/r/LocalLLM/comments/1wk6982/bonsai_2_27b_quantized_38_27b_98_intelligence_of/
- přepis přiloženého obrázku (reklama na Ternary Bonsai 2 27B)
- komentáře: `2026-09-19/_data/raw/comments.json` (klíč `1wk6982`), balíček `2026-09-19/_data/bundles/1wk6982.md`
