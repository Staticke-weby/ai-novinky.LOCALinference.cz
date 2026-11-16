# 1x3y8ot
**RTX Video Super Resolution pro ComfyUI: dlouhá videa na disk**

r/StableDiffusion · u/Away_Exam_4586 · 12. října 2026, 12:23 · 243 bodů / 43 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1x3y8ot/)

Autor sdílel odkaz na novou komponentu pro ComfyUI, která optimalizuje RTX Video Super Resolution pro dlouhá videa s ukládáním na disk a nízkou spotřebou RAM. Umí AI upscaling, odšumování a odblurrování, kódování H.264/HEVC přes NVENC, zachování zvuku a vestavěný náhled. Doplnil, že dobře funguje s jeho druhým projektem ComfyUI MiniMax H3 Extender, příspěvek nese označení News.

Největší část diskuse se točí kolem pochybnosti, zda má smysl to vůbec řešit. Nejvýše hodnocený u/rxg se upřímně ptá, jaký přínos mu uniká, když zkoušel super-resolution v jiném programu a vyšší rozlišení vypadalo stejně jako nižší. Na něj navazuje u/35point1: vestavěný RTX uzel v ComfyUI mu sice škáluje snímky rychle na větší rozměr, ale na kvalitě to podle něj skoro nic nemění, při nastavení na ultra a dvojnásobek je výsledek dokonce až nepřirozeně přeprocesovaný.

Opačnou zkušenost hlásí praktici. u/FinBenton píše, že RTX super-resolution používá ve vlastním přehrávači na bázi mpv pro Twitch a YouTube a zlepšení je podle něj propastné, hlavně u animované a 3D tvorby. u/Version-Strong ho prý používá už pár měsíců jako poslední krok za generováním videa a protože je nenáročný, čas navíc skoro nepozná. u/MastMaithun testoval schválně na nekvalitním videu a nejvíc mu zabrala kombinace kvality ultra s předzpracováním denoise ultra, po které téměř zmizelo třepotání obrazu.

Zbytek vlákna řeší srovnání a technické detaily. u/bloke_pusher se ptá na rozdíl proti oficiálním ComfyUI Nvidia VFX uzlům, u/rodinj chce ukázky a zmiňuje, že se SeedVR2 spokojený nebyl. u/AnonymousTimewaster nadhazuje, že uzel s DLSS je pro upscaling neuvěřitelný, u/paganspam zase srovnává s DLSS5 a jeho neuronovým renderingem, který mu přijde lepší, ale i pomalejší. u/HarvardCS19 se ptá, zda to zvládne video libovolné délky, a dodává, že Extender už má latentní upscaling, který by měl být lepší než VSR. Praktickou výtku přidává u/Radiant-Photograph46, který by chtěl jemnější kontrolu nad kódováním po částech a ideálně bezztrátovou volbu, a u/GlenGlenDrach se bojí o životnost SSD při průběžném ukládání na disk.

Kdo čeká zázračné dokreslení detailů, bude spíš zklamaný, jako lehký a rychlý finiš za generativním videem ale uzel podle části komunity dává smysl.
