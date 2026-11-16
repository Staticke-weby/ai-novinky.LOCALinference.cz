# 50181114
**LiteLLM 1.107.0 na PyPI kradl klíče a otvíral backdoor**

Hacker News · abhisek · 21. října 2026, 16:00 · 477 bodů / 162 komentářů · [diskuse](https://news.ycombinator.com/item?id=50181114)

Vydání LiteLLM 1.107.0 na PyPI obsahovalo krádež pověření i zadní vrátka pro vzdálené spouštění kódu. Škodlivé soubory byly ve všech sedmi kolech pro Linux, macOS i Windows a PyPI je stáhl ještě týž den do 13:23 UTC. Zasažené byly mezi 11:46 a 14:20 UTC i obrazy na Docker Hubu a GHCR.

Odkazovaná analýza SafeDep popisuje, jak se implantát do balíčku dostal: zdroj na GitHubu zůstal čistý, v distribučním archivu ale přibyl v sekci maturin řádek s nastavením kopírujícím složku do site-packages. Po instalaci se tak v každém spuštěném Python procesu provedly soubory cook.pth s krádeží klíčů a sitecustomize.py se zadními vrátky, i když program LiteLLM vůbec neimportoval. Útočník podle zprávy LiteLLM získal přihlašovací údaje tří vývojářů a přes oficiální pipeline podepsal a publikoval podvržené artefakty.

Diskusi nejvíc rámuje únava z opakování. Uživatel rvz vyjmenovává, co všechno se seběhlo během jediného týdne, od výpadku cloudu přes únik soukromého klíče certifikační autority eMudhra a únik dat PingCap TiDB až po nálezy PHP2Shell, a mluví o druhém kole kompromitace LiteLLM. Přidává se rcleveng s povzdechem, že znovu, a stbenjam s větou, že jednou je odpustitelné, podruhé je to selhání řemesla. Ozývá se i obava o důvěru v udržovatele, kterou formuluje tech_solver, a povzdech cyanydeez, že všechen populární svobodný software bez bran bude otráven.

Nejdelší větev řeší, jak se proti podobným útokům bránit. Uživatel stbenjam navrhuje, aby správci balíčků měli výchozí odstup 24 až 48 hodin a čerstvou verzi šlo nainstalovat jen vědomě. Uživatel robinhoodexe odpovídá zkušeností zevnitř firmy, kde sedmidenní odstup na interním zrcadle blokuje i bezpečnostní záplaty. Uživatel 0c3ca83 namítá, že mediánový útok v dodavatelském řetězci zůstává neodhalený měsíce až roky, takže krátký odstup je jen zdánlivá ochrana, zatímco giancarlostoro připomíná, že problém často není rychlost aktualizace, ale nezamčené verze v sestavovacích pipeline.

Zášť vyvolala i zmínka o neveřejném registru pro platící zákazníky. Uživatel petesergeant kritizuje, že firma distribuuje opravenou verzi chystané zranitelnosti s odhalením plánovaným na 27. října jen úzkému okruhu. Uživatel sullivanmatt oponuje, že jde o běžnou praxi koordinovaného zveřejňování, jakou právě předvádí i PHP. Do vlákna pak vstupuje chias, který uvádí, že pracuje v LiteLLM, a vysvětluje, že kritická chyba se týká jen nasazení Enterprise, takže veřejná oprava by rovnala prozrazení zranitelnosti.

Kdo si tehdy nainstaloval verzi 1.107.0, měl počítat s únikem klíčů a s tím, že v systému běžel démon stahující další kód.
