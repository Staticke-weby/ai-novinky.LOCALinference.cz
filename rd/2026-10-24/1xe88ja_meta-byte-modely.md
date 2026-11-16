# 1xe88ja
**Meta trénuje malé modely na syrových bajtech. Místo tokenů čtou písmena**

r/LocalLLaMA · u/DotaMate · 24. října 2026, 15:08 · 434 bodů / 134 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xe88ja/)

Uživatel DotaMate přinesl do r/LocalLLaMA odkaz na preprint, který zkouší přeskočit tokenizér a nechat model číst surové bajty, tedy prakticky písmenko po písmenku. Sám k tomu připsal shrnutí postupu i zádrhelů a na konci se ptá, jestli někdo ví o práci, která by bajtové modely zrychlila na úroveň tokenových.

Podle jeho popisu autoři trénovali modely kolem jedné miliardy parametrů, část z nich destilací z větší Llamy 3 8B, a museli přitom vyřešit překlad mezi tokenovým myšlením učitele a bajtovým čtením žáka. S malým tréninkem vedou tokenové modely s přehledem, s delším tréninkem se ale jejich křivka zplošťuje, zatímco bajtové se zlepšují dál. Slíbené vítězství nad Llama 3.2 1B a Gemma 3 1B o pár bodů je přitom jen protažení trendu do budoucna, v reálných bězích byl tokenový model stále vpředu, a úspora asi šestinásobku textu je vykoupena zhruba pětinásobkem výpočetních kroků.

Nejhlasitější reakce je otrávená z recyklace. u/Eyelbee píše, že jde o pět let starou vědu a bajtová tokenizace je nadbytečná, u/Necessary-Meeting-28 hlásí, že si pro svůj charlm volá rok 2016, a u/Altruistic-String891 připomíná dva roky staré Byte Latent Transformery od stejné Mety, které moc stop nezanechaly a podle jedné citované poznámky prý podle vlastních autorů neškálují. V podobném duchu u/OscarCookeAbbott tvrdí, že čisté bajty jen přesunou váhy k učení základních jazykových rysů a co se ušetří na slovníku, ztratí se na hustotě inteligence.

Druhá linka debaty počítá cenu za hláskování. u/Chromix_ upozorňuje, že inference podraží, protože model bude slabikovat slovo po znacích, a spekuluje, že by to mohla zachránit predikce více znaků najednou, i když ověření návrhu není zadarmo. u/IntelArtiGen staví proti sobě šestkrát méně textu na jedné straně a zhruba šestkrát víc kroků na druhé a vítězně to nevypadá, u/nullc pak logiku dotahuje do krajnosti, že když už menší predikční prostor, tak číst rovnou po jednotlivých bitech.

Mezi tím probleskují praktické postřehy a úlety. u/bigattichouse vypráví, jak cvičí model na Morseovku se slovníkem smrsknutým na pár prvků, což by z Qwenu sundalo gigabajty tokenového balastu, jen na to nemá háčka. u/trumuted rýpe, že čtení po písmenku platí jen pro ascii, u neanglických textů se písmenek za krok vejde míň, a u/Another__one naopak sní o modelu, který rovnou chrlí strojový kód. Odlehčení dodal u/ThiccStorms otázkou, co je to v článku za grafiku, a u/koolkool69 prostým dotazem, co je to bajt, za který si vysloužil spršku mínusů.

Pro malé modely do telefonů a notebooků by se každý bod kvality navíc hodil, jen tahle cesta zatím vypadá spíš na draze zaplacenou úsporu dat než na konec tokenů.
