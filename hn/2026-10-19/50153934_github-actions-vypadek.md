# 50153934
**Výpadek GitHub Actions, Pages a webhooků**

Hacker News · gateauxd · 19. října 2026, 17:52 · 154 bodů / 126 komentářů · [diskuse](https://news.ycombinator.com/item?id=50153934)

Uživatel gateauxd na Hacker News upozornil na probíhající potíže GitHubu a odkázal na oficiální statusovou stránku incidentu. Diskuse se rychle stočila k praktickým dopadům, protože řadě lidí přestaly procházet automatizované sestavy a nasazování. Celé vlákno tak působí jako hlášení z místa činu v přímém přenosu.

Odkazovaná stránka popisuje zhoršenou dostupnost služeb Actions, Pages a webhooků. Nejprve hlásila vyšetřování potíží od 15:49 UTC, poté zpoždění zpracování úloh, stavby stránek a doručování webhooků a v 16:56 UTC označila incident za vyřešený s příslibem podrobnější analýzy příčin.

Nejživější linka patří zaseknutým úlohám. Uživatel defenestration píše, že jeho úloha visí ve stavu Queued už šestnáct minut, uživatel nix0n dodává, že na webu vidí jako čekající i úlohu, která na jeho vlastním runneru přitom dávno doběhla. Uživatel serial_dev se diví, že o výpadku věděl o dvacet minut dřív než oficiální status, na což uživatel jacquesm reaguje pravidlem, že co se opraví do dvaceti minut, to se nikdy nestalo. Uživatel somehowadev pak vtipkuje, že kolem 15:00 UTC už firma pomalu počítá s týdenním výpadkem, nejspíš když se do práce pustí američtí uživatelé.

Druhé velké téma je závislost na jediném dodavateli. Uživatel outworlder líčí, jak ve firmě převedli skoro celé CI/CD i GitOps na GitHub Actions, před koncentrací všeho do jednoho košíku varoval, a teď už je mu to jedno. Uživatel coldpie mu radí užít si vynucené volno a jít do parku nebo se učit něco nového, uživatel lenerdenator to nazývá náhodnými placenými přestávkami na kávu. Uživatel gateauxd se opakovaně ptá, co je vlastně alternativa, když je přilepení k platformě tak silné, uživatel icameron přiznává, že vytrhnout GitHub z pracovních postupů týmu by bylo extrémně rušivé, a i zhoršený GitHub podle něj překonává Bitbucket, který zažil dřív.

Třetí spor se vede o příčinu úpadku. Uživatel neya viní Microsoft a jeho infrastrukturu postavenou na Azure, zatímco uživatelé boxed, nrmitchi a shadowgovt míní, že větší roli hraje exploze provozu spojená s umělou inteligencí, záplava pull requestů a agentů, která vytváří úplně jiné vzorce přístupu než lidští uživatelé. Uživatel shadowgovt odhaduje, že GitHub by mohl provoz botů filtrovat, ale nechce působit jako platforma nepřátelská k umělé inteligenci. Paralelně se hledá úniková cesta: uživatel esafak fandí každému, kdo konečně dodá takzvaného zabijáka GitHubu, uživatelé ainar-g, x86a a beardsciences navrhují GitLab či vlastní Forgejo a uživatel OlivOnTech popisuje kombinaci GitLabu s vlastními runnery, kde migraci pracovních postupů dnes snadno zvládne slušný jazykový model.

Čtenář si z toho odnese prosté poučení: když stojí CI/CD, stojí všechno, a proto se vyplatí mít plán pro chvíle, kdy zelená fajfka prostě nepřijde.
