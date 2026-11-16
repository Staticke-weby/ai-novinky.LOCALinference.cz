# 1xbsxxm
**Opus 5.5 vytvořil Unity VFX: exploze, blesky i ledové hroty**

r/ClaudeAI · u/Excifroge · 21. října 2026, 19:06 · 273 bodů / 31 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xbsxxm/)

VFX umělec u/Excifroge strávil poslední dva týdny tím, že s Claude Code a modelem Opus 5.5 stavěl herní efekty v Unity. Výsledkem jsou tři hotové prefaby: ohnivá exploze, úder blesku a ledové hroty. Nejde o vyrenderované video, ale o skutečné Shuriken particle systémy přímo v enginu.

Claude přitom neklikal v editoru, ale psal Unity editor skripty, které samy sestavily částicové systémy, materiály i přiřazení textur. Druhý skript pak nasnímal snímky pevnou kamerou s pevným seedem a poskládal je do jednoho archu, podle kterého Claude poznal, co změnit, a build skript přepsal. Každý efekt takhle prošel deseti až patnácti koly, ta pozdější už podle poznámek autora. Největší rozdíl podle něj udělal vlastní „skill" sepsaný z jeho VFX praxe s výrobními kroky a vizuálními pravidly. Textury Claude vymýšlel přes prompty a generoval přes Codex worker, každý výsledek kontroloval, ledové krystaly pak psal v Pythonu pro Blender a přes Blender MCP je nechal vymodelovat, zdecimovat a zapéct včetně normálových a maskovacích map. Všechny materiály stojí na jeho VFX shaderu VFX Essential, který s Claudem refaktoroval a zdarma uvolnil pod licencí MIT.

Diskuse se shodla, že kvalita je šílená. u/B4ckZ efekty přirovnal ke kouzlu z WoW a poděkoval za sdílení, u/Twerking_Vayne napsal jen „Holy.." a u/kylecito vyjekl nad kvalitou a prosil aspoň o hrubé tipy, co při promptování rozhoduje, že tajemství si autor klidně nechá.

Nejvíc lidi zajímalo, jak moc je to práce modelu a jak moc umělce. u/RedditsChosenName se ptal, jestli existují nahrávky prvních pokusů modelu samotného, aby bylo vidět, co udělal sám a co až po kolech revizí a vedení. u/kuroti se rovnou hlásil, že by efekty chtěl vyzkoušet, protože vypadají mnohem líp než jeho pokusy s Effekseerem, a u/bradandersonjr nadhodil, jak by se postup dal přenést do Godotu.

Třetí linka vlákna řeší jednorázové generování proti iteraci. u/Crackborn píše, že se snaží přimět Claudea k jistějším exotickým výstupům na jeden zátah, a ptá se, jestli jdou vytáhnout exotičtější věci. Automatické shrnutí od u/ClaudeAI-mod-bot to glosuje jasně: přestaňte honit dokonalý výsledek na jeden prompt, profíci staví celé workflow s kontrolním loopem a standardizovaným shaderem. Dodává i zklamání vlákna, že svůj klíčový skill autor zatím sdílet nechce.

Z vlákna tak zůstává jednoduché ponaučení: síla není v kouzelném promptu, ale v tom, že model vidí vlastní práci na archu snímků a dostane jasná výrobní pravidla, podle kterých ji umí desetkrát předělat.
