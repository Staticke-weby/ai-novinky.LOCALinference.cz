# 1xl3yxo
**Lokální Qwen 3.8 27B prolomil reCAPTCHA. Captcha už modely nezastaví**

r/LocalLLM · u/Undreren · 1. listopadu 2026, 15:08 · 632 bodů / 86 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xl3yxo/)

Lokálně běžící Qwen 3.8 27B si sám poradil s reCAPTCHou a v klidu pokračoval v práci. Autor ho propojil s prohlížečem v prostředí oMLX přes MCP, protože běžné stahování stránek na webech plných JavaScriptu vracelo prázdné výsledky. Když se modelu zeptal na novinky kolem Gemma 5, na chvíli se podíval jinam – a po návratu zjistil, že překážku prostě přeskočil. Model mu v kvantizaci Q6 běží rychlostí kolem 75 tokenů za sekundu, kvůli čemuž prý úplně zrušil soukromé předplatné Cursoru, a pokud bude Qwen4 ještě znatelně lepší, cloudové modely už nebude potřebovat vůbec.

Největší ohlas sklidila upřímná nenávist ke captchám. u/OvertaxedOne doufá, že je tohle jejich konec, protože se staly tak absurdními, že v nich chybuje už v polovině případů: každé políčko s kolem, v každém rohu kousek pneumatiky, a člověk jen tápe, jestli ho má zaškrtnout. u/Keepcompany-DEV k tomu dodává, že captcha nikdy neměla skutečně ověřovat lidství, ale byla snadnou cestou, jak nechat lidi zdarma vytvářet rozpoznávací sady. A u/05-nery to shrnuje lakonicky, že captchy zkrátka nebyly stavěné proti jazykovým modelům. u/BrightCandle přiznává, že některé reCAPTCHy jsou dnes tak matoucí, že je řeší umělou inteligencí i on.

Druhá linka diskuse se točí kolem toho, že lokální modely už na každodenní práci stačí. u/mmazing píše, že Qwen používá jako hlavního kódovacího agenta od verze 3.6 a pro schopného inženýra, který si cení soukromí, je to víc než dost. u/Spanish_bret žasne nad tím, jak model v myšlenkových blocích projde captchou jako by to bylo úterý, a právě to je prý důkaz, že na běžnou práci už nejsou cloudová předplatná potřeba. Nejvtipnější hlášku přihodil u/WinPrudent2132, když Qwena překřtil na Qwené Descartese s výrokem „Myslím, tedy nejsem robot".

Zbytek vlákna řeší technické detaily. Lidé se vyptávají, jaký harness a jaký přístup k prohlížeči autor používá, protože jejich vlastní sestavy s nástroji pro anonymní prohlížení žerou kontextové okno. u/Cacoda1mon přemýšlí, jestli zaškrtávací reCAPTCHA není jen výpočetní úkol, který vyřeší sám prohlížeč, a u/TheNovelBondrewd upozorňuje, že existuje upravený Qwen menší než 10B doladěný přímo na obcházení několika druhů captch. Skeptičtější tón vnesl u/sophware, který si Qwen 3.8 vyzkoušel na otázkách kolem záložních firewallů a narazil na zásadní selhání tam, kde Fable 5.1 obstál – a ptá se, na jakém hardwaru vůbec utáhne někdo Q6 rychlostí 75 tokenů za sekundu.

Captche přestávají být zdí a stávají se spíš zpomalovacím prahem, který lokální model přeskočí po cestě za něčím jiným.
