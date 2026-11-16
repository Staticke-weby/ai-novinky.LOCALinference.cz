# 1xte9be
**Windows widget ukazuje limity Claude přímo na liště. Postavil ho Claude Code**

r/ClaudeAI · u/abdosarmini92 · 11. listopadu 2026, 11:20 · 577 bodů / 65 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xte9be/)

Uživatele nebavilo pořád kontrolovat spotřebu Claude na webu, a tak si postavil malý widget pro Windows 11, který drží pětihodinový a týdenní limit přímo vedle hodin na hlavním panelu. Čísla se při 80 procentech zbarví oranžově a při 95 procentech červeně, po najetí myší ukážou časy resetu a v nastavení jde přepnout interval aktualizací od 30 sekund do 30 minut i zobrazení zbývajícího místo spotřebovaného. Jde o jeden zhruba 450KB velký exe soubor bez instalátoru s asi 5 MB RAM, který funguje ve světlém i tmavém režimu lišty.

Celý projekt přitom vznikal s Claude Code s modelem Opus. Autor popisuje, že mu zadal co nejlehčí nativní cestu, Claude Code porovnal alternativy a zvolil průhledné okno vložené do lišty napsané v Rustu jen s vestavěnými Windows API, protože Windows 11 zrušily oficiální deskbands. Data widget bere ze stejného endpointu, jaký používá příkaz /usage v Claude Code, a přihlášení si obnovuje stejným způsobem a se stejným zámkem, aby si obě aplikace nepřekážely. Své zásahy autor shrnuje skromně: dodal design, rozhodoval o funkcích a kontroloval výsledek, zbytek včetně oprav podle screenshotů lišty a přípravy repozitáře nechal na modelu.

Nejživší debatu vyvolala bezpečnost. u/damagemelody upozornil, že 2 ze 71 antivirů na VirusTotal soubor označily za škodlivý, a shrnutí diskuse i řada hlasů to vykládá jako typický planý poplach u nepodepsaných open source aplikací. Autor sám před varováním „systém Windows ochránil počítač" varuje předem a radí buď potvrdit spuštění, nebo si program přeložit ze zdrojů.

Technicky zvídavou linku otevřel u/NamerekDev otázkou, jestli autor při intervalu 30 sekund nenarazil na omezení 429, protože jemu častější dotazování pod pět minut na chvíli vyřadilo i vlastní /usage v Claude Code. Navazují na to dotazy, jestli widget dotazuje servery průběžně, nebo až po najetí, a prosba u/Maydayof o podporu pro dva účty najednou, pracovní a osobní.

Zbytek vlákna se rozpadl do soutěže domácích dílen. u/ThereInAFortnight ukazuje vlastní verzi pro Linux, u/einsq84 totéž pro Stream Deck a hned několik lidí se ptá, kdy bude varianta pro macOS. Objevila se i chlubivá odbočka u/MusterCheef1, jehož nástroj napsaný v céčku má 96 KB a pod 1 MB na nečinnost. Odlehčení dodal u/lazuli_s poznámkou, že mít úzkost z limitů pořád na očích musí být vyčerpávající, a u/crumpldfoil si rýpnul, že další „vibe coded" měřič spotřeby už prý opravdu chyběl.

Pro někoho, kdo žije v Claude Code s Pro nebo Max tarifem, je to lákavá drobnost: limity pořád na očích bez klikání do nastavení, a když nevěříte hotovému exáči, zdrojáky jsou na GitHubu k nahlédnutí.
