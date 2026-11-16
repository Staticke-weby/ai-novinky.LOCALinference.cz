# 1xdh57e
**Vibecoding vlastního inference engine: llama.cpp v WebGL**

r/LocalLLaMA · u/CodeMichaelD · 23. října 2026, 17:26 · 739 bodů / 168 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xdh57e/)

Autor se pokusil napsat od nuly vlastní inference engine pro GGUF modely, který běží v prohlížeči přes WebGL2. Kvantovaný model na q4 stránkuje do výpočetních bufferů zapisovaných přes GLSL přímo v HTML, jenže tokenizer a slovník se podle jeho slov změnily v nekonečné debugovací peklo. Proto ostatním vzkazuje, ať to nedělají po něm a raději prostě naklonují llama.cpp.

Soudě podle ohlasů umí jeho výtvor první věty překvapivě slušně, pak se ale zadrhne. Model prý slibuje, že pro uživatele uspořádá obrovskou párty, a následně sklouzne do nekonečné záplavy vykřičníků. Právě tahle nadšená smyčka se stala hlavním hrdinou celého vlákna.

Nejvyšší ohlasy sbírají narážky na rozjařenou povahu modelu. u/utxohodler oceňuje, že to má charakter, u/No-Craft-7979 dodává, že je model prostě hodně nadšený a u/sandraviolskyia se ptá, zda by takovou párty vůbec šlo odmítnout. u/YoungCobbler tápe v identitě a ptá se, jestli je Qwen, zda je Qwen autor a kdo vlastně Qwen je, a zároveň se zajímá, jaká ta párty byla. u/VacuumMoonshine si rýpl, že takhle ještě nikdy nikdo nemluvil, a hlášku o párty zopakoval i s tou záplavou vykřičníků.

Věcnou linku drží u/someguyinr, podle kterého už samotná věta o párty dokazuje, že dekvantizace q4 a první násobení matic fungují. Podezřívá dvě klasické chyby druhého kola generování: když se v shaderu objeví přetečení nebo nulové logity, sampler s argmaxem spadne na token s ID 0, což je v daném slovníku právě vykřičník, anebo se o jeden krok rozjede posun KV cache či RoPE, protože WebGL2 nemá nativní výpočetní buffery a vše se emuluje přes textury. Do toho zapadá i stručná rada u/tetelestia_, aby autor nepoužíval argmax pro vzorkování tokenů.

Zbytek diskuse řeší, jestli má takový projekt vůbec smysl. u/VacuumMoonshine se diví, proč někdo od nuly staví engine na WebGL, když má llama.cpp rovnou backend pro WebGPU, a sampling podle něj vypadá jako větší problém než tokenizer. Podobnou zkušenost popisuje u/GamerHaste z práce na inference v Amazonu, kde se výstup trénovacího a inferenčního týmu rozcházel kvůli desítkám tisíc drobností a ladění připomínalo hodiny hledání neviditelné chyby. Smířlivější tón přidává u/LasseDen950432te, že právě tahle bolest je jeden z nejlepších způsobů, jak se o generativní AI něco naučit.

Čtenář si odnese, že vibecoding s trpělivostí dojde překvapivě daleko, ale parita s llama.cpp se skrývá v detailech sampleru a paměti.
