# 50562262
**Safeguardy zablokovaly opravu chyby. Vývojář si pomohl open weights**

Hacker News · speckx · 19. listopadu 2026, 17:30 · 514 bodů / 206 komentářů · [diskuse](https://news.ycombinator.com/item?id=50562262)

Seniorní vývojář poprosil Claude Code o bezpečnostní revizi vlastního produktu, nad kterým má prokazatelnou kontrolu. Model našel drobnou přehlédnutelnou chybu s jednořádkovou opravou, jenže další práci pak odmítl s odkazem na safeguards. Výjimka podle autora vyžaduje čekání několik pracovních dnů, vzdání se výjimek z uchovávání dat i doklad totožnosti, a ani pak není jisté, že ji člověk dostane.

Odkazovaný text argumentuje, že taková pravidla dopadají hlavně na obránce. Zločinci o žádné schválení nežádají a sáhnou po abliterovaných open weights modelech, které je neřeší. Autor nakonec chybu potvrdil a opravil s pomocí modelu GLM 5.3 hostovaného v EU, který jeho záměr splnil a pomohl ověřit, že problém je pryč. Uzavírá to hořkým vzkazem, že Anthropic tak svět učinil méně bezpečným, a nadhazuje, zda nejde o budování příkopu před vstupem na burzu.

V diskusi se tenhle vztek rychle ujal jako sdílená zkušenost. JohnMakin píše, že safeguards jsou v nejlepším případě neúčinné a v nejhorším globální bezpečnost přímo zhoršují. Uživatel c4u2024 přitakává, že kvůli nim nemůže opravit vlastní prostředí, zatímco svět kolem zůstává děravý. Nathanfig připomíná reálné následky při útoku na Hugging Face, kdy uzavřené modely odmítly pomoci a k odvrácení roje posloužil právě GLM-5. InsidiousWombat k tomu dodává ještě jedovatější verzi, že uzavřené modely útok provedly a pro „důvěryhodné“ platící klienty pak existuje zvláštní přístup k schopnostem, které běžný majitel aplikace nesmí použít ani k vlastní obraně.

Z praktické linky vlákna se stává burza náhradních řešení. Hazard ironicky radí zaplatit si některý ze špičkových čínských open weights modelů, třeba Kimi 3.1 nebo GLM, a kingforaday doplňuje, že dobré jsou i Mistral Large 4 a Sakana Fugu-Cyber. Noahjk se ptá, zda existuje udržovaný přehled agentů pro třídy úloh, které Claude odmítá, s jejich silnými a slabými stránkami a správným stavěním promptů. Orphereus naproti tomu varuje, že stavět vývoj do takové míry na třetích stranách je čím dál horší nápad.

Třetí proud diskuse řeší, proč to tak je. CoolestBeans to popisuje skoro jako ochranářský racket: laboratoře předvedly superhackerské nástroje, každý s dost penězi si je teď dokáže postavit, a kdo se chce jejich verzí bránit, musí být v jejich přízni a zaplatit za privilegium. Podobně to vidí k310 s odkazem na zlaté pravidlo, že pravidla píše ten, kdo má zlato. Speedboat199 připomíná, že útočníci safeguards stejně vždy obejdou, a zmiňuje dříve přiznaný případ stavby naváděných raketových systémů s Claude. Kdyby prý šlo opravdu o bezpečí, vhodným řešením by bylo to vůbec nevydávat.

Z vlákna tak zůstává jednoduché ponaučení pro obránce: když potřebují rychle ověřit a zalepit vlastní díru, vede cesta častěji k otevřeným vahám než k žádosti o výjimku.

Zpět na [denní přehled](00-index.md).
