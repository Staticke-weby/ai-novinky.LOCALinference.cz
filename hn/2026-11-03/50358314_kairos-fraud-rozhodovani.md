# 50358314
**Kairos: open-source rozhodování o podvodech bez velkých anotovaných dat**

Hacker News · ayanb9440 · 3. listopadu 2026, 22:16 · 82 bodů / 17 komentářů · [diskuse](https://news.ycombinator.com/item?id=50358314)

Společnost Finic vydala Kairos jako open-source alternativu k platformám Sift, Sardine a dalším nástrojům pro real-time fraud decisioning. Vedle klasických modelů jako XGBoost a logistická regrese sází na takzvané „System One“ rozhodovací modely, do kterých lze psát otázky v přirozeném jazyce typu je tohle jednorázový e-mail. Cílem je obejít nedostatek kvalitních anotovaných dat a zachytit nestrukturované signály, na kterých klasické modely selhávají, a zároveň držet krok s podvodníky, kteří taktiky mění v řádu týdnů.

Podle popisu na GitHubu Kairos v reálném čase rozhoduje o registracích, přihlášeních, objednávkách, platbách a výplatách a každé rozhodnutí vrací jako schválit, přitvrdit, poslat na kontrolu nebo zablokovat včetně rizikového skóre a zdůvodnění. Pracuje s historií subjektu, sdílenými zařízeními, kartami a adresami, nabízí workflow, fronty a případy pro lidské review a staví na rozhodovacím modelu Grayson, jehož odpovědi se mohou stát rysy pro tradiční modely. Ladění má obstarat agent přes MCP server, který navrhne varianty, natrénuje je na nejstarších datech, vybere nejlepší podle ROC-AUC či přesnosti a vítěze nasadí jako novou verzi.

Nejživější debata se paradoxně stočila ke jménu. Messier43 upozornil, že meta linuxová distribuce se už jmenuje stejně, a jonas21 přidal firmu na ověřování identity, organizaci pro bezpečnost AI i program DARPA se slovy, že u jakéhokoli starořeckého slova se kolize najde. citguru to uzavřel smířlivě, že rychlé hledání na GitHubu ukáže desítky Kairosů, ale nic to nemění na tom, jaký problém se projekt snaží řešit, zatímco giwook jen suše nadhodil a co.

Druhá přestřelka patří slovu decisioning. tensegrist ho označil za novinku a octoberfranklin si postěžoval, že ho otravují vymyšlená slova vzniklá přilepením koncovky na podstatné jméno. Odpovědi se ale autora zastaly: bobbiechen připomněl, že v tomhle oboru jde bohužel o zavedený termín, mh- dodal, že za to nemůže autor příspěvku, a marcus_holmes argumentoval, že jazyk je tekutý a přizpůsobuje se potřebám, takže je lepší srozumitelná adaptace než úplně nové slovo bez nápovědy.

Věcnější linku přinesl bradknowles se vzpomínkou na rok 1995, kdy jako správce pošty v AOL bojoval se spammery. Novou obranu prý vyvíjeli týdny či měsíce a útočníci ji obešli za jediný víkend, dokola, a od té doby se podle něj změnil jen trh a rychlost adaptace podvodníků. factotvm pak poděkoval za otevřený kód, ale rýpl si do volby TypeScriptu na Node pro platební bránu, kde by chtěl program, který se za běhu nedokáže přepsat z externích zdrojů. V aktuálním Dockerfile podle něj nic na úrovni běhu nebrání pollution prototypů a chyba v konfiguraci je ten typ chyby, který se pak dlouho vrací.

Kdo si chce Kairos osahat, může ho provozovat v Dockeru, nebo sáhnout po hostované verzi a napojit na ni Claude Code, Cursor či Codex.
