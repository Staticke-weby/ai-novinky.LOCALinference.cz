# 1wq56pf
**Swift1.5-Qwen3.8-Flash-Next výrazně snižuje nadbytečné uvažování**

r/LocalLLaMA · u/returnity · 25. září 2026, 19:16 · 197 bodů / 91 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wq56pf/swift15qwen38flashnext_is_phenomenal_vs_base/)

Autor u/returnity, dlouhodobý fanoušek modelů Swift Qwen3.8, otestoval novinku Swift1.5-Qwen3.8-Flash-Next od autora ukisai na Hugging Face proti základnímu Qwen3.8-Flash-Next. Vlastní agentický benchmark v Aideru mu vyšel téměř nastejno v kvalitě, ale Swift spotřeboval typicky jen kolem 40 % tokenů a dokončil úlohy ve 40 % času. Nejvíc tokenů na jeden případ použil Swift 44 tisíc, zatímco základ 203 tisíc, a na dvaceti nejnáročnějších bězích základu vyřešil 16 případů ze 20 oproti 17 u základu při 29 % tokenů.

Diskuse novinku vítá hlavně jako důkaz rychlosti komunity. u/jacek2023 poznamenal, že je příjemné vidět finetuny Qwen Flash Next tak brzy, a u/akohlsmith přidal, že i větší Swift 1.5 Qwen 3.8 27B je opravdu dobrý a přemýšlí mnohem méně než původní 3.8. Praktické hlasy ale krotí nadšení: u/Dany0 se po krátkých testech vrátil k původnímu modelu, protože výstupy Swiftu mu přišly výrazně horší, a u/TaiMaiShu-71 hlásí při vlastním srovnávacím benchmarku kódu pokles skóre o 16 bodů.

Nejzajímavější spor se vede o to, zda se úspora vyplatí. u/Elouakili_Flexy napsal, že ztratit jeden případ ze dvaceti výměnou za úsporu 71 % tokenů by bral pokaždé, zatímco u/Top-Evidence174 se ptá, jestli Swift chybuje jinak — zda se rozhodne špatně dřív, nebo jen vzdá úlohy, které základ nakonec „upřemýšlí“ dalšími sto tisíci tokeny. u/dasbin zase řeší, jaký je praktický rozdíl proti pouhému limitu tokenů na uvažování nebo přepnutí na Medium místo XHigh, když finetune musí obhájit i ztrátu vyladěného prostředí kolem modelu Halogen.

Zbytek vlákna řeší detaily kolem kvantizací, licencí a slabších míst. u/AdIllustrious436 se ptá, proč Swift vždycky odnáší znalost Pythonu, autor odpovídá, že vzorek je malý, ale trend je vidět už u druhého modelu Swift. u/silenceimpaired lituje, že to stále není Apache 2 nebo MIT, na což autor namítá, že podmínky bezplatného užití do milionového obratu se dají snést. U kvantizací u/jacek2023 nechápe kouzlo souborů od Unslothu a odkazuje na GGUF přímo od ukisai, u/fgk55555 doplňuje novější GSQ-RCO varianty a u/Wooden_Jelly_5295 připomíná, že smysluplnou metrikou je čas na vyřešenou úlohu, protože tokeny za sekundu odměňují i rychlé tlachání.

Pro běžného uživatele z toho plyne jednoduché ponaučení: pokud model tráví víc času přemýšlením než prací, stojí Swift za zkoušku, jen je dobré si pohlídat Python a C++.
