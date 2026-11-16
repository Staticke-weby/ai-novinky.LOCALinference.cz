# 50317331
**Koppar postavil LTE modem do USB-C. Počítač dostane telefonní linku**

Hacker News · abijahkaj · 31. října 2026, 16:56 · 55 bodů / 37 komentářů · [diskuse](https://news.ycombinator.com/item?id=50317331)

Počítač dostane vlastní telefonní linku přes jediný USB-C kabel: čtyřvrstvá deska Koppar LTE modem přináší LTE data, SMS i hlasové hovory na fyzické nano-SIM. Staví na modulu Quectel EC25-EUX a zvukové kartě s RP2040, která převádí 1,8V PCM audio modemu na USB mikrofon a reproduktor. Po zapojení počítač vidí síťovou kartu, sériové porty pro AT příkazy a USB zvukovku a hovor může předat headsetu, skriptu nebo AI agentovi, displej, reproduktor ani baterii deska nemá.

Repozitář popisuje napájení 5 V z USB-C s 3,8V buckem dimenzovaným na 2A vysílací špičky a trojici LED NET, RING a CALL. Návrh vznikl z jednostránkové textové specifikace, kterou nástroj Koppar přetavil ve schéma a desku, a autor ho pak ručně zkontroloval proti datovým listům. Ke stažení je KiCad 10 projekt, Gerbery, podklady pro JLCPCB i firmware zvukové karty pod permisivní CERN Open Hardware Licence, revize B hlásí nula chyb a míří do výroby.

Jádro debaty obstarala nedůvěra k hardwaru navrženému umělou inteligencí. Uživatel Vaushite napsal, že je projekt očividně „vibed" a po postavení by nefungoval. Autor abijahkaj odpověděl, že je ke slepému výstupu stejně skeptický, a proto každý spoj auditoval: RF cesta vyšla na zhruba 35 Ω místo 50 Ω a skákala mezi vrstvami, buck skončil daleko od své cívky s úzkou napájecí cestou a objednávkový seznam by málem koupil 18µH tlumivku do 4,7µH pozice. Vše je i s čísly v REVIEW.md a první várka pěti holých desek a dvou osazených kusů se právě objednává, modul EC25-EUX si kvůli skladu připájí ručně.

Nejvěcnější spor se vedl o hlas po vypnutí 2G a 3G. Uživatel gruez upozornil, že bez VoLTE se z desky stane za pár let cihla. Autor vysvětlil, že EC25-EUX umí VoLTE nativně v basebandu a z pohledu desky je zvuková cesta stejná, modem interně řeší registraci i kodek a ven pouští standardní PCM. Háček je v praxi: jde o whitelist operátora a správný MBN profil přes AT+QMBNCFG, takže test registrace i pádu do starších sítí bude součástí oživení. Na to navázala otázka, zda bude LTE vůbec fungovat po příchodu 6G, a uživatel wolrah připomněl OFDM a dynamické přidělování subkanálů, díky kterému 4G nemusí ustupovat 5G tak tvrdě jako starší generace.

Zbytek vlákna snil o tom, kam by se linka vešla. Uživatel mcculley by ji nejradši viděl v 16palcovém MacBooku Pro, uživatel wlesieutre se divil, že Apple s vlastním modemem a bez poplatků Qualcommu mobilní Mac neudělal, a uživatel DaiPlusPlus oponoval, že Apple o to nestojí kvůli provázání s iPhonem a FaceTime. Padl i tip koupit notebook s vyměnitelnou Wi-Fi kartou za celulární modul a přání mít desku jako modul pro Framework. Uživatel j45 dodal, že podobné SIM krabičky dávají smysl jako domácí telefon tam, kde nejsou pevné linky.

Čtenář si odnese, že telefonní linka pro počítač je hlavně o softwaru a certifikaci u operátora, samotná deska je jen čistý USB převodník mezi SIM, LTE a headsetem.
