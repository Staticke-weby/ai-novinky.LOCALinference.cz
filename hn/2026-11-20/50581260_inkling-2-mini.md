# 50581260
**Thinking Machines vydali Inkling 2 Mini. Model se vejde na notebook**

Hacker News · jasondavies · 20. listopadu 2026, 21:12 · 860 bodů / 155 komentářů · [diskuse](https://news.ycombinator.com/item?id=50581260)

Thinking Machines vydali Inkling 2 Mini, rychlý model s otevřenými vahami, který se vejde na notebook. Jde o looped transformer, který prostřední vrstvy přepočítává třikrát na každý token, aby dosáhl hlubšího uvažování s menším počtem vypsaných tokenů. Mezi open-weights modely do 100 miliard parametrů vede na DeepSWE v1.1 se 48,2 % a na Vals Index v2.2 se 46,5 % a podle firmy zároveň běží rychleji než podobně výkonné modely.

Model je dostupný na Tinkru a Hugging Face jako směs expertů s 26,4 miliardami parametrů celkem a 3,4 miliardami aktivních. Většina vah se trénovala i nasazuje nativně v přesnosti NVFP4, poslední čtyři vrstvy v MXFP8, takže celá stopa má kolem 20 GB. Výzkumníci s ním podle oznámení letěli v letadle, kde offline na MacBooku Pro postavil během pár minut hratelný letecký simulátor, a vedle něj firma vydala i výzkumnou variantu s proměnlivým počtem průchodů pro zkoumání dohledu nad uvažováním ve smyčkách.

Největší nadšení v diskusi budí právě představa silného modelu pro lokální běh. Uživatel montroser cituje vzkaz firmy z Redditu, že velikost vybrali podle přání komunity a že trénink end-to-end v NVFP4 drží podle Unslothe kolem 90 % přesnosti i po kvantizaci, zatímco smyčky přidávají hloubku zvlášť užitečnou pro kódování. Uživatel jakswa to shrnul halasným přivítáním spásy pro ty, kdo čekají na Qwen 4, a uživatel stymaar dodal, že je rád za malou směs expertů v době, kdy Qwen menší řadu po verzi 3.6 opustil.

Technická linka se rychle stočila k praktickému rozchození. Uživatel walrus01 upozornil, že Unsloth už má GGUF kvantizaci, a uživatel jakswa přidal odkaz na pull request do llama.cpp, který přidává právě podporu pro smyčkovou architekturu. Uživatel rsolva slíbil, že model hned vyzkouší na AMD 7900XTX proti Qwen 3.8 27B, protože jako směs expertů by měl nabídnout mnohem vyšší rychlost dekódování při srovnatelném výkonu, a uživatel christkv si pochvaloval, že jeho Framework Desktop vypadá jako stále lepší investice.

Nechybí ani skepse k číslům a zvědavost na výzkum. Uživatel stavros na nadšení, že je model na úrovni Qwen3.8-27B, odpověděl, že to pro něj znamená, že čísla v reálu nejspíš neobstojí, a uživatel LPisGood se prostě zeptal, co to vlastně smyčkový model je. Uživatel mattnewton naopak napsal, že Inkling 2 Small mu přišel lepší, než naznačovaly benchmarky, a nejvíc ho zajímá právě proměnlivě smyčková varianta, protože o žádném jiném funkčním otevřeném modelu toho druhu neví. Uživatel gchadwick to vidí podobně a ptá se, zda jde o první veřejný looped transformer dost dobrý pro reálné nasazení.

Kdo shání malý model na vlastní hardware, má teď vedle řady Qwen další vážnou volbu k vyzkoušení.
