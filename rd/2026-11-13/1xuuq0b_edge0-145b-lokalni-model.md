# 1xuuq0b
**Edge0-145B: open-source model se 145 miliardami parametrů běží na vlastním počítači**

r/LocalLLaMA · u/BrightCandle · 13. listopadu 2026, 02:25 · 144 bodů / 36 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xuuq0b/)

Firma Edge0 uvolnila jako open source dvojici modelů Edge0-145B a Edge0-120B včetně vlastního inference frameworku a nástrojů pro nasazení. Větší z nich představuje jako první open-source on-device model se 145 miliardami parametrů, který má na vlastním počítači nabídnout programování, uvažování a agentní práci na úrovni špičkových cloudových modelů.

Podle doprovodného oznámení má na kompatibilním notebooku zvládnout špičku 29 GB paměti, předzpracování přes 1100 tokenů za sekundu a generování přes 80 tokenů za sekundu při kontextu 128K–256K. Uvnitř pomáhá architektura sdílející velké matice mezi skupinami 64 expertů, takže se v každém kroku počítá jen zhruba s 10 miliardami parametrů, a zřetězení paměti grafiky, systémové paměti a SSD. V interních testech firma hlásí třeba 64,6 bodu na DeepSWE 1.1 a 86,52 na Terminal-Bench 2.1 a schopnosti předvádí na úlohách od explainer videa přes manhattanskou scénu v Blenderu a program pro skutečný dron až po návrh desky v KiCadu.

Diskuse se ale rychle stočila k podezření, že jde o další variaci Qwen. Nejvíc hlasů sbírá lakonické u/Witty_Mycologist_995 s povzdechem o dalším ladění Qwen a u/longtimenoseebro to rozvádí jako doladění doladění a fork forků. Do stejného rohu míří i u/Middle_Bullfrog_6173, podle kterého je úsměvné mluvit o návrhu pro lokální běh od prvního dne, když tým podle něj vzal natrénovaný cloudový model a jen ho adaptoval, a u/Helpful_Jelly5486 v tom vidí přebalený Qwen Flash Next běžící v řežimu Nvidie FP4.

Druhá linka řeší čísla a paměť. u/0xcontext je zvědavý, jestli v reálném programování skutečně překoná Flash Next, a u/Evening-Blueberry-97 chce přímé srovnání se základním modelem na stejných testech, protože 145 miliard parametrů zní jako pořád hodně RAM bez ohledu na kvantizaci. u/DefNattyBoii vytýká úzký výběr benchmarků, kde jsou ukázané jen ty lepší, a vypisuje dlouhou řadu chybějících testů od SWE-bench přes OSWorld po MathVision. Praktickou brzdu dodává u/LaurentPayot, který stále čeká na pořádné soubory GGUF pro běžné llama.cpp, a u/barbear22, pro kterého je absence vize důvodem to rovnou přeskočit.

Zbytek vlákna doplňují pochybnosti o nováčkovi a drobné rýpnutí do formy. u/Marino4K se ptá, jestli je Edge0 vůbec legitimní skupina, a u/norenEnmotalen přiznává, že mu to celé zní podezřele. u/BawbbySmith se podivuje, proč příspěvek nese logo Perplexity, a u/Buzzard se baví tím, že graf míchá na jedné ose lineární a logaritmické měřítko.

Kdo čekal nadšení z lokálního obra, najde v r/LocalLLaMA hlavně opatrnost: papírově velká čísla ano, důvěru si ale model bude muset vybojovat reálnými testy a otevřeným vydáním.
