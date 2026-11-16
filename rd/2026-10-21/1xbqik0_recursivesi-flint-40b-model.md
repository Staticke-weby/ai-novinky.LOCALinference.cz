# 1xbqik0
**RecursiveSI/flint: 40B model s 2,5B aktivními parametry**

r/LocalLLaMA · u/coder543 · 21. října 2026, 17:38 · 441 bodů / 176 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xbqik0/)

Příspěvek bez vlastního textu upozorňuje na novinku na Hugging Face: Recursive Flint, decoder-only mixture-of-experts model pro kódové agenty a lokální provoz. Má 39,8 miliardy parametrů celkem a přibližně 2,5 miliardy aktivních na token, zbytek se dopočítává podle konvence s výstupní hlavou. Vlákno s označením New Model se rychle stočilo k poměru výkonu a nároků na hardware.

Karta na Hugging Face ho popisuje jako stroj na procházení repozitářů, opravy chyb, přidávání funkcí a psaní testů, s podporou uvažování, vícekrokového volání nástrojů a chatovací šablonou. V release evaluacích uvádí 54,9 % na Terminal-Bench 2.1, 89,7 % na SWE-bench Pro v2 a 74,2 % na SWE-bench Verified, dokumentovaný kontext 262 144 tokenů a znalostní cutoff červen 2026. BF16 checkpoint má kolem 80 GB, nástup přes SGLang počítá s jednou B300 nebo H200, licence je Apache 2.0 a navazující oznámení Nvidie slibuje přes 220 tokenů za sekundu na 64GB RTX Spark díky specializovaným kernelům.

Nejvýše je srovnání s Qweny. u/AnonLlamaThrowaway píše, že to vypadá jako vytoužená 3.8 35B-A3B, u/Yeelyy kontruje, že kdyby neexistovala Qwen3.8-27B, byl by tenhle drop šílený. u/politefella0 dodává, že na takovou velikost MoE čekal, ale od Qwen, Google a Mistral, a u/Easy_Refrigerator280 bere Flint na papíře jako rychlejší náhradu Qwen3.8 pro vývoj na 32GB w7800 a rovnou přihodil rychlý test obou modelů na stejném promptu se dvěma odkazy na jsfiddle.

Druhá linka řeší, komu se vejde do sestavy. u/crusaderky tvrdí, že nika je úzká: moc velký na 32GB unified, zatímco při 128GB unified nebo kombinaci 12GB VRAM a 64GB RAM je lepší Qwen3.8-Flash a při 24GB kartě Qwen3.8 27B, takže smysl vidí hlavně u 64GB unified nebo 12GB VRAM s 32GB RAM. Na to navazují prosby majitelů slabších strojů, kdy se u/snowieslilpikachu69 ptá na 8 GB plus 32 GB a u/NotSylver lituje, že to tak těsně nevychází, zatímco u/FatheredPuma81 vtipkuje, že dav se slabším VRAM teď někde pořádá večírek.

Třetí část vlákna jsou praktické zádrhele. Nejčastější povzdech je „bez vision", který napsal u/ubrtnk a rozvedl u/wren6991 nápadem, zda by někdo nepřilepil vision encoder po vzoru GLM-5.2. u/CulturalKing5623 našel stále otevřený pull request do llama.cpp na architekturu Flint, u/IntelligentRocks hlásí, že Ollama i v pre-release končí chybou 500 s neznámou architekturou, a u/hojnikb se nedaří model načíst ani v aktuálním Unsloth. u/wFXx upozorňuje, že odkazy na kartě modelu kromě dokumentace vedou na 404, dává odkaz na Unsloth GGUF a slibuje, že Flint postaví proti LFM MoE, a u/Porespellar se ptá, proč se reportuje Terminal-Bench 2.1, když ostatní honí verzi 4.0.

Kdo má kolem 64 GB jednotné paměti nebo silnější Nvidii a shání otevřeného lokálního kodéra s nástroji, má dalšího vážného kandidáta — jen si zatím musí pohlídat podporu ve svém runtime.
