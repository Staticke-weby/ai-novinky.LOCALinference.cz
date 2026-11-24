# 50619630
**Shirudo: OpenAI a Cisco kryjí nezaplátovaný Linux eBPF štíty**

Hacker News · acossta · 23. listopadu 2026, 22:30 · 56 bodů / 15 komentářů · [diskuse](https://news.ycombinator.com/item?id=50619630)

OpenAI a Cisco společně vydaly Shirudo, open-source runtime pod licencí BSD 2-Clause, který má chránit běžící linuxové systémy ještě před nasazením opravy. Řešení staví na eBPF: takzvaný štít dokáže zablokovat zranitelnou cestu kódu, aniž by bylo nutné službu restartovat. V ukázkovém testu štít vygenerovaný Codexem zastavil útok Java4Shell na běžící Elasticsearch, zatímco služba dál obsluhovala legitimní provoz.

Odkazovaný článek popisuje čtyři pilíře systému: živou ochranu s možností nejprve sledovat dopad štítu a teprve pak ho vynutit, agentní vyšetřování a ověřování proti exploitům i reálné zátěži, důvěryhodné nasazení a hardwarové ověření. Štíty jsou kryptograficky podepsané a procházejí eBPF verifierem, nasazení a odebírání lze dokládat přes TPM. Dlouhodobým cílem je dodávat odzkoušené štíty společně se zveřejněním zranitelnosti a zapojit do vývoje širší komunitu.

Nejživější debata se překvapivě stočila ke jménu. Futuraperdita rýpe, že „Shirudo" je jen anglické „shield" přepsané do katakany, a qmarchi navrhuje raději skutečná japonská slova pro štít či krytí. Numpad0 dodává, že bez vyznačené délky samohlásky to bude většina Japonců číst jako „šildo", a trashcan_man si z firemního pojmenovávání utahuje přáním platit podnikové ceny za produkty typu „POLÉVKOVÉ DÍTĚ".

Za humorem ale rychle nastoupila skepse k nasaditelnosti a důvěře. P0lychromatic varuje, že plná verze vyžaduje kompletní measured boot s TPM2 a unifikovaným obrazem jádra, takže nejde o nástroj, který by člověk nasadil v nouzi za odpoledne. Rkagerer zase přiznává, že mu vadí představa, že by do jádra pouštěl kód psaný umělou inteligencí a posílal telemetrii velkému dodavateli, protože taková centrální brána láká útočníky. Cvadict to vyhrocuje do obrazu vyděračského modelu s placeným „strážným agentem" a siliconc0w přidává vlastní zkušenost, kdy mu guardrails překážely už při čistě obranném prototypování.

Nejtvrďší technický rozbor přinesl jiveturkey. Tvrdí, že navzdory nálepce nejde jen o eBPF ani o nic moc agentního: přiložené záplaty pro Javu využívají existující mechanismus Javy a daly by se pustit plošně, zatímco jaderné „mikrozáplaty" jsou až na jednu výjimku jen monitory. Ta výjimka prý funkcionalitu rovnou vypíná, takže by šlo stejně dobře vypnout software celý. Za „docela fajn" naopak označuje aplikační sandbox. Podobnou obavu o praxi formuluje fathermarz: když oheň uhasí dočasný štít, vyprchá tlak na skutečné zaplátování a týmy budou jen vrstvit další pravidla.

Z projektu tak zůstává obraz slibné berličky na dny či týdny mezi zveřejněním chyby a hotovou opravou, která ale vyžaduje vyspělou infrastrukturu a disciplínu, aby se z berličky nestala trvalá náhrada za záplatování.
