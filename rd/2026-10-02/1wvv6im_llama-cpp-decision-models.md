# 1wvv6im
**Novinka v llama.cpp: Decision Models**

r/LocalLLaMA · u/paf1138 · 2. října 2026, 16:25 · 477 bodů / 122 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wvv6im/)

Uživatel u/paf1138 nasdílel do r/LocalLLaMA odkaz na blog ggml-org na Hugging Face o podpoře takzvaných Decision Models v llama.cpp. Příspěvek nemá žádný vlastní text a je označený jako Resources, ohlas je ale veliký a diskuse se rychle stočila k modelu Jev a jeho klonům.

Z odkazovaného článku se podařilo načíst jen úryvek, který zmiňuje model Clef-GGUF s 27B parametry pro zero-shot klasifikaci. Podrobnější popis novinky tak v balíčku chybí a většina vláken řeší spíš to, k čemu se rozhodovací modely hodí v praxi a proč kolem nich vznikl takový rozruch.

Největší ohlas získala poznámka u/-p-e-w-, že Jev je ukázkou nápadu bez jakékoli ochrany před konkurencí: autoři ho představili jako velkou věc v AI, ostatní s nimi souhlasili — a pak si během necelého měsíce postavili vlastní verzi. Příběh o bleskové komoditizaci pak rozvíjejí další: u/Blobstein_Ijay mluví o sprintu od novinky ke komoditě během tří týdnů a u/DanielSReichenbach připomíná, že původní myšlenka vyšla od někoho jiného a tehdy bez marketingové kampaně nezabrala. Na dotaz u/Deadlibor, co to vlastně Jev je a proč ho už nikdo neřeší, odpovídá u/Foreign_Risk_2031 prostě tím, že ostatní už si postavili vlastní a vezou se na vlně zájmu zdarma.

Druhá linka diskuse hledá pro rozhodovací modely práci. u/Narrow_Whereas_7193 nadhazuje roleplay, kde by model hlídal, aby postavy neujížděly ze scény, a u/jojotdfb to rozvádí nápadem nechat model generovat další repliku a zároveň kontrolovat, jestli táhne příběh správným směrem. u/ChikenDumbstick k tomu přidává vlastní zkušenost s Layou pro větvení promptů podle vstupu od uživatele, ale přiznává, že proti jednorázovým klasifikátorům v tom zatím nevidí nic zásadního, snad kromě složitějších rozhodovacích stromů. Podobně skepticky zní u/Nothing_from_void, podle kterého lidé tohle dělají dávno a marketing z toho jen udělal novinku, a u/arcandor, kterého udivuje, že se zapomnělo na téměř deset let starý Bert.

Nejvěcnější návrhy využití přinesli u/infectiousstupidity a u/Objective-Pair8231: neustále zapnutý směrovač, který podle promptu vybere malý či velký model, kódovací či vizuální model, míru uvažování nebo vyhledávání na webu, případně posoudí, jestli je volání nástroje riskantní. u/Lugnut1206 přidává domácí automatizaci, kde jsou tyto modely výkonnější a spolehlivější, a u/LouizFC láká představa výběru relevantních vzpomínek pro příběhové hraní. Odlehčení obstaral u/seamonn s otázkou, co si dát k obědu, a u/alex20_202020 s nápadem přidat do llama.cpp generátor náhodných čísel, který vrátí jen jedno rozhodnutí bez pravděpodobností a zbaví uživatele starostí s volbou.

Z vlákna tak nakonec plyne docela střízlivý obrázek: samotná podpora v llama.cpp je vítaná, ale největší hodnota rozhodovacích modelů zatím leží v nudných a užitečných věcech, jako je směrování, hlídání nástrojů a automatizace.
