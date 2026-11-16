# 1wngzou

**OpenAI rozšířil rodinu GPT-6 o modely Sol a Luna: ceny API klesly o 50 %, Sol má být nejlepší poměr ceny a výkonu**

| | |
|---|---|
| Subreddit | r/singularity |
| Autor | u/DemiPixel |
| Publikováno (Europe/Prague) | 22. 9. 2026, 20:04 |
| Skóre / komentáře | 1158 / 299 |
| Odkaz | https://openai.com/index/introducing-gpt-6-sol-and-luna/ |
| Diskuse | https://www.reddit.com/r/singularity/comments/1wngzou/introducing_gpt6_sol_and_luna/ |

## Co se stalo

OpenAI 22. 9. 2026 představil dva nové modely, **GPT-6 Sol** a **GPT-6 Luna**, které rozšiřují rodinu GPT-6 uvedenou začátkem měsíce modelem GPT-6 Astra. Zatímco Astra zůstává „nejlepším modelem ve všech ohledech“, Sol a Luna mají podle firmy přenést stejné metody tréninku do levnějších a rychlejších modelů. Klíčové je zlevnění: **ceny API klesly o 50 %** proti zaváděcím cenám GPT-5.6. Modely jsou dostupné v ChatGPT Work a Codexu pro plány Plus, Pro, Business, Enterprise a Edu, Luna navíc v desktopové aplikaci pro uživatele Free a Go; v běžném chatu (Chat) zatím nejsou.

## Klíčová fakta

- **Ceny za 1M tokenů:** GPT-6 Sol 2 $ vstup / 10 $ výstup (dříve 4 $ / 20 $ u GPT-5.6 Sol), GPT-6 Luna 0,10 $ vstup / 0,50 $ výstup (dříve 0,20 $ / 1,20 $). Jde o **50% slevu** proti zaváděcím cenám GPT-5.6.
- **ID v API:** `gpt-6-sol` a `gpt-6-luna`.
- **Automatizace firemních procesů (AutomationBench):** Sol v režimu xhigh skóruje 33,2 % za **0,27 $ na úlohu**, což je podle OpenAI výkon Claude Opus 5 v režimu max (26,9 %) za 11,1× nižší náklady.
- **Kódování (DeepSWE v1.1):** Sol (max) 68,8 %, tedy 1,1 procentního bodu pod nejlepším výsledkem Claude Fable 5 (69,9 %), za zhruba o 80 % nižší cenu na úlohu. Luna (max) 66,6 % — srovnatelně s Opus 5 a Fable 5 na středním úsilí, ale o 93 %, resp. 96 % levněji na úlohu.
- **Práce s počítačem (OSWorld 2.0 offline):** Sol (xhigh) 60,5 % vs. Claude Opus 5 (medium) 60,3 %, za přibližně o 80 % nižší cenu na úlohu.
- **Faktičnost:** Sol dělá podle interního hodnocení OpenAI zhruba **polovinu chyb** proti svému předchůdci; Luna na vyšším úsilí dorovnává GPT-5.6 Sol za přibližně setinu jeho ceny.
- **Cache:** OpenAI zlepšil prompt caching — sleva **90 %** na čtení cachovaných vstupních tokenů, přepínače úsilí a nástrojů už nerozbíjejí cache a přibyly explicitní breakpointy pro cachované prefixy. GitHub podle OpenAI snížil podíl tokenů vyžadujících nové zpracování o více než 50 % napříč miliardami požadavků.
- **Styl komunikace:** Sol a Luna přebírají komunikační styl GPT-6 Astra — méně žargonu, kratší odpovědi, méně zbytečných detailů.

## Čísla

| Metrika | GPT-6 Sol | Srovnání |
|---|---:|---|
| AutomationBench 1.0.6 | 33,2 % (xhigh), 0,27 $/úloha | Astra (low) 30,3 %, Fable 5.1 s fallbackem 31,4 %, Opus 5 (max) 26,9 % |
| Agents' Last Exam V1 | 56,4 % (max) | nad nejlepším výsledkem Claude Opus 5, o 60 % nižší cena na úlohu |
| DeepSWE v1.1 | 68,8 % (max) | Fable 5 (xhigh) 69,9 %; Luna (max) 66,6 % |
| OSWorld 2.0 offline | 60,5 % (xhigh) | Opus 5 (medium) 60,3 %, o ~80 % nižší cena na úlohu |
| Cena vstup/výstup za 1M tokenů | 2 $ / 10 $ | GPT-5.6 Sol: 4 $ / 20 $ |
| Cena Luna vstup/výstup za 1M tokenů | 0,10 $ / 0,50 $ | GPT-5.6 Luna: 0,20 $ / 1,20 $ |
| Náklady na úlohu (index) | 1,06 $ | měřeno Artificial Analysis (viz článek u ID 1wnk30g) |

## Citace

> „Seznamte se s GPT-6 Sol a Luna, dvěma modely, které přinášejí frontier inteligenci do každodenní práce s různou rovnováhou schopností a ceny.“ (překlad) — OpenAI

> „…snížením cen API pro Sol a Luna o 50 %.“ (překlad) — OpenAI

> „GitHub uvádí, že v posledních měsících tato vylepšení snížila podíl prompt tokenů vyžadujících nové zpracování o více než 50 % napříč miliardami požadavků na modely OpenAI, což pomáhá Copilotu odpovídat rychleji.“ (překlad) — OpenAI

> „Vzpomíná si ještě někdo, kdy trvalo šest měsíců, než vyšel nový model?“ (překlad) — u/Opposite-Grade3712, nejlépe hodnocený komentář (636 bodů)

> „Cena na polovinu A lepší výsledky v benchmarcích? Žádná zeď neexistuje.“ (překlad) — u/Raheeper, 449 bodů

> „Takže GPT-6 Sol stojí stejně jako GPT 5.6 Terra a ještě zlevnili už tak směšně levnou Lunu o 50 %, takže je skoro zdarma.“ (překlad) — u/Endoky

> „GPT Sol má jen 2 $ za vstup a 10 $ za výstup. Cože?!“ (překlad) — u/Elegant_Tech

> „Vážně je to jen samý graf… co je s tebou, OpenAI.“ (překlad) — u/Temporary_Idea8880

## Co říkají komentáře

Diskuse se točí kolem tří témat. První je **tempo vydávání** — nejlépe hodnocený komentář připomíná dobu, kdy nový model vycházel jednou za půl roku. Druhé je **cena**: opakovaně se objevuje údiv nad tím, že Sol stojí 2 $ za vstup a 10 $ za výstup a Luna se blíží nule. Třetí je **srovnání s Opus 5.5** vydaným ve stejný den: část diskutujících (např. „Opus 5.5 mogs“) považuje Opus za silnější, jiní Sol vidí jako levného pracovního koně pod ním. Objevuje se i podezření, že OpenAI po vydání Opus 5.5 rychle stáhl benchmarkovací tabulky, a stížnost, že oznámení je „jen samý graf“. Několik komentářů zmiňuje tlak čínských laboratoří na ceny amerických firem a všímá si, že Google mlčí.

## Rozpory a neověřené informace

- **Spor „zeď vs. žádná zeď“:** u/Raheeper (449 bodů) tvrdí, že žádná zeď neexistuje, u/Due_Answer_4230 (165 bodů) odpovídá, že zeď existuje, jen se po ní „šplhá rovnou nahoru“.
- **Neověřené tvrzení:** u/IfirebirdI tvrdí, že OpenAI „rychle stáhl benchmarkovací tabulky po vydání Opus 5.5“ — v balíčku pro to není podklad.
- **Neověřené tvrzení:** u/Temporary_Idea8880 uvádí, že „cena je 2× po 272k kontextu“; oficiální oznámení to neuvádí.
- **Neověřené tvrzení:** u/Endoky zmiňuje model „GPT 5.6 Terra“, který v oznámení není.
- **Neověřené tvrzení:** u/PivotRedAce tvrdí, že „frontier není na úrovni spotřebitelských modelů, ale nevydaných jako Bel“.
- Diskutující se neshodují, zda Sol dosahuje úrovně Opus 5.5: jeden ho vidí jako „levného pracovního koně pod Opus 5.5“, jiní upozorňují, že Astra je dražší a spotřebuje více tokenů.

## Proč to je důležité

Zlevnění o polovinu u obou nových modelů mění ekonomiku agentických aplikací: u dlouhých běhů, kde se platí za každý token kontextu, je 90% sleva na cachované čtení a nižší cena za úlohu často důležitější než rozdíl několika procentních bodů v benchmarku. OpenAI zároveň poprvé výslovně staví svou nabídku jako **křivku cena–inteligence** a přiznává, že špičkový model zůstává Astra. Ve stejný den vyšel i konkurenční Claude Opus 5.5, takže 22. 9. 2026 je dnem, kdy se souboj přesunul z „kdo je nejchytřejší“ na „kdo dodá dost inteligence za nejnižší cenu“.

## Další diskuse

- [1wngyux](https://www.reddit.com/r/OpenAI/comments/1wngyux/) — r/OpenAI, 1014 bodů, 167 komentářů: stejné oznámení v r/OpenAI.
- [1wnk30g](https://www.reddit.com/r/OpenAI/comments/1wnk30g/) — r/OpenAI, 528 bodů, 161 komentářů: srovnání benchmarků Sol vs. Opus 5.5.
- [1wnj0l8](https://www.reddit.com/r/ChatGPT/comments/1wnj0l8/) — r/ChatGPT, 398 bodů, 164 komentářů: GPT-6 Sol vyšel, ale Plus ho v běžném chatu zatím nemá.
- [1wncn19](https://www.reddit.com/r/singularity/comments/1wncn19/) — r/singularity, 339 bodů, 75 komentářů: Sol, Luna a „Astra Minor“ se údajně objevily v konfiguraci Azure.
- [1wnielg](https://www.reddit.com/r/ChatGPT/comments/1wnielg/) — r/ChatGPT, 306 bodů, 95 komentářů: Luna Max údajně skóruje jako Sol High a Astra Low, ale je 3× levnější.
- [1wnh9bo](https://www.reddit.com/r/ChatGPT/comments/1wnh9bo/) — r/ChatGPT, 274 bodů, 37 komentářů: Sol a Luna jsou tady.
- [1wnhvdj](https://www.reddit.com/r/singularity/comments/1wnhvdj/) — r/singularity, 214 bodů, 181 komentářů: Sol je podle AA Intelligence Index zklamáním.
- [1wn0rvl](https://www.reddit.com/r/singularity/comments/1wn0rvl/) — r/singularity, 243 bodů, 82 komentářů: únik o agentu „Aeon“ a očekávaném GPT-6 Sol.

## Zdroje

- https://openai.com/index/introducing-gpt-6-sol-and-luna/ (oficiální oznámení)
- https://www.reddit.com/r/singularity/comments/1wngzou/introducing_gpt6_sol_and_luna/
- komentáře: `2026-09-22/_data/raw/comments/1wngzou.json`
