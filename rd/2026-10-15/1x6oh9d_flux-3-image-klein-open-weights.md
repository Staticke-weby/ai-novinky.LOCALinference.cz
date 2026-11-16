# 1x6oh9d
**FLUX 3 Image Klein: open weights pro generování i úpravu obrázků**

r/StableDiffusion · u/stephen370 · 15. října 2026, 17:18 · 588 bodů / 335 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1x6oh9d/)

Black Forest Labs vydali open weights model FLUX 3 Image Klein s 5,6B parametry, který má zvládat generování i úpravu obrázků v jednom. Autor příspěvku u/stephen370 k oznámení nepřidal žádný vlastní text, jen odkaz na Hugging Face, i tak se pod ním sešlo 335 komentářů.

Odkaz vede na kolekci black-forest-labs/flux-3-image-klein na Hugging Face. Model podle popisu zvládne až 10 referenčních obrázků, nativní 4K, bounding boxy, editaci textu v obraze a style transfer, přičemž textový enkodér staví na Qwen3-VL-4B. Venku jsou base i distilled (turbo) varianty včetně kvantizací FP8, NVFP4 a INT8, které na kartách RTX 5070 a 4070 generují v rozlišení 1024×1024 výrazně rychleji než BF16 baseline, a přibyla i nativní podpora v ComfyUI.

První dojmy z testování jsou ale překvapivě tvrdé. u/meknidirta shrnuje po úvodních zkouškách, že model je k ničemu, u/Different_Fix_2217 mluví o nejrůznějších anatomických chybách, zlomku znalostí oproti Krea a dosud nejcenzurovanějším modelu. Na cenzuru si stěžují i další, u/SysPsychovi přijde výrazná a u/Shap6 nejdřív extrémní, i když pak přiznává, že se dostatečným přemlouváním dá z modelu nějaká nahota dostat.

Vlákno se rychle plní konkrétními příklady zpackaných výstupů. u/SneckoWatcher popisuje výsledky jako roztavené a zdeformované palivo pro noční můry, u/wunderbaba upozorňuje, že už samotné stock prompty v šablonách pro ComfyUI lezou s obličejem ve stylu Clegana. u/generate-addict to přirovnává v text-to-image k návratu časů SD3, Flux 2 je podle něj v přímém srovnání promptů lepší a vedle Krea 2 vypadá novinka jako odpad, editaci obrázků ještě nezkoušel.

Technická linka diskuse se drží spíš toho, co kolem modelu vzniklo. u/TheSlateGray připomíná Comfy soubory ve variantách BF16, INT8 a NVFP4 a dodává, že podpora dorazila do ComfyUI skoro ve stejnou chvíli jako oznámení. Vedle toho se ozývá nedůvěra k velikosti, u/Calm-Road-1962 se bojí pouhých 5B parametrů a u/DisorderlyBoat se ptá, proč laboratoř vydává model, který působí jako tři roky regrese v kvalitě. Světlou výjimkou je u/Friendly-Fig-6015, podle kterého je porozumění promptům i kvalita úžasná, pokud se člověk nepouští do NSFW obsahu.

Kdo čekal lehkého nástupce Flux 2 Klein, odchází zatím spíš s varováním: papírově bohatá výbava proti rozpačitým prvním obrázkům a ostré debatě o cenzuře.
