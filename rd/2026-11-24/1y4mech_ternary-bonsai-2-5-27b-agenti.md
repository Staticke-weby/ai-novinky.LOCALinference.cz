# 1y4mech
**Ternary Bonsai 2.5: 27B agentní model se vejde do 6 GB**

r/LocalLLaMA · u/jacek2023 · 24. listopadu 2026, 20:30 · 272 bodů / 50 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y4mech/)

PrismML vydal Ternary Bonsai 2.5 27B, agentní verzi své ternární řady postavenou na architektuře Qwen3.8-27B pro llama.cpp na CUDA, Metalu i CPU. Při 1,76 bitu na váhu zabírá 5,93 GB oproti 53,8 GB u FP16, tedy zhruba devítinu. V tool callingu napříč pěti benchmarky drží průměr 77,2 bodu proti 77,7 u plné přesnosti, v agentním kódování pak 90 % výkonu FP16 včetně 75,6 na SWE-bench Verified, a podle autorů jde o nejsilnější agentní model pod 10 GB.

Stránka modelu k tomu přidává praktické detaily pro nasazení: kontext 262 tisíc tokenů, licenci Apache 2.0 a soubory Q2_0 běžící na běžném llama.cpp, zatímco varianta PTQ1_0 čeká na přijetí do upstreamu. K dispozici jsou i MTP varianty s draft hlavou pro spekulativní dekódování, které na GPU od Nvidie zrychlují generování 1,5–1,8krát až k hranici kolem 300 tokenů za sekundu na H200 a B200, plus whitepaper, demo repozitář a vlastní forky kernelů pro CUDA, Metal a MLX.

Diskuse se nese v duchu opatrného usmíření. Nejvýše hodnocený u/FriskyFennecFox oceňuje, že PrismML model dál vylepšuje navzdory smíšenému přijetí, a ptá se, proč podpora P kvantů stále není v hlavní větvi llama.cpp a jaký je rozdíl mezi PQ2_0 a Q2_0. Hned pod ním u/CodeCatto připomíná, že právě Bonsai odstartoval low-bit kvantizaci jako reálnou cestu, takže se těší na testování. Skepsi přiznává i u/LMTLS5 s poznámkou, že tentokrát autoři své kvanty „vybenchovali" na agentní kódování, a u/laser50 by rád viděl skutečné nezávislé testy, ne jen čísla od autorů.

Nejsilnější linka ale patří lidem s málem paměti. u/Uncle___Marty píše, že ternární modely jsou dar z nebes pro každého s malou VRAM a systémovou RAM, protože dřív model v ternáru jen „slintal", zatímco dnes je skutečně užitečný. Podobně u/LoquatNo3841 slaví PrismML jako zachránce pro 4GB karty a u/nazastir děkuje za práci pro „zapomenuté 8GB lidi". u/hojnikb to žene do extrému, když připomíná, že Bonsai umožnil rozběhnout 27B na PlayStationu 4 s 8 GB sdílené paměti z roku 2013.

Z věcnějších hlasů zaujal u/Puzzleheaded_Base302, podle kterého je verze 2.5 milníkem, protože poprvé prošla jeho testem hustého vyhledávání 2048 jehel v kontextu, kde předchozí verze selhávala a tím padala i v kódování. Na DGX Sparku naměřil přes 936 tokenů za sekundu v prefillu a 36,8 při generování. Ještě konkrétnější je zkušenost u/majmichu, který model s MTP rozběhl jako kódovacího agenta na notebookové RTX 5060 s 8 GB: 13 ze 13 malých úkolů v céčku, goučku, JavaScriptu, bashi, Pythonu, Rustu i webovém rozhraní prošlo skrytými testy při 73,8 tokenu za sekundu, přičemž nejtěžší bash skript dal 58 kroků za 21 minut a u vágního zadání model sám doplnil hlavičku Retry-After. Jak shrnuje u/FlyingNarwhal, bere to tak, že výkon zhruba 3bitové kvantizace je tu za 1,76 bitu.

Pro majitele slabších strojů tak Bonsai 2.5 vypadá jako první ternár, který by mohl zůstat trvale zapnutý jako levný agent.
