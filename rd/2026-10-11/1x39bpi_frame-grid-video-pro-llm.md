# 1x39bpi
**Frame-Grid: formát, díky kterému LLM „vidí“ video bez serveru**

r/ClaudeAI · u/Khamubro · 11. října 2026, 16:16 · 273 bodů / 41 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1x39bpi/)

Autor u/Khamubro přiznává, že neumí napsat ani řádek kódu, specifikaci ale navrhl sám a celé programování nechal na Claudovi. Výsledkem je Frame-Grid: nástroj, který z kamery, nahraného videa nebo GIFu udělá sekvenční mřížku očíslovaných snímků v jednom PNG, maximálně v dávce dvaceti obrázků, aby si je jazykový model mohl „přečíst“ jako video. Vše drží takzvaná filozofie Xinu, tedy obráceného Unixu: jediný soubor, prohlížeč, offline a bez externích závislostí.

Odkazovaná stránka projektu slibuje, že nic neopouští počítač a nic se nemusí instalovat. Umí nastavit snímkovou frekvenci, velikost i rozměry mřížky, přidat titulky ze souborů .srt a .vtt přímo do snímků i do textového přepisu, filtrovat téměř stejné snímky a ke každému snímku volitelně přidat strukturální otisk ElasticTOK. GIFy dekóduje nativním rozhraním prohlížeče se záložním vlastním parserem a kód je zdarma na GitHubu pod křídly ConsciousNode SoftWorks.

Diskuse se rychle stočila k otázce, jestli autor nevynalezl kolo. Nejvíc hlasů posbíral u/DeliciousGorilla s odkazem na velmi podobný projekt cdaf včetně vědeckého článku, u/cuddlingisfun se ptá, zda by to samé nezvládl ffmpeg, a u/jacksterson vtipkuje, že stačí Claudovi říct a skript napíše sám. Do stejného rohu míří i u/CPSiegen: výchozí demo prý jen rovnoměrně vzorkuje snímky do mřížky, což digitální video umí odjakživa.

Právě u/CPSiegen ale přidal i nejvěcnější kritiku, když si stěžoval na nepřístupný web v mobilním tmavém režimu s drobnými prvky a mizerným kontrastem, za což podle něj mohou nehlídané modely. u/AncientGrief navrhuje místo mřížek dát umělé inteligenci rovnou přístup k ffmpeg, u/grr5000 podotýká, že streamovací služby něco podobného už dnes dělají. Automatické shrnutí od u/ClaudeAI-mod-bot pak konstatuje, že autorovi pomohla hlavně obhajoba: aplikace je zdarma, běží na klientovi a šetří tokeny, což jednoho z hlavních kritiků nakonec obrátilo.

Zbytek vlákna řeší, k čemu je to vlastně dobré. u/papayax999 se ptá, zda takhle půjde Clauda naučit něco ve formátu videa, u/BlueFrozenSoul řeší hodinová videa a to, zda k mřížce nebude potřeba ještě přepis zvuku. Nejzamilovaněji to podal u/muhuhaha, který chtěl, aby Claude „prožíval“ filmy postupně s napětím a překvapením, místo aby je dostával najednou jako synopsi. Odlehčení dodali u/beerdude26 hláškou, že jsme se kruhem vrátili k filmovým pásům, jen digitálně, a u/theycallmeslayer s poněkud drsným vtipem, co teď bude muset Claude zhlédnout.

Není to převrat, spíš šikovná zkratka: když modelu nemůžete poslat video, pošlete mu jeho papírový kontakták.
