# 50497155
**GLM-5.3 na dvou DGX stanicích: 607 tokenů za sekundu**

Hacker News · wondersky · 14. listopadu 2026, 15:09 · 133 bodů / 65 komentářů · [diskuse](https://news.ycombinator.com/item?id=50497155)

Kvantizovaný mixture-of-experts model GLM-5.3 NVFP4 má 753 miliard parametrů, z nichž se na jeden token aktivuje 40 miliard, a v paměti zabírá kolem 464 GB. Na jeden GB300 s 252 GB HBM3e se proto nevejde. Nvidia ukázala, jak ho rozdělit přes dvě stanice DGX propojené přes ConnectX-8 RDMA a obsluhovat ho přes vLLM s tensorovým paralelismem, přičemž špičkou je 607,8 tokenu za sekundu při šestnácti souběžných požadavcích.

Návod popisuje obě stanice jako jedinou službu s jedním OpenAI kompatibilním rozhraním: první stanice hostí API, druhá funguje jen jako výpočetní pracovník a každá drží i počítá zhruba polovinu vah. Pro propustnost zapíná predikci více tokenů najednou, ukládání KV cache ve formátu FP8 a cachování prefixů promptů. Měření na sadě SPEED-Bench Coding pak sleduje chování pod zátěží a nad optimálním souběhem už propustnost klesá a latence prudce roste.

Diskuse se nejdřív zastavila u toho, co to číslo vlastně znamená. osamagirl69 upozorňuje, že jde o součet přes všechny souběžné uživatele: samotný uživatel dostane kolem 107 tokenů za sekundu, při šestnácti lidech pak vychází na jednoho něco přes 35 tokenů za sekundu. I tak se část čtenářů ptá, jestli je to na dva stroje za zhruba 200 tisíc dolarů málo. jbellis tvrdí, že sestava s osmi kartami B6000 vyjde na polovinu a podle jednoho komunitního pokusu dává dokonce o 60 % vyšší propustnost, zatímco fulafel oponuje, že smyslem DGX stanic je právě to, že jsou desktopové.

Nejdelší spor se vede o návratnost. hkalbasi počítá při ceně 100 tisíc za stanici a sazbě 1,4 dolaru za milion výstupních tokenů návratnost kolem sedmi let při maximálním vytížení, a dává tak smysl hlavně kvůli soukromí. liuliu naopak s jinými cenami za vstupní a výstupní tokeny dochází k návratnosti pod jeden rok. lumost a poisonborz dodávají, že v bankovnictví, zdravotnictví nebo citlivých provozech nejde o excel, ale o to, že schválení externího API by trvalo roky a vlastní neměnný a necenzurovaný model za to stojí. AnotherGoodName varuje zájemce o domácí nasazení před spotřebou 1,6 kW na stanici, hlukem a tím, že pro domácnost je takový výkon zbytečný.

Zajímavá je i volba modelu. boodleboodle se ptá, proč Nvidia zvolila GLM a ne DeepSeek, frogblast vysvětluje, že předností DeepSeeku je právě malá paměťová stopa na uživatele a tedy vyšší souběh na stejném železe, což se u hrstky lokálních uživatelů nemusí projevit. spwa4 vyhlíží ERNIE 5.5, který by měl mít podobný výkon jako GLM-5.3 a vejít se na jednu stanici. Keyframe k tomu přidává osobní linku o cenzuře velkých služeb a chválí si domácí kombinaci staré RTX 3090 a stroje se Strix Halo, na které mu běží menší modely bez „chůvičky".

Pro čtenáře z toho plyne jednoduché poučení: dvě propojené stanice dokážou frontier model udržet lokálně a rychle, otázkou zůstává, zda takovou sestavu potřebujete celou, nebo vám stačí menší model doma a velký v cloudu.
