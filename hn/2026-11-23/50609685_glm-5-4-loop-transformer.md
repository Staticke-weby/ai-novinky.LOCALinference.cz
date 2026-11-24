# 50609685
**GLM-5.4: Loop Transformer slibuje levnější kód, váhy přijdou později**

Hacker News · foohis · 23. listopadu 2026, 11:06 · 1094 bodů / 357 komentářů · [diskuse](https://news.ycombinator.com/item?id=50609685)

Z.ai vydalo model GLM-5.4 postavený jako první veřejný loop transformer. Místo přidávání parametrů opakuje výpočet nad skrytými stavy, čímž zvyšuje efektivní hloubku sítě, a cílí hlavně na programování a agentní úlohy.

Oznámení zároveň zvedá limity předplatného GLM Coding Plan, váhy slibuje otevřít až po dodatečném bezpečnostním ořezu a veřejná srovnávací čísla v něm diskutující nenašli. Přiznává i jednu slabinu nové architektury: sklon k příliš dlouhému uvažování, kterému říká „marathon thinking“.

Právě chybějící benchmarky rozjely největší vlákno. Uživatel saretup se ptá, jak se má bez čísel poznat, jak dobrý model je, a hádá, že kdyby byla působivá, firma by je ukázala. Uživatel lesspassiveobse namítá, že důraz mohl být na cenu inference, když se zároveň zvedly limity předplatného, zatímco Systemerror7A69 píše, že benchmarky se staly marketingovým nástrojem a jemu stačí, když bude novinka lepší než jeho oblíbená GLM-5.3. V podobném duchu A_D_E_P_T chválí, že firma „nebenchmaxxuje“, a throwa356262 vtipkuje, že tím ušetřili zaměstnance Artificial Analysis, kteří by jinak museli o Díkůvzdání chystat Intelligence Index v6.

Druhá teorie kolem chybějících čísel míří k bezpečnosti. ImprobableTruth spekuluje, že kybernetický bezpečnostní ořez později skóre sníží a firma nechce, aby byl pokles vyčíslitelný, segmondy to říká natvrdo: benchmarky nemohou zveřejnit, protože po osekání útočných kybernetických schopností dopadnou hůř. Segmondy dodává, že čínská vláda to po laborkách vyžaduje a Kimi K3.1 i další model Hy4 už své poslední verze v útočném hackingu záměrně oslabily. Do stejného sporu zapadá i otázka, zda čínští poskytovatelé otevřených vah modely vůbec slaďují s nějakými pravidly, na což sorrywhat odpovídá, že modely GLM překvapivě často mluví o zásadách a hodnotách Anthropicu.

Třetí linka vysvětluje, co looping vlastně je. Uživatel dingaling911 se ptá, proč architekturu zacyklovat jen dvakrát a proč to nenechat na okolním harnessu, a jak se pak model může zaseknout v maratonovém přemýšlení. Ytxm odpovídá, že smyčka nad maticemi skrytých stavů je něco úplně jiného než smyčka nad jednotlivými tokeny, nialv7 dodává, že jde o levný způsob, jak prohloubit síť bez nových parametrů, a samrus to shrnuje slovy, že je to v podstatě návrat k rekurentním sítím. Navazuje debata o nebezpečnosti: postalcoder se diví, proč by smyčky měly být skluzavkou k neinterpretovatelnosti, nialv7 považuje strach za nesmyslný, protože jazykové modely jsou nebezpečné tak jako tak, a zozbot234 argumentuje, že zacyklený model odpovídá jen několikanásobně většímu modelu se sdílenými parametry, který má naopak méně znalostí reálného světa.

Z diskuse tak zůstává model, který je architektonicky zajímavý, prakticky levnější na kódování, ale zatím nezměřený a vědomě ořezaný dřív, než se jeho váhy dostanou ven.
