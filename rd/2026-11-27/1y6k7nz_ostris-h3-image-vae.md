# 1y6k7nz
**Ostris vydal vylepšený H3 Image VAE pro ComfyUI**

r/StableDiffusion · u/Apprehensive_Sky892 · 27. listopadu 2026, 05:32 · 186 bodů / 36 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1y6k7nz/)

Vývojář Ostris vydal vlastní doladění dekodéru VAE pro model MiniMax-H3-Image. Má fungovat jako přímá náhrada oficiálního VAE, uhladit přehnaně ostré detaily a zlepšit kvalitu malého textu a tváří. Encoder se neměnil, takže výměna nevyžaduje žádné další úpravy.

Pro ComfyUI stačí stáhnout soubor ostris_h3_image_vae_fp16.safetensors do složky s modely VAE a vybrat ho místo původního. Repozitář na Hugging Face zároveň slouží jako checkpoint pro diffusers ve formátu AutoencoderKLMiniMaxH3Image, zatím dostupný jen ve vývojové verzi knihovny. Model má 0,6 miliardy parametrů v poloviční přesnosti.

Největší ohlas sklidila praktická zkušenost u/collectedtooth404, na kterou čekal od vydání H3 Image. Původně mluvil o jemném zlepšení vzdálených tváří, po dalším testování ale nadšení stupňoval: snímky s rozlišením 16 megapixelů prý vypadají stejně dobře jako dříve 32megapixelové a použitelné jsou podle něj i surové generace se 4 a 8 megapixely. Podobně u/ApprehensiveTart3158 chválí chování při extrémním rozlišení nad 100 megapixelů, kde vedle sebe vidí jasné zlepšení. U/Personal-Position126 nový VAE zkoušel na restaurování staré jedn megapixelové fotky do 8K a oceňuje, že proti jinému výraznějšímu VAE sice nepřidává barvy, ale odstraňuje šum a drží čisté přechody.

Ozývají se ale i skeptici. U/Straight-Election963 přidal ukázku vzdálené postavy v 16 megapixelech a ptá se, co VAE vlastně opravuje, když tváře v dálce dál nefungují. U/Loose-Journalist-555 ani při stoprocentním přiblížení moc rozdílů nevidí a u/Odd-Mirror-2412 by raději ladil sampler nebo pixely. U/VasaFromParadise si ze šestnáctinásobné komprese utahuje, že ji žádné dotrénování neopraví, a volá po verzi bez VAE.

Širší debatu otevřel u/FireSilicon_, podle kterého je šestnáctinásobná prostorová komprese prostě brutální. Novinka je krokem vpřed, ale stýská se mu po ostrosti Z-Image nebo i SDXL a rozmazaný stlačený look prý vidí i u modelů s pouhým osminásobkem, jako jsou Krea a Moss. U/Additional_Drive1915 přidává, že H3 Image ve výchozím nastavení odložil, ale náhodný LoRA model pozvedl na úplně novou úroveň, takže kombinace oprav a správného nastavení mu dává smysl. Nejostřeji to shrnuje u/VladyCzech: za rozmazání často nemůže VAE, ale špatný plánovač, nízké rozlišení nebo nevhodná kombinace mergů a LoRA.

Kdo H3 Image odepsal kvůli kašovitým detailům, má teď levný důvod dát mu druhou šanci.
