# 50572348
**Signal omezuje AI agenty v iOS a Androidu ve čtení obrazovky**

Hacker News · dotcoma · 20. listopadu 2026, 10:42 · 538 bodů / 316 komentářů · [diskuse](https://news.ycombinator.com/item?id=50572348)

Signal začne na mobilech bránit systémovým AI agentům ve čtení obrazovky s konverzacemi. V iOS 27 zapíná v aplikaci blokaci screenshotů a na Androidu automaticky aktivuje nastavení Screen security, jakmile zachytí pokus asistenta sahat na obrazovku. Jde o ochranu před agenty typu Gemini Intelligence a Siri AI, kteří obsah obrazovky skenují, aby mohli odpovídat na dotazy a plnit úkoly.

Šéfka Signalu Meredith Whittakerová v oznámení navazuje na loňský zásah proti funkci Recall ve Windows 11 a popisuje stejný vzor: agent sejme data ze Signalu a ta pak leží v jeho lokální databázi nebo na cizím serveru, mimo dosah šifrování i open source kódu. Firma proto vyzývá Apple, Google a Microsoft, aby vývojářům daly jednoduché a zdokumentované vypnutí přístupu AI ke čtení obrazovky, notifikacím či souborům a aby konečně popsaly, jak agenti data zpracovávají. Přiznává přitom, že záplata je neúplná — na macOS spolehlivé blokování neumí, takže tam doporučuje vyřadit Signal v nastavení Siri, a upozorňuje i na agenty třetích stran zneužívající nastavení přístupnosti.

Diskuse se rychle stočila k hořké pointě, kterou připomněl uživatel pajamasam s odkazem na rozhovor s Whittakerovou: i když si asistenta nenainstalujete vy, může ho mít váš kontakt, a tím uniká konverzace obou. Uživatel HumblyTossed se ptá, co to vypovídá o pověsti Applu jako bezpečné platformy, když má vůbec nějaká aplikace dosah na jeho zprávy v Signalu. Uživatel nkrisc oponuje, že únik přes druhou stranu je starý jako psaní samo a žádná aplikace ho neumí zrušit.

Velký ohlas má praktická rovina. Uživatel cimnine prosí Signal, aby zveřejnil výsledky své několikaměsíční forenzní práce na iOS a Androidu jako živý dokument, z něhož by těžili i menší vývojáři a mohli do něj přispívat. Uživatel aboringusername navrhuje očividné řešení po vzoru mobilních oprávnění: samostatné povolení pro přístup AI a agentů, které by aplikace žádala až ve chvíli, kdy uživatel klepne na tlačítko pro dotaz. Uživatel ls612 k tomu dodává, že přepínač pro Siri by měl mít tři polohy, včetně režimu pouze s lokálními modely.

Třetí proud diskuse zpochybňuje samotnou důvěru v americkou neziskovku. Uživatel dijit varuje, že jedna firma v jedné jurisdikci nemá být jediným strážcem soukromých zpráv, podléhá donucení úřadů a navrhuje federaci provozu a klienty třetích stran, ideálně Matrix. Uživatel TFNA souhlasí, že žádný silný stát by masově používanou skutečně bezpečnou aplikaci nestrpěl, a podezřívá cloudovou infrastrukturu a nahrávání kontaktů na server. Do toho se mísí srovnávání s konkurencí: WhatsApp sice používá variantu protokolu Signalu, ale zálohy a sběr metadat pro reklamu ho podle diskutujících staví jinam, a část vláken řeší, zda je desktopový klient v Electronu projevem ledabylosti, nebo nutné daně za videohovory na všech systémech.

Čtenář si odnáší, že šifrování konverzace už nestačí, když obsah vidí operační systém dřív, než ho stihne ochránit.
