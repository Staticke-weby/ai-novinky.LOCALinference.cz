# 50562320
**Onlook: open-source plátno nad skutečným kódem pro designéry**

Hacker News · D_R_Farrell · 19. listopadu 2026, 17:34 · 102 bodů / 72 komentářů · [diskuse](https://news.ycombinator.com/item?id=50562320)

Onlook je desktopová aplikace, která pokládá nekonečné plátno přímo nad skutečný kód a nechává na něm pracovat designéry. Projekt z YC W25 prošel kompletní přestavbou na agentní designový nástroj a zakladatel Daniel ho představil jako open source. Podpořilo ho přes 25 tisíc designérů a vývojářů, přispělo víc než 100 lidí a dvakrát byl nejtrendovějším repozitářem světa.

Podle popisu na GitHubu jde o bezplatný lokální editor, který otevře libovolný Git repozitář na počítači, spustí vlastní vývojový server a živou aplikaci ukáže v rámech na plátně. Designér si nepřináší nový model, ale připojí účet Claude Code nebo ChatGPT/Codex, který už platí, a ten přímo přepisuje soubory v repozitáři. Výsledek lze vyvést jako soběstačné HTML, PNG, JPEG nebo PDF a každou změnu poslat jako pull request k posouzení nebo zahození, takže nevznikají makety, které by musel někdo znovu stavět.

Nejživější část diskuse je srovnávání s konkurencí. Uživatel artur_makly se ptá, čím se Onlook liší od pen.dev, a Daniel odpovídá, že Pen vsadil na vlastní formát souborů, takže práce na plátně je vždy jen kopií toho, co se nakonec nasadí. Onlook chce být naproti tomu jedna ku jedné bez překladové vrstvy mezi tím, co designér vidí, a tím, co se odešle. Podobně odpovídá na dotaz na Figmu: ta je podle něj mistrem vektorového editoru, ale kódové funkce budou vždy jen doplňkem, zatímco Onlook je od začátku stavěný jako nativní pro kód a lokální práci.

Druhá linka řeší, k čemu je plátno dobré, když už lidé navrhují v Codexu nebo v Claude. Uživatel Joshearle1 popisuje, že v Codexu ladí hrubé nápady i detaily přímo v kódu, a ptá se, co je po prvním návrhu lepšího v Onlooku. Uživatel thebrubaker vysvětluje, že jde o stejného agenta i stejnou session, jen zabalenou do plátna, kde lze držet vedle sebe varianty, stavy a stránky a rychle mezi nimi přeskakovat. Na podobnou otázku, jakou výhodu má nástroj proti návrhovému režimu Claude, Daniel říká, že ten je spíš plátnem artefaktů na skicování, zatímco Onlook je vývojové prostředí pro běžící aplikaci.

Třetí téma je praktické: peníze, jednotvárnost a šablonovitost výstupů. Na otázku uživatele RyanShook ohledně byznys modelu Daniel píše, že aplikace je zatím zdarma a do budoucna chystá placenou spolupráci, cloudové funkce a služby jako generování obrázků, vektorů nebo fontů, případně specializované sandboxy pro rychlé nápady. Uživatel husseinhb si stěžuje, že agenti kreslí pořád stejné šablony a kazí vrstvy, a ptá se po vzorech od skutečných designérů. Odpověď zní, že pomáhají reference na plátně, vlastní balíčky designových pravidel a snadné přenášení zahozených artefaktů mezi projekty.

Z kombinace otevřeného kódu, vlastního agenta a práce nad živou aplikací tak v diskusi vychází nástroj, který nechce designéry učit terminál, ale přenést jejich způsob přemýšlení v obrazech a variantách přímo do kódu.

Zpět na [denní přehled](00-index.md).
