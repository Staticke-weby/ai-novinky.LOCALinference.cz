# 1y6evzy
**Dva měsíce s Qwen 3.8 27B: lokální model stačí na 80 % práce**

r/LocalLLaMA · u/forevergeeks · 27. listopadu 2026, 00:41 · 255 bodů / 157 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y6evzy/)

Autor používá Qwen 3.8 27B už přes dva měsíce na správu systému, kód, kyberbezpečnost i studium Bible a zhruba 80 % veškeré práce s umělou inteligencí dnes zvládne lokálně. Zbytek dělí mezi předplatná Google Pro a Z.ai. Model je podle něj zhruba na úrovni, kde byl Claude na jaře letošního roku v době vydání Claude 4.8, a hustý model Meta Muse Glimmer 30B se mu v jeho testech ani nepřiblížil. Stejně jako většina vlákna teď čeká, co přinese Qwen 4 27B.

Nejvíc hlasů dostala rada od u/grabber4321, ať zkusí Qwen 3.8 Flash-Next, protože rozdíl je prý obrovský. Sám na něm staví pracovní postup pro návrh webů, kdy model staví stránky ve FigCraft a vyrábí vlastní šablonu pro WordPress, a spojení OpenCode a QFN shrnuje krátce jako lásku. Přidává se u/108er, který byl s klasickou sedmadvacítkou stejně nadšený a po přechodu na QFN se Strata prý nemusel na čtyřku vůbec čekat, a u/alcoa29 jen suše dodává, že QFN je lepší a znatelně rychlejší.

Vedlejší linka se točí kolem bezpečnosti. u/looselyhuman označuje model za skvělý a popisuje, že jeden z jeho dvou agentů s 3.8 27B hlídá domácí laboratoř. Zároveň se bojí, že na Qwen 4 nebude moct přejít, protože z trénovacích dat prý mizí kyberbezpečnostní obsah, a už zvažuje trénink LoRA adaptéru, který by slovní zásobu vrátil. I kdyby ale zůstal na verzi 3.8, vůbec by mu to nevadilo. Praktický dovětek přidává u/Mission_Wrongdoer786, podle kterého model ještě víc pozvedne dobré okolí v podobě dovedností a pracovních postupů.

Třetí proud diskuse řeší hardware a peníze. u/Remarkable_Air_8383 a u/eagle2809 se ptají na kvantizaci, délku kontextu a pořizovací i provozní náklady, tedy jestli se lokální provoz vedle placeného Clauda vůbec vyplatí. Nejpodrobněji odpovídá u/SergeOrl, který po zkoušení různých sestavení zakotvil u dynamické verze Unsloth Q4_K_XL se stejnou spotřebou zdrojů a nejlepším výkonem na reálných úkolech, běží na 64 GB RAM s mobilní RTX 5090 a kontextem 120 tisíc tokenů a popisuje i ladění vzorkování a odlehčení cache kvůli stabilitě. Kontrast přidává u/Designer_Mix_3336, jemuž byl model na Mac Studiu s M1 Max ještě pomalý, ale od příchodu M5 Ultra začátkem měsíce se stal každodenním pomocníkem s rychlostí kolem 50 až 100 tokenů za sekundu včetně skriptování.

Pobavení obstarala zmínka o studiu Bible. u/WingsOfGryphin reaguje překvapeným zdvižením obočí a u/letmeinfornow se ptá, jestli autor kvůli čínskému původu modelu nenarazil na omezení. Mezi vážnějšími hlasy zaznívá i střízlivost: u/NegotiationPrior4373 používá model na první průchod kódem, který pak čistí Claude, a u/a_beautiful_rhind má dobré zkušenosti i s DS4-flash-vision a GLM-5.3-Flash a těší ho, že bezplatné lokální modely nekončí u staré generace Llama 3.

Z vlákna tak vychází prostý vzkaz: dobře vyladěná lokální sedmadvacítka dnes unese většinu každodenní práce a nejtěžší otázkou už není jestli, ale na čem ji provozovat.
