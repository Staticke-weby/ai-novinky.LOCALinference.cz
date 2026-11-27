# 1y6fs4d
**Gemini aplikace umí vzdálený počítač, uživatelé přes něj ovládají infrastrukturu**

r/GeminiAI · u/Southern-Ad-3006 · 27. listopadu 2026, 01:26 · 196 bodů / 21 komentářů · [diskuse](https://www.reddit.com/r/GeminiAI/comments/1y6fs4d/)

Zapnutí síťového přepínače v nastavení Tasks promění aplikaci Gemini v mnohem schopnějšího pomocníka, protože jí zpřístupní virtuální počítač od Googlu podobně jako to mají Muse, Dots a GrokBot. Model si do účtu dokáže sám instalovat skilly, repozitáře, kód i externí API a autor příspěvku díky tomu se svým stackem přímo kóduje a povídá si. Sám přiznává, že zatím netuší, kolik CPU, RAM a úložiště Google přiděluje, a rozdíly proti konkurenčnímu řešení chce otestovat v příštích týdnech.

Sám autor v diskusi rozvedl, k čemu stroj používá: přes Tailscale propojil Gemini s ostatními počítači, spouští skript do svého Tailscale funnelu a dostane se tak ke kódovacím agentům. Přes aplikaci tak orchestruje boty a agentní postroje na VPS, generuje média, videa a kód a snadno je tlačí do vlastních aplikací. Oceňuje i to, že limity používání v Antigravity a v aplikaci Gemini se počítají zvlášť, a jako největší přínos vidí napojení na sdílený mozek plný kontextu, skillů a workflow, bez kterého by to byla jen další jazyková modelka. Plány a specifikace s plným kontextem si nechává připravit v aplikaci a předává je stavěcím agentům na serveru.

Nejvýše hodnocenou odpověď přinesl u/soniglf, který se podíval přímo do terminálu počítače a vypsal parametry. Běží tam Debian 12 s kernelem 6.12.105, dvoujádrový Intel Xeon Platinum 8481C pod KVM, 7,8 GB RAM bez swapu a kombinace 49GB systémového disku a 19GB pracovního úložiště, grafika chybí. Sám se ptá, jestli je funkce nová, protože ji dosud neviděl, a těší se, jak užitečná bude.

Kolem zapnutí se točí i praktické dotazy. u/bisonrbig nechápe, v čem je rozdíl, když přepínač zůstane vypnutý, protože jeho první úkol se tabulkami jízdních řádů si prý v prohlížeči poradil i bez něj. u/TheRealKyloy řeší, jak funkci vůbec zapnout, když mu v nastavení svítí šedivě, zatímco u/Kincayd jen děkuje za tip a hlásí, že ji hned aktivoval.

Poslední věcná linka patří trvalosti prostředí. u/ioanap554 se ptá, jestli sdílený pracovní prostor udrží nainstalované balíčky i mezi jednotlivými úkoly. Odpověď v balíčku nezazněla, stejně jako vysvětlení šedivého přepínače, takže kdo si chce virtuální počítač od Googlu osahat, bude si muset počkat na další zkušenosti z vlákna.
