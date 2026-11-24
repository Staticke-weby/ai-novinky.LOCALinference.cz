# 50610334
**Security hell: maintaineři už nestíhají záplavu reportů od chatbotů**

Hacker News · qtqtqt · 23. listopadu 2026, 12:34 · 242 bodů / 149 komentářů · [diskuse](https://news.ycombinator.com/item?id=50610334)

Vývojář Gentoo Michael Orlitzky popisuje další kruh bezpečnostního pekla: open source projekty zaplavují hlášení zranitelností od lidí i chatbotů. Prakticky všechny bug bounty programy se kvůli AI slopu zrušily, ale příliv reportů nepřestává a jejich třídění zabírá maintainerům stále víc času a energie.

Velká část těch hlášení jsou přitom jen teoretické chyby typu REDoS nebo jiné výkonnostní problémy bez reálného útočného scénáře. I taková neplatná hlášení ale často dostanou CVE s absurdně vysokým skóre a bezpečnostní skenery pak tlačí správce balíčků k zbytečným záplatám a prázdným bumpům verzí. Většina projektů navíc nemá kapacitu na LTS větve ani čisté bezpečnostní releasy, takže se opravy mísí s novými funkcemi, deprekacemi a změnami API a lidé níže v závislostním stromě pak musí narychlo řešit rozbité rozhraní.

Diskuse se rychle stočila k tomu, kdo za to může a co s tím. Uživatel prologic chválí úvod článku za to, že neukazuje na jednu příčinu, a přiznává, že sám už rezignoval: je rychlejší si věc potichu forknout, opravit a jít dál. Uživatel pixl97 to shrnuje větou, že na vině jsme všichni, počítače jsou nebezpečné podobně jako zbraňový uran a kritického množství jsme už dosáhli. Vedle toho se rozjela přestřelka o Rustu, když ketzu namítá, že software z minulosti byl šíleně nezabezpečený a Rust rozhodně nezastínil jinou než paměťovou bezpečnost, zatímco LtWorf odpovídá, že u každého přepisu do Rustu se bezpečnost uvádí jako jediný důvod.

Nejvěcnější spor patří zbytečným bumpům verzí. Uživatel hypfer se ptá, jestli právě tohle uklidňování skenerů nebylo chybou a jestli nemá konečně někdo dělat tření a rozbít tenhle jasně nefunkční mechanismus. PeterStuer kontruje, jak jinak má uživatelům sdělit, že zkontroloval a Gentoo se problém netýká, a TZubiri navrhuje prostou větu do readme. Uživatel hypfer ale trvá na tom, že tenhle pocit klidu je primárně compliance potřeba, kterou by si firmy měly zaplatit, a ne práce zadarmo.

Zbytek vlákna hledá východisko a moc se neshodne. Uživatel markus_zhang se diví, proč maintaineři prostě nejedou vlastním tempem s cedulí používejte na vlastní riziko, za což schytává odpovědi od AnthonyMouse, wat10000 i dspillett: u bezpečnosti nejde ubrat, protože po zveřejnění zranitelnosti běží prohraný závod s časem a neopravený projekt je nebezpečí pro celou síť. Uživatel dools navrhuje, aby údržbu open source zaplatili prodejci AI, kteří na něm trénují a jejichž nástroje díry hledají. Uživatel iamnothere volá po opaku, po méně softwaru a návratu k suckless minimalismu ve stylu OpenBSD. Do toho si snk z článku odnáší novou hlášku do podpisu o shellu, který spouští nebezpečné příkazy, když je napíšete.

Výsledkem celého kolotoče je podle Orlitzkého i komentujících ztráta důvěry: vývojáři přestávají spoléhat na okolí, všechno si bundlují a dluh jen dál roste.
