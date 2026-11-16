# 1xobe4h
**CCORE GLB-3D-Coder 4B: malý model staví 3D assety a exportuje GLB**

r/LocalLLaMA · u/ConfidentDinner6648 · 5. listopadu 2026, 07:14 · 341 bodů / 62 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xobe4h/)

Autor vydal finální verzi modelu CCORE GLB-3D-Coder, plný fine-tune modelu Qwen3.5-4B zaměřený na znovupoužitelné 3D assety. Stačí slovně popsat, co chcete, a model napíše kompletní Three.js HTML scénu s tlačítkem Export GLB – tu otevřete v prohlížeči, zkontrolujete výsledek a vyexportujete do Godotu, Blenderu, Unity a dalších nástrojů. Kromě fantasy postav zvládá budovy, prostředí, zbraně, vozidla, laboratorní vybavení, nábytek nebo sportovní potřeby a do exportu umí přidat i animace.

Kvantizační debata se rozhořela hned pod příspěvkem. u/Delicious_Stress_911 shrnul zkušenost mnoha zkoušejících lakonicky: Q4 je prakticky nepoužitelná, Q8 už dává skvělé výsledky. u/GlassLow5680 to doplnil o praktický postřeh, že Q4 rozběhne i na CPU, zatímco Q8 běží velmi svižně i na Google Colab T4, takže se hodí na herní assety nebo jako reference pro modelování.

Velikost modelu je pro komunitu hlavní atrakcí. u/MuDotGen se diví, že něco takového jde ve 4B parametrech, u/Equivalent_Bit_461 hlásí příchod éry malých modelů a u/MehTheHedgehog v tom vidí budoucnost open source – malé specializované fine-tuny, až velkých otevřených vah ubude. u/silenceimpaired přiznává, že pro model nemá využití, ale hlasuje pro už kvůli licenci Apache, u/CommitteeInfamous973 zase chválí příslib veřejného trénovacího datasetu, který autor chystá vydat 6. listopadu. Ke stažení jsou GGUF varianty Q4_K_M kolem 2,7 GB a Q8_0 plus plné váhy v Safetensors.

Nechybí ani skepse a zvídavé otázky. u/-p-e-w- předpovídá, že podobné nástroje v příštích letech sníží cenu vývoje her o 99 % a nechají práci jen naprosté špičce 3D umělců, zatímco u/heliosythic a u/breadnone rýpou do low-poly vzhledu – podle nich už v tomhle stylu nikdo pořádný hry nedělá a všechny modely včetně Claude produkují podobně mdlý styl. Praktičtější je výtka u/Flashy_Jellyfish_258, kterému jdou dobře postavy z videa, ale nedaří se ulice, sníh nebo stromy a styl mu přijde zapečený v modelu. K tomu se přidávají dotazy, kolik vlastně takový trénink stál, jestli by 4B model běžel na mobilu a jak dlouho fine-tune trval.

Autor odpovídá ukázkou místo teorie: v prohlížečové aréně RIFTWARD poskládal postavy, terén a rekvizity vygenerované lokálně právě tímhle modelem, sestavené pomocí orchestrace a validačního postroje. Hru si lze zahrát ve Space na Hugging Face, kde jsou i model, návod, systémový prompt a doporučené nastavení. Hlas s nejvřelejším tónem má u/juzzyreddit, který autorovi vzkazuje, ať pokračuje v postupném vylepšování – prý tuší, že se z toho vyklube něco velkého.
