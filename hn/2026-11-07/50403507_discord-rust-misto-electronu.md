# 50403507
**Discord ukázal Rust klienta. Startuje dřív a bere 290 MB**

Hacker News · thunderbong · 7. listopadu 2026, 12:11 · 279 bodů / 249 komentářů · [diskuse](https://news.ycombinator.com/item?id=50403507)

Discord ukázal nového desktopového klienta Phoenix přepsaného z Electronu do Rustu. Ve srovnávacím videu na dvou ThinkPadech měl seznam přátel načtený dřív, než se stávající aplikace dostala přes načítací obrazovku, přičemž oba starty byly studené. Správce úloh u novinky ukazoval 290,2 MB RAM při dvou přihlášených účtech a technický ředitel Stanislav Vishnevskiy k tomu napsal, že klikání působí okamžitě a zpátky už nechce.

Odkazovaný článek z Windows Latest video rozebírá snímek po snímku: starý klient nejdřív minuty ukazuje prázdné okno a hlášku Starting, nový naskakuje do sekundy a aktualizace řeší potichu na pozadí. Místo Electronu sází Discord na GPUI od tvůrců editoru Zed, tedy vykreslování na GPU bez HTML, sdílený kód v Rustu pro desktop i mobily a WebAssembly pro web při zachování stejného vzhledu. Soukromé testování má začít brzy a celý případ text rámuje jako vzkaz pro WhatsApp a Teams, že chatovací aplikace nemusí automaticky znamenat přibalený prohlížeč.

V diskusi se nejdřív ozvala obrana Electronu. Uživatel cheschire připomíná, že jeho hodnota nikdy nebyla v rychlosti, ale v jednom týmu a jedné aplikaci pro více systémů s minimem práce navíc. Uživatel accurrent to rozvádí vzpomínkou na balení závislostí v minulém desetiletí, kdy prohlížeč v balíčku vyřešil webkameru či multimédia, zatímco vedle Grombobulous a NetMageSCW namítají, že dnes už Rust se statickým linkováním, GPUI a WebAssembly tuhle výhodu mažou a působí elegantně napříč Windows, macOS a Linuxem.

Druhá linka řeší, zda návrat k nativním aplikacím přinesou modely umělé inteligence. Uživatel kryptonomist doufá v novou vlnu svižných desktopových programů a llm_nerd tvrdí, že kódovací asistenti změnily kalkul nákladů, takže nafouklá multiplatformní monstra už nejsou nutný kompromis. Oproti tomu ajross je skeptický a říká, že lidé milují HTML, CSS a JavaScript z dobrých důvodů a levné či pružné portování nikdy neexistovalo, zatímco r_lee a flohofwoe varují, že jakmile chce chat zobrazovat animace, videa, náhledy stránek a zvukové ukázky, stejně se bez systému webview či browser enginu neobejde.

Zaznívá i opatrnost a praktické šťouchy. Uživatel petterroea upozorňuje, že chválit přepsání je brzy, dokud novinka neprojde běžným provozem a dlouhodobou údržbou. Uživatel fg137 připomíná, že Zed trápí stroje bez grafiky, třeba virtuální desktopy, takže vítěz ještě není jistý. A uživatel itopaloglu83 s podporou dalších glosuje, že Teams a nový Outlook na papíře šetří paměť hlavně proto, že se jejich okna schovávají pod jméno Edge, podobně jako Tauri těží ze systémového webview.

Čtenář si tak odnese jednoduchý obrázek: rychlý start a nízká paměť nadchly, ale zda Rust a GPUI opravdu nahradí pohodlí webu, ukáže až ostrý provoz.
