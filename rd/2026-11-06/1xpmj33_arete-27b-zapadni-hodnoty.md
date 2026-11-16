# 1xpmj33
**Arete-27B: NousResearch přeučil Qwen na západní hodnoty**

r/LocalLLaMA · u/jacek2023 · 6. listopadu 2026, 20:58 · 216 bodů / 228 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xpmj33/)

Laboratoř NousResearch vzala 27miliardový model Qwen3.8-27B od Alibaby a čistě doladěním pod dohledem z něj udělala Arete-27B, který má místo čínského pohledu vyznávat západní hodnoty. V původním Qwenu firma pozorovala odmítání, uhýbání a odpovědi rámované optikou čínského státu na politicky citlivá témata. Novinka je určená pro běžnou asistenci a agentskou práci uživatelům, kteří právě takovou změnu pohledu chtějí, a pro výzkum toho, jak post-training mění chování modelu.

Ve vlastním měření laboratoř oddělila faktickou přesnost od framingu, tedy toho, zda model přebírá výklad čínského státu za svůj. Faktické skóre se mělo zvednout z 2,32 na 2,98 z 5 a podíl odpovědí s propagandou klesnout z 22 na 0,9 procenta, a to ve všech sedmi sledovaných kategoriích od svobody projevu přes vztah státu a trhu až po demokracii, vzdělávání, soukromí a klimatickou politiku. Trénovalo se jen metodou SFT, bez posilovacího učení a bez zásahu do architektury, a podle firmy bez citelného propadu v obecných a agentských testech.

Nejvýše hodnocená reakce udala tón celé diskuse: u/Icy-Degree6161 se ptá, jestli jen nevyměnili východní propagandu za západní. Na to navazuje u/VotZeFuk úšklebkem nad slovním spojením západní hodnoty a hláškou o tom, že zase dělají z žab homosexuály. Podobně u/Southern-Chain-6485 rýpe, že celá evaluační sada propagandy je vlastně jen o Číně, a ptá se, v čem přesně tohle mají být západní hodnoty v jakkoli volném smyslu.

Věcnější linka řeší, k čemu to vlastně je. u/cinnapear tvrdí, že Qwen mu nikdy žádnou propagandu neservíroval a přijde mu už teď dost západní, u/Zombiecidialfreak pak zajímá jediné: jestli to znamená méně odmítnutí u věcí, které se Číně nelíbí, a model prostě udělá, co po něm chce. u/Keleion přemýšlí, jak se novinka srovná s abliterovanými modely, a vidí jeden praktický prodejní argument, že američtí šéfové budou mít k nasazení v práci přívětivější vztah, zatímco u/CroquetteLauncher se ptá, zda by každá země nebo kontext neměly mít vlastní alignment, když vztah státu a trhu vypadá úplně jinak ve Francii a v USA.

Nejsilnější vtipy míří na dvojí metr. u/binary píše, že včera ho Qwen nutil před unit testy odrecitovat čtyři uvědomění a stejný prompt tady vyžaduje jen slib věrnosti vlajce. u/Littlepharaoh to rozepsal jako parodické uvažování modelu, který genocidu u protivníka označí za genocidu a volá po sankcích, u Izraele ale přepne na složitou situaci, právo na sebeobranu a hluboké znepokojení, načež detektor propagandy zahlásí 0,9 procenta a žádnou zaujatost nenajde. Do toho u/tengo_harambe utrousil, že laboratoř neuměla vylepšit kódování, tak zvolila snadnou performativní cestu.

Z vlákna tak nakonec nejvíc zůstává otázka, zda otevřené váhy mají sloužit datové suverenitě každého uživatele, nebo se jen přetahují mezi dvěma tábory převýchovy.
