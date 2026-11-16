# 1wnk30g

**Srovnání benchmarků ze stejného dne: Opus 5.5 vyhrál všechny testy proti GPT-6 Sol, Sol ale spotřebuje čtyřikrát méně výstupních tokenů**

| | |
|---|---|
| Subreddit | r/OpenAI |
| Autor | u/Vast-Grapefruits |
| Publikováno (Europe/Prague) | 22. 9. 2026, 21:55 |
| Skóre / komentáře | 528 / 161 |
| Odkaz | https://i.redd.it/6fzx59nym4rh1.png |
| Diskuse | https://www.reddit.com/r/OpenAI/comments/1wnk30g/opus_55_and_gpt6_sol_dropped_on_the_same_day_so_i/ |

## Co se stalo

Anthropic a OpenAI vydaly nové modely ve stejný den — Claude Opus 5.5 a GPT-6 Sol. Autor příspěvku sestavil vlastní srovnávací tabulku (přiložený obrázek) a doplnil ji o poznámky k ekonomice provozu. Podle tabulky **Opus 5.5 vyhrává všechny uvedené benchmarky**, výhodou Solu je ale cena a spotřeba tokenů. Autor upozorňuje na jeden překvapivý detail: v evalu GDPval („skutečná kancelářská práce“) skóruje Sol zhruba o 100 Elo níž než GPT-5.6 Sol, který nahrazuje — podle Artificial Analysis proto, že měl slabší prezentace a vynechával povinné části zadání, nikoli kvůli chybám v uvažování. Oficiální head-to-head podle autora neexistuje.

## Klíčová fakta

- Obě laboratoře vydaly model **tentýž den** (22. 9. 2026); OpenAI zveřejnila Sol zhruba dvě hodiny po Anthropicu (tvrzení diskutujícího).
- **Opus 5.5 vyhrává v každé metrice** zveřejněné v tabulce.
- **GDPval-AA v2.1:** Opus 5.5 1846 Elo vs. GPT-6 Sol 1487 Elo.
- **AA Intelligence Index:** 58 vs. 48.
- **Spotřeba výstupních tokenů na úlohu (max úsilí):** Opus 5.5 ~119 000, GPT-6 Sol ~31 000.
- **Cena:** 20 $ vs. 10 $ za milion výstupních tokenů; čtení z cache 0,20 $ za milion u obou.
- **Kontext nad 272 000 tokenů:** Opus 5.5 bez přirážky, GPT-6 Sol 2× vstup a 1,5× výstup.
- **Náklady na úlohu:** GPT-6 Sol 1,06 $ za celý index (měřeno Artificial Analysis).
- **OSWorld** autor do tabulky nezařadil, protože laboratoře používají různé testovací rámce.

## Čísla

| Metrika (22. 9. 2026) | Claude Opus 5.5 | GPT-6 Sol |
|---|---:|---:|
| AA Intelligence Index | 58 | 48 |
| Terminal-Bench 4.0 (měření Artificial Analysis) | 59,6 % | 44 % |
| GDPval-AA v2.1 (Elo, znalostní práce) | 1846 | 1487 |
| AutomationBench (firemní workflow) | 40,0 % | 33,2 % |
| FrontierCode 1.1 | 54,4 % | 49,3 % |
| Výstupní tokeny na úlohu (max) | ~119 000 | ~31 000 |
| Cena výstupu za 1M tokenů | 20 $ | 10 $ |
| Cena čtení z cache za 1M tokenů | 0,20 $ | 0,20 $ |
| Náklady na úlohu (celý index) | — | 1,06 $ |

## Citace

> „Opus vyhrává každý benchmark v tabulce.“ (překlad) — u/Vast-Grapefruits, vlastní text postu

> „Výhodou Solu je cena.“ (překlad) — u/Vast-Grapefruits, vlastní text postu

> „To, že jsou výstupní tokeny čtyřikrát vyšší, je dost otevírání očí.“ (překlad) — u/Choice-Sympathy8235

> „Srovnávat GPT-6 Sol s Opus 5.5 je trochu nefér — Opus 5.5 už překonává Fable 5.1, takže je to v podstatě nejsilnější model, který Anthropic vydal. Lepší je srovnávat ho s GPT-6 Astra.“ (překlad) — u/PotentialAd8443

> „Rozhodně to není ‚aktualizace ceny‘. Model se musel přetrénovat, aby byl mnohonásobně efektivnější a používal MNOHEM méně tokenů.“ (překlad) — u/Tree8282

> „Model, který ušetří 80 % nákladů a 80 % času, ale je o něco hloupější než Opus 5, je minimálně o 80 % lepší.“ (překlad) — u/Aranthos-Faroth

> „Skóre od Artificial Analysis možná platí pro některé zátěže nebo lidi, ale jako někdo, kdo týdně protopí 4 předplatná Max, 2 OpenAI a 2 Anthropic… nevidím v těch číslech žádný řád ani smysl.“ (překlad) — u/JonNordland

## Co říkají komentáře

Největší pozornost budí **čtyřnásobný rozdíl ve spotřebě výstupních tokenů** — byť cena za token je u Solu poloviční, u dlouhých úloh to znamená jiný výsledek než prosté srovnání ceníků. Druhá linie zpochybňuje samotné srovnání: podle části diskutujících se má Sol srovnávat spíš s GPT-6 Astra než s Opus 5.5, protože Opus 5.5 je aktuální špička Anthropicu. Objevuje se i názor, že Sol není nový model, ale „aktualizace ceny s malými změnami“, na což jiní reagují, že model musel být přetrénován na výrazně vyšší efektivitu. Třetí skupina zpochybňuje vypovídací hodnotu skóre Artificial Analysis vůči vlastní zkušenosti z praxe. Vedle toho se řeší styl psaní Opus 5.5 („vždycky má na konci ještě jednu věc navíc… prostě tak nějak povýšený“) a objevují se vtípky o položce „ass“ v tabulce.

## Rozpory a neověřené informace

- **Rozdílné hodnoty téhož benchmarku:** tabulka v tomto postu uvádí pro Opus 5.5 v Terminal-Bench 4.0 hodnotu **59,6 %** (měření Artificial Analysis), zatímco oficiální oznámení Anthropicu uvádí **66,4 %** (xhigh úsilí). Rozdíl vzniká odlišnou metodikou a nastavením úsilí.
- **Neověřené tvrzení:** u/Vast-Grapefruits uvádí, že OpenAI zveřejnila Sol dvě hodiny po Anthropicu; v balíčku pro to není přímý doklad.
- **Neověřené tvrzení:** podle u/Choice-Sympathy8235 používá Opus při vysokých benchmarcích až 8× více výpočtu a OpenAI má v záloze větší model jménem Bel.
- **Neověřené tvrzení:** u/SeidlaSiggi777 tvrdí, že OpenAI chtěla vydáním Solu „naštvat Anthropic“ a že „to velké přijde na DevDay“.
- **Neověřené tvrzení:** u/onehedgeman popisuje autonomní běh s „jedním procentem týdenního limitu“ a „nulou chyb, protože si modely navzájem testují práci“.
- Připsání poklesu GDPval u Solu slabším prezentacím je v postu citováno z druhé ruky (Artificial Analysis), nikoli z primárního zdroje.

## Proč to je důležité

Souboj dvou modelů vydaných tentýž den ukazuje, že rozhodujícím parametrem přestává být maximální skóre a stává se jím **cena za dokončenou úlohu**. Tabulka zároveň odhaluje metodický problém: stejný benchmark vychází u Anthropicu a Artificial Analysis o téměř sedm procentních bodů jinak, takže čísla z marketingových oznámení a z nezávislých běhů nelze míchat. Pro praktické nasazení je podstatné, že Opus 5.5 sice vyhrává všechny testy, ale na stejnou práci spotřebuje několikanásobek tokenů — u agentů běžících hodiny až dny to může převážit nad rozdílem ve skóre.

## Další diskuse

- [1wneb1u](https://www.reddit.com/r/singularity/comments/1wneb1u/) — r/singularity, 1042 bodů, 219 komentářů: benchmarky Opus 5.5.
- [1wnjyp1](https://www.reddit.com/r/ClaudeAI/comments/1wnjyp1/) — r/ClaudeAI, 156 bodů, 51 komentářů: stejná tabulka v komunitě Claude.
- [1wnjmwl](https://www.reddit.com/r/singularity/comments/1wnjmwl/) — r/singularity, 69 bodů, 22 komentářů: kompletní srovnání benchmarků Opus 5.5 a GPT-6 Astra/Sol.
- [1wnhawm](https://www.reddit.com/r/singularity/comments/1wnhawm/) — r/singularity, 41 bodů, 10 komentářů: Sol a Luna na benchmarcích.

## Zdroje

- https://i.redd.it/6fzx59nym4rh1.png (srovnávací tabulka; zdroje uvedené v patičce grafu: Artificial Analysis, data vydání Anthropic a OpenAI, Zapier AutomationBench)
- https://www.reddit.com/r/OpenAI/comments/1wnk30g/opus_55_and_gpt6_sol_dropped_on_the_same_day_so_i/
- lokální snímek: `2026-09-22/_data/img/1wnk30g.png`
- komentáře: `2026-09-22/_data/raw/comments/1wnk30g.json`
