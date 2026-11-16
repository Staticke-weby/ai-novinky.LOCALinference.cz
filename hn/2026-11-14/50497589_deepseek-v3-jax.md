# 50497589
**DeepSeek V3 ve 200 řádcích čistého JAX**

Hacker News · VaibhaavTiwari · 14. listopadu 2026, 16:04 · 219 bodů / 20 komentářů · [diskuse](https://news.ycombinator.com/item?id=50497589)

Vývojář Vaibhaav Tiwari přepsal architekturu DeepSeek V3 do 190 řádků čistého JAX bez Flaxu, Equinoxu i PyTorche. Parametry drží jako obyčejné slovníky polí, kde každá část modelu je čitelná funkce. Zmenšenou verzi s 36,2 milionu parametrů pak předtrénoval od nuly na MacBooku Air s 24 GB paměti na veřejně dostupné detektivní próze.

Odkazovaný repozitář s podrobným výkladem rozebírá tři hlavní nápady z technické zprávy: Multi-head Latent Attention, která v této konfiguraci zmenšuje cache ze 480 na 144 čísel na token a vrstvu, směs expertů s jedním sdíleným a šestnácti směrovanými experty a predikci více tokenů najednou. Trénink na 207 knihách o 21,7 milionu tokenů zabral 12 tisíc kroků, asi 2,6 hodiny, validační ztráta spadla z 5,02 na 3,51 a vyvažování expertů pomocí posunu se ukázalo stejně dobré jako bez něj.

V diskusi projekt sklidil hlavně vděk za srozumitelnost. Uživatel wg0 píše, že jde o skvělou učební pomůcku pro mnoho dalších, armcat dodává, že není nic lepšího než postavit model od prvních principů a že ho to láká vrátit se k JAX. Nico chválí vizualizace architektury a navrhuje příště použít standardní dataset pro snazší srovnání s jinými běhy, na což autor odpovídá, že detektivky vybral tentokrát jen pro zábavu.

Nejvěcnější linka patří portu na AMD. Uživatel joebarbere popisuje, že právě tento projekt se mu jako první podařilo celé natrénovat na Fedoře s kartou RX 7600 XT a JAX přes ROCm, a sdílí dvě potřebné proměnné prostředí a nastavení pro grafický stack včetně kontejneru. Autor jeho úpravy rovnou zapracoval, zatímco kouteiheika si posteskl, že podpora AMD mimo datacentra je po letech pořád slabá a firma tím ztrácí prodeje.

Začátečnickou otázku, jak se k takovému stavění modelů propracovat, proměnila debata v malý rozcestník. Uživatel rhdunn doporučuje videa 3Blue1Brown a Welch Labs a sérii Andreje Karpathyho od nuly až po transformery, JBits přidává stránky o JAX, projekt nanochat a původní článek Attention Is All You Need a sám autor posílá tazatele na Stanford CS336. Vedle toho se řešila i budoucnost: na dotaz, zda by šla stejně postavit V4.1, autor vysvětluje, že ta mění pozornost na hybrid dvou komprimovaných typů, a na přání C++ verze odkazuje na llama.cpp.

Z projektu si čtenář odnese hlavně to, že i špičková architektura se dá přečíst za odpoledne, když se ořeže na dřeň a natrénuje na detektivkách.
