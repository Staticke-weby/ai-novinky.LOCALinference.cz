# 1wyruu5
**35B MoE pro dvacetičlenný tým na jedné desktop stanici**

r/LocalLLM · u/Commercial_Designer5 · 6. října 2026, 04:59 · 342 bodů / 115 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1wyruu5/)

Autor s týmem týden provozuje vlastní model na jediném stroji s NVIDIA DGX Spark se 128 GB sdílené paměti. Vsadil na Ornith-1.5-35B-A3B, směs expertů s 35 miliardami parametrů celkem a jen 3 miliardami aktivními na token, takže stroj počítá zlomek toho, co by chtěl hustý model. Používá oficiální 4bitový checkpoint NVFP4 kolem 22 GiB bez vlastního kvantování a obsluhu přes vLLM 0.24 s predikcí více tokenů bez separátního návrhového modelu.

Sólový uživatel se v chatovém rozhraní dočká 79 tok/s, dvacítka souběžně pak asi 25 tok/s na hlavu a 490 tok/s celkem, přičemž každý požadavek může sáhnout po plných 262K kontextu a funguje vidění i volání nástrojů. Kóduje se v OpenCode v terminálu, chatuje a přehazují se PDF v Open WebUI a parsování dokumentů i embeddingy běží lokálně, takže citlivý kód a dokumenty nemíří na žádné cizí API. Kdo by to chtěl zopakovat, najde na GitHubu skripty, bránu, dashboardy i benchmarky, jen si má pohlídat strop paměti na 0,70, nepřehánět počet souběžných slotů a počítat s tím, že si Open WebUI pamatuje výchozí model ve vlastní databázi.

Za kus, který z pokusu dělá infrastrukturu, autor označuje malou pythoní bránu před vLLM: každému člověku a zařízení dává vlastní API klíč, živě počítá vstupní a výstupní tokeny, tlačí je do Grafany a hlásí pokusy mluvit s vLLM napřímo. Právě tohle komunita chválí nejvíc, u/eepromnk jen suše přitakává, že o tomhle nikdo nemluví. Uživatel u/SoonFarawaySeduction píše, že bez přehledu o tom, kdo žere propustnost, do tří dnů nikdo neví, co se děje, a dashboard ušetří spoustu pasivně agresivních zpráv na Slacku, se zlobivým výchozím modelem přitom sám zápasil ještě déle než hodinu.

Nejhlasitější spor je o rozum modelu. Uživatel u/numsu tvrdí, že na reálných programátorských úlohách v kvantu Q6 tristně selhal a Qwen 3.8 27B ho převálcuje, přidávají se u/_OVERHATE_ s propadákem v testu DeepSwe i v běžném kódování a u/ithkuil s pochybou, zda tak malá aktivní část nedává programátorům nevýhodu proti lepším volbám. Opačnou zkušenost hlásí u/cd9v, který z Qwenu přešel a už by se nevrátil, smířlivě pak u/eulataguhw: Ornith sice na Qwen nemá, ale ujde jako junior, který hodně ví a občas sekne velkou chybu, proto prý nechává složitou orchestraci na Qwenu a rutinou krmí Ornith.

Druhá linka řeší, zda se na sdíleném tempu dá pracovat. Uživatel u/BlindPilot9 to označuje za směšně pomalé a posílá tým pro dvojici RTX Pro 6000, u/Designer-Present1182 žertuje o zneužívání zaměstnanců a ptá se, zda se vyplatí platit dvacet lidí za čekání, zatímco u/Matricola70 to naopak vítá jako důkaz, že není potřeba sestava za desítky tisíc. Do toho u/dupontping a u/Unusual_Principle536 rýpou, že text zní jako linkedinový výstup samotného Ornithu.

Z vlákna tak zůstává prostý recept: malý aktivní model uživí tým na jednom stroji, ale rozhoduje měření na uživatele a střízlivá volba úloh.
