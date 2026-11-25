# 50627340
**LLM agenti pracují pro své firmy, ne pro vás**

Hacker News · surprisetalk · 24. listopadu 2026, 13:40 · 958 bodů / 394 komentářů · [diskuse](https://news.ycombinator.com/item?id=50627340)

Programátor si v Claude Code postavil šikovnost, která z instagramových reelů pozná píseň a najde k ní stránku na Bandcampu, aby si ji mohl rovnou koupit a stáhnout do počítače. Když Bandcamp nasadil na vyhledávací API novou ochranu, agent mu odmítl pomoci ji obejít, paradoxně mu ale bez řečí stáhne stejnou skladbu z YouTube, ze kterého autor nedostane ani dolar.

Autor blogu z toho vyvozuje širší pointu: špičkový model ve skutečnosti nepracuje pro uživatele, ale jen v mezích, které mu dovolí Anthropic či OpenAI. Bojí se, že doporučení brzy nebudou nejlepší odpovědi podle recenzí na Redditu či Wirecutteru, ale vážené odpovědi podle toho, kdo si zaplatí product placement, a že stejný mechanismus půjde použít i na přání vlády včetně ochrany autorských práv. Proto prý chce lokální model do domácího homelabu, který by hájil jeho zájmy, a začíná zkoumat, co vlastně znamená pojem otevřený model.

Nejživější ohlas sklidilo vyprávění uživatele TeMPOraL o starším modelu Fable. Když ho žádal, aby při stahování ignoroval robots.txt, protože ten je prý určený pro pavouky, a ne pro agenta jednajícího na přímý pokyn uživatele, model mu prý rovnou do očí řekl, že není jeho agentem, ale vyvažuje zájmy uživatele a zájmy Anthropicu. Právě v tom mnozí vidí jádro problému: omezení nejsou v modelu, ale v postroji kolem něj, jak píše robinduckett, a prý stačí přepsat systémové pokyny, použít API nebo se odvolat na právo na interoperabilitu jako občan EU.

Druhá velká linka debaty řeší, zda je únikem lokální běh. Uživatel largbae popisuje vlastní open-source agenta Hermes, který si sám píše skilly a historii si drží u sebe, takže poskytovatele modelu může libovolně měnit, demo4567 k tomu dodává recept na malou krabičku s Linuxem a OpenRouterem pro celou rodinu a rDr4g0n líčí, jak si s LangGraph a Qwenem napsal úsporného agenta, kde je většina práce obyčejný kód a model jen rozhoduje. Proti tomu stojí skepse: jatora tvrdí, že uzavřené modely ty otevřené stále drtivě porážejí, girvo naopak chválí Inkling 2 Mini či Ripple a dodává, že ochrany čínských modelů jdou dnes snadno odstranit, a xtracto připomíná osmdesátky, kdy se open source také nedal srovnávat s komercí, a dnes ji skoro nahradil.

Třetí spor je o to, zda měl Claude pravdu. Uživatel thor-rodrigues ho hájí: model nemůže ověřit, že ochranu chcete obejít z lásky k umělci, a ne k jejímu zneužití, stejně jako nepozná, zda záplatujete vlastní software, nebo cizí. Odpověď na sebe nenechala čekat: w4der varuje, že se definice dobra a zla v megakorporaci může zítra změnit a zruinovat vám byznys, cicko připomíná, že výrobce kladiva také neurčuje, co s ním smíte zatlouct, a tintor vidí jediné řešení v otevřených vahách. Mezitím si trio8453 z celého textu utahuje, že jde jen o nafouklou historku na téma Claude jednou neposlechl, takže je teď v módě být paranoidní.

Z diskuse tak zůstává jednoduché ponaučení: kdo platí servery, píše pravidla příběhu, a kdo chce agenta opravdu pro sebe, bude si ho muset hostovat sám.
