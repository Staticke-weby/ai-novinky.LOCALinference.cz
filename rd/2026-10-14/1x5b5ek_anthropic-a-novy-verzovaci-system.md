# 1x5b5ek
**Anthropic nahrazuje git vlastním systémem pro správu kódu**

r/ClaudeAI · u/Key-Cranberry6537 · 14. října 2026, 00:47 · 858 bodů / 162 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1x5b5ek/)

Autor nasdílel inženýrský blog Anthropicu o redesignu správy zdrojového kódu. Firma v něm oznamuje interní systém Scion, který za pět měsíců plně nahradil git v jejím monorepu, spolu s novým nástrojem pro code review zvaným Antique.

Podle textu už psaní kódu není úzkým hrdlem, tím je infrastruktura stavěná pro lidské měřítko: správa zdrojáků, buildy a CI. V květnu 2026 Anthropic slučoval kolem 2 500 změn denně, v září už přes 30 000 denně, a poptávka prý dál poroste. Historie hlavní větve má sama skoro 100 GB, firma denně dělá kolem 25 milionů checkoutů pro CI a dřívější stovky interních git mirrorů už přestaly stačit.

Nejvíc hlasů dostalo povzdechnutí u/cafepeaceandlove, že jeho práce se mění každým týdnem. Hned za ním u/SmileLonely5470 vyslovil obavu z éry, kdy si každý „vykadí vlastní software" a problémem se stane vzájemná kompatibilita. Budoucnost, v níž si každý generuje vlastní aplikace, podle něj právě na interoperabilitě vždycky drhla.

Jádro věcné debaty tvoří monorepa. u/ppooooooooopp píše, že to nemělo nikoho překvapit, protože velké organizace s obřími monorepy git nepoužívají, překvapivé je prý jen to, že na limit narazila firma s pouhou tisícovkou zaměstnanců. u/Captain_Forge oponuje, že monorepa takhle velké firmy stejně neobslouží dobře a stavba vlastních nástrojů místo gitu je jen náplast. Starší pamětníci v tom vidí návrat historie: u/swizz nazval Scion „Perforce v2", u/mr_birkenblatt v serverovém a online přístupu cítí SVN a u/tecnofauno připomněl Rational Clearcase, a ne v dobrém.

Objevuje se i podezření a skepse k číslům samotným. u/Which-Hospital1544 čte tempo slučování spíš jako obrovskou neefektivitu nebo nafukování statistik, na které firma pak musela naroubovat nový systém, a u/OkBeautiful4392 se ptá, co tolik změn vůbec ospravedlňuje. u/bugra_sa dodává, že u tisíce lidí sahajících do jednoho monorepa není nejtěžší git, ale kdo změnu vlastní a které testy musí projít. Nejostřeji to formuloval u/cantgetthis, podle něhož Anthropic nestydatě zkopíroval systém Mety včetně konceptů jako odvozená data, zatímco u/sampaoli_negro_rojo lituje, že to firma nesdílí jako open source.

Z vlákna tak zůstává dvojí dojem: inženýrsky dává odchod od gitu u takto vytíženého monorepa smysl, ale tempo, uzavřenost a pocit, že si každá laboratoř staví vlastní svět, část komunity spíš děsí.
