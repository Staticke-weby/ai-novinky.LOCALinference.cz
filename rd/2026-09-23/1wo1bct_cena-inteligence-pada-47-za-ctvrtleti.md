# 1wo1bct

**Cena inteligence padá o 47 % za čtvrtletí, OpenAI prý utrácí 4 miliony dolarů denně**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Terminator857 |
| Publikováno (Europe/Prague) | 23. 9. 2026, 11:38 |
| Skóre / komentáře | 385 / 150 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1wo1bct/cost_of_intelligence_is_dropping_fast/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wo1bct/cost_of_intelligence_is_dropping_fast/ |

## Co se stalo

Do r/LocalLLaMA přišel 23. září 2026 příspěvek s titulem „Cena inteligence padá rychle“ (překlad) shrnující novou analýzu institutu Epoch AI. Autor u/Terminator857 cituje příspěvek Epoch AI na síti X a tvrdí, že cena výkonu klesá rychleji než u kterékoli jiné technologie v historii. Příspěvek obsahuje náhledový graf (preview.redd.it/43n0bhiap8rh1.png); stažený obrázek balíček neobsahuje, o jeho podobě tedy nelze nic usoudit.

Stejné téma se ve stejný den objevilo ještě ve třech dalších příspěvcích zařazených do tohoto souhrnu: v r/OpenAI šlo o odhad útraty výzkumníků OpenAI za tokeny, v r/singularity o dva příspěvky sdílející report Epoch AI „Padající cena myšlení“ (překlad).

Jádrem diskuse jsou dvě čísla: tempo zlevňování zhruba 47 % za čtvrtletí (13× za rok) a odhad denní útraty za tokeny přes 4 miliony dolarů, ovšem oceněný v API cenách, nikoli jako skutečný interní náklad firmy.

## Klíčová fakta

- **Report Epoch AI** byl publikován 22. září 2026, autory jsou Luke Emberson a David Roodman. Zkoumá pět benchmarků z matematiky, přírodních věd a her dovednosti za poslední tři roky.
- **Tempo zlevňování:** cena dosažení dané úrovně výkonu AI klesla od roku 2023 zhruba o 47 % za čtvrtletí, tedy 13× za rok.
- **Srovnání s jinými technologiemi:** pokles je podle Epoch AI čtyřikrát rychlejší než u sekvenování DNA, šestkrát rychlejší než u výpočetního výkonu, 18krát rychlejší než u lithium-iontových baterií a 54krát rychlejší než u elektřiny (v století do roku 1973).
- **Rozdíly podle domény:** u herních hlavolamů je pokles pomalejší, 39–43 % za čtvrtletí, u matematických úloh rychlejší, 50–52 % za čtvrtletí.
- **Záleží na úrovni výkonu:** u výkonu, který právě debutoval jako špičkový (SOTA), cena padá 66 % za čtvrtletí (75× za rok); o dva roky později už jen 32 % za čtvrtletí (4,7× za rok).
- **Ukázkový příklad:** model o3 od OpenAI dosáhl 75 % ve zkoušce GPQA Diamond za průměrně 30 centů na otázku (31. ledna 2025); o necelých 18 měsíců později dosáhl stejného skóre model GPT-5.6 Luna za 0,0004 dolaru na otázku – pokles 725násobný.
- **Metodika:** pro odhad výkonu při omezeném rozpočtu používají autoři postup vyvinutý federálním Centrem pro standardy a inovace v AI (CAISI), který z přepisu běhu bez rozpočtového omezení odvozuje, kolik otázek by model stihl zodpovědět při nižších rozpočtech.
- **Odhad útraty OpenAI:** analytik Abtin Forouzandeh vychází z věty v oznámení o GPT-6 – při ocenění v API cenách přesáhla denní spotřeba tokenů 600 dolarů u mediánového výzkumníka a 7 000 dolarů na 90. percentilu. Z toho odhaduje přes 4 miliony dolarů denně, ovšem jen za výzkumníky a jen v API cenách.

## Čísla

| Ukazatel | Hodnota | Zdroj |
|---|---|---|
| Pokles ceny za čtvrtletí (od 2023) | 47 % | Epoch AI |
| Roční ekvivalent poklesu | 13× za rok | Epoch AI |
| Srovnání: sekvenování DNA | 4× pomalejší | Epoch AI |
| Srovnání: výpočetní výkon | 6× pomalejší | Epoch AI |
| Srovnání: lithium-iontové baterie | 18× pomalejší | Epoch AI |
| Srovnání: elektřina (do 1973) | 54× pomalejší | Epoch AI |
| Pokles u SOTA na debutu | 66 % za čtvrtletí (75× ročně) | Epoch AI |
| Pokles dva roky po debutu | 32 % za čtvrtletí (4,7× ročně) | Epoch AI |
| Cena otázky GPQA Diamond, o3 (leden 2025) | 0,30 dolaru | Epoch AI |
| Cena otázky GPQA Diamond, GPT-5.6 Luna | 0,0004 dolaru | Epoch AI |
| Pokles ceny mezi oběma modely | 725násobný za méně než 18 měsíců | Epoch AI |
| Denní útrata výzkumníka, medián | přes 600 dolarů | abtin.com / OpenAI |
| Denní útrata výzkumníka, 90. percentil | přes 7 000 dolarů | abtin.com / OpenAI |
| Počet výzkumníků v odhadu | 1 125 (25 % ze 4 500 zaměstnanců) | abtin.com |
| Střední hodnota denní útraty | 3 768,29 dolaru | abtin.com |
| Odhad celkové denní útraty | 4 239 325 dolarů | abtin.com |
| Podíl 10 % nejsilnějších uživatelů (power users) na hodnotě | 73,7 % | abtin.com |
| Průměr na nejsilnějšího uživatele / na ostatní | 27 789 / 1 099 dolaru | abtin.com |
| Skóre a komentáře, hlavní příspěvek | 385 / 150 | balíček |

Podle abtin.com jsou medián 600 dolarů a 90. percentil 7 000 dolarů v odhadu brány jako přesné kvantily a rozdělení denní útraty je lognormální. Střední hodnota 3 768,29 dolaru je tak 6,28násobek mediánu. Desetina největších uživatelů spotřebuje 73,7 % celkové denní hodnoty. Samotný autor odhadu ale dodává, že zdroj uvádí „přesáhla“, nikoli „rovná se“, že oba prahy neurčují střední hodnotu ani horní konec rozdělení, a že 4,24 milionu dolarů tedy není prokázaná dolní mez. Číslo 4 500 zaměstnanců je z března 2026 a týká se jiného období než pozdější měření spotřeby.

## Citace

> „50 % za čtvrtletí je úžasné. 4× rychleji než sekvenování DNA, 6× rychleji než výpočetní výkon, 18× rychleji než lithium-iontové baterie a (do roku 1973) 54× rychleji než elektřina.“ (překlad) — u/Terminator857, text hlavního příspěvku 1wo1bct

> „Každý další rok bude výrazně odlišný od toho předchozího. Co si myslíte? Na telefonech budeme brzy provozovat kódovací agenty.“ (překlad) — u/Terminator857, text hlavního příspěvku 1wo1bct

> „Cena dosažení dané úrovně výkonu AI klesla za poslední tři roky zhruba o 47 % za čtvrtletí, což je rychleji než u jakékoli jiné transformativní technologie v historii.“ (překlad) — Epoch AI, report „Cena myšlení“ (The plunging price of thought)

> „Je to jako kdyby cena nového auta klesla z 50 000 dolarů na 69 dolarů.“ (překlad) — Epoch AI, report „Cena myšlení“ (The plunging price of thought)

> „Při ocenění v API cenách přesáhla denní spotřeba tokenů 600 dolarů u mediánového výzkumníka a 7 000 dolarů u výzkumníků na 90. percentilu.“ (překlad) — citát z oznámení o GPT-6, jak jej uvádí abtin.com

> „Pamatujte, Uber byl levnější než taxi, protože… dotace od venture kapitálu! Podobný vývoj u taxi by naznačoval, že jízdy už dnes mají být zdarma, ale nejsou. A tentokrát jsou dotace do AI na rekordní úrovni, což taky znamená, že nemusí dlouho vydržet. Je to velká sázka.“ (překlad) — u/a235, komentář (306 bodů)

> „Právě teď je WinRAR ziskovější než OpenAI a Anthropic dohromady.“ (překlad) — u/tecneeq, komentář (137 bodů)

> „Zoufale potřebujeme revoluci. Řídká pozornost (sparse attention) je fajn, MoE mají nevýhody, ale zatím fungují… Obojí je ale spíš optimalizace prvního řádu. Potřebujeme transformers 2.0.“ (překlad) — u/Dany0, komentář (59 bodů)

> „Jestli je AI tak levná, jak to, že se mi ztrojnásobil účet za elektřinu a moje DDR5 sada stojí 10× tolik, co jsem za ni dal? Ta matematika nějak nevychází, když uděláte krok zpět.“ (překlad) — u/fgk55555, komentář

> „…mělo by se o tom před veřejností mluvit jako o výkonu automatického doplňování (autocomplete). Cena automatického doplňování klesá.“ (překlad) — u/05032-MendicantBias, komentář

## Co říkají komentáře

Diskuse pod hlavním příspěvkem (150 komentářů) se točí okolo jedné otázky: je zlevňování skutečný technologický posun, nebo jen dočasně dotovaná cena? Nejvýše hodnocený věcný komentář (u/a235, 306 bodů) přirovnává situaci k Uberu, jehož cena byla nízká díky dotacím od venture kapitálu. Podobně u/tecneeq (137 bodů) tvrdí, že WinRAR je ziskovější než OpenAI a Anthropic dohromady.

Proti tomu stojí skupina, podle níž je pokles reálný. u/miversen33 argumentuje, že náklad na výzkum je jednorázový a úspora zůstane i po skončení dotací; u/The_Primetime2023 dodává, že zatímco trénink je drahý, inference je levná a zisková; u/kingslayerer tvrdí, že AWS už u open source provozuje 50% marži.

Třetí téma je technologické: podle u/Dany0 se současné přístupy blíží svým limitům a je potřeba „transformers 2.0“. u/MrBIMC naopak vypočítává, kde ještě zbývá prostor – MoE přesunuly úzké hrdlo na paměť, vylepšení pozornosti zlevňují práci s dlouhým kontextem, sdílené vrstvy zvyšují tokenovou efektivitu. u/PayMe4MyData varuje, že velká část výzkumu zaměřeného na optimalizaci současné generace bude po nástupu nové architektury zbytečná.

Čtvrtý, pro r/LocalLLaMA nejpříznačnější motiv, je rozpor mezi levnou cloudovou inferencí a dražším hardwarem. u/CrowdGoesWildWoooo si stěžuje, že lokální modely „jsou čím dál horší“, protože GPU, APU i paměti zdražují; u/fgk55555 zmiňuje ztrojnásobený účet za elektřinu a desetinásobnou cenu DDR5. u/MLuminos naopak popisuje, že mu qwen 8.2b běží na 12GB kartě za 250 dolarů, a ptá se, zda nejde o snahu udržet GPU nedostupné a protlačit cloud. Jiní (u/Cradawx) namítají, že nejlepší model, který dnes na spotřebitelské kartě utáhnete, je schopnější než v minulosti.

Diskutuje se i samotné slovo „inteligence“: u/05032-MendicantBias tvrdí, že přesnější by bylo mluvit o „výkonu automatického doplňování“. u/monerobull a u/lqvz zmiňují, že konkurenční tlak (například u Deepseek) drží ceny nízko. Jeden vysoce hodnocený komentář (u/Tr4sHCr4fT, 346 bodů) sestával výhradně z obrázku bez textu.

## Rozpory a neověřené informace

- **47 % versus 50 %.** Hlavní příspěvek pracuje s „50 % za čtvrtletí“, zatímco report Epoch AI uvádí 47 %. Jde o zaokrouhlení v textu příspěvku.
- **Dotace versus efektivita.** Komentující se neshodují, zda je pokles cen dán dočasnými investicemi, nebo skutečným zlepšením výzkumu a zlevněním inference. Text ani extrakce nerozhodují.
- **Ziskovost frontierových (špičkových) laboratoří.** Tvrzení o WinRARu, o Anthropicu „velmi blízko ziskovosti“, o „extrémně ziskové inferenci“ i o 50% marži AWS u open source nejsou v podkladech doložena čísly a jsou označena jako neověřená.
- **Záchranný balíček od vlády USA a údajné nastrčené firmy („shell companies“) pro skrývání ztrát** jsou spekulace z komentářů označené jako neověřené.
- **Odhad 4,24 milionu dolarů denně** sám autor uvádí jako odhad podmíněný nepublikovanými předpoklady (podíl výzkumníků 25 %, lognormální rozdělení). Nejde o změřený firemní údaj ani o prokázanou dolní mez; počet zaměstnanců je navíc z března 2026, zatímco spotřeba tokenů z pozdějšího období.
- **Srovnání s jinými technologiemi.** Sám report přiznává, že „cena myšlení“ je vágnější pojem než cena elektřiny a že porovnání je částečně srovnáváním jablek s hruškami.
- **Metodické výhrady Epoch AI:** možné „benchmaxxing“, benchmarky nejsou totéž co užitečná práce, analýza předpokládá uživatele vždy hledajícího nejlevnější model a data za tři roky jsou neúplná a zašuměná.
- **Lokální modely.** Jeden tábor tvrdí, že spotřebitelské modely jsou stále schopnější, druhý, že jsou pomalé vůči frontierovým modelům a hardware je nedostupný.

## Další diskuse

| id | subreddit | skóre | komentářů | čas | přeložený titulek | permalink |
|---|---|---:|---:|---|---|---|
| 1woct12 | r/OpenAI | 231 | 49 | 19:41 | Výzkumníci OpenAI možná utrácejí přes 4 miliony dolarů denně za tokeny (v API cenách) | https://www.reddit.com/r/OpenAI/comments/1woct12/openai_researchers_might_be_spending_4mday_on/ |
| 1wnolng | r/singularity | 171 | 39 | 00:49 | Padající cena myšlení | https://www.reddit.com/r/singularity/comments/1wnolng/the_plunging_price_of_thought/ |
| 1wo5ndm | r/singularity | 203 | 22 | 15:13 | Schopnosti AI zlevňují o 47 % každé čtvrtletí, rychleji než výpočetní výkon, sekvenování DNA, baterie nebo elektřina | https://www.reddit.com/r/singularity/comments/1wo5ndm/ai_capability_is_getting_47_cheaper_every_quarter/ |

Příspěvek 1woct12 odkazuje na blogový zápis na abtin.com z 22. září 2026, který obsahuje výpočet odhadu denní útraty za tokeny. Příspěvek 1wnolng odkazuje přímo na report Epoch AI a příspěvek 1wo5ndm na redditovou galerii se stejným tématem. Komentáře k těmto třem příspěvkům nebyly do balíčku staženy.

## Proč to je důležité

Pokud tempo zhruba 47 % za čtvrtletí platí, znamená to, že každý další rok přinese přibližně třináctinásobné zlevnění stejné úrovně výkonu. To je rychlejší pokles, než jaký kdy zažila elektřina, výpočetní výkon, lithium-iontové baterie nebo sekvenování DNA – technologie, které samy o sobě změnily ekonomiku celých odvětví.

Pro r/LocalLLaMA je podstatný druhý, méně příjemný důsledek. Zlevňuje inference v cloudu, ale hardware, paměti a elektřina pro lokální provoz naopak zdražují. Část komunity proto vidí budoucnost v API, část ji vidí jako závislost na cizí infrastruktuře – a ptá se, jakou cenu má možnost spouštět model na vlastním stroji.

Ekonomický rozměr dokresluje odhad útraty OpenAI. I když jde o číslo v API cenách a s řadou nezveřejněných předpokladů, ukazuje řád, v jakém se pohybují náklady frontierových laboratoří na používání jejich vlastních modelů. A protože cena stejného výkonu padá o desítky procent za čtvrtletí, vyplývá z toho podle Epoch AI, že nadstandardní zisky z poskytování LLM mohou být pro konkrétní model pomíjivé – což je zároveň příčina i důsledek závodu, v němž se dnes AI firmy nacházejí.

Otázka z hlavního příspěvku – zda budeme brzy provozovat kódovací agenty na telefonech – zůstává otevřená. Zlevňování inference tomu nahrává, dostupnost hardwaru a spotřeba energie naopak ne.

## Zdroje

- https://www.reddit.com/r/LocalLLaMA/comments/1wo1bct/cost_of_intelligence_is_dropping_fast/
- https://x.com/EpochAIResearch/status/2102510281176023529
- https://epoch.ai/publications/the-plunging-price-of-thought
- https://www.reddit.com/r/singularity/comments/1wnolng/the_plunging_price_of_thought/
- https://www.reddit.com/r/singularity/comments/1wo5ndm/ai_capability_is_getting_47_cheaper_every_quarter/
- https://www.reddit.com/r/OpenAI/comments/1woct12/openai_researchers_might_be_spending_4mday_on/
- https://www.abtin.com/blog/2026-09-22-openai-spend.html
- 2026-09-23/_data/bundles/1wo1bct.md
- 2026-09-23/_data/extracts/1wo1bct.json
