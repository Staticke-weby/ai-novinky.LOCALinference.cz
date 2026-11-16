# 50447074
**Anthropic našel tisíce zranitelností. VulnCheck: opraveno je jen 217 z nich**

Hacker News · panic · 10. listopadu 2026, 23:17 · 366 bodů / 168 komentářů · [diskuse](https://news.ycombinator.com/item?id=50447074)

Sedm měsíců po startu projektu Glasswing eviduje VulnCheck 442 zranitelností CVE připisovaných Anthropicu, tedy zhruba půl procenta všech letošních CVE. V praxi byly podle sledování služby VulnCheck KEV zneužity pouze dvě z nich, takže dramatický obraz éry automatického objevování zranitelností zatím neodpovídá realitě.

VulnCheck ve své listopadové bilanci rozebírá především firemní ledger: z 37 966 nahlášených nálezů je veřejných 7 349, tedy 19,4 procenta, a jako opravené je označeno jen 217 případů. Od září Anthropic přidal téměř 12 tisíc nálezů, ale zaznamenal pouze 15 dalších oprav, takže rozdíl mezi objevováním a odstraňováním se dál zvětšuje. Zhruba 1 654 nálezů firma označila za duplicity, což je téměř osmkrát více, než kolik jich bylo opraveno, a projekt OSS Scanner přesunul třídění na správce – u curlu bylo 19 ze 34 zveřejněných hlášení odmítnuto a šest potvrzeno jako nízká závažnost. Tím autor zpochybňuje uváděnou míru skutečných pozitiv, která mezitím stoupla z 90,8 na 94,2 procenta.

Diskuse se nejdřív stočila k tomu, kde je slibovaná katastrofa. Uživatel fny píše, že nejvýmluvnějším signálem planého poplachu je absence ničivých útoků, které by tyto nálezy způsobily. Odpovědi mu ale oponují: tensor připomíná týdenní rytmus velkých úniků u právních firem, vývojářských platforem i firem všeho druhu, stavros mluví o odhalování kritických chyb skoro obden a qnleigh varuje, abychom si vzhledem k rychlosti pokroku nic takového nepřáli.

Druhá větev řeší, co čísla vůbec říkají. Uživatel dfee namítá, že jde o analýzu přeživších, protože většina nálezů je stále pod embargem a o neveřejném zbytku nelze nic soudit. ASalazarMX to vysvětluje zahlcením lidí ve smyčce a chtěl by po nejlepším kódovacím modelu i návrhy oprav, zatímco jknoepfler soudí, že kdyby šlo o zlatý důl, firma by frontu na kontrolu dávno odbavila. Uživatel jrflo pak rýpne, že závěr článku podezřele ladí s byznysmodelem VulnChecku, který čtenáře hned pod textem zve ke koupi prioritizace zranitelností.

Třetí linka je pro mnohé nejpodstatnější: co když umělá inteligence bude trvale lepší v bourání než ve stavění. Uživatel delichon se obává rostoucího poměru nálezů a oprav, shiandow dodává, že je potřeba být velmi opatrný, když model iteruje na kódu, dokud sám nehlásí žádné problémy. InsidiousWombat oponuje, že s dokumentovaným testem je umělá inteligence v opravách velmi dobrá, pokud se na kód podívá člověk. Do toho zapadá i zkušenost správců: pratzc07 čekal přesně tohle zahlcení nicneříkajícími hlášeními a snowwrestler s timr popisují současné agenty spíše jako vytrvalou průměrnost s nekonečnými znalostmi než jako roj superhackerů.

Z článku tak zůstává rozpor mezi tisíci nálezy a hrstkou dotahovaných oprav, který tíží právě open source správce, jimž měl projekt původně pomáhat.
