# 1x41myz
**QwenGyre: RL framework pro extrémně dlouhé agentní úlohy**

r/LocalLLaMA · u/ResearchCrafty1804 · 12. října 2026, 15:18 · 437 bodů / 40 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x41myz/)

Autor představil QwenGyre jako elastický RL framework pro trénink agentů s extrémně dlouhým horizontem a přidal odkaz na paper na arxiv.org. Jeho prvním pilířem je elastický plánovač, který za běhu přesouvá GPU mezi rollouts a tréninkem bez přerušení živých běhů a slibuje až 1,85násobné zrychlení proti Colocate a 1,78násobné proti Async. Druhým je procesor trajektorií, který větvící se běhy s kompaktováním, sub-agenty a retry mění na stromy se sdílenými prefixy s omezenými deduplikovanými vzorky, přičemž i částečný pokrok po timeoutu se dál boduje. Ve velkém měřítku na modelu Qwen3.8-2.4T-A95B s rollouts kolem 700 tisíc tokenů zvedl NL2RepoBench z 52,5 % na 58,5 % za 48 kroků a zkrátil celkový čas tréninku zhruba o 44 % proti Async.

Nejvýše hodnocená reakce je prosté uznání – u/DAlmighty píše, že jsou prostě až příliš dobří. Věcnější linku přidal u/Mysterious_Finish543, který v paperu napočítal čtrnáct zmínek o Qwen3.6-122B a připomíná, že právě po tomto modelu se v r/LocalLLaMA dlouho volalo. Na to navazuje vyhlížení další generace: u/BVCC6FNTKX je přesvědčený, že Qwen 4 bude pecka, a u/lolwutdo se modlí, aby přišel ještě tento týden.

Druhá velká linka řeší, co to znamená pro domácí trénink. u/Dany0 vtipkuje, že teď už můžeme doma trénovat agentská monstra, jen musíme spojit výpočetní výkon, a u/Elouakili_Flexy to rozvádí: Qwen vydá model, pak framework, pak GPU cluster, zatímco my tu pořád jen sdružujeme výpočty. Do toho zapadá i povzdech u/Bulky-Priority6824 nad $6500, které si šetřil, protože podobné novinky podle něj znovu vyženou ceny a poptávku. Praktickou zkušenost přidal u/knownboyofno, který něco podobného zkoušel stavět jen pro kód a narazil na problémy s časováním při více bězích najednou, a u/bahwi se ptá po zdrojovém kódu, protože by to chtěl na trénink vyzkoušet.

Závěr patří hře se jménem. u/xNaXDy řeší, jestli se „G" v „Gyre" vyslovuje jako „G" ve „gif", nebo jako „G" v „regex", a u/Porespellar přihazuje další varianty od Qwen-Guy-Ray přes Qwen-Gee-Ruh až po zoufalé Quagmire s tím, že už nic nemá.
