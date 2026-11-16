# 1xlh0zw
**GLB-3D-Coder: malý 4B model tvoří 3D assety pro Godot**

r/LocalLLaMA · u/ConfidentDinner6648 · 1. listopadu 2026, 23:56 · 284 bodů / 60 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xlh0zw/)

Vývojář z komunity dotrénoval Qwen3.5-4B na generování herních 3D assetů. Model s názvem GLB-3D-Coder píše Three.js scény s exportem do GLB, takže výsledné objekty lze přenést do editorů jako Godot. Navazuje na autorův předchozí 3D coding model a video v příspěvku ukazuje několik ukázek včetně importu přímo v Godotu.

Ovládání má být záměrně jednoduché: stačí systémový prompt z model card a obyčejné anglické zadání typu „Create a mana potion“ nebo „Build a weathered frontier medic station“. Jde o první funkční checkpoint, který má v testech většinou vyjít na první pokus, i když část generací potřebuje opakování nebo drobnou opravu kódu. Autor doporučuje teplotu 0.8, top-k 40, top-p 0.95 a min-p 0, trénink měl doběhnout večer 2. listopadu a po jeho konci slibuje plné Safetensors váhy i trénovací dataset. Kvóty Q4_K_M a Q8_0 mezitím vyměnil za novější checkpoint se znatelně lepší kvalitou, staré soubory je potřeba smazat a stáhnout znovu.

Komunita nápad s neutrálním formátem rychle pochopila. Jak píše u/CiobanuXashi, generování Three.js scény s exportem do GLB elegantně obchází „problém enginu“, protože model musí umět jen jeden formát a GLB pak vezme Godot i Unity. Vedle toho se množí pochvaly za užitečnost při prototypování, u/MKU64 to vidí jako cestu, jak může kdokoli začít stavět své nejzajímavější herní nápady, a u/Uncle___Marty autorovu práci jen stručně označuje za úchvatnou.

Nejživější je debata o tom, co kolem modelu postavit dál. u/Yorn2 navrhuje aplikaci ve stylu FastAPI, která by z textového vstupu rovnou chrlila GLB soubory, a k tomu propojení přes MCP až do Godotu. u/Galactic_Neighbour se ptá, proč model negeneruje GLB přímo a co vlastně produkuje, a rovnou nadhazuje další směr: trénink na procedurální textury z node editorů jako Blender nebo Material Maker z Godotu, jehož projektové soubory jsou obyčejný JSON. K tomu se přidává otázka u/Photoperiod, zda model zvládne vyrobit 3D asset z 2D obrázku podobně jako Meshy, a pochybnost u/politefella0, jestli se Three.js práce do Godotu vůbec dobře přenáší.

Třetí linka řeší dostupnost a praktické limity. Na 4B velikost žasne víc lidí, u/saumanahaii obdivuje, že se to do tak malého modelu vůbec vešlo. u/Square_Light1441 prosí o kvantizaci pro uživatele s málem VRAM a u/LaidBackDev se ptá, zda to poběží na notebooku s 8 GB RAM. u/Usual-Buffalo-1791 zase řeší, zda model nesype zbytečné vertexy a těžké plochy navíc, což je u herních low-poly assetů zásadní. Inspirativně působí vzkaz u/StubbornNinjaTeej, kterého předchozí autorův příspěvek přivedl k vlastní LoRA pro CadQuery díly na FDM tisk, zatímco u/Cool-Chemical-5629 sní o větší MoE směsi, kde by podobní malí specialisté dělali agenty, frontend, 2D, 3D nebo audio.

Z vlákna tak zbývá hlavně příslib: malý lokální model, pár slov v angličtině a herní rekvizita připravená k importu do Godotu.
