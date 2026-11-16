# 1xff9e4
**CrowdGPT: LLM trénovaný davem bez datacenter**

r/LocalLLaMA · u/Vxtzq1 · 25. října 2026, 23:07 · 312 bodů / 94 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xff9e4/)

Autor vyvíjí CrowdGPT, jazykový model s miliardou parametrů, který se má trénovat po částech na počítačích dobrovolníků, bez datacenter a milionových rozpočtů obvyklých u velkých firem. Na rozdíl od amerických a čínských laboratoří slibuje zveřejnit nejen váhy, ale i sto procent trénovacích dat, a dát každému možnost data dodávat a mluvit do směřování projektu. Současná velikost je podle něj jen proof of concept, větší a lepší verze má přijít později.

Jádro diskuse tvoří obava z otravy dat a zadních vrátek. Nejvýše hodnocený komentář od u/Fit-Produce420 varuje, že k prolomení stačí pár příspěvků, protože k tomu stačí malé procento parametrů rozprostřených náhodně. Na něj navazuje u/CiobanuXashi, kterého právě tohle odrazuje od zapojení: když nelze prokázat, co každý příspěvek s váhami skutečně udělal, jeden škodlivý aktér vymaže práci celého davu. Do stejné linky zapadá i vtip u/ericw31415, který připomíná pokus trénovat na datech od uživatelů s odkazem na chatbot starý deset let, z něhož se stal rasistický nacista.

Druhá silná linka řeší efektivitu a ekologii. U/offlinesir označuje tvrzení o větší ekologičnosti za šíleně zavádějící, protože spousta malých zařízení jedoucích na domácí elektřinu a spotřebitelské grafiky jen působí čistěji, i když dohromady spolykají víc energie než datacentrum. Podobně to vidí u/synth_mania: distribuovaný trénink bude výrazně méně efektivní než trénink v datacentru, což je v pořádku, pokud jde autorovi o zajímavost a snazší získávání výpočetního času než peněz, ale ne o udržitelnost.

Autor se v příspěvku ptá, co lidem brání přispět, a nadhazuje odměnu v podobě bezplatných inferenčních kreditů na modelu CrowdGPT. Právě to zvedlo ze židle uživatele u/Bleach984, který se ptá, zda autor plánuje prodávat model natrénovaný na cizích kartách a elektřině. Praktičtější radu dává u/bachp, podle něhož by laťku pro vyzkoušení snížil OCI kontejner snadno spustitelný přes podman či docker. U/Trojan_Horse_of_Fate pak projektu radí, aby sháněl hlavně akademické zázemí, katedry informatiky, které ověří technickou proveditelnost, dodají legitimitu a nějaký výkon, a u/captainmadness nadhazuje inspiraci architekturou Folding@home.

Do vlákna vstoupil i moderátor u/ttkciar, který projekt výslovně podpořil jako přesně to, co komunita potřebuje pro dobu, až korporátní laboratoře přestanou rozdávat modely. Opatrnější je u/GeneralMuffins, který upozorňuje na možné právní riziko v Evropské unii: výjimky pro vytěžování textu a dat automaticky nedovolují zveřejňovat chráněné materiály, takže závazek publikovat sto procent dat může být problém.

Z diskuse tak vychází CrowdGPT jako sympatický, ale zatím naivní experiment: davové nadšení naráží na nedůvěru k cizím datům, fyziku distribuovaného tréninku a právo.
