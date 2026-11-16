# 50079464
**AlphaNIST: Nvidia a univerzita ve Washingtonu učí robota vysoké přesnosti**

Hacker News · jasonjmcghee · 13. října 2026, 23:57 · 58 bodů / 19 komentářů · [diskuse](https://news.ycombinator.com/item?id=50079464)

Na přední stránku Hacker News se probojoval odkaz na AlphaNIST, společný projekt Nvidie a University of Washington. Uživatel jasonjmcghee ho vyvěsil bez vlastního textu, jen s odkazem na doprovodný blog k jejich práci o posilovaném učení pro vysoce přesné robotické úlohy. Terčem je standardní montážní výzva amerického úřadu NIST, tedy zasouvání kolíků, utahování matic a manipulace s drobnými díly.

Samotná stránka ukazuje chování naučené v simulaci. V jednom záběru chapadlo položí osmimilimetrový kolík a znovu ho uchopí u samého konce, aby mu na zasunutí zůstala co nejdelší volná část. Právě takové finty bez explicitního programování autoři vydávají za hlavní lákadlo.

Největší rozruch vzbudil název. Mr_P se diví, proč si práce Nvidie s univerzitou přivlastňuje „Alpha", které historicky znamenalo Google DeepMind, a k tomu „NIST", jež si mnozí spojí se sadou pro rozpoznávání znaků. Přidává se geerlingguy s povzdechem nad přetížením zkratek a sdenton4 s žertem, jestli DeepMind vyřešil celý úřad pro standardy. Do vlákna proto vstoupil jeden z autorů, romesc, a vysvětlil, že jde o poctu skupině Davida Silvera z let 2016 až 2018, na které jeho generace vyrostla. Připustil, že přenos na skutečný hardware v téhle práci ještě chybí, ale odkázal na novější výsledky chystané pro konferenci CoRL.

Věcná linka patří samotnému učení. Wasabi991011 chválí nápad startovat trénink z různých míst úlohy a přednostně vzorkovat startovní stavy podle dosavadního úspěchu a ptá se, jak je to nové. Romesc odpovídá, že mechanismus má blízko ke curriculum learning a v metodickém doprovodném textu ho srovnávají s postupy PLR, SFL a ručně navrženými plány. Slibuje, že princip zkusí příště vysvětlit na jednodušším příkladu, aby byl srozumitelnější.

Zbytek diskuse řeší, jak daleko je to k reálnému nasazení. BoppreH nadchlo cvrnkavé chování a organické pohyby chapadla, zároveň upozorňuje, že robot vidí mračna bodů, tedy téměř celý stav simulace kromě rychlostí, a v omezeních práce se otevřeně píše, že chybí odolnost vůči chybám vnímání, latenci a nepřesnosti kontaktního modelu. Amluto baví způsob, jak robot utahuje matice, o kterém pochybuje, že by prošel ve fyzickém světě, a varuje, že statisíce pokusů s drobnými díly by znamenaly neustálý úklid a rozbité vybavení. Hansmoravec se proto ptá, kolik inženýrské práce s modely a laděním identifikace systému si vyžádal přenos na skutečného robota. Squanch pak celou podívanou uzavírá přirovnáním, že chapadlo hrající si s dlouhými díly mu připomíná pohyb koňské hlavy.
