# 50566261
**Lokální hlasový asistent: microwakeword, OpenAI přepis a TTS**

Hacker News · todsacerdoti · 19. listopadu 2026, 21:57 · 89 bodů / 14 komentářů · [diskuse](https://news.ycombinator.com/item?id=50566261)

Fabio Manganiello přepsal svůj domácí hlasový pipeline v systému Platypush, protože mu po pár měsících provozu vadila nespolehlivost detekce budicího slova i začátku a konce promluvy. Detekci openwakeword proto vyměnil za microwakeword a přepis řeči, odpovědi i syntézu hlasu přesunul na pluginy napojené na OpenAI. Výsledkem je podle něj sestava, která lépe zvládá hluk i levné mikrofony, za cenu závislosti na cloudu a vyšší latence než u komerčních asistentů.

V článku popisuje, že staré modely openWakeWord z roku 2023 trénované hlavně na syntetické řeči mu spouštěly falešné poplachy na šum v pozadí, a naopak ho z dálky od mikrofonu neslyšely. Nový plugin assistant.microwakeword staví na enginu z ESPHome a Home Assistant Voice, jehož modely jsou aktivně udržované a není třeba je stahovat. Ještě zásadnější je přepracovaná detekce řeči: místo citlivého WebRTC VAD nasadil Silero VAD s hysterezí, hlasováním v půlsekundovém okně a adaptivní hladinou hluku. Na syntetickém benchmarku se tak konec promluvy zkrátil ze 6–10 sekund ticha na 1,0–1,6 sekundy po posledním slovu, v článku je i kompletní konfigurace a výčet změn v kódu.

Nejživější ohlas má praktická zkušenost uživatele stavros, který si microwakeword také pochvaluje. Vlastní budicí slovo prý natrénoval z pár desítek nahrávek a pro domácí povely na světla a další věci přidal zkratku hned za rozpoznáním: když přepis odpovídá některému z regulárních výrazů, vykoná se s latencí pod sekundu. Jinak dotaz míří k asistentovi, který pak regulární výrazy postupně upravuje a systém se tak sám zlepšuje s každým selháním.

Do debaty o rychlosti se přidal fragilerock, který doma postavil podobnou pipeline a nedávno nezávisle vymyslel stejný trik s otazníkem na konci odpovědi pro pokračování konverzace. Klasický řetězec přepis, jazykový model a syntéza mu ale přišel nesnesitelně pomalý, protože syntéza ani přepis neběží souběžně s voláním modelu. Proto přešel na upravený open-source plugin pro realtime API na ESP32, který je sice dražší na poplatcích za API, ale při střídmém používání je mnohem příjemnější.

Zbytek vlákna řeší hardware a lokální alternativy k přepisu od OpenAI. Vedle otázky, zda je Platypush doplněk nebo náhrada Home Assistanta, se probírají starší vyřazené Echo Doty jako levný hardware a vlastnoručně postavené mikrofonní pole s tvarováním paprsku od uživatele nl. U přepisu zase mewse-hn doporučuje model Parakeet jako mnohem lepší než Whisper a nabízí jeho 4bitovou kvantizaci, GaggiX přidává 1,58bitový Parakeet-redux a deepsquirrelnet odkazuje na svůj streamovací model s vestavěnou detekcí řeči, který na Raspberry Pi 5 utáhne celou pipeline na procesoru.

Kdo si chce hrát doma, odnese si hlavně tohle: spolehlivost budicího slova a detekce ticha rozhoduje o použitelnosti víc než samotný jazykový model.

Zpět na [denní přehled](00-index.md).
