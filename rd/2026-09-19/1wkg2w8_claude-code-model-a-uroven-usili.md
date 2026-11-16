# 1wkg2w8

**Anthropic vysvětluje, jak v Claude Code vybírat model a úroveň úsilí. Komunita varuje: změna uprostřed relace zruší cache**

| | |
|---|---|
| Subreddit | r/ClaudeAI |
| Autor | u/theleller |
| Publikováno (Europe/Prague) | 19. 9. 2026, 09:56 |
| Skóre / komentáře | 466 / 65 |
| Odkaz | https://www.reddit.com/r/ClaudeAI/comments/1wkg2w8/claude_code_effort_level_and_model_selection/ |
| Diskuse | https://www.reddit.com/r/ClaudeAI/comments/1wkg2w8/claude_code_effort_level_and_model_selection/ |

## Co se stalo

Post odkazuje na **oficiální článek Anthropicu** (autorka **Lydia Hallie**, 7. 7. 2026) o výběru modelu a úrovně úsilí v Claude Code. Článek rozlišuje dvě věci: **volba modelu** znamená, které zmrazené váhy a jaký rozsah schopností daný požadavek zpracuje, zatímco **úroveň úsilí (effort)** určuje, kolik práce Claude na požadavku celkově udělá — včetně počtu přečtených souborů, použitých nástrojů a kroků před tím, než se ozve zpět.

Článek doporučuje začínat s výchozím úsilím, používat menší modely na rutinní úlohy a větší na složité či nejednoznačné. Přináší i praktické vodítko: pokud Claude měl veškerý kontext, jasně se snažil, a přesto to pokazil, je čas na **schopnější model**; pokud to pokazil tím, že vynechal soubor, nespustil testy nebo vzdal refaktoring v půlce, je čas na **vyšší úroveň úsilí**. Modely charakterizuje jako specialistu (**Fable**), experta (**Opus**) a velmi dobrého generalistu (**Sonnet**).

V komentářích se ale objevilo praktické varování, které v článku chybí: **změna úrovně úsilí uprostřed relace zruší prompt cache**, což na dlouhých konverzacích zbytečně stojí peníze i kvótu.

## Klíčová fakta

- **Zdroj:** článek Anthropicu z 7. 7. 2026, autorka Lydia Hallie, odhadovaná doba čtení 10 minut.
- **Model vs. úsilí:** model = které zmrazené váhy požadavek zpracují; úsilí = kolik práce Claude vykoná (uvažování, čtené soubory, nástroje, ověřování, kroky před ohlášením).
- **Doporučení:** začít s výchozím úsilím; menší modely na rutinu, větší na komplexní a nejednoznačné úlohy.
- **Rozhodovací pravidlo:** chybějící znalost → větší model; vynechané soubory, testy nebo dvojitá kontrola → vyšší úsilí.
- **Charakteristiky modelů:** Fable specialista, Opus expert, Sonnet generalista.
- **Interní měření Anthropicu:** Opus 4.8 při výchozím úsilí podal lepší výsledky než Opus 4.7 při výchozím úsilí, a to zhruba za stejný počet tokenů.
- **Varování z komentářů:** změna úsilí uprostřed relace zruší prompt cache; u Fable 5.1 platí výjimka, u Opusu je oprava v beta verzi pro API.
- **Vysvětlení pojmů:** Ultracode je podle komentujícího jen xHigh s dodatečnou instrukcí používat workflows; Ultrathink je starší klíčové slovo v promptu.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Datum článku | 7. 7. 2026 |
| Odhadovaná doba čtení | 10 min |
| Ilustrace v článku: více tokenů při vysokém úsilí | ~7× |
| Náklady na cache při promptu do 1 hodiny (komentář) | 10 % |
| Náklady na cache po 1 hodině (komentář) | 200 % |
| Náklady na zápis do cache po vypršení TTL (komentář) | 2× cena vstupních tokenů |
| Platnost cache u subagentů (komentář) | 5 minut |
| Skóre / komentáře postu | 466 / 65 |
| Nejhlasitější komentář (u/CoamIthra) | 144 bodů |
| Komentářů v balíčku | 24 |

## Citace

> „Úsilí znamená víc než ‚čas na přemýšlení‘. Řídí, kolik práce Claude na vašem požadavku celkově udělá — včetně počtu přečtených souborů, použitých nástrojů a toho, kolik kroků udělá, než se vám ozve.“ (překlad) — Lydia Hallie, článek Anthropicu

> „Pokud Claude měl veškerý relevantní kontext, jasně se snažil, a přesto to pokazil, je to signál vybrat schopnější model. Pokud to pokazil tím, že vynechal soubor, nespustil testy nebo vzdal refaktor v půlce, zvolte vyšší úroveň úsilí.“ (překlad) — Lydia Hallie

> „Fable je specialista, který viděl problémy, jaké téměř nikdo jiný neviděl, Opus je expert a Sonnet je opravdu dobrý generalista.“ (překlad) — Lydia Hallie

> „Změna úrovně úsilí uprostřed relace zruší vaši prompt cache. Takže to na dlouhých konverzacích nedělejte, pokud nemáte rádi utrácení peněz nebo kvóty!“ (překlad) — u/CoamIthra, 144 bodů

> „Ultracode je falešná úroveň úsilí. Je to vlastně jen xHigh s dodatečnou instrukcí používat workflows.“ (překlad) — u/CoamIthra

> „Jsem rád, že průvodce klade kontrolu kontextu před přepínáním nastavení. Pokud se požadavek nikdy nedostal do konverzace, vyšší úsilí může znamenat jen důkladněji postavenou verzi špatné věci.“ (překlad) — u/robinekren

> „Poté, co Opus vytvoří plán, mu v téže relaci zadám: ‚Jednej jako orchestrátor subagentů…‘“ (překlad) — komentující popisující svůj postup

## Co říkají komentáře

Nejužitečnější přínos diskuse je **praktický a v článku chybí**: změna úrovně úsilí uprostřed relace zruší prompt cache, což je při delší práci drahé. Na to se nabaluje druhá linie o **nákladech cache** (10 % při dotazu do hodiny, 200 % po hodině, dvojnásobná cena za zápis po vypršení TTL) a třetí o **významu jednotlivých nastavení** — Ultracode je podle komentujícího jen xHigh s instrukcí k workflows, Ultrathink je starší klíčové slovo. Několik lidí sdílí vlastní postupy: nejdřív silný model na plán, pak levnější model nebo subagenti na provedení. Zaznívá i chvála, že průvodce staví **kontrolu kontextu před přepínáním nastavení** — protože vyšší úsilí u špatně zadaného požadavku znamená jen důkladnější provedení špatné věci.

## Rozpory a neověřené informace

- **Neshoda:** jeden komentující se domníval, že přepínáním úsilí šetří, nejhlasitější komentář tvrdí opak — zrušením cache se prodražuje.
- **Neshoda:** část vlákna řeší, zda špičky v nákladech způsobuje přepínání úsilí, nebo jen uživatelé na nevhodném tarifu.
- **Neověřená tvrzení (komentáře):** že změna úsilí uprostřed relace zruší cache, že Fable 5.1 drží cache při změně úsilí mezi zprávami a že u Opusu je oprava v beta verzi pro API.
- **Neověřená tvrzení:** že Ultracode je jen xHigh s instrukcí k workflows, že Ultrathink je převážně legacy klíčové slovo, a že cache subagentů vydrží 5 minut.
- **Neověřené údaje:** konkrétní procenta nákladů na cache (10 % / 200 % / 2×) uvádějí komentující, nikoli článek.

## Proč to je důležité

Jde o vzácný případ, kdy se **oficiální dokumentace a komunitní zkušenost doplňují**: Anthropic vysvětluje, jak o úloze uvažovat (model = schopnost, úsilí = důkladnost), a komunita dodává to, co v dokumentaci chybí — jaké to má provozní důsledky (cache, náklady, kvóty). Rozlišení „chybí znalost → větší model“ versus „vynechal kroky → vyšší úsilí“ je přitom praktické pravidlo, které ušetří jak peníze, tak zbytečné přepínání nastavení uprostřed práce.

## Zdroje

- https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- https://www.reddit.com/r/ClaudeAI/comments/1wkg2w8/claude_code_effort_level_and_model_selection/
- komentáře: `2026-09-19/_data/raw/comments.json` (klíč `1wkg2w8`), balíček `2026-09-19/_data/bundles/1wkg2w8.md`
