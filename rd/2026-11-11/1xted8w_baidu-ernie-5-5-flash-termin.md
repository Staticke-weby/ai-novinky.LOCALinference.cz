# 1xted8w
**Baidu potvrdilo Ernie 5.5 Flash. Model má vyjít za dva týdny**

r/LocalLLaMA · u/jacek2023 · 11. listopadu 2026, 11:26 · 268 bodů / 62 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xted8w/)

Baidu oznámilo konkrétní termín vydání modelu Ernie 5.5 Flash, vyjít má přibližně za dva týdny. Oznámení firma zveřejnila na síti X a na r/LocalLLaMA vyvolalo během hodin desítky reakcí. Příspěvek nese označení News a odkazuje právě na tento příspěvek Baidu.

Model má být k dispozici ve variantě Base BF16 na Hugging Face, příprava podpory běží i v llama.cpp, kde na něj existuje draft pull request. Podle diskuse by se 4bitová kvantizace měla vejít na sestavy s 32 GB VRAM a 128 GB RAM, což z něj dělá lákavý cíl pro lokální provoz. Slibovaných 200 tokenů za sekundu ale většina čtenářů bere s rezervou.

Nejvýše hodnocený komentář patří u/PrimeDirective8, který chválí právě pevný termín: neví, zda to bude hit nebo propadák, ale konkrétní datum je příjemná změna proti obvyklému „brzy“. Podobně u/ps5cfw píše, že doufá v benchmarky a čím víc konkurence, tím líp. U/TheLightDances se líbí velikost modelu, v Q4 by se měl vejít na stroj s dostatkem RAM a díky MoE architektuře zůstat docela rychlý, jenže bez ukázky schopností nemá velký model smysl, když ho porazí sedmadvacetimiliardový model.

Právě srovnání s konkurencí táhne velkou část vlákna. U/Psyko38 vtipkuje, že si Baidu mělo počkat ještě týden, aby ho nesnědl Qwen 4 27B, zatímco u/CTRL___ALT___DEL rozebírá slibované výsledky: méně parametrů než GLM-5.3-Flash, lepší skóre než GLM-5.3 a v některých oblastech i nad DeepSeekem. U/One_Difficulty_39 proto nadhazuje, zda nejde na první pohled jen o post-train GLM 5.3 Flash. Opatrnější hlasy se ptají na praktické detaily, u/StartupTim na podporu obrazových a video vstupů a u/spaceman_ na omezení, protože čeká, že se model zasekne na čemkoliv kolem bezpečnosti jako mnohé moderní releasy.

Nechybí ani rýpnutí do historie a nadsázka kolem hardwaru. U/TruthHistorical7515 připomíná, že Baidu zkoumalo strojové učení už v roce 2013 a pak míč výrazně pustilo z rukou, u/rorowhat se ptá, zda někdo vůbec používal předchozí modely Ernie, o kterých skoro nic neslyší. Číslo 200 tokenů za sekundu si vzal na paškál u/Nepertia s tím, že na svém hardwaru toho zaručeně nikdy nedosáhne, u/Icy_Restaurant_8900 pro srovnání odhaduje kolem 20 tokenů za sekundu na RTX 5090 s 96 GB DDR5 v kvantizaci iQ3.

Kdo má dva týdny čas, může si nastavit připomínku a počkat na reálná čísla, zatím jde hlavně o příslib termínu a lokálně rozumné velikosti.
