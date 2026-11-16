# 1xhubiw
**Unsloth naučil lokální Qwen ovládat prohlížeč. Stačí jeden příkaz**

r/LocalLLaMA · u/HolidayBit143 · 28. října 2026, 18:19 · 465 bodů / 59 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xhubiw/)

Unsloth přidal do své výbavy pro lokální běh funkci browser-use, díky které dokáže model Qwen3.8 27B sám ovládat prohlížeč a plnit v něm úkoly. Ukázkové video zachycuje agenta při práci a autor příspěvku to slaví jako velký moment pro dostupnost lokální AI. Jsme prý jasně ve „věku agentů" a čím víc lidí se k lokálním modelům dostane, tím hůř se je prý podaří někomu sebrat.

K novince autor přihodil i odkaz na GitHub Unslothu a na oficiální návod, jak browser-use rozjet. Právě tahle jednoduchost je podle něj hlavní pointa: nejde ani tak o to, že by něco takového nikdy neexistovalo, ale o to, aby to zvládl i úplný začátečník bez složitého nastavování.

Právě kolem toho se rozjela největší přestřelka. Nejvýše hodnocený komentář u/Blaze6181 chladí nadšení: agenti tohle uměli už dávno přes browser-harness a podobné nástroje, je to prý příjemná funkce, ale žádný obří skok. Přidávají se u/MundanePercentage674, který to samé dělal před pár měsíci přes Open WebUI a Camofox, i u/wren6991 s připomínkou CUA integrace v DeepSeek Harness. U/DistributionBrief644 se ptá, v čem je to jiné než Playwright MCP, a u/mecshades popisuje vlastní harness s MCP, screenshoty, myší a klávesnicí, který umí ovládat celý počítač, byť pomalu.

Zastánci Unslothu ale vytahují jeden argument, který v diskusi rezonuje: spolehlivost na menších modelech. Uživatel u/yoracale vysvětluje, že ovládání prohlížeče pro lokální modely bylo vždy možné, jenže jiné postupy se na modelech jako Qwen3.8-27B nebo dokonce Gemma 4 E4B často zacyklily nebo předčasně skončily. Unsloth má být výjimečný právě samoopravujícími se voláními nástrojů a ochranou proti smyčkám. Do toho zapadá i rýpnutí u/politefella0, jestli video neběží tisíckrát zrychleně, protože Qwen3.8 27B je prý přemýšlivý model a takhle rychle se nerozhoduje.

Třetí linka vlákna řeší, co se stane, když agentovi dáte do ruky internet. U/applefreak111 se ptá, jestli zvládne captchu, u/TerminalNoop vtipkuje o nové vlně podvodníků na chess.com a další přidávají boty na Instagramu a X. U/HangryRatel přiznává, že se nebojí převzetí světa, ale toho, že model online udělá něco, co ho reálně dostane do potíží. U/Inevitable_Ad_711 to shrnuje drsně: svěřit Qwen3.8-27B root přístup k počítači je jako dát tříletému dítěti kódy k jaderným zbraním. Na druhé straně u/CryptographerLow6360 a u/Aggressive-Sign-8167 chválí, že pro každodenní použití je Unsloth prostě skvělý a pro nováčky nejsnazší cesta.
