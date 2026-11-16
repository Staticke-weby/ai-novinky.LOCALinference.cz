# 1xj9w8d
**Diffusion model běží na Game Boy Color. Obrázek počítá 85 sekund**

r/StableDiffusion · u/ready-eddy · 30. října 2026, 09:35 · 919 bodů / 71 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xj9w8d/)

Na handheldu z roku 1998 běží skutečný diffusion model. Po stisku tlačítka A se na vlastním 8MHz procesoru Game Boy Color rozjede 16 kroků a z čistého šumu se zhruba za 85 sekund vykreslí jednoduchá kresba, bez připojeného počítače a bez streamování. Srdcem je MLP denoiser 784 → 512 → 512 → 784 s 1,08 milionu parametrů v int8 vahách a 4bitových aktivacích, trénovaný na 880 tisících obrázcích z Quick, Draw! v osmi třídách po 110 tisících kresbách – 2MB ROM zabírají skoro celé právě váhy.

Autor musel obejít i to, že procesor neumí násobit. Každé násobení nahrazuje dvojice vyhledávání v 24KB tabulce v operační paměti, což dává asi 18 strojových cyklů na jednu operaci, celkem kolem 8,8 milionu operací na obrázek. Trénování přitom přesně napodobuje celočíselnou matematiku konzole a emulátor po každém ze 16 kroků sedí s Python verzí bit po bitu pro všech osm kategorií.

Nejvýše hodnocená reakce z toho udělala nový měřítko odvahy. Uživatel u/Enshitification napsal, že diffusion bude nový Doom test pro zařízení, která na diffusion nemají co mít, a u/DonKeehot hned vyhlásil výzvu, zda to spustí diffusion. Uživatel u/VTPunk připomněl, jak lidé dostávali Doom na stále jednodušší hardware, až se prý zobrazil na bakteriích E. coli.

Vedle toho se nese vlna upřímného úžasu nad množstvím práce. Uživatel u/Ok_Top_2319 přiznává, že si rozsah úsilí ani nedokáže představit, a píše o pocitu, jako by znovu viděl zrození první generace Stable Diffusion, s nadějí na úsvit doby, kdy stabilní diffusion poběží na čemkoliv. Uživatel u/PxTicks autora škádlí, ať teď vytvoří hratelný world model, zatímco u/Incognit0ErgoSum poznamenává, že specifikace Game Boy Color zhruba odpovídají domácím počítačům z osmdesátých let, a ptá se, kolik výpočtů spolklo trénování.

Technická debata se rychle stočila k násobení. Uživatel u/NineThreeTilNow navrhuje, že s váhami kolem 2,5 bitu by násobení nebylo potřeba vůbec a stačilo by sčítání a bitové posuny. Humor obstaral u/Dahvikiin hláškou, že on stejně jako procesor neumí násobit, u/crystal_alpine nabídkou práce v Comfy a u/Rogerooo poznámkou, že jde konečně o diffusion řešení, které si může dovolit, jen by ho zajímala klasická zakázka na dívku na trávě v 8k. Uživatel u/MessageSelfdestructs to shrnul za mnohé, když projekt pochválil jako k ničemu nepoužitelný, ale skvělý právě proto, že odpovídá na otázku, zda by to fungovalo.

Zůstává obrázek jablka, které občas zůstane otevřené, a ryby, která se občas rozpadne – ale vzniká z šumu na kapesní konzoli staré skoro tři dekády, a to diskusi stačí k nadšení.
