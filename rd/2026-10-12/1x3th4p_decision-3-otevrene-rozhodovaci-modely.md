# 1x3th4p
**Decision 3.0: otevřené multimodální rozhodovací modely od 0,6B do 27B**

r/LocalLLaMA · u/henzy123 · 12. října 2026, 07:26 · 521 bodů / 104 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x3th4p/)

Tým vLLM Semantic Router vydal novou generaci svých rozhodovacích modelů Decision 3.0, zkráceně d3. Jde o otevřenou rodinu od 0,6B do 27B pod licencí Apache-2.0, která umí číst text, obrázky i video, a autor ji v r/LocalLLaMA představil s flairem New Model i s odkazem na kolekci na Hugging Face.

Základem jsou modely Qwen3.5 u variant 0,8B, 2B, 4B a 9B a Qwen3.8-27B u největší verze, přičemž udávané počty parametrů zahrnují i vision enkodér – 0,33B u 4B modelu a 0,46B u 27B modelu. Místo generování textu řeší d3 jen tři typy rozhodnutí – volbu z možností, odpověď ano/ne a číselné skóre – a ke každé odpovědi vrací pravděpodobnost. Několik otázek ke stejnému vstupu vyřídí v jednom volání, každou vlastním průchodem přes vstup. Váhy jsou v BF16, načítají se přes Transformers s trust_remote_code=True a trénink běžel na AMD Instinct MI325X.

Obrazové vstupy zvládne po několika v jednom požadavku v rozlišení do 1,6 MP, video ve formátech MP4, WebM, MOV a MKV vzorkuje rychlostí 2 snímky za sekundu, nejvýše 32 snímků na klip, každý do 0,2 MP. Podle vlastního měření autora oficiální sadou Jev 0.3 na vydaných vahách vede největší 27B model obě tabulky se skóre 64,7 v textu a 71,6 ve vision části před všemi uvedenými modely včetně modelů od tvůrců Jevu. Každá velikost 0,6B, 0,8B, 4B a 9B vede svou velikostní kategorii a 9B varianta s přízviskem d3-flash překonává 27B model předchozí generace Decision 2.0. Zajímavý je výsledek na videu, které žádný model při tréninku neviděl: na všech 19 140 validačních otázkách Perception Testu dává 27B model zero-shot 77,4 a 4B model 70,3.

Pro lokální nasazení je to lákavá volba všude tam, kde místo ukecaného chatbotu stačí rychlá a kalibrovaná odpověď s pravděpodobností – třídění, směrování požadavků nebo hodnocení výstupů jiných modelů.
