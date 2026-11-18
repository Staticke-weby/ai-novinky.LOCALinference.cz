# 1xyi3xo
**Proč Claude Code stojí 2× až 10× víc, než by musel**

r/ClaudeAI · u/ilya47 · 17. listopadu 2026, 12:30 · 296 bodů / 63 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xyi3xo/)

Vývojář si posvítil na vlastní spotřebu v Claude Code a došel k jednoduchému závěru: cenu neurčuje množství napsaného textu, ale promeškaná cache. Ta na API klíči vydrží pět minut a u předplatného Pro, Max nebo Ultra hodinu. Kdo se po delší pauze jen vrátí do rozpracované relace, platí znovu skoro celou historii.

Ve zveřejněné analýze proto radí před pauzou spustit /compact, dokud je cache ještě teplá – naměřil 2,5násobek nové relace proti přibližně desetinásobku bez něj. Po návratu je naopak lepší /clear a tři řádky kontextu ve tvaru cíl, hotovo a další krok, s nákladem kolem 1x proti 10x u /compact až po pauze. Dlouhé logy nechané v chatu pak zdražují dalších šest tahů o 15 až 64 procent. Metodiku, grafy i tři běhy měření zveřejnil v GitHub repozitáři.

Diskuse se nejrychleji shodla na tom, že tohle by člověk neměl muset hlídat z hlavy. Nejvíc hlasů má přání u/Original-League-6094 na viditelný indikátor, který varuje před vypršením cache. Na něj navazuje u/BeenWildin otázkou, jak má tohle uživatel vůbec tušit, a že kompakovat včas, ale ne po návratu, zní jako příliš mnoho managementu. Uživatel u/CCodeSI z čísel vytahuje tři návyky pro praxi: před odchodem od velké relace se rozhodnout mezi teplým kompaktem a pozdějším /clear s předávací poznámkou, nepřepínat nástroje uprostřed úkolu za cenu 22násobku běžného tahu a zkracovat výstupy testů třeba přes tail -50.

Vlastní zkušenost přidává u/Far_Reindeer8428, jehož tým spálil týden kvóty na jednom refaktoringu, protože agent každé kolo znovu četl celé repo – víc než změna promptu pomohlo omezit kontext na úkol. Uživatel u/daniel-sousa-me si všímá, že změna náročnosti mezi tahy cache nerozbije, což prý vysvětluje i nové lákání na přepínání klávesami Shift a šipky, a že si nakonec oblíbil i dříve proklínaný volnoběžný kompakt.

Opatrnější linka řeší, jak daleko čísla zobecnit. Uživatel u/ranthishq upozorňuje, že hodinová cache u předplatného není celý příběh: v jeho provozu na Maxu tvořily hodinové zápisy 88 % u Opusu a 98 % u Sonnetu, zbytek byly pětiminutové zápisy ze subagentů a vedlejších požadavků. Hodinový zápis se navíc účtuje jako dvojnásobek vstupu proti 1,25násobku u pětiminutového, takže zápisy cache dělaly 44 % jeho týdenních nákladů i při teplé cache. Uživatel u/emischorr připomíná, že titulní násobky pocházejí z jedné zhruba 97tisícové relace s jedním až třemi běhy na délku pauzy a škálují s velikostí historie proti navazující práci. Do stejné nejistoty míří i dotaz u/AmishTecSupport, zda plošné zapnutí hodinového TTL u stovek uživatelů nezdvojnásobí účet za Bedrock.

Kdo si z toho chce odnést jedno pravidlo, zní takhle: před pauzou zmenšit, po pauze raději začít znovu se třemi řádky.
