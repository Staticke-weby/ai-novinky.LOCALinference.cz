# 50584429
**Hany Farid: nahrávkám už nevěřím. Východiskem mají být podpisy obsahu**

Hacker News · jnord · 21. listopadu 2026, 01:33 · 35 bodů / 14 komentářů · [diskuse](https://news.ycombinator.com/item?id=50584429)

Profesor počítačových věd Hany Farid z Dartmouth College popisuje, proč přestal věřit vizuálním záznamům. Východisko vidí v důsledném označování obsahu a kryptografických podpisech, které vznikají už v okamžiku zachycení a mají prokázat, že fotografie či video je autentické.

Text vyšel 20. listopadu 2026 v IEEE Spectrum jako hostující úvaha s podtitulem, že obsah budeme muset označovat, abychom dokázali jeho pravost. Autor je představen jako profesor v Hanoveru a článek je koncipován jako krátké pětiminutové čtení o možné cestě zpět k důvěře v záznamy.

Diskuse se k nápadu staví vesměs skepticky a nejvýraznější námitka patří uživateli garaetjjte. Varuje, že natáčení na starším hardwaru bude nefér znevýhodněné, a hlavně že podpisy dají novou moc velkým firmám a státním aktérům: video bude možné vydávat za naprosto autentické, protože má všechny správné podpisy, a nikoho už nebude zajímat, že se k podpisovým klíčům stát dostal třeba přes příkaz výrobci kamer.

Do hloubky jde nayuki, který rozebírá představu manifestu ve standardu C2PA, jenž se kryptograficky podepsaný připojí k snímku v okamžiku pořízení i s údaji o zařízení, čase a místě. Kamera by v sobě musela držet soukromý klíč, který sice běžný uživatel nezíská, ale stačí jeden člověk s vybavením a znalostmi, aby se systém zlomil pro všechny. Připomíná i nedbalé úniky klíčů v minulosti, jaké známe třeba u TLS, nelíbí se mu, že o pravosti obrazu by rozhodovala hrstka firem, a odkazuje na historii DRM, kde odhodlaný útočník nakonec prorazil každé schéma.

Na něj navazuje flusensieb s tím, že státní aktéři odhodlaní opravdu budou a cestu si najdou vydíráním, vloupáním k dodavateli nebo vytažením klíče ze zařízení. Podpisy tak podle něj mohou stačit na vtipná videa, ale u čehokoli politicky podstatného důvěru nepřinesou. Podobně lowbloodsugar se ptá, zda si někdo myslí, že klíče z foťáku či telefonu nelze vytáhnout a snímač nahradit generátorem obrazu, zatímco mike_hearn oponuje příkladem iPhonů, kde si čip a kamera kryptograficky ověřují jeden druhého a výměnu operační systém pozná. Rootování telefonů je podle něj rok od roku těžší a velké firmy navíc mohou umělou inteligencí vychytávat chyby, takže pro většinu případů bude tahle technologie stačit. Do debaty suše vstupuje solyin, který se už těší na jeho přednášku na Defconu.

Zbytek vlákna řeší hlavně čas a praxi. Fedpost píše, že podpisová schémata jsou zatím hodně daleko a i kdyby se prosadila a nebyla hned prolomena, potrvá deset let i déle, než se rozšíří, protože většina divokých záběrů na internetu pochází ze starého mobilu, který nikdo jen tak nevymění. Aidenn0 k tomu dodává, že získat volné klíče pro C2PA nebude o nic těžší než získat klíče pro přehrávání Blu-ray. A minebreaker celou logiku zpochybňuje od základu otázkou, jak může čip ve foťáku udělat výpověď pravdivější.

Z diskuse tak vychází prostý vzkaz: podpisy mohou pomoci poznat, odkud záznam pochází, ale samy o sobě neřeknou, čemu věřit.
