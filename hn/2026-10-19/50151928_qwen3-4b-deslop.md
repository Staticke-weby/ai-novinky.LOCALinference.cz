# 50151928
**Qwen3-4B bez AI frází: model, který se naučil psát lidsky**

Hacker News · erikkannike · 19. října 2026, 15:00 · 146 bodů / 108 komentářů · [diskuse](https://news.ycombinator.com/item?id=50151928)

Erik Kannike doladil Qwen3-4B-Instruct a vydal ho pod jménem qwen3-4b-deslop, aby model přestal psát typickým asistentím stylem. Kvantovaná GGUF verze má 2,5 GB a spouští se přes Ollama jedním příkazem.

Na 40 promptech, které model při tréninku neviděl, kleslo autorem měřené „slop score" ze 121 na 12,5 na 1000 slov a 68 % odpovědí spadá do pásma lidského psaní. Používání pomlček typu em dash spadlo z 20,5 na nulu na 1000 slov, přitom model dál správně odpovídá na 30 z 30 faktických otázek a žánr i délku drží podobně jako originál.

Neživější úvodní debata se ale netýkala modelu, nýbrž webu. Čtenáře rozptylovaly cizí kurzory pohybující se po stránce, anilgulecha se ptal, o co jde, a RonanSoleste si stěžoval, že kvůli pocitu sledování stránku zavřel před koncem prvního bloku. Sám autor erikkannike se omluvil, že šlo o jeho experiment s WebRTC a knihovnou Trystero, který nečekaně potkal nápor z Hacker News, a kurzory přepnul na vypnuté ve výchozím stavu.

Pak se diskuse vrátila k samotnému psaní. chmod775 to popsal obrazem, že jako by všechny knihy na světě napsalo jen pět lidí, kteří si navíc nepamatují, co psali včera, takže se člověk rychle unaví stále stejnými kudrlinkami. Royce-CMR autorovi zatleskal, ale upozornil, že vyčištěná verze jeho příkladu s novým firemním CRM působí jako rozvláčný text mileniála, zatímco „slop" verze vypadá jako návrh, který by mohl poslat manažerům, takže každý styl má jiné ideální použití. Skeptičtější hlasy dodávají, že výstup je pořád poznatelně strojový a špatně se čte, mrweasel si stěžuje, že se musí neustále vracet o větu zpět, protože text se mu prostě neukládá do hlavy.

Řešila se i detektivní práce na úrovni jednotlivých frází. bschwarz si rýpl, že věta „and needs no system prompt" je sama ukázkou strojenosti a člověk by napsal „and doesn't need a system prompt". V odpovědích se ale ozvalo, že člověk by klidně mohl napsat obojí, jen druhé je formálnější a stručnější, a bityard přiznal, že po nástupu ChatGPT svůj dřívější formální styl záměrně uvolnil, protože se bál, že ho budou mít za bota.

Nakonec se přeli i o to, jestli takový model vůbec chtít. f311a se ptal, proč podobné projekty podporovat, když by text od jazykových modelů měl zůstat co nejdéle rozpoznatelný, jinak prý zahyne lidská komunikace na internetu. Proti tomu dofm hájil méně otravný automaticky generovaný text i asistivní použití, třeba převod znakového jazyka do řeči, kde si uživatelé zaslouží přirozený a osobní projev. Mezitím BoredomIsFun připomněl staršího průkopníka, antislop verzi Gemma 3 27B od sam-paech, a uživatel 10111001 si z celé snahy utáhl v opačném směru a žádal model s AI zlozvyky vytočenými na maximum, aby šéf viděl, že je hodný kluk a umělou inteligenci používá.

Z vlákna tak zůstává dojem, že zbavit se pomlček a „delve" je ta snazší část, těžší je trefit hlas, který se dobře čte a hodí se pro danou situaci.
