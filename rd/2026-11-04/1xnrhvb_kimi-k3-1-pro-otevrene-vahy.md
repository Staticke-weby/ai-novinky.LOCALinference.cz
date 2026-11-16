# 1xnrhvb
**Kimi K3.1 Pro: 2,8 bilionu parametrů s otevřenými váhami a licencí bez háčků**

r/LocalLLaMA · u/ApprehensiveAd3629 · 4. listopadu 2026, 16:44 · 1278 bodů / 239 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xnrhvb/)

Moonshot AI vydal Kimi K3.1 Pro, svůj dosud nejschopnější model třídy 3T. Jde o otevřené váhy s architekturou Mixture-of-Experts o 2,8 bilionu parametrů celkem a 104 miliardách aktivovaných na token, s nativní multimodalitou a kontextovým oknem milion tokenů. Model vznikl dotrénováním Kimi K3 rozsáhlým společným reinforcement learningem napříč stovkami oblastí a má výrazně zlepšit kódování, tvorbu 3D, finanční výzkum i agentní schopnosti.

Karta modelu na Hugging Face slibuje běh přes vLLM, SGLang a TokenSpeed a nasazení přes API pod názvem kimi-k3.1-pro s nastavitelnou mírou uvažování. Největší pozornost ale budí licence Kimi K3.1 Pro: osobní použití povoluje bez omezení a ke komerčnímu stačí atribuce, s dodatečným omezením jen pro poskytovatele API. V tabulce výsledků se model porovnává s Claude Fable 5.1, GPT-6 Astra nebo Claude Opus 5.5 a hlásí třeba 65,7 v Terminal-Bench 4.0 nebo 92,1 v BrowseComp.

Právě licenci komunita řeší nejvíc. u/FriskyFennecFox ji označil za naprosto šílenou v dobrém slova smyslu, protože kromě atribuce pro komerční použití nemá další omezovače. u/OnlineParacosm k tomu dodal, že firma vyslyšela zpětnou vazbu a opustila jednu z nejhorších licencí, jaké kdy viděl, což byla podle něj jediná cesta vpřed. Stejný uživatel popsal vlastní zkušenost, kdy ho jeden náročný úkol vyšel zhruba na 30 dolarů oproti asi 10 dolarům na GLM 5.3 Flash, ale Kimi ho zvládla asi desetkrát rychleji.

Zbytek vlákna se nese v duchu sebeironie majitelů slabého hardwaru. u/Diabolicor hlásí, že jeho GTX 1030 je připravena, u/countermike se ptá, jestli model poběží na třistaosmdesátšestce se 640 kB paměti, a u/mrinterweb si stěžuje, že se mu model nenačítá na Raspberry Pi. u/Vusiwe prosí o slitování, že ještě ani z poloviny nestáhl Mistral Large, a u/Monofart to uzavírá vyhlídkou, že tohle budou naše děti pouštět na iPadu mini.

Vážnější linka počítá, co by provoz reálně znamenal. u/Daniel_H212 odhaduje nativní čtyřbitovou kvantizaci na 1,56 TB, tedy cluster čtyř Mac Studií s 512 GB paměti za cenu kolem 89 200 dolarů. u/redditnosedive se proto ptá na realistické nároky při nízké kvantizaci a u/lxe se spokojí, až se model ořeže do bramborové kvality spustitelné na malině. Naděje se upínají i jinam: u/IsopodMysterious9125 spekuluje, že přípona Pro naznačuje příchod odlehčené Flash verze, a u/Fusseldieb doufá, že někdo šikovný model destiluje pro ostatní.

Otevřené váhy v tomhle případě neznamenají, že si třítunový model pustíte doma, ale že ho komunita může zkoumat, destilovat a stavět na něm bez strachu z licence.
