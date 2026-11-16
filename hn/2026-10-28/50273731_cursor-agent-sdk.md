# 50273731
**Cursor Agent SDK: agenty jako kód, které hlídají pull requesty**

Hacker News · torutofu · 28. října 2026, 15:02 · 114 bodů / 118 komentářů · [diskuse](https://news.ycombinator.com/item?id=50273731)

Cursor vydal Agent SDK, framework, na kterém sám staví vlastní pomocníky Bugbot, Security Reviewer a Rollouts. Firmy si v něm mohou definovat agenty šité na míru vlastnímu fungování a spravovat je jako běžný softwarový projekt s verzováním a recenzemi.

Podle firemního blogu agenti reagují na události z GitHubu, GitLabu a Bitbucketu – zkontrolují pull request, pohlídají compliance proces nebo prošetří incident. Prompty se píšou v Markdownu a nástroje v TypeScriptu, hotového agenta vývojář pošle příkazem agent-sdk deploy na infrastrukturu Cursoru, nebo ho zabalí jako jediný Node proces do vlastního kontejneru. Vývoj mají zrychlit vestavěné evals a přehrávání událostí, jako příklady slouží interní kb-reviewer postavený asi za den, který každý pull request porovnává se znalostní bází ponaučení, i nasazení u PGA Tour.

Nejživěji se řeší, jestli je další SDK vůbec potřeba. Uživatel pscanf píše, že má pro agenty spoustu využití, ale nechce si aplikaci připoutat k jednomu dodavateli a volá po standardu jako openresponses.org, alternativy vidí v Agent API od OpenAI a Agent SDK od Anthropicu. Uživatel scosman si povzdechne nad názvy – Agent SDK už mají OpenAI i Anthropic, Vercel má AI SDK – a uživatel Raed667 dodává, že Google má ADK.

Druhé velké téma je únava z tempa. Uživatel username_my1 přirovnává ekosystém modelů k JavaScriptu: každý den nový nástroj a ty z minulého týdne jsou zastaralé, s malým rozšířením. Uživatel gonzalohm to nazývá konzumerismem přeneseným do softwaru, uživatel dangoodmanUT to omlouvá tím, že je vše nové a správná odpověď se teprve hledá, zatímco uživatel virgil_disgr4ce se brání a ptá se, proč by mělo vadit množství nápadů a frameworků. Uživatel maxdo v tom vidí přípravu na konec éry, kdy lidé posílají kód do gitu, a uživatel wslh dodává, že ty nekonečné nástroje budou stejně používat hlavně jiní agenti bez vědomí lidí.

Praktickou linku otevírá otázka uživatele simianwords, proč by rozhraní agentího SDK nemohl být prostě soubor PROMPT.md s během, který pustí model s nástroji, a k čemu jsou těžké abstrakce typu LangChain. Uživatel ashishmax31 vysvětluje, že vlastní běhové prostředí znamená vlastní smyčku a nástroje s přesně vymezenými právy, což pomáhá s autorizací. Uživatel zomtorg přidává, že firmy si zatím nemohou dovolit neomezený model s nástroji, různé části workflow potřebují různé modely, nástroje a mantinely a bezpečnostním a právním týmům se musí dát vysvětlit, jak se zachází s daty, co se loguje a co se stane při překvapení.

Od architektury se debata stáčí k penězům a otevřenosti. Uživatel h0rv se ptá, proč v říjnu 2026 nepoužít open-source harness. Uživatel chrisvalleybay odpovídá, že s předplatným Claude Code Max vyjde špičkový model Opus 5.5 / Fable 5.1 levněji než přes API, uživatel sodacanner mluví o vysoce dotovaném předplatném a složitější funkce označuje za divadlo produktivity. Nejpodrobněji to shrnuje uživatel csallen: lidé už mají Claude Code nastavené, nechtějí se učit nové rozhraní, předplatné jim bohatě stačí a přechod jinam je snadný, takže není kam spěchat.

Z oznámení o jednom SDK se tak stala debata o standardech, únavě z novinek a o tom, zda budoucnost patří kódu, promptu, nebo předplatnému.
