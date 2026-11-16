# 50504077
**Kiri: kontejnerový runtime, který slibuje osmkrát rychlejší start než Docker**

Hacker News · nikolay · 15. listopadu 2026, 05:40 · 93 bodů / 34 komentářů · [diskuse](https://news.ycombinator.com/item?id=50504077)

Kiri se představuje jako moderní kontejnerový runtime s jedním daemonem, který umí spouštět běžné Docker kontejnery. Hlavním lákadlem je rychlost startu: příkaz docker run na Kiri zabere 22 ms, zatímco na Docker Desktopu 178 ms, na Colimě 152 ms a na OrbStacku 279 ms, vše při 2 CPU a 8 GB paměti. Verze 0.2.1 je zdarma v betě pro macOS, Windows a Linux.

Odkazovaný web to vysvětluje jedinou virtuální mašinou a daemonem, který si sám vytváří namespaces, cgroups a mounty a po kontejneru nenechává běžet žádný pomocný proces. Studený start mašiny má trvat 112 ms místo 810 ms u běžného kernelu, komunikace jde jedním vsock kanálem a samotný daemon drží kolem 15 MB, po minutě nicnedělání usne a probudí se za 0,15 sekundy. K tomu slibuje správu Compose projektů, buildy přes BuildKit včetně skenu zranitelností, cluster k3s za asi 20 sekund, linuxové stroje, otevírání aplikací jménem s HTTPS a veřejné sdílení kontejneru přes runkiri.cloud.

Diskuse se rychle stočila k tomu, co vlastně číslo osmkrát znamená. Uživatel cholindo se ptá, jestli běží rychleji kontejnery, nebo jen nástroje kolem nich, a uživatel tpetry odpovídá, že se měří jen start kontejneru. Rozdíl kolem dvou set milisekund při spouštění jednou za několik dní prý nepozná, stejně jako úsporu paměti při více než stovce kontejnerů, a dodává, že u OrbStacku je pro něj klíčové rychlé bind mountování, o kterém Kiri mlčí.

Další linka řeší architekturu a názvosloví. Uživatel i_v popisuje, že agent v hostu funguje tak trochu jako init a unikernel a ptá se, jestli Kiri implementuje celý vlastní runtime, nebo vzadu používá containerd. Uživatel 5G_activated si stěžuje, že se pletou pojmy engine, runtime, manažer a desktopová aplikace, a Kiri mu připadá jako nová desktopová aplikace, která se tváří jako runtime. Uživatel gempir se pak přímo ptá, jaké architektonické rozhodnutí má ten osminásobný náskok vůbec umožnit.

Nejostřejší výtku přinesl uživatel binsquare, který udržuje vlastní smolvm. Tvrdí, že test docker run --rm alpine true s již staženým obrazem měří v podstatě jen teplý start přes stejné docker CLI, a upozorňuje na odkládaný úklid po skončení kontejneru, který může při chybě tiše hromadit nepořádek. Jinak vlákno odlehčují jména: uživatel ksajadi chválí perské jméno, uživatel wiether připomíná, že Kiri je ve Francii značka dětského sýra, a uživatel sercant si utahuje z věty, že měřená čísla grafy brzy nahradí. Několik hlasů pak web označuje za vygenerovaný kýč s okázalými animacemi.

Kdo hledá náhradu Docker Desktopu na Macu, ten si z vlákna odnese hlavně otázku, jestli mu jde o milisekundy při startu, nebo o svižné mounty a zaběhlou každodenní rutinu.
