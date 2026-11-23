# 50597959
**Muru: autor mod_wsgi staví Rust server pro Python s pomocí AI**

Hacker News · joshcsimmons · 22. listopadu 2026, 10:57 · 75 bodů / 11 komentářů · [diskuse](https://news.ycombinator.com/item?id=50597959)

Graham Dumpleton, tvůrce mod_wsgi starého dvacet let, staví nový server Muru v Rustu. Má zvládat aplikace v ASGI i WSGI, sloužit vývoji i produkci a být podle něj nejlepší možnou cestou, jak pythonový web provozovat.

Upozornil na něj Simon Willison, který shrnul, že Dumpleton k projektu vede mimořádně podrobný vývojový deník. Za tři týdny od začátku listopadu vyšlo kolem dvaceti textů o architektuře, vnitřku workerů, společném běhu WSGI a ASGI, škálování nebo HTTPS ve vývoji. Sám autor projekt označuje za asistovaný umělou inteligencí a v textu o AI jako životní volbě píše, že AI sice dělá spoustu práce na povrchu, ale rozhodnutí, co ještě není dost dobré, zůstává na něm – a pomáhá mu v tom dvacet let chyb s mod_wsgi.

Nejživější debata se stočila k tomu, proč dnes autoři zdůrazňují, co stvořili před AI. Uživatel tamimio v tom vidí zoufalou snahu signalizovat, že člověk není jen producentem balastu, a ptá se, jestli na tom, zda někdo AI použil, vůbec záleží. Uživatel zodwick mu dává částečně za pravdu, ale přiznává, že právě jméno autora a Willisonovo doporučení ho přiměly se na projekt podívat – váhu dává spíš části „tvůrce něčeho“ než části „před AI“. Uživatel tempest_ dodává, že chlubení minulými zásluhami tu bylo vždy, jen je teď kvůli rychlosti jazykových modelů vidět častěji.

Druhá linka řeší, jak se AI píše a kde má člověk ještě místo. Uživatel d1l říká, že si Grahama váží a mod_wsgi kdysi v první pythonové práci provozoval, ale texty mu přijdou většinově generované, neohrabané a bez duše. Podobně uživatel ptx označuje generované psaní za neuvěřitelně úmorné ke čtení. Uživatel sheepscreek si ironicky všímá obratu od řečí o agentech s vlastní vůlí k tomu, že člověk má vůli nad nimi, uživatel fn-mote proti tomu staví smířlivější citát, že AI bere otravnou dřinu a nechává člověku nápady a radost z fungující věci. Uživatel bayarearefugee to shrnuje do čtyř fází od „AI je k ničemu“ přes „hlídanou užitečnost“ až po strach z nahrazení a tvrdí, že vývojáři jsou předvojem ve třetí fázi.

Technicky nejvíc zaujalo přednačtení aplikace a forkování workerů. Uživatel ptx chválí nápad připomínající Zygote z Androidu, včetně zmrazení pohledu garbage collectoru na přednačtené objekty příkazem gc.freeze(), a navrhuje zajít dál – forkovat sandboxovaného workera pro každého uživatele s vlastními právy a spojit to s řádkovým zabezpečením v PostgreSQL, aby dopad SQL injection i vzdáleného spuštění kódu byl menší. Uživatel lovasoa namítá, že proces a databázové spojení na uživatele by byly hodně drahé. Uživatel bri3d odpovídá, že model s předforkováním je docela běžný a že co je staré, je zase nové – podobně fungovaly databázové RAD systémy jako 4D nebo server IBM pro AS/400.

Z Muru tak zatím nejvíc vyčnívá kombinace známého jména, otevřeného deníku a přiznané spolupráce s AI, která část publika láká a část odrazuje od čtení.
