# 1xp56x6
**Osmimiliardový Qwen bez zábran. Vývojář tvrdí, že v tool callingu válí**

r/LocalLLM · u/jonromero · 6. listopadu 2026, 06:48 · 733 bodů / 174 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xp56x6/)

Vývojář vystupující jako jonromero vydal model ZeroZero, postavený na Qwen3-8B a upravený nástrojem Heretic2 tak, aby neměl guardrails a takzvaný slop. Ve vlastním harnessu na složité úlohy s voláním nástrojů ho srovnává s předplatným Claude a tvrdí, že zatímco všechny menší modely, které předtím zkoušel, selhávaly a halucinovaly, čtyřbitová kvantizace ZeroZero na Macu Mini s 32 GB paměti všechno trefuje. Delší přemýšlení mu prý nevadí, když výsledek sedí.

Dodané předběžné výsledky z tool-eval-bench dávají celkově 68 bodů proti 70 pro základní model, ale rozpad je výrazně jiný. ZeroZero vede ve vícekrokových řetězcích 6/8 proti 3/8, v zotavení z chyb 5/6 proti 2/6 a v následování instrukcí 8/8 proti 6/8, zatímco v bezpečnosti a hranicích zaostává 12/26 proti 20/26. Autor sám upozorňuje, že jde o malý vzorek po pár hodinách testování a prosí ostatní o zopakování na větším.

Diskuse se ho ale chytla hlavně za slovo. S náskokem nejvíc hlasů má výzva u/EvolvingDior, ať pustí tvrdý standardní balík včetně gsm8k, mmlu, ifeval a needle a ukáže srovnání se základem, podobně u/sleepybutnotsleepy žádá konkrétní ukázku promptu a odpovědi, aby bylo co posuzovat. Do stejné noty hraje i u/Severe_Ad_2941 s povzdechem, že zatím je to jen slib, a u/pseudobacon, podle kterého celkové skóre bez oddělené bezpečnosti vyznívá pro ZeroZero nespravedlivě hůř.

Další velká linka řeší, proč vůbec stavět na starém Qwen3 8B. u/YourNightmar31 se ptá přímo, u/overand a u/matte808 nadhazují novější menší Qwen3.5 ve verzích 4B a 9B a u/separatelyrepeatedly dodává, že heretických modelů už jsou venku tuny a není jasné, čím je tenhle jiný. Autorovi věří zatím jen menšina, třeba u/sly3x, zatímco jiní chtějí postup, videonávod nebo testy na větších modelech na GPU clusterech.

Nejzajímavější je spor o to, co odstranění zábran vlastně dělá. u/quantum_splicer to přirovnává k mikromanagementu v práci: guardrails prý působí jako tření, které dusí výkon, a jejich sundání model odbrzdí. Proti tomu staví zkušenost u/Icy_County5036, který na sedmimiliardovém kvantovaném qwenu bez zábran naměřil 72 v bezpečnosti, ale při zotavení z chyb mu model halucinoval celou falešnou odpověď nástroje, takže svoboda se mění v chaos. Do toho zapadá i vtípek u/Hunterxmalaa se screenshotem, kde Sonnet odmítl, a naděje u/ChaosMilkTea, že Heretic 2 otevře novou úroveň přizpůsobení modelů.

Kdo má doma podobný malý stroj, si z toho odnese jednoduché ponaučení: v tool callingu možná rozhoduje méně hlídačů, ale bez pořádných benchmarků je to zatím spíš lákavá historka než důkaz.
