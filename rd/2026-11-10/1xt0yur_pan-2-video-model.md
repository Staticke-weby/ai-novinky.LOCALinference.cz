# 1xt0yur
**PAN 2: open-weight video model se 29 miliardami parametrů**

r/StableDiffusion · u/Aggressive-Zebra-949 · 10. listopadu 2026, 23:38 · 560 bodů / 89 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xt0yur/)

Tým IFM zveřejnil PAN 2, otevřený video model s 29 miliardami parametrů postavený na latentní difuzi. Váhy jsou volně dostupné pod licencí Apache 2.0 a model zvládne vygenerovat až dvacetisekundové video v rozlišení 720p při 24 snímcích za sekundu. Spolu s vahami vyšel i trénovací kód a technický popis na blogu projektu.

Zvláštností architektury je silné zapojení jazykového modelu, který autor popisuje spíš jako konceptuálního myslitele než obyčejný přepisovač promptů. Tenhle model vytváří husté textové scénáře, v nichž jsou události a akce časované a kamera je sice vnořená pod událost, ale oddělená od akce. Autor uvádí, že při testování běžně zkoušel dvacetisekundová videa s tuctem i více časovaných pohybů kamery. Podporu model má v Diffusers i FastVideo, recept je připravený i pro VLLM.

Diskuse se rychle stočila k tomu, jak model zvládá logiku a fyziku. Uživatel u/Astral-Lemmons píše, že práce s logikou v ukázkách je naprosto šílená a že prostorové uvažování působí skoro jako kouzlo, u/ninjaGurung chválí prostorové vnímání a simulaci fyziky. Konkrétně zaujaly ukázky s vodou a viskozitou, které vypíchl u/zodiacrenders, i záběr s jablkem v otáčené nádobě, na jehož prompt se ptá u/Apprehensive_Sky892. U/Ramdak to shrnuje údivem nad úrovní porozumění světu a rovnou se ptá na generační časy.

Druhá velká linka je licence. U/SharkWipf oceňuje právě to nejpraktičtější: licenci Apache 2.0 na model místo restriktivních podmínek, kterými je podle něj zatížený konkurenční model H3. Podobně to vidí u/Enshitification, kterému se líbí právě těsné propojení jazykového modelu s difuzním modelem, a děkuje za vydání. Vděčnost za otevřené váhy se v komentářích vrací opakovaně.

Třetí téma je přízemnější: na čem to poběží. U/reeight lakonicky nadhodil „H200…“ a ptá se, jestli budou kvantované verze kompatibilní s ComfyUI pro smrtelníky s herními grafikami. Na integraci do ComfyUI netrpělivě čekají i u/Katsumend, u/Mysterious-String420 nebo u/E1DOLON, který doufá, že se model vejde do 24 GB paměti. U/Astral-Lemmons zase doufá v šanci na běh na běžném spotřebitelském hardwaru.

Z PAN 2 se tak přes noc stal nadějný otevřený hráč na poli generativního videa: slibuje dlouhá videa, chytré časování scén a kamer a hlavně svobodnou licenci s otevřeným tréninkem.
