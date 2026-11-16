# 50380704
**Stroq ukáže, co váš kódovací agent skutečně dělal**

Hacker News · agybay_07 · 5. listopadu 2026, 16:54 · 79 bodů / 27 komentářů · [diskuse](https://news.ycombinator.com/item?id=50380704)

Na Hacker News se představil Stroq, lokální audit a strážce pro kódovací agenty typu Claude Code, Codex CLI nebo Cursor. Načte session za posledních 30 dní a ukáže, které příkazy vznikly z textu, který agent předtím přečetl, a které klíče opustily stroj.

Popis na GitHubu slibuje, že nástroj jen vypisuje názvy klíčů, nikdy jejich hodnoty, a vše zůstává v ~/.stroq bez účtu a telemetrie. Hooky mají před spuštěním posuzovat každé volání, zastavit curl | sh i odchozí volání nesoucí známé tajemství, a když příkaz opakuje přečtený text, agent se má nejdřív zeptat. Instaluje se příkazem npx @stroq/cli, potřebuje Node.js 22 a je pod Apache-2.0.

Nejostřejší výhradu vznesl uživatel embedding-shape: audit je podle něj pozdě, když agent už stihl spustit něco jako rm -rf --no-preserve-root. Napsal, že kdo je jeden zatoulaný příkaz od smazání vlastního počítače, provozuje agenta špatně, a místo auditování by mu měl dát vlastního uživatele a omezit cesty a síť. Autor na to v úvodu jen stručně odpověděl, že Stroq má chránit před nebezpečnými příkazy, které agent pouští bez kontroly.

Další linka se točila kolem toho, jak vyhodnocování funguje. Uživatelé emscb, bill10 a sebion7125 se ptali, zda za tím je model, nebo pravidla, a autor potvrdil, že žádné LLM se neúčastní a čte se přímo log session a text příkazů. Uživatel lhk931122 nadhodil, že velký model by byl přesnější, ale stál by tokeny a čas, a autor dodal, že pravidla sice nechytí všechno, ale může je doplnit kdokoli, zatímco model čte stejný text jako agent, takže ho lze oklamat také.

Zbytek vlákna míchá nápady s odlehčením. Uživatel hmokiguess navrhl démona na pozadí s ikonou v liště, který upozorní na shodu a nabídne začernění či opravu, uživatel maven29 doporučil eBPF backend a uživatel philips popsal vlastní izolaci v gVisor s proxy, která spojení pozastaví a nechá člověka kývnout na hostitele hypervisorovou klávesou. Mezitím se řešilo, zda se Stroq vyslovuje jako stroke, a chválila se sovička Hoo jako maskot.

Kdo pouští agenta do terminálu, asi by si měl nejdřív zkontrolovat, co už agent četl a kam poslal klíče, a teprve pak řešit, zda mu věří i příště.
