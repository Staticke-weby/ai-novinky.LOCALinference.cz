# 1xr6krp
**Next-Concept Modeling slibuje paralelní generování textu. Praxe je zatím opatrná**

r/LocalLLaMA · u/Lorian0x7 · 8. listopadu 2026, 20:19 · 215 bodů / 62 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xr6krp/)

Nový výzkum Next-Concept Modeling rozděluje tvorbu textu na dvě fáze: nejdřív hrubý náčrt významu a pak postupné přidávání jemnějších detailů. Text se nejprve zakóduje do hierarchie diskrétních kódů pomocí víceúrovňového VQ-VAE a transformer pak generuje jednu úroveň po druhé, přičemž všechny kódy uvnitř úrovně předpoví najednou. Místo generování slovo po slově tak model postupuje ve větších paralelních skocích.

Podle abstraktu na arXivu autoři na srovnatelně velkých modelech hlásí lepší perplexitu než nejsilnější difuzní základ na LM1B při 21krát rychlejším běhu, na OpenWebTextu konkurenceschopný výsledek při desetinásobném zrychlení a na XSumu stejnou ROUGE-L při 31krát rychlejším generování. V úloze sudoku pak NCM překonává autoregresivní i difuzní záklasy napříč všemi obtížnostmi a vystačí si s menším počtem vyhodnocení funkce.

Autor příspěvku k tomu přidal odvážnou představu, že podobně úsporná architektura brzy umožní provozovat inteligenci na úrovni Opus 5.5 na 32 GB videopaměti, protože úzkým hrdlem přestane být propustnost paměti a stane se jím výpočet. Právě tahle věta diskusi rozdělila: u/Double_Cause4609 se ptá, odkud se takový závěr bere, když při stejném objemu paměti vypadají klasický model a konceptuální model zhruba rovnocenně. Podobně u/Memestonks2020 připomíná, že Opus 5.5 je model o řádu stovek miliard parametrů, a ten se na běžný domácí hardware prostě nevejde.

Nejvíc se přitom v celém vlákně chytl ironický tón. Komentář u/AdGlittering1378, že tohle „úplně všechno změní“, nasbíral nejvyšší hodnocení a doprovodily ho memové obrázky, zatímco u/legislat nabádá k opatrnosti, dokud se neobjeví skutečně použitelné textové difuzní modely, protože na papíře vypadá dobře všechno. V tomtéž duchu u/Bagelsarenakeddonuts čeká spíš kombinaci difuze a transformerů, která ale za klasickým přístupem masivně zaostává, protože zatím nepřinesla ani jeden užitečný model. Skepsi shrnuje u/log_2 svým vzorcem, že dopad novinky se rovná jedné lomeno počtem videí a článků s titulkem o konci velkých jazykových modelů.

Do debaty vstoupily i první praktické zkušenosti. U/AwelessFire píše, že podle článku zkusil natrénovat miliardový model, ale generování se zadrhává opakováním a špatně vybranými slovy a funguje mu spíš jen na překlad a úzce vymezené úlohy. Naproti tomu u/geteum tvrdí, že v logických hrách a hádankách je přístup jasně lepší než běžné modely, jen je potřeba ho nejdřív natrénovat, což je prý celkem snadné. Odbornější výhrady přidává u/james_pic, podle něhož metoda kromě sudoku není chytřejší než stávající difuzní modely, které samy zaostávají za autoregresivními, a u/Presstabstart upozorňuje, že trénink na stejnou délku kontextu bere dvojnásobek paměti a autoři zveřejnili jen kód pro odvozování.

Celkově tak vlákno čte NCM spíš jako slibný rychlejší difuzní jazykový model než jako okamžitou náhradu transformerů na domácí grafice.
