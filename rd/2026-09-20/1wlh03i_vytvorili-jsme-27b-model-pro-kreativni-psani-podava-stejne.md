# 1wlh03i

**Vytvořili jsme 27B model pro kreativní psaní. Podává stejně dobré výsledky jako Claude Fable 5 za 40× nižší cenu, s otevřenými váhami**

| Položka | Hodnota |
|---|---|
| Subreddit | r/GeminiAI |
| Autor | u/Lukinator6446 |
| Čas | 20. 9. 2026 15:23 (Europe/Prague) |
| Skóre | 701 |
| Komentáře | 150 |
| Odkaz | https://www.reddit.com/r/GeminiAI/comments/1wlh03i/we_made_a_27b_model_for_creative_writing_performs/ |
| Diskuse | https://www.reddit.com/r/GeminiAI/comments/1wlh03i/we_made_a_27b_model_for_creative_writing_performs/ |

## Co se stalo

Na subredditu r/GeminiAI oznámil uživatel u/Lukinator6446 vydání modelu **hemmingway-1**. Jde podle popisu o 27miliardový (27B) model, který jeho tvůrci trénovali specificky pro eseje, dialogy, scénáře, kreativní psaní a běžné textování. Oznámení nese flair „Self promo“ a odkazuje na web hemmingway.io, kde je model nabízen spolu s aplikací.

Autor v příspěvku uvádí, že model dosahuje „frontier“ úrovně za 40× nižší cenu. Konkrétně tvrdí skóre **1330 na EQ-Bench 4**, tedy těsně za Claude Fable 5 a před mnoha dalšími frontier modely včetně GPT-5.5 a Opus 4.8. Interní benchmarky jsou podle něj k dispozici na model card na adrese hemmingway.io/model/. Váhy jsou údajně veřejné, takže si model může každý spustit sám.

Součástí oznámení je i vlastní aplikace pro model. Její funkce „autopilot“ má za uživatele odpovídat na e-maily a textové zprávy; aplikace je nabízena pro macOS, Windows a Android. Vyzkoušet ji lze zdarma na hemmingway.io.

Diskuse se rychle stočila k praktickým otázkám. Uživatelé se ptali na hardwarovou náročnost, vodoznak, kvantizaci, dostupnost na OpenRouteru, latenci a ceny API. Autor na část z nich odpověděl přímo v komentářích: model podle něj není vodoznakovaný, při FP8 zabírá přibližně 27 GB a lze ho kvantizovat na menší velikost. Na OpenRouter se tým snaží dostat, ale zatím od platformy nedostal odpověď.

Vedle toho se rozvinula debata o tom, co je základem modelu. Několik komentujících usoudilo, že jde o fine-tuning modelu Qwen, a autor v odpovědi potvrdil „3.8-27b“. Ozvaly se i výhrady k tomu, že tato informace nebyla zmíněna přímo v příspěvku, ale pouze na stránce na Hugging Face. Testující uživatelé popsali smíšené zkušenosti s kvalitou výstupu a část vlákna se věnovala i tomu, proč je propagační příspěvek publikován zrovna na subredditu o Gemini.

## Klíčová fakta

- Model **hemmingway-1** má 27B parametrů a je podle autora trénovaný pro eseje, dialogy, scénáře, kreativní psaní a každodenní textování.
- Autor tvrdí skóre **1330 na EQ-Bench 4** – těsně za Claude Fable 5 a před GPT-5.5 a Opus 4.8.
- Uvedená cena má být **40× nižší** než u srovnávaných frontier modelů, váhy mají být veřejné.
- K modelu existuje aplikace s funkcí autopilot pro odpovídání na e-maily a zprávy, dostupná pro macOS, Windows a Android, se zdarma dostupnou zkušební verzí na hemmingway.io.
- V komentářích autor upřesnil, že model není vodoznakovaný, při FP8 zabírá kolem 27 GB a jde kvantizovat níž.
- Základem je podle autora Qwen 3.8 27B; na OpenRouter se model teprve snaží dostat.
- Podle autora tvoří tým dva švýcarští a jeden jihoafrický zakladatel.

## Čísla

| Číslo | Význam |
|---|---|
| 27B | počet parametrů modelu hemmingway-1 |
| 40× | deklarovaná úspora ceny oproti frontier modelům |
| 1330 | deklarované skóre na EQ-Bench 4 |
| ~27 GB | velikost modelu v FP8 podle autora (lze kvantizovat níž) |
| 701 | skóre příspěvku na Redditu |
| 150 | počet komentářů u příspěvku |
| 25 z 43 | počet komentářů stažených do balíčku vs. celkem stažených |
| 466 / 132 | skóre a počet komentářů u duplicitního postu 1wlhh08 v r/LocalLLM |
| 100× / 500× | odhad komentujícího u/OKMiddleOwl, že Opus je zhruba 100× a Fable 500× větší než 27B model (tvrzení komentujícího) |

## Citace

> „Právě jsme vydali hemmingway-1. Je to 27B model, který jsme trénovali speciálně pro eseje, dialogy, scénáře, kreativní psaní a pro každodenní textování.“ (překlad) — u/Lukinator6446

> „Na EQ-Bench 4 dosahuje skóre 1330, hned za Claude Fable 5, a poráží mnoho dalších frontier modelů včetně GPT-5.5 a Opus 4.8.“ (překlad) — u/Lukinator6446

> „Váhy jsou veřejné, takže si ho můžete spustit sami.“ (překlad) — u/Lukinator6446

> „Vůbec není vodoznakovaný, je to 27B model, takže v FP8 má kolem 27 GB. Ale dá se kvantizovat na méně.“ (překlad) — u/Lukinator6446

> „Snažíme se dostat na OpenRouter, ale zatím se nám neozvali.“ (překlad) — u/Lukinator6446

> „Přijde mi trochu nefér, že je jen na stránce na Hugging Face (kterou jsi sem nedal odkaz) zmíněno, že jde v podstatě o fine-tuning qwen3.8 27b. To neznamená, že nemůže být skvělý, ale myslím, že je to podstatná informace.“ (překlad) — u/arturdent

> „Je mi líto, ale zdaleka není na úrovni fable… V humoru a komedii, které mám nade všechno, je mnohem méně vtipný než Gemini.“ (překlad) — u/BedNo8822

## Co říkají komentáře

- **Dostupnost, váhy, kvantizace a ceny** – uživatel u/who_am_i_to_say_so se ptal, zda se model objeví na OpenRouteru, a další se dotazovali na velikost, kvantizaci, latenci a ceny API; autor odpověděl, že tým o zařazení na OpenRouter usiluje, ale platforma zatím nereagovala.
- **Jde o fine-tuning Qwen a měl by být přiznán** – někteří komentující (u/snowieslilpikachu69, u/arturdent, u/marloquemegusta) upozorňovali, že model je založený na Qwen, a autor to v odpovědi potvrdil jako „3.8-27b“.
- **Testy kvality psaní se smíšenými výsledky** – někteří uživatelé (např. u/nps44, u/eldercito, u/cryptoking_93) si psaní pochvalovali, jiní (u/BedNo8822, u/FussyBowser) hlásili slabší výkon v humoru nebo generickou odpověď místo přímé reakce.
- **Skeptický pohled na původ laboratoře** – u/After_Smile7163 se pozastavil nad rozporem mezi tvrzením o švýcarské laboratoři a dřívější zmínkou o Jihoafrické republice; autor to vysvětlil složením týmu.
- **Relevance příspěvku na r/GeminiAI** – u/the_mighty_skeetadon a u/FlavorChamp zpochybnili, proč je propagační příspěvek na subredditu o Gemini.

## Rozpory a neověřené informace

- **Srovnání s Claude Fable 5**: autor tvrdí frontier úroveň a blízkost Fable 5 podle EQ-Bench 4, zatímco u/BedNo8822 uvádí, že model zdaleka není na úrovni fable v humoru, a u/FussyBowserovi přišel generický prolog jako neodpovídající této úrovni.
- **Základní model**: komentující tipovali různé verze Qwen (3.6 vs 3.8 27B); autor v odpovědi uvedl 3.8-27b. Ani jedno tvrzení není v balíčku nezávisle ověřené.
- **Původ laboratoře**: objevila se otázka, zda jde o švýcarskou, nebo jihoafrickou laboratoř; autor uvádí tým dvou Švýcarů a jednoho jihoafrického zakladatele.
- **Tvrzení autora, že testeři označili model za nejlepší AI na psaní, jakou kdy použili, a že zní lidsky** – jde o zprostředkovanou zpětnou vazbu od testerů, nikoli o nezávisle doložené tvrzení.
- **Benchmark EQ-Bench 4 (1330) a srovnání s GPT-5.5 a Opus 4.8** – jde o interní benchmarky na model card; v balíčku nejsou nezávisle ověřené.
- **Odhad velikosti srovnávaných modelů** – u/OKMiddleOwl tvrdí, že Opus je zhruba 100× a fable 500× větší než 27B model; jde o odhad komentujícího.
- **Domněnka o webovém rozhraní** – u/nps44 se domnívá, že webové rozhraní bylo napsáno s Claudem, protože formulace působí „opusovsky“; jde o dohad komentujícího.

## Proč to je důležité

Oznámení ukazuje rostoucí trend malých specializovaných modelů s otevřenými váhami, které cílí na kreativní psaní místo obecných úloh. Tvrdí-li 27B model srovnatelné výsledky s výrazně většími frontier modely za zlomek ceny, je to pro uživatele, kteří na psaní spotřebovávají velké objemy tokenů, ekonomicky relevantní. Diskuze zároveň ukazuje, jak silně komunita tlačí na transparentnost – zejména na přiznání základního modelu a na doložitelnost benchmarků. Duplicitní publikace v r/LocalLLM srovnatelně vysokým skóre ukazuje, že téma rezonuje i mimo subreddit o Gemini.

## Další diskuse k tématu

- 1wlhh08 | r/LocalLLM | 466 skóre | 132 komentářů | 15:44 | „Vytvořili jsme 27B model pro kreativní psaní. Podává stejně dobré výsledky jako Claude Fable 5 za 40× nižší cenu, s otevřenými váhami“ | https://www.reddit.com/r/LocalLLM/comments/1wlhh08/we_made_a_27b_model_for_creative_writing_performs/

## Zdroje

- https://www.reddit.com/r/GeminiAI/comments/1wlh03i/we_made_a_27b_model_for_creative_writing_performs/
- https://www.reddit.com/r/LocalLLM/comments/1wlhh08/we_made_a_27b_model_for_creative_writing_performs/
- https://hemmingway.io
- https://hemmingway.io/model/
