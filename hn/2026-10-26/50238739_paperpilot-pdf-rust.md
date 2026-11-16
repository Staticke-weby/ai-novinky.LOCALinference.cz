# 50238739
**PaperPilot: PDF engine v Rustu pro agenta i člověka, zcela bez cloudu**

Hacker News · vardhan1237 · 26. října 2026, 04:29 · 230 bodů / 84 komentářů · [diskuse](https://news.ycombinator.com/item?id=50238739)

Autor vardhan1237 představil PaperPilot jako odpověď na vlastní frustraci z běžných PDF nástrojů. Vadí mu, že člověk kvůli sloučení, kompresi nebo podpisu daňového formuláře či smlouvy musí nahrávat důvěrné dokumenty na cizí server. PaperPilot je proto napsaný v čistém Rustu a slibuje přísně lokální provoz, kdy soubory nikdy neopustí stroj uživatele.

Odkazovaný repozitář popisuje jeden engine s pěti rozhraními: příkazová řádka pro dávkové zpracování, desktopová aplikace v Tauri a Svelte, webová verze běžící ve WebAssembly na adrese usepaperpilot.com, lokální REST služba na localhost:7823 a MCP server pro kódovací agenty typu Codex, Claude Code nebo Cursor. Dnes umí verze 0.6 slučovat, dělit, otáčet a přeskupovat stránky, komprimovat, tahat text i OCR, přidávat vodoznak nebo skenovat citlivé údaje, na cestě jsou převody do Markdownu a Wordu, šifrování, formuláře a opravy.

Nejostřejší výměna se strhla kolem originality. Shorel se ptal, jestli projekt přináší něco, co by už dávno nešlo snadno udělat nástroji z příkazové řádky, a později rýpl, že autorovi jde jen o to, že se bojí terminálu. Podobně darksim905 kroutil hlavou, proč by někdo vedle odzkoušeného Foxitu potřeboval další základní funkce, a Gigachad pochyboval, zda vůbec existuje reálný případ pro ruční tvorbu PDF mimo textový editor.

Ještě tvrdší bylo obvinění od colesantiago, zda nejde o kód přepsaný z MuPDF, který by pak musel být pod AGPLv3 místo Apache. Autor vardhan1237 to důrazně odmítl s tím, že v PaperPilotu není žádný kód, FFI ani transpilace z MuPDF a jádro stojí na knihovnách lopdf, pdf-writer, hayro a image s licencemi Apache 2.0 a MIT. Do stejného tématu se opřel fschuett, autor konkurenční knihovny printpdf, podle kterého lidé zbytečně znovu programují PDF engine včetně tohoto projektu postaveného na pdf_oxide a pak znovu narážejí na dávno vyřešené záludnosti typografie, sloupců, poznámek pod čarou nebo hebrejštiny zprava doleva.

Z toho se vyvinula obecnější debata o době, kdy je předělávání téměř zadarmo. SecondCrack nadhodil, zda za ignorováním let práce stojí lidé, nebo AI, kterou nepřečetla historii vývoje PDF. Uživatel frumiousirc odpověděl, že vyhledávání je dnes tak špatné a jazykové modely tak dobré, že je rychlejší věc znovu napsat než znovu použít. A piokoch to shrnul jako levnou strategii pro publicitu, podobně jako se vyrojily čtečky PDF a AI nadstavby terminálu. Vedle toho se řešily praktické věci: febed chtěl odemykání hesla a podpisy, na což autor odepsal, že pdf_decrypt i pdf_sign už existují, chiharukiryu se ptal na oficiální rozhraní a dozvěděl se o desktopové aplikaci pro macOS, Windows i Linux, a spwa4 snil o jednom HTML souboru s malým lokálním modelem, který by nástroje ovládal hlasem i na pracovním notebooku.

Čtenář si z vlákna odnese známý střet: touha po soukromém nástroji bez cloudu je silná, i když komunita pochybuje, zda kvůli ní má vznikat další PDF engine.
