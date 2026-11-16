# 1xfl3al
**Clown Prophecy: jak zastavit degradaci při řetězení MiniMax H3**

r/StableDiffusion · u/roychodraws · 26. října 2026, 03:35 · 338 bodů / 130 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xfl3al/)

Uživatel u/roychodraws vydal sadu Clown Context Suite, která má zastavit postupné měknutí obrazu při řetězení klipů MiniMax H3. Každý nový klip totiž vychází z konce předchozího, kousek detailů se vždy ztratí a kolem desátého klipu je obraz měkký a vybledlý. Autor to přirovnává k lučištníkovi, kterému řeknete, odkud má zhruba mířit, ale nikdy mu nedáte terč.

Proto modelu dává terč i na konci. Clown Context připne poslední snímky předchozího klipu na začátek nového, aby plynule navázal pohyb, zatímco Clown Prophecy předem vyrenderuje konec záběru z čistého promptu a referenčních obrázků. Clown Anchoring pak tenhle čerstvý konec připne dozadu, takže model jen doplňuje střed a má přistát na kvalitních snímcích. Sada je zdarma na GitHubu včetně ukázkového workflow, počítadla záběrů a přepínače pro spouštění proroctví každých N záběrů.

Nadšenci nápad hodně chválí. U/LatentForge-Dev píše, že dát modelu explicitní cíl je chytrý způsob, jak zatočit s hromaděním chyb, protože každý další klip je jinak na konci ničím neomezený. Připnutím začátku a čerstvého konce se podle něj sevře drift z obou stran, což je ideální pro delší vyprávění. Podobným směrem se vydal i u/One-Explanation-4625, který ve svých Hand-Tie-Clips už dřív dělal návaznost přes předvizualizaci a nabízí sdílení zkušeností.

Zároveň se ozývají pochybnosti, jestli předpovězený konec zvládne živější akci. U/Dogluvr2905 se ptá, jak to funguje, když žena na videu jen nesedí, ale třeba tančí, protože odhadnuté koncové snímky nemusí sednout na pohyb, který model nakonec vyrobí. U/MastMaithun to rozvádí k měnícím se úhlům kamery a novým detailům v kontinuálním záběru a navrhuje zátěžový test: šedesát sekund z dvanácti pětisekundových klipů s různou kamerou v každém.

Praktické ohlasy jsou zatím opatrně optimistické. U/GrapplingHobbit po šesti spojených generacích hlásí, že kvalita držela dobře, jen konec jedné generace úplně nelícoval se začátkem další a lehce to cuklo. Alternativu přidal u/infearia: renderovat odzadu, kdy se prvních N snímků desátého klipu použije jako posledních N snímků devátého, a spoje překrýt prolínačkou. Mezi tím se mísí i pobavení klaunem, kdy u/Silly-Dingo-7086 píše, že klauna prostě musí sledovat a hlasovat, a u/boozelessensthepain přiznává, že výkladu fandí, ale cítí se jako opice na přednášce o teorii barev.

Kdo řetězí delší videa, odnese si z vlákna jednoduché ponaučení: hlídat nejen začátek, ale i konec záběru, a u složitých pohybů si správné promptování a frekvenci proroctví otestovat na vlastní scéně.
