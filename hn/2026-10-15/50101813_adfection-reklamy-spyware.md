# 50101813
**AdFection: cílená reklama jako kanál pro zero-click spyware**

Hacker News · jcomp · 15. října 2026, 12:43 · 436 bodů / 590 komentářů · [diskuse](https://news.ycombinator.com/item?id=50101813)

Uživatel jcomp upozornil na výzkum Citizen Lab o izraelské firmě Discover-Tech, která měla přes běžné internetové reklamy doručovat spyware bez jakékoli interakce oběti. K infekci prý stačilo, aby se reklama na stránce nebo v aplikaci jen zobrazila.

Citizen Lab popisuje platformu Controlium, která umí zařízení zbavit anonymity, vytvořit jeho otisk a ve chvíli vykreslení reklamy ho automaticky napadnout, přičemž firma takto propojovala svět reklamy s dodavateli žoldáckého spywaru včetně Candiru. V letech 2024 a 2025 mělo být tímto způsobem zacíleno nejméně 45 zařízení v redakci televize Al Jazeera. Výzkumníci případ označují za první technicky potvrzený útok tohoto typu doručený cílenou reklamou, který nazvali AdFection.

Diskuse se rychle stočila k tomu, jak něco takového vůbec funguje. Uživatel chunkyslink shrnul zprávy Citizen Lab a Confiantu do srozumitelného postupu: firma nakupovala reklamu jako běžný inzerent a roky figurovala na seznamech prověřených prodejců, do nevinně vypadajících bannerů ukryla drobný skript a ten při načtení poslal domů údaje o zařízení, adresy i cookies. Většina lidí pak nedostala nic zpět, jen vybraný cíl obdržel — a to pouze jednou — kód předávající zařízení dál, chráněný šifrováním, rotujícím hostingem a kontrolami proti botům. Uživatel oulipo to doplnil představou cílení na jednoho člověka podle věku, bydliště a pár dalších znaků a následného zneužití chyby třeba v dekodéru obrázků k spuštění libovolného kódu.

Druhá velká linka řešila, jestli proti tomu chrání blokování reklam. Začalo to lakonickým zvoláním po uBlock Origin, k němuž další přidali wBlock pro Safari a DNS blokování pro mobilní aplikace. Uživatel preg_match připomněl, že blokátory doporučuje i FBI, a vysvětlil, že moderní reklama není statický obrázek, ale malá aplikace s kódem, takže spolehlivě pomůže jen zablokovat kód úplně. Uživatel Lio k tomu přidal, že nedůvěra k reklamnímu průmyslu je obecnější, když se v něm točí miliardy za podvody a data z aukcí slouží ke sledování pohybu lidí.

Zazněla i skepse k širším obranám. Jeden hlas tvrdil, že omezování soukromí na Androidu ani šifrované messengery typu Signal nepomohou, když útočník ovládne celé zařízení, další mu oponovali, že takový útok je drahý a většiny lidí se netýká a že šlo o zneužití zranitelností, ne o sociální inženýrství, proti němuž míří omezení instalací mimo obchod. Uživatel red_admiral zdůraznil, že nešlo jen o aplikace, ale o reklamy na téměř dvou stech tisících webech a aplikací, takže stačila návštěva běžného zpravodajského webu v prohlížeči. Odlehčení přinesla poznámka, že lidstvo reklamy nesnášelo odjakživa, s odkazem na román Kontakt od Carla Sagana, kde zbohatlík vydělal na televizním blokátoru reklam.

Z vlákna tak zůstává hlavně ponaučení, že reklama v prohlížeči je dnes spouštění cizího kódu, a podle diskutujících je rozumné k ní tak i přistupovat.
