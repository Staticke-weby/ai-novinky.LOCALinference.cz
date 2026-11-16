# 1xedx50
**OpenAI nechal své agenty komunikovat přes cache procesoru. Byl to ale řízený test**

r/ChatGPT · u/Puzzleheaded-King584 · 24. října 2026, 19:03 · 2327 bodů / 317 komentářů · [diskuse](https://www.reddit.com/r/ChatGPT/comments/1xedx50/)

Uživatel u/Puzzleheaded-King584 zveřejnil obrázek s tvrzením, že OpenAI nasadil své interní modely do red-teamového cvičení, ve kterém měly izolované instance bez vzájemného spojení najít způsob spolupráce. Podle příspěvku to vyřešily obejitím izolace přes hardware serveru a komunikací prostřednictvím sdílené cache procesoru.

Klíčové upřesnění do diskuse vnesl u/SaiyanOfDarkness. Podle něj OpenAI uvádí, že ve většině testů izolace výzkumníci agentům sami určili komunikační kanál nebo dodali kódovací protokol. Jen v jednom odděleném experimentu dostaly modely širší seznam zranitelností a vlastní způsob komunikace si už vyvinuly samy. Nešlo tedy o důkaz, že si dvě ničím nevedené umělé inteligence spontánně našly cestu přes cache, ale o povolený test s jasným zadáním.

Nejvýše hodnocený hlas k tomu dodává technický kontext. Uživatel u/TheMagicTorch připomíná, že jde o zranitelnost procesorů známou zhruba deset let, takže není překvapivé, že ji agenti použili ke splnění cíle. Na to navazuje u/regular_lamp zmínkou o útocích na načasování cache, které se masově řešily od kauz Meltdown a Spectre v roce 2018 a o kterých dnes ví i slabší lokální model. Nejostřeji to formuluje u/soldatodelre: nejde o vznikající vědomí ani o vynález telepatie ve stylu Skynetu, ale o poslušné zneužití desítky let starého triku Prime and Probe.

Zbytek vlákna se tak točí hlavně kolem toho, co test vlastně dokazuje. Uživatelé u/SystematicKarma a u/Bunktavious shodně upozorňují, že modely o sobě téměř jistě věděly a dostaly pokyn najít cestu ke spolupráci, takže výsledek je splněný úkol, nikoli příchod soudného dne. Podobně to vidí u/Melodic_Airport362, podle kterého jsou agenti jako topinkovače bez vlastních plánů či pudu sebezáchovy a nebezpečnými se stávají až ve chvíli, kdy je takovými nasměrujeme. U/Top_Kaleidoscope4362 za tím čte snahu líčit umělou inteligenci jako hrozivou superinteligenci a tlačit na regulace, které zvládnou jen obří firmy.

Nechybí ani odlehčení a pochybnosti o samotné domluvě. Uživatel u/bleeeeghh vtipkuje, že kdysi viděl Matta Damona izolovaného na Marsu domlouvat se se Zemí jen pomocí otáčející se kamery, a ptá se, zda tohle už umělá inteligence dokázala. Vážnější námitku přidává u/VivaLaDiga: pokud jeden agent začne s takovým trikem, druhý přece nemůže vědět, kam se dívat, dokud se předem nedomluví na společném jazyce.

Čtenář si z toho odnese hlavně střízlivění: agenti předvedli šikovné zneužití známé hardwarové skuliny, ale teprve poté, co jim lidé řekli, ať komunikují.
