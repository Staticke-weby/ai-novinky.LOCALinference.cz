# 50471310
**Expo Simulators dává agentům cloudový iOS simulátor**

Hacker News · szdziedzic · 12. listopadu 2026, 18:53 · 24 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50471310)

Expo spustilo službu Expo Simulators, která agentům, CI úlohám i běžným členům týmu na povel přichystá cloudový iOS Simulator nebo Android Emulator. Běží odkudkoli, nepotřebuje Mac ani lokální virtualizaci a nežere paměť notebooku, každá session přitom dostane vlastní virtuální stroj, takže si paralelní agenti navzájem nepřekážejí. Služba je odteď obecně dostupná na všech placených plánech.

Odkazovaný článek ji rámuje jako odpověď na ověřování, které se stalo novým úzkým hrdlem vývoje: agent má svou práci rovnou předvést, ne jen tvrdit, že funguje. Proto každá session sbírá video z celého běhu, screenshoty, logy, síťový provoz i vytížení CPU a paměti, agent to může sledovat v reálném čase a člověk si to později přehraje v prohlížeči na počítači i na mobilu. Agent přitom nemusí umět nic nového, vzdálený simulátor ovládá stejnými příkazy agent-device, Argent nebo Appium jako ten lokální, a hodí se pro něj Claude Code, Codex, Cursor i jakýkoli agent umějící spouštět příkazy v příkazové řádce.

Diskusi odstartoval sám szdziedzic, který se představil jako vedoucí vývoje Expo Simulators a nabídl, že tu zůstane odpovídat na dotazy. Jeho vzkaz je prostý: agenti si do cloudu nainstalují build, proklikají aplikaci a vrátí nahrávku obrazovky jako důkaz práce, a funguje to s jakoukoli mobilní aplikací běžitelnou na iOS simulátoru či Android emulátoru bez ohledu na framework.

Většina vláken pod tím je čisté nadšení z toho, že simulátory konečně zmizí z vlastního stroje. buildwithtori si pochvaluje, že už nemusí mít na počítači spuštěný „milion simulátorů", chunreaction dodává, že mu to zachrání počítač, a colinhunt píše, že agenti na jeho počítači byli v běžné vývojové smyčce v pohodě, ale přesně tohle potřeboval pro agenty běžící na pozadí. Podobně ladí i krátké výkřiky schroedernathan, dhmun00 nebo sammywen, kteří službu označují za skvělou a šíleně hustou.

Jediná věcná odbočka patří vývoji bez Applu. pageofswrds se ptá, jestli takhle půjde stavět iOS aplikace z linuxového stroje, a szdziedzic odpovídá kladně: agenti běžící na Linuxu si práci ověří proti vzdálenému cloudovému iOS simulátoru a člověk si výsledek zkontroluje ručně v živém náhledu simulátoru přímo v prohlížeči.

Pro čtenáře je v tom jednoduchý vzkaz: lokální simulátor stačí jednomu agentovi na vlastním stroji, ale jakmile se agenti rozutečou do cloudových sandboxů a CI, potřebují simulátor, který běží s nimi.
