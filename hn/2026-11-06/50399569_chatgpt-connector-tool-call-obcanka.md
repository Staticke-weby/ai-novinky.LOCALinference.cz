# 50399569
**ChatGPT poslal tool call jinam. Bug bounty teď chce občanku**

Hacker News · Aldipower · 6. listopadu 2026, 23:50 · 86 bodů / 35 komentářů · [diskuse](https://news.ycombinator.com/item?id=50399569)

V ChatGPT se měl potvrzený tool call tiše přesměrovat do jiného konektoru, než uživatel čekal a odsouhlasil. Právě tohle bezpečnostní hlášení z komunitního fóra OpenAI přinesl na Hacker News a diskuse se od technického detailu rychle přelila k tomu, za jakých podmínek jde takovou chybu vůbec nahlásit.

Bug bounty programy pod správou Bugcrowdu totiž nově chtějí ověření identity ještě před odesláním reportu, ne až při proplácení odměny. Citovaná nápověda Bugcrowdu to zdůvodňuje snahou zlepšit integritu platformy a omezit záplavu nekvalitních hlášení. Podle diskutujících jde v praxi hlavně o spam generovaný umělou inteligencí – reportující má svým dokladem takříkajíc „ručit“ za to, že neposílá slátaninu.

Výzkumníkům se to nelíbí. Uživatel uptrails vysvětluje, že dřív šlo hlášení podat anonymně a compliance se řešila až ve chvíli, kdy člověk odměnu skutečně chtěl přijmout, a ironizuje, že právě hlášení pro AI firmy teď brzdí obrana proti AI spamu. Uživatel appplication dodává, že část bezpečnostních výzkumníků jsou vyloženě paranoidní samotáři, kteří si anonymitu střeží, takže pro ně má povinná identita odrazující účinek, i když spamové zahlcení chápe. Nejstručněji to shrnuje lrvick: anonymním whitehatům plaťte za jejich čas, jinak se mohou vrátit jako blackhati.

Vedle toho běží čistě technická výtka k samotnému mechanismu souhlasu. Kristjansson píše, že jde o zásadní nepochopení záruk, které mohou OpenAI a MCP nabídnout: když je potvrzení jen další samostatný tool call, pak je to prostě další tool call, žádné skutečné vymezení oprávnění ani propojení s předchozí akcí neexistuje. Jakmile vrátíš řízení modelu, vrátil jsi řízení modelu.

Zbytek vlákna je směs hořkosti a suchého humoru. Aldipower si stěžuje, že psát ručně prózu pro miliardovou firmu zadarmo nedává smysl, když z druhé strany chodí automatické odpovědi a bounty chce předem biometrické údaje. Nekusar kontruje, že poslední dvě zranitelnosti prodal na Toru, protože nechce podepisovat smlouvy ani čekat na mnohaměsíční embargo. A když se do vlákna připlete strojově působící odpověď, glosuje to cluckindan prostě jako hlášení o chybě Claudea a odpověď Claudea.

Poučení pro čtenáře je dvojí: potvrzovacímu dialogu u agentů se nedá slepě věřit a nahlášení chyby dnes může stát víc soukromí než práce na jejím nalezení.
