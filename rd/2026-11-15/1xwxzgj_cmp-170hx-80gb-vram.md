# 1xwxzgj
**Napěťový glitch odemkl na kartě CMP 170HX 80 GB VRAM. Stačilo 15 hodin práce**

r/LocalLLaMA · u/Yarukiless-cat · 15. listopadu 2026, 16:16 · 701 bodů / 188 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xwxzgj/)

Autor na těžební kartě Nvidia CMP 170HX provedl napěťový glitch a odemkl plných 80 GB paměti místo továrně zpřístupněných 8 GB. Informace o postupu se objevila před pěti dny, autor si nejdřív ověřil, že to půjde nástrojem pico, a dnes to dotáhl do konce. Skript pro část s omezeným zápisem mu napsal model Astra a po téměř 15 hodinách práce hlásí hotovo, druhou kartu CMP chce upravit později.

Nejvýše hodnocený komentář patří u/krish_bhanderi, který to shrnul hláškou, že umělá inteligence napsala skript, který odemkl víc paměti pro běh víc umělé inteligence, a kruh se tím uzavřel. Hned pod ním se rozjela debata o plýtvání hardwarem: u/Green-Ad-3964 píše, že když firma osadí kartu 80 GB a zapne z toho jen 8 GB, ukazuje to rozměr toho, jak málo by paměť bez spekulací stála. Podobně to vidí u/rockknocker, kterému přišlo skvělé už to, že starší P102-100 měla dvakrát víc paměti, než inzerovala, ale desetinásobek je podle něj šílený.

Proč se takové karty vůbec prodávaly zaškrcené, vysvětluje v diskusi u/Snarks_Domain. Těžba Etherea tehdy potřebovala DAG soubor o velikosti lehce přes 4 GB, který pomalu rostl, a hranice 8 GB by při zachování proof-of-work přišla v březnu 2027. Omezení tak podle něj byla plánovaná zastaralost, která měla těžaře donutit koupit novější karty. Na to navazuje otázka u/JoNike, jestli nebylo prostě levnější nechat na desce plné osazení a jen ho softwarově zamknout, než vyvíjet úplně jinou variantu.

Třetí linka vlákna řeší, jestli se risk vyplatí. u/txoixoegosi upozorňuje, že CMP 170HX jsou v podstatě A100 s vadnými nebo horšími čipy, takže nelze čekat, že každá karta po plném odemčení podá stoprocentní výkon. u/TheManicProgrammer proto přemítá, jak dlouho vydrží, a u/Nirmal1992 se ptá, jak karta drží dlouhý inference běh a jaké má po delší zátěži teploty. u/caetydid se v té souvislosti ptá, jestli kromě nárůstu ze 64 GB po firmwarové úpravě na 80 GB existuje ještě jiný přínos, který by ospravedlnil riziko.

Závěrečné téma jsou peníze a dostupnost. u/Jumpy-Operation-4615 prorokuje, že cena stopadesátých teď vystřelí vzhůru, a u/Snarks_Domain dodává, že se karty už teď prodávají blízko původní ceny přes 4000 dolarů. u/ds_account_ lituje, že o úpravě nevěděl, když se karta prodávala za 250 dolarů, zatímco u/cibernox si pochvaluje 320 GB při propustnosti 8,2 TB/s za šest tisíc jako dost možná svůj nejlepší nákup a chystá se upravit všechny čtyři své kusy. Podobně váhá u/NeoID, který má doma dvě karty, bojí se, že skončí mezi těmi, které plných 80 GB nedají, a prosí o podrobný návod a skripty.
