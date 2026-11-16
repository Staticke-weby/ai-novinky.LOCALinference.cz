# 50503241
**Kolik stojí jeden úkol na Opus 5.5: rozbor nákladů agentního kódování**

Hacker News · gmays · 15. listopadu 2026, 02:57 · 24 bodů / 23 komentářů · [diskuse](https://news.ycombinator.com/item?id=50503241)

Addy Osmani v novém rozboru ukazuje, kolik v praxi stojí jednotlivé úlohy na modelu Opus 5.5 v Claude Code. Model má nižší cenu za token než předchozí Opus 5 a podle ilustrativních propočtů vychází typická agentní práce zhruba o třetinu levněji už jen díky samotné změně ceníku. Text má čtenáři odpovědět na tři otázky: co stojí jeho běžný úkol, která nastavení cenu mění a jak si vlastní spotřebu zkontrolovat.

Odkazovaný článek vysvětluje, že úkol v Claude Code je smyčka, ve které model čte konverzaci, volá nástroj a jde znovu dokola. Cenu pak určují čtyři věci: počet otoček, podíl čtení z cache, množství výstupních tokenů včetně přemýšlení a volba modelu. Uvádí ceníkové ceny 4 dolary za milion vstupních tokenů, 20 dolarů za milion výstupních a 0,20 dolaru za milion čtení z cache a přidává interaktivní kalkulačku i rady, kdy stačí prostřední úsilí a kdy už dává smysl přejít na větší model.

Místo počítání se ale diskuse stočila hlavně ke stylu textu. Taylorfinley si rýpl, že je zklamáním číst strojový balast od firmy, která si může dovolit lidské autory, a simianwords píše o typických znacích umělé inteligence a o nuceně úderné vznešenosti úvodu. Přidal se hxugufjfjf s tím, že ho z takového jazyka až fyzicky bolí oči, a cajal vtipkuje, jestli lidé v Anthropicu po neustálém klódování sami nezačali mluvit jako model. Replwoacause pak ironicky dodává, jestli se dočkáme superinteligence dřív, než se modely naučí psát lidsky.

Proti tomu se ozval mycall s otázkou, zda má někdo chuť řešit i samotný obsah o cenách Opusu 5.5. Odpověděl mu x-complexity, podle kterého má smysl hlavně přiložená kalkulačka, zatímco zbytek shrnuje známé rady z videí: maximalizovat čtení z cache, držet se prostředního a vyššího úsilí a pravidelně komprimovat kontext před hranicí 200 tisíc tokenů. IshKebab k tomu suše podotýká, že modely OpenAI a Googlu píší lépe, a to i než Opus 5.5.

Třetí linka řeší, jak náklady ovlivňují používání agentů při vývoji. Hodgesrm píše, že mu přijde článek poučný, ale nerozumí, jak má být Anthropic ekonomicky udržitelný při nepředvídatelných a potenciálně neomezených nákladech pro firmy, a proto prý běží na modelech Quen. Qazxcvbnmlp kontruje, že počkejte, až se dozví, jak nepředvídatelné a neomezené náklady mají lidští zaměstnanci. Z praktických dotazů zaujala otázka KellyCriterion, kde má uživatel webu vidět, kolik tokenů už probíhající konverzace spálila, a dotaz, zda se dá Opus 5.5 používat zdarma, na který IshKebab odpovídá, že je dostupný i v nejlevnějším předplatném.

Kdo si z vlákna odnese jedno ponaučení, je to prosté: nejlevnější otočka agenta je ta, která vůbec nemusela proběhnout.
