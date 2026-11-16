# 1xdwquj
**Anthropic: většina agentů má mít jeden cyklus, ne hromadu subagentů**

r/ClaudeAI · u/emarkosov · 24. října 2026, 04:15 · 771 bodů / 75 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xdwquj/)

Uživatel u/emarkosov shrnul příručku, kterou Anthropic vydal 22. října pod názvem „When to fold subagents into your main agent loop“. Je mířená na firemní stavitele agentů, ale dopadá i na každého, kdo si v Claude Code nahromadil zástup subagentů. Autor přiznává, že jich měl sám šest a nakonec mu zbyli dva, protože většina z nich byly jen dovednosti s vlastním oknem kontextu.

Příručka doporučuje výchozí stav jeden model, jeden kontext a jeden otevřený nástrojový cyklus, kdy postupy patří do skills a tvrdé limity do nástrojů. Subagenty má podle ní smysl držet jen při měřitelném zahlcení kontextu, pro paralelní práci s jednorázovým kontextem nebo při konfliktu instrukcí a přemíře nástrojů. Jeden zákazník s jediným cyklem běžel zhruba dvakrát rychleji než s multiagentním harnessem, volba nástrojů se kazí po 30–50 definicích a Anthropic u Claude Code zkrátil systémový prompt pro novější modely o více než 80 procent.

Největší ohlas měla věta, že polovina subagentů byly jen oslavené jednořádkovky s čerstvým kontextem, jak píše u/Jealous-Sink-9400. Praktickou shodu shrnul u/bostonaholic: subagent si vydělá na čtenářsky těžké úkoly, kdy se má vrátit jen shrnutí z prohledávání kódu, logů nebo čerstvá oční kontrola diffu, zatímco cokoliv sdílející stav s hlavní smyčkou patří do skillu. Podobně u/Fair-Perspective7352 potvrzuje, že po překročení čtyřiceti definic nástrojů začal jeho automat špatně volit nástroje a pomohlo až seskupení podle záměru s odloženým načítáním.

Proti tomu stojí tábor recenzí cizím modelem. Nejvýše hodnocený hlas u/BringMeTheBoreWorms tvrdí, že kontrola a spolupráce modelů od různých poskytovatelů dává masivně lepší a lépe prozkoumané výsledky, i když je pomalejší. U/OriginalUsername0112 popisuje testy, kde mu nepřátelský recenzní subagent Opus a čtecí subagent Haiku téměř vždy chytily aspoň jeden zásadní problém, a u/ChemicalExcellent463 trvá na tom, že plánování a exekuce mají zůstat oddělené a recenze musí přijít z jiného modelu v jiném harnessu, protože harness kontrolující sám sebe nic skutečného nenajde.

Třetí linka řeší cenu a nedůvěru. U/Amarsir připomíná, že radit „nechte všechno na našem velkém modelu“ je pro Anthropic i sebezajímavé, a dál deleguje, protože chce vidět plán před změnami a Haiku je tak levné, že ani zbytečný subagent nebolí. U/ECrispy se ptá, jak může jediný rostoucí kontext porazit čerstvý kontext pro grepování, editace a testy, kde je důležitý jen výsledek. A u/K-etoranger popisuje, že narazil na „Frankenprompt“ v malém: po každé chybě připsal pravidlo pro ten jeden incident, až soubor přerostl práci, a zastavila to až dvě pravidla o pravidlech samotných.

Z diskuse tak vychází úklid, ne konec subagentů: zrušit ty, co jsou jen převlečené dovednosti, a nechat si je na jednorázové čtení, paralelní výpady a oponenturu odjinud.
