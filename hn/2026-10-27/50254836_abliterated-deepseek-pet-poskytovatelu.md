# 50254836
**Abliterovaný DeepSeek má už pět inference poskytovatelů**

Hacker News · moeadham · 27. října 2026, 05:53 · 94 bodů / 118 komentářů · [diskuse](https://news.ycombinator.com/item?id=50254836)

Abliterovaná verze DeepSeeku se zabydluje jako běžná infrastruktura: stránka AllModels pro model zbavený bezpečnostních odmítnutí ukazuje pět nezávislých inference poskytovatelů. Má jít o rychlý uvažující model, který plní požadavky bez obvyklých zábran a slouží jako otevřená alternativa k laděným komerčním systémům.

Služba podle popisu drží textové požadavky ve společném záložním poolu, takže výpadek jednoho poskytovatele převezme jiný. Požadavky s obrázky naopak posílá jen tam, kde je poskytovatel skutečně umí přečíst.

Diskusi odstartovala otázka autora, jak vypadá svět s úplně otevřeným přístupem k modelům bez sladění. Uživatel whatshisface odpovídá stroze, že v něm už žijeme, Moosdijk pochybuje, že by šlo o skutečné nulové sladění, a uživatel grokisracist připomíná, že abliterované modely kolují už dva a půl roku. Někdo proto ironicky slaví operace zdarma pro všechny, jiný nadhazuje, že výsledkem může být paradoxně méně překvapivých vzdálených útoků na počítač.

Nejživější linka řeší, co vlastně běžný DeepSeek odmítá. Uživatel heythere22 vypráví, jak mu práci, kterou jiný asistent vzdal, DeepSeek ochotně udělal bez stížností. Vzápětí se ale hromadí opačné zkušenosti: odmítnutý solver na captchy, software na lámání DRM, záplata na kontrolu licence u starého 3D programu přeloženého ve Visual C++ 6.0 i dotazy na vstup Číny do WTO, masakr na Tchien-an-men či přirovnání Si Ťin-pchinga k Medvídkovi Pú. Jeden z diskutujících popisuje, jak blokaci obešel tím, že model v nové relaci navedl přes Ghidru a hledání řetězce v kódu, až nakonec blokování vyskakovacích oken funkce povolil.

Z těchto zkušeností pramení obhajoba abliterovaných variant. Lidé popisují kutilské opravy firmwaru starých zařízení, snahu vzít si zpět kontrolu nad koupenou chytrou televizí nebo rekompilaci firmwaru postaveného na nedostupném komerčním překladači, kde je odmítnutí legitimní žádosti spíš překážkou než ochranou. Ozývá se i opačný hlas: uživatel hypfer tvrdí, že s otevřenými váhami pracuje týdny a na odmítnutí narazil u Qwenu jen jednou, takže u kódovacích modelů důvod k abliteraci nevidí. Bezpečnostní obavy shrnuje uživatel rvz varováním, co se stane, když se silné modely bez zábran pustí na otevřený internet, a radí vsadit na paměťově bezpečné jazyky jako Rust – na což mu další odpovídá, že ani Rust není nezneužitelný.

Řeší se i důvěryhodnost samotných poskytovatelů. Na otázku, které z nich jsou honeypoty, autor odpovídá protiotázkou, zda na tom záleží, a uživatel ddxv rozvádí, že riziko úniku klíčů či firemních dat je stejné jako u jakéhokoli jiného API. Uživatel himata4113 navíc tvrdí, že abliterované varianty trpí zhoršeným výkonem a kromě škodlivějšího tónu nic zásadního navíc neumí – místo nich mu prý lépe funguje přepsat uvažování méně sladěným modelem a pak ho vrátit DeepSeeku, aby ochotně pokračoval.

Z vlákna tak vychází abliterace méně jako konec cenzury a více jako kutilský nástroj, který ale neřeší ani výkon, ani důvěru v toho, komu posíláte data.
