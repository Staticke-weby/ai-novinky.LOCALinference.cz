# 1y1c950
**Minimax H3 zvládá nativní úpravy videa. Komunita testuje i 48megapixelové výstupy**

r/StableDiffusion · u/smereces · 20. listopadu 2026, 20:19 · 322 bodů / 51 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1y1c950/)

Minimax H3 umí nativně upravovat video a měnit v něm postavy jen pomocí textového zadání. Uživatel ukázal edit, který řídí jazykový model a k samotné úpravě stačí turbo LoRA na osmi krocích. Výsledek drží původní pózu i pohyb, zatímco oblečení a identita postavy se kompletně přepíšou.

Klíčový trik popsal v diskusi u/roychodraws: stačí promptování a latentní maskování, žádné Viggle ani swapovací LoRA. Na GitHubu zveřejnil workflow i ukázku zadání, kde dospělou ženu s růžovou parukou, klaunským nosem a korzetovými šaty definuje jako náhradu za velkého obrněného záporáka z původního videa. Druhý subjekt, malá kreslená kočičí dívka se žlutýma ušima, pak ukazuje, že stejným způsobem jde do scény dosadit i zcela stylizovanou postavu.

Právě jednoduchost ale naráží na výdrž. Uživatel u/whoisxx píše, že při pokusech o převod podle referenčního videa se mu vracel stále stejný výstup, a z padesáti generací považoval za povedené jen dvě. Sám autor vlákna u/smereces slibuje, že svůj postup teprve přidá na GitHub a Patreon, a část lidí se proto ptá, kterou z mnoha turbo LoRA vlastně používá.

Zkušenější testeři upřesňují, kdy výměna funguje. Uživatel u/Suibeam tvrdí, že swap je snadný, dokud je anatomie jasná a člověk se moc neplete do prostředí a ostatních lidí, jako protipříklad uvádí wrestling. Na to navazuje u/Jamsemillia s postřehem, že vzhled musí být dost odlišný, ale silueta podobná, jinak se model rychle zadrhne a jemné změny postavy odmítá. Uživatel u/RianCoff si naopak všímá, že póza, telefon, hrnek na kávu i sloupy za postavou zůstávají zamčené, zatímco postava se mění, a zajímá ho, jestli osmikroková verze udrží i rychlejší pohyb.

Do debaty se vrátila i známá citlivá otázka. Uživatel u/NoHopeHubert se oklikou ptá, jestli model zvládne i „tyhle“ videa se skutečnými lidmi, zatímco u/Aaron_rowe81 připomíná civilnější využití, tedy přepis nápisů nebo dialogů při jinak stabilním záběru. Stranou přitom nezůstávají ani statické obrázky: jeden z autorů v navazující diskusi ukázal, že H3 zvládne přímo 48megapixelový výstup bez upscaleru.

Z vlákna tak vychází H3 jako překvapivě schopný, ale vrtkavý nástroj na výměnu postav: když sedí silueta a scéna je klidná, drží pozadí i rekvizity, ve složitých interakcích a při sériové výrobě ale zatím hodně záleží na štěstí při generování.

---

**Další diskuse:**

- [r/StableDiffusion – 232 bodů, 71 komentářů](https://www.reddit.com/r/StableDiffusion/comments/1y11q2d/)

[Zpět na index](00-index.md)
