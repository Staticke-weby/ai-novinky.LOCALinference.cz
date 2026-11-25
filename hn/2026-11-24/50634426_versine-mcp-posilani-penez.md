# 50634426
**Versine chce naučit AI agenty posílat peníze přes MCP**

Hacker News · harshithl1777 · 24. listopadu 2026, 21:44 · 82 bodů / 65 komentářů · [diskuse](https://news.ycombinator.com/item?id=50634426)

Trojice zakladatelů Harshith, Param a Vishnu představila v Launch HN startup Versine z akcelerátoru YC F26, který má fungovat jako Venmo ovládané přes MCP. Agent za uživatele rozúčtuje večeři, skupinový výlet nebo pokerové dluhy a rovnou peníze pošle či vyžádá – klidně až od stovky lidí najednou, včetně příjemců bez účtu, kteří si je pak vyberou do banky do dvou minut.

V pozadí stojí self-custodial peněženka s USDC na síti Base, pro uživatele ale skrytá za vklady přes Apple Pay, Google Pay či kartu a výběry v dolarech na bankovní účet. Každá platba standardně vyžaduje schválení passkey v mobilní aplikaci, jen předem nastaveným důvěryhodným kontaktům smí agent posílat samostatně a v limitech. Když příjemce mimo Versine nepotvrdí OTP, peníze podle zakladatelů nikdy neopustí peněženku odesílatele – jen se odloží stranou, odkaz po sedmi dnech vyprší a odesílatel může převod mezitím kdykoli zrušit.

První reakce zněla, že tohle Cash App a Venmo rychle okopírují, a přidali se i další s tipy na Stripe, Revolut či Wise. Zakladatel harshithl1777 odpovídá, že samotné posílání peněz není obrana, jen klín k agent-first bance stavěné od základů pro agenty. Jako příklad uvádí, že agent by bance mohl rovnou říct, aby předem odmítla stržení za prodlužující se trial – rozhodnutí, která dnes lidem banky vůbec nevystavují.

Nejvěcnější spor otevřel uživatel atakanelik se zkušeností s podvody a chargebacky: když agent zaplatí špatnému člověku, jak vypadá storno? Odpověď je strohá – platby jdou přímo z vlastní peněženky, jsou finální a skutečně je vrátit nelze. Právě proto je defaultem passkey a autonomie jen pro lidi, kterým uživatel věří, že mu omyl pošlou zpět. Uživatel whatever1 namítá, že i drátové převody a debetní transakce jsou v praxi skoro nevratné, zatímco skeeter2020 to shrnuje jako volné sólo s jednosměrným kryptem pro podivně malý průnik power-userů.

Řešila se i ztráta klíčů a byznys model. Na dotaz uživatele alasdair_ zakladatel přiznává, že u self-custodial peněženky může uživatel o vše přijít, v praxi to ale tlumí synchronizace passkeys přes iCloud Keychain či Google Password Manager a možnost exportu záložního klíče. Na dotazy na výdělek opakuje, že peer-to-peer platby samy nevydělávají, cestou je plná banka s úroky z vkladů a kreditkami, později s fiatem u partnerské banky. Právě stablecoiny přitom zvolili i z nouze – po pivotu měli na stavbu asi čtyři týdny a klasický fiat by znamenal příliš pomalá regulatorní kolečka.

Čtenář si z toho odnese jednoduché dilema: posílání peněz povídáním je lákavě snadné, ale bez vratek a s vlastními klíči se hodí hlavně mezi lidi, kterým věříte i bez agenta.
