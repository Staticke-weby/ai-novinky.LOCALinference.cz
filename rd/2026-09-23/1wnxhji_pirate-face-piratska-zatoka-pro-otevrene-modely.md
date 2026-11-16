# 1wnxhji

**Pirate Face: pirátská zátoka pro otevřené modely**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Atagor |
| Publikováno (Europe/Prague) | 23. 9. 2026, 07:50 |
| Skóre / komentáře | 865 / 122 |
| Odkaz | https://pirateface.co/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wnxhji/pirate_face_pirate_bay_for_llms/ |

## Co se stalo

Dne 23. 9. 2026 v 07:50 (Europe/Prague) zveřejnil uživatel u/Atagor v subredditu r/LocalLLaMA příspěvek s titulem „Pirate Face - pirate bay for LLMs" a s flairem „Resources". Příspěvek není samostatný text, ale odkaz na web https://pirateface.co/, přičemž poměr kladných hlasů dosáhl 0,92 a pod ním se sešlo 122 komentářů.

Vlastní text příspěvku byl krátký. Autor v něm uvedl, že název mluví za vše a že smyslem je mít alternativu pro případ, kdyby někdo cenzuroval Hugging Face. Po vlně reakcí příspěvek upravil a doplnil tři body: není autorem služby; kdyby autorem byl, slovo „piracy" (pirátství) by nepoužil; a pokud je autorem někdo jiný, měl by doménu přejmenovat — co je od počátku svobodné, má se tak i jmenovat, protože se tu nic nepirátí.

Samotná služba Pirate Face se prezentuje jako decentralizovaná infrastruktura pro „suverénní AI". Otevřené modely — jazykové, obrazové, zvukové i datasety — převádí na magnetické odkazy ve formě torrentů a drží je peer-to-peer distribuovaně místo u jediné společnosti. Web stojí na třech pilířích: odolnost proti cenzuře, ověřování kontrolních součtů a plánované „drop-in" API. U odolnosti proti cenzuře web ukazuje scénář, kdy je model na Hugging Face odstraněn a přenos se přesune na peer-to-peer síť; u ověřování uvádí, že každý soubor nese oficiální haš SHA-256 z Hugging Face, takže si každý bajt může uživatel ověřit sám.

Výpis na webu zahrnuje podle vlastního tvrzení více než 669 tisíc způsobilých modelů a sekci s aktuálně trendujícími modely pod licencí Apache-2.0 a MIT. Služba nabízí také rezervaci veřejných přezdívek ve tvaru pirateface.co/jmeno, ověřený odznak pro tvůrce, kteří prokáží shodu s účtem na Hugging Face, a bodový systém za doporučení a za „zachráněné" modely. Procházení, stahování i seedování jsou podle webu možné i bez účtu.

## Klíčová fakta

- **Torrent jako záloha, ne hostování.** Model je magnetický odkaz s takzvaným web-seedem — obyčejnou HTTPS adresou na soubor téhož modelu u Hugging Face (specifikace BitTorrent BEP-19). Dokud je model dostupný, stahuje se přímo odtud; když zmizí, web-seed přestane fungovat a přenos převezme peer-to-peer síť. Takový model web označí jako zachráněný (Rescued).
- **Ověřování kontrolních součtů.** Každý soubor s váhami nese oficiální haš SHA-256 z Hugging Face, takže stažená kopie musí bit po bitu odpovídat originálu; web to popisuje jako ochranu před podvrženým obsahem.
- **Plánované API pro přímé zapojení (drop-in API).** Stačí prý nastavit proměnnou `HF_ENDPOINT` na adresu https://pirateface.co a stávající pipeline začne modely řešit přes Pirate Face — stejné cesty, stejné API, bez změny kódu. Funkce je na webu označená jako „soon", tedy dosud nespuštěná.
- **Přezdívky a ověření identity.** Jméno si může rezervovat kdokoli, odznak ověřeného tvůrce ale získá jen ten, kdo prokáže kontrolu nad odpovídajícím účtem na Hugging Face. Účet `john123` tak ověří přezdívku `john123`, ne `john`; skutečný vlastník může rezervované jméno získat zpět ověřením.
- **Ruční přidávání modelů.** Vlastní magnet lze poslat s dochovanou kopií a důkazy: připnutou revizí, kontrolními součty souborů a dokladem o licenci. Povoleny jsou jen licence MIT a Apache-2.0 plus schválená výjimka pro Kimi-K3. Shoda s oficiálními LFS haši Hugging Face zveřejní záznam okamžitě, neshody nebo zmizelý zdroj zůstávají ve frontě ke kontrole.
- **Závislost na Hugging Face zatím trvá.** Web sám přiznává, že dnes některé jeho části na Hugging Face a jeho komunitě závisí a že přímé publikování modelů bez předchozího nahrání na Hugging Face je teprve plánované. Odeslání modelu dnes vyžaduje účet na Hugging Face a model tam už musí být.
- **Bodový systém.** Body mají uznávat účast v žebříčku, nejsou peníze ani kredit na výpočetní výkon. Uvítací body náleží jen za první způsobilou přezdívku na účet. Odměny za seedování jsou označené jako plánované a neaktivní, protože web nejprve potřebuje doložitelné důkazy o seedování. Token podle webu neexistuje.
- **Žádný přiložený obrázek.** V podkladu není žádný obrázek; pole `image_text` v extrakci je prázdné. Jeden komentující odkazuje na externí PNG náhled, který součástí balíčku není.

## Čísla

Parametry příspěvku a jeho přijetí:

| Ukazatel | Hodnota |
|---|---|
| Skóre | 865 |
| Komentářů | 122 |
| Poměr kladných hlasů | 0,92 |
| Způsobilých modelů (údaj webu) | 669 tis. + |
| Nejlepší komentář (skóre) | 414 |
| Referenční počet seedujících v ukázce záchrany | 1 240 |
| Velikost souboru v ukázce ověření | 6,7 GB |

Trendující modely tak, jak je uvádí výpis webu (velikost, údaj u magnetu, stažení):

| Model | Zaměření | Velikost | 🌱 / stav | Stažení |
|---|---|---|---|---|
| convaiinnovations/laya | klasifikace textu | 843 MB | 4 | 0 |
| prism-ml/Ternary-Bonsai-2-27B-gguf | generování textu | 54 GB | 6 | 3,0 mil. |
| XingChen-AGI/Xing4.0-29B-A4B | generování textu | 62 GB | 16 | 42 tis. |
| deepseek-ai/DeepSeek-V4.1-Flash | obrázek–text–text | 765 GB | 9 | 606 tis. |
| Qwen/Qwen3.8-27B | obrázek–text–text | 56 GB | 19 | 6,8 mil. |
| AlexWortega/openjev | klasifikace textu | 89 GB | Ready | 0 |
| XiaomiMiMo/MiMo-V2.6-Pro-RL | generování textu | 535 GB | Ready | 9,8 tis. |
| XiaomiMiMo/MiMo-V2.6-Flash-RL | generování textu | 163 GB | Ready | 19 tis. |
| XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B | obrázek–text–text | 19 GB | 1 | 5,7 tis. |

Profil ověřené organizace zai-org (Z.ai / Zhipu AI, Peking) uvádí u modelu GLM-5.2 celkem 1 800 seedujících, u GLM-4-9B 1 240 a u obrazového CogVideoX-5B 760.

Bodové odměny podle webu:

| Aktivita | Body | Limit |
|---|---|---|
| Uvítací body | — | jedna způsobilá přezdívka na účet |
| Doporučení nového účtu | 50 | nejvýše 10 uznaných doporučení na účet |
| Zachráněný model | 25 | za každý jednotlivý zachráněný model, prvnímu ověřenému vlastníkovi |
| Odměny za seedování | plánováno | dosud neaktivní |

## Citace

> „Název mluví sám za sebe. Pro případ, že se někdo rozhodne Hugging Face cenzurovat, budeme mít alternativu." (překlad) — u/Atagor, text příspěvku

> „Nejsem autor. Kdybych byl autorem, nepoužil bych slovo ‚pirátství'. Pokud jsi autorem ty, prosím, přejmenuj doménu! Co je od počátku svobodné, se tak musí i jmenovat, nic nepirátíme." (překlad) — u/Atagor, dodatek k příspěvku

> „Proměňte AI v torrenty, které žijí navěky." (překlad) — web Pirate Face, pirateface.co

> „Otevřené modely — LLM, obrazové, zvukové, datasety — jako magnetické odkazy, které nelze nikdy stáhnout dolů. Žádný jediný vlastník ani místo selhání." (překlad) — web Pirate Face, pirateface.co

> „Trendující modely pod licencemi Apache-2.0 a MIT, synchronizované v přímém přenosu z Hugging Face — každý se stává torrentem s ověřeným kontrolním součtem." (překlad) — web Pirate Face, pirateface.co

> „Ověřeno proti Hugging Face — bit po bitu, nepozměněno." (překlad) — web Pirate Face, ukázka ověření souboru

> „Torrentování se nerovná pirátství." (překlad) — u/DeathToOrcs2, komentář se skóre 414

> „Ano, není to pirátství, když to bylo od počátku svobodné a otevřené." (překlad) — u/Turbulent-Alps4046, komentář se skóre 181

> „No teda. Čekal jsem převážně prázdnou pustinu jako u tolika jiných pokusů o tohle. Tohle je úžasné a už teď masivně naplněné modely. Opravdu doufám, že se to chytí. Dobrá práce!" (překlad) — u/Odd-World4925, komentář se skóre 81

> „No, to je proto, že to při každém požadavku na stažení skoro výhradně jen stahuje z HF. Ty modely nehostují a ani pro ně nemají seedující." (překlad) — u/-Cubie-, komentář se skóre 66

> „Máme Pirate Bay pro LLM dřív než GTA 6." (překlad) — u/bakatristan, komentář se skóre 6

## Co říkají komentáře

Jednoznačně nejhlasitější linka se točí kolem slova „pirátství". Komentář „Torrenting != piracy" od u/DeathToOrcs2 získal 414 bodů, tedy téměř polovinu skóre příspěvku, a odpověď u/Turbulent-Alps4046 se 181 body ho doplňuje: o pirátství nejde, pokud byl obsah od počátku svobodný a otevřený. Stejně to vidí u/Feztopia — pirátství a torrentování nejsou totéž. Kryje se to s dodatkem samotného autora, který se od slova „pirátství" distancoval. Proti stojí menšinový hlas u/lucideer (9 bodů): torrentování pirátství není, ale trénování LLM podle něj obvykle ano — doklad k tomu v podkladu není.

Druhá linka je překvapení nad stavem služby a chvála provedení. u/Odd-World4925 (81 bodů) čekal prázdnou pustinu a doufá, že se projekt chytí, u/Infamous_Sorbet4021 chválí UX, u/tugoubxs a u/Odd_Error_6736 vyzývají, ať takových projektů vzniká víc.

Třetí linka je věcná skepse. u/-Cubie- (66 bodů) upozorňuje, že služba skoro výhradně jen stahuje z Hugging Face, modely nehostuje a pro všechny ty torrenty nemá seedující — což vysvětluje rozpor mezi chválou naplněného katalogu a realitou přenosu. u/name_was_taken dodává, že torrenty žijí a umírají podle seedujících a kdo jen stahuje a provozuje model, systému škodí; seedovat by se mělo alespoň do sta procent. u/North_Affect_8167 se ptá, kdo dokáže dlouhodobě seedovat půlterabajtový torrent.

Čtvrtá linka je praktická: u/No-Refrigerator-1672 se ptá na pohodlné stažení jediným příkazem z Linux CLI pro self-hosted servery a u/Odd-World4925 odpovídá příkazem `torrent -magnet '<magnet_link>' -dir /cesta/do/cile`. K vizuálu se vyjadřuje u/RiskyBizz216 dotazem na externí PNG náhled a u/BangkokPadang návrhem na obrázek ve stylu „HuggingBay".

Pátá linka jsou narážky na jméno a historii: u/snugglezone (146 bodů) navrhuje přejmenovat projekt na verylegalverycoolface.com, u/RollingMeteors variantu doplňuje, u/mitchins-au se ptá, co se stalo s „hugging bay", u/zitr0y a u/bakatristan žertují o úhlavním nepříteli a o Pirate Bay pro LLM dřív než GTA 6 a u/Lerola vzpomíná na potichu vypouštěné magnet odkazy. Nejostřejší je u/_tessarion (87 bodů): když autor nezná takovou základní věc, je podle něj celý projekt „slopcoded".

## Rozpory a neověřené informace

- **Trvanlivost a nezničitelnost.** Tvrzení webu, že magnetické odkazy „nelze nikdy stáhnout dolů" a že modely přežijí díky swarmu, je marketingové a v podkladu není nezávisle ověřené. Stejně tak je neověřený údaj o více než 669 tisících způsobilých modelech a o „živé" synchronizaci s Hugging Face.
- **Naplněný katalog vs. seedování.** Zatímco u/Odd-World4925 a další chválí katalog jako masivně naplněný, u/-Cubie- tvrdí, že jde téměř výhradně o stahování z Hugging Face bez hostování a bez seedujících. Obě tvrzení pocházejí z komentářů a ani jedno není v podkladu doloženo měřením.
- **Cenzura vs. licence.** Autor příspěvku rámuje projekt jako pojistku pro případ cenzury Hugging Face, komentáře ale namítají, že o pirátství nejde, protože modely jsou svobodné a otevřené. Rozpor je v interpretaci, ne ve faktech o službě.
- **Nesoulad rétoriky nezávislosti a přiznané závislosti.** Web se hlásí k nezávislosti na centralizovaném hostingu, zároveň sám uvádí, že dnes části služby na Hugging Face závisí a že přímé publikování modelů teprve plánuje. Podmínka „model už musí být na Hugging Face" platí i pro ruční přidání.
- **„Žádný token" vedle bodů a plánovaných benefitů.** Web výslovně uvádí, že token neexistuje a že body nejsou peníze ani výpočetní kredit; zároveň zmiňuje plánované volné výpočetní kredity a exkluzivní vydání modelů a odměny za seedování označuje jako plánované. Podmínky, limity ani termíny nejsou zveřejněné, body se na kredity automaticky nepřevádějí.
- **Tvrzení bez opory.** Komentář u/lucideer, že trénování LLM obvykle pirátstvím je, nemá v podkladu žádný doklad. Doloženo není ani tvrzení u/_tessarion o „slopcodingu".
- **Role autora příspěvku.** u/Atagor uvádí, že není autorem služby, ale v diskusi vystupuje jako ten, kdo projekt představil, a v dodatku oslovuje skutečného autora. Zda s projektem jinak souvisí, podklad neříká.

## Proč to je důležité

Pirate Face staví na problému, který komunita kolem otevřených modelů řeší dlouhodobě: co se stane s veřejně dostupnými váhami, když je hostující platforma odstraní. Odpověď je architektonická — torrent s web-seedem funguje i bez jediného peer a skutečná peer-to-peer síť nastupuje teprve ve chvíli, kdy zdroj zmizí. Samotné váhy se přitom nemění: kontrolní součet SHA-256 zůstává stejný, ať data přijdou odkudkoli.

Druhým momentem je licence. Ruční přidání modelu vyžaduje doložení licence a povoluje jen MIT a Apache-2.0 plus výjimku pro Kimi-K3. Právě proto zní hlavní námitka diskuse tak silně: u skutečně svobodných licencí se o pirátství mluvit nedá a název služby i doména tomu podle kritiků škodí. Zároveň se vyjasňuje, že projekt není o obcházení licencí, ale o zálohování legálně volně šířitelného obsahu.

Třetím momentem je ekonomika seedování, na kterou upozorňují skeptičtější komentáře: torrent o velikosti 535 GB nebo 765 GB nemá dlouhodobého seedujícího jen tak, a bez něj zůstává záchrana po odstranění z Hugging Face jen teoretickou možností. Web si to zjevně uvědomuje, když odměny za seedování odkládá, dokud nebude mít doložitelné důkazy. Ani API pro přímé zapojení, ani rezervace přezdívek s ověřením proti účtu na Hugging Face zatím spuštěné nejsou, takže o skutečné nezávislosti na původním hostiteli se rozhodne až později.

## Zdroje

- https://pirateface.co/
- https://www.reddit.com/r/LocalLLaMA/comments/1wnxhji/pirate_face_pirate_bay_for_llms/
- 2026-09-23/_data/bundles/1wnxhji.md
- 2026-09-23/_data/extracts/1wnxhji.json
