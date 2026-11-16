# 49952111
**SCM: lokální AI vyhledávání ve fotkách a videích na macOS**

Hacker News · allenleee · 4. října 2026, 11:24 · 151 bodů / 67 komentářů · [diskuse](https://news.ycombinator.com/item?id=49952111)

Vývojář allenleee představil SCM, tedy Screen Memories, nástroj pro macOS slibující hluboké AI hledání v každé fotce a v každém snímku videa v libovolné složce. Vzpomínku stačí popsat běžným jazykem a inference proběhne přímo na Macu bez účtů, cloudu a nahrávání médií kamkoliv ven.

Stránka projektu popisuje pět způsobů hledání: Soubory najdou celé fotky a videa podle významu, Scény míří na přesný záběr i s časovým kódem, OCR čte text viditelný v obraze a Dialogy hledají doslovně v přepisu mluveného slova z Whisperu. Volitelný místní chat pak odpovídá nad už vytěženými dialogy, texty a názvy souborů a ke každé odpovědi přikládá klikatelné citace.

Nejživější byla otázka škálování. Uživatel stephenitis přiznal, že se mu líbí celá myšlenka, ale od zkoušení ho zrazuje neznámá doba zpracování dvanácti tisíc videí. Uživatel hn3ufz62f7 na základě vlastní stavby podobného hledání s CLIP na M1 odpověděl, že snímkovací frekvence je celá hra a jedno políčko za sekundu u takového objemu znamená dny, zatímco jen klíčové snímky stáhl na práci přes noc. Na to navázal uživatel xnx dotazem, zda nezkusil detekci scén, protože střihy kamery budou ještě řidší než klíčové snímky, a uživatel pezgordo přidal zkušenost ze střihového světa se zmenšenými náhledy a varoval, že hledaný moment kratší než vzorkovací interval snadno propadne.

Řešila se i konkurence a praktické nasazení. Uživatel lucideer připomněl multiplatformní Immich jako přibližné AI hledání fotek a videí, i když bez záruky hledání po jednotlivých snímcích. Uživatel mannyv ho ale zkoušel a vadila mu mimo jiné záplava složek s náhledy v každém rozlišení u mnohaterabajtové knihovny sbírané desítky let. Jiné dotazy mířily na hledání lidí, tváří a mazlíčků po vzoru iOS a na rešerši fotobanky o dvou tisících fotkách, třeba domů s palmami, kuchyní nebo pouštní krajiny, přičemž uživatel tredre3 namítl, že přirozeným jazykem už umí hledat přímo Apple Fotky.

Nejostřejší výměna se stočila k technologiím. Uživatel postalcoder vyčetl, že na Macu měl místo Tesseractu nastoupit Apple Vision framework, který je rychlejší i přesnější. Autor souhlasil, že čistě pro Mac by Vision použil, ale sáhl po Tesseractu kvůli snadné přenositelnosti, protože celá inferenční vrstva je v JavaScriptu od začátku do konce přes Transformers.js a ONNX pro CLIP a SigLIP, Whisper a Tesseract.js ve WASM. Nativní větev ve Swiftu s MLX prý zkoumá zvlášť. Do toho uživatel cpursley rýpl, proč je to javascriptový moloch místo nativní aplikace či Rustu, na což uživatel collingreen odpověděl, že nic nebrání vydat vlastní fork v Rustu.

Z vlákna tak vychází SCM jako sympaticky soukromý, ale výpočetně náročný koníček: všechno zůstane doma, jen si na to velké videotéky musí vyhradit noc.
