# 1xiz1vy
**Global Law převádí zákony celého světa do git historie. Kód napsal Claude**

r/ClaudeAI · u/SnooPeripherals5313 · 30. října 2026, 00:00 · 736 bodů / 70 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xiz1vy/)

Autor představil projekt lexifina/global-law, který ukládá zákony jednotlivých zemí do git historie tak, že jeden commit odpovídá jedné změně účinné k danému datu. Cílem je udělat z práva sémantická, verzovaná a dohledatelná data, na která se dá odvolat po slovech a která mohou dotazovat i agenti. Téměř celý kód přitom napsal Claude Code s modelem Opus 5.5, autor si podle vlastních slov nechal na starost cíle, výběr zdrojů a designová rozhodnutí.

Přiložený popis na GitHubu vysvětluje, že repozitář je pod licencí CC0 a každá jurisdikce v něm žije ve vlastním repozitáři připojeném jako submodul, přičemž dějiny všech zemí se prolínají do jedné časové osy podle data účinnosti. K tomu patří skript law.py a server s osmnácti nástroji, které umí říct, co platilo k určitému datu, kdo které slovo napsal nebo jak se paragraf mezi dvěma daty změnil. Pokrytí se přitom hodně liší, Česko, Španělsko nebo Švýcarsko mají celou sbírku, americký korpus tvoří jen devět hlav zákoníku a britský zatím jen zákon o speciálních vzdělávacích potřebách.

V diskusi převládlo nadšení. u/shableep píše, že sledovat historii změn zákonů by se mohlo hodit obrovskému množství lidí, u/whatiseveneverything láká rychlé srovnávání zemí a hledání trendů v čase a u/sordimin to shrnuje hláškou, že jediná sbírka zákonů pro všechny země by prostě měla být na GitHubu. Největší ohlas přitom sklidil údiv u/MassiveBoner911_3 nad rozsahem dějin, které čítají 339 000 commitů.

Zároveň se rychle ozvali ti, kdo hledali vlastní zemi. u/elhombremontana píše, že z Rakouska našel jen ústavu a zákon o ochraně dat, tedy zlomek toho, co by čekal, další se ptají po zákonech Quebecu nebo Arizony. Podobnou linku drží u/Professional_Split14, podle kterého nic jako britské právo neexistuje a databáze bude muset rozplést právo Anglie a Walesu, Skotska a dalších jurisdikcí.

Nejvěcnější spor vedou právníci kolem toho, co v gitu chybí. u/Able-Okra7134 vysvětluje, že legislativa je jen půlka práva a v zemích s obecným právem ji neustále přetváří judikatura, která se navíc často schovává za placenými službami, a ptá se, jak by systém zvládl data vyhlášení, přechodná ustanovení nebo prováděcí předpisy. Na to navazuje u/grateful2you s námitkou, že právo není pevný seznam dokumentů, ale živá věc, kde záleží na přesnosti a aktuálnosti, a u/Unlucky_Quote6394 dodává, že brzy bude potřeba řešit i soudní rozhodnutí. Mezitím to u/SteveDougson otočil do žertu, jestli mu Claude konečně spočítá, zda Batman porušil zákon, když na konci Batman začíná nechal zemřít Ra'se al Ghula.

Z vlákna tak zůstává obraz velké ambice s dírkami na mapě: strojově čitelná historie zákonů nadchla i skeptiky, ale než z ní budou moci vycházet agenti i lidé, bude muset dorůst pokrytí zemí a najít odpověď na judikaturu.
