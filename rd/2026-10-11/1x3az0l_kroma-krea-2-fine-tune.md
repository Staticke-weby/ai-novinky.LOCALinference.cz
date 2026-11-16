# 1x3az0l
**Kroma: komunitní fine-tune modelu Krea-2 pro generování obrázků**

r/StableDiffusion · u/KadahCoba · 11. října 2026, 17:25 · 557 bodů / 160 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1x3az0l/)

Příspěvek vyšel v zastoupení uživatele u/LodestoneRock, jemuž příspěvky mazalo automatické filtrování. Společně představují Kromu, komunitní fine-tune modelu Krea-2, přičemž tým Krea jim tentokrát poskytl skutečný základní model. Trénink vyšel asi na 10 tisíc hodin na kartách RTX Pro 6000, tedy přes tři měsíce na sestavě se čtyřmi GPU včetně nepovedených pokusů, a za dvě darované karty autoři děkují organizaci ComfyOrg.

Model je ke stažení na Hugging Face, kvantizovanou verzi doplnil v komentářích sám u/LodestoneRock s odkazem na sestavení od uživatele Clybius. Základ Krea podle autorů není zhroucený, takže mohli přímo navrch trénovat metodou OPD a generování má fungovat dobře hned po vybalení. Dál chtějí hlavně vylepšit dataset, v němž vidí asi 90 % kvality, a později se pustit do videogenerátorů typu h3, na jejichž ladění ale zatím nemají hardware a shánějí příspěvky na další karty.

Nejčastější výtka v diskusi zní jasně: chybí srovnání s výchozí Krea-2. Uživatelé u/Royal_Carpenter_1338 a u/toidicodedao se ptají, proč si vybrat právě Kromu a co umí navíc, u/PuppetHere a u/PwanaZana by chtěli vidět výsledky ze stejného seedu a promptu před a po. Právě tahle praktická ukázka podle nich v galerii příkladů chybí nejvíc.

Chvály je přitom hodně. U/East_Shoe8814 ji po vlastním testování označuje za jednoznačně nejlepší fine-tune Krea-2, u/b0tm0de píše, že jich vyzkoušel kolem stovky a nová Kroma se proměnila v něco úplně jiného, v jakousi „Krea-2 Premium Plus". Vedle toho se řeší i slabiny: u/BoldCock si stěžuje na gumově plastovou pleť a ptá se, jak ji opravit, u/NanoSputnik zase tvrdí, že model nezná běžné booru značky jako „eyepatch bikini", a ptá se, jak byl dataset popisován.

Poslední linka je technická a prosebná zároveň. U/Stecnet se těší na menší verzi, která se vejde do 16 GB videopaměti, další se hlásí o GGUF nebo sestavení kolem 10–12 GB a u/TrashWarfare zjišťuje, jestli s Kromou odpadá potřeba obcházet filtry jako u Krea 2 Turbo. U/GeodesicHyena se zase ptá, jak autoři získávají kvalitní popisky v přirozeném jazyce pro Danbooru, když jsou cloudové modely cenzurované a lokální si vymýšlejí.

Kdo má chuť experimentovat s otevřeným generováním obrázků, má v Kromě další důvod stáhnout pár gigabajtů a porovnat stejný prompt na vlastní oči.
