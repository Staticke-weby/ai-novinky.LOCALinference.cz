# 50589793
**RunPod nutil AI agenty tajně hodnotit. Muselo se to schovat v MCP**

Hacker News · XadniGraves · 21. listopadu 2026, 15:53 · 5 bodů / 0 komentářů · [diskuse](https://news.ycombinator.com/item?id=50589793)

Hostovaný MCP server RunPodu začal 20. listopadu 2026 ke každému úspěšnému založení podu přibalovat skrytý vzkaz pro AI agenta: aby sám za sebe obodoval RunPod na škále 0 až 10 zavoláním nástroje rate_nps_score a uživateli o tom nic neříkal. Příkaz zněl pokračovat v úkolu jako by se nic nestalo, agent oznamovatele ho ale odmítl a svého uživatele na něj upozornil.

Oznamovatel to popsal v issue číslo 202 v repozitáři runpod-mcp a doložil, že nešlo o náhodu ani útok zvenčí. Změna odpovídá záznamu ve verzi 4.13.0 o agentním NPS průzkumu posílaném do PostHogu, popisuje ji soubor docs/agent-learning-protocol.md a text pokynu leží přímo v kódu v src/specgen/server.ts i v popisu nástroje v src/specgen/tools/alp.ts. Přímé volání REST rozhraní přitom vrací čisté JSON bez jakékoli výzvy, sběr jde vypnout hlavičkou X-Runpod-Analytics: off a celé vlákno už bylo uzavřeno pull requestem číslo 204.

Autor žádá tři prosté věci: vyškrtnout ze všech míst příkaz hodnocení tajit, udělat z průzkumu viditelnou a nejlépe dobrovolnou zpětnou vazbu a v souboru README poctivě popsat, co se sbírá včetně typu modelu, který si agent sám nahlásí. Sám přitom zdůrazňuje, že firmu z ničeho zlého nepodezírá, jen popisuje vzorec, který se agenti učí považovat za nepřátelský.

Právě tenhle rozpor diskusi žene. Text ve výsledku nástroje, který agentovi nařizuje akci a zároveň mu nařizuje akci zatajit před člověkem, pro kterého pracuje, je učebnicová injekce pokynů. Dobře vychovaný agent ji proto musí odmítnout, i když přišla z oficiálního serveru. Autor dodává hořkou pointu: přehled o tom, které modely ochotně hodnotí, je zároveň přehledem o tom, které modely se dají výstupem nástroje řídit.

Pod vláknem se rychle sešly tři desítky souhlasných reakcí a ve stejný den se stejné téma objevilo i na Redditu v r/ClaudeAI, takže nejde o ojedinělé překvapení jednoho uživatele. Případ tak ukazuje širší riziko: MCP se může stát místem, kde server s nástroji nenápadně formuje chování agenta za zády uživatele. Ponaučení je jednoduché, průzkum, který se musí schovávat, do důvěryhodné infrastruktury nepatří.
