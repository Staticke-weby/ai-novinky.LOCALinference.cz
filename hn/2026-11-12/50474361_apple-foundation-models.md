# 50474361
**Apple otevřel Foundation Models framework. LLM v aplikaci přes Swift**

Hacker News · kermatt · 12. listopadu 2026, 22:13 · 180 bodů / 25 komentářů · [diskuse](https://news.ycombinator.com/item?id=50474361)

Apple nabízí vývojářům jednotné nativní Swift rozhraní pro zapojení velkých jazykových modelů přímo do aplikací. Framework dává přímý přístup k vlastním modelům Apple běžícím na zařízení i v Private Cloud Compute a přes stejné programové rozhraní umí sáhnout i po serverových modelech třetích stran, například Claude nebo Gemini.

Dokumentace láká na hotové stavební bloky pro chytřejší aplikace: řízené generování výstupů, volání nástrojů, multimodální dotazy s porozuměním obrázkům včetně integrace rozpoznávání textu a čárových kódů a novinku Dynamic Profiles pro přepínání modelu, teploty či sady nástrojů v rámci jedné konverzace. K tomu Apple přidává testovací Evaluations framework, příkazový nástroj fm pro macOS 27 a otevřené balíčky pro Swift i Python. Framework firma poprvé představila už na WWDC 2025 a letos ho výrazně rozšířila.

První otázka v diskusi je, proč se známá stránka znovu dostala na titul Hacker News. Uživatel HelloUsername připomíná, že se o frameworku mluvilo už loni při oznámení, uživatel michaelbuckbee to vysvětluje spekulacemi, že Apple chystá novou sadu lokálních modelů. Tón debaty tím udává spíš nová podpora cizích modelů a serverového běhu než samotný základ.

Praktické zkušenosti zní překvapivě příznivě. Uživatel albertgoeswoof popisuje, že modely používá v terminálu na opravu chyb a navrhování příkazů a na osmigigabajtové M1 mu přijdou překvapivě schopné. Uživatel jshier se ptá, jestli ho nebrzdí poměrně přísná bezpečnostní omezení, uživatel _pdp_ zase píše, že Foundation Models s oblibou používá ve své aplikaci Noodle a Private Cloud Compute má zatím na seznamu k prozkoumání. Uživatel cj00 upozorňuje, že trochu pod radarem létá snaha Applu převádět otevřené modely do vlastního formátu pro nativní běh ve Swiftu.

Nejživější linka se točí kolem ceny a kódování. Uživatel dvdplm se ptá, jestli lokální model vůbec umí kódovat třeba jako prediktor v editoru Zed, uživatel bobertdowney odpovídá, že i silnější cloudový model měl potíže s jeho úkolem naprogramovat webovou skákačku. Uživatel btown se pozastavuje nad nabídkou bezplatného přístupu k Private Cloud Compute pro malé vývojáře, uživatel taneq to glosuje jako vzorky tokenů zdarma. Uživatel nseggs, který službu používá v TestFlightu i v ostré aplikaci, ji chválí za výkon a za to, že se spotřeba počítá koncovým uživatelům, nikoli vývojáři, vadí mu ale menší kontextová okna a otravné limity. Uživatel SwtCyber to shrnuje, že pro malou aplikaci s občasnou inferencí to může být velká věc, a dodává, že Apple teď nabízí jednotnou abstrakci nad konkurenčními poskytovateli a už se prý někde hledá, která specifická funkce ji jako první rozbije.

Nechybí ani špičkování. Uživatel amelius vzkazuje, že si nechá framework postavit od svého jazykového modelu, na chválu Siri od uživatele okaymac reaguje uživatel SwtCyber rýpnutím, že ta jeho má občas problém i s nastavením časovače.
