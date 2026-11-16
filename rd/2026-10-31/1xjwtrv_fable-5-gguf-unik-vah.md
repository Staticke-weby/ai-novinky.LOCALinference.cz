# 1xjwtrv
**Fable 5.gguf: únik 8TB vah rozebírá LocalLLaMA**

r/LocalLLaMA · u/speedb0at · 31. října 2026, 02:00 · 1667 bodů / 379 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xjwtrv/)

Na r/LocalLLaMA se objevil inzerát slibující váhy modelu Fable 5. Snímky obrazovky ukazují shard o velikosti kolem 7 GB s číslováním model-00638-of-00640, tedy 640 dílů dohromady zhruba za 4,4 TB, zatímco samotný inzerát mluví o 8 TB. Vlákno označené jako vtip se okamžitě stočilo k tomu, kdy se objeví Fable 5 ve formátu GGUF pro domácí stroje.

Technickou linku rozjel u/pantalooniedoon, který ze snímků vyčetl tvary tenzorů a podivný datový typ 0C_28FF. Podle něj nejde o běžné F16, BF16 ani FP8, ale o vlastní kvantizační formát s maticí škálovacích koeficientů, přičemž bias zůstal v plné přesnosti F32. Kdyby šlo o 8 bitů, odhaduje model na 4,4 bilionu parametrů a víc, při 4 bitech by to prý byl skoro 9bilionový obr, což by prý odpovídalo utrácení laboratoří ve stovkách miliard. Jak poznamenává u/nullc, detaily architektury by možná byly ještě zajímavější než samotné váhy.

Většina vlákna ale čte snímky jako podvrh postavený na volně dostupném modelu. U/lil_nosh_X cituje tvrzení, že soubory patří DeepSeeku a po bajtu odpovídají open-source modelu DeepSeek V4.1-Flash-1017 vydanému 17. října, prodejce na ně jen přelepil nálepku Fable 5. U/qnixsynapse dodává, že screenshot zmiňuje region eu-north-1, který Fable nehostuje, a že někdo v hex editoru přepsal sedmiznakové F8_E8M0 za falešné 0C_28FF. U/CasualCapybara si dohledal, že posuny dat ze třetího snímku přesně sedí na DeepSeek-V4.1-Flash-1017, a u/jbaenaxd shrnuje, že shoduje se i přesná velikost 7 216 564 KB a číslování shardů, takže jde podle něj o přejmenovaná data zdarma vydávaná za zboží.

Skepsi přidává i u/-p-e-w-: nechápe, proč by interní model měl v metadatech reklamní popisek, veřejné marketingové jméno Fable 5 a formát safetensors, když si velké firmy obvykle staví vlastní systémy. U/Betadoggo_ upozorňuje, že takovou věc je triviální zfalšovat a prodejce má nový účet bez reputace, u/d70 glosuje, že jeden shard ze 640 nám stejně nic nedá. Odtud pramení i vtipy: u/SwimmerJazzlike hlásí Fable 5 Q1_S_Q.gguf, u/Fit_Split_9933 slibuje běh verze s extrémní kvantizací na jedné kartě a u/NoFaithlessness951 se ptá, jestli si ten shard má člověk pověsit na zeď, zatímco u/MillerBurnsUnit radí rychle najít ostatní horcruxy.

Za žerty se ozývá ekonomika obřích modelů. U/Lifeisshort555 se směje, že 8 TB vysvětluje jméno Fable a naznačuje ještě větší příští generaci, jen netuší, jak by se to mohlo zaplatit za výpočetní výkon. Podobně u/FormerIYI pochybuje, co by 4 či 8 bilionů parametrů přineslo proti střední třídě typu DeepSeek za zlomek paměti, a mluví o pálení cloudových peněz, kterého si všímá i finanční sektor.

Zůstává tak historka o nemožném úniku: buď by domácí GGUF verze Fable 5 byla sci-fi o terabajtech, nebo – a tomu věří většina diskuse – jde o přebalený DeepSeek s vymyšleným datovým typem.
