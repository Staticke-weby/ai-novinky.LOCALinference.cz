# 50467439
**LibreAGI: torrentový tracker, který zachraňuje open-weight modely**

Hacker News · satuke · 12. listopadu 2026, 15:11 · 137 bodů / 27 komentářů · [diskuse](https://news.ycombinator.com/item?id=50467439)

Na Hacker News se objevil projekt LibreAGI, soukromý BitTorrent tracker, kde členové drží kopie open-weight modelů, kterým hrozí, že zmizí z internetu. Heslem tvůrců je, že otevřené modely by měly přežít místa, která je hostují, a proto zájemci musí projít přihláškou a pak modely nejen stahovat, ale hlavně seedovat.

Web projektu vysvětluje, jak má archiv fungovat: kredit za seedování roste s velikostí a časem, přičemž model s jedinou kopií vydělává čtyřnásobek základní sazby, protože právě vzácné kusy potřebují pomoc nejvíc. Přijímá formáty od safetensors a GGUF po ONNX pod licencemi Apache-2.0, MIT nebo Qwen Community License, každý soubor se kontroluje proti zdrojovému commitu a každý model prochází ruční revizí. Pojistkou je podepsaný veřejný katalog se seznamem modelů, hashů a zdrojů, podle kterého by šlo swarms obnovit, i kdyby samotný web zmizel, a k tomu otevřený IRC kanál pro dotazy ještě před registrací.

Největší debatu vyvolalo právě to, že je tracker soukromý a vyžaduje přihlášku. InsideOutSanta nechápe, k čemu je to dobré, když jde o v zásadě rozumný nápad, a cat_screamer píše, že by rád seedoval, ale odrazuje ho nutnost se přihlašovat. Odpověď přichází hned z několika stran: simonmales nadhazuje jedním slovem odpovědnost, gorszon připomíná, že je to u soukromých trackerů standard, který brání malwarovému peklu ve stylu Pirate Bay a nutí lidi vracet do oběhu aspoň to, co si stáhli. Sám zakladatel satuke v diskusi vysvětluje, že jde o lehkou formu, jejímž cílem je vymáhat seedování jedna ku jedné a nerozložit zátěž velkých modelů na pár nadšenců, což bez účtů a vymahatelnosti pravidel nejde.

Podobně praktická je výtka uživatele modimihir, že pro decentralizovaný archiv otevřených modelů musí existovat lepší cesta než autorizace a formulář. Do stejného tématu zapadá i dotaz uživatele randomblock1, čím se LibreAGI liší od veřejných archivů typu Hugging Face. Gorszon na to odpovídá, že se lišit nemusí a že více trackerů je dobře už jen kvůli redundanci, protože když jeden padne, ostatní drží kopie dál.

Řeč se stočila i k formátům a nostalgii po starých trackerech. Uživatel jcelerier se ptá, proč omezení na safetensors a GGUF, když právě ONNX vzniklo pro přenositelnost, na což wtallis kontruje, že ONNX u velkých jazykových modelů prakticky nevídá a zná ho jen z malých modelů pro koncová zařízení. Největší ohlas přitom sklidilo přirovnání uživatele rgbrgb, že jde o Oink či Waffles.fm pro modely, na které nathancahill jen suše přidal vzpomínku na jejich konec. Třešničkou je pak povzdech uživatele zymhan, že je obrovská škoda, že se projekt nejmenuje Liberagi.

Z diskuse tak vyplývá, že nápad archivovat váhy v torrentové síti se lidem líbí, ale soukromí a přihlášky zůstávají kamenem úrazu mezi touhou po otevřenosti a potřebou udržet seedery u zodpovědnosti.
