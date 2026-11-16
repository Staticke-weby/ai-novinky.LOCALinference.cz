# 1xqd058
**Observer promění starý telefon v lokálního AI hlídače**

r/LocalLLaMA · u/Roy3838 · 7. listopadu 2026, 19:16 · 338 bodů / 52 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xqd058/)

Observer je open-source aplikace pro iOS a Android, která z telefonu udělá autonomního pozorovatele čehokoliv, na co namíříte foťák. Všechno vyhodnocování běží lokálně přímo v zařízení, bez posílání obrazu do cloudu. Aplikace je zdarma a její kód autor zveřejnil na GitHubu.

Ve výchozím nastavení kombinuje dva malé modely: rozhodovací OneJev-0.8b a pozorovací qwen-0.8b. Podle autora zvládnou běžet i na starších telefonech, které se lidem válí doma v šuplíku, takže místo sbírání prachu mohou hlídat. Sám ukazuje pět příkladů z praxe: upozornění s fotkou, když se k jeho autu přiblíží cizí člověk, zpráva přes telegram, když na hnízdo přiletí pták, telefonát, když pračka přejde do máchání, notifikace, když pes dojí misku, nebo volání, když se v posilovně uvolní stroj.

Ohlas v diskusi je vesměs nadšený. u/MuzafferMahi ji označil za jednu z nejzajímavějších ukázek, jaké v komunitě viděl, další děkují za nástroj i rychlé demo. Největší fantazii ale vyvolala otázka, co by lidé hlídali sami: u/nokia7110 by chtěl verzi, která telefon úplně zamkne, dokud neudělá dvacet kliků nebo dvacet minut nečte knížku, u/redbeardy_daddy zase navrhuje namířit ji na koš s prádlem a poslat upozornění, až ho někdo jiný uklidí, což by prý skvěle otestovalo dlouhodobou stabilitu.

Vedle nápadů se řeší i technické limity. u/MagicalVagina namítá, že na tyhle úlohy je to špatný nástroj a obyčejné strojové vidění by bylo mnohem rychlejší. u/Erdeem se ptá, zda aplikace zvládne sledovat víc zdrojů najednou, třeba celou mřížku domácího kamerového systému pokrývajícího pokoje i pozemek, a zda něco podobného nemá Home Assistant. Praktické pochybnosti přidávají u/WorriedBlock2505 s dotazem na vybíjení baterie a u/tf2ftw, kterého zajímá, jak si agent vede po několika hodinách běhu a zda si při pravidelném snímání nenafukuje kontext.

Detailisté si všimli i samotného videa. u/littlejerry99 upozorňuje, že v ukázce se židlí agent ještě ověřoval záběr, když před ní autor stál, a teprve v momentě usednutí kolem 58. sekundy ohlásil, že bude posílat upozornění. Odlehčení přidal u/aqezz otázkou, zda má autor nastaveného hlídače, který ho upozorní na příchod Qwen 4. Starý telefon jako soukromý hlídač auta, hnízda nebo pračky tak místním dává smysl právě proto, že nic nikam neposílá.
