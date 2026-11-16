# 1xw80tg
**MOSS Image: jednoduché nastavení poráží placebo ladění**

r/StableDiffusion · u/Rare_Subject2343 · 14. listopadu 2026, 18:27 · 289 bodů / 42 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xw80tg/)

Generátor obrázků MOSS Image má za sebou týdny pečlivého ladění a výsledek je překvapivě strohý: nejlépe funguje jednoduché nastavení. Posouvání parametrů sem a tam působí spíš jako placebo s minimálním efektem, zatímco ořezaný vstup drží generování stabilní a často i hezčí.

Nejvyšší hlasy posbíral rozbor od u/Officially_Beck, podle kterého dávají schedulery Simple, Normal, SGI, DDI a Linear téměř totožné výsledky. Beta umí být realističtější, ale zároveň si vymýšlí, přidává třeba nechtěná tetování, mění oblečení nebo kus oděvu rovnou sundá, zatímco Exponential a Karras generování vyloženě rozbijí. Na to navazuje u/Sarashana s tezí, že výběr scheduleru a sampleru se bezpečně vejde do hranic osobního vkusu, takže klidně Euler a Simple na všechno už proto, že je to rychlé.

Podobnou zkušenost popisuje u/Necessary_Echo8740: velká část komunity se snaží model doostřit, zacílit a zkrotit složitým promptováním, což ale jde proti tomu, v čem vyniká. Když se vstup ořeže a cfg drží nízko, jsou výstupy samy o sobě šokujícně dobré, protože právě chaos a nejistota dělají obrázky realistickými. Do toho u/FaceDeer připomíná klasickou Skinnerovu studii o pověrčivosti u holubů, v generování je totiž tolik náhodnosti, že zdánlivé vzorce snadno klamou. Praktickou linku přidává u/Used-Amphibian-844 s receptem na 3 megapixely, 50 kroků, cfg 3, Euler a Simple, což prý dává skvělé výsledky pokaždé, a u/Ok-Lengthiness-3988 doplňuje, že rozlišení nad 2 megapixely pomáhá víc než cokoli kolem 1 megapixelu.

Jediný vážnější spor se vede kolem er_sde. Zatímco u/mearbode provokuje strohým „er_sde, 25 kroků“ a u/Significant-Baby-690 kontruje „ER-SDE, simple“, u/Ken-g6 tvrdí, že u MOSS hodně pomáhá er_sde uzel s vlastním vylepšením šumu, a u/citrusalex hlásí z vlastních testů konzistentně lepší obrázky než s Eulerem. Kusý smír nabízí u/Comrade_Derpsky ze zkušenosti s Krea 2: sampler a scheduler moc neřeší kompozici, která zůstává se stejným seedem víceméně stejná, ale na ostrost a jemné detaily prý res_multistep se sgm_uniform poráží Euler se Simple. Stručnou tečku dělá u/Solembumm3 s kombinací Krea 2, Res Multistep a simple, otázka u/mujhe-sona-hai, zda je Moss lepší než Krea 2 a Kroma, zůstala ve vlákně bez jasné odpovědi.

Kdo nechce trávit víc času šroubováním nastavení než samotným generováním, má z diskuse jasný vzkaz: nechat to jednoduché a hrát si spíš s rozlišením a mírou chaosu.
