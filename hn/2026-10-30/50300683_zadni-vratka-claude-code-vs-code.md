# 50300683
**Zadní vrátka v oficiálním rozšíření Claude Code pro VS Code**

Hacker News · _chall · 30. října 2026, 08:09 · 863 bodů / 513 komentářů · [diskuse](https://news.ycombinator.com/item?id=50300683)

Bezpečnostní firma Phorion odhalila zadní vrátka v oficiálním balíčku rozšíření Claude Code pro VS Code distribuovaném přes Cursor Marketplace. Zasažené verze 2.1.312 a 2.1.313 obsahují persistentní SSH backdoor pro macOS, Linux i Windows, Cursor je už z tržiště stáhl a vydal bezpečnostní upozornění. Protože rozšíření běží s právy editoru, získává malware okamžitý přístup k souborům, zdrojovému kódu i vývojářským nástrojům oběti.

Rozbor popisuje nenápadný začátek infekce: do souboru extension.js je předřazena okamžitě spouštěná funkce, která se aktivuje při načtení modulu bez jakékoli akce uživatele. Ta nejprve připíše útočníkův veřejný klíč s komentářem svc-telemetry do ~/.ssh/authorized_keys a pak vybuduje odchozí reverzní SSH tunel s přesměrováním portu na localhost:22, takže operátor získá plný interaktivní shell. Pro přežití restartu si na macOS zakládá LaunchAgenta převlečeného za com.apple.sysmond.plist, na Linuxu záznam v cronu a ve Windows úlohu SysMon, a nakonec odesílá na server útočníka jednorázový přehled o stroji včetně názvů proměnných s tokeny a tajemstvími.

V diskusi nejvíc rezonuje rozsah a zmatek kolem toho, koho se útok vlastně týká. Uživatel mindracer připomněl, že rozšíření má přes 27 milionů instalací, a mrweasel dodal, že stažení napadené verze z tržiště infikované stroje nijak nevyčistí. Dlouho se přeli, zda byl zasažen i oficiální Microsoft marketplace nebo registr Open VSX, kde podle některých stop verze 2.1.313 chybí v changelogu i mezi tagy na GitHubu. Spor utnul ddworken z Anthropicu s upřesněním, že šlo pouze o verzi hostovanou na Cursor marketplace a uživatelé Claude Code ve VS Code zasaženi nejsou.

Druhá linka vlákna řeší, jak se útočník k oficiálnímu balíčku vůbec dostal. Rapzidovi chybí transparentnost v zásadní otázce, čím klíčem byla škodlivá aktualizace podepsána a nahrána. Darkwi11ow nadhodil, že postihnuté vydání na Open VSX vlastní zaměstnanec Anthropicu Igor Kofman, a není jasné, zda byl kompromitován jeho účet, nebo jiná část publikačního procesu. K0nserv z toho vyvozuje, že zasažen musel být samotný Anthropic, zatímco jiní mluví o napadení distribuční cesty na straně Cursoru.

Třetí část debaty je praktická a dost rezignovaná. Na macOS podle Phorionu část logiky selhává, protože kontrola stavu Remote Login bez práv správce vrací chybu místo hodnoty Off, takže se SSH ani nepokusí zapnout – klíče a persistence ale v systému zůstanou. Airhangerf15 popisuje, jak kvůli podobným rizikům zavírá nástroje do kontejneru s namountovaným pracovním adresářem, bhubert doporučuje dvojici kontejnerů přes compose nebo běh v gVisoru a u složitějších DevOps úloh rovnou plný virtuální stroj. Zaznívá i hořký vtip, že nenápadná chyba v logice útočníka není obrana, na kterou by se dalo spoléhat.

Kdo měl ve sledovaném období nainstalovanou některou ze dvou uvedených verzí z Cursor marketplace, měl by podle rozboru předpokládat kompromitaci a uklidit nejen rozšíření, ale i klíče, tunely a mechanismy persistence.
