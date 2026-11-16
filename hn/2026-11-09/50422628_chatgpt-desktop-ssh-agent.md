# 50422628
**ChatGPT Desktop posílá váš SSH agent do vzdálených strojů**

Hacker News · DenGorbachev · 9. listopadu 2026, 09:17 · 207 bodů / 73 komentářů · [diskuse](https://news.ycombinator.com/item?id=50422628)

Desktopová aplikace ChatGPT přeposílá lokálního SSH agenta do vzdálených strojů, na kterých běží její agent. Ten se tak dokáže přihlásit pomocí SSH údajů uživatele, například pushovat do jeho soukromých repozitářů na GitHubu. Autor jako důkaz odkazuje na diskusi u pull requestu OpenAI Codex číslo 28131, který nakonec nebyl sloučen.

Největší ohlas získala praktická obrana: nenechat klíč volně v agentovi. littlecranky67 doporučuje na macOS klíče v secure enklávě, které pro každou novou session vyžadují otisk prstu, takže agent nic nespustí bez vědomí uživatele. bradfa k tomu přidává YubiKey s povinným dotykem, kdy klíčenka před autorizací zabliká, itissid pro stejný účel používá aplikaci Secretive a Lukas_Skywalker má klíče v desktopové aplikaci Bitwarden nastavené tak, aby pokaždé žádala o potvrzení. causal ale upozorňuje, že ani správce hesel samotné přeposlání agenta nezastaví, a navrhuje oddělený klíč pro každý účel a kontrolu, který klíč se skutečně použil.

Druhá linka diskuse řeší, jestli má bezpečnost bolet. recsv-heredoc tvrdí, že v bezpečnosti je tření dobrá věc a k důležitým krokům patří obřad, zatímco arghwhat odpovídá, že automatické přeposílání agenta na cizí stroje není vyvážené řešení a chybí možnost filtrovat a schvalovat jednotlivé požadavky na podpis. api to popisuje jako věčné napětí mezi pohodlím a bezpečností, kvůli kterému lidé vypínají ochranu i protahují se za cizími zády do zabezpečených budov, a scotty79 připomíná, že právě bezbolestnost pomohla rozšířit npm navzdory jeho šílenému bezpečnostnímu modelu.

Proti kultu tření se ozývají hlasy varující před únavou z potvrzování. hgoel připomíná, že příliš mnoho výzev vede k tomu, že uživatelé začnou vše slepě odklikávat, což je už teď problém u volání nástrojů velkých modelů. siva7 dodává, že frustrace z překážek lidi spíš odnaučí bezpečnost brát vážně. jasonjayr proto navrhuje jemnější cestu v podobě podúčtů s omezenými právy, třeba po vzoru bankovního rozhraní, které podřízenému uživateli dovolí jednou měsíčně zaplatit vodu do dvou set dolarů a člověka otravuje jen při překročení.

Nejtvrdší komentáře pak zpochybňují samotný způsob, jakým se agenti pouštějí do světa. m000 píše, že lokální zábrany stojí na nespolehlivých zákazových seznamech a pořádné pískoviště zůstává domácím úkolem pro uživatele, simoncion radí nikdy tyto nástroje nespouštět pod běžným každodenním účtem. causal míní, že lidé postupují pozpátku, když nejdřív dají plný přístup desktopové verzi a teprve pak objeví cloudové sandboxy od Claude a ChatGPT, které na psaní kódu bohatě stačí. Skepsi shrnuje yfontana otázkou, co má vlastně dokazovat odkaz na uzavřený a nesloučený pull request, na což paxy suše odpovídá, že stačí přečíst titulek a rozhořčit se.

Poučení z vlákna je jednoduché: kdo nechce, aby mu agent sahal na klíče, ať mu nedává volnou ruku a klíče zamkne za dotyk, otisk nebo potvrzovací dialog.
