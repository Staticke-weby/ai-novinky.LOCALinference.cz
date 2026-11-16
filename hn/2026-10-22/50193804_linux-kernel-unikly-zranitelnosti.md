# 50193804
**Zranitelnosti Linux kernelu omylem unikly na veřejný mailing list**

Hacker News · mrkn1 · 22. října 2026, 13:12 · 244 bodů / 87 komentářů · [diskuse](https://news.ycombinator.com/item?id=50193804)

Přes noc se na veřejném mailing listu linuxového jádra LKML objevilo hned několik hlášení o dosud neznámých zranitelnostech. Poslala je tam Zero Day Initiative společnosti Trend Micro, která je normálně posílá na soukromý bezpečnostní list. Druhý muž linuxového vývoje Greg Kroah-Hartman na to reagoval u každého hlášení dotazem, proč to jde veřejně.

Podle serveru Phoronix jde o neobvyklý a rizikový způsob zveřejnění, protože chyby zatím nejsou opravené v hlavní vývojové větvi mainline. Nejvýše hodnocené mají skóre CVSS 9,0: chyba SMB Direct s podtečením celého čísla a race condition v KSMBD, obě umožňující vzdálené spuštění kódu. Zbytek tvoří lokální eskalace privilegií v síťovém kódu skb_zerocopy a v ovladači VMWGFX, neinicializovaný zdroj v kódu NVMET vedoucí k úniku informací a přetečení zásobníku v TCP dotazech, přičemž u některých už se záplaty testují nebo čekají ve větvích -next.

Na Hacker News se nejvíc řeší, jestli šlo opravdu o nehodu. Uživatel NooneAtAll3 v tom s nadsázkou vidí snahu vyvolat paniku, aby se pak prodávaly bezpečnostní produkty, pelagicAustral souhlasí, že poslat takovou kořist omylem na mailing list je divoká představa, a ReDress poctivě dodává, že bezpečnostní představy ZDI a správců jádra se prostě nemusí shodovat. Uživatel dayofthedaleks by titulek rovnou doplnil o jméno Trend Micro, aby bylo koho zostudit za amaterismus.

Velkou odezvu má nápad, že o omyl vůbec nejde, ale o nové pravidlo. Uživatel wongarsu připomíná, že jádro po zahlcení soukromého listu duplicitami žádá chyby nalezené s pomocí umělé inteligence hlásit veřejně, a smashed k tomu cituje dokumentaci: kdo k hledání chyby použil asistenci AI, musí s ní zacházet jako s veřejnou. Uživatel rwmj to považuje za správné, protože chybu nalezenou jedním modelem umí najít i jiný model. Do toho zapadá postřeh uživatele lynndotpy, že nejzávažnější chyby jsou v SMB a KSMBD a web Trend Micro se zrovna chlubí velkým nápisem o pokroku v bezpečnosti s Anthropic.

Třetí vlákno se točí kolem toho, co obě devítkové chyby vlastně ohrožují. Uživatel fguerraz žertem navrhuje vyhodit implementace SMB z jádra, případně tam rovnou začlenit PHP, ReDress připomíná, že se SMB do jádra dovezlo jako optimalizace uživatelské verze, a pavon uklidňuje, že jde o modul, takže neriskuje nikdo, kdo ho nenačítá. Odlehčení dodává cookiengineer opravou vtipu o posledních zranitelnostech roku slovy až do dneška, zatímco debatu o bezchybném systému s AI shazuje regenschutz hláškou, že všechno je bez chyby, dokud v tom někdo chybu nenajde.

Omyl jedné firmy tak znovu otevřel starou otázku, jestli v éře automatického hledání chyb má ještě smysl tajit je před veřejností.
