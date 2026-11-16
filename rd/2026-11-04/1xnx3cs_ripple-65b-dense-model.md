# 1xnx3cs
**Ripple-65B: hustý model od pěti lidí poráží open-weight modely s 500 miliardami parametrů**

r/LocalLLaMA · u/coder543 · 4. listopadu 2026, 20:16 · 282 bodů / 81 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xnx3cs/)

Společnost Ricursive Intelligence vydala Ripple-65B Preview, hustý transformer s 65 miliardami parametrů natrénovaný na 12 bilionech tokenů s kontextem až milion tokenů. V agentním kódování na TerminalBench 2.1 získal 80,52 bodu a nechal za sebou výrazně větší americké open-weight modely včetně Reflection Beam 501B s 80,1 bodu.

Karta modelu popisuje stroj postavený od nuly na architektuře blízké Gemma 3N, úzký a hluboký s 80 vrstvami, který se obejde bez směsi expertů, vlastních kernelů i kvantizace. Tým se během vývoje rozrostl z jednoho na pět lidí, výpočetní efektivitu na kódu zlepšil šestnáctkrát oproti Olmo 3 a u plného tréninku až pětapadesátkrát a výsledek vychází pod licencí Apache 2.0. Model se vejde i na NVIDIA DGX Spark a v datacentru má na dvou B200 dávat 250 tokenů za sekundu.

Komunitu nejvíc vzala představa, že hustý šedesátipětimiliardový model drží krok s MoE monstry nad 500 miliard parametrů. u/Chromix_ to označil za velkou věc a připomněl, že podobně překvapuje i Qwen s 27 miliardami, jen je potřeba počítat s nároky na paměť: v kvantizaci kolem dvou RTX 3090 a rychlostí zhruba 25 až 35 tokenů za sekundu, zato bez nutnosti obrovské systémové RAM jako u velkých MoE. u/MerePotato v tom vidí ideální třídu pro náročnější domácí nasazení a u/HistoricalStrength21 se těší, že i kdyby to na jeho stroji lezlo pomalu, poběží mu to na vlastním hardwaru.

Technická debata se stočila k pozornosti. u/ttkciar chválí kombinaci velkého počtu hlav, střídání plné a lokální pozornosti s oknem a úprav jako gated attention či ořezávání aktivací a spočítal, že režie pozornosti dělá jen asi 9 GB při 128 tisících tokenech a 66 GB při milionu. Právě v tom vidí spolu s dalšími šanci pro domácí laboratoře limitované pamětí grafických karet a možný začátek trendu, kdy se nepůjde jen cestou MoE optimalizovaných pro souběžné obsluhování zákazníků.

Praktické zkoušky zatím hlásí smíšené tempo. u/james_pic sáhl po průběžných GGUF kvantech od AtomicChat, model mu prošel kouřovým testem s odvyprávěním Zlatovlásky nasucho a s humorem, ale na Strix Halo se trápil kolem pěti tokenů za sekundu a při ladění konverze ho překvapil přemýšlením dlouhým třicet tisíc tokenů, ačkoliv na chybu přišel brzy. Skeptičtější hlasy krotí nadšení z tabulek: u/brainExploded99 se diví srovnání se staršími modely a u/Mediocre_Safety5743 chce před důvěrou v grafy počkat na víc lokálních zkušeností. Odlehčení dodal u/Porespellar připomínkou, že Ripple se jmenovalo i sladké šumivé víno z roku 1959 proslavené sitcomem Sanford and Son.
