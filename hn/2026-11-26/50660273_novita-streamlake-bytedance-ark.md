# 50660273
**Novita a StreamLake jsou přeprodejci ByteDance Ark, tvrdí investigace**

Hacker News · leafingensemble · 26. listopadu 2026, 22:59 · 77 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50660273)

Blog zveřejněný 25. listopadu tvrdí, že poskytovatelé Novita, StreamLake a Ant Digital ve skutečnosti jen přeprodávají přístup k modelům DeepSeek přes platformu Ark firmy ByteDance. Autor sledoval tok tokenů DeepSeeku přes jejich endpointy a podle grafu měla samotná Novita posílat 120 až 160 miliard tokenů denně, zatímco Ant Digital 21. listopadu vyskočil zhruba z 1 na 35,8 miliardy tokenů denně.

Jako důkazy uvádí několik shodných otisků: obrázky poslané do modelů stahují servery Volcano Engine v Pekingu a BytePlus v Singapuru, odpovědi nesou request ID ve formátu ByteDance a tool-call ID ve tvaru Ark a na citlivé dotazy se vrací čínská strojová odmítnutí. Přidává i starší kauzu s modely MiniMax, kdy třetí strana otevřela unikátní adresy vložené do promptů s odstupem 40 až 130 hodin, a poznamenává, že OpenRouter mezitím odebral Novitě status zero data retention a stáhl 16 jejích endpointů.

Právě nulové uchovávání dat je pro diskusi hlavní téma. Uživatel keyle píše, že by OpenRouter měl u každého poskytovatele vyžadovat vlajku země, protože značce „zero data retention" už nevěří a sám si provoz omezuje na dva až tři ověřené dodavatele. Autor vlákna leafingensemble na to odpovídá, že Novita byla na stránce poskytovatele označená jako firma se sídlem v USA, ale požadavky směrovala na servery v Číně a Singapuru.

Uživatel snake_doc vysvětluje možný ekonomický motiv jako arbitráž výpočetního výkonu: přeprodejce nakoupí základní provoz za běžné ceny API a marži si nechá ve chvíli, kdy se mu podaří sehnat levné přerušitelné grafické karty. Uživatel samuelknight varuje, že si takovými hrami poskytovatelé zničí pověst během jediného dne a stáhnou s sebou i OpenRouter, pokud pochybné firmy okamžitě nevyhodí.

Nejemotivněji to formuluje uživatel jmward01, pro kterého je nulová retence červenou čárou a otázkou živobytí. Pokud jeho data skutečně končí u firmy, která je čte a využívá, píše, že neví, co na to říct. Uživatel peri-cl pak obviňuje OpenRouter, že měsíce inzeroval poskytovatele z Kajmanských ostrovů jako bezpečného a nedělal žádnou kontrolu ani hloubkovou prověrku.

Závěr vlákna tak spíš než o samotný Ark je o důvěře: bez ověřitelné garance, kudy požadavky skutečně tečou, je nálepka soukromí jen slibem na papíře.
