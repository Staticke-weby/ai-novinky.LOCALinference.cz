# 49964303
**Pixel 11 zatím nesplňuje bezpečnostní standardy GrapheneOS a může být vynechán**

Hacker News · finnlab · 5. října 2026, 15:02 · 402 bodů / 267 komentářů · [diskuse](https://news.ycombinator.com/item?id=49964303)

Tým GrapheneOS po týdnu práce dokončil jen částečný port na řadu Pixel 11 a dál se neposunul kvůli chybějící podpoře ARM hardware memory tagging v softwaru, firmwaru a možná i hardwaru. Podle projektu za tím stojí snaha Googlu ušetřit, a celá generace tak může z podpory vypadnout.

Odkazované oznámení vysvětluje, že GrapheneOS používá značkování paměti v celém základu systému včetně jádra a všech běžných procesů jako ochranu před vzdálenými i místními útoky, zatímco Pixel 8 ho měl od října 2023 a stock Android ho nikdy standardně nezapnul. Text zároveň chválí Memory Integrity Enforcement na iPhonu 17 a vylepšení Pixelu 11 jako postkvantové ověřené spouštění nebo Titan M3, ale ztrátu značkování označuje za zásadní a kupujícím doporučuje spíš Pixel 8, 9 a 10.

Úvod diskuse se stočil k tomu, zda vůbec jde o novinku. Uživatel Retr0id se ptá, jestli je oznámení nové, a arusahni s Medeou odpovídají, že text vyšel 29. srpna a naposledy byl upraven 30. srpna, přičemž 1. září už projekt hlásil možnou cestu vpřed. Uživatel rickdeckard proto mluví o špatném poměru signálu a šumu a o emotivní debatě o srpnové zprávě, na což přímo účet grapheneos reaguje, že informace jsou přesné, nic nevzal zpět a Pixel 11 podporu značkování stále nemá ani v operačním systému, ani ve firmwaru.

Samotné chybějící značkování část čtenářů nepřekvapuje. Uživatel podocarp píše, že když se funkce v Androidu stejně nepoužívala, Google asi čekal, že si toho nikdo nevšimne, a pro většinu lidí si toho opravdu nikdo nevšimne. Proti tomu uživatel microtonal namítá, že obor jde opačným směrem, Apple nasadil vlastní rozšíření v jádru i systémových procesech a Samsung se značením experimentuje v betaverzích OneUI 9, zatímco uživatel croes spekuluje, že Google osekl hardwarovou akceleraci v cache procesoru, takže funkce je pomalá a ve firmwaru vypnutá. Účet grapheneos to doplňuje, že ani nová beta firmwaru z Androidu 17 QPR2 Beta 4 nestačí, protože značkování se nedá zapnout ze systému, ale jen příkazem z režimu fastboot, a dá se tak i vypnout.

Zbytek vlákna řeší, zda má smysl Pixel 11 vůbec kupovat. Uživatel aftbit označuje telefon za první Pixel po takzvané RAMpocalypse, plný kompromisů kvůli ceně, a kdyby se mu rozbil Pixel 8, sáhl by raději po použitém Pixelu 10, k čemuž se přidávají další majitelé osmiček, devítek a desítek s tím, že chytré telefony jsou už dávno vyřešený problém. Ozývá se i obhajoba výměnných bonusů a úspornějšího čipu s modemem a vtipná linka uživatele mrbn100ful o Motorole s pětiprocentním podílem, přes kterou prý půjdou fronty na kontrolách rychleji, zatímco jiní řeší, že právě chystaná Motorola má být prvním telefonem této značky s GrapheneOS.

Pro čtenáře z toho plyne jednoduché ponaučení: kdo chce GrapheneOS, ať zatím zůstane u starších Pixelů a počká, zda Google značkování do firmwaru doplní.
