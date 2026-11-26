# 50644817
**1Password: útočník přes GitHub získal data zákazníků**

Hacker News · lxhrstn · 25. listopadu 2026, 18:18 · 1307 bodů / 548 komentářů · [diskuse](https://news.ycombinator.com/item?id=50644817)

1Password od 19. listopadu 2026 vyšetřuje incident, při kterém útočník ovládl firemní GitHub účet jednoho ze zaměstnanců. Přes něj se dostal ke zdrojovému kódu a protlačil škodlivý kód do backendových služeb. Ty pak stáhly administrativní záznamy o zákaznících.

Podle firemního blogu šlo o jména a e-maily, identifikátory účtů a uživatelů, časy založení a posledního přihlášení, veřejné klíče a parametry protokolu SRP a tokeny z pozvánkových a recovery odkazů. Obsah trezorů ani klíče, které je chrání, prý zasaženy nebyly, firma neukládá ani hesla k účtům či tajné klíče. Útočník zároveň zkopíroval privátní repozitáře a dostal se do CI/CD systému, firma proto rotovala všechny potenciálně odhalené credentials. Jako prevenci proti hádání prodloužila ochranné kódy v e-mailech pro pozvánky a obnovu ze šesti číslic na deset alfanumerických znaků.

Nejživější technická linka řeší, jak mohl jediný účet protlačit kód až do produkce bez kontroly. tom1337 se diví, že zjevně nefungovalo code review, misker1 připomíná, že administratorský účet umí ochranu v GitHubu prostě překliknout, a hnlmorg dodává, že oprávnění v GitHubu připomínají spíš sociální síť než podnikový nástroj. loginatnine pak rozebírá celou řadu cest, jak pravidla obejít – od schváleného agenta přes staré schválené pull requesty až po dočasné vypnutí pravidel administrátorem organizace – zatímco fidotron se ptá, kolik kroků navíc by útočníkovi zbývalo k nasazení škodlivých klientů.

ChrisHardie píše, že jako dlouholetý uživatel si právě kvůli podobným incidentům drží lokální trezor na starších verzích aplikací a přeje si návrat plné podpory offline trezorů. Souhlasí s ním řada dalších, padají tipy na KeePass, Enpass nebo Keyguard s importem databáze ve formátu KDBX. Proti tomu ale TremendousJudge a Johnny555 namítají, že lokální uložení proti kompromitované aplikaci nepomůže – kdyby útočník podstrčil škodlivou aktualizaci, dostane se i k odemčenému lokálnímu trezoru, protože 1Password stejně nedrží heslo ani tajný klíč uživatele.

tptacek hodnotí 1Password jako na poměry oboru relativně seriózní a připomíná architekturu typu assume breach, kdy se firma k otevřenému textu trezorů prostě nedostane ani vlastními servery. jamesmccann se naopak pozastavuje nad formulací v rozeslaném e-mailu, která informování o vážném průniku podává jako laskavost. dwightgunning shrnuje pocit z toho, jak hluboko se útočníci dostali, slovy, že jen těsně nedopadlo hůř, a firma proto varuje hlavně před phishingem vydávajícím se za pozvánky a obnovu účtu.

Pro čtenáře z toho plyne hlavně ostražitost vůči nečekaným e-mailům a zadávání hesla a tajného klíče jen do oficiální aplikace.
