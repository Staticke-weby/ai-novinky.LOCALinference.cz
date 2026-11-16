# 50458166
**Huawei vydal MACaQ. Kvantizuje 122B model za 64 minut**

Hacker News · thefox96 · 11. listopadu 2026, 21:23 · 81 bodů / 23 komentářů · [diskuse](https://news.ycombinator.com/item?id=50458166)

Huawei zveřejnil MACaQ, otevřený a modelově agnostický kvantizér pro lokální inferenci textu, obrázků, videa i audia. Láká na to, že 122B model zvládne zkomprimovat za 64 minut s pouhými 32,5 GB paměti zařízení.

Repozitář na GitHubu popisuje podporu pro llama.cpp s 2/3/4bitovými formáty GGUF, dále vLLM, Diffusers, PyTorch a Ascend. Autoři slibují nižší perplexitu než MR-GPTQ a DuQuant++, případně stejnou kvalitu jako nejlepší výsledek konkurence u Llama-3-8B s jedenáctkrát kratším časem kvantizace. K projektu patří paper na arXivu 2611.10649 a kolekce modelů na Hugging Face.

Nejživější vlákno se ale nejdřív chytlo samotného jména. Uživatel utternerd suše poznamenal, jaký to je název projektu, a QuantumNomad_ to rozvedl domněnkou, že odkazuje na makaky. Ostatní si z toho udělali legraci o dostatečném zapření a o tom, že by makakům tohle přivlastnění jména nevadilo.

Vážnější debatu otevřel Rabbit504030201 otázkou, proč lidé na HN raději odkazují na GitHub než na oficiální stránku, když Huawei podléhá sankcím a cokoli hostované mimo Čínu může kdykoli zmizet. Uživatel nout oponoval, že na GitHubu hned vidí kód a ví, kam kliknout, zatímco produktové stránky zdržují marketingovými obrázky a videi. Uživatel lukasc-ch doplnil, že řada repozitářů firmy je tam už dlouho, a ptal se, proč by se měly sankcionovat věci dávané zadarmo.

Praktickou linku přinesl dotaz, zda vyšel i nějaký hotový model a jestli se to hodí pro Stratu. Uživatel minraws odpověděl, že pro Qwen 3.8 27B už kvantizace ve verzi MACaQ existuje, a lukasc-ch přidal odkaz na Reddit, kde lidé metodu reprodukují a tvoří vlastní GGUF soubory. Z papírových slibů se tak podle diskuse rychle stává věc, kterou si komunita kolem lokálních modelů zkouší na vlastní hardware.
