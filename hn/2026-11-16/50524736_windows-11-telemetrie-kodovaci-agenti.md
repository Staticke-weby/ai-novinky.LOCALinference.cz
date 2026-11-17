# 50524736
**Windows 11 sleduje, které kódovací agenty a vývojářské nástroje používáte**

Hacker News · cwaffles · 16. listopadu 2026, 23:58 · 428 bodů / 273 komentářů · [diskuse](https://news.ycombinator.com/item?id=50524736)

Windows 11 potichu eviduje, zda uživatel spustil kódovací agenty jako Codex, Claude, Copilot či Cursor, i běžné vývojářské nástroje od Pythonu přes .NET a GCC až po VS Code. Jejich jména jsou natvrdo zapsaná v knihovně MissionControlAggregator.dll, která použití zaznamená do bitové mapy, uloží na disk a předá do Windows Diagnostics. Má-li uživatel zapnutá volitelná diagnostická data, což je výchozí stav, míří přehled do Microsoftu.

Autor nález popsal na svém blogu jako výsledek reverzního inženýrství, při kterém si procházení binárek nechal pomáhat AI agentem. Komponenta má čtyři sloty pro terminálové agenty a pět pro desktopové, u některých nástrojů kontroluje i vydavatele, a výsledek posílá jako událost Segments.SubCohorts přes ETW. Funkčnost ověřil pokusem, kdy přejmenoval cmd.exe na codex.exe a v hlášení se rozsvítil právě bit Codexu, podobně přejmenování na gcc.exe zapnulo kategorii překladačů a debuggerů.

V diskusi se hodně ozývá únava, že jde jen o další potvrzení známého. Zatímco TacticalCoder se ptá, zda se Microsoft chová neeticky, j3th9n kontruje, že tohle se dalo dávno čekat, a onemoresoop dodává, že Windows 11 sbírá zdaleka víc a posílá to domů. Elseself to žene do vtipu, že Microsoft už asi sbírá i barvu ranní moči, nelsonfigueroa přiznává, že hláška o Windows jako spywaru už mu nepřijde přehnaná, a joshAg lituje, že operační systémy se od vrcholu kolem roku 2009 jen zhoršují.

Do debaty vstoupil i pseudosavant s otázkou, proč stejné pobouření neprovází Android, iOS, ChromeOS a Mac, když komerční systémy sledují spouštěné aplikace vesměs všechny a Google navíc data propojuje napříč e-maily, prohlížením a dalšími službami. Mnozí to berou jako argument, že výjimkou nejsou špehující Windows, ale naopak linuxové distribuce, které to nedělají. Skeptičtější hlas má lesspassiveobse, podle kterého vzniknou takto velmi zkreslená data, protože popisují jen uživatele Windows s nevypnutou telemetrií, na což speed_spread odpovídá, že jde o předfiltrování trhu podle toho, kdo si telemetrii neumí vypnout.

Třetí proud diskuse se tak logicky stočil k útěku na Linux. cheschire prostě poslal návod na instalaci Mintu, PcChip místo něj doporučuje CachyOS kvůli novějším ovladačům a kernelu i snadným snapshotům a Kodiack varuje, že Mint s pouhým X11 neumí třeba HDR. fuzzfactor popisuje bezproblémový dual boot vedle Windows 11 na jedné linuxové partition a odbočka u knollimara končí u přání, aby na Linuxu fungoval anticheat a produkty Autodesku, což jiní rovnou otáčejí v obavu, že s podepsanými kernely by si Linux přivezl stejné neduhy jako Windows.

Kdo nechce, aby Microsoft věděl o jeho agentech, musí během instalace nebo později v nastavení odmítnout volitelná diagnostická data.
