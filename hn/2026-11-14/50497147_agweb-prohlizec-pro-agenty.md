# 50497147
**agweb: prohlížeč pro agenty, který nekrade fokus**

Hacker News · paul_nameless · 14. listopadu 2026, 15:08 · 93 bodů / 27 komentářů · [diskuse](https://news.ycombinator.com/item?id=50497147)

Na macOS vznikl agweb, prohlížeč pro kódovací agenty postavený na WebKitu, enginu Safari. Běží v jediném okně, které nikdy nepřebírá fokus ani nevyskakuje do popředí, a agenti ho ovládají z shellu příkazy ve stylu playwright-cli. Autor ho postavil proto, že mu okna Playwrightu neustále kradla klávesnici, zatímco bezhlavé prohlížeče některé weby blokovaly a nešlo poznat, co se pokazilo.

Nečinné panely se uspávají, takže pět otevřených stránek má podle autora nulové vytížení procesoru a zabere 590 MB paměti proti 1,6 GB u Playwright Chrome. Přehled na klávesu ⌘D ukazuje živě všechny panely všech agentů včetně jejich posledního příkazu, pojmenovaný profil sdílí jedno přihlášení mezi více agenty najednou a tajemství se dá vyplnit tak, aby se nikdy nepropsalo do přepisu. Klikání a klávesy přitom působí jako lidské události, takže fungují i rozbalovací menu a přetahování.

Nejživější ohlas přišel od lidí, které trápí totéž co autora. anigbrowl píše, že testuje hlavně vlastní webové aplikace a přebírání fokusu během testů pro něj bylo bolestivé, k tomu mu vadila neúměrná náročnost Chromu. O to víc zamrzela podmínka macOS 26 a novější, kvůli které si _blk povzdechl, že se vrátí, až někdo pošle verzi pro Linux. CharlesW se ptal, proč vznikal další nástroj, když existuje agent-browser.dev a spousta alternativ, na což kevsamuel oponoval otázkou, která z alternativ ukazuje takový živý náhled.

Hodně se řešil sdílený profil. agline_in upozornil, že je to šikovné, ale jeden agent může odhlásit nebo zablokovat ostatní, když se odhlásí, přepne účet nebo narazí na limit webu, a ptal se na odštěpenou nebo jen čtecí kopii cookies. tomaskafka souhlasil, že někdy chce cookies sdílet, třeba při sledování tržiště, a jindy mít pro každého agenta vlastní pískoviště, což by mohlo naznačovat i rozhraní. pklym odpověděl, že zatím pomůže uložení stavu v jednom pracovním prostoru a načtení v čistém, takže odhlášení zůstane jen tam, a příznak pro odštěpení by šel dodělat.

Zbytek vlákna řeší kompatibilitu a detaily pro agenty. jazzypants se divil, proč nástroj napodobuje příkazy Playwrightu, ale nepodporuje CDP, bez kterého je pro něj nepoužitelný. bookernath ho chce zkusit na ověřovací toky a zarazilo ho, že je blokování reklam zapnuté výchozí, 7777777phil naopak chválil, že blokovač nechává na pokoji dialogy se souhlasem s cookies, což jstanley glosoval otázkou, co je na nich dobrého. Praktickou tečku přidal dfish, podle kterého agweb denně používají a mají ho rádi jako lehčí náhradu plné plochy Atlasu.
