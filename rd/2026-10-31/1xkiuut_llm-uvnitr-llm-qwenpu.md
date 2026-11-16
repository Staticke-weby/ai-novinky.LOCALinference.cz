# 1xkiuut
**LLM uvnitř LLM: QwenPU spouští stories260k ve vlastních vahách**

r/LocalLLaMA · u/LatentSpacer · 31. října 2026, 20:18 · 223 bodů / 49 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xkiuut/)

Uvnitř vah modelu Qwen 3.5-4B běží další samostatný jazykový model. Projekt QwenPU tam spouští stories260k, drobný model od Karpathyho, přičemž jeho váhy leží přímo v paměti Qwenu a obejde se bez jakýchkoliv externích nástrojů. Jde o další kousek stejného autora, který už dřív do vah Qwenu vestavěl procesor RISC-V.

Podle autorova popisu je stories260k v podstatě jen program v céčku, a aby mohl běžet uvnitř hostitelského modelu, zkompiloval autor do jeho vah vlastní NPU. To bitově přesně počítá maticové násobení, softmax i attention. Kód projektu je na GitHubu a váhy na Hugging Face, na rychlosti si dal autor hodně záležet. Plný popis ale zatím odložil, protože je nemocný, a slibuje, že blog s detaily a další optimalizace dopíše, jakmile se uzdraví.

Diskuse se okamžitě stočila k vtipům o zanoření. Nejvíc bodů posbíralo suché u/some_user_2021 se hláškou o tom, že slyšel, že máš rád jazykové modely, a přidávají se u/Manerfish s rekurzivními modely, u/FBIFreezeNow s verzí Inceptionu i u/ChocolateNo3010 s LLM inceptionem. Do stejné noty hrají i u/Dreeew84, podle kterého se obecná umělá inteligence odemkne při páté iteraci tohohle, a u/vogelvogelvogelvogel, který tipuje, že autor za další dva příspěvky objeví rekurzivní sebezdokonalování dřív než Anthropic.

Vedle toho se mísí úžas s mírnou bezradností. u/Imatros přiznává, že slovům rozumí, ale smysl mu uniká, a proto si připadá jako naprostý amatér. u/Jacalyn_Nivins to shrnuje poznámkou, že váhy jsou teď zároveň data, instrukce i hardware, takže už jen čeká, až na nich někdo rozběhne Doom. Stejné přání opakují u/_VirtualCosmos_ i u/toiletman74, zatímco u/GenChadT celou věc glosuje jen pobaveným oslovením známým z memu o Xzibitovi.

Vážnější linka řeší, jak je to vůbec možné a k čemu to je. u/anthropicagiuser se ptá, jak autor udrží vnitřní váhy bitově přesné, když sedí uvnitř paměti vnějšího modelu, a u/Serious-Regular připomíná předchozí procesor z jedenácti transformerových vrstev před vlastními vrstvami Qwenu a zajímá ho, čím se to liší od obyčejného spuštění procesoru bokem. u/Dorkits se jako nováček ptá prostě proč, u/hainesk tuší, že se to jednou dá nějak zneužít, a u/mycall kontruje, že lokální modely už nikdo nezastaví. Budoucnost s modely natvrdo zapečenými do čipů na míru skicuje u/CipherWeaver, jenže k tomu by se podle něj modely musely na chvíli přestat zlepšovat.
