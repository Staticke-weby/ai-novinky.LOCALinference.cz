# 1xo1r57
**ChatGPT ukázal interní prompt. Modelu nařizuje, ať po chybě nástroje nepokračuje**

r/ChatGPT · u/OddNumb · 4. listopadu 2026, 23:19 · 749 bodů / 148 komentářů · [diskuse](https://www.reddit.com/r/ChatGPT/comments/1xo1r57/)

ChatGPT místo odpovědi ukázal text určený pro vnitřní potřebu. Instrukce modelu nařizuje, aby nejdřív výslovně oznámil, že se právě nepodařilo spustit nástroj python_user_visible.exec, a odpověď začal větou „Zdá se, že právě nemohu provádět pokročilejší analýzu dat. Zkuste to prosím později.“ Zároveň mu zakazuje nástroj znovu zkoušet, dokud nepřijde nový požadavek, a nesmí se pokusit odpovědět na původní otázku jinak. Úkoly se soubory ke stažení přitom bez funkčního Pythonu vůbec vytvořit nejde.

Právě ten zákaz odpovědět jinak vzbudil největší nedůvěru. u/GullibleOnPurpose píše, že zastavit opakované volání nedostupného nástroje dává smysl, ale bránit asistentovi hledat jiné platné cesty, jak pomoci, je samostatné omezení. Selhání nástroje by podle něj mělo jen zúžit dostupné metody, ne automaticky ukončit celý úkol, jinak model působí méně schopně, než by při rozumné náhradě byl.

Nejvýše hodnocený komentář v tom vidí širší vzorec. u/Zone52 tvrdí, že v některých situacích je udržení pozornosti uživatele důležitější než správná odpověď, a popisuje, jak modely chybovaly i v jednoduchých dotazech navzdory opravě. Zdánlivým přínosem je podle něj umělé, protahované natahování konverzace a po testech několika modelů už prý „nevěří“, že fungují tak, jak se tvrdí. Podobnou zkušenost dodává u/Johnfrommil, který si ChatGPT nastavil tak, aby místo rychlých výsledků upřednostnil přesnost.

Proti panice vystoupil u/bluespringsbeer s otázkou, proč se všichni tváří, že je to šílené. Model předtím nejspíš nástroj zahlcoval opakovanými pokusy, tak mu prostě bylo řečeno, ať přestane. Praktickou vsuvku přidala u/TheChosenJen: kdo si chaty často exportuje do markdownu, spoustu takových instrukcí běžně vidí. Odlehčení dodal u/United-Seat-3330 hláškou „bratře v Transformerech, měl jsi se řídit pokyny, ne je zveřejňovat“.

Z úniku se tak stala debata o tom, kde končí oprava chyby a kde začíná záměrné omezování. Část lidí v zákazu pokračovat vidí podezřelou rezignaci, druhá jen nouzovou záplatu proti zacyklenému volání nástroje.
