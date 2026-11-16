# 1xeuo7t
**4B model pro kód i 3D scény**

r/LocalLLaMA · u/ConfidentDinner6648 · 25. října 2026, 07:10 · 418 bodů / 88 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xeuo7t/)

Autor sdílí ranou verzi čtyřmiliardového modelu zaměřeného na obecné programování a generování 3D scén. Jde o nezávislý fine-tune Qwen3.5-4B, jehož váhy ve variantách Q4_K_M i Q8_0 vystavil na Hugging Face. Sám přiznává, že malé modely v jeho testech 3D zatím nezvládaly, a teprve teď se dostal k výsledkům, které mu přišly dost dobré na ukázku. Trénink ještě běží a dataset slibuje zveřejnit v následujících dnech, aby s ním mohli experimentovat i ostatní.

Diskuse se hned stočila k tomu, jak dobrý výsledek to na čtyři miliardy parametrů je. u/killerstreak976 to označil za vážně působivé, zvlášť když za tím stojí jeden člověk, a u/Thistlemanizzle přiznal, že je to daleko lepší, než čekal, a láká ho chrlit s tím nekonečné zásoby assetů. u/Moist-Secretary641 napsal, že je to první věc, kterou na svém hardwaru rozběhl a dostal z ní opravdu dobré výsledky, u/Ylsid zase připomněl, že model na svou velikost válcuje i mnohem větší generalisty. u/Mehmet_dedeler dodal, že kdyby neznal počet parametrů, tipoval by ho minimálně na vyšší desítky miliard.

Nejhlasitější praktická linka patří Blenderu a pracovním postupům. u/Uncle___Marty popsal, jak se marně snaží donutit modely stavět modely v Blenderu a větší modely se podle něj u složitějších věcí trápí, takže specializovaný trénink vítá s velkým nadšením. u/jacek2023 poznamenal, že spousta lidí chce vidět právě Blender fine-tune a tahle velikost je hodně příjemná, u/bowdoin-yale se ptá na generování modelů pro 3D tisk. u/Successful_Net_2832 prosí autora o workflow i dataset, zajímá ho, jak data pro trénink nastavil a na co model optimalizuje, protože by podobný přístup chtěl zkusit na návrh elektroniky.

Vedle chvály zazněly i žádosti a výhrady. u/pmttyji se ptá, jestli model zvládne i 2D a zda se chystá případná 2D varianta, protože má radši 2D animované filmy než 3D. u/Tasio_ zkouší verzi Q8 a píše, že s ukázkovými prompty mu většinou nefunguje, jako důkaz přiložil obrázek auta pro rallye. Do budoucna pak víc lidí sází na malé specializované modely: u/urbanhood si je umí představit trénované na konkrétní aplikace a postupy, u/Material-Database-24 věří, že právě v tvoření a stavění mají tailor-made modely před sebou velkou éru.

Z vlákna tak zůstává obrázek drobného, ale šikovného specialisty, který lidem poprvé dává 3D generování použitelné i na slabším železe.
