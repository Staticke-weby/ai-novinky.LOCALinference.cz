# 1wixzts
**XGBoost proti lidským trhům**

r/MachineLearning · u/TravalonTom · 17. září 2026, 17:59 · 0 bodů / 16 komentářů · [diskuse](https://www.reddit.com/r/MachineLearning/comments/1wixzts/xgboost_vs_human_markets_p/)

Autor trénuje XGBoost na dostizích, konkrétně na horizontálních sázkách, a snaží se přiblížit přesnosti sázkového trhu. Modelu dává stejné informace, jaké má k dispozici trh, jenže v přesnosti Top 1 dostává pořádně na frak a v Top 2 ztrácí zhruba deset procentních bodů. Přidání kurzových informací do modelu přitom nepomáhá, spíš přesnosti škodí, a tak autor tápe, jestli naráží na strop možností XGBoostu, na špatné kódování dat, nebo mu jen chybí data.

Nejvýše hodnocený hlas patří u/marr75, podle kterého je už samotné zadání postavené na vodě: trh ani agregát lidí nejsou pořádně definované pojmy. XGBoost podle něj neumí předpovídat náhodné jevy, neumí si sám shánět informace, nemá tělo ani životní zkušenost a okolní kontext, zatímco lidé všemožně podvádějí a často jsou sami členy komunity, která trhem hýbe. Nová vnější proměnná tak model položí, kdežto lidé se jen na chvíli zarazí.

Do podobného místa míří i další věcná linka vlákna. u/currentscurrents píše, že krmit model stejnými informacemi, jaké má trh, je právě ten problém: kdo chce trh porazit čímkoli, potřebuje informace, které trh ještě nemá, protože všechno veřejně známé je už v kurzech započítané. u/gwern k tomu dodává, že v každém skutečném trhu už účastníci dávno pustili na snadno dostupná data XGBoost nebo něco lepšího, takže odkud by se měla vzít výhoda. Autor se v odpovědích ptá, jestli by trh šlo se správně zakódovanými informacemi aspoň dorovnat a kolik dat by na dosažení větších populací potřeboval.

Teoretičtější kontrapunkt přidává u/relevantmeemayhere: stromové modely jsou stejně jako sítě, spliny nebo gaussovské procesy univerzální aproximátory, na samotném XGBoostu tedy nic zvláštního není. Jenže to platí, jen když se nehromadí chyba ze špatně zadaného modelu, a trhy jsou nestacionární, takže ani XGBoost naroubovaný na dobrý stavový model pravý signál nedožene. Autor by prý byl nadšený, kdyby se mu podařilo dorovnat běžnou moudrost, zatím ale všechno ukazuje na to, že napodobit nejpřesnější model, tedy samotný trh, stejnými veřejnými daty prostě nejde.
