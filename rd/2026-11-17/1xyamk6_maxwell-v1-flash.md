# 1xyamk6
**Maxwell-V1-Flash: 35 miliard parametrů, 3 aktivní a kontext 256 tisíc tokenů**

r/LocalLLaMA · u/pmttyji · 17. listopadu 2026, 05:04 · 334 bodů / 59 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xyamk6/)

Maxwell Team představil Maxwell-V1.0-Flash, směs expertů s 35 miliardami parametrů celkem a 3 miliardami aktivních na token. Model zvládne kontext až 256 tisíc tokenů a míří na silné uvažování, agenty a práci s dlouhým kontextem při únosných nákladech inference.

Odkazovaná technická zpráva stojí na pozornosti Maxwell Block Sparse Attention, která drží fixních 8 prefixových a 8 lokálních bloků po 128 tokenech a přidává až 16 vzdálených bloků vybraných učeným indexerem. Její jádro je při 256K o 6,7x rychlejší než hustá GQA, trénink běžel na zhruba 26 bilionech vícejazyčných tokenů s optimalizérem Muon a ladění spojilo dvoustupňové SFT, samostatné RL větve a multi-teacher on-policy distilaci.

Nejčastější otázku vlákna položil u/Dabalam, jestli jde o doladěný Qwen v trenčkotu, nebo skutečně nový model. Odpověď komunity se rychle přiklonila k druhé variantě, u/Witty_Mycologist_995 přiznává, že si nejdřív myslel totéž, ale mýlil se, podobně to vidí u/CodeCatto a u/True_Requirement_891 slaví konečně novou architekturu. Nadšení podpořil u/ApprehensiveTart3158, podle kterého jde o nový model ze Singapuru s překvapivě silnými benchmarky.

Druhá linka se točí kolem paměti. u/wombweed chválí šokující vysoká skóre a lákavou řídkou pozornost, ale zajímá ho, kolik zabere KV cache v plném kontextu v bf16 proti Qwen 3.6 nebo Gemma 4, a mrzí ho chybějící podpora v llama.cpp pro offloading expertů na procesor. u/Gohab2001 odhaduje cache na 4,5násobek Qwen 3.5 35B, tedy skoro 24 GB při 256 tisících tokenech, a u/EvolvingDior se ptá na cenu VRAM na token kontextu. u/Marcuss2 v tom vidí vzorec nových laboratoří, které přijdou se skvělými čísly, ale s nenasytnou cache, již pak v další verzi opraví.

Třetí proud řeší, jak model reálně rozběhnout. u/Old-Fix-9 se ptá prostě na GGUF, u/Atagor a u/TokenLearner doufají v podporu ve Strata, u/xkalibur3 by chtěl verzi nvfp4 s MTP a u/keylimesoda odkazuje na rychlý start a vyhlíží komunitní kvantizace. První zkušenost přidal u/JAlbrethsen, který zkusil kvantizaci q4 a chválí, že u jednoduchých dotazů skoro neuvažuje a u složitých se rozepsaně rozjede, takže ho plánuje nasadit jako lokálního subagenta pro kódování. u/akumaburn mezitím sdílel necenzurovanou variantu Heretic a její SmoothQuant verzi.

Z vlákna tak vychází silný nováček s velkorysým kontextem, jehož největší otazník zatím není výkon, ale velikost cache a dostupnost úsporných formátů pro domácí stroje.
