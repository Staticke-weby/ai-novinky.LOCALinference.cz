# 50155245
**Mercury 3: difuzní LLM, který běží několikrát rychleji**

Hacker News · cmrdporcupine · 19. října 2026, 19:27 · 239 bodů / 85 komentářů · [diskuse](https://news.ycombinator.com/item?id=50155245)

Startup Inception Labs představil Mercury 3, který označuje za dosud nejschopnější velký jazykový model postavený na difuzi. Odkaz na firemní blog se na Hacker News rychle chytil a přitáhl i spoluzakladatele firmy, který přišel do diskuse odpovídat na dotazy.

Podle oznámení firma více než čtyřicetkrát zvětšila parametry oproti Mercury 1, aniž by model zpomalil. Na benchmarcích má překonávat GPT-6 Luna a Claude Haiku 5.5 a běžet čtyřikrát až osmkrát rychleji, přes tisíc tokenů za sekundu. Konkrétně firma uvádí 1 068 tokenů za sekundu na grafických čipech Nvidia, kontext milion tokenů a zaváděcí cenu 0,10 dolaru za milion vstupních a 0,35 dolaru za milion výstupních tokenů. Ranní partneři ho nasazují na hlasovou a chatovou podporu, doučování v reálném čase, datové úlohy a ovládání webu.

Do vlákna dorazil i Volodymyr, spoluzakladatel a vědecký šéf Inception, s vysvětlením hlavní teze: difuze škáluje. Tokeny se negenerují jeden po druhém, ale paralelně přes opakované odšumování, takže čím déle uvažující modely přemýšlejí, tím víc roste náskok nad autoregresivními modely stejné velikosti. Nabídl 100 milionů tokenů zdarma na vyzkoušení a kompatibilitu s OpenAI API, zájem byl ale hlavně o to, co firma neřekla.

Nejčastěji se opakovala jedna otázka: jak je model velký a budou váhy k dispozici. Ptali se na to Jacquesm, AmazingTurtle i WithinReason, loufe zase zajímalo, čím se trénink lišil od klasického modelu. Naději na otevřené váhy rychle zchladil SillyUsername povzdechem, že na takový model stále čeká, a moonu si postěžoval, že novince chybí multimodalita. Praktičtěji se ptal AmazingTurtle na tool calling a agentní harness a ttul na kódování, kde Mercury 3 v DeepSWE zaostává za Haiku 46 procenty proti 52 procentům.

Nejvěcnější spor se vedl o škálování v provozu. LarsDu88 připomněl výzkum Googlu, podle kterého výhoda difuze mizí při větších dávkách, a ptal se na čísla propustnosti podle velikosti dávky. Famouswaffles a clhodapp to rozvedli: Diffusion Gemma prý na těžších úlohách ztrácela čím dál víc a z dávkování netěží tak jako klasické modely, takže je skvělá na latenci pro jednotlivce, ale dražší na token ve velkém. Do toho zapadla i poznámka simonw, proč Google po loňské rychlé ukázce Gemini Diffusion vlastně ztichl. Optimističtější tón dal UncleOxidant, který Mercury 3 rovnou zkusil na vlastním repozitáři a byl mile překvapen, zatímco snake_doc namítl, že na OpenRouteru mu přijde pomalejší v nástupu první odpovědi než DeepSeek V4.1 Flash.

Z celé výměny tak zůstává obraz slibné, ale zatím uzavřené cesty: rychlost je reálná, otevřenost a chování ve velkém provozu se teprve musí prokázat.
