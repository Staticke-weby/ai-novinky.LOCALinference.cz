# 50340992
**Skill pro Claude Code vyrobí produktové video z reálného průchodu aplikací**

Hacker News · aaitor · 2. listopadu 2026, 19:10 · 87 bodů / 26 komentářů · [diskuse](https://news.ycombinator.com/item?id=50340992)

Vývojář Aitor Argomaniz zveřejnil open-source projekt skill-video-studio ve verzi 1.0.1, lokální workspace, který přes skill /devrel-video pro Claude Code vyrábí produktová dema z reálného průchodu aplikací. Skutečné interakce s produktem nahrává přes Playwright CLI, titulky, kapitoly a výzvy k akci skládá v HyperFrames a finální střih a kontrolu obstarává FFmpeg. Začít se má tichou ukázkou, vyprávění, hudbu, titulky nebo vlastní záběry moderátora lze přidat až dodatečně.

Návod v repozitáři popisuje rychlý start: naklonovat celý workspace, otevřít Claude Code a příkazem připravit třeba pětadvacetisekundovou tichou procházku přibalenou ukázkovou aplikací Acme. Každé video řídí soubor brief.yaml s adresou produktu, publikem, sdělením a jednotlivými kroky, značkové barvy leží ve složce brands a výstup vzniká přímo ve složce projektu. Plná produkce vyžaduje lokální nástroje včetně Node.js 22, FFmpeg, Chromia a pomocných pythoních závislostí, přibalené jsou i dva hotové příklady s anglickými a španělskými titulky.

Sám autor v diskusi vysvětluje motivaci: po nadšení z funkční hračky pro něj byla propagační část vždy spíš povinnost, manuály a videa zanedbával, a skill má pomoct právě s tím posledním krokem. S tímto pocitem se ztotožnil uživatel aleyan, pro kterého je sdílení vlastní práce nejhorší částí práce softwarového inženýra, zvlášť když komunity trestají sebepropagaci. Uživatel testycool mu za tuhle upřímnost rovnou děkuje, že ho přesvědčil.

Nejhlasitější linka se ale točí kolem kvality ukázkového videa. Uživatel tjohnell upozorňuje, že vypravěč je v jedenácté sekundě useknutý, což potvrzuje i uživatel TomGarden a ptá se, zda se autor na vlastní výstup vůbec podíval. Uživatel meta-meta kritizuje příliš hlasitou hudbu s dunivým kopákem a agresivním odskočením pod vyprávěním, uživatel malnourish dodává, že mix je nevyrovnaný a hudba vyprávění přehlušuje. Uživatel bakugo to glosuje vtípkem, že sledovat video je moc práce a agent to měl udělat za diváka.

Praktickou debatu vedou lidé, kteří něco podobného už staví. Uživatel gopalv píše, že takový skill má smysl šít na míru firemnímu stylu a prodejnímu týmu, sám si prý před konferencemi nechává generovat balíček dem s aktuálními firmami a případy užití. Uživatel coreylane jezdí přes filmcraft-cli s dabingem z ElevenLabs a řeší jen mobilní nahrávání, uživatel mrieck točí tiktoková dema s avatarem za asi dva dolary přes vlastní klíč k fal.ai. Uživatelé solatic a marcellosso přidávají alternativy: jeden nechává Claude psát skript, který aplikací prochází a nahrává ji, druhý si místo nahrávání nechává rozhraní přegenerovat, aby bylo celé animovatelné.

Nechybí ani skepse k samotným skillům. Uživatel jackfreeman tvrdí, že Claude Opus 5.5 to zvládne dobře i bez nich, uživatelé mirzap a zeroq označují skilly za nafouknutý hype a slova přidaná do kontextu. Uživatel jjcm přidal přímé srovnání videa bez skillu a se skillem a varuje před vážnými zranitelnostmi Playwright, na což uživatel RugnirViking reaguje, že mu obě videa přijdou skoro stejná.

Z vlákna tak zůstává jednoduché ponaučení: automatické točení dem dává smysl až tehdy, když přežije i nemilosrdné uši a oči diváků.

[Zpět na index](00-index.md)
