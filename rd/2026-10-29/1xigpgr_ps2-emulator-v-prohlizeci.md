# 1xigpgr
**PS2 emulátor běží v záložce prohlížeče. Většinu kódu napsal Claude**

r/ClaudeAI · u/yousriii · 29. října 2026, 11:52 · 1193 bodů / 81 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xigpgr/)

Dvojice kamarádů představila TabStationToo, emulátor PlayStationu 2, který běží přímo v záložce prohlížeče. Stojí na jádru PCSX2 pod licencí GPL-3.0, které přenesli do webu a obalili vlastním rozhraním: stačí otevřít stránku, vybrat BIOS a složku s vlastními obrazy disků a hrát. Kód PlayStationu se za běhu překládá do WebAssembly a grafiku vykresluje WebGPU, přičemž disky i BIOS zůstávají v počítači uživatele a nic se nenahrává. Většinu programování odvedl Claude Opus 5.5, lidé určovali cíle, testovali hry a hlásili chyby, a na jejich strojích takhle chodí GTA San Andreas, Final Fantasy XII, Resident Evil 4 nebo Guitar Hero, jen nejtěžší scény stále nejsou v plné rychlosti.

Vlákno projekt okamžitě přijalo za vlastní a nejvíc hlasů dalo vtipu u/BoxLegitimate9271, že emulátor v záložce prohlížeče je skvělý nápad a jeho ventilátor v notebooku už prý začal vydávat zvuk startu PS2. Hned pod ním se ale ozývají lidé, kteří to rovnou zkusili: u/nenecaliente69 žasne, že mu bez jakéhokoliv mapování fungoval ovladač z PS5 a v King of Fighters 2002 zatím nepozoruje žádný vstupní lag, u/pechSog hlásí, že právě hraje Ring of Red. Nadšení doplňují chvály na drobné animace rozhraní, které by podle u/fireflamesniper slušely i některým zavedeným frontendům.

Vedle nadšení se řeší hlavně dvě praktické věci, výkon a smysl prohlížeče. u/floriandotorg se ptá, jak si vede proti nativnímu PCSX2, a odpověď z vlákna zní, že nativu se kvůli limitům webu zatím nerovná, i když na slušném hardwaru jede řada her v plné nebo téměř plné rychlosti. Dokládá to i u/Damn-Sky, kterému přijde projekt působivý, ale Tekken Tag Tournament se mu vleče. u/ChocolateGoggles se ptá, proč to vůbec cpát do prohlížeče, a diskuse mu vrací jednoduchou výhodu, že není potřeba nic instalovat a funguje to napříč systémy.

Poslední linka vlákna je herní a záchranářská. u/WaffleKnght nutně potřebuje vědět, jestli poběží Need for Speed Underground 1 a 2, u/Wild_Inspector_8579 zase prosí o Most Wanted z roku 2005 a Carbon, aby mohl oba tituly znovu porazit. Mezi ovládáním se řeší klávesnice i gamepady, u/Chrisgpresents se ptá, jestli vystačí s klávesami, a u/pechSog zjišťuje, zda se ukládá tlačítkem State. Přesahy hezky shrnul u/tanepiper, který sám pracuje na uchovávání jednotlivých her a tohle mu přijde jako uchovávání celého systému na další úrovni.

Z diskuse tak zůstává obraz hračky, která překvapivě funguje a nejvíc baví právě tím, že stačí záložka v Chromu a vlastní dump BIOSu a her.
