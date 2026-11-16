# 50002215
**Clojure v éře jazykových modelů**

Hacker News · silcoon · 8. října 2026, 07:56 · 36 bodů / 13 komentářů · [diskuse](https://news.ycombinator.com/item?id=50002215)

Uživatel silcoon nasdílel esej programátora vystupujícího pod jménem yogthos o tom, proč se učit Clojure právě teď. Tvrdí v ní, že v době generativních modelů je nejdůležitější umět rozpoznat tvar problému a zvolit správný způsob jeho vyjádření. Imperativní programování se podle něj stává obdobou assembleru: modely umějí psát kód v malém, ale tápou ve vysoké architektuře a návrhu.

Největší váhu přikládá rychlosti ověřování. Clojure běží v živém procesu, funkci lze předefinovat v REPL a nová verze začne platit okamžitě, bez restartu a bez zdlouhavého přestavování stavu aplikace. K tomu se přidává neměnnost a čisté funkce, které lze testovat po jedné a v izolaci, a makra s homoionickou syntaxí, kdy kód je zároveň datová struktura. Výsledkem je stručný deklarativní kód, který stojí méně tokenů a vejde se i s širším kontextem do okna modelu. Tření kolem JVM má pak odstranit projekt Jolt, kompilátor v jediném binárním souboru s vestavěnou správou závislostí, který umí přes FFI vyjít s nativním ekosystémem a stavět samostatné binárky.

Právě kolem znovuvytváření stavu se rozjela nejdelší výměna. Uživatel mrkeen namítl, že od toho jsou testy a žádný vnitřní stav by neměl vyžadovat složité naklikávání, aby se k němu člověk dostal jednoduchým voláním. Autor eseje yogthos odpověděl, že unit testy pomohou jen do určité míry, protože nezachycují vztahy napříč kódem, a při hledání správného řešení psaní testů předem svazuje a brzdí experimentování.

Souhlasně se ozval dzonga: Clojure je pro éru modelů dobře stavěná, protože je úsporná na tokeny, všechno je data a čisté funkce se snadno ověřují. Zároveň ale upozornil, že člověk pořád musí umět clojurský kód číst a psát, což jde proti módní vlně, která hlásá, že kód už číst netřeba. Yogthos na to navázal výzvou, aby se lidé Clojure skutečně učili, protože porozumění kódu zůstává nutné a stručný expresivní jazyk dává s modely po boku větší smysl než kdy dřív.

Závěr vlákna patří živému ladění. Uživatel slifin chválí nástroj Flowstorm, který zpřístupní všechna data programově, takže si z nich člověk může postavit vlastní rozhraní nebo je předhodit modelu, aby hlouběji pochopil chování programu. Giancarlostoro k tomu dodává vlastní zážitek s tvorbou grafických rozhraní v Clojure, kdy se výsledek překresluje v reálném čase.

Z diskuse tak vychází Clojure nikoli jako nostalgická exotika, ale jako praktický nástroj pro dobu, kdy je psaní kódu levné a drahé zůstává ověřování a iterace.
