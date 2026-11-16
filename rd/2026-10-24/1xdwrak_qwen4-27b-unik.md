# 1xdwrak
**Qwen4-27B unikl přes pull request. Napovídá to termínu vydání**

r/LocalLLaMA · u/brainExploded99 · 24. října 2026, 04:16 · 606 bodů / 220 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xdwrak/)

Uživatel u/brainExploded99 upozornil na pull request číslo 22 v repozitáři analytics-zoo/vllm-xpu-kernels, který pracuje s označením Qwen4-27B. Podle něj autor requestu dlouhodobě přispívá do intelovských repozitářů a do vLLM a předtím dělal na Qwen3.8. Jméno má navíc sdílet s člověkem spojovaným s vedením v Alibabě a se Zhejiang Lab. Z kódu autor příspěvku vyčetl, že velikost KV cache se u nového sedmadvacetimiliardového modelu nesnižuje, což by se projevilo hlavně na paměťových nárocích při dlouhém kontextu.

Nadšení v diskusi je okamžité. u/Dangerous_Bid2935 píše, že se vyloženě třese na Qwen 4 Flash, protože už Qwen 3.8 Flash Next je podle něj neuvěřitelný model. u/ttkciar v tom vidí dobré znamení a doufá, že přijdou i Qwen4-4B, Qwen4-9B a Qwen4-14B. u/Goldkoron zase sní o tom, že řada Qwen4 zdědí část schopností 3D modelování a animace, jaké umí Opus 5.5. Jiní už řeší praktickou stránku: u/Dwedit se ptá po MoE variantě a chválí, jak dobře běží kvantovaný 35B A3B na pouhých 6 GB VRAM.

Vedle toho se rozjela detektivní linka kolem důvěryhodnosti. u/Alternative_You3585 upozorňuje na bezejmenný repozitář bez hvězdiček a se sedmi sledujícími a bojí se, že jde o šum, i když by mu přišlo vtipné, kdyby Alibaba používala Codex, kterým je request označený. Oproti tomu u/Nearby-Hospital9830 argumentuje, že zmínky o nevydané architektuře přímo v hardwarově specifickém repozitáři působí divoce, ale vzhledem k autorově historii u Intelu a vLLM to vypadá jako legitimní časný signál. Opatrnější u/ceygull oponuje, že takové kernelové requesty občas používají jen zástupné názvosloví pro testování nových rozměrů architektury, takže číslo 27B může být interní testovací konfigurace.

Nejvíc se ale řeší právě KV cache. u/MiaIsOut stručně shrnuje pointu slovy o nezměněné velikosti a u/MerePotato dodává, že i tak zůstává natěšený. u/mikumikubeeeeaaaammm to bere s nadsázkou a prosí bohy Qwenu o menší cache. Věcněji na to jde u/Thomasedv, kterému pomohlo streamování KV cache a její přesun do běžné RAM, díky čemuž mohl na kartě 3090 zvednout kvantizaci Qwen3.8 a doufá, že totéž půjde i u Qwen4. A u/CiobanuXashi z ploché cache vyvozuje, že pokrok se musel přesunout jinam, nejspíš do velikosti kontextového okna.

Pokud se stopa v kernelovém repozitáři potvrdí, komunita už má jasno, co bude sledovat: kdy přijdou váhy, jaké budou menší velikosti a kolik paměti spolkne dlouhý kontext.
