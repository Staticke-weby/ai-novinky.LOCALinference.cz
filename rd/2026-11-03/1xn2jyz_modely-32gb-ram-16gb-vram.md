# 1xn2jyz
**Co rozjede 32 GB RAM a 16 GB VRAM? Gemma 4, Qwen 3.8 a zapomenutý střední segment**

r/LocalLLaMA · u/FormationHeaven · 3. listopadu 2026, 20:28 · 258 bodů / 258 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xn2jyz/)

Autor se po delší pauze vrátil do dění kolem lokálních modelů a nestíhá novinky od Straty po nejnovější rodiny vah. Má doma počítač s 32 GB operační paměti a 16GB grafickou kartou a ptá se, co se na takové sestavě dá dnes smysluplně provozovat jako programátorský pomocník nebo univerzální asistent, když má pocit, že všichni kolem vlastní RTX 6000 a nesmyslně drahé stroje.

Jasným vítězem hlasování se stala Gemma 4 26B A4B. u/BookProper9115 ji označil za bezkonkurenčně nejlepší volbu pro každodenního asistenta, pokud člověk neprogramuje, a přidali se i další. u/TastyStatistician tvrdí, že skvělí pomocníci jsou všechny modely Gemma 4 a že i menší varianta zvládne běh na 16GB notebooku bez grafiky, zatímco u/SigAddict doporučuje vyzkoušet kvantizovanou verzi Gemma-4-12b od Unslotu. Ta se totiž celá vejde do videopaměti, na rozdíl od směsových MoE modelů, které se při odkládání expertů do systémové RAM výrazně zpomalí.

Pro kódování se diskuse opakovaně stáčí ke Qwenu. Padá Qwen 3.8 27B, často ve skromné kvantizaci IQ3_S, i větší Qwen 3.6 35B A3B, se kterým u/Philophon hlásí na 16 GB videopaměti rychlost kolem 5 až 10 tokenů za sekundu. u/smiffy2422 ho na starší 3060 Ti s odkládáním části výpočtu na procesor žene na asi 25 tokenů za sekundu a na programování mu to stačí, pokud modelu dává menší úkoly po kouskách místo zadání typu naprogramuj celou hru najednou. Vedle toho se objevují tipy na Swift 1.5 27B, Ornith 1.5 35B ve dobré kvantizaci, GLM 4.7 Flash nebo specializované kodéry.

Vlastní linku tvoří uživatelé Straty. u/FishingOk3916 radí prostě nainstalovat Stratu a zkusit menší model Gyro, se kterým se na 12 GB videopaměti a 32 GB RAM dostává na 60 tokenů za sekundu. Jiní přes ni pouštějí Qwen pro agentní kódování nebo kombinují lokální RAG s Qwen embeddingem a Gemmou 4 třeba na třídění fotek a dokumentů. u/d0pe-asaurus zase chválí experimentální fork llama.cpp s optimalizacemi pro RDNA a streamováním kontextu z RAM, díky kterému drží na 16GB kartě 50 tokenů za sekundu i s obřím kontextem.

Nejvtipnější část vlákna ale řeší samotné slovo normální v titulku. u/StormMysterious7592 se ptá, jestli autor právě označil 16 GB videopaměti za normál, u/Logicalist dodává, že je zábavné si to vůbec myslet, a u/sgt_Berbatov přiznává, že byl nadšený, když si konečně pořídil 12GB kartu s 32 GB RAM. Přidal se i povzdech uživatele s 16 GB RAM a 8GB kartou, který to celé jen čte, a pozvánka na r/LowEndLocalAI. Nejstřízlivější radu dal u/jonas-reddit: pořiď druhou stejnou grafiku, zdvojnásobíš videopaměť za zlomek ceny velkých karet a 32 GB už odemkne velmi slušné modely.

Pro běžnou sestavu tak podle komunity neplatí, že by byla odepsaná, jen je potřeba vybírat: menší husté modely do videopaměti na asistenta a chat, větší kvantizované Qweny na kódování s trpělivostí.
