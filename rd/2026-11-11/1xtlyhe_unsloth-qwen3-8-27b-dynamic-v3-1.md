# 1xtlyhe
**Unsloth vydal kvantizace Qwen3.8-27B v3.1. Slibuje o 5–10 % lepší přesnost**

r/LocalLLaMA · u/danielhanchen · 11. listopadu 2026, 17:17 · 441 bodů / 126 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xtlyhe/)

Unsloth zveřejnil nové dynamické GGUF kvantizace v3.1 pro model Qwen3.8-27B. Pokrývají škálu od dvoubitových po šestibitové verze, tříbitové autor neaktualizoval, protože starší UD3 jsou prý na stejné úrovni, a na DeepSWE, Terminal Bench a dalších úlohách mají být o 5–10 % přesnější než UD3, GSQ-RCO a Exllama-3. Agentní benchmarky běžely s kontextem 256K, ostatní se 128K a klíčové testy opakoval několikrát, LiveCodeBench například šestkrát.

Nejdelší část oznámení věnuje autor tomu, proč jeho čísla vypadají jinak než u konkurence. U Exllamy-3 vynechal z osy grafu vrstvu tokenových embeddingů, protože ji Exllama drží v BF16, a tvrdí, že při započtení plné velikosti ke stažení a reálné spotřeby paměti vychází Exllama hůř. U GSQ-RCO odhaduje, že soupeř měřil LiveCodeBench jen s rozpočtem kolem 96K, kde jeho kvantizace vedou, zatímco při 128K se karta obrací ve prospěch Unslothu, a jednorázovou stoprocentní obnovu přesnosti na AIME25 staví proti vlastním čtrnácti běhům s průměrem 93–96 %.

Komunita ale nejvíc řeší samotné grafy. U/fgk55555 píše, že u většiny bodů včetně vrcholů chybí popisky a nechápe propad skóre mezi Q3 a Q4 na DeepSWE a Terminal Bench – kdyby podle nich vybíral kvantizaci pro kartu s 24–32 GB, netušil by kterou, a celé to prý vypadá, že vychází nejlépe IQ3_S. Podobně se u/_wortkarg_ ptá, které dva body ze trojice UD-IQ3_XXS, UD-IQ3_S a UD-Q3_K_XL jsou v grafu zobrazené a které verze obsahují vestavěný MTP návrh.

Kritičtější linku přidává u/geekyjackson, podle kterého v grafech chybí obrovské implicitní chybové úsečky a tak neprůkazná data firmě, která je jinak zlatým standardem GGUF kvantizací, spíš škodí na důvěryhodnosti. Chtěl by otevřené a ověřitelné testování, tohle na něj působí spíš jako marketing než věda. Praktičtější dotazy pak míří na to, jestli je zlepšení pětibitových a šestibitových verzí tak velké, aby se kvůli nim vyplatilo je znovu stahovat, jak se ptá u/james_pic, nebo zda by šel zmenšit MTP soubor, když varianta od GSQ-RCO má 10,90 GB proti kombinaci Unslothu s 12,27 GB, jak spočítal u/deeefunkt.

Vedle toho se řeší, zda půjde stejným postupem ořezat tokenizér pro 16GB kartu, jak běží UD-Q4_K_M na MacBooku proti oQ4e a oQ6e a zda se dočkají i aktualizace NVFP4, EXL3 nebo dalších modelů. Nechybí ani popichování k budoucnosti – u/EngelbertStuss z grafů vyvozuje, že autor už musí mít v ruce váhy Qwen4, u/Hefty_Wolverine_553 by s ním rád viděl souboj proti NVFP4 a EXL3 a u/DefNattyBoii namítá, že Exllama je dál ve vedení pro ty, kdo mají videopaměť, protože její varianty umí poskládat kdokoli doma. U/bennmann to celé shrnuje přáním, aby byl v příštích týdnech udržitelný aspoň spánek autorů.

Pro zájemce o lokální běhání tak zůstává hlavní otázka prostá: kterou kvantizaci reálně stáhnout na svou kartu, na což zatím ani nové grafy jasně neodpovídají.
