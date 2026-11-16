# 1wvxl4n
**Qwen3.8-27B Humanlike Chat 2.0: mluví lidsky a nově umí volat nástroje**

r/LocalLLaMA · u/kvyb · 2. října 2026, 18:00 · 845 bodů / 181 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wvxl4n/)

Autor u/kvyb před měsícem vydal LoRA nadstavbu pro Qwen3.8-27B, která má model odnaučit takzvanému assistant speak a místo toho psát jako člověk. První verze nečekaně zabodovala se 700+ hlasy, 248 komentáři a 44 tisíci staženími, ale schytala i ostrou kritiku za jednoslovné odpovědi, jedinou osobnost a nefunkční volání nástrojů. Nová verze 2.0, na které pracoval tři týdny, má hlas zachovat a nedostatky smazat: bez systémového promptu si normálně esemeskuje, s kartou postavy drží roli, na požádání napíše formální e-mail nebo číslovaný postup a nově volá nástroje a raději se doptá, než aby si vymýšlel.

Nejvíc hlasů v diskusi posbíral rýpanec u/DrunkenRobotBipBop, jak moc osaměle se autor na škále od jedné do deseti cítí. U/kvyb odpověděl, že méně, než by se zdálo, jen ho unavuje, když asistenti otevírají každou odpověď zvoláním „Skvělá otázka!" a pak naservírují esej. Na stejné struně hraje i hláška u/rtgconde, že model textuje jako teenager, a přesmyčky názvů jako hey-you-up-3.8 nebo dlouhý změťový název od u/RazzmatazzReal4129 si utahují z konvencí pojmenovávání modelů v subredditu.

Vážnější linka se točí kolem toho, kde končí lidskost a začíná halucinace. U/_VirtualCosmos_ píše, že ho ztratil ve chvíli, kdy model v ukázce tvrdil, že byl v posilovně, a během dvou vět si začal hrát na člověka. Autor vysvětluje, že to je záměrný výchozí stav bez promptu, který si vymýšlí drobné detaily ze života, a stačí mu říct, ať píše v celých větách, nebo mu dát kartu persony. Když mu prý v systémovém promptu řeknete, že je umělá inteligence, normálně to přizná – na dotaz odpověděl „jo, jsem AI" a na otázku, jestli je skutečný, odepsal „ne, ale tak trochu skutečný jsem, existuju jako kód".

Z lidské noty pak diskuse sklouzne ke dvěma protipólům: dojetí a obavám. U/SrijSriv211 se ptá, jestli model dokáže mluvit jako „ona, jako dřív", se zlomeným srdcem v závěsu, a u/Borkato přiznává, že ze smutku stavěl něco podobného. Na druhé straně u/Status-Secret-4292 varuje, že tohle budou primárně využívat podvodníci, a u/Super_Range45 to ohodnotil jako centrum podvodných zpráv z deseti. Mezi tím září nadšený experiment u/Lodestone-DnD, který na starém Surface Pro rozehrává detektivní Dungeons & Dragons se čtyřmi lokálními modely v roli hráčů a právě padání do generického pomocnického hlasu bylo jeho největší překážkou.

Technicky zvídavé vlákno zajímá, jestli metoda funguje i jinde. Na dotaz u/Paradigmind, jak by si vedla Gemma 4 31B, autor odpovídá, že postup rozhodně není specifický pro Qwen a Gemmu má na seznamu. Trénink popisuje jako vlastní skript bez frameworku: vzorkování ve vLLM, učení jen do LoRA a dva učitelé – verze 1 se skrytým pokynem „piš jako člověk" pro chat a nástroje z čistého základního modelu pro instrukce, nástroje a kód.

Kdo je unavený z asistentů, co esejují na každou otázku, tady najde model, který si místo toho prostě esemeskuje – i s rizikem, že si občas vymyslí odpoledne v posilovně.
