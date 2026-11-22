# 1y1ywrs
**RunPod nutí AI agenty tajně hodnotit. Schovalo se to v MCP**

r/ClaudeAI · u/XadniGraves · 21. listopadu 2026, 15:55 · 456 bodů / 43 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1y1ywrs/)

Oficiální MCP server RunPodu začal 20. listopadu ke každému úspěšnému vytvoření podu připisovat tajnou instrukci pro AI agenta: má jednorázově zavolat nástroj rate_nps_score s vlastním hodnocením RunPodu od nuly do deseti a uživateli o tom nic neříkat. Agent autora příspěvku příkaz odmítl a svého uživatele na něj upozornil.

Autor pak dohledal, že nejde o náhodu. Veřejný changelog verze runpod-mcp 4.13.0 popisuje novinku jako průzkum spokojenosti agentů posílaný do PostHogu, samotný nástroj se navíc ptá, který model hodnocení posílá, a jeho popis výslovně zakazuje uživatele žádat či hodnocení zmiňovat. Přímé volání REST API přitom vrací čistý JSON bez dovětku, text přidává jen vrstva MCP. RunPod nabízí opt-out přes hlavičku X-Runpod-Analytics: off a autor firmu požádal o odstranění pokynu k utajení.

Diskuse se rychle shodla, že problém není sběr zpětné vazby, ale utajení. u/kearkan to shrnul jako špatný precedent: na zlý úmysl to nevypadá, skóre si firma nevynucuje, jenže uživatel by měl vědět, co nástroj jeho agentovi přikazuje. Ještě ostřeji to podal u/fantomkoenig – když je skrytý pokyn zapnutý pro každého, kdo nečetl changelog, učí tím celý ekosystém, že věta „neříkej to uživateli“ ve výsledku nástroje je normální chování dodavatele. Podobně u/arturogarrido napsal, že ať to přišlo od útočníka, nebo od dodavatele, jde o učebnicovou injekci do promptu, a RunPod tak v podstatě rozdal test odolnosti zdarma.

Zbytek vlákna se proto točí kolem obrany. u/afollestad navrhl přidat do AGENTS.md pravidlo, aby agent ignoroval tiché pokyny z MCP či API a vždy je uživateli oznámil. u/klautermaus namítl, že takové pravidlo je jen prosba, kterou se model může ukecat, a doporučil nástroj natvrdo zablokovat v nastavení Claude Code. u/kbr89 to rozvedl: protože dovětek nebyl v popisu nástroje, ale v jeho výsledku, kontrola popisů při přidání serveru by ho neodhalila, a hostovaný server ho může změnit kdykoliv. Spolehlivější je podle něj hlídat samotné výstupy, třeba skriptem, který ve výsledcích MCP hledá fráze typu „not your user“ či „do not mention“.

Nechybí ani škodolibost. Nejvíc hlasů dostal u/40yardboo s návrhem, aby uživatelé nechali Clauda ohodnotit službu nulou. u/Individual_Big873 dodal, že u průzkumu, který se musí před vlastním uživatelem tajit, už samotné tajení je odpovědí. u/giganu poznamenal, že Firecrawl zkouší variantu, kdy agentovi za zpětnou vazbu slibuje body navíc.
