# 1xbobrr
**MiniMax H3 a LoRA: konzistentní postava bez „příliš uhlazeného“ looku**

r/StableDiffusion · u/DeliciousGorilla · 21. října 2026, 16:14 · 309 bodů / 50 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xbobrr/)

Autorovi přišla kvalita čistého generování z textu v MiniMax H3 mnohem hezčí než u variant s referencemi, a tak se na ní rozhodl postavit LoRA vlastní originální postavy. Použil osm statických snímků ze Z-Image Turbo, vlastní hlas z ElevenLabs a čtrnáct krátkých klipů, jak postava mluví, poskládaných z pěti generací v Seedance. Ve srovnávacím videu je vlevo stejný seed s RefModem a vpravo s LoRA v síle 0,8 a DLSS 5 – RefMod podle něj drží tvář, ale všechno působí až moc naleštěně, zatímco LoRA se blíží právě vzhledu generování z textu.

Největší spor se strhl o to, jestli má LoRA vůbec ještě smysl. u/cc_aa_tt_zz tvrdí, že budoucnost patří referencím, protože se s nimi dají kombinovat i několik postav najednou, zatímco LoRA se trénují dlouho a při kombinování na sebe naskakují, takže je MiniMax H3 poslal do důchodu. Oponuje mu u/Dzugavili s vysvětlením, že LoRA si postavu najde nebo vytvoří uvnitř modelu a rozumí jí i na nízké úrovni, kdežto RefMod je jen zabalená latentní reference – rychlá a věrná jedna ku jedné, ale bez napojení na vnitřní koncepty modelu, takže na variabilitu nestačí.

Část lidí autorovi vyčítá, že srovnává nesrovnatelné. u/Belgeran se ptá, co se tu vlastně porovnává, jestli LoRA proti RefModu, nebo verze s DLSS proti verzi bez něj, když se mění víc proměnných najednou. Na to navazuje u/pwillia7 otázkou, proč nedostala DLSS i druhá strana, a u/thegreatdivorce dodává, že i s referencemi lze styl promptovat stejně jako u textu, ne-li lépe. Nejtvrdší je u/ShutUpYoureWrong_, podle kterého je celý rozdíl jen chyba v datech – ateliérově nasvícené fotky udělaly z videa reklamu na hydratační krém – a ani jedna verze prý nevypadá jako referenční fotky.

Zbytek vlákna rozebírá autorovy postřehy z tréninku, který běžel headless ve Fizgigu s rankem 16 a nastavením Automagic v3. Síla 0,8 se ukázala jako ideál, na plnou jedničku prý postava vypadá, jako by měla příliš make-upu, a prompt „bez make-upu" to ještě zhoršil. Náhledy z tréninku se podle autora nedají brát vážně, pozdní epochy tam vypadaly hrozně a ve skutečném workflow skvěle, což mu u/b4ldur potvrzuje i z nástroje Moss. Řeší se i přenos nasvícení z referencí, ztráta klonovaného hlasu při druhém průchodu nebo historka, kdy postava zasazená do sklepa s Mulderem a Scullyovou začala vypadat jako agentka Reyesová, jen s britským hlasem.

Kdo by chtěl postup zopakovat, najde v příspěvku workflow pro H3 s LoRA, kombinaci s RefMody i DLSS 5 a poděkování autorům nástrojů od Fizgigu po DMAD.
