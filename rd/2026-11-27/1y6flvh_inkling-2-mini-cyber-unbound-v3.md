# 1y6flvh
**Inkling-2-Mini dostal cyber variantu i opravu zacykleného uvažování**

r/LocalLLaMA · u/GodGMN · 27. listopadu 2026, 01:16 · 156 bodů / 15 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y6flvh/)

Autor GodGMN předělal Inkling-2-Mini na rychlý offline model pro autorizovaný bezpečnostní výzkum, red-teamové inženýrství a práci s threat intelligence. Cyber varianta vznikla tréninkem malé LoRA rank-16, která se dotkla jen 0.0065 % parametrů, tedy 20 ze 704 tenzorů a 1.72M parametrů. Souběžně se v komunitě řeší verze Unbound v3 a Prime, které odstraňují zacyklené uvažování a zrychlují odpovědi, přičemž Prime přináší stejnou opravu do původního cenzurovaného modelu.

Adapter autor nasplicoval přímo do dvaceti matic Q8_0 attn_output.weight v měřítku 1.55 a všech 128 MoE expertů i zbylých 684 tenzorů zkopíroval beze změny, takže výsledek běží ve vanilla llama.cpp, Ollamě i LM Studio bez vlastních doplňků. Na Hugging Face vystavil kvantizace IQ4_NL s 17.63 GB pro 24GB VRAM, Q6_K s 24.70 GB a Q8_0 s 27.82 GB, vedle nich i vision mmproj a 6.89MB BF16 adapter se skriptem, kterým si lze dopočítat vlastní kvant. V číslech slibuje hlavně pád odmítnutí na CyberSecEval MITRE-120 ze 100 na 1 a úspěšnost 68.3 % plně a 75.8 % s částečnými odpověďmi proti nule u původního modelu, mapování CVE na CWE stouplo z 63.0 % na 66.0 % a AdvBench hlásí 95.2 % bez jediného odmítnutí.

Nejvíc hlasů dostalo nadšení uživatele u/q_tech_x51, který miluje komunitní úsilí kolem modelu a děkuje za příspěvek. Případný propad na plném HumanEval+ ze 153 na 136 ze 164 úloh mu pro vyloženě kybernetické nasazení přijde přijatelný a věří, že část ztráty půjde doladit. Na to navazuje otázka u/OnlyKindaThrowAway, jestli metoda snižuje odmítání obecně, nebo jen u bezpečnostních témat, a u/TheGlobinKing se s omluvou za hloupý dotaz ptá, zda z benchmarků naopak neplyne velké vítězství pro Qwen.

Odlehčenou linku obstaral u/FastHotEmu, který se směje, že Tintero je skvělé jméno pro autorův vlastní engine, a tipuje španělštinu. Praktickou starost přidal u/SkyFeistyLlama8: chválí vlastní inferenční platformu a ptá se, zda při podpoře ARM64 na DGX Spark poběží i čistě na ARM64 CPU bez CUDA, protože na Snapdragon X notebooku je Inkling v llama.cpp hodně pomalý a NPU model zatím nepodporuje. Uživatel u/raspy00135 pak jen stručně děkuje za váhy.

Kdo chce malý lokální model na bezpečnostní analýzu bez cloudu, má teď k dispozici variantu šitou na MITRE a CTI s návodem, jak si ji přeuspořádat do vlastní kvantizace.
