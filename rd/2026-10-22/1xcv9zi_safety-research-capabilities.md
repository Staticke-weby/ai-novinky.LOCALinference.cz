# 1xcv9zi
**Safety research = capabilities research: 4 000× zrychlení bez backprop**

r/singularity · u/ResultBackground2450 · 22. října 2026, 23:24 · 376 bodů / 34 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xcv9zi/)

Autor sdílel obrázek, který láká na projekt QLabs Noise trénující malý model zcela bez zpětného průchodu, jen pomocí perturbací aktivací. Příspěvek označený flairem AI okamžitě rozdělil diskusi na nadšené a skeptické, protože titulek zní jako průlom v samotných základech trénování sítí.

Odkaz na stránku projektu doplnil v komentářích u/yaosio a rovnou přidal varování, že jde o velmi malý model a vůbec není jasné, jestli se metoda škáluje. Právě tato stránka je faktickým zdrojem čísel z obrázku, externí článek se k balíčku nenačetl.

Vysvětlení čísel přinesl u/daniellenton: čtyřtisícinásobné zrychlení se měří proti jejich vlastnímu prvnímu běhu bez backpropu dlouhému 1,76 hodiny, a to k validační ztrátě 4,2 na GPT se 37,7 milionu parametrů. Výsledek 3,676 sice poráží backprop s Adamem s hodnotou 3,769, ale stejný optimalizátor s backpropem je podle autorů pořád vpředu. Zároveň odmítá tvrzení o continual learningu, protože jde pořád o odhad gradientu posílaný do normálního optimalizéru a zapomínání vzniká tím, že nové updaty přepisují ty staré, ať byl gradient získán jakkoli levně.

Nadšení v diskusi patří hlavně matematice. U/veshneresis se jako ML inženýr přiznává, že o odhadu gradientů perturbací aktivací nikdy neslyšel, přijde mu to neznámé, ale hodně elegantní, a v editaci hlásí, že si metodou natrénoval hračkový model na MNISTu. U/maj160 z toho vyvozuje největší praktický slib: když odpadne posílání všech gradientů mezi grafickými kartami v každém batchi, mohl by fungovat distribuovaný trénink klidně po internetu, něco jako LLM doma, a perturbace po jednotlivých tokenech prý dávají víc tréninku z jednoho vstupu. U/Valeand ale kontruje, že právě škálování je velké jestli a dimenzionální exploze bude místo, kde přístup selže.

Třetí linka jsou domácí pokusy a krocení očekávání. U/AI_Simp si na laptopu upravil původní Dust kód a model se 147 tisíci parametry mu za asi 12 minut správně spočítal 560 z 956 zadržených sčítání, přičemž operandy byly 0–99 a obrácené dvojice byly zadržené spolu. U/New_World_2050 připomíná, že zisky jsou jen relativní vůči dosavadním metodám bez backpropu, které byly mizerné, a nejde o čtyřtisícinásobek proti současnému backpropu. Zbytek už je směs úžasu, žádostí o vysvětlení pro laiky a jízlivostí o senzačním titulku, nejsyrověji od uživatele, podle kterého jde o šarlatány skládající slova dohromady pro body na internetu.

Z diskuse tak zbývá elegantní trik, který funguje v malém a láká představou levného distribuovaného tréninku, ale důkaz ve velkém zatím chybí.
