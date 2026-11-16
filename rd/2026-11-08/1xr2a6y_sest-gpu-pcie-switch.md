# 1xr2a6y
**Šest GPU na jednom slotu. PCIe switch rozjel Qwen3.8-27B**

r/LocalLLaMA · u/bolts98 · 8. listopadu 2026, 17:23 · 178 bodů / 37 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xr2a6y/)

Nadšenec vměstnal šest grafických karet do jediného x16 slotu běžné desky ASUS TUF X570-Plus s Ryzenem 9 3900X a 128 GB RAM. Za přepínačem Broadcom PEX88096 běží čtyři Radeon AI PRO R9700 s 32 GB paměti a dvě RTX 3090 s 24 GB, na jednom hostu s Debianem bok po boku ROCm i CUDA. Čtveřice R9700 zapojená do tensorového paralelismu zvládne u modelu Qwen3.8-27B prefill 32tisícového promptu rychlostí kolem 4 700 tokenů za sekundu a šestnáct souběžných klientů dohromady dává asi 601 tokenů za sekundu.

Odkazovaný článek popisuje, proč autor sáhl po switchi místo obyčejné rozdvojky: bifurkáce umí z jednoho slotu udělat nanejvýš čtyři x4 linky, kdežto switch dá každé kartě vlastní gen4 x8 a navíc nechá R9700 komunikovat přímo mezi sebou. Právě peer-to-peer provoz přitom nikdy neopustí switch – při kopírování všemi čtyřmi kartami najednou naměřil 54,7 GB/s, tedy zhruba dvojnásobek jednosměrné propustnosti x16 uplinku. Zbytek textu je přehlídka ladění BIOSu, jaderných parametrů a vlastních modulů pro velké BARy, odemčení tensorového výkonu na 3090 i obcházení problémů s úsporným režimem karet.

V diskusi nejvíc rezonuje údiv, že to na obyčejné desce vůbec drží pohromadě. u/sleight42 to shrnuje nefalšovaně: jak to, že se stroj z toho nezblázní, a znamená to, že na starou desku jde pověsit čtyři x16 a dvě x8 karty a pojedou naplno? u/Royale_AJS jen suše přitakává, že switche jsou zkrátka cesta, a u/jbarrio_ dodává, že jedinou daní je pomalé úvodní nahrání modelu do paměti, když už tam pak Qwen zůstává natrvalo.

Odpověď na otázku u/Pyrolistical, proč neběží P2P i na 3090, přináší sám článek: karty si ponechaly malé 256MB BARy, se stock ovladačem 580 hlásí nvidia-smi mezi nimi stav nepodporovaného čipsetu a kopie tak chodí přes paměť hosta. Na to navazuje u/a_beautiful_rhind s výhradou, že switche jsou skvělé, ale u hybridní inference člověka zaškrtí linka PCIe do CPU, a přeje si switch s agregovanými upstream porty. A u/putrasherni rovnou přitvrzuje: jít ještě dál, vzít deset SlimSAS 88096 karet a dostat R9700 na plné x16 s 7 500 tokeny za sekundu při prefillu.

Praktická linka se točí kolem železa, ceny a provozu. u/OvertaxedOne se ptá na fyzickou vrstvu, jak všechny karty vůbec zasunout a napájet, když samotný switch je ta snadná část. u/NickCanCode řeší vysoký klidový odběr a jestli jde uspat aspoň samotný switch bez restartu, když odpojování karet je nepraktické. A u/Physical_Gold_1485 se ptá za všechny zvědavé nováčky, jestli být na jednom slotu znamená, že karty lépe sdílejí prostředky a lokální AI je rychlejší – odpověď je v článku: ano, ale hlavně díky lokálnímu P2P provozu uvnitř switche.

Kdo čekal datacentrum, našel ho postavené z bazarového železa a spotřební desky.
