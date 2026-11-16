# 1x1ldef
**Qwen-Image-2.1-Turbo: generování obrázků v 8 krocích**

r/LocalLLaMA · u/chocofoxy · 9. října 2026, 15:28 · 459 bodů / 105 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x1ldef/)

Na r/LocalLLaMA se objevil odkaz na Hugging Face s novým checkpointem Qwen-Image-2.1-Turbo. Jde o zrychlenou verzi modelu Qwen-Image-2.1 pro generování obrázků z textu i jejich úpravy, která si vystačí s osmi denoising kroky. Váhy jsou otevřené a příspěvek nese označení New Model.

Podle karty modelu využívá stejnou 7B architekturu a načítá se přímo přes QwenImage21Pipeline v Diffusers. Doporučený rozvrh vzorkování je uložený přímo v checkpointu, takže není potřeba ručně nastavovat scheduler. Výchozí generování počítá s CFG=1 a prefix KV caching znovu využívá kontext textu i referenčního obrázku napříč kroky.

Nejvíc hlasů dostala praktická otázka u/Repulsive_Initial308, jak to celé nejjednodušeji spustit lokálně, ideálně bez skládání třiceti krabiček před výstupní krabičkou. u/Payne6t6 odpověděl, že pro něj je nejjednodušší stable-diffusion.cpp, a u/No_Establishment2918 přihodil odkaz na imagegen-mac. Do stejné linky zapadá i povzdech u/geldonyetich, že pro novinku zatím není workflow pro ComfyUI, a popis zmatků kolem hledání složky s workflow, zatímco u/StopCreepy volá po verzi ve FP8 a u/Steuern_Runter se ptá na nejrychlejší kvantizaci pro kartu s 24 GB.

Druhá velká linka řeší, v čem je Turbo vlastně jiné. u/Jigawattts se ptá prostě na rozdíl proti verzi 2.1 a u/YoinkedGaming dodává, jaký je rozdíl proti turbo LoRA hlavního modelu. Věcnou odpověď nabízí u/Open-Adhesiveness-86: osm kroků se vyplatí jen s vypnutým vedením, protože destilované checkpointy ho mají zapečené v sobě a vyšší CFG znamená dva průchody na krok i vypraný kontrast. Dodává, že LoRA trénované na základní verzi 2.1 při osmi krocích často přeženou výsledek a váhu je potřeba stáhnout zhruba na 0,6. Na to navazuje i u/No_Algae1753, kterému při CFG 1 model špatně poslouchá instrukce a neví, jestli musí zůstat u hodnoty kolem 6.

Okolo toho se mísí nadšení s vtipy. u/barbear22 píše, že tím se Qwen vykoupil, základ byl skvělý, ale tohle je prý doslova šéfkuchařův polibek, zatímco u/ihexx kontruje, že základ už byl rychlý až dost. u/Sabin_Stargem si počká na necenzurovanou verzi kvůli zvrhlým kočičím dívkám a u/Elouakili_Flexy předpovídá, že do pondělí někdo rozjede necenzurované turbo workflow pro kočičí dívky v ComfyUI. Nejstřízlivější hlas patří u/bugra_sa: novinku by netestoval na jednom hezkém obrázku, ale na deseti opakovaných úpravách a počítal by, jak často zmizí dřívější detail.

Pro čtenáře z toho plyne jednoduché ponaučení: rychlost osmi kroků dává smysl, jen když se k ní správně nastaví vedení a otestuje se na delší editační práci, ne na jedné ukázce.
