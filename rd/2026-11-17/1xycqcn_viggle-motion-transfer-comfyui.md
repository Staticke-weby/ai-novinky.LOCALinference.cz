# 1xycqcn
**Viggle motion transfer v ComfyUI: přenos pohybu na 6 GB VRAM**

r/comfyui · u/cgpixel23 · 17. listopadu 2026, 07:00 · 253 bodů / 16 komentářů · [diskuse](https://www.reddit.com/r/comfyui/comments/1xycqcn/)

Autor v r/comfyui zveřejnil plně automatizovaný workflow pro přenos pohybu postavy v ComfyUI, který funguje už na 6 GB VRAM. Stačí dodat referenční obrázek libovolné postavy a video s pohybem, výsledek pak pohyb z videa přenese na zvolenou postavu s překvapivou přesností. Nízké nároky zajišťuje INT8 ConvRot verze modelu Viggle, alternativně lze použít LoRA, která přepíná MiniMax H3 Ref2V do režimu Viggle.

Celý postup je stavěný na co nejmenší námaze: uživatel nahraje referenci postavy, nahraje pohybové video a zvolí délku výstupu, o zbytek se postará integrovaný systém Qwen VL, který video analyzuje a sám připraví prompty. Protože Viggle generuje jen v 480p nebo 720p, přidal autor do workflow i upscaling přes RelayVSR. Pětisekundové video ve 480p se na jeho sestavě počítá zhruba dvacet minut a kompletní workflow i s videonávodem dal ke stažení přes Drive a Civitai.

Nejživší debata se stočila k věrnosti obličejů. u/Far_Patience4517 chválí, že výsledek vypadá opravdu dobře, ale všímá si, že všechny postavy ve videu mají prakticky stejný obličej, a navrhuje promptem lépe držet proporce tváře a těla z reference. Podobně u/cenn_john píše, že u druhé dívky se identita tváře úplně ztratila, a u/seppe0815 první proměnu rovnou označuje za nepovedenou.

Druhá linka vlákna řeší, co workflow umí a kde naráží na limity. u/Medical-Ad-1058 se ptá, jestli zvládne pohyb úst při zachování zubů, a u/toooft zajímá, zda lze proti původnímu videu něco změnit, třeba předmět držený v ruce. u/somewherePastExit9, kterého dosud odrazovala složitost podobných postupů, se ptá na delší klipy a na to, zda postava po chvíli nezačne ujíždět a drží konzistenci.

Zaznívají i praktické zkušenosti s rychlostí a vzhledem. u/Aileana06 workflow vyzkoušela, výsledky byly podle ní opravdu dobré, jen render trval dost dlouho, zatímco u/sky_shazad chválí povedené ukázkové video. Kritičtější je u/Justify_87, kterému vadí statické pozadí, a hned dva diskutující se vracejí k času výpočtu – u/Tobia96 zajímá, zda dvacet minut za pětisekundový klip zahrnuje i krok čtení videa přes Qwen VL, nebo jen samotnou generaci ve Viggle.

Pro majitele slabších karet je to hlavně praktický návod: pohyb z videa na vlastní postavu bez složitého promptování a bez potřeby špičkového hardwaru, jen s delší čekací dobou a s kompromisy v identitě tváře.
