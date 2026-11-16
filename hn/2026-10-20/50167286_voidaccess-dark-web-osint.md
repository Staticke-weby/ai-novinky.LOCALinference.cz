# 50167286
**VoidAccess: open-source OSINT pro temný web s výstupem do grafu**

Hacker News · coding-maniac · 20. října 2026, 16:49 · 127 bodů / 13 komentářů · [diskuse](https://news.ycombinator.com/item?id=50167286)

Na Hacker News se představil Katriel, bezpečnostní výzkumník a nadšenec, s nástrojem VoidAccess. Podle vlastních slov chtěl ve vlně umělé inteligence postavit novou generaci bezpečnostních nástrojů jako otevřený engine, který překoná i placené produkty. VoidAccess vznikl proto, že obsah temného webu se prý pro člověka ručně prochází jen těžko: instalace má být na pár příkazů a pak už čištění šumu a filtrování nevhodného obsahu přebírá engine, který běží až do hotového výsledku nebo do uživatelem nastaveného limitu.

Stránka projektu na GitHubu ho popisuje jako samostatně provozovatelný Python nástroj, který z výzkumného dotazu udělá strukturované zpravodajství o hrozbách. Paralelně prohledává Tor indexy, paste servery, code forges a bezpečnostní feedy, z nalezených stránek vytahuje entity od indikátorů kompromitace přes peněženky a přihlašovací údaje až po zranitelnosti, aktéry a organizace. Ty pak obohacuje o reputační, breach, passive DNS, sandboxová a blockchainová data a ukládá je jako aktéry a vztahy, takže z pátrání vzniká graf souvislostí s exporty od STIX přes MISP až po YARA či pravidla pro Snort a Suricata.

Nejhlasitější reakce v diskusi byla nedůvěřivá. Uživatel sandworm101 napsal, že to působí jako nástroj napsaný umělou inteligencí a oznámený oznámením od umělé inteligence, přičemž pár překlepů už dnes nikoho nepřesvědčí. Uživatel berofeev k tomu přidal, že všude jsou i falešné komentáře.

Proti skepsi se ozval uživatel varman11, který napsal, že se na repozitář podíval a přijde mu docela zajímavý. Autor mu poděkoval a oplatil mu kompliment. Věcnější linku otevřel uživatel girishkvs otázkou, zda může autor sdílet nějaké zajímavé bezpečnostní reporty – coding-maniac odpověděl odkazem na vlastní hlubší pátrání o ransomwaru a trhu s přístupem, který podle něj živí každý ransomwarový útok.

Technicky nejdál zašel uživatel CreepyHunterX. Ptal se, podle čeho se záznamy slučují do jednoho uzlu – zda podle sdíleného PGP klíče, kryptoměnové adresy, nebo zda má každý zásah vlastní uzel – a co se stane, když stejnou přezdívku náhodou používají různí lidé.

Vlákno tak zůstalo napůl mezi zvědavostí na automatizované pátrání v temném webu a pochybností, zda za uhlazeným představením stojí skutečná práce analytika.
