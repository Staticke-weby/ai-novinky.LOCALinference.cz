# 50220042
**Root na TCL Android TV přes zranitelnost Mali**

Hacker News · t20n · 24. října 2026, 12:51 · 55 bodů / 18 komentářů · [diskuse](https://news.ycombinator.com/item?id=50220042)

Uživatel t20n vyvěsil odkaz na gitlabový projekt mali-pagecache-root, který slibuje autonomní získání roota na televizích TCL s Android TV. Stojí na zneužití zranitelnosti v grafických čipech Mali označované jako CVE-2022-22706. Má jít o hotový postup pro majitele, kteří chtějí převzít kontrolu nad vlastní televizí.

Samotný repozitář je podle popisu v diskusi vesměs pod permisivní licencí MIT, jedinou výjimkou je výňatek z jádra v souboru kernel/mem.c. Ten si ponechává původní licenci GPL-2.0 včetně údajů o autorských právech. Právě tahle dvojkolejnost později rozpoutala licenční přestřelku v komentářích.

Největší ohlas má prosté konstatování uživatele Hydraulix989, že by měl mít root na televizi, kterou si koupil, zaplatil a vlastní. Uživatel kyriakos ho rozšiřuje na mobily a tablety a diví se, že spousta lidí přitom velké firmy za zamykání hájí. Uživatel zug_zug souhlasí a dodává, že takovéto hackování je podle amerického zákona DMCA zcela jasně legální, jen je škoda, že vyžaduje tolik práce.

Praktický protipól přidává uživatel BLKNSLVR, který má TCL s Android TV doma. Stačil mu přístup přes ADB, tedy bez roota, aby vyměnil výchozí launcher: domovská obrazovka je pak jen hezké pozadí a aplikace, které chce, a žádné reklamy. Root zatím nepotřebuje i proto, že nechce z hlavní televize v obýváku udělat cihlu, s hraním si počká, až se televize přesune na vedlejší kolej a objeví se televizní obdoba LineageOS.

Zbytek vlákna se dělí mezi techniky a nostalgiky. Uživatel realusername poznamenává, že pokud televize opravdu běží na kombinaci Android 11 a Linux 4.4, bude na ni pravděpodobně fungovat spousta rootovacích exploitů. Uživatel shakna zase řeší, že GPL-2.0 je nakažlivá a měla by se vztahovat na celé dílo, zatímco uživatel pessimizer oponuje, že kód pod MIT lze bez problémů šířit i pod GPL-2.0, a uživatel tadfisher připomíná, že nakažlivost se týká šíření kombinovaného díla. Do toho uživatel zb3 vzpomíná, jak kdysi hacking znamenal vloupávání do cizích systémů, a dnes se zranitelností dobývají výrobky, které člověk vlastní, na což uživatel basilikum odvětí, že hacking vždycky znamenal tvořivé a zvídavé použití techniky.

Čtenář si z toho odnese, že root na televizi je pro část komunity otázkou vlastnictví, pro část otázkou pohodlí, které často vyřeší i obyčejné ADB bez rizika.
