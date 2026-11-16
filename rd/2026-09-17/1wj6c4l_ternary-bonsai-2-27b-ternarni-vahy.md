# 1wj6c4l
**Ternary Bonsai 2: 27B model pod 6 GB s ternárními váhami**

r/LocalLLaMA · u/xenovatech · 17. září 2026, 23:05 · 1654 bodů / 342 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wj6c4l/ternary_bonsai_2_27b_just_released_on_hugging/)

Na Hugging Face vyšel Ternary Bonsai 2 s 27 miliardami parametrů. Vychází z modelu Qwen3.8-27B, architektura zůstala stejná, ale díky ternárním vahám se vejde pod 6 GB. Spustit se dá lokálně, a to i přímo v prohlížeči přes WebGPU.

Karta modelu slibuje, že je devětkrát menší než FP16 verze a zachovává si 98,2 % inteligence. Autor příspěvku odkazuje na kolekci modelů Bonsai 2 a na demoverzi, která běží právě přes WebGPU kernelech.

Právě číslo 98,2 % se stalo hlavním terčem diskuse. Nejvýše hodnocený komentář od u/Embarrassed_Adagio28 o něm vážně pochybuje, ale dodává, že model vyzkouší. u/crapaud_dindon k tomu poznamenává, že to bude nejspíš 98 % oproti dvoubitové kvantizaci, u/Due-Memory-6957 míní, že modelu stačí porazit menší modely podobné velikosti, a u/McBonderson se ptá, co 98 % inteligence vůbec znamená. Nedůvěru přiživuje u/BumbleSlob vzpomínkou na minulé sliby tvůrců, které označuje za směšně mylné.

Oproti tomu praktická linka vlákna model vítá. u/Illustrious-Row2751 píše, že ho zajímá víc než další obří model s biliony parametrů, který si doma nespustí. u/Rye2-D2 oceňuje, že ternární modely míří na 16GB grafické karty, zatímco ostatní podle něj cílí buď na 24 GB a víc, nebo na 8 GB a míň, s výjimkou GPT-OSS 20B.

První testy z komunity jsou rozporuplné. u/kayox chválí povedený test se šachovnicí v SVG a na RTX 3090 naměřil průměrných 56 tokenů za sekundu. u/ithinkitslupis nechal model vygenerovat kód, výsledek označil za slušný, ale upozornil, že model na to spotřeboval asi 20 tisíc tokenů uvažování a úkol v něm prakticky sedmkrát zopakoval. Naopak u/rJohn420 popisuje, že se model při dotazech na Rust v demoverzi zacyklil, a podobné zacyklení hned na první prompt hlásí i u/letsgoiowa, podle kterého pomůže výrazně upravit penalizaci opakování nebo vypnout uvažování.
