# 1wpq8by
**Claude postavil 3D koně v Three.js: komunita si z toho udělala benchmark**

r/ClaudeAI · u/bursinru · 25. září 2026, 07:46 · 1531 bodů / 251 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1wpq8by/testing_claude_for_3d_creation_max_took_a_whole/)

Autor u/bursinru nechal Claude postavit běžícího low-poly koně v Three.js, procedurálně z primitivní geometrie, s animovanýma nohama, tělem, hlavou a ocasem v jediném samostatném HTML souboru. Zkoušel různé verze modelu a ptal se, která je nejlepší. Varianta Max nad úkolem počítala celou hodinu, výsledek ale komunitu nadchl.

Odkazovaný článek k příspěvku není, celé vlákno stojí na videu a na promptu z popisku. Právě jednoduchost zadání z něj udělala ideální test: jeden příkaz, jeden soubor, a kůň buď běží, nebo ne.

Diskuse se během pár hodin proměnila v neoficiální „horse benchmark“. Uživatelé házejí stejný prompt na další modely a srovnávají videa: Haiku to podle u/all43 stihl za 61 sekund, Qwen 3.8 s 27 miliardami parametrů za čtyři minuty překvapivě dobře, GPT 5.6 Sol High za čtrnáct minut a Kimi K3 Max za dvanáct. Největší pozornost má rodina Opus 5.5 — Max je vizuálně nejpůsobivější, ale u/vzakharov píše, že se mu nejvíc líbí prostřední verze a pohyby zadních nohou jsou u High dokonce lepší než u Max.

Nejvtipnější linka patří rozklepaným kouskům. Verze od Haiku dostala přezdívky od plížení se v noci od ledničky přes „corgi energy“ až po vítězného koně, který „je perfektní“. GPT 5.6 Sol High si vysloužil od u/Warm_Map_7489 pochvalu za „působivý moonwalk“ a Grok 4.7 za 26 minut komentář, že vypadá přesně tak, jak by člověk od Groku čekal. Uživatel u/EnumeratedArray se ptá, proč všechno low-poly z Three.js od Claude vypadá stejně, a u/Socially_Dead_JB_285 odpovídá, že se z toho stává nový generický styl.

Vedle legrace se řeší i vážnější pointa: přemýšlení navíc výsledku škodí. Uživatel u/all43 zkoušel Gemini 3.8 Flash a na vysoké náročnosti dostal po sedmi minutách nefunkční demo, které musel druhým promptem opravovat, zatímco stejný model na nízké náročnosti vrátil za třicet sekund lepší výsledek. Podobně u Opusu se za skutečného vítěze považuje High, který nabídne téměř kvalitu Max za zlomek času. U/cxfoulke to shrnuje, že koňský benchmark schvaluje a přijde mu užitečnější než „náhodný uzavřený benchmark číslo 445“.

Z koně v Three.js se tak stal test, který je zábavný i výmluvný zároveň: během minuty poznáte, jak model zvládá kód, animaci i zadání. A kdo by čekal konec animátorů, toho u/Candle-Jolly uklidňuje pohledem na trhané koňské nohy.
