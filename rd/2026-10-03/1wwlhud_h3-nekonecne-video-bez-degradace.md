# 1wwlhud
**H3: nekonečné prodlužování videa bez viditelné degradace**

r/StableDiffusion · u/SIR_NVAX_A_LOT · 3. října 2026, 14:00 · 433 bodů / 140 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1wwlhud/)

Autor dál testuje vlastní ComfyUI node, který umí generace modelu H3 prodlužovat, předsazovat i přemosťovat přímo v latentním prostoru. Nové prodloužení začíná v čase 0:27, autor přidal deset dalších oken postupně po jednom a starý i nový latent pak spojil do jediného dekódovacího průchodu, jinak by ve spojích byly vidět švy, posuny barev a tmavnutí. Tvrdí, že obrazová kvalita drží napříč okny bez degradace a vypálení, nejlépe s nativním latentem, ale převést prý jde i hotové pixelové video. Sám video glosuje, že mu hrdinka připomíná Carmen Electru ze Scary Movie, a zve k dotazům.

Nejhlasitější část vlákna jsou vtipy na účet samotného námětu. u/VodaYoda se ptá, jestli takhle léčíme rakovinu, u/MuffDivers2_ ironicky obviňuje autora, že lže a jen si doma točí ženu v prádle ve své vile. u/Barkhardt utrousí jen „katalog Sears", na což autor se smíchem vzpomíná, jak byly katalogy Sears a Victoria's Secret kdysi zásadní, a u/Easy_Manager6167 nadhodí slona v místnosti. Na to se nabalí dvojsmyslné narážky na proporce hrdinky i poznámka u/FlexFanatic, že jde o trik „rozptyl mě, ať nevidím morfování pozadí".

Pod vtipy se opakuje jedna praktická otázka: kde je workflow. Ptají se na něj u/Sad_Coach_1433, u/fluce13 i u/FeelingOld9046, autor odpovídá, že teprve přijde, protože chce nejdřív otestovat mluvící hlavu, aby splnila zadání. Sám přiznává limity: rychlost a moment pohybu se mezi okny těžko řídí a zvuk se může rozpadat, takže doporučuje zmrazit video a dohnat audio více kroky, nebo to opravit v postprodukci, což je nejlevnější a nejspolehlivější. Dodává, že postava jménem Tanya nemá žádnou zvukovou kotvu, takže se její hlas v každém okně vymýšlí znovu.

Nejcennější spor vede u/acedelgado, podle kterého k degradaci dochází dál, protože je daná způsobem, jak model odšumuje. Statický záběr se podle něj časem stejně rozpadne a jediná obrana je střih a hodně pohybu kamery i pozadí, přičemž popisuje i vlastní pokus, kdy každý klip měřil proti prvnímu a dopočítával korekční odšumění, ale ani tak neuspěl. Autor oponuje, že testovací video záměrně nemá žádný podklad prostředí a jen zkouší švy mezi pokračováními, s referenčním obrázkem pozadí prý drží mnohem lépe, protože si model mezi okny nese jen posledních pár sekund. Shodnou se aspoň na zvuku, který autor označuje za těžko řešitelný, zřejmě architektonický problém.

Z vlákna si čtenář odnese jednoduchý recept: spojovat v latentu a dekódovat najednou, hlídat pohyb a na audio si nechat zadní vrátka v postprodukci.
