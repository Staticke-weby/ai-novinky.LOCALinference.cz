# 50634658
**GPT-6 navrhl proteiny jen pomocí uvažování a kódu**

Hacker News · acossta · 24. listopadu 2026, 22:02 · 229 bodů / 69 komentářů · [diskuse](https://news.ycombinator.com/item?id=50634658)

OpenAI 24. listopadu popsala, že modely řady GPT-6 dokážou navrhovat nové tvary proteinů i jejich aminokyselinové sekvence jen pomocí psaného uvažování a kódu, bez volání specializovaných biologických modelů pro samotný návrh. Interní výzkumný model byl u většiny ze čtrnácti testovaných proteinových úloh srovnatelný nebo lepší než specializované nástroje. V laboratorních testech s firmou Onava se pak u všech pěti zvolených cílů našel alespoň jeden protein z návrhu GPT-6.2, který vykázal vazbu, a přepracované protilátky si vazbu na původní cíl udržely.

Odkazovaný článek ukazuje, jak model při návrhu kombinuje matematiku, fyziku, chemii a biologii, což je vidět v jeho úvahách i vepsaném kódu. Badatelé ho mohli řídit pouhou změnou promptu od jedné vazby mezi dvěma atomy až po celkový tvar minibinderu, včetně toho, kde se má přichytit a kolik má mít závitů a vláken. Slabinu přitom firma přiznává v predikci celé prostorové struktury proteinu a u laboratorních pokusů dodávaly sekvence a výběr kandidátů k otestování specializované modely.

Právě tahle dělba práce zarazila v diskusi nejvíc lidí. fabian2k se ptá, co vlastně GPT-6.2 navrhla, když sekvenci pak doplnil specializovaný SolubleMPNN, protože sekvence je pro protein v podstatě strukturou. changoplatanero odpovídá, že je to v de novo designu běžné: GPT udělala první krok, návrh páteře, což je většina cesty k funkčnímu návrhu. the__alchemist to rozepisuje na tři kroky, návrh páteře, předpověď sekvence a předpověď struktury, a gavinray přidává analogii s puzzle: díra má tvar šestiúhelníku a model navrhl, z jakých dílků ten šestiúhelník poskládat.

Druhá velká linka se točí kolem kódu jako superschopnosti. gopalv píše, že dokud se k pokroku stačí dostat lepším kódem, budou se modely zlepšovat, a ralusek glosuje, že psaní kódu byla superschopnost i pro lidi. jubilanti ale namítá, že slovo intrinzický mu tu nesedí, protože model sice nepoužil proteinový model, ale opřel se o existující oborové knihovny. cyanydeez a hooloovoo_zoo dodávají, že těžké je hlavně přesně definovat, co je dobré, a spolehlivě měřit pokrok, zatímco aabhay varuje, že modely září v jednom souboru do zhruba pěti tisíc řádků, ale ve větším měřítku sklouzávají k duplicitám a neudržovatelnému kódu.

Zbytek vlákna míchá údiv, skepsi a humor. mrkn1 vtipkuje, že GPT-6 už zvládla akademii: vymyslí nápad, práci nechá na postgraduantech a vezme si zásluhy. comex se ptá, čím se to vlastně liší od lidského výzkumníka se stejnými nástroji a znalostmi, protože firma je záměrně mlhavá v detailech. Zatímco fedupnow to označuje za marketing pro lidi, kteří nedokážou tvrzení posoudit, ACCount39 a yieldcrv oceňují, že dostatečně schopný model si mezioborově poradí tam, kde jsou lidské obory stále silně oddělené.

Čtenář si z toho odnese hlavně tohle: tvar bez sekvence zatím v laboratoři neobstojí, a právě spolupráce obecného uvažování s úzce zaměřenými modely rozhodla o výsledku.
