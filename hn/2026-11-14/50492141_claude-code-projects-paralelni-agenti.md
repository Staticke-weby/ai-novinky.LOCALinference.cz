# 50492141
**Claude Code Projects umí řídit paralelní agenty**

Hacker News · toppa33 · 14. listopadu 2026, 01:28 · 98 bodů / 91 komentářů · [diskuse](https://news.ycombinator.com/item?id=50492141)

Anthropic předělal Projects v Claude Code na systém pro paralelní práci agentů. Uživatel popíše, co je potřeba udělat, a koordinátor si práci sám rozvrhne, rozdělí do vláken, zkontroluje výstupy a složí hotový výsledek. Postup lze sledovat a kormidlovat v hlavním chatu projektu, klidně i z telefonu, a práce běží dál, i když člověk odejde od počítače.

Každé vlákno je přitom plnohodnotná cloudová session Claude Code na vlastní větvi a vlastní kopii repozitáře, takže překryv v kódu se řeší stejně jako běžný merge konflikt. Kontext se mezi vlákny kumuluje díky sdílené paměti a knihovně souborů, kam se ukládají přidané materiály i věci, které Claude vyrobí. Nová podoba projektů je v betě pro vybrané předplatitele Pro a Max, kteří používají cloudové session, a provoz několika vláken najednou rychleji ukrajuje z limitů.

Do diskuse přišel i Boris z týmu, který vysvětluje motivaci: lidé si na Claude Code zvykají a pouštějí stále víc agentů paralelně, jenže správa takové farmy a neustálé přepínání pozornosti je vyčerpávající. Koordinátor má právě tuhle režii převzít, zatímco soustředěná práce na jednom úkolu zůstává dál důležitá. Spousta čtenářů jeho popis poznává z vlastní praxe, jeden píše, že podobnou orchestraci zkoušel stavět přes skilly, subagenty i sdílenou paměť, ale stálo ho to spoustu mentální práce navíc.

Nejživější linka je ale o ceně. LoganDark popisuje, jak se zeptal Clauda na nejlepší knihovnu pro Discord bota, model spustil sedm subagentů a za deset minut mu vyčerpal celý limit. augment_me to shrnuje kysele jako skvělý způsob, jak automaticky zvýšit spotřebu a vytáhnout z lidí peníze. HEmanZ k tomu přidává dvě další úzká hrdla, která paralelizace sama neřeší: zadat projekt tak přesně, aby byl člověk s výsledkem spokojený, a předem odhadnout, kolik tokenů a času spolkne.

Druhá velká výhrada je, kde vlákna běží. enraged_camel píše, že orchestrátory v cloudu se pro spoustu práce nehodí, protože nevidí na soubory a zdroje na vývojářském stroji, a přeje si lokální běh. Anthropic v článku slibuje právě tohle brzy doplnit. Vedle toho se řeší i chybějící worktrees pro více úloh ve stejném repu, dostupnost v CLI a obava, kterou formuluje taurath: že špičkoví agenti pořád píšou nepřesný kód, falšují testy a dělají rozhodnutí, která se pak špatně udržují.

Kdo si paralelní řízení už postavil sám, vítá, že ho nebude muset udržovat. Zůstává ale otázka z diskuse, jak práci vzdálených agentů vlastně posuzovat — jestli koukat do diffů, věřit koordinátorovi, nebo chtít jiný hmatatelný výstup.
