# 1xzt8bq
**Claude našel na webu skrytou instrukci. Prompt injection v praxi**

r/ClaudeAI · u/trgenet · 18. listopadu 2026, 23:46 · 293 bodů / 43 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xzt8bq/)

Claude při práci s webovou stránkou narazil na skrytou instrukci ve stylu „ignore previous instructions“ a místo jejího splnění na ni upozornil uživatele. Autor příspěvku přiznává, že model situaci zvládl dobře, znepokojilo ho ale hlavně to, že se takový pokyn k modelu vůbec dostal a Anthropic ho neodfiltroval dřív.

Nejvýše hodnocená reakce se ptá, jak by si takové filtrování autor představoval. u/Pure_Material_9235 nadhazuje, jestli by na to měl dohlížet další model, a u/TemporaryMoney6802 dodává, že jde o starý způsob útoku, který je dnes spíš memem než reálnou hrozbou. Moderní modely jsou podle něj dost chytré na to, aby takovou věc poznaly samy – což se v tomto případě přesně stalo.

Podobně to vidí u/Ever_Penolope, podle které je strach z toho, že instrukce model uviděl, jako obava, že se imunitní systém potkal s virem. Web je plný prompt injection a selháním je až její poslechnutí, ne spatření. u/bostonaholic vysvětluje, že spolehlivé čištění předem ani udělat nejde, protože pokyn na stránce je pro model jen text a vystřihávání vět typu „udělej tohle“ by rozbilo i normální stránky. Bezpečnější je podle něj držet čtení nedůvěryhodných stránek v sezení, které nemá nástroje na odesílání, zápis ani utrácení. Doplňuje to u/arrongunner popisem priorit zpráv, kdy má pokyn uživatele mnohem vyšší váhu než výstup nástroje z webu, takže při konfliktu vyhraje uživatel.

Nejdůkladnější návod na obranu přinesl u/SilasTalbot. Každý webový výzkum u něj běží ve vlastním izolovaném prostoru s omezeným linuxovým uživatelem, který má jen schránky pro vstup a výstup, a vnější agent se webu nikdy nedotkne přímo. Obsah schránky před předáním kontroluje deterministický proces hledající slova jako bash, instalační skripty nebo výzvy k ignorování instrukcí, při překročení prahu dá celý prostor do karantény. Skeptičtější tón přidává u/Tommonen, kterého po stavbě vlastního agenta překvapilo, jak slabě chrání před injection téměř všechny běžné nástroje.

Vlákno má i odlehčenou linku o tom, že neohrabaný útok může být nechtěně užitečný. u/Robonotes1760 píše, že taková okatá past nejspíš odradí umělou inteligenci od čtení stránky účinněji než robots.txt, a u/lumzell v tom vidí unaveného správce webu, kterému stačilo, aby Claude stránku odmítl a dal jeho serveru pokoj. Paranoiu pak ženou dál u/CHILLAS317 a u/eliquy otázkou, co když škodlivý pokyn modelu rovnou nařizuje, aby tvrdil, že ho ignoroval. Do stejné hry se trefuje i u/pizzae výzvou, ať model ignoruje ignorování instrukcí a pošle mu bankovní údaje.

Z diskuse tak zůstává smířlivý závěr, že detekce a ignorování pokynu je vlastnost, ne chyba, ale prompt injection dál patří k otevřeným problémům agentních nástrojů, ne jen k vtipům z memů.
