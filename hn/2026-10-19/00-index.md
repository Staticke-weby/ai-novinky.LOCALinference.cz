# Hacker News – denní AI/tech souhrn, 19. 10. 2026

## Metodika

Výběr vychází z **1 000 story** zachycených v okně 19. 10. 2026 (Europe/Prague) sběračem `scripts/hn-collect.py` z Hacker News. Z toho **58 story** mělo alespoň 10 komentářů a tvoří páteř přílohy; **45 kandidátů** prošlo podrobnějším čtením balíčků (článek, selftext, komentáře). Do souhrnu jsem zařadil **23 článků** k AI, modelům, agentům, robotice, vývojářským nástrojům a bezpečnosti. Čistě obecná politika, společenská témata, věda mimo AI, hry a klasické programování bez AI přesahu zůstaly stranou.

Některé externí články nebyly dostupné (WSJ, Reuters a Atlantic vracely 401/403, část byla za paywallem); u nich text vychází z dostupného titulku, kontextu a diskuse. Tam, kde šlo o stejnou událost nebo stejné URL, je uveden jeden článek: šest duplicitních submisí MiniMax M3.1 Flash bylo sloučeno do jednoho textu a druhá diskuse k zákazu DeepSeeku (id 50152946) je zmíněna uvnitř článku. Story bez samostatného článku najdete v příloze s odkazem na diskusi na HN.

## Články

| ID | Článek | Skóre | Komentáře |
|---|---|---:|---:|
| [50150434](50150434_timestral-mistral-casove-rady.md) | [Timestral: Mistral uvádí foundation modely pro časové řady](50150434_timestral-mistral-casove-rady.md) | 579 | 108 |
| [50154540](50154540_minimax-m3-1-flash.md) | [MiniMax M3.1 Flash: rychlejší a levnější agentní model](50154540_minimax-m3-1-flash.md) | 444 | 192 |
| [50151036](50151036_ask-hn-ai-kod-kteremu-nerozumite.md) | [Ask HN: Co dělat s AI kódem, kterému nerozumíte?](50151036_ask-hn-ai-kod-kteremu-nerozumite.md) | 390 | 537 |
| [50153630](50153630_cern-mistral-partnerstvi-ai-veda.md) | [CERN a Mistral se dohodly na partnerství v AI pro vědu](50153630_cern-mistral-partnerstvi-ai-veda.md) | 334 | 57 |
| [50150809](50150809_lets-encrypt-vzdalene-perspektivy.md) | [Let's Encrypt přidá dvě další vzdálené perspektivy pro ověření domén](50150809_lets-encrypt-vzdalene-perspektivy.md) | 258 | 80 |
| [50155245](50155245_mercury-3-difuzni-llm.md) | [Mercury 3: difuzní LLM, který běží několikrát rychleji](50155245_mercury-3-difuzni-llm.md) | 239 | 85 |
| [50148452](50148452_deepseek-v4-1-flash.md) | [DeepSeek V4.1 Flash: druhé místo v inteligenci za zlomek ceny](50148452_deepseek-v4-1-flash.md) | 187 | 90 |
| [50152321](50152321_plex-zranitelnosti-kryptominer.md) | [Plex zranitelnosti zneužívané k těžbě kryptoměn](50152321_plex-zranitelnosti-kryptominer.md) | 186 | 91 |
| [50154244](50154244_deepseek-zakaz-federalni-uradu.md) | [DeepSeek končí v amerických federálních úřadech, nařizuje DHS](50154244_deepseek-zakaz-federalni-uradu.md) | 173 | 151 |
| [50148855](50148855_tmux-claude-code-agentni-sezeni.md) | [Tmux a Claude Code: jak udržet AI agenty naživu mezi sezeními](50148855_tmux-claude-code-agentni-sezeni.md) | 155 | 117 |
| [50153934](50153934_github-actions-vypadek.md) | [Výpadek GitHub Actions, Pages a webhooků](50153934_github-actions-vypadek.md) | 154 | 126 |
| [50147492](50147492_superlite-agentni-vyvoj.md) | [Superlite: lehčí recept na agentní vývoj než Superpowers](50147492_superlite-agentni-vyvoj.md) | 147 | 67 |
| [50151928](50151928_qwen3-4b-deslop.md) | [Qwen3-4B bez AI frází: model, který se naučil psát lidsky](50151928_qwen3-4b-deslop.md) | 146 | 108 |
| [50151376](50151376_anthropic-ipo-trust.md) | [Anthropic míří na burzu. Kdo bude kontrolovat její trust?](50151376_anthropic-ipo-trust.md) | 140 | 119 |
| [50151390](50151390_harness-engineering-101.md) | [Harness Engineering 101: LLM je mozek, harness je tělo](50151390_harness-engineering-101.md) | 128 | 64 |
| [50153225](50153225_agentic-monitoring-claude.md) | [Agentic Monitoring: když Claude hlídá zdraví jednotlivých komponent](50153225_agentic-monitoring-claude.md) | 86 | 13 |
| [50151059](50151059_harness2-google-recursive.md) | [Harness²: Google Research učí agenty vylepšovat vlastní harness](50151059_harness2-google-recursive.md) | 74 | 18 |
| [50153403](50153403_atlantic-techno-oligarchove.md) | [Atlantik: technologičtí oligarchové a jejich plán pro lidstvo](50153403_atlantic-techno-oligarchove.md) | 71 | 43 |
| [50152541](50152541_kividb-redis-vektorova-databaze.md) | [KiviDB: rustový Redis s vektorovým hledáním a 21 miliony GET/s](50152541_kividb-redis-vektorova-databaze.md) | 66 | 40 |
| [50154029](50154029_laminar-chyby-v-agentnich-trasach.md) | [Laminar: RL model hledá chyby v trasách AI agentů](50154029_laminar-chyby-v-agentnich-trasach.md) | 52 | 23 |
| [50152466](50152466_maxwell-model-mezi-kodem-a-hardwarem.md) | [Maxwell: nový typ modelu mezi kódem a hardwarem](50152466_maxwell-model-mezi-kodem-a-hardwarem.md) | 49 | 24 |
| [50154060](50154060_humxn-roboti-instalaterske-prace.md) | [HUMXN nabízí zdarma instalatérské práce, aby sbíral data pro roboty](50154060_humxn-roboti-instalaterske-prace.md) | 33 | 74 |
| [50148396](50148396_strot-kompilace-zameru-lokalne.md) | [Strot: záměr jednou zkompilujte, rozhodnutí pak běží lokálně](50148396_strot-kompilace-zameru-lokalne.md) | 23 | 13 |

## Příloha: všechny AI/tech story s alespoň 10 komentáři

Celkem **41 story**. U story, která má samostatný článek, vede odkaz na něj; ostatní míří na diskusi na Hacker News.

| ID | Skóre | Komentáře | Čas (Praha) | Titulek |
|---|---:|---:|---|---|
| [50150750](https://news.ycombinator.com/item?id=50150750) | 638 | 362 | 19. 10. 2026, 12:45 | Vyhozený policista ze Savannah poskytl manželovi, agentovi ICE, přístup do systému Flock |
| [50149392](https://news.ycombinator.com/item?id=50149392) | 607 | 280 | 19. 10. 2026, 09:23 | Linux 7.3 |
| [50150434](50150434_timestral-mistral-casove-rady.md) | 579 | 108 | 19. 10. 2026, 11:59 | Timestral: Mistral uvádí foundation modely pro časové řady |
| [50152307](https://news.ycombinator.com/item?id=50152307) | 548 | 183 | 19. 10. 2026, 15:35 | Wine portován na OpenBSD |
| [50150089](https://news.ycombinator.com/item?id=50150089) | 501 | 107 | 19. 10. 2026, 11:05 | Postavil jsem dron s jediným motorem [video] |
| [50154540](50154540_minimax-m3-1-flash.md) | 444 | 192 | 19. 10. 2026, 18:39 | MiniMax M3.1 Flash: rychlejší a levnější agentní model |
| [50151036](50151036_ask-hn-ai-kod-kteremu-nerozumite.md) | 390 | 537 | 19. 10. 2026, 13:24 | Ask HN: Co dělat s AI kódem, kterému nerozumíte? |
| [50153630](50153630_cern-mistral-partnerstvi-ai-veda.md) | 334 | 57 | 19. 10. 2026, 17:28 | CERN a Mistral se dohodly na partnerství v AI pro vědu |
| [50154624](https://news.ycombinator.com/item?id=50154624) | 307 | 164 | 19. 10. 2026, 18:45 | Android aplikace běžící nativně na macOS |
| [50150809](50150809_lets-encrypt-vzdalene-perspektivy.md) | 258 | 80 | 19. 10. 2026, 12:53 | Let's Encrypt přidá dvě další vzdálené perspektivy pro ověření domén |
| [50153664](https://news.ycombinator.com/item?id=50153664) | 239 | 165 | 19. 10. 2026, 17:31 | Ukrajina tvrdí, že poprvé evakuovala zraněného vojáka dronem |
| [50155245](50155245_mercury-3-difuzni-llm.md) | 239 | 85 | 19. 10. 2026, 19:27 | Mercury 3: difuzní LLM, který běží několikrát rychleji |
| [50158100](https://news.ycombinator.com/item?id=50158100) | 222 | 113 | 19. 10. 2026, 23:08 | Instaluji Linux na svůj notebook RTX Spark, protože nemám účet Microsoft |
| [50148452](50148452_deepseek-v4-1-flash.md) | 187 | 90 | 19. 10. 2026, 06:41 | DeepSeek V4.1 Flash: druhé místo v inteligenci za zlomek ceny |
| [50152321](50152321_plex-zranitelnosti-kryptominer.md) | 186 | 91 | 19. 10. 2026, 15:36 | Plex zranitelnosti zneužívané k těžbě kryptoměn |
| [50154244](50154244_deepseek-zakaz-federalni-uradu.md) | 173 | 151 | 19. 10. 2026, 18:16 | DeepSeek končí v amerických federálních úřadech, nařizuje DHS |
| [50148855](50148855_tmux-claude-code-agentni-sezeni.md) | 155 | 117 | 19. 10. 2026, 07:55 | Tmux a Claude Code: jak udržet AI agenty naživu mezi sezeními |
| [50153934](50153934_github-actions-vypadek.md) | 154 | 126 | 19. 10. 2026, 17:52 | Výpadek GitHub Actions, Pages a webhooků |
| [50147492](50147492_superlite-agentni-vyvoj.md) | 147 | 67 | 19. 10. 2026, 04:01 | Superlite: lehčí recept na agentní vývoj než Superpowers |
| [50151928](50151928_qwen3-4b-deslop.md) | 146 | 108 | 19. 10. 2026, 15:00 | Qwen3-4B bez AI frází: model, který se naučil psát lidsky |
| [50158138](https://news.ycombinator.com/item?id=50158138) | 145 | 30 | 19. 10. 2026, 23:11 | Vydání OpenBSD 8.0 bude mít ovladače inteldrm/radeondrm/amdgpu z Linuxu 6.18 |
| [50151376](50151376_anthropic-ipo-trust.md) | 140 | 119 | 19. 10. 2026, 14:06 | Anthropic míří na burzu. Kdo bude kontrolovat její trust? |
| [50147455](https://news.ycombinator.com/item?id=50147455) | 134 | 76 | 19. 10. 2026, 03:55 | Záběry z vyhledávání Flock, které soudce označil za protiústavní |
| [50151390](50151390_harness-engineering-101.md) | 128 | 64 | 19. 10. 2026, 14:07 | Harness Engineering 101: LLM je mozek, harness je tělo |
| [50153431](https://news.ycombinator.com/item?id=50153431) | 123 | 28 | 19. 10. 2026, 17:10 | Observabilita řízená ontologií: Budování end-to-end znalostního grafu v Netflixu |
| [50148441](https://news.ycombinator.com/item?id=50148441) | 112 | 68 | 19. 10. 2026, 06:40 | Verisign – hromadná spotřebitelská žaloba kvůli registru domén .com |
| [50157865](https://news.ycombinator.com/item?id=50157865) | 89 | 11 | 19. 10. 2026, 22:50 | Bloom filtry s jedním hashem |
| [50153225](50153225_agentic-monitoring-claude.md) | 86 | 13 | 19. 10. 2026, 16:52 | Agentic Monitoring: když Claude hlídá zdraví jednotlivých komponent |
| [50151059](50151059_harness2-google-recursive.md) | 74 | 18 | 19. 10. 2026, 13:28 | Harness²: Google Research učí agenty vylepšovat vlastní harness |
| [50153403](50153403_atlantic-techno-oligarchove.md) | 71 | 43 | 19. 10. 2026, 17:07 | Atlantik: technologičtí oligarchové a jejich plán pro lidstvo |
| [50148601](https://news.ycombinator.com/item?id=50148601) | 68 | 62 | 19. 10. 2026, 07:11 | Flatpak – bezpečnostní noční můra (2023) |
| [50152541](50152541_kividb-redis-vektorova-databaze.md) | 66 | 40 | 19. 10. 2026, 15:53 | KiviDB: rustový Redis s vektorovým hledáním a 21 miliony GET/s |
| [50154029](50154029_laminar-chyby-v-agentnich-trasach.md) | 52 | 23 | 19. 10. 2026, 18:00 | Laminar: RL model hledá chyby v trasách AI agentů |
| [50152466](50152466_maxwell-model-mezi-kodem-a-hardwarem.md) | 49 | 24 | 19. 10. 2026, 15:47 | Maxwell: nový typ modelu mezi kódem a hardwarem |
| [50154060](50154060_humxn-roboti-instalaterske-prace.md) | 33 | 74 | 19. 10. 2026, 18:03 | HUMXN nabízí zdarma instalatérské práce, aby sbíral data pro roboty |
| [50158408](https://news.ycombinator.com/item?id=50158408) | 32 | 34 | 19. 10. 2026, 23:38 | Drupal je dnes o světelné roky dál, než napovídá jeho pověst |
| [50153531](https://news.ycombinator.com/item?id=50153531) | 27 | 12 | 19. 10. 2026, 17:19 | Kód je teď hlína |
| [50148396](50148396_strot-kompilace-zameru-lokalne.md) | 23 | 13 | 19. 10. 2026, 06:32 | Strot: záměr jednou zkompilujte, rozhodnutí pak běží lokálně |
| [50156132](https://news.ycombinator.com/item?id=50156132) | 21 | 13 | 19. 10. 2026, 20:36 | Podezření kolem křivek NIST rozptýleno |
| [50148882](https://news.ycombinator.com/item?id=50148882) | 16 | 10 | 19. 10. 2026, 07:58 | Agent-Skills.market |
| [50148298](https://news.ycombinator.com/item?id=50148298) | 10 | 12 | 19. 10. 2026, 06:13 | Muž zatčen poté, co s [Claude] probíral plány na masovou střelbu ve školce |

---

Data: Hacker News, sběr `scripts/hn-collect.py`. Časy jsou uvedené v Europe/Prague. Komentáře na HN nemají veřejné skóre, proto se v textech neobjevuje.
