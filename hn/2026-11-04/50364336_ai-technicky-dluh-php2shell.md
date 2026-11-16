# 50364336
**AI nutí firmy splácet 40 let technického dluhu. Případ PHP2Shell**

Hacker News · pseudolus · 4. listopadu 2026, 12:52 · 1144 bodů / 662 komentářů · [diskuse](https://news.ycombinator.com/item?id=50364336)

Bezpečnostní firma Calif se letos pustila do nezávislého auditu PHP sponzorovaného OpenAI a do dvou týdnů její výzkumník s pomocí nástrojů AI našel způsob, jak přes chybu nedostatku paměti spouštět na hostitelském serveru libovolný kód, instalovat malware nebo číst kritická data. Z drobného bugu se tak rázem stala kritická zranitelnost PHP2Shell a tým okamžitě upozornil PHP Foundation, aby začala pracovat na záplatě. IEEE Spectrum případ popisuje jako předzvěst bezpečnostního pekla, ve kterém nás umělá inteligence nutí splatit čtyřicet let technického dluhu.

Odkazovaný text podle titulku tvrdí, že právě AI tenhle dluh neúprosně vytahuje na světlo. Zrychluje hledání i zneužívání chyb, takže starý kód, odkládané opravy a zastaralé komponenty už neobstojí. Organizace tak musí řešit závislosti a výrazně rychlejší tempo útoků, jinak je útočníci s AI v ruce předběhnou.

Část diskutujících to čte optimisticky, jako velký úklid. Kevin_Flynn proto navrhuje titulek otočit: AI nám pomáhá čtyřicet let dluhu odstraňovat, když chybu našla a záplatu už v tuhle chvíli pravděpodobně také vygenerovala. Bearjaws píše, že za poslední tři měsíce opravil víc chyb a zranitelností než za celé roky v předchozí práci, a Lucasoato to shrnuje, že AI prostě sebrala všechny výmluvy, proč technický dluh neodstraňovat.

Vedle toho se ozývá skepse, že nový dluh vzniká rychleji, než se ten starý splácí. Lelanthran připomíná, že každý řádek kódu je závazek, a ukazuje to na nedávném útoku přes brotli, které skoro nikdo nepoužívá a nikdo ho vlastně nepotřebuje, a přitom ho neslo všechno od IIS po Caddy. Stuaxo lakonicky dodává, že AI přináší i nový druh technického dluhu, jen mnohem rychleji, a ChuckMcM varuje, že ve více než polovině případů oprava navržená AI něco jiného rozbije, takže to bude přinejmenším zpočátku z devadesáti procent lidská práce. Loquebantur z toho vyvozuje, že když AI dokáže otestovat lidský software do krajnosti, budou nakonec všechny chyby objevené, a jedinou cestou je skutečně bezchybný a dokazatelný software, což bez AI reálně nepůjde.

Třetí linka míří ke zpravodajským službám a k papírové bezpečnosti. Walrus01 by se vůbec nedivil, kdyby v NSA nebo GCHQ právě teď seděl velký tým, který sleduje díry objevené moderními modely v běžně používaném softwaru a do denních hlášení píše, co ze seznamu tajně využívaných děr škrtnout, protože to zrovna záplatují Debian nebo RHEL. Hn_submit předpovídá, že až budou počítače úplně bezpečné, budou tajné služby a policie lobovat za povinná zadní vrátka, klidně přes tajné soudy. A getfacl s Wickedsight dodávají, že certifikáty typu ISO27001 se dají až příliš snadno obehrát a existují spíš kvůli shodě s předpisy než kvůli bezpečnosti, protože firmě stačí říct, že dodavatel byl certifikovaný, a za lhaní při auditu nebývá nikdo stíhán.

Z diskuse tak zůstává obraz nucené splátky: AI útočníka i obránce zrychlila natolik, že odkládat opravy už nejde, ale zároveň se jede na dluh nový.
