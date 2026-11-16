# 1xp7e5x
**Nejlepší Moss workflow? Komunita se pře o pár drobných kroků**

r/StableDiffusion · u/Ill_Resolve8424 · 6. listopadu 2026, 09:06 · 551 bodů / 158 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xp7e5x/)

Uživatel nasdílel screenshot workflow pro realističtější výstup základního modelu Moss a označil ho za nejlepší, na jaké narazil. Podle něj ukazuje skutečný potenciál modelu, a tak ho předává dál ostatním. Původní příspěvek nejdřív nemohl najít, ale později ho do textu doplnil i s odkazem na zdroj.

Nejhlasitější část diskuse workflow odbyla jako naprostou samozřejmost. u/Jealous_Piece_1703 ho nazval v podstatě nejzákladnějším workflow v historii, u/AidenAizawa se ptá, co mu uniká, a přidávají se hlasy, že jde o výchozí nebo standardní postup. Někteří to rovnou označují za trollení či návnadu a ptají se, čím by mělo být tak výjimečné.

Proti tomu se postavil u/ArkCoon s podrobným vysvětlením, že zdánlivé drobnosti mají dohromady obrovský vliv na výsledek. Workflow podle něj stojí na base modelu, který je pro realismus mnohem lepší než verze SFT, používá sampler er_sde s pokročilým nastavením eta, s_noise a max_stages, kde je s_noise nastaveno na 1,1, a pracuje s vrstvami Skip Layer Guidance 22 a 24 v rozsahu 0,0 až 1,0 místo výchozích 22 s rozsahem do 0,5. Právě tahle kombinace podle něj výstup úplně proměňuje, on sám prý už chtěl Moss vzdát a od nálezu workflow ho zase baví.

Do vlákna pak vstoupil i samotný původní autor u/Outrageous_Still9335, který potvrdil, že je workflow jeho, a pochopení pro záměnu s výchozím postupem má. Rozdíl je podle něj právě ve Skip Layer Guidance a v injekci šumu v pokročilých volbách sampleru ER_SDE, což base modelu pomáhá s realističností a držením promptu i s typickou rozmazaností a měkkostí. Podobně to popisuje u/LumaBrik: s_noise přidává při každém kroku šum navíc, s vyšší hodnotou přibývá detailů a base modelu to svědčí, zatímco u SFT modelu to prý není potřeba.

Zbytek diskuse se vede mezi nadšením a praktickými dotazy. u/Bulky_Chemistry_196 workflow označuje za kouzelné pro práci s base a nedá na něj dopustit ani v kombinaci s Kromoss, u/Bbmin7b5 píše, že proměnilo Moss ze špatného ve výborný. Opakují se prosby o nasdílení postupu, na které jiní odpovídají, že je vše na obrázku a dá se postavit za dvě minuty bez zvláštních uzlů, a padají i další tipy od uzlu TE-speed-moss pro zrychlení generování přes úplné vypuštění vynechávání vrstev až po poznámku u/gutster_95, že většině lidí spíš hapruje promptování než workflow.

Kdo si chce s Mossem hrát dál, ve stejný den komunitou koloval i seznam 52 filmových a kamerových promptů pro MOSS Image, který se hodí právě k ladění realistického vzhledu.
