# 49981905
**Funkce navrhovaných zpráv v Claude Code: skutečným zákazníkem je model**

Hacker News · zed_labs_dev · 6. října 2026, 20:00 · 165 bodů / 89 komentářů · [diskuse](https://news.ycombinator.com/item?id=49981905)

Uživatel zed_labs_dev nasdílel blog, který označuje navrhované zprávy za nejchytřejší funkci Claude Code. Jde o šedý text s tipem na další příkaz, který stačí potvrdit klávesou Tab a odeslat. Podle ohlasů v diskusi ho část lidí vídá už měsíce, jiní o něm slyší poprvé.

Samotný blog se nepodařilo načíst, z reakcí je ale jasná jeho hlavní teze: návrhy tu nejsou primárně pro pohodlí člověka, nýbrž jako tréninkový signál pro model. Přijetí návrhu znamená dobré, odmítnutí a vlastní text znamená špatné – plus k tomu zdarma kvalitní data přímo z produktu.

Právě kolem téhle teze se strhla nejvěcnější přestřelka. Uživatel stavros namítá, že k tréninku zobrazení vůbec není potřeba, model může tipovat potichu a porovnat s realitou, takže jediný důvod ukazování je ovlivnit další prompt. Uživatel bugos se ptá podobně a uživatel spwa4 vysvětluje logiku druhé fáze tréninku: ten jeden bit informace, zda člověk návrh vzal, je cenný a přímo svázaný s produktem. Proti tomu stojí uživatelé namanyayg, yapfrog a wzdd s námitkou, že zobrazený tip odpověď zkresluje a vnese do dat nechtěné vychýlení, zatímco uživatel ismailmaj hájí opačný pohled, že vlákno má mnoho rozumných pokračování a bez ukázky by se model trestal za tip, který by uživatel klidně vzal.

Druhá linka řeší, jak návrhy mění práci. Uživatel gedy si stěžuje, že tip často není špatný, ale není to to, co chtěl udělat dál, přesto ho vyruší a někdy se jím nechá strhnout, takže z predikce je spíš sebenaplňující se proroctví. Uživatel crazygringo to naopak popisuje jako největší úsporu ve fázi implementace, kdy jen kontroluje okrajové případy a potvrzení přes šipku a enter mu ušetří psaní asi ve třetině tahů. Uživatel andy99 dodává, že problém není koncept výchozí volby, ale rozhraní, které člověka vyruší právě ve chvíli, kdy přemýšlí, a přirovnává to k otravným vyskakovacím pomocníkům.

Třetí proud je čistá averze vůči doplňování vět. Uživatel Cyan488 píše, že podobné našeptávače nesnáší od dob navrhovaných odpovědí v e-mailech, uživatel kccqzy kvůli tomu léta vypíná i návrhy vyhledávání a uživatel jonplackett se ptá, jak to vypnout ve zprávách od Applu. Odlehčení přinesl uživatel benregenspan poznámkou, že tady mu to nevadí, protože robot se na rozdíl od člověka neurazí méně procítěnou odpovědí, a uživatel rspeele historkou o Gmailu, který sám skládá přeslazené odstavce o rodině a kočce. Mezitím uživatelé cmrx64, skeledrew a ehwa37 upřesňují, že funkce žije už měsíce a vyvolává se Tabem, a uživatel GoToRO připomíná vedlejší sběr zpětné vazby na otázku, jak se Claudu daří, včetně celé relace.

Z diskuse tak zůstává rozpolcený obrázek šikovného pomocníka a tichého sběrače dat v jednom: šetří prsty, ale zároveň formuje, co člověk vůbec napíše.
