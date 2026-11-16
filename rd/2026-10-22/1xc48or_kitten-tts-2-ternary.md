# 1xc48or
**Kitten-TTS 2: první 1,58bitový TTS běží na CPU**

r/LocalLLaMA · u/ElectricalBar7464 · 22. října 2026, 02:33 · 723 bodů / 147 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xc48or/)

KittenML vydal otevřený model Kitten-TTS 2 se 1,7 miliardy parametrů, který je podle autorů prvním 1,58bitovým modelem pro převod textu na řeč na světě. Každá váha v těle modelu nabývá jen jedné ze tří hodnot -1, 0 a +1, takže má drobný otisk a zvládá generování v reálném čase na obyčejném CPU. Láká na klonování hlasu z méně než pětisekundové ukázky bez dolaďování, podporu více než dvacítky jazyků včetně klonování napříč jazyky a řízení důrazu či expresivity, kód a váhy jsou na GitHubu a Hugging Face.

Právě běh bez grafiky komunitu nejvíc nadchl. u/OpenComplaint524 to označil za zásadní změnu pro lokální agenty, protože syntéza v reálném čase na CPU nevezme jazykovému modelu ani megabyte VRAM. u/wasthespyingendless hlásí z M1 Max asi trojnásobek reálného času a chválí výslovnost cizích slov v anglickém textu, u/Acceptable-Cycle4645 přidal návod na vyzkoušení v audio.cpp, odkazy na GGUF a čísla z M4 Pro, kde se po NEON optimalizaci dostal s osmi vlákny na faktor 0,506.

Zvuk už tak jednotný ohlas nemá. u/Z-Dante píše, že ukázka ve videu zní pořád trochu roboticky a jeho přenosný tandem na audioknihy, Kokoro a piper s hlasem alba, mu přijde přirozenější, byť bez emocí. Podobně dopadl slepý souboj u/mrgulabull: Kokoro s hlasem af_heart i Omnivoice zněly přirozeněji, Kokoro je navíc menší a rychlejší a Omnivoice má pořád lepší klonování, takže novinka podle něj nevede nikde. u/vladoportos slyší v hlase zkreslení, u/OtherUse1685 shrnuje, že na ElevenLabs to ještě nemá, ale na lokální stroj to bude časem stačit.

Do detailů jdou jazykové postřehy. u/Synor chválí němčinu, která je srovnatelná se včerejším Phonon 40m, a k tomu výborné klonování, zatímco u/beryugyo619 hlásí, že výchozí japonština zní americky a nezvládá čtení kandži. Humor obstaral u/FatheredPuma81 s povzdechem, že ze smíchu v ukázkách mu jde strach o život, a u/Elouakili_Flexy, podle kterého je 1,58 bitu sotva dost na ano, ne a možná, a model v tom klonuje hlasy ve dvaceti jazycích na CPU. Praktickou brzdu přihodil u/howardhus: pro komerční použití zdarma je potřeba roční tržby i celkové financování pod milion dolarů, povinná registrace u Stellon Labs a uvedení autorství, po překročení limitu licence končí.

Kdo má slabou grafiku a chce si hlasového klona hostovat sám, má novou hračku na hraní, jen od ní zatím nemá čekat špičkovou přirozenost.
