# 1y5m0sn
**Kiyo LTX: open-source LoRA na rekonstrukci mozaiky ve videu**

r/comfyui · u/treehog2 · 26. listopadu 2026, 00:29 · 311 bodů / 63 komentářů · [diskuse](https://www.reddit.com/r/comfyui/comments/1y5m0sn/)

Kiyo LTX je LoRA doladěná nad modelem LTX 2.5, která umí znovu vystavět pixelované části videa. Kód i váhy jsou k dispozici zdarma pod licencí GPL 3.0 nebo LTX Community a celý projekt je zatím v betaverzi, takže autor sbírá zpětnou vazbu i nepovedené případy.

K vyzkoušení nabízí dvě cesty: vyhrazenou aplikaci Kukkiri pro Windows a příkazový řádek pro Linux, vedle toho ukázková workflow pro ComfyUI včetně varianty postavené jen na základních uzlech. Kukkiri podle autora používá sloučený optimalizovaný model jen pro video a vlastní detektor mozaiky pro delší vstupy, v jeho testech běží rychleji a s lepším detailem než běžná kombinace LTX plus LoRA.

Diskuse se okamžitě stočila k tomu, na co se takový nástroj použije nejčastěji. u/BigNaturalTilts si povzdechl „mozaiky? Na tohle já využití mám“, u/Silly_Goose6714 slavil konec cenzurovaných psů a u/CATLLM hlásil vylepšení své sbírky japonských videí. u/vyralsurfer k tomu přidal meme „už vím, co jsi za člověka“, ale vážněji uznal, že výsledek vypadá působivě – sám prý kdysi zkoušel něco podobného s maskováním a regenerací, ale nikdy to nebylo nic moc.

Nejvěcnější zkušenost přinesl u/butthe4d, který místo ComfyUI workflow zkusil samostatnou aplikaci. Desetiminutové video ve 1080p mu na sestavě s kartou 4090, procesorem 12900K a 64 GB paměti zabralo kolem pěti minut na rychlém modelu kiyo-v4 a dvacet až pětadvacet minut na kvalitativním modelu kiyo-ltx-v1. Rychlý model označil pro hrané záběry za v podstatě nepoužitelný, kvalitní za rozporuplný a chvílemi až děsivý, zatímco anime v jeho testech fungovalo výrazně lépe. Podobně to vidí u/wywywywy, který Kiyo porovnával s nástrojem Lada: nejdřív omylem testoval výchozí model V4, po přepnutí na ltx-v1 ale mluví o kvalitě vysoko nad Ladou, i když asi pětkrát pomalejší, přičemž detekce prý ještě potřebuje práci.

Zbytek vlákna řeší hranice možného. u/Seyi_Ogunde se ptá, jestli to zvládne i rozmazané nebo malé čtvercové mozaiky, u/RidiPwn zajímá, zda by šly obnovit poznávací značky a obličeje, a u/barepixels spekuluje, jestli by šlo video s nízkým rozlišením zvětšit, záměrně pixelizovat a pak obnovit. Skepticky se ozval u/phazei s tím, že z pixelizace chybí tolik informací, že model v podstatě generuje od nuly, vzápětí ale uznal, že jako hravá LoRA je to fajn. Výstižnou tečku přidal u/Apprehensive_Sky892 vysvětlením, že kukkiri je japonské příslovce pro „jasně, zřetelně, ostře“.

Pro čtenáře z toho plyne jednoduché rozdělení: na anime a stylizované záběry už je to překvapivě použitelná hračka, na věrné hrané video zatím spíš experiment k dalšímu ladění.
