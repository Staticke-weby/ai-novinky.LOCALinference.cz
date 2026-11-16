# 50285452
**Jediná SMS shodí Android. Chyba v telephony padá i nouzová volání**

Hacker News · MarkBlah · 29. 10. 2026, 08:08 · 316 bodů / 182 komentářů · [diskuse](https://news.ycombinator.com/item?id=50285452)

Jediná pečlivě zformátovaná WAP Push SMS poslaná na číslo oběti dokáže bez jakéhokoliv kliknutí shodit proces com.android.phone a tím přerušit probíhající hovory včetně tísňových. Chyba leží v komponentě WapPushOverSms v základním telefonním stacku Androidu a autor k ní zveřejnil funkční ukázku i zdrojový kód na GitHubu. Podle jeho testů padají telefony od Androidu 12 až po Android 16 se stoprocentní úspěšností napříč Pixely i Samsungy.

Web smsofdeath.com vysvětluje příčinu jako nezkontrolované přetypování délky hlavičky: pětibajtová hodnota 88 80 80 80 00 se vyhodnotí jako 0x80000000, po převodu na znaménkový int jako -2147483648, a alokace pole této velikosti vyhodí výjimku, která zabije hlavní vlákno telefonie. Zpráva přitom zůstane neviditelná ve frontě a operátor ji opakovaně doručuje, takže telefon může padat i po restartu a kolem dvaceti zpráv ho vyřadí na delší dobu. Google chybu podle webu opravil až v říjnové aktualizaci pro Androidy 14 až 17, starší zařízení mimo aktualizační okno tak zůstávají zranitelná, a záchrana jinak vyžaduje počítač s ADB a mazání fronty surových SMS.

V diskusi nejvíc rezonuje forma, ne jen chyba. Uživatel 0xcrypto si posteskl, ať lidé přestanou pro každou zranitelnost stavět nový web, a sklidil obranu ze všech stran – solyin připomněl, že módu samostatných webů zavedl už Heartbleed, __m se zastal líbivé prezentace a rustyhancock poznamenal, že web dává smysl právě když chybí CVE a hrozí ignorace. Autor MarkBlah odpovídá ironicky o návratu ke gopheru a token ringu, vážněji pak dodává, že jen chtěl mít kde chybu sdílet a text si nechal jazykově učesat, nejde mu o slávu, ale o opravu a odpovědi pro lidi, kterým telefon záhadně vypadává ze sítě.

Druhá linka řeší, zda šlo chybu přehlédnout. Uživatel klhs se diví, jak něco takového mohl někdo odložit, MarkBlah to vysvětluje zahlcením hlášeními a tříděním přes externí asistenci, zatímco anonymous908213 a paxy pochybují, zda web vygenerovaný modelem nepřehání. Tečku dělá uživatel grapheneos, který píše, že Google opravu interně napsal už 15. června a GrapheneOS ji expedoval v červencových náhledech, do listopadového bulletinu jde jako CVE-2026-58882 s kritickou závažností, a původní zamítnutí tak zřejmě vzniklo nedorozuměním nebo chybným zavřením.

Třetí proud je praktický: jak takovou SMS vůbec poslat a zda ji síť přenese. Uživatel yellow_lead se ptá právě na to a dostává odpověď, že na webu je ke stažení ukázková aplikace, ale obecněji jeroenhd popisuje tiché SMS a obejití přes modem či levnou vývojovou desku s LTE a lesspassiveobse vzpomíná na starší HushSMS, jíž šlo kdysi vyvolat nesmazatelné upozornění na hlasovou schránku. Shoda je, že důvěřivý signalizační systém operátorů podobné zprávy tradičně propouští a na filtrování se nedá spoléhat.

Z jedné SMS se tak stává učebnice toho, jak dlouho umí přežívat chyba v kódu, na který všichni spoléhají, a jak tenká je hranice mezi otravným pádem a nedostupností tísňové linky.
