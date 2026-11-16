# 1wzf641
**AI dokázala optimalitu skládání 11 čtverců, ověřeno v Lean**

r/singularity · u/Hyperreals_ · 6. října 2026, 23:41 · 855 bodů / 244 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1wzf641/)

Uživatel u/Hyperreals_ zveřejnil obrázek podivně natočených čtverců s tvrzením, že modely Astra a Claude konečně rozsekly starý geometrický oříšek. Prokázaly, že nejlepší známé poskládání jedenácti jednotkových čtverců je skutečně optimální. Důkaz je formalizovaný v Lean, tedy strojově ověřený.

Samotný příspěvek tvoří jen obrázek s odkazem na X, takže detaily museli čtenáři lovit v diskusi. Přímý repozitář 11SquaresFormalized tam nahodil u/p3r3lin a autor v komentářích doplnil přesnou hodnotu strany vnějšího čtverce vzorcem (6u+4)/(1+2u-u^2), kde u je kořenem polynomu 5u^8-10u^7-2u^6+14u^5+12u^4-6u^3+2u^2+2u-1 na intervalu (9/25, 37/100), číselně asi 3.87708359.

První vlna reakcí řeší hlavně to, jak příšerně výsledek vypadá. Nejvýše hodnocený u/Savings-Divide-7877 vesmíru vyčítá, že čtverce vůbec fungují takhle, u/rarzwonovi přijde obrázek „opakem uspokojivého" a u/tribecous píše, že kdyby někoho viděl takhle rovnat krabice, okamžitě by si o něm pomyslel, že je idiot. Do téhle noty zapadá i u/MelvinCapitalPR, podle kterého je skládanka tak ošklivá, až se to obrací zpátky v krásu, a u/Exodus_Green, kterého nejvíc drásá malá mezera mezi zelenými čtverci, kam se špičkou vtlačuje kosočtverec.

Věcnou linku drží sám autor. Vysvětluje, že tohle rozložení bylo nejlepším známým už od roku 1979, jen se dosud nevědělo, zda je optimální, a na otázku u/onnoowl, kde se takové důkazy vůbec začínají, odpovídá chytrou redukcí na konečnou množinu podezřelých případů, které pak jeden po druhém vyloučí. Když se u/THROWAWTRY diví, že tenhle obrázek viděl už před deseti lety, upřesňuje pointu: do žádného menšího čtverce jedenáct jednotkových čtverců prostě nenacpete.

Zbytek vlákna sklouzává k parodii a praktickým poznámkám. u/JoelMahon glosuje vyčnívající špičku hláškou o tom, že „špička se nepočítá", u/FreeKony2016 i u/waxen_earbuds si utahují z přemoudřelého žargonu o svazcích a nekonvexní optimalizaci a u/vicarion přihazuje trefný XKCD 2740. Mezi tím se objeví i čistě lidská otázka u/Distinct-Question-16, jaká je asi šance tohle náhodně poskládat, když člověk v kufru auta rovná jedenáct krabic.

Zapadá to do větší série: navazující preprint Almana a Vassilevske Williamsové hlásí první skutečně subkvadratický 3SUM a subkubický APSP od interního modelu Anthropicu, takže formální matematika se rýsuje jako jedna z nejviditelnějších arén současných modelů.
