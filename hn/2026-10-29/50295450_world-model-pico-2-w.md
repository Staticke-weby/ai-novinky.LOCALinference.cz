# 50295450
**World model na Raspberry Pi Pico: hra se sní a hraje sama**

Hacker News · airinei · 29. října 2026, 21:32 · 175 bodů / 10 komentářů · [diskuse](https://news.ycombinator.com/item?id=50295450)

Na mikrokontroleru Raspberry Pi Pico 2 W běží dvě miniaturní neuronové sítě, které se navzájem sní a hrají. První síť funguje jako svět: z aktuálního snímku a akce předpoví další snímek a odměnu, druhá síť jako hráč z vygenerovaného snímku vybere tah. Autor projektu tinyworldformer sáhl po looped transformeru, který opakovaně používá stejné váhy a šetří paměť, a rozběhal tak přímo na desce varianty Breakout, Doom, Flappy a Pong.

Svět má podle popisu na GitHubu 26–131 tisíc parametrů podle hry a herec jen 9–16 tisíc, jeden snímek světa stojí 2–8 milionů operací. Na čipu přitom nikdy neběží skutečná hra: herec vidí jen snímky ze snu a svět dostává jen jeho akce, obě sítě běží na jednom jádře čipu RP2350, zatímco druhé jádro řeší USB a displej. Později autor přidal streaming reinforcement learning, takže se čerstvý agent učí hrát od nuly uvnitř vlastního snu, stisk tlačítka ale kdykoliv předá řízení člověku.

Diskuse se nejdřív rozjela nadšením z toho, jak deterministicky se síť chová. Uživatel dannyw označil za fascinující, že looped transformer byl potřeba pro mini-Doom, ale ne pro jednodušší hry. Uživatel nater5000 napsal, že právě schopnosti world modelu jsou na tom to nejšílenější a Pico je jen dělá ještě působivějšími, a přemýšlel, jestli by se tahle logika nedala vložit do větší tradiční hry jako procedurální generování, které by se obešlo bez jeho obvyklých neduhů.

Na to navázala otázka, jestli jsou sítě schopné takové přesnosti díky přetrénování a zda je to jeden model pro všechny hry. Uživatel svantana upozornil, že různé počty parametrů a operací naznačují samostatné modely, a mnohem působivější by byl jeden svět, který by si mezi natrénovanými hrami vysnil nové hry. Sám autor vystupující jako sheepseb to potvrdil: pro každou hru je samostatná soběstačná síť, trénovací data se ale s validačními nepřekrývají, a spojit je do jednoho modelu by podle něj bylo snadné.

Nejpraktičtější výměna se týkala tréninku a zneužívání nedokonalostí snu. Na dotaz na hardware autor odpověděl, že svět trénoval na RTX 4060, ale agent hrající hru běžel přímo na Picu. Uživatel xpct se ptal, jestli je herec trénovaný i na chybách světa a neučí se tak vynucovat halucinace, které ho dostanou do snazšího stavu. Závěr obstaralo nedorozumění kolem hardwaru: na otázku, zda to poběží na WebGPU, když to běží na „PI“, odpověděl uživatel jbarberu, že Pico 2 W není počítač, ale mikrokontrolér, který běží na holém železe nebo s RTOS.

Z malého čipu se tak stává laboratoř celé myšlenky world modelů: hra, hráč i učení se vejdou do pár set kilobajtů a sen je dost věrný na to, aby se v něm dalo hrát.
