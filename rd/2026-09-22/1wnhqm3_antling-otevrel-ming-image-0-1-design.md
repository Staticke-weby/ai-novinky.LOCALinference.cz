# 1wnhqm3

**inclusionAI otevřelo rodinu Ming-Image-0.1-Design: 6B model pro UI a design vede žebříček Artificial Analysis, Kijai ho přidává do ComfyUI**

| | |
|---|---|
| Subreddit | r/StableDiffusion |
| Autor | u/fruesome |
| Publikováno (Europe/Prague) | 22. 9. 2026, 20:32 |
| Skóre / komentáře | 223 / 40 |
| Odkaz | https://i.redd.it/x891zktr74rh1.png |
| Diskuse | https://www.reddit.com/r/StableDiffusion/comments/1wnhqm3/open_source_mingimage01design_family/ |

## Co se stalo

Na r/StableDiffusion vyšel 22. 9. 2026 příspěvek o open-source vydání rodiny **Ming-Image-0.1-Design** od inclusionAI (AntLing): jde o modely **Ming-Image-0.1-Design, 6B** a **Ming-Image-0.1-Design-Layer, 6B**, oba pod licencí MIT. První z nich vytváří kompletní uživatelská rozhraní, dashboardy, infografiky a plakáty ze strukturovaných promptů o délce až 8 000 tokenů, s konzistentním rozložením, typografií, barvami a obrázky, a nativně generuje RGBA assety s průhledným pozadím. Varianta **Layer** převádí sloučenou grafiku na 2–9 samostatně editovatelných RGBA vrstev. Přiložený obrázek je žebříček Artificial Analysis „Text to Image Leaderboard: UI/UX Design“, kde Ming-Image-0.1-Design figuruje na prvním místě se skóre 1082 Elo.

## Klíčová fakta

- **Ming-Image-0.1-Design, 6B** — text-to-image model pro UI, infografiky, plakáty a další textově bohatý vizuální design; licence MIT.
- **Ming-Image-0.1-Design-Layer, 6B** — převod sloučené grafiky na **2–9** nezávisle editovatelných RGBA vrstev.
- **Výsledky Layer varianty:** nejlepší výsledky ve **všech 12** hodnocených nastaveních na testovací sadě Crello a **4,3× rychlejší** běh než 20B otevřený baseline Qwen za stejného nastavení benchmarku.
- **Žebříček UI/UX (Elo z naslepo hlasovaných preferencí):** Ming-Image-0.1-Design **1082** (1. místo), Ideogram 4.0 (Quality) 1052, Ideogram 4.0 1015, HunyuanImage 3.0 Instruct 1005, FLUX.2 [dev] 1000.
- **Doporučené nastavení:** rozlišení 2048×2048 (nebo 1024×1024), 12 kroků vzorkování, CFG 1.0, BF16, jedna CUDA GPU s **80 GiB VRAM** (validovaná konfigurace).
- **Nasazení:** doporučeno přes vLLM-Omni; vylepšování promptů přes Ling-3.0-flash-VL nebo qwen3.8-27B.
- **ComfyUI:** Kijai implementaci přidal do ComfyUI (pull request Comfy-Org/ComfyUI #16482).
- Na Hugging Face měl model v době sběru dat **132 lajků**.

## Čísla

| Údaj | Hodnota |
|---|---:|
| Velikost modelů | 6B |
| Maximální délka strukturovaného promptu | 8 000 tokenů |
| Počet editovatelných vrstev (Layer) | 2–9 |
| Hodnocených nastavení na sadě Crello | 12 |
| Zrychlení proti 20B baseline Qwen | 4,3× |
| Elo Ming-Image-0.1-Design (UI/UX) | 1082 (1. místo) |
| Elo Ideogram 4.0 (Quality) / Ideogram 4.0 | 1052 / 1015 |
| Elo FLUX.2 [dev] | 1000 |
| VRAM pro validovanou konfiguraci | 80 GiB |
| Skóre příspěvku / komentářů | 223 / 40 |

## Citace

> „Ming-Image-0.1-Design vytváří kompletní UI, dashboardy, infografiky a plakáty ze strukturovaných promptů o délce až 8K tokenů, s konzistentním rozložením, typografií, barvami a obrázky.“ (překlad) — u/fruesome, vlastní text postu

> „Ming-Image-0.1-Design-Layer převádí sloučenou grafiku na 2–9 nezávisle editovatelných RGBA vrstev.“ (překlad) — u/fruesome, vlastní text postu

> „Ming-Image-0.1-Design je 6B text-to-image model pro UI, infografiky, plakáty a další textově bohatý vizuální design.“ (překlad) — inclusionAI, model card

> „Hardware: **jedna CUDA GPU s 80 GiB VRAM** (validovaná konfigurace).“ (překlad) — inclusionAI, model card

> „Pokaždé, když vyjde nový model, mám pocit, že si jen vymyslí ‚náhodný sloupcový graf benchmarku‘ a dají sebe na vrchol.“ (překlad) — u/CorpPhoenix, 66 bodů

> „Podpora průhlednosti **a** licence MIT!“ (překlad) — u/Technical_Fish_9638, 46 bodů

> „Jak to Kijai vždycky stihne dřív než plán, pracuje na implementacích do ComfyUI rychlostí světla?“ (překlad) — u/Haiku-575, 12 bodů

> „Vypadá to zajímavě, ale jejich GitHub repo zatím není dostupné.“ (překlad) — u/comfyanonymous, 22 bodů

## Co říkají komentáře

Nejvýraznější je **skepse k benchmarkovým grafům** — nejlépe hodnocený komentář (66 bodů) tvrdí, že si firmy výsledky vymýšlejí, a jiný diskutující oponuje („Vůbec ne, podívej se na nový benchmark s mým modelem!“). Druhé téma je **licence a průhlednost**: komentující chválí kombinaci MIT licence a nativní podpory průhlednosti (RGBA). Třetí je **ComfyUI**: Kijai sám odpověděl „Zkoumám to“ a ostatní oceňují, jak rychle implementace vznikají; objevuje se ale i upozornění, že repozitář na GitHubu ještě není přístupný. Diskutuje se také o **hardwaru** — jeden komentář cituje požadavek 80 GiB VRAM a jiný odhaduje, že ve fp16 má model asi 13 GB a v fp8/int8/Q8 GGUF kolem 7 GB. Několik lidí se ptá, kde v žebříčku chybí Krea 2, a zaznívá i pochybnost, zda výstupy nejsou „jen jpegy“.

## Rozpory a neověřené informace

- **Neověřené tvrzení autora postu:** že varianta Layer „dosáhla nejlepších výsledků ve všech 12 hodnocených nastaveních na sadě Crello“ a je „4,3× rychlejší než 20B baseline Qwen“ — jde o tvrzení autora, v balíčku nejsou primární data.
- **Neověřené tvrzení:** komentář u/boxwrenchx („Vůbec ne, podívej se na nový benchmark s mým modelem!“) odkazuje na obrázek v komentáři, který není v balíčku ověřen.
- **Neověřený odhad:** u/Acceptable_Secret971 odhaduje velikosti kvantizací („fp8, int8 nebo Q8 GGUF by měly být kolem 7 GB“).
- **Neshoda o umístění dalších modelů:** u/roculus se ptá, kde je Krea 2; u/Dante_77A tvrdí, že v kategorii UI/UX testována nebyla; u/stddealer ji řadí „těsně pod“ Ming-Image.
- **Rozpor o charakteru výstupů:** u/eggplantpot tvrdí, že příklady jsou „jen jpegy“, zatímco post i model card uvádějí nativní RGBA výstup s průhledným pozadím.
- **Neověřené pozorování:** u/comfyanonymous uvádí, že repozitář `github.com/inclusionAI/Ming-Image` nebyl v době komentáře dostupný.
- Poznámka k implementaci v ComfyUI („Kijai už to implementoval“) je v postu označena jako editace; sám Kijai odpověděl pouze „Zkoumám to“.

## Proč to je důležité

Ming-Image-0.1-Design cílí na jinou úlohu než běžné generátory obrázků: **textově bohatý design** — rozhraní, dashboardy, infografiky a plakáty s konzistentní typografií. Právě tam dosud otevřené modely selhávaly a musely se kombinovat s vektorovými editory. Vedle toho je významná kombinace **MIT licence a nativních RGBA vrstev**, která z modelu dělá prakticky použitelný nástroj v produkčním workflow (vrstvy lze dál editovat, ne jen vygenerovat plochý obrázek). Náročnost na 80 GiB VRAM zároveň ukazuje, že kvalita v této kategorii zatím není zdarma.

## Další diskuse

- [1wnipcz](https://www.reddit.com/r/LocalLLaMA/comments/1wnipcz/) — r/LocalLLaMA, 320 bodů, 32 komentářů: nový 6B image model, AntLing otevřel rodinu Ming-Image-0.1-Design.
- [1wnh7tk](https://www.reddit.com/r/LocalLLaMA/comments/1wnh7tk/) — r/LocalLLaMA, 107 bodů, 12 komentářů: AntLing otevřel rodinu Ming-Image-0.1-Design.

## Zdroje

- https://huggingface.co/inclusionAI/Ming-Image-0.1-Design
- https://huggingface.co/inclusionAI/Ming-Image-0.1-Design-Layer
- https://github.com/Comfy-Org/ComfyUI/pull/16482
- https://www.reddit.com/r/StableDiffusion/comments/1wnhqm3/open_source_mingimage01design_family/
- lokální snímek žebříčku: `2026-09-22/_data/img/1wnhqm3.png`
- komentáře: `2026-09-22/_data/raw/comments/1wnhqm3.json`
