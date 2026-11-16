# 49979793
**OpenChart: open-source alternativa TradingView s vlastním AI agentem**

Hacker News · Warren93 · 6. října 2026, 17:16 · 40 bodů / 16 komentářů · [diskuse](https://news.ycombinator.com/item?id=49979793)

Na Hacker News se představil Weilun, spoluzakladatel projektu OpenChart. Vadilo mu, že AI modely jako Claude nebo Codex přistupují k trhům přes příkazovou řádku, zatímco lidé přes grafy, a tak postavil nástroj, kde agent pracuje přímo s grafem. Umí okomentovat obchodní situaci, napsat indikátor, prozkoumat pohyb trhu nebo založit alert, přičemž graf, konverzace i výzkum žijí v jednom pracovním prostoru.

Odkazovaný web projekt líčí jako grafy bez softwarových kvót – indikátory, Volume Profile i mřížka až 4×4 bez omezování plánem. Stačí nakreslit na graf čáru či zónu a po proražení ceny alert spustí agenta, který pohyb prozkoumá a uloží rešerši s odkazy na zdroje. Vlastní logiku a indikátory se píšou v jazyce Tea inspirovaném Pine Scriptem od TradingView, desktop je zdarma k vlastnímu účtu Claude, Codex či Gemini a zdarma jsou i základní data, placená jsou jen rychlejší cloudová.

Diskuse se nesla ve znatelně nadšeném duchu, několik lidí projekt rovnou přirovnalo k lokálnímu TradingView. Uživatel aurielws chválí volbu držet všechno lokálně a kombinaci soukromí, otevřeného kódu a agentního přístupu prý u trhů ještě neviděl. Warren93 mu přitakal, že soukromí je pro tradery zásadní a má i praktický bonus – agent díky tomu zná investiční kontext, který má člověk obvykle uložený v notebooku.

Jiné vlákno řeší napojení na existující agentní nástroje. Uživatel ranli slaví konečně lokální sjednocující vrstvu pro Codex a Claude Code a Warren93 vysvětluje, že systém staví na komunikačním protokolu nezávislém na poskytovateli, takže by teoreticky měl zvládnout jakýkoli harness. Uživatel indigo-lu píše, že open-source náhradu TradingView schopnou běžet lokálně dlouho hledal, uživatel homerg to shrnuje prostě jako lokální TradingView.

Jedinou praktickou výtku přidal uživatel aidiveyt, kterému alertem spuštěné běhy po hodině nečinnosti přepsaly asi 130 tisíc cache tokenů v Claude Code. Nejkonkrétnější přání vyslovil uživatel crosscorsair, který chválí nezvykle hladkou integraci předplatného Claude a jako příležitostný trader by rád viděl podporu iOS a Androidu pro každodenní použití. Warren93 odpovídá, že předplatné AI na mobilu neběží snadno, ale na rozšíření na další platformy už pracují – zatím je totiž aplikace jen pro macOS na Apple Silicon.

OpenChart tak zatím vypadá jako slib pro tradery, kteří chtějí grafy bez limitů, data u sebe doma a agenta po ruce.
