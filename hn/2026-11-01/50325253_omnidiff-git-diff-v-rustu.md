# 50325253
**OmniDiff: obsahově citlivý git diff v Rustu**

Hacker News · FabCH · 1. listopadu 2026, 14:02 · 196 bodů / 46 komentářů · [diskuse](https://news.ycombinator.com/item?id=50325253)

OmniDiff je open-source nástroj v Rustu pod licencí AGPLv3, který umí obsahově citlivě porovnávat kód ve 25 jazycích i konfigurace, obrázky, PDF, archivy, kurzory a fonty. Autor ho postavil na ručním rozboru dvou tisíc reálných diffů ze 7 400 repozitářů evidovaných v balíčcích Gentoo a slibuje, že i C++ soubory o desítkách tisíc řádků zvládne pod 100 ms. Projekt je ve verzi 0.3.0 a autor ho měsíce používá jako každodenní git difftool.

Stránka projektu slibuje rychlost, robustnost a přesnost: medián diffu 4,2 ms, zvládnutí 99,95 % změn kódu a obsahově specifické algoritmy pro naprostou většinu změn. Nabízí interaktivní terminálové rozhraní, dávkový i JSON výstup a napojení na git přes difftool i GIT_EXTERNAL_DIFF či na Jujutsu, instalaci přes cargo, hotové binárky, Homebrew, Debian i Nix. Autor otevřeně přiznává výraznou pomoc Claude Code, ale odmítá, že by šlo o bezmyšlenkovité vibe coding.

Nejživější je srovnávání se zaběhnutými nástroji. paaloeye se ptá, v čem je nástroj lepší než Delta, a FabCH vysvětluje, že Delta jen obarvuje standardní git diff, zatímco OmniDiff používá úplně jiný stromový algoritmus a výrazně lépe zvládá přesunutý kód. Podobně na dotaz cocoto srovnává s Difftastic: ten umí jen kód, tedy asi dvě třetiny všech diffů, a v testech je perfektní v 64 % případů proti 90 % u OmniDiff, v mediánu rychlosti 35 ms proti 4 ms. arkenflame chválí mnohem úspornější diffy, jen mu chybí zobrazení vedle sebe, na což FabCH odpovídá, že široký režim se zapíná od 200 sloupců a vynutit jde klávesou v.

Do debaty o licenci vnáší anilgulecha varování, že model AGPL plus dary projekt v zárodku zabije a standard se prosadí spíš pod BSD licencí. FabCH oponuje, že copyleft je vědomá politická volba, na komerční licenci mu nezáleží a klidně přežije, když jeho nápad někdo převezme. IshKebab dodává, že Difftastic a Diffsitter pod MIT už tu dávno jsou, a tak se nic takového nestalo, zatímco enriquto právě svobodu pod AGPL vítá.

Z praktických otázek zaujala nabídka davvid, autora původního git difftool, aby se nastavení dostalo přímo do gitu, i zvědavost na trojcestné diffy pro merge. FabCH slibuje, že se ozve kvůli upstreamu, ale trojcestné slučování je podle něj nejtěžší dlouhodobý cíl, protože použitý algoritmus APTED pro něj přirozeně nic nenabízí. gslepak řeší použití bez zásahu do globální konfigurace a dostává tip na GIT_EXTERNAL_DIFF=omnidiff git diff, zatímco nh2 upozorňuje, že roura z git diff nástroji bere informace, které ke své práci potřebuje. Skepsi přináší burner-account, kterému ukázky nepřijdou lepší než klasika, a blahgeek, kterého děsí, co se stane s oněmi 0,05 % změn, které nástroj nezvládne.

Kdo trpí na nepřehledné přesuny funkcí a binární balast v diffu, ten má po této diskusi o důvod víc OmniDiff vyzkoušet.
