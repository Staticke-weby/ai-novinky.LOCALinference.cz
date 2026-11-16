# 1wj4yeo
**FastH3 od FastVideo je dostupný v ComfyUI**

r/comfyui · u/crystal_alpine · 17. září 2026, 22:13 · 106 bodů / 14 komentářů · [diskuse](https://www.reddit.com/r/comfyui/comments/1wj4yeo/fasth3_by_fastvideo_is_available_in_comfyui/)

Tým kolem ComfyUI oznámil, že model FastH3 od FastVideo lze nově spouštět lokálně přímo v ComfyUI. Láká na generování videa včetně nativního stereofonního zvuku v řádu sekund, přičemž ke spuštění slouží připravené šablony pro převod textu na video a obrázku na video.

Podle popisu v příspěvku se model hodí hlavně pro previzualizace a animatiky, kde je potřeba rychle zkoušet hodně variant, dále pro ověřování časování a dialogů před drahým finálním renderem a pro krátká videa na sociální sítě s napjatými termíny. Zvuk se negeneruje dodatečně, ale vzniká společně s obrazem.

Nejviditelnější ohlas patří uživateli u/Diligent-Rub-2113, který model chválí jako skvělý pro rychlé prototypování nápadů. Zároveň si posteskl, že komunita o spoustě novinek vůbec neví — zmínil podporu YuE2, zrychlení Gemma 4, nový uzel pro řídkou pozornost modelu — a poprosil o návrat rekapitulačních videí a článků na blogu, protože sledovat pull requesty, changelog, profil na Hugging Face a tisíce zpráv na Discordu každý den prostě nejde. Na to reagoval u/Leary_2844 skepticky, že komentáře pod videi stejně tvoří hlavně stížnosti na rozbité workflow, a u/DJBFilmz souhlasil, že by pomohl týdenní přehled změn.

Kritičtější linku otevřel u/IllExample3639, podle kterého výstup vypadá divně a raději by si hodinu počkal na něco použitelného. Praktickou protiváhu přinesl u/Hrmerder, který upozornil, že je potřeba aktualizovat na nejnovější stabilní verzi ComfyUI, kde se šablony objeví. První načtení do paměti mu trvalo kolem 400 sekund, ale dalších pět sekund videa pak vzniklo asi za 40 sekund, což mu na rychlou práci přijde slušné a výsledek podle něj vůbec nevypadá zle. Podobně uvažuje u/TheMoogster, který se ptá, zda smyslem těchto rychlých modelů není právě rychlé otestování promptu před pořádným během.

Zbytek vlákna řeší kvalitu a srovnání s konkurencí. U/ResponsibleTruck4717 hlásí hodně špatné výsledky u převodu obrázku na video, u/Puzzleheaded_Art2809 si jako začátečník pochvaluje kombinaci pracovního postupu diffusion model fast s výchozím modelem int8 a LoRA hardgravy2, která mu drží rychlost a přitom vypadá znatelně lépe. U/GeroldMeisinger se ptá, jak novinka souvisí s žebříčkem H3 Acceleration, kde FastH3 vychází hůř než jiné metody, a proč nevyužít vítězné turbo LoRA. U/Luke2642 se zase ptá na roadmapu pro opravy a workflow pro video upscale Seedvr2 7B přes comfy-kitchen a u/RaspberryNo6411 prosí o srovnání FastH3 v2 s LTX 2.5 a původním int8 H3.
