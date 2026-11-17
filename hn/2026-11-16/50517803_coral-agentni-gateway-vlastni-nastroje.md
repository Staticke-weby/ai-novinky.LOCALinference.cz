# 50517803
**Coral: agenti si píšou vlastní nástroje a příště si pamatují cestu**

Hacker News · jcs · 16. listopadu 2026, 15:14 · 52 bodů / 24 komentářů · [diskuse](https://news.ycombinator.com/item?id=50517803)

Coral je open-source a self-hostovaná brána mezi agenty a systémy, na kterých pracují. Agent v ní nevolá nástroje po jednom, ale napíše krátký program v TypeScriptu, a když postup zafunguje, uloží si ho jako vlastní nástroj k opakovanému použití. Na úlohách v GitHubu, Linearu a Slacku s modelem Opus 5.5 byly takové vlastní nástroje o 29 procent rychlejší a o 31 procent levnější než práce od nuly.

Přiložené readme to ukazuje na jednoduchém příkladu: agent poprvé najde otevřené pull requesty bez recenzenta, po schválení je pošle do Slacku a kód si uloží, druhý den už jen zavolá vlastní nástroj v jednom kroku. Každý program běží v čerstvé izolaci V8 bez přístupu k síti a pověření, Coral každé volání zkontroluje proti politice pracovního prostoru a teprve pak doplní klíče a požadavek přepošle. Je napsaný v Rustu, běží jako desktopová aplikace na notebooku nebo jako sdílený server ve vlastním cloudu a jádro je pod licencí Apache 2.0.

Nejvěcnější linka diskuse patří nasazení. ocamoglu chválí jemnější kontrolu a paměť šitou na míru úloze a ptá se na zkušenosti z reálného provozu. James, jeden ze zakladatelů, radí začít lokálně v desktopové aplikaci a teprve pak investovat do sdíleného serveru s vlastním poskytovatelem identity. Vlastní nástroje podle něj nemá smysl navrhovat předem: lepší je nechat agenty, ať si samy objeví, co potřebují, a člověk jen reviduje přidávání a úpravy. Třetí rozhodnutí je identita u poskytovatele, většina týmů prý volí přihlášení každého za sebe přes jednorázový OAuth tok místo sdíleného tokenu.

Kolem toho se rozběhly dvě odbočky. fg137 si stěžuje, že název mate, protože Google měl svou platformu Coral s TPU v USB klíčence a vyhledávání „Coral AI“ najde spoustu jiných firem. James přiznává, že metafora korálu se týmu líbí, ale přídavné slovo by možná nebylo od věci. anonyonoor by zase chtěl knihovnu mini-aplikací, které agenti píší ve všestranném HTML, ale zůstávají zavřené v konkrétní platformě a chatu. James odpovídá, že to týmy řeší dvojím způsobem, buď si postaví generický host pro artefakty a data a politiku nechají na Coralu, nebo použijí omezenější sadu HTML šablon pro dashboardy a widgety.

Neživěji bylo při debatě o důvěře. jrflo se ptá na politiku zakládání nových účtů kvůli nafouknutí zájmu při launchi a wavemode vlákno rovnou nahlásil jako boty. James se omlouvá a tvrdí, že nejde o podvod, jen pozvali preview uživatele a hrst z nich si kvůli oznámení založila nové účty. Věcněji se nese dotaz eb379, jak fungují schválení napříč agenty. Coral na to má stránku s čekajícími i minulými souhlasy, agent v odpovědi vrátí odkaz jako další akci a kde to jde, pošle hezčí dialog jako MCP aplikaci, protože nativní MCP vyžádání prý nástroje implementují divoce, Claude Desktop je od srpna automaticky zamítá a Codex je naopak někdy automaticky schvaluje.

Z diskuse tak zůstává jednoduché ponaučení: nechte agenta, ať si vyšlape cestu jednou pořádně, a příště už ho po ní jen pošlete.
