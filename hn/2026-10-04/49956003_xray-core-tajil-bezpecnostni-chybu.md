# 49956003
**Xray-core půl roku tajil obejití ověření certifikátů**

Hacker News · timbill · 4. října 2026, 19:38 · 78 bodů / 10 komentářů · [diskuse](https://news.ycombinator.com/item?id=49956003)

Na Hacker News se objevil odkaz na issue #672 v repozitáři net4people/bbs, který má 5,3 tisíce hvězd. Jeho autor, který se představuje jako nálezce chyby, v něm obviňuje populární proxy software Xray-core, že půl roku zamlčoval zranitelnost umožňující obejít ověření certifikátů a vystavit uživatele útoku muže uprostřed. Příspěvek staví případ jako selhání odpovědnosti a transparentnosti u bezpečnostního open-source projektu.

Podle textu issue nahradil Xray-core v lednu 2026 původní volbu pinnedPeerCertificateChainSha256 novou volbou pinnedPeerCertSha256, která měla při použití self-signed certifikátů v kombinaci s allowInsecure zajišťovat vlastní připnutí certifikátu. Útočník do ní ale mohl vložit listový certifikát kamkoliv do řetězu a logika ho přijala jako ten připnutý. Nálezce chybu 6. února 2026 nahlásil soukromě, správci ji ještě týž den tiše opravili s poznámkou o „zjednodušení kódu“ a ve verzi v26.2.6 o ní nepadlo ani slovo, zatímco na Telegramu ve stejný den hlásali, že software musí být navržen s bezpečností v jádru. Když 3. července 2026 zjistil, že oprava je neúplná a obcházení je za určitých okolností stále možné, zveřejnil ji proto přes GitHub Security Advisory.

Věcná část diskuse se shoduje, že mlčení je větší problém než samotná chyba. Uživatel eriwang915 shrnuje podstatu tak, že nová logika považovala podstrčený list za ten připnutý certifikát, aniž by to oprava přiznala jako zranitelnost, uživatel cryptolobster nad reakcí Xray-core jen vyjadřuje zklamání. Uživatel LoganDark v narážce na předchozí shrnutí dodává, že z příběhu nelze vynechat pokrytectví ani to, že i opravená verze dál propouštěla, a uživatel soltanov to zobecňuje: oprava kódu je jen polovina reakce na incident, bez upozornění, výčtu zasažených verzí a notifikace dál se uživatelé nedozvědí, zda jsou stále v ohrožení.

Vedle toho se řeší, kde se Xray vlastně používá. Uživatel usernomdeguerre se ptá, zda není většina využití v pevninské Číně a proč odtud nepřicházejí sofistikovanější řešení, když tomu napovídají tamní restrikce i počet připojených lidí. Uživatel ranger_danger odpovídá, že podobně blokují provoz i Írán nebo Rusko a mnohdy přitom projde i prosté VPN v běžném TLS nebo čisté SSH, novinkou je náhodné měnění otisků TLS a maskování za legitimní provoz a domény či rozprostření tunelu přes více koncových bodů najednou. Uživatel wartywhoa23 doplňuje, že v Rusku je nyní Xray obrovský a často jedinou cestou do vnějšího internetu.

Závěr patří dvěma praktickým poznámkám. Uživatel amritananda přidává využití k obcházení captive portálů, kde část provozu prochází: u některých letů s messagingem zdarma se prý kontroluje jen SNI, takže stačí nastavit doménu Xray na whatsapp.com. Uživatel wartywhoa23 k samotné zranitelnosti dodává, že je podle něj bezpečnější nechat TLS na reverzní proxy před Xray.

Příběh tak zůstává připomínkou, že u bezpečnostního nástroje rozhoduje nejen oprava, ale i to, zda se o ní uživatelé včas dozvědí.
