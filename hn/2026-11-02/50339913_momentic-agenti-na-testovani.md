# 50339913
**Momentic spustil QA agenty, kteří sami procházejí aplikaci a hledají chyby**

Hacker News · wuweiweiwu · 2. listopadu 2026, 18:05 · 137 bodů / 92 komentářů · [diskuse](https://news.ycombinator.com/item?id=50339913)

Startup Momentic představil agenta Mo, který sám plánuje, prochází ovládací prvky a uživatelské toky ve webových, iOS a Android aplikacích a sbírá chyby. Zakladatelé Wei-Wei a Jeff si tím chtějí ulevit od úmorného psaní a údržby testů v nástrojích jako Playwright a Selenium. Místo generování skriptů sází na myšlenku, že se v nové éře budou testovat agenti navzájem, a Mo staví na třech letech vývoje a milionech tras z reálných aplikací.

Ukázka na webu firmy zachycuje typický úlovek: na feature branchi prý změna směrování přihlášení přeskočila ověření nového zařízení. U spotřebitelské fintech aplikace tak tiše vypadl bezpečnostní krok, který měl nové přihlášení dodatečně potvrdit.

Nejživější debata se strhla kolem čísel, která Momentic sám zveřejnil. Čtenáře zarazilo přiznání, že Mo má přesnost 84 % proti 86 % u Codexu a stojí 2,67 dolaru za chybu proti 0,80 dolaru, a ptali se, zda to není vlastně reklama na konkurenci. Inženýr Henry vysvětlil, že firma optimalizuje hlavně na záchyt: za stejný čas prý Mo najde více než třikrát tolik správných chyb jako nejbližší další QA agent, protože nejhorší je chybu přehlédnout a pustit rozbité do produkce. Doplnil to kolega Gabe tvrzením, že proti Claude Code najde Mo zhruba pětkrát víc chyb a o 35 % levněji za chybu v hodinové relaci. I tak si část vláken utahovala, že věta v oznámení je napsaná tak nešikovně, až jeden z diskutujících po několika přečteních usoudil, že si má raději obnovit předplatné Codexu.

Druhá velká linka je o penězích a závislosti. Uživatel aliasxneo si postěžoval, že jde o další službu účtující vlastní tokeny, které nelze přenést ze zbytků jeho jiných předplatných, a přirovnal to k leteckým mílím. Spoluzakladatel Jeff odpověděl, že o podpoře vlastních klíčů dlouho přemýšleli, ale s hotovými modely nebyli spokojení s výkonem, protože velká část práce byla v ladění rutinní dřiny jako ukotvení prvků a vizuální porozumění. V podobném duchu odpovídal na otázky kolem vendor lock-inu: Mo generuje testovací případy v přirozeném jazyce, na přání je přepíše do Playwrightu do repozitáře, průzkumné testování je záměrně nedeterministické a determinismus řeší až regresní produkt pomocí cachování.

Třetí spor je o to, co zbude, až tohle umí frontier modely samy. Na otázku, v čem je příkop, odpovídá jeden z komentujících, že asi tak týden, než stejnou schopnost integrují velké laboratoře, další připomíná osud mnoha vlastních harnessů, které smetla nová generace modelů. Jeff oponuje, že právě na vlastním harnessu, odolném kontextu a datech záleží, zmiňuje popularitu Devinu a nástrojů pro review kódu postavených na běžných modelech a věří, že třeba Opus 6 schopnosti Mo spíše odemkne, než aby je sebral. Praktickou tečku přidává popis uzavření smyčky: Mo prý nemá chyby opravovat, k tomu firma dodává rozhraní a dovednost pro kódovacího agenta, takže se dá postavit postup, kdy jeden agent funkci postaví, Mo ji otestuje a člověk vstupuje do hry až po vyčištění chyb.

Kdo si z vlákna odnese jednu větu, bude to tahle: automatizované procházení aplikace dává smysl, ale zákazníci chtějí přenositelné tokeny, přenositelné testy a důkaz, že vlastní harness přežije další vlnu modelů.

[Zpět na index](00-index.md)
