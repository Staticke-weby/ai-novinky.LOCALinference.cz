# 50384233
**MS Paint má zranitelnost RCE. Útočník prý nepotřebuje interakci**

Hacker News · kuberwastaken · 5. listopadu 2026, 21:43 · 428 bodů / 159 komentářů · [diskuse](https://news.ycombinator.com/item?id=50384233)

V databázi CVE se objevil záznam CVE-2026-83844, který popisuje vzdálené spuštění kódu v aplikaci Microsoft Paint. Záznam ji vede jako síťově zneužitelnou bez autentizace a bez interakce uživatele, což u malování působí překvapivě. Microsoft zároveň hodnotí zneužitelnost jako Exploitation Less Likely, veřejné prozrazení ani aktivní zneužívání nehlásí a oprava je ve verzi 11.2609.401.0.

Právě to slovo vzdálené diskusi zarazilo nejvíc. Uživatel tosti se ptá, jak může být spuštění kódu v Paintu vzdálené, a VorpalWay připomíná, že Paint z jeho zkušenosti žádné síťové funkce neměl. Pokud je to pořád pravda, nadhazuje možnost, že jde o chybné zařazení a zranitelnost ve skutečnosti vzdálená není. Podobně se ptají ajasmin a gregschlom, který cituje popis o speciálně vytvořeném paketu poslaném po síti, a dodává, že otázka jak tím nezmizela.

Vysvětlení se tak hledá oklikou přes soubory a handlery. Uživatel dboreham píše, že to bude nejspíš klasická chyba grafických nástrojů, kdy útočník přiměje oběť otevřít podstrčený soubor. TZubiri spekuluje o škodlivém BMP, které po otevření naváže odchozí spojení a dál přijímá příkazy, hoppp to vidí stejně jako návnadu k phishingu přes kliknutí na soubor. Jinou cestu navrhuje 6thbit, podle kterého by mohlo jít o file handler nebo vlastní odkaz, který Paint otevře a při čtení z vadné cesty přeteče. Sohcahtoa82 to glosuje jízlivě, že definice vzdáleného se rozšířila i na poslání škodlivého souboru, který musí oběť otevřít.

Mezitím se vlákno rozjelo do vtipů a praktických starostí. Uživatel stygiansonic píše, že až přijde RCE v hledání min, bude po všem, caust1c si už vyhlíží RCE v kalkulačce a itopaloglu83 dodává, že po nedávné chybě v poznámkovém bloku má Microsoft formu. Uživatel arm32 nabádá všechny k záplatování Paintu a Oarch se těší na budoucí vysvětlení od Raymonda Chena. Vedle toho řeší everylostbit s Kapurou a tjohnsem číslování verzí kolem 11.2605 a diví se, co se na Paintu verze 11 vlastně mohlo tolik měnit.

Zůstává tak paradox: na papíře kritická vzdálená chyba bez kliknutí, v praxi podle Microsoftu nepravděpodobná k zneužití a podle komunity nejspíš jen další chyba v parsování souboru, kterou bude muset někdo nejdřív otevřít.
