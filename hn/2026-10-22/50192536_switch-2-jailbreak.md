# 50192536
**Switch 2 dostal první softwarový jailbreak**

Hacker News · ledoge · 22. října 2026, 10:01 · 760 bodů / 265 komentářů · [diskuse](https://news.ycombinator.com/item?id=50192536)

Výzkumník vystupující jako pepsipu zveřejnil projekt ns2jb, softwarový tethered jailbreak pro Nintendo Switch 2 s firmwarem 23.0.1. Tvrdí, že jde o první takový exploit pro novou konzoli. Jako ukázku schopností nechal model Codex upravit exkluzivní Mario Kart World a do závodu doplnit nové postavy.

Podle přiloženého článku začíná řetězec chybou v interpretu hry SmileBASIC 4, kde přetečení 32bitového celého čísla při mazání prvků pole umožní čtení a zápis mimo paměť. Následuje přetečení haldy v sysmodulu fs při normalizaci cesty s lomítkem a dvěma tečkami, přes které autor získá libovolný přístup do paměti, plná práva k souborům a nakonec spuštění vlastního nativního kódu s oprávněními libovolného běžného sysmodulu i vestavěného fs.

Největší ohlas měla samotná laboratoř, v níž exploit vznikal. Codex ovládá konzole přes JetKVM, obraz sleduje přes HDMI a restart po pádu řeší bluetooth vypínačem světla z Amazonu, jehož páčka mačká tlačítko napájení. Uživatel KeplerBoy oceňuje, jak tahle běžně dostupná automatizace umožňuje podobný výzkum, uživatel xacky se směje jailbreaku pomocí vypínače a uživatel hturan to popisuje jako silné paradigma dát jazykovým modelům ruce a oči, aby mohly běžet paralelně a nonstop. Podobné sestavy přidávají i uživatelé gcoakes a ecliptik, kteří takto nechávají agenty sahat na IoT zařízení nebo portovat hry na DOS a klasický Macintosh.

Druhá linka řeší cenu vstupu, tedy hru SmileBASIC 4 za 25 dolarů. Uživatel Gigachad připomíná, že konzolové exploity takhle vypadají běžně a teprve otevřou dveře dalším chybám, uživatel unrented7977 dodává, že od prvního Xboxu přes PlayStation až po PSP se zámky nejlépe otevírají s klíčem v podobě konkrétní hry. Padají i historky o GTA Liberty City Stories pro PSP nebo Cubic Ninja, po kterém hra zdražila na stovky dolarů, a uživatel haunter radí obejít nákup stažením japonského dema zdarma. Uživatel StilesCrisis čeká rychlý přísun dalších chyb, protože jailbreak zviditelní spoustu dříve nešifrovaného kódu.

Třetí proud diskuse je o dopadech. Uživatel hturan odhaduje, že se dumpy her objeví během hodin a ve světě recompilací to může znamenat exkluzivity hratelné na cizím hardwaru, a poznamenává, že takový nález by na HackerOne od Nintenda snadno vynesl přes 50 tisíc dolarů, což mu uživatel TuxSH rozporuje částkou kolem 30 tisíc. Uživatel SaltyBackendGuy čeká tvrdou odpověď nintendích právníků, zatímco vedle se rozhořel spor o takzvané game key cards. Uživatel _imnothere volá po tvrdším odporu vůči Nintendu kvůli kartám bez plné hry, ale uživatelé chocochunks, croes, rk06 a roli64 brání výrobce tím, že plné hry na kartách dává a za klíče i kódy v krabici mohou vydavatelé a drahé paměti.

Z vlákna tak zůstává obraz prvního softwarového průlomu do Switch 2, který je zároveň přehlídkou nové praxe, kdy agent hackuje hardware s kamerou, ovladačem a vypínačem v ruce.
