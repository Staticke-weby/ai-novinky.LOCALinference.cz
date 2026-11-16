# 1xst2qe
**Claude Code dostal živou mapu. Mod ukazuje cestu agenta**

r/ClaudeAI · u/alexeyw · 10. listopadu 2026, 18:31 · 770 bodů / 64 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xst2qe/)

Už ho nebavilo louskat nekonečný seznam volání nástrojů, tak si nechal od Claude Code postavit mod, který práci agenta kreslí jako živou mapu v panelu vedle chatu. Agent sedí uprostřed a kolem něj je deset stanic – uživatel, model, paměť, soubory, shell, síť, prohlížeč, subagenti, dovednosti a hooky. Každý požadavek na model, volání nástroje i hook vyšle pulz ze středu ke stanici a zpět, chyby zčervenají, často používané paprsky tloustnou a prstenec kolem středu ukazuje zaplnění kontextového okna. První verzi napsalo Opus 5.5, druhý den ji přepracovalo Fable 5.2, mod je zdarma pod licencí MIT a neposílá žádné síťové požadavky, zobrazuje jen názvy, nikdy obsah.

Největší ohlas má právě ta přehlednost na první pohled. u/Budget-Kelsier píše, že sledovat Claudea pouhým čtením je těžké a musí ručně rozklikávat každou krabičku, zatímco mapa hned ukáže, jestli sahá po agentech nebo internetu. Podobně to vidí u/twinsBuild, podle kterého živá mapa poráží scrollování v logech ve chvíli, kdy člověk zjišťuje, kam se agent zatoulal, a rovnou se ptá, jestli mapa ukáže i dotčené soubory. Pro u/emmat470 je záchranou prstenec kontextu, protože plnost kontextu prý pozná až ve chvíli, kdy Claude začne zapomínat.

Do debaty se rychle dostala i podoba mapy. u/MrLMNOP by si představoval uživatele dole a síť či prohlížeč nahoře, protože on sedí přímo před Claudem a internet je „tam venku“. Kritičtější linku otevřel u/jerkosaur otázkou, jestli mod jen parsuje příkazy a mapuje je na stav a jak je připravený na budoucnost, když model přidá nové stavy. Textový výpis je podle něj pořád jasnější v tom, co úkol skutečně dělá, a duální zobrazení mu přijde zbytečné. Odpověď mu v balíčku nezazněla, zato u/suremise nápad chválí a přemýšlí, jak podobný lesk dodat vlastnímu panelu aktivit s běžícími procesy a úlohami na pozadí.

Nejvtipnější hlášku utrousil u/FireTech88 nad dokumentací: copak je tohle rozumné readme. Praktická část vlákna pak řeší kompatibilitu, autor totiž mod testoval jen na macOS. u/HighSeasArchivist hlásí, že na Windows naskočil perfektně i ve starších sezeních a fungoval bez jediného zásahu, zatímco u/BazookaLucca na Linuxu na Steamu vidí jen spodní část jednotlivých fází, ale ne samotnou vizualizaci.

Z diskuse tak vychází jednoduché ponaučení: místo rozklikávání desítek volání stačí jeden pohled na mapu, kde agent právě je a kolik paměti mu ještě zbývá.
