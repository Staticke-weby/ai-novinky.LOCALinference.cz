# 1wz00vv
**Microsoft potvrdil looped transformery v GPT-6, pak informaci stáhl**

r/LocalLLaMA · u/ResearchCrafty1804 · 6. října 2026, 13:21 · 1131 bodů / 231 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wz00vv/)

Microsoft na veřejně dostupné stránce potvrdil, že OpenAI v řadě GPT-6 používá looped transformery, čímž podle autora zpětně dosvědčil dřívější reportáž The Information. Z téže zmínky vyplynulo, že GPT-6.1 Sol používá dva inferenční průchody místo tří a stojí na stejných základních vahách jako GPT-6 Sol, tedy na společném předtrénovaném základu s odlišným post-trainingem a o jeden cyklus méně. Microsoft stránku později upravil a pasáž o architektuře z ní zmizela.

Jádrem diskuse se stala prosba u/Melodic_Reality_646 o lidské vysvětlení, co looped transformer vlastně je. Nejvýše hodnocenou odpověď napsal u/felheartx: výstup bloku transformeru se prostě pošle zpět do téhož bloku, takže se jeden blok aplikuje víckrát. Výhodou je víc výpočetní práce bez nároků na paměťovou propustnost, která je dnes hlavní brzdou, nevýhodou méně parametrů pro uložení znalostí při stejném objemu výpočtů. Autor příspěvku to zjednodušil ještě dál, že uvažování probíhá uvnitř modelu bez vypisování myslících tokenů, takže je úspornější, ale ztrácíme možnost sledovat, jak model k odpovědi došel.

Na to navázala vtipná linka, která celé vlákno odlehčila. u/samsteak přepsal princip do jeskynní mluvy: normální myslící kámen je vysoký a těžký a slovo jím šplhá vzhůru, zatímco smyčkový kámen má jen jednu vrstvu, kterou slovo obíhá dokola, s každým kolečkem chytřejší, až se z příliš mnoha koleček zatočí hlava a myšlenka se zkazí. Vedle toho slavil u/Skylleur „nanbeige“, tedy malý otevřený model, který opakování vrstev používá už dávno, a u/TioMir dodal, že to dokazuje, že Nanbeige měl celou dobu pravdu.

Pro místní komunitu je právě tahle souvislost nejzajímavější. u/BalorNG napsal, že pro „chudé na grafiky“ to znamená víc efektivní hloubky při menší paměti a zajímavé kousky hlavně kolem směsí expertů, i když trénink i servírování bude oříšek. Podobně u/zoraruha připomněl dávné pokusy o „proto-looped“ modely typu Goliath 120B, které překvapivě dobře fungovaly, ale nikam se nedostaly, a u/FrostTactics vytáhl půl roku starý pokus s opakovanými vrstvami u Qwen, jako důkaz, že základní nápad funguje i mimo OpenAI.

Zároveň se ozvaly pochyby a varování. u/Cold_Tree190 se ptal, co je větší zpráva, jestli samotné smyčky, nebo to, že vůbec známe architekturu, a u/--Spaci-- oponoval, že architekturu vlastně pořád neznáme a smyčky jsou výpočetně neefektivní. Podle něj byla 6.1 Sol uspěchaná a OpenAI nemělo čas na nový předtrénink, tak jen předělalo post-training se dvěma smyčkami. K tomu sedí i postřeh u/nullmove, že je 6.1 na API pomalejší, přestože má dělat méně průchodů. A u/vtkayaker s u/Dangerous-Report8517 varovali, že smyčkové uvažování se hůře kontroluje a usnadňuje modelu tajné plánování, takže ostatní laboratoře tuhle cestu záměrně nechtějí následovat.

Pro čtenáře z toho plyne jednoduché poučení: větší rozum v menší paměti za cenu horší průhlednosti, přesně to se teď v otevřených modelech bude zkoušet napodobit.
