# 1x4y61f
**Qwen 27B běží na jailbreaknuté konzoli PS5**

r/LocalLLM · u/AdIllustrious7246 · 13. října 2026, 16:29 · 700 bodů / 92 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1x4y61f/)

Vývojář se inspiroval projektem PS5LM od u/metover a pořádně ho předělal. Zatímco původní port běžel jako payload na procesoru s asi 6 GiB paměti, jeho fork spouští llama.cpp jako nativní aplikaci pro PS5 na grafice přes Vulkan. Díky tomu má k dispozici zhruba 11,4 GiB paměti a zvládne výrazně větší modely: Qwen 3.8 27B dává kolem 20 tok/s, Gemma 4 E4B asi 61 tok/s a Llama 3.2 3B kolem 124 tok/s. Součástí je dashboard na televizi s výkonem a teplotami, knihovna modelů, stahování z Hugging Face s kontrolou i chat z jakéhokoli zařízení přes webové rozhraní a API.

Největší ohlas sklidilo samotné překvapení, že konzole tak velký model vůbec utáhne. u/Fusseldieb přiznává, že 27B vůbec nečekal, a vtipkuje, že tomu média zajistí pozornost a ceny konzolí vyletí nahoru. Na to navazuje nejvýše hodnocený komentář od u/spyputs1, ať to autor raději hned smaže, protože sehnat PS5 je kvůli GTA 6 těžké už teď. u/NecessaryButFatal z toho vyvozuje, že novým modem budou clustery z PS5, a u/aiyakisoba rovnou navrhuje naskládat jich pět na sebe.

Vážnější linka diskuse se stočila ke kvantizaci. u/LooseBackHole si stěžuje, že bez uvedení kvantizace v titulku to nedává smysl, protože o běh v Q2 nikdo nestojí, a u/separatelyrepeatedly přitvrzuje, že cokoli pod q4 je k ničemu. Smířlivěji to bere u/hurrdurrmeh, jehož nadšení sice s IQ2 opadlo, ale zajímá ho, jestli by rychlé SSD konzole nepomohlo s odkládáním a umožnilo kvalitnější IQ3 až IQ4. u/giveen pak nadhazuje vyzkoušet EXL3, se kterou by si Qwen mohl při malé velikosti uchovat víc kvality.

Zbytek vlákna chválí zpracování a řeší praktické detaily. u/INeatFreak píše, že rozhraní vypadá lépe než 90 % komerčních aplikací, a u/Max_skyl1n3 připomíná vlastní pokusy s modely na PS4 pod Linuxem, kde ho se 4 GB paměti po pár zprávách vždycky shodil ovladač grafiky. Objevují se i zvědavé dotazy na prefill, na verzi pro PS5 Pro nebo na to, jak autor u 27B modelu dosáhl 64tisícového kontextu, a u/SethBrayman se ptá, jaké běžné grafice výkon konzole odpovídá.
