# 1xbe2tf
**Linux kernel už nebude vyžadovat deklaraci použití AI u nového kódu**

r/singularity · u/chessboardtable · 21. října 2026, 06:55 · 824 bodů / 130 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xbe2tf/)

Vývojáři linuxového jádra už u nových patchů nemusejí přiznávat, že jim pomáhá umělá inteligence. Změna přišla jen několik hodin před zveřejněním příspěvku, který ji bez dalšího komentáře ohlásil jen obrázkem s označením AI – a v diskusi je čtena hlavně jako tichá normalizace kódu psaného s AI.

Nejvýše hodnocený komentář patří u/dsanft, podle kterého staré předsudky o tom, že kód z AI je automaticky odpad, pocházejí ještě z éry Sonnetu 4.5 a na dnešní Opus 5.5 už nesedí. Podobně laděný je i vzkaz u/ProxyLumina, že kódu od AI věří víc než kódu od lidí, a provokativní glosa u/tendeer, že kdo dnes jako vývojář nepracuje s asistencí AI, není to otázka vkusu, ale neschopnosti držet krok. U/141_1337 k tomu jen suše předpovídá, že kolem zrušení povinnosti bude ještě pořádný poprask.

Druhá, věcnější linka debaty řeší, proč deklarace vůbec skončila. Podle u/Big-Molasses-7942 nebyla nikdy vymahatelná, protože nikdo nebude na patch, který tři hodiny ladil, dobrovolně lepit nálepku asistence. Tvrdí, že AI patche mají v diffu svůj otisk – zbytečnou obranou kontrolu na hodnotu, která nemůže být prázdná, komentář co čtyři řádky vysvětlující samozřejmost a sebevědomou commit zprávu bez zmínky o tom, co se cestou rozbilo. U/Fickle_Surprise8316 to rozvíjí: kernel AI kód nikdy nezakázal, jen přestal chtít jeho označování, což je vlastně přiznání, že nálepka nikdy nedělala skutečnou práci.

Když totiž kód projde čtením a testy, nálepka bezpečnost nezvýší, a když špatný patch projde, je to selhání recenze, ne označování. Do toho zapadá i připomínka u/superkickstart, že asistovaný kód byl povolený vždy a dál musí projít kontrolou a schválením jako dřív, takže o volnou cestu pro ledabyle nahozené kusy nejde. Praktický dopad popisuje u/AirGief: otravnou chybu v ovladači pro určitý čip si na svých strojích opravuje ručně při každém vydání jádra a teď zvažuje, že opravu pošle přes Claude, protože ho dřív odrazovala hlavně byrokracie kolem přispívání.

Z vlákna tak nakonec nejvíc vyčnívá věta, kterou sem poslal u/confused-photon: kód mluví sám za sebe. Deklarace končí, odpovědnost za řádek zůstává.
