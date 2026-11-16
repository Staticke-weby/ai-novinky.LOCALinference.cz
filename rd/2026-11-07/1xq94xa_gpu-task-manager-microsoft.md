# 1xq94xa
**GPU Task Manager od Microsoftu ukáže, co skutečně vytěžuje grafiku**

r/StableDiffusion · u/BrooklynBrawl · 7. listopadu 2026, 16:33 · 394 bodů / 76 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xq94xa/)

Viceprezident Microsoftu Scott Hanselman si ve volném čase naprogramoval vlastní správce úloh pro grafickou kartu. Nástroj s názvem gputaskman má na první pohled ukázat, které procesy právě ukrajují výkon z GPU, což se hodí hlavně lidem, kteří generují obrázky a přetahují se o každý gigabajt paměti. Zdrojový kód dal k dispozici na GitHubu a podle prvních ohlasů funguje opravdu dobře.

Nejvíc hlasů posbíral údiv, že za takovou drobností stojí zrovna viceprezident, jak poznamenal u/JamesLahey08. Hned za ním se ozval u/JustSomeIdleGuy s otázkou, která napadla víc lidí: není to prostě jen nvidia-smi? Naráží tím na klasickou konzolovou utilitu od Nvidie, která využití grafiky i seznam procesů ukazuje už roky, a dává tak najevo, že novinka ho nijak neohromila. Podobně u/ZerOne82 tvrdí, že totéž by zvládl v méně než deseti řádcích pythonovského kódu, a u/octopus_limbs se rovnou ptá, proč je tohle vůbec zpráva.

Nejtvrdší kritika přišla od lidí, kteří nástroj hned vyzkoušeli na Linuxu. U/lmpdev popisuje rozhraní jako nepromyšlené a přeplněné textem, ve kterém se těžko vyzná. Procesy mu každou sekundu přeskakují z místa na místo a klávesa „s“ na změnu řazení prý vůbec nefunguje, takže se program dal používat jen s pozastavenými aktualizacemi. I když nápadu věří, nedbalé zpracování ho podle jeho slov zatím moc nenadchlo.

Kolem zpracování se pak rozjela širší hádka o vibe coding. Zatímco u/roculus se takto vzniklých nástrojů zastává a vzkazuje kritikům, ať slezou z vysokého koně, protože vibe coding se každým dnem lepší, u/SHEEP_PIZZA si neodpustil, že nic jiného od „inženýra Microsoftu“ ani nečekal. Do toho u/Wilbis vytáhl konkurenční TMOG od bývalého microsoftího inženýra, který umí totéž a víc, jen prý není vibe-coded. Veselejší notu přidali u/Apprehensive_Sky, který slaví podporu AMD a Linuxu hned od prvního dne, a u/load-blower-134, který přesně ví, co jeho grafiku vytěžuje.

Pro někoho, kdo generuje obrázky a pořád řeší, co mu sežralo paměť, může být jednoduchý přehled procesů na GPU užitečný, i když ostřílení uživatelé zatím zůstávají u osvědčených nástrojů.
