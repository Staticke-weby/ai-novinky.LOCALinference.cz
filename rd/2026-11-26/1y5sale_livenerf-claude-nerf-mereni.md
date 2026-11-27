# 1y5sale
**LiveNerf: 63 dní měření, jestli Claude po launchi slábne**

r/ClaudeAI · u/TheOnlyVibemaster · 26. listopadu 2026, 05:51 · 315 bodů / 59 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1y5sale/)

Autor projektu LiveNerf už přes dva měsíce bez vynechání každý den zkouší Opus 5.5 a Fable 5.2 na stejných 78 otázkách z GPQA Diamond, MMLU-Pro, soutěžní matematiky a AIME. Prompty i hodnotitelé má zamčené, verze Claude Code připnuté a metodiku předregistrovanou, aby šlo poznat, jestli model po uvedení skutečně slábne. U Opusu 5.5 přitom žádný jasný pokles nevidí: startoval na 58,4 %, ve dnech 11–20 měl 59,2 % a poslední dokončené desetidenní okno bylo dokonce nejsilnější ze všech. Celý projekt je open source na GitHubu a má sloužit jako protiváha dojmům o potichém „nerfování“ modelů.

Právě citlivost testu se stala největším tématem diskuse. Nejvýše hodnocený dotaz u/Active-Season5521 rýpe, jestli to není ten nástroj, který předtím nedokázal rozlišit různé verze Opusu, a u/ShadowBannedAugustus se ptá, zda už dnes pozná Opus 5 od Opusu 5.5. Obránci v čele s u/Muhlwa_Sholanke namítají, že na začátku bylo málo dat a že dva měsíce zmrazené metodiky bijí dojmy, zvlášť když je poslední desetidenní okno rekordní. Praktický test citlivosti navrhuje u/Few-Divide1870: schválně pustit benchmark na nižší úroveň úsilí a sledovat, jestli se graf vůbec pohne.

Druhá linka je klasický souboj dat a pocitů. u/WillGrindForXP píše, že datům věří, ale bijí se s jeho zkušeností – Claude mu prý opakovaně během stejného workflow „zhloupnul“ tak, že musel práci na pár dní odložit, a pokaždé do pár dnů vyšel nový model. Podobně u/EconomistMuted6987 podotýká, že benchmark je jedna věc a hodiny práce na reálném kódu věc druhá. Odpověď statistiků přináší u/weird__guy: 78 otázek je malý vzorek, při úspěšnosti kolem 60 % má jeden běh chybu asi 5,5 bodu, takže rozdíl 58,4 proti 61,7 je pořád šum, a pomohlo by každou otázku pouštět víckrát denně nebo rotovat větší pool.

Třetí debata řeší, jak by k případnému zhoršení vůbec došlo a jak ho lépe zachytit. u/JaggedTex tvrdí, že celé „nerfování“ mu nedává smysl, protože ubrání výpočetního výkonu by model jen zpomalilo, nikoli zblblo – inteligenci by změnila jen úprava vah. Na to ostatní odpovídají, že cest je víc, od kvantizace přes směrování až po systémové pokyny. Proto u/South_Hat6094 radí logovat i region, tarif a feature flagy, protože pevná sada úloh ukáže drift, ale nevyloučí směrování pro vybrané skupiny, a u/wwdennis5 přidává sledování spotřeby tokenů a ceny jako signál tichého testování další verze.

Z měření si tak čtenář odnáší hlavně klid a otazník zároveň: Opus 5.5 zatím podle pevného testu neslábne, ale úzký benchmark nemůže vyloučit změny, které prostě nejsou vidět na 78 otázkách.
