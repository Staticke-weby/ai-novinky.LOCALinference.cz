# 1xr2aaa
**Tencent představil DSpine. Spekulativní dekódování má zrychlit 27B modely**

r/LocalLLaMA · u/emdeka87 · 8. listopadu 2026, 17:23 · 222 bodů / 25 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xr2aaa/)

Tencent zveřejnil novou metodu spekulativního dekódování DSpine pro modely Qwen3.8-27B. Podle autorova shrnutí má přinést až trojnásobné zrychlení generování a odkaz míří na variantu Qwen3.8-27B-DSpine na Hugging Face. Načasování řada lidí čte jako přípravu na příchod Qwen4.

Nejkonkrétnější čísla zatím přinesl u/BringTea_666, který metodu zkouší ve vlastním enginu pro RTX 5090 se střední kvantizací kolem Q5. Bez uvažování naměřil zhruba 420 tokenů za sekundu s DFlash2 proti 800 tokenům za sekundu s DSpine, tedy skoro dvojnásobek. V reasoning režimu se ale poměr otočil, 320 tokenů za sekundu s DFlash2 proti 280 tokenům s DSpine, což vysvětluje menší jistotou prvních jednoho až dvou tokenů a věří, že by to šlo dotrénovat během několika dnů.

Opoznaný optimismus přinesl u/valdev, který DSpine nasazoval do LumaBrowseru kvůli přímému srovnání s MTP. Po prvních testech hlásil, že nenašel jediný scénář, kde by byla metoda v llama.cpp rychlejší než DFlash2, a navíc vyžaduje více paměti. Po dokončení benchmarků svůj závěr potvrdil, v llama.cpp je podle něj znatelně horší bez jakéhokoliv přínosu, v SGLang to ale může dopadnout jinak.

Zbytek vlákna tak spíš sbírá střípky a čeká na další měření. u/Present_Resource4022 trefně poznamenal, že je to ideální týden na vydání, u/KillerX629 se rovnou ptal, jak si DSpine stojí proti DFlash2, a u/pmttyji odkázal na souběžné vlákno s detaily ke studii o paralelním draftování a podmínění skrze hloubku.

Zatím to vypadá, že přínos DSpine hodně závisí na enginu, kvantizaci a zapnutém uvažování, takže jediné číslo o zrychlení nestačí.
