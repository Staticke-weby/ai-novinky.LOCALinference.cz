# 1wlsaoq

**Ternary Bonsai 2 27B: téměř špičkový výkon a přitom se vejde do 8 GB VRAM**

| Položka | Hodnota |
|---|---|
| Subreddit | r/LocalLLM |
| Autor | u/37Scorpions |
| Čas | 20. 9. 2026 22:41 (Europe/Prague) |
| Skóre | 223 |
| Komentáře | 148 |
| Odkaz | https://i.redd.it/ztxmob1ukqqh1.jpeg |
| Diskuse | https://www.reddit.com/r/LocalLLM/comments/1wlsaoq/ternary_bonsai_2_27b_near_top_performance_while/ |

## Co se stalo
Uživatel u/37Scorpions zveřejnil v r/LocalLLM příspěvek s vlastním srovnávacím testem modelu Ternary Bonsai 2 27B od firmy PrismML. Podle autora jde o model třídy 27B, který je tentokrát velký přibližně 7 GB a vejde se celý do 8 GB VRAM grafické karty RTX 4060. Předchozí Bonsai 27B byl podle něj kvantován na Q1 s tréninkem citlivým na kvantizaci, díky čemuž běžel ve 4 GB a přesto byl „docela chytrý“. U Ternary Bonsai 2 27B si autor přesnou velikost není jistý.

Autor doplňuje praktickou poznámku: aby model v LM Studio vůbec běžel, musel si sestavit fork llama.cpp od PrismML a ten použít. Postup mu prý zabral několik hodin. V komentáři později popsal i to, jak v LM Studio vyměnit soubory llama.dll a ggml.dll za verzi z forku (s upozorněním, že je nutné složku nejprve zálohovat).

Srovnávací test (benchmark) je autorův vlastní a amatérský. Autor sám uvádí, že není expert na benchmarky, ale hobbyista, který se snaží vytěžit užitečné informace pro lidi s podobným hardwarem. Testuje pouze modely běžící na spotřebitelském hardware – konkrétně na 8GB RTX 4060 a 16 GB RAM. Všechny modely měří s vypnutým uvažováním („thinking“) a s limitem odpovědi 4096 tokenů; delší odpověď podle něj vždy znamená, že se model zacyklil. Otázky si vytvořil sám a výsledky vyhodnocoval ručně.

Hlavní graf v obrázku řadí Ternary Bonsai 2 27B PTQ1 na druhé místo, hned za model Ministral3 14B Q4_K_M. Autor uzavírá, že model si v jeho testu vedl dobře, ale praktické nasazení teprve otestuje – chce na nějakou dobu přesunout všechny své AI potřeby na Bonsai a průběžně o tom informovat. Zároveň se ptá ostatních, jaké mají s Bonsai 2 zkušenosti, protože slýchá, že je v praxi špatný.

## Klíčová fakta
- Ternary Bonsai 2 27B je model třídy 27B od firmy PrismML, velký přibližně 7 GB, který se má vejít celý do 8 GB VRAM karty RTX 4060.
- První Bonsai 27B byl kvantován na Q1 s kvantizací citlivou na trénink a běžel ve 4 GB.
- Pro běh Ternary Bonsai 2 v LM Studio je podle autora nutné sestavit fork llama.cpp od PrismML a použít jeho knihovny.
- Autorův vlastní test má 18 otázek v 6 kategoriích (všeobecné znalosti, matematika, programování, výdrž, logické hádanky, prostorové uvažování).
- Všechny modely testuje s vypnutým myšlením a limitem odpovědi 4096 tokenů.
- V přiloženém grafu je Bonsai2 Ternary 27B PTQ1 druhý, hned za Ministral3 14B Q4_K_M.
- Jeden z komentujících (u/SamTanna) hlásí běh modelu PQ2_0 27B na 12GB RTX 4070 rychlostí přibližně 42–50 tok/s, s podporou vidění a strukturovaných volání nástrojů a s kontextem 32K.

## Čísla
- 223 – skóre příspěvku.
- 148 – počet komentářů u příspěvku.
- 27B – třída modelu Ternary Bonsai 2.
- 4 GB – velikost, do níž se vešel první Bonsai 27B díky kvantizaci Q1.
- ~7 GB – přibližná velikost modelu Ternary Bonsai 2 27B podle autora (sám uvádí, že si není jistý).
- 8 GB – VRAM karty RTX 4060, do níž se má model vejít celý.
- 16 GB – operační paměť testovacího počítače autora.
- 18 – počet otázek v autorově testu.
- 6 – počet kategorií otázek.
- 4096 – limit tokenů na odpověď v testu.
- 42–50 tok/s – rychlost, kterou u modelu PQ2_0 27B na 12GB RTX 4070 hlásí komentující u/SamTanna (tvrzení komentujícího).
- 32K – kontext, se kterým podle u/SamTanna model běžel (tvrzení komentujícího).
- 12 GB – VRAM karty RTX 4070 v testu komentujícího u/SamTanna.
- 7000 tokenů – spotřeba jednoho neúspěšného pokusu o naprogramování hry Flappy Bird (tvrzení komentujícího u/Low_Bet_8805).
- 6 GB VRAM a 28 GB DDR5 – konfigurace, kterou pro běh MoE modelu Qwen 3.6 35B A3B Q4 uvádí komentující u/No-Business5854 (tvrzení komentujícího).
- 187 – skóre nejhlasitějšího komentáře (u/EasterElk).

## Citace
> „Tentokrát jde o ~7GB model, který vykazuje úžasnou inteligenci a přitom se vejde celý do 8 GB VRAM karty RTX 4060.“ (překlad) — u/37Scorpions

> „Pokud si ho chcete spustit sami, budete muset sestavit fork llama.cpp od PrismML.“ (překlad) — u/37Scorpions

> „Ternary Bonsai2 27B si v mém testu vede docela dobře, což často odpovídá i mému osobnímu názoru, ale budu ho muset otestovat v praxi.“ (překlad) — u/37Scorpions

> „Tento model je v praxi k popukání špatný. Plete si věci, zacykluje se, rozpadá se a dělá špatná rozhodnutí.“ (překlad) — u/EasterElk

> „Můj závěr je, že Bonsai funguje a na 12 GB funguje překvapivě dobře, ale není dost spolehlivý na to, aby byl hlavním mozkem univerzálního agenta bohatého na nástroje.“ (překlad) — u/SamTanna

> „Tento model – a rodina Bonsai obecně – je dokonalým příkladem toho, co je benchmaxxing, a proč benchmarky absolutně *nejsou* reprezentativní pro skutečný výkon modelu.“ (překlad) — u/Kodix

## Co říkají komentáře
- **Model je v praxi špatný nebo nepoužitelný i přes výsledky benchmarků.** Téma podporuje mnoho nejvýše hodnocených komentářů (u/EasterElk se skóre 187, dále u/Human_Information561, u/HumbleMemeFarm, u/RedWolf_HU, u/den0rk, u/wednesdaywoe13). Uvádějí zmatené odpovědi, zacyklení, halucinace a rozpad projektů.
- **Selhává u agentního a nástrojového použití a v multi-turn práci.** Vychází z podrobného testu komentujícího u/SamTanna a navazujících reakcí o selháních nástrojových smyček; model podle nich najde odpověď brzy, ale pokračuje ve zkoumání, dokud nevyčerpá kontext.
- **Metodika benchmarků je bezcenná / jde o benchmaxxing.** Téma zastávají u/alpacadaver, u/Kodix, u/PestiferousGamer a u/ethereal_intellect. Kritizují zejména testování modelu pro hluboké uvažování s vypnutým myšlením a domněnku, že výsledek testu vypovídá o skutečném výkonu.
- **Jiné malé modely nebo MoE jsou lepší alternativou.** Srovnání s modely Qwen, Mistral a Gemma uvádějí u/No-Business5854, u/Invader-Faye a u/PeterPorox.
- **Výměna knihoven v LM Studio.** Samostatně se objevuje poděkování autorovi za poznámku o LM Studio (u/darthrobe) a návod autora, jak nahradit soubory llama.dll a ggml.dll z forku.

## Rozpory a neověřené informace
- **Rozpor mezi autorem a komentujícími:** autor tvrdí, že Ternary Bonsai2 27B podává téměř špičkový výkon v benchmarku a má úžasnou inteligenci v 8 GB VRAM, zatímco většina komentujících označuje model za nepoužitelný, zacyklující se a v praxi se rozpadající.
- **Rozpor v relativním pořadí:** komentující u/Invader-Faye uvádí, že model je lepší než Gemma 12 a Qwen 3.5 9B, ale horší než Qwen 3.8 27B Q2; u/PeterPorox se ptá, zda je stále lepší Ministral 3 14B, což odpovídá grafu, v němž vede Ministral3 14B.
- **Neověřené tvrzení autora:** sám autor uvádí, že si u Ternary Bonsai 2 27B není jistý („nejsem si přesně jistý“), pokud jde o velikost ~7 GB a úžasnou inteligenci vejít se do 8 GB VRAM. Jde o tvrzení autora, ne o ověřený údaj.
- **Neověřené:** žebříčky v přiloženém grafu jsou autorův vlastní ručně vyhodnocený test, nikoli nezávislý benchmark.
- **Neověřené tvrzení komentujícího (u/No_Delay_319):** že „udržení výkonu“ u kvantizace Q1 vydrží jen asi tři prompty a pak model hloupne.
- **Neověřené tvrzení komentujícího (u/Holiday_Point_603):** že přetrénované modely si drží solidní výkon i přes extrémní kvantizace a že většina dnešních benchmarků je taková.
- **Neověřená hodnocení komentujících:** stížnosti na zacyklení, halucinace a selhání v praxi jsou osobní zkušenosti jednotlivých komentujících, nikoli měření.

## Proč to je důležité
Ternární kvantizace je jedním ze způsobů, jak dostat modely třídy 27B na hardware, který si běžný uživatel skutečně může dovolit – zde 8GB RTX 4060. Příspěvek ale zároveň ukazuje propast mezi výsledky vlastního benchmarku a zkušenostmi z praxe: zatímco v testu se model drží na druhém místě, řada komentujících ho označuje za nepoužitelný pro skutečnou práci a zejména pro agentní úlohy s nástroji. Diskuse je tak i příkladem skeptického vztahu části komunity k benchmarkům a k pojmu „benchmaxxing“.

## Zdroje
- https://www.reddit.com/r/LocalLLM/comments/1wlsaoq/ternary_bonsai_2_27b_near_top_performance_while/
- https://i.redd.it/ztxmob1ukqqh1.jpeg
- https://preview.redd.it/7jg13iqpkqqh1.png?width=1532&format=png&auto=webp&s=e94711d1c99bd534a59ac762f65a7fbc05d2078a
- https://preview.redd.it/x4btgdkqkqqh1.png?width=1439&format=png&auto=webp&s=e1a3da677049db75d50cbda6b7f32a82ecd31206
- https://preview.redd.it/6lnlrw9rkqqh1.png?width=1432&format=png&auto=webp&s=64445e851a1d4b94226c5ad61521ebfcfe21f57b
- https://preview.redd.it/xc0b6nzrkqqh1.png?width=1437&format=png&auto=webp&s=353e9f7f5170379284519603b8fa8a020abf5c20
- https://preview.redd.it/iv902aoskqqh1.png?width=1714&format=png&auto=webp&s=e28ec6b5dc6f724f4c296e5ee4a2dd8beade6840
