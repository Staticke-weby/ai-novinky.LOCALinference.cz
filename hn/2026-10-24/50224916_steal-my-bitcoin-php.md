# 50224916
**Steal My Bitcoin: 500 dolarů za průnik přes PHP zranitelnost**

Hacker News · cloudlandsdev · 24. října 2026, 22:30 · 461 bodů / 286 komentářů · [diskuse](https://news.ycombinator.com/item?id=50224916)

Autor si po několika dnech paniky kolem zranitelnosti PHP pro vzdálené spuštění kódu položil zvědavou otázku, jestli ji někdo umí skutečně zneužít, a odpověď nabídl rovnou otestovat v praxi. Na adrese stealmybitcoin.com proto vyvěsil výzvu: kdo se přes zranitelnou instalaci dostane ke skrytému klíči, může si odměnu nechat.

Server byl krátce po zveřejnění přetížený, takže uživatel nayuki pro ostatní opsal celé znění výzvy. Stojí v něm, že klíč je dostupný účtu, pod kterým běží PHP, přes binárku print-flag, a že na stroji je verze PHP z doby před zveřejněním zranitelností PHP2SHELL. Vítěz si peníze může nechat, nebo je věnovat organizaci GiveWell, veškerý provoz se ale loguje a autor upozorňuje, že na známém zranitelném stroji nelze zaručit soukromí.

Nejživější debata se vede o tom, co vlastně nevybrání odměny dokazuje. Uživatel hau chválí nápad jako způsob, jak tvrzení o triviálním exploitu ve volné přírodě učinit vyvratitelným, uživatel akerl_ namítá, že neúspěch existenci exploitu vyvrátit nemůže, ukáže jen to, zda ho někdo použil proti tomuto serveru. Uživatel jgalt212 k tomu dodává, že nejde o důkaz s nulovou znalostí, ale pokud je provozovatel důvěryhodný, je to silný signál, že exploit není triviální. Podobně to vidí uživatelé ls612 a fwlr: pět set dolarů je cenovka vložená do debaty o tom, zda umělá inteligence umí řetězit složité exploity automaticky a ve velkém.

Právě kolem částky se strhla hádka o ekonomiku. Uživatel jerrythegerbil tvrdí, že nabídka zůstane chvíli ležet, protože pro toho, kdo exploit má, je demonstrační cena směšně nízká proti riziku odevzdání funkčního postupu, a že za 15 až 25 tisíc by klíč zmizel okamžitě. Uživatel oofbey mu odpovídá, že otázka je jednodušší: staly se už exploity natolik běžnými, aby stály za pět set dolarů? Uživatel lukeify si rýpne, že autor dlouhého rozboru o hodnotě času právě strávil několik minut psaním komentáře s nulovou ekonomickou hodnotou, uživatel ncruces zase připomíná obrat o sto osmdesát stupňů od rad před osmdesáti hodinami okamžitě shodit všechny weby. Uživatel msm_ věc uklidňuje technicky: desítky funkčních exploitů existují, jen zatím není jeden univerzální a každý cíl vyžaduje znát konfiguraci serveru.

Stranou stojí praktické i pobavené hlasy. Uživatel jackdecker hlásí, že průnik komplikuje nginx s limitem velikosti požadavku na jeden megabajt, uživatel zoeysmithe vtipkuje, že za pět set dolarů může autor z logů posbírat nové varianty útoků a prodat je za tisíce. Mezitím uživatel xmcp123 poznamenává, že někdo do peněženky přispěl a odměna se zdvojnásobila na zhruba 1004 dolarů. Uživatel TacticalCoder doufá, že pokud klíč ukořistí jazykový model, dočká se komunita i popisu postupu.

Zůstává tak otevřená sázka: buď někdo brzy ukáže, jak snadné zneužití PHP skutečně je, nebo ticho kolem peněženky napoví, že strach z okamžitého automatického dobývání serverů byl přehnaný.
