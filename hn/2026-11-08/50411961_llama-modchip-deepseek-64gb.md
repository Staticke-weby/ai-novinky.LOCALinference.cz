# 50411961
**284B DeepSeek běží na 64 GB RAM bez GPU. Projekt sází na dvoubitovou kvantizaci**

Hacker News · joshcsimmons · 8. listopadu 2026, 11:22 · 402 bodů / 180 komentářů · [diskuse](https://news.ycombinator.com/item?id=50411961)

Open-source projekt Llama-modchip slibuje dostat model DeepSeek-V4-Flash ze 76,87 GiB na 56,56 GiB a rozjet ho na Linuxu se 64 GB RAM bez grafické karty. Právě vejít se do běžné desktopové paměti bez pádu na nedostatku paměti je celé kouzlo projektu.

Hned první otázka v diskusi zněla, při jaké kvantizaci se to má povést. Podle komentujících jde zhruba o dvoubitovou kvantizaci, a právě to vyvolalo největší skepsi. Uživatel efficax to shrnuje slovy, že při dvou bitech to pro skutečnou práci asi nebude nic moc, madduci dodává, že všechno pod čtyři až pět bitů je opravdu špatné, a Tepix si utahuje z titulků o běhu na vypínači, za kterými je podle něj vždy kvantizace pod čtyři bity na váhu a vesměs nepoužitelný výsledek.

Do toho přichází pochybnost o samotných číslech. Uživatel adrian17 upozorňuje, že soubory DeepSeek-V4-Flash od Unslothu jsou mnohem větší, jejich nejmenší kvantizace má 82,5 GB a IQ2_XXS dokonce 91 GB, takže není jasné, ke kterému modelu a jakému měření se údaj v projektu vztahuje. Zmínky o kompresi a prořezávání směs expertů podle něj zavánějí ještě citelnějším ořezáním schopností modelu, podobně to vidí i walrus01, který mluví o lobotomizovaném modelu a připomíná, že i 97GB verze se výrazně rozchází s plnou přesností.

Zvláštní kapitolu tvoří dokumentace projektu. Uživatel intoXbox ji označuje za nepříjemný balast, který sice obaluje llama.cpp, ale neříká, na jaké platformě má vlastně fungovat. Ostatní se přidávají: superkickstart by uvítal úklid emoji, epihelix lituje, že lidé už nepíší poznámky sami, a micromacrofoot to glosuje radou, ať si to čtenář nechá shrnout modelem.

Praktickou zkušenost přináší antirez, podle kterého lze na stroji se 128 GB sjednocené paměti model provozovat použitelně rychle jako kódovacího agenta. Reakce jsou ale rozpačité. Uživatel embedding-shape namítá, že video ukazuje asi čtyři sekundy na zpracování 43 vstupních tokenů, což je na agenta procházejícího celé soubory daleko od pohodlí, kgeist popisuje 116 sekund na překlad jedné věty jako v praxi nepoužitelné a Aurornis přiznává, že podobné sestavy miluje na noční úlohy na pozadí, ale na práci u stolu to pohodlné není. Optimističtější tón drží liuliu s odkazem na stabilních zhruba 30 tokenů za sekundu při dekódování a liuliu s prefillem kolem 400 tokenů za sekundu na paměti o stejné velikosti.

Teoretickou tečku přidává spor o to, kde je hranice únosnosti. Uživatel armcat cituje studii, podle níž je poměr velikosti a výkonu nejlepší kolem čtyř bitů a níž už jde výkon prudce dolů, Youden ale namítá, že práce neřeší trénink s vědomím kvantizace, který extrémní osekání mění. Uživatel pu_pe pak říká z vlastní zkušenosti, že by klidně vyměnil část přesnosti za to, že věc vůbec poběží, když se čtyřbitová verze do jeho sestavy nevejde.

Kdo má doma velkou sjednocenou paměť, může si hrát, kdo čeká plnohodnotného asistenta na běžném počítači, ten si podle diskuse ještě počká.
