# 1xauekr
**Pocket TTS se zmenšil na 1,9 milionu parametrů, umí klonovat hlas**

r/LocalLLaMA · u/Affectionate_Hat_585 · 20. října 2026, 16:59 · 360 bodů / 43 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xauekr/)

Laboratoř Kyutai ukázala novou verzi Pocket TTS, drobného modelu pro převod textu na řeč, který se vejde do 1,9 milionu parametrů a zvládne klonování hlasu přímo v zařízení. Odkaz míří na firemní blog a příspěvek je označený jako diskuse bez dalšího komentáře od autora.

Samotný blog se načetl jen částečně, jeho titulek ale říká podstatné: „The tiny TTS was actually 10x too big". Kyutai tím naznačuje, že předchozí drobná verze byla zhruba desetkrát větší, než bylo nutné, a novinka jde cestou radikálního zeštíhlení pro plně lokální běh.

Největší ohlas přesto neměla velikost, ale cenzura. u/JMowery si postěžoval, že model místo „What the fuck" říká „What the dee", jako by se sám cenzuroval, a ptal se, co je to za nesmysl. Vlákno se ho rychle chytlo: u/Federal_Order4324 nechápal, proč něco takového vůbec cenzurovat, u/LuCiAnO241 kvůli tomu model rovnou odepsal a zůstává u Kokoro a u/Caffdy se ptá, proč komunita dosud nenatrénovala necenzurovanou variantu, když jsou modely tak malé. Ozval se ale i opačný hlas, u/Stepfunction píše, že žádné cenzurování nepozoroval a nadávky modelu procházejí bez potíží.

Věcnější linku otevřel u/Ok-Solution-7889 přáním vidět měření přirozenosti, rychlosti a věrnosti hlasu napříč různými mluvčími, protože právě u drobných modelů je zajímavé, zda udrží inference kompletně lokálně. Srovnání s konkurencí vyznívá smíšeně: u/Wooden_Archer5690 má stále raději zvuk Kokoro, ale Kyutai chválí i za jejich model pro převod řeči na řeč, který lze provozovat lokálně. Podobně u/james_pic připadá novinka o něco přirozenější než Piper při podobné velikosti, jenže častěji kazí výslovnost a nabízí méně hlasů.

Praktické zkoušky pak řeší detaily. u/shotan chválí slova, ale píše, že model klopýtá na číslech, datech a neznámých slovech typu „blogpost", což prý větší původní model nedělal. u/Shap6 dodatku, že při minulé zkoušce klon vůbec nedržel původní přízvuk mluvčího. Užitečným příspěvkem jsou odkazy od u/Shot-Height-7194 na Hugging Face a GitHub, odkud si zájemci model stáhnou, zatímco u/Wix86 už vyhlíží převod do gguf.

Takhle malý hlasový model ukazuje, že kvalitní syntéza už nemusí znamenat obří váhy v cloudu, jen si komunita vedle velikosti hlídá i to, aby mluvil přirozeně a bez roubíku.
