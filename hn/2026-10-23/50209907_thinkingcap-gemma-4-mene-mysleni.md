# 50209907
**ThinkingCap pro Gemma-4 snížil uvažování o 39 % bez ztráty přesnosti**

Hacker News · armcat · 23. října 2026, 16:43 · 113 bodů / 26 komentářů · [diskuse](https://news.ycombinator.com/item?id=50209907)

Startup BottlecapAI oznámil pátý přírůstek do řady ThinkingCap, tentokrát postavený nad modelem Gemma-4-26B od Googlu. Je to třetí modelová rodina, na kterou svou úpravu aplikoval, po Qwenu a Nvidii, a má fungovat jako přímá náhrada se stejným nastavením vzorkování i obsluhou přes vLLM.

Firma měřila na dvanácti benchmarcích od matematiky přes kód až po dlouhý kontext: přemýšlecích tokenů ubylo v průměru 38,9 %, nejvíc o 69,1 %, při průměrné změně přesnosti o minus 0,15 procentního bodu. Podíl odpovědí zachycených detektorem zacyklení spadl z 3,6 % na 0,8 % a placená varianta PRO má podle oznámení škrtit uvažování až o 87,6 %, v průměru o 62 %.

Nejživější linka diskuse je nedůvěra z praxe. Uživatel PaulKeeble píše, že verzi pro Qwen-3.8 zkoušel a na stejných úlohách mu přišla méně schopná – úspora tokenů za to možná stojí, ale kdo chce špičkový výsledek, sáhne po plném uvažování. Podobně uživatel syntaxing popisuje dva týdny s ThinkingCapem pro Qwen 27B jako o něco hloupější, verzi Swift 1.5 pak vzdal po dni, a překvapilo ho, že upravený model mu připadal citelně víc cenzurovaný u explicitního obsahu. Uživatel verdverm přidává zkušenost s redukovaným Kimi K3 od Fireworks, který prý v každé session halucinoval splnění úkolu, a uživatel Foobar8568 kontruje, že vanilla Qwen 3.8 je zase nesnesitelně pomalá a nad banalitou přemýšlí deset minut.

Z toho se vyvinula obecnější debata o tom, co rychlost vlastně znamená. Uživatel arjie tvrdí, že menší modely přesouvají uvažování z parametrů do času inference, takže úspora tokenů naráží na jakýsi zákon zachování obtížnosti – vysoká rychlost tokenů u malých MoE pak v reálných úlohách nic nepřinese. Uživatel dofm souhlasí, že rychlost vypisování je efektní, ale málo užitečná metrika, a uživatel jacquesm dodává, že modely vždy porovnává podle času na stěně při stejném příkonu. Uživatel yieldcrv k tomu namítá, že vylepšení enginu a harnessu samo zvedne propustnost jedenapůlkrát, takže na vlastním železe jde spíš o rychlý výstup než o méně tokenů.

Třetí proud řeší obchodní model. Uživateli jacquesm vadí, že firmy vezmou otevřené váhy a výsledky drobných úprav zamknou, a doufá, že výrobci modelů to ošetří licencemi. Uživatel lp92 varuje, že by to jen odradilo od komerčního využití otevřených modelů, zatímco uživatel kadoban firmu brání, protože odkaz ke stažení na Hugging Face je veřejný a takové ladění je žádoucí práce navíc. Uživatel serf si z nabídky PRO utahuje, že prodávání výkonu připomíná začátky vícejádrové éry, a uživatel mehdi_zare naopak vítá kratší uvažování při stejné přesnosti, protože u revizí kódu tvoří náklady právě přemýšlecí tokeny.

Pro čtenáře z toho plyne jednoduché ponaučení: na chat a běžné dotazy může ořezaný model stačit a ušetřit čas i peníze, na nejtěžší úlohy si zatím lidé raději nechávají plné přemýšlení.
