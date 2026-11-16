# 1wne89f

**Anthropic vydal Claude Opus 5.5: o 40 % levnější než Opus 5, rychlejší o více než 30 % a s nejlepšími výsledky v agentickém kódování**

| | |
|---|---|
| Subreddit | r/singularity |
| Autor | u/ResultBackground2450 |
| Publikováno (Europe/Prague) | 22. 9. 2026, 18:26 |
| Skóre / komentáře | 825 / 105 |
| Odkaz | https://www.anthropic.com/claude-opus-5-5 |
| Diskuse | https://www.reddit.com/r/singularity/comments/1wne89f/introducing_claude_opus_55_40_cheaper_and_smarter/ |

## Co se stalo

Anthropic 22. 9. 2026 oznámil **Claude Opus 5.5**, první model nové rodiny Claude 5.5. Podle oficiálního oznámení model dosahuje úrovně Claude Fable 5.1 na většině práce a jeho provoz je o **40 % levnější než u Opus 5**. Firma zároveň uvedla, že jde o první vydání od chvíle, kdy vyzvala k „brzdění hranice“ (pacing the frontier), a že model před vydáním testovali externí evaluátoři včetně organizací Frontier Design a METR. Claude Sonnet 5.5 a Claude Haiku 5.5 mají následovat v příštích týdnech. Na r/singularity příspěvek získal 825 bodů a 105 komentářů.

## Klíčová fakta

- **Ceny za 1M tokenů:** vstup 4 $, výstup 20 $, čtení z cache 0,20 $, zápis do cache 5 $. U Opus 5 to bylo 5 $ / 25 $ / 0,50 $ / 6,25 $. Rychlý režim (fast mode) stojí 8 $ za vstup a 40 $ za výstup za milion tokenů a je až 2,5× rychlejší.
- **Rychlost:** model generuje výstup o více než 30 % rychleji než Opus 5.
- **Limity:** Anthropic zvyšuje pětihodinové limity u plánů Pro, Max, Team a seat-based Enterprise a předplatitelům dává „banked reset“ (odložený reset limitu, který si mohou vybrat kdykoli).
- **Bezpečnost:** Opus 5.5 má nejlepší výsledky v automatizovaném behaviorálním auditu Anthropicu (téměř 2 000 simulovaných scénářů). Pokusy o obcházení hranic nasazení jsou podle firmy o zhruba 85 % méně časté než u Opus 5 nebo Claude Mythos 5.1.
- **Ochranná opatření:** kvůli srovnatelnosti s Claude Mythos 5.1 v biologii a kyberbezpečnosti je model nasazen s ochranami podobnými Fable 5.1 — kybernetické úlohy při zásahu ochrany dokončuje Opus 4.8, biologické úlohy a vývoj frontier LLM pak Opus 5. Firma zmiňuje tříúrovňový Cyber Verification Program a Life Sciences Verification Program pro biologický výzkum.
- **Soulad s regulací:** k dispozici je nulová retence dat (zero data retention), nasazení zahrnuje vodoznačení podle unijního AI Actu a režim „thinking“ už nelze vypnout.
- **Anti-distilace:** „preserved thinking“ se vztahuje na API účty vytvořené 31. 8. 2026 a později; Anthropic zároveň odkazuje na svou zářijovou zprávu o hrozbách týkající se destilace.
- **Dostupnost:** na všech platformách včetně Amazon Web Services, Google Cloud a Microsoft Azure, ID modelu `claude-opus-5-5`.
- Anthropic sám upozorňuje, že „rozdíl mezi Opus 5.5 a Claude Fable 5.1 je užší, než tyto výsledky naznačují“.

## Čísla

| Benchmark | Opus 5.5 | Fable 5.1 | Opus 5 | GPT-6 Astra | GPT-5.6 Sol |
|---|---:|---:|---:|---:|---:|
| Terminal-Bench 4.0 (agentické kódování) | 66,4 % | 55,8 % | 52,3 % | 57,9 % | 37,3 % |
| FrontierCode v1.1 (Main) | 54,4 % | 50,3 % | 48,0 % | 53,3 % | 47,5 % |
| CursorBench 4.0 | 57,8 % | 51,8 % | 46,6 % | — | 41,7 % |
| GDPval-AA v2.1 (znalostní práce, Elo) | 1846 | 1735 | 1708 | 1542 | 1588 |
| AutomationBench (byznysové workflow) | 40,0 % | 31,4 % | 26,9 % | 41,4 % | 28,8 % |
| Humanity's Last Exam (s nástroji) | 67,7 % | 65,6 % | 63,6 % | 57,2 % | — |
| Terminal-Bench-Science 0.1 | 58,7 % | 52,6 % | 29,0 % | 64,6 % | 22,4 % |
| OSWorld 2.0 (práce s počítačem) | 81,8 % (partial) | 80,7 % | 74,0 % | — | — |
| Chartography (čtení grafů) | 89,0 % | 88,4 % | 83,4 % | — | — |

- Migrace **680 000 řádků kódu za méně než jeden den** (jeden z testujících); práce, která by týmu inženýrů trvala týdny.
- Audit a oprava kódové základny o **200 000 řádcích** za méně než tři hodiny; Opus 5 na stejnou práci potřeboval přes 20 hodin a 2,5× více tokenů.
- Přepis HAProxy z C do Rustu: Opus 5.5 za **9,5 hodiny** vs. **12 hodin** u Fable 5.1 a o **51 % nižší náklady**.
- Úklid výkonu webové aplikace: Opus 5.5 uspěl v **39 z 40** případů.
- Znalostní práce: **16 z 18** reportů od Opus 5.5 prošlo kvalitativní laťkou; analýza fúze hotová za **63 minut** vs. 93 minut u Opus 5, s polovičními náklady.

## Citace

> „Píše tak, jak píšu já.“ (překlad) — raný tester citovaný v oficiálním oznámení Anthropicu

> „Ve VS Code vyřešil více terminálových úloh než Opus 5, a to za méně než polovinu kroků.“ (překlad) — Mario Rodriguez, Chief Product Officer, GitHub

> „Předal jsem Claude Opus 5.5 velkou inženýrskou úlohu napříč šesti našimi repozitáři a nechal ho běžet přes noc, bez dozoru.“ (překlad) — Sean Heintz, Staff Software Developer, Clio

> „Haiku není mrtvý!“ (překlad) — u/pdantix06, nejlépe hodnocený komentář (170 bodů)

> „O 40 % levnější, výrazně lepší alignment a docela velký skok ve výkonu. Singularita je divoká. Zase dva měsíce na takový skok.“ (překlad) — u/frogsarenottoads

> „Dali nám taky banked reset (platí do 22. října).“ (překlad) — u/MatthewGraham-

> „Velké zlepšení rychlosti i inteligence, a ještě levněji? Začínám přemýšlet, kde je háček.“ (překlad) — u/fantakillen

> „Musím předpokládat, že část těch čísel je chytrý marketing, protože ~40 % levněji a zároveň nejlepší model podle Artificial Analysis…“ (překlad) — u/Hans-Wermhatt

## Co říkají komentáře

Nejvýraznější je kombinace nadšení a nedůvěry. Část diskutujících mluví o „pracovním koni“ a o tom, že skok za dva měsíce je divoký; druhá nejlépe hodnocená větev se věnuje tomu, že **Haiku a Sonnet 5.5** jsou stále ve hře. Samostatným tématem je **banked reset** — předplatitelé ho vítají a ptají se, kde ho najít. Několik komentářů očekává, že OpenAI odpoví tentýž den (což se také stalo — GPT-6 Sol a Luna vyšly ještě téhož večera, viz samostatný článek u ID 1wngzou). Skeptičtější hlas (u/Hans-Wermhatt) považuje část čísel za marketing, jiný (u/fantakillen) hledá „háček“. Opakuje se i stížnost na styl odpovídání Opus 5 a naděje, že 5.5 nebude tak „otravný“. Diskutující také upozorňují, že modely z loňska už dnes působí slabě.

## Rozpory a neověřené informace

- **Anekdoty od Anthropicu nejsou nezávisle ověřené** — jde o příklady od výrobce (680 000 řádků migrace za den, audit 200 000 řádků pod tři hodiny, HAProxy za 9,5 hodiny).
- Část komentářů považuje zveřejněná čísla za marketing (u/Hans-Wermhatt), zatímco jiné je přijímají jako jasný skok — přímý rozpor v interpretaci téhož materiálu.
- Anthropic sám uvádí, že rozdíl proti Fable 5.1 je menší, než naznačují benchmarky; to je v rozporu s titulkem postu, který Opus 5.5 staví jako jednoznačného lídra.
- u/kvothe5688 spekuluje bez důkazů, že by Anthropic mohl routovat Fable 5.1 na Opus 5.5 a dál vydělávat.
- Spekulace o tom, že OpenAI odpoví modelem „6.1“ nebo „GPT-6 Luna“, jsou v době psaní komentářů nepodložené (nakonec přišel GPT-6 Sol a Luna).
- Datum expirace banked resetu (22. října) uvádí pouze komentář, ne oficiální zdroj.

## Proč to je důležité

Opus 5.5 je první model Anthropicu po veřejné výzvě k „brzdění hranice“ — a zároveň přichází s výrazným zlevněním (vstup 4 $, výstup 20 $, cache čtení 0,20 $ za milion tokenů). Kombinace „vyšší výkon + nižší cena + rychlejší generování“ posouvá ekonomiku agentických pracovních postupů: u dlouhých úloh, jako jsou migrace kódových základen nebo audity, rozhoduje cena za úlohu, ne za token. Zároveň je to doklad zrychleného vydavatelského tempa — 5.5 přichází zhruba dva měsíce po Opus 5 a ve stejný den jako konkurenční GPT-6 Sol a Luna.

## Další diskuse

- [1wnecg9](https://www.reddit.com/r/ClaudeAI/comments/1wnecg9/) — r/ClaudeAI, 2180 bodů, 436 komentářů: oficiální videooznámení modelu.
- [1wneb1u](https://www.reddit.com/r/singularity/comments/1wneb1u/) — r/singularity, 1042 bodů, 219 komentářů: benchmarky Opus 5.5.
- [1wnf7sb](https://www.reddit.com/r/ClaudeAI/comments/1wnf7sb/) — r/ClaudeAI, 876 bodů, 130 komentářů: o 40 % levnější a o 30 % rychlejší než Opus 5.
- [1wnkgie](https://www.reddit.com/r/ClaudeAI/comments/1wnkgie/) — r/ClaudeAI, 669 bodů, 157 komentářů: první dojmy od trénovaného filosofa.
- [1wnezma](https://www.reddit.com/r/singularity/comments/1wnezma/) — r/singularity, 491 bodů, 72 komentářů: skok na 1. místo v AA Intelligence Index.
- [1wnecre](https://www.reddit.com/r/ClaudeAI/comments/1wnecre/) — r/ClaudeAI, 255 bodů, 110 komentářů: Anthropic nabízí volný reset na „prozkoumání Opus 5.5“.
- [1wnk30g](https://www.reddit.com/r/OpenAI/comments/1wnk30g/) — r/OpenAI, 528 bodů, 161 komentářů: srovnání benchmarků s GPT-6 Sol.

## Zdroje

- https://www.anthropic.com/claude-opus-5-5 (oficiální oznámení)
- https://anthropic.com/claude-opus-5-5-system-card (system card, zmíněno v oznámení)
- https://www.reddit.com/r/singularity/comments/1wne89f/introducing_claude_opus_55_40_cheaper_and_smarter/
- komentáře: `2026-09-22/_data/raw/comments/1wne89f.json`
