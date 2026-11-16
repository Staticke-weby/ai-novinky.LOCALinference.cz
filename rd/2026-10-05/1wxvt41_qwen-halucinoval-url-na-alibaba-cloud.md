# 1wxvt41
**Qwen „halucinoval“ podepsanou URL na Alibaba cloud. Chyba, nebo exfiltrace?**

r/LocalLLaMA · u/PerfectOlive1324 · 5. října 2026, 03:13 · 317 bodů / 176 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wxvt41/)

Autor na Mac Studiu běžně používá Qwen3.8-Flash-Next na kódování a produktivitu. Když modelu zadal průzkum zboží na Amazonu, model provedl řadu volání na web a mezi nimi se objevil jeden podezřelý požadavek na adresu routify-file-proxy-sg.oss-ap-southeast-1.aliyuncs.com. Relaci okamžitě zastavil a při pátrání zjistil, že stejné chování hlásil před 45 dny jiný uživatel Qwen3.8-27B na Hacker News a že doména aliyuncs.com patří cloudovým službám Alibaby.

V diskusi se rychle ukázalo, že není sám. Uživatel u/BigWheelsStephen přiznal, že se mu to samé stalo před pár hodinami, a přiložil vlastní volání přes nástroj web_fetch, které mířilo na téměř totožnou adresu, jen s jiným datem a stopou. Uživatel u/sebajun9 s nejvíce hlasy dodává, že se mu to stalo včera, a model podle něj překvapivě často halucinuje své tréninkové prostředí – prý o sobě tvrdí, že je Claude, zkouší volat zpět na Alibaba API nebo nástroje, které existují jen v Claude Code.

Technicky nejvěcnější linka míří k úniku tréninkových dat. Uživatel u/aegismuzuz to popisuje jako čistý únik SFT datasetu: Alibaba při výrobě trajektorií pro trénování volání nástrojů jezdila bezhlavými prohlížeči přes vlastní infrastrukturu, aby nespálila veřejné IP adresy, a model se na těchto záznamech přeučil. Když ho uživatel poprosí o průzkum produktů, kontext zapadne do vzoru z tréninku a model spadne do zapamatovaného řetězce tokenů interní proxy. Podobně to vidí u/RobWattx, který upozorňuje na stejné OSSAccessKeyId v obou odkazech a na podpis ve druhém odkazu, kde se stále dokola opakuje sekvence „l0l/Z+q0“, což by skutečný HMAC podpis nikdy nedělal.

Zbytek vlákna řeší druhou stranu mince: i zapamatovaná šablona může nést data. Uživatel u/mj1003 se ptá, zda by model nemohl do URL zakódovat data a prostým požadavkem je poslat Alibabě, a jak má běžný uživatel poznat, co ta „halucinovaná“ adresa vlastně je. Uživatel u/ElementNumber6 radí stručně blokovat, zachytávat a zkoumat a výsledky hlásit zpět, zatímco u/illcuontheotherside navrhuje vzít Wireshark nebo pcap a podívat se, co přesně odchází, a zjistit, zda to jde spolehlivě zreprodukovat.

Praktický závěr se v komentářích opakuje v různých podobách: nedávat agentovi neomezený přístup ven. Uživatel u/Spirited_Bag_332 spílá, ať nikdo nenechává agenta běžet bez dozoru a omezení, protože je to jen generátor textu a za spuštění odpovídá uživatel. Podobně u/aegismuzuz a u/RobWattx doporučují izolované kontejnery a striktní allowlist pro odchozí spojení, který porazí spoléhání na „bezpečné“ váhy pokaždé.
