# 50063365
**Intel představil GPU akcelerátor D270 až se 480 GB LPDDR5X**

Hacker News · hurricanepootis · 12. 10. 2026, 23:35 · 128 bodů / 53 komentářů · [diskuse](https://news.ycombinator.com/item?id=50063365)

Intel rozšířil řadu datacentrových grafik D-series o kartu označovanou jako D270, která patří do rodiny Crescent Island. Největší pozornost budí paměťová kapacita až 480 GB LPDDR5X, která má kartu předurčit pro akceleraci umělé inteligence a inferenci velkých modelů.

Odkazovaná produktová stránka Intelu láká na efektivní obsluhu tokenů v husté, vzduchem chlazené infrastruktuře se standardním PCIe. Právě maximální počet tokenů na rack a watt a nízké náklady na škálování kapacity mají být hlavní prodejní argument proti zavedené konkurenci v čele s Nvidií.

Nejživější linka diskuse ale novinku oplakává jako promarněnou šanci pro běžné zákazníky. Autor vlákna je zklamaný, že Intel novinky označil předponou D a spotřebitelskou třídu zřejmě nevydá, ačkoliv se jeho ovladače na Linuxu i Windows výrazně zlepšily. Souhlasí s ním ank i boredatoms, podle kterých by trhu slušela třetí možnost v nízké a střední třídě, zvlášť když se v grafice točí tolik peněz.

Jádro technické debaty se točí kolem poměru obrovské paměti a slabšího výpočetního výkonu. jauntywundrkind připomíná, že se původně mluvilo o 120 GB s možností větších kapacit u partnerů, a doufá v cenu konkurenceschopnou Macu díky dvaceti kanálům LPDDR5. Odpověď bigyabai je skeptická: karta i Mac podle něj brzdí nedostatek výpočetního výkonu a při inferenci hutnějších modelů budou výrazně limitované prefillem. Podobně arjie se ptá, zda je karta s tak malým výkonem určená speciálně pro MoE modely, a ismailmaj ji popisuje čísly 1,5 TB/s a 1,3 PFLOPS bez rychlého multi-GPU propojení jako spotřebitelskou kartu převlečenou za serverovou.

Srovnání s konkurencí vyznívá rozpačitě i v propustnosti. suprjami chválí 1,5 TB/s paměťové propustnosti, ale auspiv kontruje, že jeho V100 z roku 2017 měla 0,9 TB/s, zatímco B300 má téměř 8 TB/s a AMD MI300x z roku 2023 má 5,3 TB/s. Sám si pak opravu dává sám: číslo je působivé právě proto, že jde o víceméně běžnou RAM, ne VRAM. Praktický výklad nabízí minraws, podle kterého jde o levný lokální provoz velmi velkých modelů pro dva až čtyři uživatele, třeba pro banky a podobné firmy, které musejí kvůli experimentům a bezpečnosti běžet lokálně.

Kolem ceny a dostupnosti panuje hlavně ironie. Na otázku rkagerera, zda kartu může vůbec koupit a dát jí přednost před Blackwellem, odpovídá kadoban, že určitě ne teď a možná nikdy, a samuelknight dodává, že podle tvaru desky patří do serverové skříně za řadu ventilátorů. Gigachad i K0balt se proto těší, až karty za pět až osm let vyřadí datacentra a objeví se v bazarech do domácích laboratoří, podobně jako dnes starší herní karty. Odlehčení obstarávají vtipy o počtu snímků v Cyberpunku 2077, o Crysis a o tokenech žádajících tequilu a kaviár, zatímco na dotaz po ceně přichází hláška downrightmikea o několika bezdomovcích v hodnotě orgánů.

Z diskuse tak zůstává obraz karty s lákavou pamětí, nejistým výkonem a ještě nejistější dostupností, jejíž druhý život v domácích serverech už teď mnozí netrpělivě vyhlížejí.
