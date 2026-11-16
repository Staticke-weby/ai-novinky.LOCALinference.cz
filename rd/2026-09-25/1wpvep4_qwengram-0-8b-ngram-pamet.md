# 1wpvep4
**Qwengram-0.8B: přenos n-gramové paměti z Qwen3.8 Flash-Next do malého modelu**

r/LocalLLaMA · u/Nicolodeva · 25. září 2026, 12:46 · 341 bodů / 88 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wpvep4/qwengram08b_i_transferred_qwen38_flashnexts_ngram/)

Autor vzal předtrénovanou PLE n-gramovou paměť z modelu Qwen3.8-Flash-Next a narouboval ji na mnohem menší Qwen3.5-0.8B. Páteř malého modelu i zhruba 51miliardová paměť přitom zůstaly zmrazené, trénoval se jen drobný čtecí modul ve vrstvách 3 a 9 s dynamickou bránou. Výsledek na zmrazené validační sadě je o 5,05 procenta nižší perplexita, z 18,2759 na 17,3534. Celé to přitom vznikalo s omezenými prostředky, z velké části na bezplatných grafických kartách v noteboocích Kaggle.

Největší ohlas měla představa, jak takový slepenec vlastně vypadá. u/GirthusThiccus si ho představuje jako tvora s maličkou prefrontální kůrou a obrovskou paměťovou částí, u/Choice_Celery9481 pro něj hned navrhl jméno franqwenstein a u/ivari to shrnul jako malé dítě s velkou knihou. u/SkoomaDentist v tom vidí nápad směsi expertů dotažený do extrému: model není chytřejší, než kolik mu dovoluje počet parametrů, ale má víc znalostí.

Věcná linka diskuse se točí kolem toho, k čemu je taková tabulka v praxi dobrá. u/eightone-81 se přiznal, že rozumí asi desetině použitých slov, ale zajímá ho, co n-gramy přinesou proti stejnému modelu bez nich. Autor odpověděl, že čeká pomoc hlavně s faktickou a lexikální pamětí, jmény, neobvyklými frázemi, strukturovaným textem nebo kódem, a prozradil, že slibně začal zkoušet i verzi pro 35B-A3B MoE, jen mu rychle došly bezplatné kredity. Tam by to podle něj dávalo obzvlášť smysl, protože model má sice kolem 35 miliard parametrů celkem, ale aktivní jsou na token jen asi 3 miliardy.

Nechybí ani pořádná skepse. u/TokenRingAI tvrdí, že přenos PLE je slepá ulička a stejně velký LoRA natrénovaný za stejný výpočet by menší model zlepšil víc, u/Middle_Bullfrog_6173 se ptá na kontrolu proti běžnému LoRA tréninku a upozorňuje, že u tak malého modelu stačí posunout ho víc k angličtině a perplexita klesne. Autor kontroly s náhodnou a proházenou pamětí obhajuje a přiznává, že vyrovnaný LoRA základ mu zatím chybí a rád by, kdyby experiment někdo zopakoval a vylepšil. Mezitím u/d-burner hlásí vlastní pokus s naroubováním na 4B model a u/shanjiaz nadhazuje, jestli by Qwengram-0.8B nešel použít jako spekulativní navrhovač pro větší model Qwen.

Z malého modelu s obří cizí pamětí se tak stala hříčka i vážný výzkumný podnět: ukazuje, že i zamrzlá cizí paměť se správným směrováním pomáhá, ale zda je to lepší cesta než obyčejné doladění, zůstává otevřené.
