# 50468888
**smolmaxxing: největší model na nejmenším hardware**

Hacker News · mrashad74 · 12. listopadu 2026, 16:23 · 325 bodů / 117 komentářů · [diskuse](https://news.ycombinator.com/item?id=50468888)

Projekt smolmaxxing hledá největší jazykový model, který ještě reálně běží na nejmenším hardware, co lidem leží doma ladem – TV boxu, starém tabletu, jednodeskovém počítači nebo routeru. Pomáhají mu k tomu vlastní kernely, pečlivá práce s pamětí a streamování vah z flash úložiště, přičemž každé uvedené číslo bylo změřené přímo na daném zařízení. Zatím dokumentuje dva stroje: Xiaomi TV Box S třetí generace s necelými dvěma gigabajty RAM a iPad Air z roku 2013 s jedním gigabajtem, na obou přitom rozběhal i šestnáctimiliardový mixture-of-experts model Ling-mini-2.0.

Repozitář na GitHubu popisuje postup jako patch nad llama.cpp. Pro slabé čipy chystá na míru stavěné 1-bitové a 2-bitové kernely, ořezává zřídka používané řádky slovníku a v případě televize vypíná i launcher a služby Googlu, aby ušetřil paměť. Klíčový trik je stránkování expertů: model si jich pro každý token žádá jen pár, takže ty oblíbené zůstávají v RAM a zbytek se za běhu dotahuje z flashe, podobně se streamují i husté modely větší než paměť.

Nejživější část diskuse se točila kolem toho, jaké ještě šílenější zařízení by měl autor zkusit. Uživatel post-it navrhl vapku s displejem, fredley kapesní konzoli Playdate a Copenjin zase Raspberry Pi Zero jako vstupenku k levnému vestavěnému LLM modulu pro kutilské projekty. Nejpropracovanější nápad přinesl boricj s PlayStationem 2 s rozšířenou pamětí, kde by se váhy tahaly přes sběrnice a výpočet by hnaly vektorové jednotky, autorovi se líbil i odkaz uživatele jedbrooke na miniaturní pohádkový model rozběhaný na Nintendu Wii.

Druhá linka řešila, k čemu jsou takové ořezané modely vůbec dobré. Uživatelé yjftsjthsd-h a sebazzz pochybovali, zda umí něco jiného než zkomolit recept na palačinky, na což gonzalohm oponoval, že právě komunitní výzkum úspornosti je důležitý, protože velké firmy mají zájem na hladových modelech. Autor mrashad74 připustil, že bez pořádného doladění na úzká data jde zatím hlavně o zábavu a novinku, ale z vlastní zkušenosti věří v jedno- až dvoumiliardové modely vyladěné na zákaznická data a ve fígle, které se pak přenesou na běžné notebooky.

Třetí spor se vedl o to, kdo vlastně práci odvedl. Farmadupe2 tvrdil, že napsat inference engine pro staré železo dnes zvládne agent na jeden příkaz, stačí mu sehnat hardware a přístup přes SSH. Autor souhlasil, že Claude a další modely používá hodně, ale upozornil, že za výsledky je přes 150 experimentů a hledání v obrovském prostoru kernelů a úprav modelů, přičemž cílem nejsou triviální půlmiliardové hračky, ale použitelných 16 miliard parametrů a víc.

Z projektu tak zůstává jednoduchý vzkaz: i krabička za pár stovek umí s chytrým hospodařením s pamětí promluvit, otázkou už není jestli, ale jak velkým hlasem.
