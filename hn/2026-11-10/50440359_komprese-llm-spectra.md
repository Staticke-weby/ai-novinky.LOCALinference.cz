# 50440359
**Komprese LLM na třetinu. Neuracryption slibuje běh pod 50 MB RAM**

Hacker News · anushka_gandhi · 10. listopadu 2026, 14:51 · 34 bodů / 33 komentářů · [diskuse](https://news.ycombinator.com/item?id=50440359)

Společnost Neuracryption představila SPECTRA, kompresní engine, který má zmenšit velké jazykové modely zhruba na třetinu téměř bez ztráty kvality. Komprese má fungovat bez kalibrace, s Group-32 mikroškálováním a 4bitovou kvantizací, a to i pro architektury typu Mamba-2 nebo SSM hybridy. Celé to má běžet na CPU a vystačit si s méně než 50 MB RAM, takže by se hodilo i pro malá zařízení.

Odkazovaná výzkumná stránka staví příběh na takzvané memory wall. Na mobilní RTX 3050 Ti se sedmimiliardový model v FP16 fyzicky nevejde do 4 GB videopaměti a odkládání vrstev do systémové RAM přes PCIe Gen3 x4 sráží generování na 0,28 tokenu za sekundu. SPECTRA na to odpovídá teorií o Shannonově kódování, bezkalibračním vyhledáváním citlivých kanálů z normalizačních vah a vlastními jádry pro 4bitové maticové operace.

Diskuse je k tomu výrazně opatrná a velká část se hned stočila k formě stránky. Uživatel ngruhn si stěžuje na odbytý design, uživatel whizzter přiznává, že ho stránka na první pohled odradila, a uživatel fishfasell píše, že poznal generativní rozhraní na první pohled a že to podrývá důvěryhodnost celého projektu. Autorka mu odpovídá, že web vznikl v Gemini, protože jako výzkumnice neumí pořádně HTML a věnovala se raději obsahu.

Věcnou linku otevřel uživatel Aurornis, podle kterého jde o jazykovým modelem vygenerované šarlatánství, protože odhození dvou třetin vah nemůže být téměř bezeztrátové. Na stránce prý nenašel kvalitativní testy, jen rychlostní, a tvrzení o stoprocentním běhu v GPU u modelu, který se tam nemůže vejít, mu nedává smysl. Uživatel goodmythical k tomu dohledal, že za vším stojí nedávno registrovaná NeuraCryption Private Limited bez předchozích publikací a že kód zatím vypadá jako běžný kvantizér, u kterého není jasné, jak by dokázal stlačit desítky gigabajtů vah na třetinu jen s 50 MB paměti.

Zbytek vlákna řeší praktický přínos. Uživatel velox se ptá, v čem je to lepší než existující 4bitový kvant téhož modelu, uživatel hedora zase zjišťuje, zda by šla metoda skládat s už kvantovaným modelem do pásma půl až půldruhého bitu. Autorka vysvětluje, že vstupem musí být váhy v BF16, jinak model degraduje a halucinuje, a že hlavní výhoda je rychlost: komprese trvá sekundy místo pěti až deseti minut a nevyžaduje řešit tokenizer. Uživatel tor0ugh to shrnuje slovy, že to zní až příliš dobře a někde musí být háček, zatímco uživatel Roark66 by chtěl férové srovnání třeba na Qwenu střední velikosti proti běžné kvantizaci kolem 4,5 bitu.

Kdyby se sliby potvrdily, šlo by o významný posun pro lokální inferenci na spotřebitelském hardwaru, zatím ale vlákno čte SPECTRA spíš jako firemní výzkumnou stránku bez nezávislého ověření.
