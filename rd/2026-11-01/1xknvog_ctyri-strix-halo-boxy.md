# 1xknvog
**Čtyři Strix Halo boxy: domácí AI cluster s 512 GB RAM**

r/LocalLLM · u/420Microbiologist · 1. listopadu 2026, 00:01 · 198 bodů / 100 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xknvog/)

Uživatel koupil čtyři Strix Halo stroje, každý se 128 GB RAM, a chce z nich postavit domácí AI cluster s celkem 512 GB sdílené paměti. Jako hlavní modely plánuje provozovat GLM-5.3 a DeepSeek 4.1 Flash, případně Qwen, až vyjde čtyřková verze, zatímco spárované dvojice boxů mají obsluhovat lehčí GLM-5.3 Flash, MiniMax nebo MiMo. Sestava má pohánět finanční a životní dashboard a k tomu zvládnout i část profesionální práce.

Nejvěcnější odpověď v celém vlákně patří uživateli u/feelspeaceman, který sám na Strix Halo denně běhá a radí nováčkovi dvě věci. Zaprvé se vyhnout oficiálnímu llama.cpp a sáhnout po upravených enginech jako gufo, halogen nebo strixite, protože zatímco oficiální build dává u Q38FN kolem 20 tokenů za sekundu při dekódování a 300 při prefillu, upravené enginy zvládnou 50 až 70 tokenů při dekódování a 1600 až 2400 při prefillu. Zadruhé odkazuje na návod ke clusterování přes RDMA a dodává, že pokud Q38FN stačí na jeden stroj, nemá smysl ho vůbec rozdělovat, případně pomůže Strix Halo Homelab Discord, kde už viděl clustery z deseti a více boxů.

Zbytek diskuse se točí kolem toho, jestli ta ambiciózní sestava nebude zklamáním. u/BackgroundNo2157 píše, že si autor koleduje o velké rozčarování, u/Krothic přiznává, že ho u více boxů ubíjely právě pomalé prefill rychlosti a jediný snesitelný recept byl halogen s Qwen3.8 Flash Next, a u/dgibbons0 si stěžuje, že jeho box jiné značky je při inferenci hlučný a pomalý tak, že se v místnosti nedá být. Jejich obavy doplňují technické otázky, jak boxy propojit, protože jak píše u/Suspicious_Mix529, právě propojení mezi krabičkami začne být rozhodující, jakmile se velký model rozseká na části. Řeší se Oculink karty pro RDMA, obyčejný ethernet s llama.cpp RPC i propojení přes Thunderbolt.

Do toho se míchá počítání peněz a nadšení. Na dotaz u/jacek2023, kolik stála ta výhodná koupě, se v komentářích opakuje částka kolem tří tisíc za kus, což jeden z diskutujících označuje za krádež a další tipuje aktuální slevu na Bosgame M5 s Ryzen AI Max+ 395. u/fortminorlp to glosuje hláškou o tom, jak říct, že člověk je bohatý, aniž by to řekl, zatímco u/arr_jay se autora zastává, že se dvěma boxy pro paralelní kódovací agenty a upraveným enginem gufo už zrušil předplatná velkých služeb. Jak to shrnul u/Layney_Butcher, čtyři boxy a těžké modely na noční směnu, zatímco lehké flash modely obslouží den, zní jako plán, který si zaslouží respekt.

Kdo o podobném clusteru uvažuje, odnese si z vlákna hlavně tohle: samotné krabičky nestačí, rozhodne vyladěný engine a rychlé propojení.
