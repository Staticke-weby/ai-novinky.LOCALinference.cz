# 50163961
**Výpadek Google Cloud v Evropě ochromil banky i Revolut**

Hacker News · paweladamczuk · 20. října 2026, 12:26 · 362 bodů / 182 komentářů · [diskuse](https://news.ycombinator.com/item?id=50163961)

V evropské části Google Cloudu nastal výpadek, který ochromil bankovní služby a další online provozy. Uživatelé od rána hlásí nefunkční aplikace, zamítnuté platby kartou i nemožnost dostat se k vlastním penězům.

Odkaz míří na zprávu Neowinu, která potíže spojuje s HSBC, Revolutem, Bank of Scotland, Lloyds a Equifaxem. Google na statusové stránce citované v diskusi mluví o výpadku proudu v zóně europe-west2-b s počátkem v pondělí ve 23:08 pacifického času a slibuje postupnou nápravu nejprve u infrastrukturních služeb. Souběžně se na Hacker News řeší nefunkční Revolut a výpadek zóny europe-west2 ve dvou samostatných vláknech.

Nejosobněji zní úvodní zkušenost uživatele paweladamczuk: nemá přístup k hlavnímu účtu, neprovede výběr ani platbu a v aplikaci se nikam nedovolá, protože neexistuje telefonní číslo ani živý kontakt. Podobně dopadl rpozarickij, který nezaplatil v obchodě a obsluha se ho rovnou zeptala, zda platí Revolutem, naštěstí měl po ruce kartu jiné banky v Apple Pay. Výpadek se propsal i mimo bankovnictví, misstuned ráno neodemkl sdílené kolo v systému Beryl. Odlehčení dodává chrisjj poznámkou, že tahle „banka" možná tuší, že by s cloudem lehly i její telefony, a gadders rýpnutím, že do Lloyds se leckdo nepřihlásí, ani když už cloud poběží.

Druhá linka se točí kolem toho, proč vše spadlo najednou. Arbortheus oceňuje Monzo, které po dřívějším výpadku postavilo nouzový systém na odděleném kódu a u jiného poskytovatele cloudu, takže základní bankovní operace jedou i bez parádiček. Navazuje debata o suverenitě: gentlerain glosuje, že se mluví o suverenitě v umělé inteligenci, ale zapomnělo se na suverenitu výpočetní, zatímco Arbortheus a crumby připomínají, že právě požadavek držet data v Británii tlačí firmy do jediné britské zóny se všemi vejci v jednom košíku.

Třetí spor patří architektuře a měření výpadků. Uživatel nickcw se diví, že velké firmy nejely přes více zón, robinson-wall odpovídá, že s multizónou je to jako se zálohami, netestovaná neexistuje, a bsuvc dodává, že někdy mají závislosti napříč zónami i sami poskytovatelé. Přitvrzují TacticalCoder s obrazem opitého „cloudového" slibu, že se o všechno někdo postará, Betelbuddy tvrzením, že zóna Googlu není totéž co zóna u Amazonu, a kune odkazem na dokumentaci, podle níž mají některé regiony všechny zóny v jedné či dvou budovách. Stranou se hádá o Downdetector: bcvvvy ho kvůli hlášením od uživatelů pokládá za špatný zdroj a tvrdí, že jeho HSBC funguje, zatímco m11a, rurp a Johnny555 oponují, že prudké špičky hlášení sedí a oficiální statusové stránky mlčí častěji.

Z vlákna tak zůstává hlavně varování před soustředěním klíčových služeb u jednoho poskytovatele a v jednom místě, bez zálohy, která by byla skutečně vyzkoušená.
