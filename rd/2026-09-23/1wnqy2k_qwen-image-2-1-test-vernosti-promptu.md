# 1wnqy2k

**Qwen-Image-2.1: věrnost promptu je vysoká, uživatelé ale srovnávají s Krea 2**

| | |
|---|---|
| Subreddit | r/StableDiffusion |
| Autor | u/kosovack |
| Publikováno (Europe/Prague) | 23. 9. 2026, 02:30 |
| Skóre / komentáře | 397 / 71 |
| Odkaz | https://www.reddit.com/gallery/1wnqy2k |
| Diskuse | https://www.reddit.com/r/StableDiffusion/comments/1wnqy2k/tried_out_qwenimage21_today_and_the_prompt/ |

## Co se stalo

Uživatel u/kosovack zveřejnil 23. 9. 2026 ve 02:30 (Europe/Prague) v komunitě r/StableDiffusion příspěvek s flairem „Workflow Included“. Tvrdí v něm, že vyzkoušel model Qwen-Image-2.1 a že jeho věrnost promptu (prompt adherence) je neuvěřitelná. Test měl podle autora cílit na surovou, neformální estetiku amatérského snímku z telefonu (raw candid) s dynamickým pozadím — konkrétně na rozmazání pohybem (motion blur) a šum ze slabého osvětlení na nádraží.

K příspěvku autor přiložil kompletní sadu podkladů: model Qwen-Image-2.1, dvě LoRA z Civitai (lenovo-ultrareal a nicegirls-ultrareal), pracovní postup (workflow) pro ComfyUI a texty promptů, obojí na Pastebin. Jde tedy o příspěvek, který se dá reprodukovat, což komunita explicitně ocenila.

Příspěvek vzbudil velký ohlas: 397 bodů, 71 komentářů a poměr kladných hlasů 0,93. V tentýž den na totéž téma navázaly tři další příspěvky: rozsáhlé srovnání Qwen Image 2.1 proti Krea 2 na 192 obrázcích, dotaz, zda se model vůbec vyplatí, a oznámení čtyřkrokové Turbo LoRA od Viggle.

Nutno dodat omezení podkladu: odkaz vede na redditovou galerii (`https://www.reddit.com/gallery/1wnqy2k`), ale samotná galerie v balíčku stažena není. Balíček neobsahuje žádné řádky s přílohou obrázku a extrakce má pole s textem obrázků prázdné, takže vizuální obsah snímků nelze v tomto článku popsat ani posoudit. Rovněž video u navazujícího příspěvku s Turbo LoRA se nestahuje — k dispozici je jen titulek, text a komentáře. Vše, co je níže uvedeno o vzhledu výstupů, je proto tvrzení diskutujících, nikoli zde ověřené pozorování.

## Klíčová fakta

- Hlavní test popisuje sám autor jako zkoušku surové amatérské estetiky telefonního fotoaparátu s dynamickým pozadím. Model: Qwen-Image-2.1. LoRA: lenovo-ultrareal a nicegirls-ultrareal. Workflow a prompty: odkazy na Pastebin.
- Podle komentujícího u/wunderbaba šlo o v podstatě standardní ComfyUI workflow pro převod textu na obrázek (T2I) s modelem Qwen, přesto ocenil, že autor podklady přiložil.
- Komentující u/Apprehensive_Sky892 tvrdí, že autor nahrál PNG soubory s neporušenými metadaty, a odkazuje na návod, jak metadata a workflow z nahraných obrázků získat. Sám uvádí, že to vyzkoušel u prvního obrázku.
- Navazující příspěvek u/dh7net obsahuje srovnání 192 obrázků z Qwen Image 2.1 a 192 obrázků z Krea 2 v galerii na imagebench.ai, roztříděné podle kategorií (generování textu, anatomie člověka a další). Autor uvádí, že musel použít kvantovaný textový encoder (NF4), zatímco denoisač (denoiser) ve verzi BF16 běžel na grafické kartě řady 5090.
- Navazující dotaz u/knhabs přichází od uživatele Krea 2: model mu běží dobře na kartě 5070ti, ale chybí mu skutečné editační schopnosti. Jako řešení používá editaci přes model Phroot QWEN AIO, u níž chválí konzistenci editace (snadné tvorby storyboardů s postavami, zvířaty či auty), ale kritizuje výslednou kvalitu — kůže označuje za plastovou, textury oblečení za falešné, srst zvířat za špatnou a auta za plastové hračky.
- Navazující oznámení u/fruesome přináší čtyřkrokovou Turbo LoRA pro Qwen Image 2.1 od Viggle, s modelem a Space na Hugging Face.

Pro čtenáře je důležité oddělit měření od dojmů. Doložená jsou jen čísla o příspěvcích, počtu obrázků, krocích vzorkování, použitém hardwaru a rozsahu stažených komentářů. Vše, co se týká „věrnosti promptu“ nebo „realističnosti“ výstupů, jsou subjektivní hodnocení jednotlivých diskutujících.

## Čísla

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Skóre hlavního postu | 397 | 1wnqy2k |
| Komentářů u hlavního postu | 71 | 1wnqy2k |
| Poměr kladných hlasů | 0,93 | 1wnqy2k |
| Stažených komentářů / uvedených v balíčku | 44 / 25 | 1wnqy2k |
| Obrázků od každého modelu ve srovnání | 192 | 1wny8w8 |
| Kroků vzorkování v testu uživatele u/kemb0 | 25 (int8) | komentáře |
| Grafická karta u srovnání 192 obrázků | 5090 | 1wny8w8 |
| Grafická karta u uživatele Krea 2 | 5070ti | 1wnq6nb |

| Souhrn navazujících postů | Skóre | Komentářů | Poměr hlasů |
|---|---:|---:|---:|
| Srovnání 192 obrázků Qwen vs Krea 2 | 97 | 63 | 0,92 |
| Dotaz, zda se Qwen Image 2.1 vyplatí | 6 | 47 | 0,58 |
| Turbo LoRA ve 4 krocích od Viggle | 157 | 38 | 0,98 |

Tyto údaje pocházejí z metadat příspěvků zaznamenaných v balíčku. Nejde o měření kvality modelu — vypovídají o pozornosti komunity, ne o výkonu srovnávaných nástrojů. Nízké skóre dotazovacího příspěvku (6 bodů při 47 komentářích a poměru hlasů 0,58) ukazuje spíš na sporné téma než na jednoznačný výsledek.

## Citace

> „Páni, dnes jsem vyzkoušel Qwen 2.1 a věrnost promptu je neuvěřitelná!“ (překlad) — u/kosovack, text hlavního příspěvku

> „Zkouším surovou, neformální estetiku amatérského telefonního fotoaparátu s dynamickým pozadím (rozmazání pohybem, šum ze slabého světla na nádraží).“ (překlad) — u/kosovack, text hlavního příspěvku

> „Bez znalosti promptů se to těžko hodnotí. Obrázky s jednou dívkou jsou ale celkem snadné. Zkusil bych opravdové složité scény s více subjekty a prvky.“ (překlad) — u/TheAncientMillenial, komentář

> „Pro mě se to rychle rozpadá, jakmile se dostanete za instagramovou „jednu dívku“, kterou OP postoval.“ (překlad) — u/tom-dixon, komentář

> „Qwen vypadá mnohem přirozeněji, ale všude glitchuje.“ (překlad) — u/crooi, komentář

> „Textový encoder může výstup výrazně ovlivnit. Nepoužití plného encoderu u Qwenu z toho pravděpodobně dělá nefér srovnání.“ (překlad) — u/Enshitification, komentář k postu o 192 obrázcích

> „Můj hlavní model je krea2. Podle mě byste na změnu ještě neměli skákat, krea má víc LoRA a aspoň u mě rychlejší generování.“ (překlad) — u/kosovack, komentář

> „Takže pro vás, kdo používáte Qwen Image 2.1: vyplatí se? Je kvalita obrázku lepší nebo podobná tomu, co máme u Krea2 a Flux Klein po editaci v Qwen Image 2.1?“ (překlad) — u/knhabs, text navazujícího příspěvku

## Co říkají komentáře

Nejvýše hodnocený komentář (49 bodů) od u/TheAncientMillenial zpochybňuje vypovídací hodnotu testu: bez znalosti promptů se výsledek těžko posuzuje a scény s jednou dívkou jsou snadné. Podobně reagoval u/MistaPlatinum3, který téma „věrnost promptu“ glosoval slovy, že uvnitř najde jen „jednu dívku, sedící/stojící“.

Nejpodrobnější metodickou námitku přidal u/Ok-Fennel6578 (43 bodů). Doporučuje netestovat množství detailů, ale „provázání“ atributů (binding): tři lidé v červené, modré a zelené bundě, každý s jiným předmětem, na pevných pozicích vlevo, uprostřed a vpravo, jedna konkrétní akce na osobu a dva detaily pozadí, které musí také přežít. Instrukce by se měly měnit vždy jen po jedné. Model podle něj může působit velmi věrně u jediného subjektu a přesto selhat, jakmile si musí udržet, komu patří který atribut. Pokud by Qwen 2.1 udržel přiřazení bez záměny oblečení, rekvizit a pozic, byl by to podle komentujícího mnohem silnější výsledek než obvyklý test „složitý prompt = hezký obrázek“.

u/kosovack na kritiku reagoval věcně: doplnil odkazy na prompty. u/Keyflame_ autora žádal, aby příspěvek nesmazal, protože si ho chce vyzkoušet později.

Druhá linie diskuse se týkala samotných LoRA modelů. u/_VirtualCosmos_ poznamenal, že tyto LoRA vypadají dobře bez ohledu na použitý model, a u/FlyingAdHominem jejich autora označil za kouzelníka. To je podstatná výhrada k testu věrnosti: pokud velkou část vizuálního výsledku nese LoRA, nevypovídá snímek primárně o schopnostech základního modelu.

Věcné dotazy směřovaly k náročnosti a srovnatelnosti. u/rguerraf se ptal, kolik času na grafické kartě generování zabere ve srovnání s jinými text-to-image nástroji, zda velikost unet neznamená nižší nároky na paměť a jak si model stojí proti Qwen-2511 image edit. Odpovědi byly částečné: u/kosovack odkázal na prompty v Pastebinu, u/rguerraf sám doplnil, že mnoho LoRA je dostupných na Hugging Face. u/Independent-Reader přišel s návrhem doplnit „refiner“, tedy druhý průchod, a u/Chiduk99 volal po stylové LoRA, protože mu část výstupů připomíná vzhled GPT-image.

U srovnání 192 obrázků se vedle metodické námitky k encoderu objevila i řada hodnocení samotného vzhledu (viz následující oddíl) a praktická poznámka u/kemb0: tělesné chyby (například chybějící nebo zauzlené nohy u sedící postavy) se podle něj dají často opravit prostým doplněním instrukce, například větou, že postava sedí s nohama na podlaze. Sám uvádí, že se mu výsledky s výchozími 25 kroky a režimem int8 líbí víc než u Krea 2.

## Rozpory a neověřené informace

- **Věrnost promptu.** Autor tvrdí, že je „neuvěřitelná“. u/tom-dixon oponuje, že se model rychle rozpadá mimo styl jednoduchých snímků s jednou dívkou, a u/MistaPlatinum3 test ironizuje jako triviální. Jde o dva protichůdné subjektivní dojmy bez společné metriky.
- **Vypovídací hodnota srovnání 192 obrázků.** u/MastMaithun a u/crooi tvrdí, že Qwen vypadá realističtěji, u/ArkCoon a u/TheAncientMillenial naopak, že srovnání nic takového nedokazuje, protože Krea 2 potřebuje jiné stylové vedení promptu a ideálně LoRA, aby svůj realismus ukázala. u/TheAncientMillenial navíc uvádí, že srovnávání stejného promptu napříč modely už podle něj není vypovídající.
- **Kvantovaný encoder.** u/Enshitification označuje postup s kvantovaným textovým encoderem NF4 za nefér srovnání. Autor srovnání sám přiznává, že kvantizaci musel použít, aniž by vysvětlil, proč. To je neověřené tvrzení o vlivu na výsledek, nikoli doložené měření.
- **Metadata v PNG.** u/Apprehensive_Sky892 tvrdí, že nahrané obrázky nesou neporušená metadata a workflow. Toto tvrzení není v balíčku doloženo a autor příspěvku je nepotvrdil ani nevyvrátil.
- **Chování při změně oblečení.** u/SelectCoconut5594 uvádí osobní zkušenost, že si model vícenásobné pózy v charakterovém listu se změnou oblečení neporadil. Jde o jeden neověřený zážitek.
- **Kvalita po editaci.** u/knhabs popisuje Krea2 identity edit jako „ne skutečný editační model“ a výstupy editace přes Phroot QWEN AIO jako plastové. Obě tvrzení vycházejí z jeho vlastní praxe a nejsou v podkladu doložena.
- **Realističnost jako vlastnost modelu.** Hodnocení „přirozenější“, „plastový“ nebo „kreslený“ jsou dojmy jednotlivých uživatelů, nikoli výsledky měření. Snímky samotné nejsou v podkladu k dispozici, takže je nelze ověřit.

## Další diskuse

| id | subreddit | skóre | komentářů | čas | přeložený titulek | permalink |
|---|---|---:|---:|---|---|---|
| 1wny8w8 | r/StableDiffusion | 97 | 63 | 08:34 | 192 vygenerovaných obrázků vedle sebe: Qwen Image 2.1 vs Krea 2 | https://www.reddit.com/r/StableDiffusion/comments/1wny8w8/192_generated_image_side_by_side_qwen_image_21_vs/ |
| 1wnq6nb | r/StableDiffusion | 6 | 47 | 01:58 | Vyplatí se Qwen Image 2.1? | https://www.reddit.com/r/StableDiffusion/comments/1wnq6nb/is_qwen_image_21_worth_it/ |
| 1wo6d82 | r/StableDiffusion | 157 | 38 | 15:42 | Čtyřkroková Turbo LoRA pro Qwen Image 2.1 je tu od Viggle | https://www.reddit.com/r/StableDiffusion/comments/1wo6d82/qwen_image_21_4_steps_turbo_lora_is_here_by_viggle/ |

První z navazujících příspěvků (u/dh7net) posouvá diskusi od dojmů k pokusu o rozsáhlejší srovnání: 192 obrázků na model, roztříděných podle kategorií, s odkazem na veřejnou galerii. Právě u něj se ale objevily nejostřejší metodické výhrady — ke kvantovanému encoderu i k tomu, že srovnání nezohledňuje potřebu odlišného vedení promptu u Krea 2.

Druhý příspěvek (u/knhabs) přináší pohled praktického uživatele, který řeší kombinaci generování a editace: spokojenost s Krea 2 při generování proti nespokojenosti s kvalitou po editaci v jiném modelu. Ptá se proto, zda Qwen Image 2.1 nabízí kvalitu srovnatelnou s Krea2 nebo Flux Klein. Komentáře k tomuto příspěvku nebyly do balíčku staženy, takže odpovědi komunity k němu nemáme k dispozici — stejně jako u třetího příspěvku.

Třetí příspěvek (u/fruesome) je oznámení čtyřkrokové Turbo LoRA od Viggle s modelem a Space na Hugging Face. Dosáhl poměru kladných hlasů 0,98, tedy nejvyššího ze všech čtyř sledovaných příspěvků. Také u něj platí, že komentáře nebyly staženy a že odkazované video není v podkladu dostupné.

## Proč to je důležité

Diskuse je užitečná jako příklad toho, jak rychle se z osobního dojmu stane zdánlivý fakt. Hlavní příspěvek obsahuje reprodukovatelné podklady — workflow i prompty — což je nadstandard; i tak v něm ale chybí srovnávací základna a test omezený na jeden typ výstupu. Komentáře tuto mezeru přesně pojmenovávají a nabízejí konkrétnější metodiku: testovat přiřazení atributů k subjektům, měnit vždy jen jednu instrukci a přiznat vliv LoRA na výsledek.

Zároveň se ukazuje, že volba mezi Qwen Image 2.1, Krea 2 a Flux Klein není jen otázkou „kdo je lepší“, ale kombinace několika praktických faktorů: dostupnost LoRA, rychlost generování, nároky na hardware a schopnost editace. Autor hlavního příspěvku sám opakovaně uvádí, že jeho hlavním modelem zůstává Krea 2 a že na změnu zatím není důvod spěchat. To je pozoruhodné právě proto, že jeho vlastní test vznikl na obhajobu opačného modelu.

Pro každého, kdo zvažuje nasazení modelu, z toho plyne střízlivý závěr: doložená jsou čísla o ohlasu příspěvků a rozsah srovnání, nikoli nadřazenost jednoho modelu. Rozhodující budou vlastní testy na vlastním typu úlohy — tedy přesně to, co navrhoval komentář s vícenásobnými subjekty a pevnými pozicemi.

## Zdroje

- Balíček: `2026-09-23/_data/bundles/1wnqy2k.md`
- Extrakce: `2026-09-23/_data/extracts/1wnqy2k.json`
- Hlavní diskuse: https://www.reddit.com/r/StableDiffusion/comments/1wnqy2k/tried_out_qwenimage21_today_and_the_prompt/
- Galerie k hlavnímu příspěvku: https://www.reddit.com/gallery/1wnqy2k
- Workflow autora: https://pastebin.com/YE3ZXYEq
- Prompty autora: https://pastebin.com/kYzviaES
- LoRA lenovo-ultrareal: https://civitai.red/models/1662740/lenovo-ultrareal?modelVersionId=3349565
- LoRA nicegirls-ultrareal: https://civitai.red/models/1862761/nicegirls-ultrareal?modelVersionId=3349686
- Srovnání 192 obrázků: https://www.reddit.com/r/StableDiffusion/comments/1wny8w8/192_generated_image_side_by_side_qwen_image_21_vs/
- Galerie srovnání: https://imagebench.ai/gallery?g=1_vxj22_s0
- Dotaz na vyplatitelnost modelu: https://www.reddit.com/r/StableDiffusion/comments/1wnq6nb/is_qwen_image_21_worth_it/
- Turbo LoRA ve 4 krocích: https://www.reddit.com/r/StableDiffusion/comments/1wo6d82/qwen_image_21_4_steps_turbo_lora_is_here_by_viggle/
- Model Turbo LoRA: https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/tree/main
- Space Turbo LoRA: https://huggingface.co/spaces/Viggle/Qwen-Image-2.1-viggle-turbo
