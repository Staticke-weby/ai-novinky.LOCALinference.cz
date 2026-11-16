# 50167617
**Jev Cards: lidský kvíz proti vision modelu**

Hacker News · totisjosema · 20. října 2026, 17:11 · 58 bodů / 49 komentářů · [diskuse](https://news.ycombinator.com/item?id=50167617)

Vývojář totisjosema postavil kvízovou hru Jev Cards kolem vision modelu Jev od TypeSafe. Model dostane stejný obrázek jako hráč a otázku, na kterou odpoví nebo ťukne na správné místo přibližně za čtvrt sekundy. Hrát se dá sólo se žebříčkem pro každý režim, nebo živě s přáteli, kde je Jev dalším protihráčem. Kód je otevřený na GitHubu, karty autor vytvořil od nuly pomocí vision modelů Opper a Claude Code, a i když pracuje v Opper, hra je zdarma a otevřená všem.

Nejčastější zážitek z diskuse je pokora. Inerte přiznává, že měl špatně asi polovinu odpovědí, a i když trefil správně, Jev byl pořád rychlejší. Autor ho utěšuje vlastní statistikou z prvních dvou set karet, kde měl model 160 správně s mediánem 261 milisekund. Podobně to vidí edaemon: Jev je sice jednoznačně rychlejší, ale chyboval znatelně častěji než on, a arm32 to shrnuje hláškou o hodu mincí.

Zaujaly hlavně postřehy ke skórování, kde rychlost přebíjí přesnost. Jrflo popisuje, jak dal ve sprintu stoprocentně za asi 45 sekund, a pak jen zběsile proklikal a s dvaceti procenty úspěšnosti byl časem na 42 sekundách technicky lepší. Autor slíbil zvýšit trest za chybu a žebříček vynulovat. V podobném duchu se diví geooff_, že prohrál s deseti z deseti proti osmi z deseti na straně modelu, a TZubiri, že při sedmi z deseti proti šesti z deseti vyhrál Jev, asi kvůli sto sekundám proti šedesáti. Autor vysvětluje, že model odpovídá v průměru za dvě až tři sta milisekund a hra odměňuje rychlost s přesností, zatímco chyba přidá patnáct sekund.

Casey2 nejdřív pohořel, když dal pět a Jev nulu v řadě, ale pak aplikace hlásila, že Jev vyhrál 2 613 z 3 300 her. Po patnácti správných dodává, že kdo úlohu už viděl, odpoví rychle taky, takže smysl je spíš v úlohách, kde stačí i poloviční přesnost, ale musí být vyřešeny okamžitě. Drivers99 si všímá, že v režimu proti sobě rozhoduje i čas, když při deseti z deseti proti sedmi z deseti bral 1 201 bodů proti 1 034, přičemž jedna jeho odpověď trvala 9,6 sekundy proti 0,3 sekundy.

Vedle taktiky se řeší i konkrétní karty a chyby. Nextaccountic prosí o možnost vypnout otázky z hudební teorie, kde může jen náhodně klikat, coolThingsFirst se diví, že kosatka je delfín, a joshstrange přiznává, že Jev porazil, ale šipkový terč neumí přečíst vůbec. Podnami to shrnuje jako čistou zábavu na 62 sekund, než zjistil, jak je špatný. Kritičtější hlasy mluví o nejasném ovládání u grafů a šachové úlohy, kde bylo potřeba ťuknout na cílové pole místo tahu figurkou, nebo o otázce s neviditelným správným tlačítkem. Darepublic naopak chválí, že stránka je vkusná a svižná na mobilu.

Z Jev Cards se tak vyklubal hlavně rychlý test lidské ješitnosti: proti stroji, který odpoví za mrknutí oka, člověk občas vyhraje na přesnost, málokdy na čas.
