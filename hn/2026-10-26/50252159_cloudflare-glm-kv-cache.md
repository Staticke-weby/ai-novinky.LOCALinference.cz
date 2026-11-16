# 50252159
**Cloudflare: chyba v SGLang ukázala cizí data ve 155 odpovědích GLM-5.3**

Hacker News · wondersky · 26. října 2026, 23:41 · 111 bodů / 37 komentářů · [diskuse](https://news.ycombinator.com/item?id=50252159)

Cloudflare popsal narušení izolace mezi zákazníky u modelu GLM-5.3 ve službě Workers AI. Od spuštění 27. srpna do 9. září se v celkem 155 odpovědích objevila data z cizích relací. Na problém upozornil 8. září bezpečnostní výzkumník Gadi Evron z firmy Knostic, Cloudflare model stáhl z veřejného provozu a ještě týž den ho vrátil zpět.

Podle firemního blogu šlo o souběh dvou věcí: předvyplňovací grafické procesory měly v KV cache místo jen pro 681 280 tokenů, zatímco inzerované kontextové okno činilo 1 048 576 tokenů, a SGLang v disaggregovaném režimu místo chyby poslal dál jednotokenovou náhradu na dekódovací uzel. Ten pak generoval odpověď nad starými stránkami paměti, které předchozí požadavky jen nepřepsaly. Cloudflare proto zvětšil pool na zhruba 2,04 milionu tokenů a opravil odmítací cestu tak, aby odmítnutý požadavek skončil ještě před přenosem, nenašel přitom známky úmyslného zneužití a zprávu vydal v koordinaci se správci SGLang.

Diskuse nejvíc oceňuje otevřenost rozboru. Uživatel kami23 chválí, že Cloudflare přiznává mezeru v testování i rychlost, s jakou dokázal servírování modelu zastavit. Zároveň se ozývá nedůvěra ke sdílenému provozu: 0xbadcafebee přiznává, že na kouzelnou izolaci tokenů zapomněl a citlivá firemní data by patřila na vyhrazené stroje, thehamkercat soudí, že jiní provideři o podobném úniku ani nevědí, a 8cvor6j844qw_d6 dodává, že mu to vysvětluje pár zcela nesouvisejících odpovědí od jednoho nejmenovaného poskytovatele.

Nejostřejší spor se vede o titulek. Uživatel jacquesm tvrdí, že s modelem jako takovým to nemá nic společného, jde o chybu Cloudflaru a SGLang v účtování paměti, a firma by neměla v titulku jmenovat nevinnou třetí stranu. Odpověď přichází přímo od uživatele kflansburg, který vysvětluje, že zákazníci musí poznat, který koncový bod byl zasažen, a proto se důsledně píše o modelu GLM-5.3 ve Workers AI, nikoli o modelu samotném. Uživatel aliasxneo to podporuje s tím, že dovětek o Workers AI jasně ukazuje na produkt Cloudflaru, takže narážky na zaujatost vůči autorům modelu nedávají smysl, zatímco adg001 a sauravadhk navrhují neutrálnější název o přesahu cache mezi požadavky.

Praktickou linku otevírá otázka uživatele segmondy, zda Cloudflare inzeroval delší kontext, než uměl obsloužit. Uživatel weird-eye-issue připomíná firemní očekávání, že motor příliš dlouhý prompt prostě odmítne, a hedgehog vysvětluje, že k selhání vedl jen jednorázový vstup bez zásahu cache, zatímco běžné vícekrokové kódovací sezení se k plné délce dostane postupně, takže spouštěč byl vzácný. Uživatel octoberfranklin to glosuje poznámkou, že i engine psaný v Rustu doplatil na neinicializovanou paměť, a 6thbit přidává vlastní zážitek, kdy mu diktování v ChatGPT po zpracování vrátilo cizí konverzaci.

Z vlákna tak zůstává ponaučení, že dlouhý kontext bez kontroly skutečné kapacity paměti a bez ověření výstupu je slepé místo, které žádný stavový kód neprozradí.
