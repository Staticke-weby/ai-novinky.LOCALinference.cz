# 50399695
**OpenAI otevřel telefonní hovory přes SIP pro všechny organizace**

Hacker News · arbayi · 7. listopadu 2026, 00:03 · 73 bodů / 60 komentářů · [diskuse](https://news.ycombinator.com/item?id=50399695)

OpenAI zpřístupnil v rozhraní GPT-Live telefonování přes SIP trunk pro všechny organizace. Příchozí i odchozí hovory se tak dají napojit přímo na hlasového agenta, kdy poskytovatel typu Twilio obstará telefonní číslo a přenos zvuku a vlastní backend řeší nastavení session a obchodní logiku. Odchozí volání přitom funguje přes Live API, nikoli přes starší endpoint pro vytváření hovorů v Realtime API.

Dokumentace popisuje příchozí hovor jako webhook live.transport.incoming, který backend ověří, deduplikuje a pak přijme nebo odmítne. Přijetí se dělá požadavkem na session s modelem gpt-live-1, hlasem a režimem delegování, odmítnutí pak SIP stavem třeba 486 pro obsazeno. Signalizace běží přes TLS a zvuk musí jít přes SRTP, po přijetí se backend připojí vedlejším WebSocketem pro přepisy, nástroje a příkazy. Pro evropské uložení dat slouží adresa sip-eu.api.openai.com, vyzvánění je omezené na 3 minuty a spojený hovor na 2 hodiny.

Diskuse se okamžitě stočila ke spamu a podvodům. Uživatel joecool1029 se ptá, kdo další netrpělivě čeká na záplavu podvodných volání z ChatGPT, runnr_az dodává, co by se tak mohlo pokazit. Uživatel edoceo popisuje, že na dobře zveřejněném čísle dostává desítky spamových volání denně a filtry nezabírají, jordemort hlásí sedm a více robotických volání za poslední dva dny. Uživatel viraptor radí volat zástupcům a tlačit na postihy volajících a operátorů, transitorykris to shrnuje tak, že telefon už je jen na podvody a Den matek.

Druhá linka je sarkasmus o regulaci. Uživatel bcrl píše o snižování bariér k podvodům páchaným umělou inteligencí, jeden SIP trunk po druhém, a pochybuje o odpovědnosti OpenAI. Uživatel seanp2k2 předpovídá, že firma se sebereguluje tak, že zabanuje poctivé firmy a podvodníkům s tisíci účtů projde všechno, Arubis v tom vidí cestu k regulacím umělé inteligence. Uživatel koskon glosuje, že funkci sponzorovala indická podvodná call centra, sscaryterry dodává, že si o žaloby a regulaci firma vyloženě říká.

Našly se i věcnější a vtipnější hlasy. Uživatel ranger_danger se ptá, čím se to liší od Twilio Voice API, které existuje od roku 2008, uživatel dqv to naopak vítá a těší se, že vlastní SIP server bude moci ChatGPT přizvat do konferencí nebo nechat zvedat příchozí hovory. Uživatel kyleee doufá, že přes SIP půjdou posílat i faxy, na což iAMkenough odpovídá historkou o faxovém spamu s falešnými fakturami a úvahou, jestli už někdo zkusil prompt injection faxem. Uživatel RicoElectrico radí předstírat nedoslýchavost a chtít po agentovi, aby po každém slově s písmenem a říkal Albuquerque v Novém Mexiku, uživatel opengrass to uzavírá, že už se člověk nedovolá člověku a všichni budou blokovat čísla mimo kontakty.

Telefon se tak na Hacker News stal spíš symbolem nedůvěry než pokroku: nová hlasová brána je technicky elegantní, ale komunita v ní vidí hlavně další palivo pro robotické volání.
