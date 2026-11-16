# 50024913
**Microsoft představil Decision-1, model pro rychlé rozhodování**

Hacker News · lisajaloza · 9. října 2026, 20:38 · 174 bodů / 56 komentářů · [diskuse](https://news.ycombinator.com/item?id=50024913)

Microsoft představil Microsoft-Decision-1, model určený pro rychlé rozhodování místo generování textu. Má dodávat strukturované výstupy, se kterými může software rovnou pracovat, a hodí se pro směrování požadavků, klasifikaci, prioritizaci, ověřování a řízení workflow.

Odkazovaný článek tvrdí, že model dosáhl nejvyšší přesnosti ve srovnání 36 benchmarků s téměř 150 tisíci otázkami, které byly při tréninku skryté. V měření rychlosti měl být 2,5krát rychlejší než druhý H2O-Lightning-4B v1.1 a 35krát rychlejší než GPT-6 Sol, k vyzkoušení je v Microsoft Foundry a přes OpenRouter.

Nejživější linka diskuse řeší, na čem model stojí. Uživatel nejch upozorňuje, že jde o doladění menšího modelu Qwen, stejně jako Cloudflare Clef, Strands decider a řada dalších novinek z posledních týdnů. Uživatel simonw cituje přiznání Microsoftu, že jde o post-trénink Qwen3.5-9B s plánovaným přechodem na modely Microsoft AI a OpenAI, a glosuje to slovy, že strach z čínských modelů zjevně polevuje. Uživatel dr_kiszonka odpovídá, že moc na výběr není, a uživatel mjb dodává, že Strands decider už existuje i ve variantách na základu Gemma 4. Do toho zapadá postřeh uživatele manmal, že nekomprimovaný Qwen v BF16 poráží i dvakrát větší kvantovaný model, takže právě kvantizace zřejmě kazí přesnost rozhodování.

Druhé velké téma je lokální běh. Uživatel chris_money202 má pocit, že Microsoft sází na lokální inference a nativní AI rozhraní ve Windows, která poběží lokálně nebo volitelně v cloudu. Uživatel ampersandwhich doufá, že se tak jeho Copilot+ PC konečně naučí něco užitečného, Phi Silica pro Advanced Paste byl podle něj dobrý, i když opožděný začátek. Skeptičtější uživatel a_vanderbilt to čte jako snahu ospravedlnit investice do Copilotu a NPU, které Microsoft tlačil výrobcům, zatímco uživatel sebazzz připomíná, že lokální rozhraní už existují v podobě Microsoft Foundry Local s podporou GPU, NPU i CPU.

Třetí spor se vede o cenu a srovnání s Jev. Uživatel HarHarVeryFunny vyčítá Microsoftu, že cenu srovnává jen s GPT Sol, a ne s levnějšími GPT Terra, GPT Luna ani samotným Jev, který má stát čtyři desetiny ceny Luny. Uživatel sidd0103 oponuje, že Decision-1 stojí 0,042 dolaru za milion vstupních tokenů, tedy stejně jako Jev, a dodává, že část výkonu pomohlo rychle dotáhnout duševní vlastnictví startupu Pi Labs. Nechybí ani vtipy: uživatel hollow-moe se diví, že Microsoft pojmenoval produkt jasně a stručně, a uživatel buredoranna v tom vidí návrat Clippyho.
