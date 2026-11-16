# 1wnwdww

**Apple spustil bilionparametrový model na čtyřech Mac Studiích z jedné zásuvky**

| | |
|---|---|
| Subreddit | r/LocalLLM |
| Autor | u/Novel-Lifeguard6491 |
| Publikováno (Europe/Prague) | 23. 9. 2026, 06:50 |
| Skóre / komentáře | 192 / 105 |
| Odkaz | https://www.reddit.com/r/LocalLLM/comments/1wnwdww/apple_just_ran_a_1t_parameter_model_on_four_mac/ |
| Diskuse | https://www.reddit.com/r/LocalLLM/comments/1wnwdww/apple_just_ran_a_1t_parameter_model_on_four_mac/ |

## Co se stalo

Uživatel u/Novel-Lifeguard6491 zveřejnil v komunitě r/LocalLLM příspěvek s tvrzením, že Apple předvedl běh modelu Kimi K2.6 — otevřeného modelu s jedním bilionem parametrů — na čtyřech počítačích Mac Studio zapojených do jedné zásuvky ve zdi. Informaci přisuzuje agentuře Reuters a jejímu článku z 22. září 2026 o snaze Applu konkurovat Microsoftu a Nvidii a snížit náklady na umělou inteligenci.

Podle textu příspěvku mají nové Mac Studio dorazit na konci října s až 512 GB unifikované paměti (unified memory) a rozhraní Thunderbolt 5 spolu s technologií RDMA (Remote Direct Memory Access, vzdálený přímý přístup do paměti) má strojům umožnit chovat se jako jeden cluster. Apple má tvrdit, že čtyři Mac Studio dokážou dodat až trojnásobný výkon při inferenci (inference, čili běh již natrénovaného modelu) oproti jednomu stroji.

Autor sám rámuje příspěvek jako otázku: cloudová inference podle něj stále vítězí v měřítku, ale ekonomika „koupit výpočetní výkon jednou a přestat platit za token“ se podle něj pro některé týmy začíná vyplácet. Připomíná, že lokální umělá inteligence bývala hlavně o soukromí a o experimentování, kdežto nyní se hlavním argumentem stávají náklady. Na konci se ptá, kterou zátěž by čtenáři jako první přesunuli z cloudu, pokud by se hardwarová ekonomika vyvíjela tímto směrem.

Do stejného souhrnu patří i sloučený příspěvek z komunity r/LocalLLaMA od uživatele u/jacek2023, který oznamuje zveřejnění modelu apple/LensVLM-9B na Hugging Face. Jde o devítimiliardový vizuálně-jazykový model (VLM), který umí číst komprimované obrázky textu a následně cíleně rozbalovat pouze relevantní stránky do nekomprimované podoby.

## Klíčová fakta

- **Téma celého souhrnu:** ekonomika lokálního běhu velkých modelů na hardwaru Apple a souběžné vydání nového vizuálně-jazykového modelu LensVLM-9B.
- **Kimi K2.6** je v příspěvku popisován jako otevřený model (open-weight) s jedním bilionem parametrů; běžel údajně na čtyřech Mac Studiích.
- Autory dema i čísla o výkonu příspěvek přisuzuje Applu přes odkaz na agenturu Reuters — jde tedy o tvrzení z druhé ruky, nikoli o měření, které by měl autor k dispozici.
- **Thunderbolt 5 + RDMA** je v příspěvku uvedeno jako mechanismus, který ze čtyř samostatných strojů dělá cluster. V komentáři sám autor upřesňuje, že jde o obousměrné propojení až 80 Gb/s.
- **Kapacita paměti:** příspěvek uvádí až 512 GB unifikované paměti na jeden Mac Studio. Komentující tento údaj rozporují jen ohledně termínu dodání, nikoli ohledně samotné hodnoty.
- **Termín:** podle příspěvku mají nové stroje vyjít na konci října; komentující tvrdí, že 512GB varianta je objednatelná až od konce října.
- **Vedlejší vydání:** v samostatném příspěvku v r/LocalLLaMA je oznámeno, že Apple publikoval model LensVLM-9B na Hugging Face ve formátu váh i v GGUF kvantizaci od uživatele bartowski.
- **LensVLM-9B** je podle karty modelu devítimiliardový VLM postavený na modelu Qwen/Qwen3.5-9B. Model naskenuje komprimované obrázky textu a potom pomocí naučených nástrojů rozbalí jen relevantní stránky.
- **Licence:** soubory modelu včetně Apple úprav modelu Qwen jsou pod licencí Apple Machine Learning Research Model License; přiložený zdrojový kód je distribuován zvlášť pod licencí Apple Sample Code License.
- **Dostupné kompresní úrovně:** 5×, 10× a 15×.
- **Odkazy z karty modelu:** článek (paper) na arXiv:2605.07019 a kód v repozitáři github.com/apple-aiml-research/ml-lensvlm.

## Čísla

Následující tabulka shrnuje číselné údaje z podkladu. Položky z komentářů jsou tvrzení uživatelů, ne ověřená měření.

| Údaj | Hodnota | Kde je uveden |
|---|---|---|
| Parametry modelu Kimi K2.6 | 1 bilion (1T) | text příspěvku 1wnwdww |
| Počet Mac Studií v demu | 4 | text příspěvku 1wnwdww |
| Maximální unifikovaná paměť Mac Studio | až 512 GB | text příspěvku 1wnwdww |
| Zrychlení clusteru oproti jednomu stroji | až 3× | text příspěvku 1wnwdww (tvrzení Applu) |
| Propustnost propojení Thunderbolt 5 + RDMA | až 80 Gb/s obousměrně | komentář autora příspěvku |
| Skóre / komentáře / poměr hlasů (1wnwdww) | 192 / 105 / 0,87 | metadata balíčku |
| Skóre / komentáře / poměr hlasů (1wodf84) | 78 / 22 / 0,93 | metadata balíčku |
| Cena Mac Studio s 256 GB v Nizozemsku | 11 tisíc € (€11k) | komentář u/HenkPoley |
| Parametry modelu LensVLM-9B | 9B | karta modelu na Hugging Face |
| Stažení LensVLM-9B za poslední měsíc | 455 | karta modelu na Hugging Face |
| Kompresní úrovně LensVLM-9B | 5×, 10×, 15× | karta modelu na Hugging Face |
| Kvantizace LensVLM-9B | 9 modelů | karta modelu na Hugging Face |

Pro kontext uvádíme i čísla z výpočtů diskutujících; jde o uživatelská tvrzení bez ověření (viz část o rozporech).

| Tvrzení z komentářů | Hodnota | Autor |
|---|---|---|
| Běh Qwen3.8 27b na dvou roky staré RTX 4090 | 100 tps, 2,5 miliardy výstupních tokenů ročně | u/73td |
| Elektřina versus cloud pro tento běh | ~600 $ za elektřinu vs. 6–8 tis. $ v cloudu | u/73td |
| Výkon MiMO-2.6-flash na 256GB stroji | 2,5 tis. PP, 90–100 TG | u/bakawolf123 |
| Úspora při lokálním běhu GLM-5.3-flash | ~0,25 $/hodinu, ~2 tis. $/rok | u/OhSillyDays |
| Srovnání s frontier modelem | ~20 $/hodinu, ~175 tis. $/rok úspora | u/OhSillyDays |
| Domácí odběr při provozu AI | ~3 kW | u/1Poochh |

## Citace

> „Apple předvedl Kimi K2.6, otevřený model s 1 bilionem parametrů, na čtyřech z nich zapojených do jedné jediné zásuvky ve zdi.“ (překlad) — u/Novel-Lifeguard6491, text příspěvku 1wnwdww

> „Zajímá mě, kterou zátěž byste vlastně vytáhli z cloudu jako první, kdyby se hardwarová ekonomika vyvíjela tímto směrem?“ (překlad) — u/Novel-Lifeguard6491, text příspěvku 1wnwdww

> „100 tisíc utracených za Kimi 2.6 koupí hodně tokenů… nejsem si jistý, že ekonomika sama o sobě ospravedlní takové pořízení.“ (překlad) — u/etaoin314, komentáře

> „Apple dělá boží práci, když vyrábí hardware, který je pro lokální AI energeticky efektivní.“ (překlad) — u/redditnosedive, komentáře

> „512GB variantu paměti Mac Studio lze objednat (znovu) až od konce října.“ (překlad) — u/HenkPoley, komentáře

> „LensVLM je devítimiliardový vizuálně-jazykový model (VLM), který skenuje komprimované obrázky textu a poté cíleně rozbaluje pouze relevantní stránky do jejich nekomprimované podoby pomocí naučených nástrojů.“ (překlad) — u/jacek2023, text příspěvku 1wodf84

## Co říkají komentáře

Diskuse pod příspěvkem se nesla hlavně v rovině ekonomiky a spolehlivosti. Extrakce rozpoznává pět opakujících se témat.

**Ekonomika clusteru versus cloudové tokeny.** Nejvýše hodnocený komentář (u/etaoin314, 68 bodů) zpochybňuje, že by se pořízení čtyř strojů zaplatilo jen úsporou za tokeny: velký rozpočet utracený za Kimi 2.6 odpovídá velkému množství tokenů. V odpovědích zaznívá protiargument, že nejde jen o počet tokenů, ale o stabilitu a o to, vědět, co vám běží a kde jsou uložená data (u/Own_Mix_3755, 41 bodů). u/Murder_1337 (10 bodů) dodává, že na podnikové úrovni je práce s API velmi drahá a že každé omezení či zpomalení služby znatelně dopadá na běžný pracovní den.

**Energetická efektivita hardwaru Apple.** Druhý výrazný proud chválí Apple za energeticky úsporný hardware pro lokální AI (u/redditnosedive, 39 bodů). Navazuje u/1Poochh (10 bodů), který doma na AI spotřebovává kolem 3 kW a těší se na Mac, protože mu vadí spotřeba energie i teplo z dosavadního řešení. Proti tomu stojí přiznání, že modely jsou dobré, ale Maca velmi drahá (u/john_mach, 17 bodů), a vtipné poznámky o hypotékách (u/ephemeralsynth).

**Oprava termínu dodání.** Několik komentujících nesouhlasí s formulací, že Mac Studio s až 512 GB unifikované paměti vychází právě teď. u/ZergvProtoss (12 bodů) to označuje za dezinformaci, u/Objective-Bed-393 (5 bodů) se pozastavuje nad stejnou formulací a u/HenkPoley (8 bodů) upřesňuje, že 512GB variantu lze objednat znovu až od konce října, alespoň v Nizozemsku, kde 256GB verze už stojí 11 tisíc eur (€11k).

**Lokální běh v regulovaných oborech.** Advokátní a zdravotnické provozy by podle u/davecrist (7 bodů) měly zájem provozovat modely této velikosti, aniž by musely posílat data mimo vlastní infrastrukturu.

**Menší „flash“ modely, které se vejdou na jeden stroj.** u/TheLexoPlexx (57 bodů) se ptá, zda by se GLM5.3-Flash neměl vejít na jediný M5 Ultra; u/shayanx45 (5 bodů) uvádí, že Mimo v2.6 flash právě vyšel, podává lepší výsledky než glm 5.3 flash a vejde se na 256GB stroj se dvěma Sparky nebo na Mac Studio. u/bakawolf123 (3 body) přidává skeptický pohled: clustering se podle něj nebude dobře škálovat pro souběžné požadavky, což člověk na on-premise provozu pro více lidí potřebuje, a paged attention v MLX podle něj nebyl tak účinný jako vLLM na Nvidii.

**Specifické dotazy a přirovnání.** u/Limp_Lingonberry_538 se ptá na rychlost propojení RDMA a sám autor odpovídá, že až 80 Gb/s obousměrně. u/Ok-Addendum3545 srovnává čtyři Mac Studia proti jedné stanici DGX Station GB300, u/ddimick přišívá paralelu se zlatou horečkou, v níž Apple prodává „krumpáče a lopaty“.

## Rozpory a neověřené informace

V podkladu se objevují tvrzení, která nelze považovat za doložená fakta. Patří sem především:

1. **Demo Applu.** Informace, že Apple předvedl Kimi K2.6 na čtyřech Mac Studiích z jedné zásuvky, je v příspěvku připsána Reuters. Balíček ani extrakce neobsahují samotný text článku Reuters ani nezávislé potvrzení — jde tedy o tvrzení z druhé ruky.
2. **Výkon clusteru „až 3×“.** Toto číslo je v příspěvku prezentováno jako tvrzení Applu, nikoli jako výsledek nezávislého měření. Komentář u/bakawolf123 navíc tvrdí, že škálování clusteru pro souběžné požadavky nebude dobré a že paged attention v MLX zaostává za vLLM na Nvidii — i to je ale jen uživatelské tvrzení bez doložených měření.
3. **Termín a objednatelnost.** Text příspěvku a komentáře se rozcházejí v tom, zda Mac Studio s 512 GB vychází „právě teď“, nebo zda jde jen o objednávky od konce října. Ani jedna strana sporu nepředkládá ověřitelný zdroj; komentující uvádějí, že údaj platí „alespoň v Nizozemsku“.
4. **Uživatelské výpočty nákladů.** Čísla u/73td (100 tps na RTX 4090, 600 $ za elektřinu proti 6–8 tisícům dolarům v cloudu), u/bakawolf123 (2,5 tis. PP a 90–100 TG na MiMO-2.6-flash), u/OhSillyDays (0,25 $/hodinu a 2 tisíce $ ročně proti 20 $/hodinu u frontier modelu) i u/1Poochh (3 kW doma) jsou subjektivní odhady a anekdoty, nikoli doložená měření.
5. **Budoucí scénáře.** Úvahy o tom, že se předplatné v hodnotě bilionů „vypaří“, až Apple dostane schopný model do iPhonu, nebo že přechod na čínské otevřené modely zničí obchodní model OpenAI a Anthropicu, jsou spekulace diskutujících.
6. **Vedlejší příspěvek.** Balíček výslovně uvádí, že komentáře u sloučeného příspěvku 1wodf84 nebyly staženy. Údaje o modelu LensVLM-9B proto pocházejí jen z karty modelu na Hugging Face a z textu příspěvku, nikoli z nezávislého hodnocení.

## Další diskuse

Do souhrnu byl sloučen jeden související příspěvek ze stejného tématu — oznámení vydání modelu LensVLM-9B.

| id | subreddit | skóre | komentářů | čas (Europe/Prague) | přeložený titulek | permalink |
|---|---|---:|---:|---|---|---|
| 1wodf84 | r/LocalLLaMA | 78 | 22 | 23. 9. 2026, 20:04 | apple/LensVLM-9B na Hugging Face | https://www.reddit.com/r/LocalLLaMA/comments/1wodf84/applelensvlm9b_hugging_face/ |

Příspěvek od uživatele u/jacek2023 odkazuje na repozitář apple/LensVLM-9B a na jeho GGUF kvantizaci od uživatele bartowski. Nese nálepku „New Model“ a poměr kladných hlasů 0,93. Komentáře k němu balíček výslovně neuvádí jako stažené, takže reakce čtenářů k dispozici nemáme.

## Proč to je důležité

Bilion parametrů je měřítko, které se ještě nedávno pojilo výhradně s datovými centry. Pokud se takový model dá spustit na čtyřech stolních strojcích z jedné zásuvky, mění se rámec úvahy o tom, kde má inference běžet. Klíčové ale je, že velká část tohoto příběhu stojí na tvrzeních z druhé ruky: číslo „až 3×“, parametry dema i termín dodání přicházejí zprostředkovaně a uživatelé si je v diskusi vzájemně opravují.

Pro praktické rozhodování je zajímavější, jak diskuse rozděluje argumenty. Zastánci lokálního běhu neargumentují jen cenou za token, ale také spolehlivostí a kontrolou nad tím, co model je a kde leží data — což rezonuje v právním a zdravotnickém prostředí. Odpůrci poukazují na vysokou vstupní cenu hardwaru, nejisté škálování clusteru pro souběžné dotazy a na to, že malé rychlé modely se často vejdou na jediný stroj.

Druhá polovina souhrnu ukazuje opačný konec spektra. Zatímco Kimi K2.6 představuje honbu za co největším modelem, LensVLM-9B je devítimiliardový specialista, který problém délky kontextu řeší jinak — komprimuje obrázky textu a rozbaluje jen to, co je potřeba.

Pro evropské čtenáře je podstatná i cena: údaj, že Mac Studio s 256 GB unifikované paměti stojí v Nizozemsku 11 tisíc eur (€11k), ukazuje, jak drahý je vstup do lokálního běhu velkých modelů v Evropě.

## Zdroje

- Balíček: `2026-09-23/_data/bundles/1wnwdww.md`
- Extrakce: `2026-09-23/_data/extracts/1wnwdww.json`
- Hlavní příspěvek: https://www.reddit.com/r/LocalLLM/comments/1wnwdww/apple_just_ran_a_1t_parameter_model_on_four_mac/
- Článek Reuters zmíněný v příspěvku: https://www.reuters.com/business/retail-consumer/with-new-macs-apple-aims-take-microsoft-nvidia-rush-lower-ai-costs-2026-09-22/
- Sloučený příspěvek: https://www.reddit.com/r/LocalLLaMA/comments/1wodf84/applelensvlm9b_hugging_face/
- Karta modelu LensVLM-9B: https://huggingface.co/apple/LensVLM-9B
- GGUF kvantizace LensVLM-9B: https://huggingface.co/bartowski/LensVLM-9B-GGUF
- Článek k modelu: https://arxiv.org/abs/2605.07019
- Kód k modelu: https://github.com/apple-aiml-research/ml-lensvlm
