# 50006114
**AI agent na Nokii 110: reverse engineering a 48 MB RAM**

Hacker News · anupray · 8. října 2026, 16:18 · 27 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50006114)

Autor si pořídil Nokii 110 4G, aby omezil čas na displeji, a pak dostal nápad dostat do ní AI agenta. Nejprve zkoušel nainstalovat Android, jenže ten se do telefonu s pouhými 48 MB RAM nevešel, a tak se na několik dní pustil do reverse engineeringu firmwaru.

Z vestavěné kalkulačky udělal chatovací aplikaci ovládanou numerickou klávesnicí. Ta posílá napsanou zprávu na DeepSeek chat API a přes tool calls ovládá nativní funkce telefonu: zjistí stav baterie, rozsvítí svítilnu, zahájí hovor a nastaví budík. Jde o prototyp, který se do telefonu nahrává z počítače do RAM, po restartu je nutné ho nahrát znovu, ale odpojený od kabelu už běží přes mobilní data. S vývojem pomáhal OpenAI Codex.

V diskusi se nejdéle řešilo, jestli se na tuhle řadu Nokií dají přidávat vlastní aplikace. Uživatel butz si posteskl, že před dvaceti lety na mobilech běžely Java aplikace J2ME, zatímco dnes nic. Autor odpověděl, že firmware téhle Nokie je psaný v C, na rozdíl od starších verzí v Javě, a vlastní aplikace přidat jdou, jen jeho současný postup po restartu zmizí.

Na otázku uživatele sparkling, kde je v tom vlastně to „AI", autor vysvětlil, že odpovídání na otázky a volání nástrojů z běžného textu dělá agent: jednoduchá smyčka volá DeepSeek API, to vrátí JSON a podle něj telefon vyvolá nativní funkci Nokie, nebo odpoví na dotaz. Pro uživatele samaltmanfried pak popsal postup podrobněji: vytáhl firmware, nastudoval, jak vestavěné aplikace používají displej, klávesnici, síť a další funkce, a napsal malou aplikaci v C, která po stisku klávesy ukázala v kalkulačce nápis „PDP". Nejtěžší prý bylo zachytit odpověď API, která se nevešla do malé paměti a schovávala se někde v bufferu.

Zbytek vlákna jsou hlavně pochvaly. Uživatelé moshetanzer a sshussain270 autorovi gratulují k zábavnému kousku a RexHuang glosuje, že nejtěžší je pro něj takovou Nokii 110 vůbec sehnat. Z kdysi hloupého telefonu na omezení scrollování je tak malá ukázka toho, že i tlačítkový veterán umí volat moderní API a sahat si na vlastní hardware.
