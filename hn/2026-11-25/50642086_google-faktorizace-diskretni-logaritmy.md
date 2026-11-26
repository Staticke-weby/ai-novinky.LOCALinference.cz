# 50642086
**Google zveřejnil důkazy o faktorizaci a diskrétních logaritmech**

Hacker News · rgwohlbold · 25. listopadu 2026, 14:33 · 475 bodů / 342 komentářů · [diskuse](https://news.ycombinator.com/item?id=50642086)

Google Research 25. listopadu 2026 zveřejnil sadu matematických prací vzniklých v systému Cogentic. Dva z nich slibují bezpodmínečnou faktorizaci celých čísel v čase L_N[1/3, O(1)] a diskrétní logaritmy v konečných tělesech pevné charakteristiky v sub-kvazipolynomiálním čase. Nejde o tvrzení o P = NP, pro praxi kolem RSA a ECDSA je to zatím spíš teoretický posun než praktický zlom.

Odkazovaný adresář na GitHubu popisuje Cogentic jako zdroj těchto prací a odkazuje na práci Cogentic: Multi-Agent Orchestration for Automated Proof Discovery. Uvádí hned šest nových textů od faktorizace přes Nashovy rovnováhy až po log-rank domněnku a rekonstrukci grafů, starší přírůstky jsou z 23. a 18. listopadu a z 30. října. Obsah je zveřejněn pod licencí Apache 2.0 s dovětkem, že nejde o oficiální produkt Googlu.

Nejživější část diskuse se hned stočila k tomu, co Cogentic vlastně je. david-gpu ho popisuje jako svazek pro spolupráci existujících modelů na matematických domněnkách s centrálním orchestrátorem a sdílenou databází mezikroků důkazů, v tomto případě s během na Gemini 4 Argon. schleck8 k tomu doplnil kontext odkazem na srpnový preprint o multiagentní orchestraci pro automatické objevování důkazů a wood_spirit předpovídá přesun od vyhledávání ke kódovým serverům, které budou zároveň kanálem mezi subagenty.

Druhá linka řeší, jestli se díky tomu bude na klasických počítačích faktorizovat ve velkém. roomey se ptá, zda přijde faktorizace velkých čísel bez kvantových počítačů a zda proti tomu pomohou postkvantové algoritmy. vlovich123 odpovídá dost střízlivě: pro 4096bitový klíč RSA by klasické GNFS potřebovalo asi 10^47 operací, zatímco nový postup asi 10^2572, jediným zlepšením je garance pro libovolná čísla. Pro běžné velikosti klíčů RSA tak podle něj průlom nečeká a u kryptografie na eliptických křivkách se faktorizace vůbec nehraje, postkvantové konstrukce pak staví na jiných matematických základech.

Do toho se mísí obavy doktorandů i kariérní debata. edumucelli píše, že studenti matematiky a teorie informatiky nevědí, zda se jejich téze nestane příští trofejní prací OpenAI, Anthropicu, a nyní Googlu. brandonpelfrey namítá, že doktorát může být právě o tom, jak modely a agenty chytře využívat k prozkoumávání nápadů, a jvanderbot dodává, že jeho zčásti aplikovaná práce s robotem a důkazy správnosti by dnes byla s jazykovou pomocí spíš snazší. Paralelně se na Hacker News řešily i fámy, že některá z laboratoří umí faktorizaci v polynomiálním čase, o „bombshells“ prý z více zdrojů slyšel i Scott Aaronson.

Zůstává tak obraz průmyslové revoluce v matematice: stroje chrlí důkazy, lidé řeší, co s nimi. Pro čtenáře je podstatné rozlišit bezpodmínečné, ale stále těžké algoritmy Googlu od spekulací o polynomiální faktorizaci, které by teprve otřásly světem šifrování.
