# 1wk9fag

**Alibaba otevřela model Damo Radar: čte CT a v testu předčil 23 z 26 radiologů**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/giveen |
| Publikováno (Europe/Prague) | 19. 9. 2026, 04:08 |
| Skóre / komentáře | 1271 / 82 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1wk9fag/alibaba_opensources_medical_ai_model_that_can/ |
| Další diskuse | [r/singularity](https://www.reddit.com/r/singularity/comments/1wk6hzr/alibaba_opensources_ai_model_that_can_detect/) (159/18) |

## Co se stalo

Výzkumná divize **Damo Academy** společnosti **Alibaba Group Holding** otevřela zdrojový kód modelu **Damo Radar** — vision-language modelu pro čtení **kontrastních CT snímků břicha**. Model pokrývá **18 břišních orgánů** a rozpoznává **téměř 150 onemocnění a abnormalit** včetně zhoubných nádorů. Trénován byl na CT snímcích ve dvojici s klinickými zprávami a testován na **téměř 40 000 reálných vyšetřeních**; přes **146 klinických nálezů** dosáhl průměrné plochy pod křivkou (AUC) **0,913** (1,0 je dokonalá přesnost).

Ve srovnávací studii s **26 radiology** z několika nemocnic model podle článku překonal **23 z nich**. S asistencí modelu se radiologům zlepšila schopnost zabránit přehlédnutým diagnózám o **10 %** a čas potřebný k vyšetření se zkrátil o **více než 30 %**. Výzkum vyšel v časopise **Science** a účastnila se ho mimo jiné nemocnice napojená na Zhejiang University. Jde o pokračování jarních aktivit Damo Academy — v dubnu firma představila model **Coca AI** pro včasný záchyt kolorektálního karcinomu, vyvíjený s Guangdong General Hospital.

## Klíčová fakta

- **Model:** Damo Radar, vision-language model pro kontrastní CT břicha, otevřené váhy.
- **Rozsah:** 18 břišních orgánů, téměř 150 onemocnění a abnormalit včetně zhoubných nádorů.
- **Trénink:** CT snímky párované s klinickými zprávami.
- **Validace:** téměř 40 000 reálných vyšetření, průměrné AUC 0,913 přes 146 klinických nálezů.
- **Srovnání:** 26 radiologů, model jich překonal 23.
- **Přínos v praxi:** o 10 % lepší záchyt přehlédnutých diagnóz, o více než 30 % kratší čas.
- **Publikace:** časopis Science; spoluúčast nemocnice napojené na Zhejiang University.
- **Předchozí model:** Coca AI (duben) pro včasný záchyt kolorektálního karcinomu.
- **Odkazy z komentářů:** repozitář `alibaba-damo-academy/damo-radar` na GitHubu a `radar-generalist` na Hugging Face (neověřeno v textu článku).

## Čísla

| Údaj | Hodnota |
|---|---:|
| Břišních orgánů | 18 |
| Onemocnění a abnormalit | téměř 150 |
| Klinických nálezů v hodnocení | 146 |
| Reálných vyšetření | téměř 40 000 |
| Průměrné AUC | 0,913 |
| Radiologů ve srovnání | 26 |
| Radiologů, které model překonal | 23 |
| Zlepšení záchytu přehlédnutých diagnóz | 10 % |
| Zkrácení času | více než 30 % |
| Skóre / komentáře postu | 1271 / 82 |
| Komentářů v balíčku | 25 |

## Citace

> „Výzkumná divize společnosti Alibaba Group Holding, Damo Academy, otevřela zdrojový kód modelu umělé inteligence, který dokáže identifikovat téměř 150 břišních onemocnění — včetně rakoviny — čtením snímků z počítačové tomografie (CT), což je dalším krokem v rostoucím úsilí firmy v oblasti medicínské AI.“ (překlad) — South China Morning Post

> „Model byl trénován na CT snímcích ve dvojici s klinickými zprávami. Na téměř 40 000 reálných vyšetřeních dosáhl průměrné plochy pod křivkou (AUC) 0,913 přes 146 klinických nálezů.“ (překlad) — South China Morning Post

> „… první expertní generalistický model medicínského zobrazování na světě.“ (překlad) — South China Morning Post

> „Screening rakoviny udělá pro reputaci AI víc než jakákoli ukázka chatbota. Otevřené váhy znamenají, že nemocnice, která si nemůže dovolit API, si model stejně spustí.“ (překlad) — u/Muhlwa_Sholanke, 331 bodů

> „Tohle je přesně to, na co by se měly OpenAI a Anthropic soustředit, ale jejich finanční podporovatelé chtějí chatbot, který nahradí všechny jejich zaměstnance předplatným.“ (překlad) — u/PerceiveEternal, 50 bodů

> „Ideálně by vaše snímky měl projít radiolog i AI. Ne buď/anebo, ale obojí… bohužel realita bude ‚nahradit radiologa! ušetřit na platech!‘ a ředitel si koupí novou jachtu.“ (překlad) — u/krileon, 18 bodů

> „Od čínských lokálních AI modelů čekám dobré věci, hlavně v oblastech, které zlepšují život běžných lidí a malých firem. Od amerických uzavřených modelů čekám hlavně oligopol.“ (překlad) — u/brahh85, 92 bodů

> „U abdominálně-pelvických CT se přehlédne nějakých 30 % incidentalit, takže tohle bylo pravděpodobně trénované na spoustě špatných dat.“ (překlad) — u/catinterpreter, 13 bodů

## Co říkají komentáře

Nejvýše hodnocený komentář shrnuje náladu: **otevřený medicínský model dělá pro pověst AI víc než chatboti** a otevřené váhy znamenají, že model si může spustit i nemocnice bez rozpočtu na API. Druhá linie je **výčitka americkým laboratořím**, že se místo medicíny soustředí na nahrazování pracovníků. Třetí, silně zastoupené téma je **geopolitické** — srovnání čínských otevřených modelů s uzavřeným americkým trhem. Objevuje se i obava z vytlačení radiologů a jedna věcná pochybnost o kvalitě trénovacích dat: podle komentujícího se u břišně-pánevních CT běžně přehlíží výrazná část incidentalit, takže část dat může být zatížená chybami.

## Rozpory a neověřené informace

- **Neověřené odkazy:** GitHub repozitář `alibaba-damo-academy/damo-radar` a Hugging Face `radar-generalist` uvádí komentující, nikoli stažený článek.
- **Neověřené tvrzení:** u/catinterpreter uvádí „nějakých 30 %“ přehlédnutých incidentalit bez zdroje; jde o argument proti kvalitě trénovacích dat.
- **Neshoda:** komentující se rozcházejí v motivech — otevřené váhy jako veřejný statek versus tvrzení, že velké AI firmy slouží investorům a chtějí nahradit práci, ne léčit.
- **Neshoda:** část komentujících chce AI jako doplněk radiologa, část očekává, že management použije model k nahrazení lidí.
- **Nepotvrzené:** tvrzení, že jde o „první expertní generalistický model medicínského zobrazování na světě“, je formulace z článku SCMP, nikoli nezávisle ověřený fakt.

## Proč to je důležité

Jde o konkrétní, publikovaný výsledek s velkým validačním vzorkem a s otevřenými vahami — tedy o něco jiného než demo chatbota. Pokud se výsledky potvrdí v dalších nemocnicích, je to jeden z mála případů, kdy AI **měřitelně mění klinickou praxi** (kratší čas, méně přehlédnutých diagnóz), a zároveň ukázka toho, že otevřené modely se prosazují i v doméně, kde jde o nejcitlivější data. Diskuse zároveň přesně pojmenovává riziko: technologický přínos se dá snadno obrátit v argument pro snižování stavů.

## Zdroje

- https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions
- https://www.reddit.com/r/LocalLLaMA/comments/1wk9fag/alibaba_opensources_medical_ai_model_that_can/
- komentáře: `2026-09-19/_data/raw/comments.json` (klíč `1wk9fag`), balíček `2026-09-19/_data/bundles/1wk9fag.md`
