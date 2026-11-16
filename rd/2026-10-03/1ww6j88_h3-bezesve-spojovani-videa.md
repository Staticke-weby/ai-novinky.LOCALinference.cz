# 1ww6j88
**Seamless pokračování videa v H3: workflow bez spálení**

r/StableDiffusion · u/roychodraws · 3. října 2026, 00:01 · 344 bodů / 114 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1ww6j88/)

Uživatel roychodraws zveřejnil verzi 7.1 svého workflow pro model H3 i s pomocnými nástroji na GitHubu, repozitářem minimax_wf a dvojicí splitterů na video a na kontinuální audio. Slibuje s nimi bezšvě spojovat delší videa bez spálení, respektive se stejným minimem spálení v celém materiálu, důkaz má být ve videu od času 2:00. Návody k použití odkazuje do starších tutoriálů na svém profilu.

V navazujícím vlákně s degrade workflow pak dovysvětluje princip: místo nekonečného prodlužování jedné latentní sekvence generuje po úsecích a šev přesampluje přes FL2V, čímž se degradace obejde. Drobné chyby ve střihu, třeba posunutá židle, se podle něj dají dorovnat další referencí. To druhé vlákno nasbíralo 298 bodů a 120 komentářů.

Nejvýše hodnocený komentář ale nadšení brzdí. Uživatel u/acedelgado píše, že autora považuje za fantastického, jenže tohle prý neřeší problém, se kterým lidé zápasí, a slovo přenechává Bradovi s ukázkovým videem degradace i při plném použití latentů. Na to navazuje u/not_food poznámkou, že degradace nastupuje, když je kamera statická a nehýbe se, výměna celé scény je jen obchvat. Nejvýmluvněji to podává u/ArmadstheDoom: nechápe, proč lidé nechápou jádro věci, protože pohyblivou kamerou se vada zamaskuje, ale statický záběr jako zprávy, vlog nebo rozhovor prý v současnosti bez degradace vygenerovat nejde, leda po zhruba třicetisekundových klipech. Situaci přirovnává k filmu Manos: The Hands of Fate, který se točil ruční kamerou taky jen po třiceti sekundách.

Technické vysvětlení nabízí u/WASasquatch: jde o reziduální latentní šum, žádný model prý neodšumí dokonale ani na hodnotě 1.0 a VAE pak šum při dekódování zvýrazní, což pomáhá pro img2img, ale ne pro tohle. Do praxe to převádí u/Danny_Stock zkušeností, že do deseti až patnácti sekund je výsledek přijatelný, kolem pětadvaceti sekund je problém jasně vidět a dál se jen zhoršuje. Sám autor u/roychodraws v diskusi přiznává, že tohle zatím není oprava celého problému, a vzkazuje, ať lidé vydrží.

Zbytek vlákna je směs díků a humoru kolem bizarního obsahu ukázek. Uživatel u/_VirtualCosmos_ glosuje, že jsou to zase ty jeho klaunské ženy, u/Memestonks2020 dodává, že mohlo být hůř a lidé mají být rádi, že to není furry, a u/TheJaffo si všímá camea maga psa. Mezi tím se mísí vděčné vzkazy jako od u/Hy4ne nebo u/Joethedino a autor sem tam odlehčí hláškou, že jde o clussy meme nebo že když to udělá někdo jiný, bude žalovat.

Kdo potřebuje navazovat pohybové záběry, má v ruce použitelný postup, kdo touží po dokonale stabilním statickém záběru na minuty, musí zatím počítat s postupným rozpadem obrazu.
