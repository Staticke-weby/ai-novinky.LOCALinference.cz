# 50008427
**Whistle: převod řeči na text v 16,9 MB**

Hacker News · gmays · 8. října 2026, 18:59 · 677 bodů / 143 komentářů · [diskuse](https://news.ycombinator.com/item?id=50008427)

Společnost Cactus Compute představila Whistle, model pro rozpoznávání řeči mířený na mobily, wearables, roboty, chytrou domácnost, automotive a mikrokontrolery. Vejde se do jediného souboru o velikosti 16,9 MB a na procesoru běží bez závislostí.

Podle firemního blogu zvládne na jeden průchod až 30 sekund angličtiny, němčiny, francouzštiny, španělštiny, italštiny, nizozemštiny a polštiny, přičemž jazyk pozná sám, pokud ho uživatel nezadá. Kromě přepisu vrací časové značky jednotlivých slov i embedding řeči po rámcích dlouhých 80 ms, a zvuk přitom nikdy neopouští zařízení. Uvnitř běží ve stejném C++ enginu jako Needle, dekóduje s pěti paprsky a zadaná klíčová slova zvýhodňuje přes Aho-Corasickův automat. V papírových číslech poráží na řadě sad Whisper base i Moonshine tiny v2 a první token vydává za jednotky milisekund.

Diskuse se nejprve proměnila v testovací laboratoř přímo v prohlížeči. andy_ppp píše, že se model snažil záměrně zlomit a angličtina ho přesto „pochopila dokonale", kamranjon mluví o složitých větách a časování, které model přepsal bez zaváhání, a jayshah5696 hlásí, že si poradil i s jeho indickým přízvukem a chystá se ho pustit na linuxovém stroji. Do nadšení ale vstoupil tecleandor se zkušeností, že španělština vyrábí neexistující slova a překlepy, na což kaoD oponuje, že s kastilskou španělštinou neměl problém.

Nejsilnější linka patří INTPenis, který popisuje čtyřiaosmdesátiletého chorvatského otce po mrtvici: pořídil mu přepis hlasu ve Windows, takže stránku autobiografie zvládne za deset minut místo dnů u klávesnice, jenže na stránce končí i každý nechtěný zvuk z úst. ComputerGuru mu odpovídá, že na tohle je potřeba diktační model, který polyká brepty a opravuje přeřeky, a zmiňuje nové Gemini 3.5 Transcribe přes API, zatímco yu3zhou4 připomíná tři trvalé potíže přepisu poruch řeči: málo dat, nepravidelnost projevu a velké rozdíly mezi pacienty. Vedle toho se rozjela debata o smyslu malosti: bob1029 a yymir vysvětlují, že model vměstnatelný do L3 cache škrtá celá latencí pásma, islewis dodává, že právě tohle otevírá soukromý přepis na zařízení bez cloudu.

Závěr vlákna patří limitům a humoru. mo2art narazil na chybovou hlášku o překročení délky zvuku a jjice se ho ptá, zda nenahrával přes limit, albert_e postrádá průběžný přepis už během mluvení a iforgotmypasswo kvůli tomu zatím zůstává u Deepgramu. joewhale přiznává, že titul nejprve četl jako „pískání na text", což by prý bylo mnohem zábavnější, mejutoco na to odkazuje na hvizdný jazyk Silbo Gomero a charv přidává marvelovského Yondua. Praktický tip přihodil rpdillon s klávesnicí FUTO, která přepisuje celá na zařízení.

Z vlákna tak vychází Whistle jako překvapivě přesný drobek pro soukromý přepis tam, kde nesmí data do cloudu ani čekat na server.
