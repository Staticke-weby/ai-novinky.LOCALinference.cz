# 1y1fion
**Claude Code napsal 14 KB velký webový server, který je sám operačním systémem**

r/ClaudeAI · u/JaguarMoe · 20. listopadu 2026, 22:34 · 327 bodů / 50 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1y1fion/)

Vývojář nechal Claude Code napsat statický webový server, který je zároveň vlastním operačním systémem: 14 KB x86-64 assembleru s boot sektorem, síťovým ovladačem, TCP, TLS 1.3 a HTTP. Z adresáře souborů sestaví bootovatelný image a na dvoujádrovém cloudovém stroji zvládne dvakrát až třikrát více nových TLS spojení a malých stránek za sekundu než nginx. Kód psal podle autora Claude Code převážně s modelem Fable 5.2, člověk určoval zadání a co vynechat.

Největší ohlas sklidilo právě to, že model donutil psát méně, ne více. u/RichardEpsilonHughes píše, že přimět Claude řešit problémy menším množstvím kódu namísto většího si zaslouží respekt, a technicky zaměření čtenáři souhlasí, že sizecoding je pro modely nezvykle těžký, protože bývají upovídané a ztrácejí přehled o celku. Druhý nejhlasovanější příspěvek je přitom jen hláška u/Abject-Kitchen3198, že je to „4“, a u/pkkid se ptá, jestli tenhle strohý příspěvek také psal Claude – věta „co ho hlídalo, byly testy“ prý zní ze všeho nejvíc jako Claude.

Odměna 200 dolarů v bitcoinech za prolomení TLS klíče serveru běžícího na 15kb.org do 18. února 2027 se v diskusi čte jako nejlepší možný důkaz odvahy. u/kilaire si utahuje z kolísání kurzu, že je to odměna 200 dolarů… 5 dolarů… 3000 dolarů… 10 dolarů, u/PiDigitsOfPi chválí povedené doménové jméno a u/Real_Style443 píše, že dát na klíč skutečné peníze je mnohem lepší test než jen říkat „věřte mi, je to bezpečné“. Na chvíli zavládla panika, když u/Fine_League311 citoval z repozitáře řádky o generování 24slovné peněženky v RAM, automatické shrnutí ale uklidňuje, že šlo jen o komentář a skutečný klíč je v bezpečí.

Zbytek vlákna řeší, jestli přísné testování stačí i na zbytek takto malého stacku. Autor každou změnu bootoval v QEMU a TLS kód kontroloval pomocí Wycheproof, tlsfuzzer a Valgrind, což u/Independent-Sir3234 chválí jako zdroj skutečné důvěryhodnosti pro takto drobnou implementaci, a ptá se, která část nejvíc bojovala s limitem velikosti, protože zpracování handshake a chybové cesty prý při fuzzingu rychle bobtnají. u/ianreboot namítá, že Wycheproof s tlsfuzzer pokrývají kryptografii a handshake, ale příspěvek nejmenuje orákulum pro zbytek serveru, tedy parser HTTP požadavků a přijímací smyčku TCP, kde se špatné délky projeví zásekem nebo pádem. Vedle toho se objevuje úžas z blízkosti k hardwaru: u/dunder_name píše, že celé se to vejde do L1 cache procesoru a blíž už by to bylo jen ve firmwaru samotném, u/MeButItsRandom v tom vidí předzvěst dalších podobných unikernelů.

Čtenář si z toho odnese, že malý a rychlý kód umí napsat i model, když ho někdo drží přísnými testy a jasným zadáním – a odvahu pak dosvědčí vypsanou odměnou.

---

[Zpět na index](00-index.md)
