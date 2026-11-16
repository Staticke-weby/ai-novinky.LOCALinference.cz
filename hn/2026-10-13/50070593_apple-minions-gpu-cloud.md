# 50070593
**Apple staví distribuovaný GPU cloud z nečinných čipů Apple Silicon**

Hacker News · acossta · 13. října 2026, 14:26 · 240 bodů / 96 komentářů · [diskuse](https://news.ycombinator.com/item?id=50070593)

Apple publikoval paper Minions o virtuálním GPU cloudu postaveném na nečinných zařízeních s Apple Silicon. Odkaz na výzkumnou stránku firmy se objevil na Hacker News a rychle kolem sebe shromáždil desítky reakcí. Sloužit má k rozsáhlým inferenčním úlohám v době, kdy centrální kapacity nestíhají.

Podle shrnutí Applu naráží centralizovaná infrastruktura na cenu, malou pružnost a dlouhé čekání na volné zdroje, zatímco moderní Macy mají výkonné grafiky, které při běžném používání většinou zahálejí. Systém proto tyto grafiky spojuje do sdíleného fondu a slibuje pružné spouštění úloh, odolnost proti chybám a dobré vytížení bez nutnosti pořizovat další hardware.

Uživatel railka vysvětluje, že jde o interní podnikový systém, který Apple už používá, a uvádí na pravou míru, jak funguje. Nejde o dělení jednoho velkého modelu mezi více grafik, ale o paralelismus na úrovni úloh: velká dávka se rozseká na nezávislé podúlohy, například tvorbu embeddingů pro milion dokumentů, a ty se rozešlou po jednotlivých strojích. Uživatel Telemakhos to doplňuje představou firemní sítě, kde dávky s nízkou prioritou běží v noci, když jsou pracovní stanice volné, takže firma pro občasné výpočty nemusí kupovat žádné servery navíc.

Právě ta jednoduchost ale schytala největší kritiku. Uživatel skhameneh paper po přečtení shrnuje jako pouhý plánovač úloh postavený na Ollamě a staví proti němu projekt exo, který podle něj stojí na modernějším distribuovaném výpočtu. Podobně uživatel brandonpelfrey se ptá, kde je inovace, když popis zní jako databáze úkolů, flotila Maců a ukládání vstupů a výstupů do S3. Přidává se i uživatel djoldman s rýpnutím, že jde o nejkratší propagovaný paper, jaký od velké technologické firmy viděl, a další hlas lituje mělkosti textu proti dřívějším povedeným malým modelům Applu.

Třetí linka se točí kolem peněz, energie a důvěry. Uživatel Bric3d si utahuje, že tohle Apple slepí dohromady, ale do racku si od něj pořád nic nekoupíte, a uživatel pm90 míní, že firma nechává ležet peníze na stole, když nebuduje vlastní cloud a nezávislé dodávky čipů. Ostatní mu oponují, že kapacity továren se neshánějí snadno, čekání na některá Studia se počítá na týdny a návrat k vlastnímu serverovému systému by znamenal údržbu platformy, o kterou datová centra na Linuxu nestojí. Vedle toho uživatel lynndotpy sní o tom, že by se takto dala přes noc spojit domácí zařízení do superpočítače pro renderování dětských pokusů s 3D grafikou, zatímco uživatelé chasil a mindwork se ptají, kdo zaplatí elektřinu a zda půjde o dobrovolné zapojení s kompenzací, nebo o tiché vysávání cizích strojů.

Z diskuse tak Minions vychází spíš jako praktický interní pomocník pro odložitelné úlohy než jako průlom v distribuovaném počítání.
