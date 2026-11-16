# 1xlra3n
**Stáhl si 120B model na herní PC. Běží 17,8 tokenu za sekundu a sežere skoro všechnu RAM**

r/LocalLLM · u/Full-Independence554 · 2. listopadu 2026, 08:55 · 520 bodů / 177 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xlra3n/)

Hráč ze zvědavosti rozjel 120B model přímo na svém herním počítači a dostal se na 17,83 tokenu za sekundu, což mu přišlo překvapivě použitelné. Model mu přitom obsadil téměř celou systémovou paměť. Běžně používá cloudové modely, ale lokální zálohu si stáhl pro případ, že by vypadl internet nebo spojení s cloudem přerušil třeba větší konflikt, a pro základní věci ve stylu Wikipedie.

Největší ohlas v diskusi sklidila rada, aby to celé zase smazal. u/esw123 mu s nadsázkou vzkázal, ať model smaže a stáhne Qwen 3.8 Flash Next, protože za pár dní ho stejně smaže kvůli Qwen 4 Flash Next. V podobném duchu píšou i další: u/feelspeaceman označil GPT-OSS 120B za prastarý model a slibuje si od Qwen 125B úplně jiný paralelní svět, u/dagerika doporučuje Qwen 3.8-27B a u/ScuffedBalata tvrdí, že rok a půl starý model je proti novinkám úplně mimo.

Do toho se mísí vtipy na adresu Sama Altmana a nedostatku pamětí. u/ImproveYourMeatSack píše, že Altman pláče nad tím, jak autor plýtvá DRAM, místo aby skončila v datacentru, u/tim-7 se pohoršuje, jak si vůbec dovoluje mít 64 GB RAM a nedat je Altmanovi, a přidávají se u/DrBearJ3w s u/plonkman s narážkami na nestoudné využití osobní paměti. Narážka míří na známé stížnosti, že osobní hardware s velkou RAM ubírá čipy datacentrům.

Vážnější linka řeší, jestli se takový obr na domácím stroji vůbec vyplatí. u/Hacker_ZERO upozorňuje, že Qwen 27B má mnohem lepší benchmarky, běží výrazně rychleji a spokojí se s asi 20 GB paměti, u/90hex označuje GPT-OSS-120B za zastaralý a hluboko pod Qwenem 3.8 27B a u/Code_Xero připomíná, že cokoliv odložené do systémové RAM bude velkým úzkým hrdlem pro generování tokenů. Na autorovu představu o lokální Wikipedii pak reaguje u/aersel24 tím, že používat AI jako Wikipedii je špatný nápad, protože si věci vymýšlí, a u/-chaotic_randomness- radí stáhnout si celou Wikipedii offline přes Kiwix, což zvládne i telefon. u/g_rich to rozvádí do detailu a navrhuje lokální kopii Wikipedie případně napojenou na model jako RAG, včetně projektů na internet v krabici pro dlouhé výpadky.

Z vlákna tak nakonec plyne, že lokální obr funguje, ale menší moderní modely udělají stejnou službu rychleji a s menší spotřebou paměti.
