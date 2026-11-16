# 1xossr5
**Z.ai ukázal tréninkový pipeline GLM-5.5. Menší verze mají 32, 122 a 256 miliard parametrů**

r/LocalLLaMA · u/wapswaps · 5. listopadu 2026, 21:06 · 992 bodů / 173 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xossr5/)

Hlavní vědecký pracovník Z.ai Jie Tang na přednášce na univerzitě Tsinghua představil zákulisí chystaného modelu GLM-5.5. Ten má přijít hned ve třech velikostech se 32, 122 a 256 miliardami parametrů, takže nejmenší varianta by měla být použitelná i na běžnějším lokálním hardwaru.

Místo veřejných datasetů staví předtrénink podle shrnutí na síti X na šesti interních zdrojích. Jde o bilion webových stránek stahovaných tempem asi deset miliard denně, dvě miliardy vědeckých PDF zpracovaných vlastním GLM-OCR, 50 milionů knih s úpravou rozvržení a filtrem poškozeného textu, 500 milionů repozitářů proměněných ve spustitelné úlohy s testy, deset miliard videí pro dlouhé sekvence a 300 milionů hodin audia přepsaných do bilionů tokenů.

Komunita se do čísel zamilovala na první pohled. u/Equivalent_Bit_461 vzkazuje, že se mu líbí všechna tři, u/No_Algae1753 slaví, že 122 a 32 miliard dorazí najednou, a u/kanduking si u 122 miliard uleví, že už bylo na čase. Nadšení shrnuje u/Any_Librarian205, podle něhož novinka okamžitě zastiňuje jeho očekávání od Qwen 4, zatímco u/Cool-Chemical-5629 to čte jako návrat ke kořenům z dob, kdy byl top modelem právě GLM 4 s 32 miliardami. Někdo v tom vidí i návrat oblíbeného GLM Air a důstojného soupeře pro Qwen 4 s 27 miliardami, jiní si dělají legraci z pojmenování a menší modely přes současné zvyklosti křtí jako Nano, Micro a Tiny.

Největší spor se vede o architekturu. u/Vielklug spekuluje, že vůbec nejde o samostatné modely, ale o podmodely, které se sloučí do zhruba bilionového GLM-5.5. Část vlákna doufá, že menší verze budou směsí expertů, u/bartsimpsonwin prosí, ať je 32miliardová verze MoE, a u/ThankGodImBipolar předpokládá, že směsí expertů budou všechny. Kdyby se takto malý model výkonem přiblížil GLM 5.3F, byl by to podle něj divoký release. Proti tomu stojí u/MerePotato s přáním dalšího modelu kolem třiceti miliard: ať je raději hustý.

Nechybí ani nedůvěra. u/jacek2023 píše, že fámu slyšel už před pár dny a celé mu to přijde nepravdivé, u/paf1138 to označuje za podezřelé, i když doufá v opak. Podobně se ozývá dotaz, co se stalo s verzí 5.4, kdy novinka vyjde a zda vedle ní dorazí i ještě větší model.

Pokud se čísla potvrdí, mohla by být menší GLM poprvé po dlouhé době skutečně lokální alternativou k největším otevřeným modelům.
