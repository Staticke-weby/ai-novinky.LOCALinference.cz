# 1y1diuk
**Thinking Machines vydali Inkling 2 Mini. Model s 26 miliardami parametrů se vejde na notebook**

r/LocalLLaMA · u/Skyline34rGt · 20. listopadu 2026, 21:10 · 1196 bodů / 353 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y1diuk/)

Thinking Machines Lab vydali Inkling 2 Mini, multimodální model s otevřenými váhami, který přijímá text i obrázky a generuje text. Celkem má 26,2 miliardy parametrů, z nichž je aktivních 3,4 miliardy, díky opakovanému průchodu středními vrstvami ale připadá na jeden token efektivně asi 5,4 miliardy aktivních parametrů. Jde o první model firmy mířený přímo na lokální uživatele, velikostí se má vejít i na běžnou herní kartu.

Podle modelové karty je to 24vrstvý decoder-only transformer se sparse směsí expertů, prostředních 12 vrstev se provádí třikrát se sdílenými váhami, takže z 24 vrstev vah vzniká 48 aplikací vrstev na token. Každý token míří na 8 ze 128 expertů, pozornost kombinuje lokální a globální vrstvy a obraz zpracovává vision transformer ve společném prostoru s textem. Model vede open-weight modely pod 100 miliard parametrů na DeepSWE v1.1 se 48,2 % a Vals Index v2.2 se 46,5 %, nativně zvládá 256 tisíc tokenů kontextu a s YaRN až milion, a verze GGUF od Unslothu je už venku.

Do diskuse přišel i u/programmerChilli, který v Thinking Machines pracuje. Napsal, že velikost modelu zvolili podle toho, co si lidé z tohoto subredditu nejčastěji žádají, a vypíchl dva body pro lokální provoz: trénink kompletně v nvfp4, díky kterému model podle měření Unslothu drží 90 % top-1 přesnosti i při 1bitové kvantizaci, a právě loopovanou architekturu, která přidává hloubku bez parametrů navíc a pomáhá hlavně v kódu.

Největší ohlas měla srovnání s konkurencí. u/soteko žasnul, že novinka hraje vyrovnaně s Qwenem 3.8 s 27 miliardami parametrů, u/LMTLS5 to shrnul jako souboj na stejné úrovni a u/Vid4771 glosoval, že Qwen 4 jsou vlastně modely, které jsme potkali cestou. u/fbms2 hlásí, že model na první pokus prošel jeho testem s hrou Bomberman, v čemž je lepší než Qwen 3.6 s 27 miliardami, jiní ho zase popisují jako Qwen 3.8 na steroidech. Kritičtější hlasy ale zmiňují vyšší halucinace a přísnější bezpečnostní pravidla, u/tonibm19 si stěžoval, že mu model odmítl pomoct se zkompilováním forku přehrávače, protože to vyhodnotil jako obcházení ochran.

Zbytek vlákna řeší, jestli se na to dá opravdu hrát doma. u/TapAggressive9530 popsal provoz na RTX 5060 Ti se 16 GB v kvantizaci UD-Q3_K_XL: čistě textově jede kolem 34 tokenů za sekundu, jen se pár expertů odkládá do RAM, zapnutí vision projektoru ho ale srazí asi na 13 tokenů. u/q_tech_x51 vyčíslil 8bitovou verzi na 22,9 GB a u/FoxiPanda nadšeně poznamenal, že málo který malý model nabízí nativně tak dlouhý kontext. Část lidí zároveň hlásí, že GGUF verzi zatím nenačtou v llama.cpp, u/silenceimpaired to předpokládal předem a u/LosEagle lakonicky napsal, že si počká, až se do toho obuje bartowski.

Kdo hledá menší otevřený model na kód a agenty, který se vejde na jeden počítač, má teď vedle Qwenu další vážnou volbu.

---

**Další diskuse:**

- [r/singularity – 324 bodů, 32 komentářů](https://www.reddit.com/r/singularity/comments/1y1fntc/)
- [r/LocalLLaMA – 243 bodů, 45 komentářů](https://www.reddit.com/r/LocalLLaMA/comments/1y1drpd/)

[Zpět na index](00-index.md)
