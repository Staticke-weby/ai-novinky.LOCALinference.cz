# 1xo1f2a
**RTX Spark na Linuxu ztrácí výkon. Místo 65 tokenů jede 14**

r/LocalLLM · u/CantaloupeCamper · 4. listopadu 2026, 23:06 · 195 bodů / 32 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xo1f2a/)

Na notebooku MSI Prestige N16 Flip AI Plus s čipem RTX Spark se podařilo rozběhat nativní Linux včetně grafické akcelerace přes otevřený ovladač Nvidie, s plným desktopem ve 4K při 120 Hz. Jakmile se ale stroj připojí do zásuvky, takt grafiky se zasekne kolem 780 MHz oproti více než 2,2 GHz ve Windows. U modelu GPT-OSS-120B to v testu znamenalo propad z 65,4 tokenu za sekundu ve Windows na pouhých 13,9 tokenu na stejném stroji pod Linuxem.

Odkazovaný test ukazuje prstem na komponentu, kterou Windows hlásí jako Nvidia Platform Controllers and Framework a která na notebooku rozděluje společný napájecí rozpočet mezi procesor a grafiku. Její tabulka výkonu je šifrovaná a rozklíčovat ji umí jen windowsový ovladač – když autor kontroler pokusně vypnul i ve Windows, spadly takty na stejných 786 MHz. Vedlejším zádrhelem je paměť, notebook si standardně nechává 96 GB sjednocené paměti pro grafiku a ubrat mu jde jen z Windows, i samotná instalace dala zabrat, Debian potřeboval USB adaptér na síť a hladce naběhlo až Omarchy s přibaleným ovladačem. Praktickým východiskem je podle autora WSL, které běží nad windowsovými ovladači, drží plný boost a zvládne i linuxové nástroje typu vLLM po ručním navýšení výchozího 14GB limitu.

Diskuse pod příspěvkem je k Nvidii hodně jízlivá. u/doneddat si utahuje, jak dlouho bude firma předstírat nečekanou chybu, než přizná, že ji Microsoft štědře zaplatil za udržení při životě, a u/derspenti mluví o šifrovaném firmwaru se zabudovanou linuxovou daní, jejíž vyšetřování bude jistě důkladné a oprava vyjde každým dnem. u/Dwengo k tomu dodává, že taková praktika zavání porušením soutěže a na Nvidii se už začínají soustředit rozpálené pohledy z Evropy.

Vedle toho se řeší čistě technická otázka, proč je napájecí tabulka vůbec šifrovaná. u/PM_ME_MH370 se ptá prostě proč, u/albsen namítá, že když ji Windows na stejném stroji umí rozšifrovat, je jen otázkou času, než to zvládne i Linux. u/Insomniac897 spekuluje, jak reálné by bylo šifrování prolomit a reverzně zanalyzovat, a u/vexatious-big vzpomíná na podobné trápení s první generací Intel Alder Lake v HP, kde Linux na baterii padal na 400 MHz kvůli signálu BD PROCHOT. u/KubeCommander nadhazuje, zda by nepomohl DGX OS, protože zaseknutý takt prý trápí vlivem napájecí jednotky i samotné DGX.

Nejvíc lidi baví převrácená logika celého problému. Na baterii totiž Linux drží kolem 1800 MHz a 61 až 67 tokenů za sekundu, tedy skoro jako Windows, a teprve po zapojení do sítě spadne k 15 tokenům, jak si všímá i u/riceinmybelly. Ten se zároveň ptá, jestli když je notebook s RTX Sparkem rychlejší než desktopový DGX Spark s nativním Linuxem, nedalo by se zrychlit i to DGX. Nejvýše hodnocený komentář vlákna od u/FallenVampireLord to shrnuje lakonicky slovy, že to zvládneme lépe.

Pro zájemce o lokální modely tak zatím vychází nejrozumněji dual-boot s Windows kvůli nastavení paměti a pro samotnou práci WSL, dokud Nvidia nepřenese správu napájení i do linuxového ovladače.
