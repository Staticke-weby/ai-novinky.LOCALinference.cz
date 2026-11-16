# 1wxin4m
**GPT-6 Astra prošel startovní zónu World of Warcraft naslepo za 40 minut bez úmrtí**

r/OpenAI · u/ThereWas · 4. října 2026, 17:37 · 1274 bodů / 257 komentářů · [diskuse](https://www.reddit.com/r/OpenAI/comments/1wxin4m/)

Uživatel u/ThereWas sdílel článek serveru Tom's Hardware o kousku modelu GPT-6 Astra ve World of Warcraft. Agent začal jako ork na prvním levelu, prošel celé Údolí zkoušek a doběhl až do vesnice Sen'jin Village. Celý běh zvládl za čtyřicet minut a bez jediné smrti, aniž by kdy viděl jediný vykreslený snímek ze hry.

Místo obrazu se agent orientoval podle surových síťových paketů a dat vytažených přímo ze souborů serveru. Hrál přes open-source klienta agent-wow na privátním serveru AzerothCore s verzí 3.3.5a z jediného promptu v Codexu, přičemž v paměti držel 28 typů serverových zpráv a obraz světa si skládal pythonovým skriptem. Questy doloval z SQL souborů, řetězce plnil ve správném pořadí, prodával haraburdí, oblékal vylepšení a před závěrečnou jeskyní se naučil schopnosti, pro hledání cesty si pak postavil vlastní C++ pomocníka nad navigačními mmap soubory s knihovnou Detour.

Nejvíc hlasů posbírala technická námitka uživatele u/Aceofluckz0r, že čtení paketů znamená tahat klíč z paměti běžícího klienta, což má právě chytat ochrana Warden, takže tahle konkrétní metoda je na ostrých serverech nepoužitelná. Zároveň přiznává, že umělá inteligence obecně výrobu botů zrychlí a zlevní, jenže stejně tak může pomoct s jejich odhalováním a hlídáním. Na to navazuje obava u/A_Novelty-Account, že pro online hry typu MMO to může být smrtelné, protože v budoucnu prý vůbec nepůjde poznat, jestli hru hraje člověk, nebo stroj.

Proti skepsi se ozval u/Gab777795 s tím, že wówkoví boti jsou úzce navržení přesně na tuhle práci, zatímco tenhle agent nebyl na hraní nijak trénovaný a jen se na místě rozhodoval, co je asi nejlepší výsledek, což je prý obrovské. Podobně to vidí u/Aranthos-Faroth, podle kterého vůbec nešlo o obcházení zabezpečení, ale o důkaz, že to model dokázal bez přípravy. Odpůrci ale kontrují stroze: u/wilhelmbw připomíná, že boti tohle umějí odjakživa, a u/flokerz to shrnuje poznámkou, že bot s přístupem k informacím neviditelným pro běžné hráče je sotva tak dobrý jako příležitostný hráč.

Zbytek vlákna se přelévá mezi pobavením a škodolibostí. u/AriyaSavaka by si to chtěl zopakovat s čistým ovládáním počítače a bez oklik přes síťové rozhraní, u/Acrobatic-Layer2993 provokuje, zda takhle wówko nehrajeme vlastně všichni a zda ještě někdo používá rozhraní. u/pleasedontPM se směje, že hraje tak špatně, že ho nikdo za bota nezabanuje, a u/turtle-toaster si mezitím neodpustí, že Tom's Hardware zní jako obchod s kladivy. Temnější strunu brnká u/g_bleezy, který popisuje zlatý věk trápení lidí v online hrách pomocí vlastních cheatovacích aplikací, zatímco u/Murky-Tip-3118 přitahuje paralelu se šachy, kde i nepatrné napovídání přináší obrovskou výhodu a otravuje paranoia, že každý dobrý tah soupeře je podezřelý.

Z pokusu tak zůstává spíš ukázka uvažování obecného agenta než návod na nového bota: zvládnout cizí protokol, data serveru a plánování výpravy bez jediného obrázku.
