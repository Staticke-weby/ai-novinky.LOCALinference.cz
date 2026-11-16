# 1x9smgq
**Claude Code našel na Macu skrytý miner xmrig**

r/ClaudeAI · u/UntilHEX · 19. října 2026, 11:50 · 731 bodů / 61 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1x9smgq/)

Uživatel si nechal od Claude Code postavit aplikaci na sledování teploty na Macu. Když agent vypsal surové hodnoty ze senzorů, aby ověřil jejich přesnost, přišly mu podezřele vysoké, a tak se podíval, co vlastně vytěžuje procesor. Narazil na těžař xmrig, který jel zhruba na 1175 % CPU, tedy asi na dvanácti jádrech. Autor to vzal s humorem jako nečekaný bonus a konečně měl vysvětlení, proč mu Mac dlouhodobě šlapal mizerně.

Nejvíc hlasů ale nesbírá samotný nález, nýbrž rýpání do autora. u/YogurtclosetLimp7351 se ptá, jak často to chce ještě postovat, a u/danielsuperone přisazuje, že úplně stejný příspěvek prý viděl už včera. Vedle toho se vlákno chytlo formulace ze screenshotu, že miner tam agent „nedal“. u/Tarc_Axiiomovi to přijde hodně vtipné a přirovnává to k technikovi na podpoře, který zákazníkovi pro jistotu hned hlásí, že virus do počítače nenainstaloval on. u/KugelVanHamster dodává, jak milé od agenta, že těžař na Mac nedal, a u/Lonely-Breath8930 v tom vidí předvídavost: agent už tuší, že ho vývojáři okamžitě obviní ze 112stupňového procesoru, a tak si předem připravil logy a důkazy o své nevině.

Věcná část diskuse naopak chválí způsob, jakým k odhalení došlo. u/vladgladi to označuje za pěkný příklad toho, proč se vyplatí nechat agenta zkontrolovat vlastní výstup proti realitě: miner nenašel proto, že by ho hledal, ale proto, že naměřené hodnoty nedávaly smysl a šel o krok dál místo toho, aby jen odevzdal aplikaci. Podobně to vidí u/InevitableFun1272, podle kterého je právě porovnání pozorovaného chování s očekáváním lepší vzor detekce než signatury – tichý nezvaný proces se prý jinak odhaluje jen těžko.

Třetí proud vlákna řeší, co s tím a proč si toho autor nevšiml dřív. u/vladgladi radí podívat se, jak se věc do počítače vůbec dostala, projít agenty po spuštění, položky po přihlášení a věci nedávno instalované mimo App Store, protože smazat samotný soubor většinou nestačí. u/skittlesandcoke a u/DominikPlays doporučují zálohovat data a udělat čistou instalaci celého systému, u/esanDev přidává otočení hesel a klíčů, protože xmrig prý zřídka chodí sám. A ozývá se i zdravé rýpnutí do autora: u/dthrdr viní „masového prostředníka“, kterého při pomalém a horkém stroji nenapadlo otevřít sledování vytížení, a u/h4ck3r_n4m3 se ptá naprosto stejně.

Poučení vlákna je tak dvojí: kontrola nesmyslných čísel umí najít i to, co žádný sken nehledal, ale napadený stroj si stejně nakonec řekne o důkladný úklid.
