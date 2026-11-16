# 1xv8t2e
**llama.cpp vydal verzi 1.0. Lokální inference dostala stabilní základ**

r/LocalLLaMA · u/unofficialmerve · 13. listopadu 2026, 15:07 · 1532 bodů / 187 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xv8t2e/)

Projekt llama.cpp se po letech nočních buildů dočkal verze s jedničkou na začátku. Oznámila ji přímo v komunitě Merve z Hugging Face s tím, že tým chce dál pokrývat všechny platformy a typy modelů a zároveň udržet základ lehký a robustní pro navazující aplikace.

Součástí oznámení jsou i desktopové aplikace Llama postavené právě na llama.cpp, které mají snížit vstupní bariéru k lokální AI na pár kliknutí. Autorka nechala odkazy na podrobnosti k verzi i k aplikacím v komentářích pod příspěvkem, včetně blogu a poznámek k vydání.

Komunita bere jedničku hlavně jako důvod k díkům. Nejvýše hodnocený hlas patří u/bharattrader, který píše, že bez projektu by se prakticky nikdy nenaučil to, co dnes umí při pouštění modelů doma na vlastním stroji. Podobně to formuluje u/_tylermatthew: kdyby si nemohl s modely hrát lokálně, umělou inteligenci by prý skoro neřešil, a právě proto je vděčný za nástroj, který mu nechává techniku v rukou ve světě ovládaném obřími silami.

Oslavy ale rychle doplnila i praktická linka o údržbě. Komentář u/New_Comfortable7240 žádá víc maintainerů kvůli hromadě otevřených problémů a návrhů na změny a přidává se k němu i u/TimGoTheCreator. V podobném duchu píše u/johnzadok, že na své grafice od AMD musí stále používat rychlejší forky mimo hlavní větev, a doufá, že po dosažení milníku zbude čas na slučování komunitních nápadů a úpravy kódu.

Nejasnosti budí samotné číslování. Uživatel u/ClaimNo6416 se ptá, jak to, že po roce stahování denních verzí s čísly kolem 12360 najednou přišla verze jedna. Na to navazuje u/OsmanthusBloom otázkou na pravidla pro velké a malé verze: za důvod k nové major verzi se uvádějí jen změny v C API, zatímco běžné uživatele prý víc bolí nekompatibilní změny v parametrech příkazové řádky nebo v REST API.

Zbytek vlákna míchá nostalgii s výhledem. Uživatel u/wywywywy vzpomíná na začátky, kdy projekt běžel jen na procesoru, u/nfox01 označuje llama.cpp za terénní vůz, který drží soukromou AI nad vodou, a ptá se, jak se dá misi pomoci. A u/mecshades nadhazuje, zda by hlavní větev neměla přebrat metody pro streamování u MoE modelů ve stylu Strata či gufo, protože záplava forků připomíná problém se spoustou streamovacích služeb.

Z diskuse tak zůstává dvojí vzkaz: respekt k základu, na kterém stojí lokální hraní s modely, a přání, aby se jednička promítla i do rychlejšího odbavování návrhů a výkonu mimo hlavní proud.
