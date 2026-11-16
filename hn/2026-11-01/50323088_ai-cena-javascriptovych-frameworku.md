# 50323088
**AI cena JavaScriptových frameworků: benchmark místo dojmů**

Hacker News · luu · 1. listopadu 2026, 07:06 · 336 bodů / 258 komentářů · [diskuse](https://news.ycombinator.com/item?id=50323088)

Vývojář Nolan Lawson se rozhodl skoncovat s dohady o tom, který JavaScriptový framework je „nejlepší pro agenty“, a nechal model Opus 5.5 postavit v každém z nich tu samou pokémonní aplikaci nad otevřeným PokéAPI. Stejné zadáníportoval do Next.js, Nuxtu, SvelteKitu, Astra, Qwiku a dalších sedmi stacků a každý pokus pro jistotu pětkrát zopakoval, aby odfiltroval náhodné výkyvy.

Z výsledků mu vyšlo, že rozdíly v ceně nejsou dramatické, ale jsou měřitelné: kombinace Hono + htmx a Astro se vešly zhruba do 2,70 dolaru na jeden běh, zatímco SolidStart a TanStack Start překročily 3,50 dolaru. Spolu s cenou rostla i spotřeba tokenů, čas běhu a počet řádků kódu a přidal k nim měření v Lighthouse – vedle téměř stoprocentního skóre výkonu a přístupnosti hlavně objem přeneseného JavaScriptu, blokovací čas a vykreslení největšího prvku. Sám přitom upozorňuje, že jde o jeden typ obsahové aplikace, že agenti i Lighthouse jsou silně náhodní a že oficiální MCP a pomocné dovednosti frameworků agenti využívali jen někdy.

Největší nadšení v diskusi vzbudilo Astro. Uživatel tancop píše, že bere Astro na příští projekt kvůli nejlepšímu času, druhé nejnižší útratě a nulovému klientskému JavaScriptu, vermilingua potvrzuje velmi příjemnou práci a genshii ho chválí na obsahové weby i reaktové aplikace. Ozývá se ale i protihlas: skrebbel připomíná, že test byl šitý na míru obsahovým webům, a ptá se, jak by dopadla interaktivní aplikace v reálném čase, zatímco spieke brání progresivní vylepšování ve SvelteKitu, které je s JavaScriptem rychlejší.

Druhá velká linka patří Angularu, který skončil s nejvyšším účtem i největším objemem kódu. Uživatel usernametaken29 v tom vidí potvrzení, že Angular je rozbitý i pro agenty, ozim ale jeho plošné odsudky odmítá s tím, že na malé aplikace se Angular prostě nehodí. Alex_suzuki vzpomíná, že právě přísnost a jednotnost Angularu mu v agentuře šetřila hlavu při přeskakování mezi projekty, TheRoque ho popisuje jako radost, která se rok od roku lepší, a Aozora7 tipuje, že nuda v podobě formulářů s validacemi by pořadím pořádně zamíchala.

Zbytek vlákna řeší, jestli má takové měření vůbec smysl. Uživatel neya namítá, že výběr frameworku nestojí na rychlosti, ale na znalosti týmu, udržitelnosti a důvěře, a raději si připlatí dva dolary za kód, kterému rozumí, selfmodruntime dodává, že mrtvě jednoduchá ukázka má k firemnímu produktu daleko. Vedle toho se vrací evergreen o holém HTML – drnick1 volá po stránkách bez javascriptových oblud, mmusc označuje frameworky za zbytečný boilerplate v éře AI a Joeri kontruje, že výhoda vanilly je i v menším balíku a kontextu pro agenta.

Ponaučení je tak spíš metodické než fanouškovské: místo dojmů se dá změřit cena, tokeny i JavaScript, ale jeden benchmark o obsahovém katalogu nerozhodne, na čem stavět složitou aplikaci.
