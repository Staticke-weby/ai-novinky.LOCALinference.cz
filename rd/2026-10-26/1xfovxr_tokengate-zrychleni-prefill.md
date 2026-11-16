# 1xfovxr
**TokenGate zrychluje long-context prefill až 11,3krát**

r/LocalLLaMA · u/MundanePercentage674 · 26. října 2026, 07:06 · 406 bodů / 47 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xfovxr/)

Uživatel u/MundanePercentage674 přinesl do r/LocalLLaMA zprávu o TokenGate, modulu pro zrychlení prefillu u dlouhého kontextu od výzkumníků ze Stanfordu a UC Berkeley. K odkazu připojil jen lakonické „doufám, že je to pravda“. Princip je prostý: model si vstup jen zběžně prolétne a plně zpracuje pouze tokeny, které vyhodnotí jako důležité.

Odkazovaný článek popisuje, jak to funguje uvnitř. K předtrénovanému modelu se přidá malý MLP gate s LoRA (r=16), zkoušelo se to na Qwen3-1.7B a Qwen3.5-2B až do 128 tisíc tokenů. Průchod se dělí na tři fáze, po prořezání se nahoře zpracuje jen vybrané top-K a pro zahozené tokeny se vůbec netvoří KV záznamy, přičemž otázka se neprořezává nikdy. Měření na jedné A100 slibují 1,4krát až 11,3krát rychlejší čas do prvního tokenu a 1,5krát až 3,4krát nižší špičkovou paměť prefillu.

Největší ohlas ale nesklidila samotná čísla, nýbrž odkazy a web, na kterém zpráva vyšla. u/Megatron_McLargeHuge vytáhl přímé odkazy na papír a repozitář, aby se čtenáři vyhnuli reklamám a popupům, a u/bahwi si neodpustil poznámku na adresu příšerného webu. u/FastDecode1 přiznal, že podle názvu TokenGate nejdřív čekal dramatický post o ukradených tokenech, a u/KevWeng lituje, že se zkratka z práce nejmenuje GTA.

Vážná linka debaty se točí kolem jedné námitky: prořezávání rozbíjí prefix caching. u/Kodix to popisuje jako spekulativní prefill v jiném kabátě – zbavujete se nedůležitých tokenů, které se ale o pár tahů později mohou stát důležitými. Podobně u/niksonrt tvrdí, že právě prefix caching dělá dlouhý kontext na lokálním stroji vůbec použitelným, a bez něj slibované zrychlení ztrácí smysl. u/CiobanuXashi to shrnuje úsečně: radši pomalejší prefill, který nikdy nezahodí zakopaný řádek, než rychlý, který tiše prořeže odpověď na navazující otázku.

Přesto v diskusi zůstává zvědavost. u/FullOf_Bad_Ideas by to chtěl vidět integrované ve vLLM nebo SGLangu, klidně i pro rozhodovací modely. u/fallingdowndizzyvr nevěří samotné spolupráci: že by se Cal spojil se svým úhlavním rivalem Stanfordem? A u/jinnyjuice už sní o kontextech v řádu milionů až desítek milionů tokenů pro velké projekty.

Z vlákna tak nakonec plyne typicky lokální ponaučení: papírové zrychlení je lákavé, ale dokud metoda neprokáže, že přežije cachování a navazující dotazy, zůstane u nadšeného „snad je to pravda“.
