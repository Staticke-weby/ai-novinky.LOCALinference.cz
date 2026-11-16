# 50069337
**Show HN: Použijte předplatné OpenAI k výrobě audioknih**

Hacker News · janpmz · 13. října 2026, 12:08 · 161 bodů / 82 komentářů · [diskuse](https://news.ycombinator.com/item?id=50069337)

Autor janpmz v rubrice Show HN představil službu PDF TO MP3, která slibuje proměnit dokument v audioknihu pomocí umělé inteligence, za kterou už uživatel platí. V Codexu nebo Claudovi si stačí přidat její MCP server, přiložit PDF do chatu a poslat pokyn k převodu na audioknihu.

Odkazovaný web to celé dělí na dvě platby: zpracování dokumentu má pokrýt předplatné přes MCP, zatímco samotné namluvení se hradí zvlášť přes vlastní klíč pro OpenAI nebo Google. Návod popisuje tři kroky, připojení AI přes adresu streamovatelného serveru a ověření účtu, přidání klíče čistě na řeč a odeslání prvního dokumentu, a celou nabídku rámuje lákadlem na převod za nula dolarů.

Právě tohle dělení vyvolalo největší hádku o zavádějící titulek. Uživatel embedding-shape čekal přihlášení přes OpenAI a jízdu čistě na předplatné, a když stránka chtěla API klíč, označil to za klamání, které ani neprošlo testováním. Přidali se wastewastewaste a scrollop s tím, že poctivý název by musel znít „použijte předplatné a klíč pro syntézu řeči“, a kaoD rýpnul do výrazného nápisu o nulové ceně. Sám janpmz v diskusi vysvětloval, že dokument skutečně zpracuje předplatné a klíč platí jen hlasový výstup, kde si lze vybrat mezi Gemini a OpenAI.

Druhá silná linka řešila bezpečnost vkládání klíčů na cizí web. Uživatel s přezdívkou x______________ to přirovnal k odevzdání čísla kreditní karty, draugadrotten odkázal na plně offline generátory audioknih, které běží lokálně. Yohannparis radí pro takové případy vygenerovat samostatný klíč s rozpočtovým limitem a hlídáním útraty, walrus01 připomněl starý žertovný web na „zkontrolování“ soukromého SSH klíče a Onavo poznamenal, že služba nabízí i přihlášení přes OAuth. Uživatel simianwords by to celé nejraději viděl jako běžný plugin nebo přihlášení přes ChatGPT.

Nejživější je ale kutilská větev o domácích podcastech z článků. Xenocratus popsal vlastní postup, kdy z webové stránky očistí jen článek, převede ho syntézou řeči a přes cloudové úložiště s RSS ho poslouchá jako podcast v Apple Podcasts, což nadchlo hned několik dalších. Brumar tvrdí, že tři čtvrtiny jeho poslechu už tvoří obsah generovaný Claudem a hlasy od Mistralu, kolinko chválí výběr hlasů v ElevenLabs a radí nechat si článek před namluvením lehce přepsat pro příjemnější poslechový rytmus. BeetleB si vystačí s převodem na Google Cloud, který je fakticky zdarma, AbsurdCensor každé ráno skládá z odběrů FreshRSS desetiminutový přehled zpráv přes F5-TTS a ph4rsikal doporučuje pro dlouhé lokální čtení Qwen3-TTS.

Do toho si posluchači stěžovali, že ukázkové video končí těsně před ukázkou výsledku. Janpmz je odkázal na stránku s příklady, dodal, že přes MCP je na výběr ze všech hlasů OpenAI a Gemini podle použitého klíče, a přiznal, že syntéza řeči je teď největší úzké hrdlo, které zkouší zlevnit rychlou lokální variantou Kokoro.
