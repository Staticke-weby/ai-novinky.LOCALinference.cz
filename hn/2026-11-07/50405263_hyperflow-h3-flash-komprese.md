# 50405263
**HyperFlow H3 Flash zmenšil 31B video model na 14B a šest kroků**

Hacker News · jiant · 7. listopadu 2026, 16:16 · 62 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50405263)

Startup Video Rebirth vydal HyperFlow H3 Flash, odlehčenou verzi otevřeného modelu MiniMax-H3. Původní transformer s přibližně 31 miliardami parametrů osekal na 13,7 miliardy ve variantě fl2va a 13,9 miliardy ve variantě ref2va. Model generuje najednou video a synchronizovaný stereo zvuk, ve výchozím nastavení v rozlišení 1344×768 při 24 snímcích za sekundu a délce 5,2 až 15 sekund.

Podle repozitáře na GitHubu stačí k vzorkování čtyři, šest nebo osm kroků bez classifier-free guidance, přičemž šest je výchozí. Pětisekundový klip v šesti krocích vznikne za 8,7 sekundy na 4× B200, za 36 sekund na jedné H200 a za 92 sekund na jedné RTX 5090. Pro domácí karty je určená kvantizace Q4_K_M s velikostí 9,1 GB, která běží v ComfyUI na 24GB GPU v počítači se 16 GB systémové paměti. Kód je pod licencí Apache-2.0, váhy jsou derivátem MiniMax-H3 pod jeho komunitní licencí.

V diskusi se sám představil Jian, jeden z inženýrů projektu. Vysvětluje, že za zrychlením stojí kombinace tří zásahů: vyhození několika bloků z padesáti a rozklad 102 lineárních vrstev na nízkorankové, dvoučasové podmínění, kdy každý krok zná aktuální šum i cílový bod, a kvantizace W8A8 s Hadamardovou rotací. Upřesňuje také zmínku o reálném čase: jejich vlastní balíček dělá 5,2sekundový klip za 8,7 sekundy, rychlosti přehrávání dosahuje až runtime SOL-H3 od Nvidie, který model podporuje od prvního dne.

Nejživější praktická linka řeší, jak model vlastně spustit. Uživatel xrd si postěžoval, že mu ComfyUI připadá neohrabané, a přál by si jednoduchý nástroj ve stylu llama.cpp. Swiftcoder mu doporučil stable-diffusion.cpp jako nejbližší obdobu ve světě difuzních modelů a syntaxing přidal, že právě přes něj s pomocí jazykového modelu řízeného z příkazové řádky rozbíhá nové modely nejrychleji. Gavmor naopak popisuje, že pracovní postupy ComfyUI řídí přes jeho API, které nechává psát i agenta, a spouští je dávkově z kontejnerů.

Třetí proud diskuse se točí kolem kvality. Swiftcoder by uvítal srovnání kvality a času mezi jednotlivými kvantizacemi, Reubend se přidal s přáním vidět přímé porovnání s originálem a amelius to přirovnal ke zmenšení JPEG na polovinu bez ukázky, jak vypadá. Ricardobeat na to odkazuje na stránku s ukázkovými videi a kodablah se ptá, jak si novinka stojí proti FastVideo FastH3, se kterým na běžném notebooku s nvidii dělá pětisekundové 480p video se zvukem za 90 sekund.

Z vlákna tak vychází známý obrázek: komprese je na papíře působivá a běží i na spotřebitelském hardwaru, o jejím skutečném přínosu ale rozhodne až přímé porovnání obrazu a zvuku.
