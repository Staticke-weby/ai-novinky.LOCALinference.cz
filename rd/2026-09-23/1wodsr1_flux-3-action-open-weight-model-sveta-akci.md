# 1wodsr1

**Flux 3 Action: open-weight model světa akcí pro roboty**

| | |
|---|---|
| Subreddit | r/StableDiffusion |
| Autor | u/Scriabinical |
| Publikováno (Europe/Prague) | 23. 9. 2026, 20:18 |
| Skóre / komentáře | 140 / 47 |
| Odkaz | https://huggingface.co/collections/black-forest-labs/flux-3-action |
| Diskuse | https://www.reddit.com/r/StableDiffusion/comments/1wodsr1/flux_3_action_7b_action_world_model/ |

## Co se stalo

Uživatel u/Scriabinical zveřejnil 23. 9. 2026 ve 20:18 (Europe/Prague) v subredditu r/StableDiffusion příspěvek s flairem News a titulkem „Flux 3 Action – 7B model světa akcí“ (překlad). Odkaz vede na kolekci Black Forest Labs na Hugging Face. Příspěvek získal skóre 140 při 47 komentářích a poměru kladných hlasů 0,99.

Stažený externí obsah je modelová karta repozitáře `black-forest-labs/flux-3-action-base` (6198 znaků). Podle ní jde o model světa akcí (world action model) s otevřenými vahami o velikosti 7 miliard parametrů. Vstupem jsou snímky z kamery, stav robota a textová instrukce; výstupem je další dávka akcí (next chunk of actions), odšumovaná společně s následujícími snímky videa.

Repozitář `flux-3-action-base` je ale jen adaptační komponenta, nikoli hotová robotická politika. Obsahuje akční základ `flux-3-action-base.safetensors`, sdílený video VAE (`video_vae.safetensors`) a sdílený textový enkodér v adresáři `text_encoder/`. Základ má 457 tenzorů, video a textové toky, sdílený akční „trunk“ a akční hlavy `ee50` a `gaming`; nové typy těles (embodimentů) potřebují vlastní akční hlavy. Textový enkodér je neupravená kopie modelu Qwen/Qwen3-VL-4B-Instruct a jeho licence (Apache-2.0) zůstává v souboru `text_encoder/README.md`.

Hotové politiky se mají načítat z repozitářů SO-101 nebo DROID – jejich konfigurace na sdílené enkodéry odkazují automaticky. Karta uvádí dva finetuny a Space `multimodalart/flux-3-action-so101-sim`; kolekce má tři položky (základ se sdílenými enkodéry, politiku SO-101 a politiku DROID s optimalizačními variantami).

Licenčně model spadá pod FLUX Kommunity License v.1.0; textový enkodér pod Apache-2.0 a kód v projektu `flux-action` má vlastní licenci. Karta vymezuje i použití mimo rozsah: model vrací kloubní cíle (joint targets) a neomezuje rychlost, sílu ani pracovní prostor kloubu – limity musí vynutit aplikace a hardwarové zastavení musí být na dosah; před provozem u lidí doporučuje validaci v simulátoru. Zakázané je použití v rozporu se zákonem, ovládání stroje ohrožující lidi bez dohledu, plně automatizované rozhodování s dopadem na práva jednotlivce a obtěžování či zneužívání nezletilých. Hlášení bezpečnostních obav míří na safety@blackforestlabs.ai.

Balíček slučuje ještě tři související diskuse: testy modelu Ming Image v ComfyUI, zrychlení video VAE modelu MiniMax H3 a pracovní postup (workflow) V6 pro cílené úpravy videa pomocí masky.

## Klíčová fakta

- Black Forest Labs vydali Flux 3 Action, model světa akcí s otevřenými vahami (open weights) o velikosti 7B, přes kolekci na Hugging Face.
- Model bere snímky kamery, stav robota a textovou instrukci a vrací další dávku akcí, odšumovanou společně s dalšími snímky videa.
- Repozitář `flux-3-action-base` je adaptační komponenta, ne kompletní politika; obsahuje akční základ, sdílený video VAE a sdílený textový enkodér Qwen3-VL-4B-Instruct.
- Základ má 457 tenzorů se sdíleným akčním trunkem a hlavami `ee50` a `gaming`; nová tělesa potřebují vlastní akční hlavy.
- Hotové politiky pro SO-101 a DROID odkazují sdílené enkodéry automaticky; hlavy pro nový robot nebo simulátor lze dotrénovat podle návodu Fine-tune.
- Licence modelu je FLUX Kommunity License v.1.0, textový enkodér zůstává pod Apache-2.0, kód `flux-action` má vlastní licenci.
- Model vrací kloubní cíle a neomezuje rychlost, sílu ani pracovní prostor — limity musí hlídat aplikace.
- Obrázek k postu o VAE je graf měření „Video VAE MiniMax-H3, čas na krok“ (překlad) s upřesněním „1344×768, 129 snímků, RTX 5090. Kratší je lepší.“ (překlad) a porovnáním stavu „před touto aktualizací“ a „nyní“ ve fázích kódování a dekódování.

## Čísla

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Velikost modelu Flux 3 Action | 7B (open weights) | modelová karta |
| Tenzory v akčním základu | 457 | modelová karta |
| Lajky u `flux-3-action-base` | 70 | modelová karta |
| Sledující Black Forest Labs | 41,8 tis. | modelová karta |
| Lajky u `Kijai/Ming-Image-ComfyUI` | 55 | modelová karta Ming |
| Stažený text modelové karty | 6198 znaků | balíček |
| Skóre / komentáře hlavního postu | 140 / 47 | metadata postu |
| Zrychlení kódování video VAE MiniMax H3 | až ~2,2× | post o VAE a blog Comfy |
| Zrychlení dekódování video VAE MiniMax H3 | ~1,4–2,7× | post o VAE a blog Comfy |
| Ming: paměť a čas generování | ~19,7 GB na RTX 4090, ~50 s na 2048×2048 při 12 krocích | text postu u/GreyScope |

Měření z grafu v postu o VAE (1344×768, 129 snímků, RTX 5090; zrychlení vztaženo k nejpomalejšímu kroku dané fáze):

| Varianta | Fáze | Před aktualizací | Nyní |
|---|---|---|---|
| Default VAE | kódování | 17,5 s (1,0×) | 11,7 s (1,5×) |
| Default VAE + `--fast fp16_accumulation` | kódování | 17,6 s (1,0×) | 8,1 s (2,2×) |
| Default VAE | dekódování | 12,2 s (1,0×) | 10,7 s (1,1×) |
| Default VAE + `--fast fp16_accumulation` | dekódování | 10,2 s (1,2×) | 8,2 s (1,5×) |
| int8 VAE | dekódování | 6,7 s (1,8×) | 4,6 s (2,7×) |

Slučované posty podle metadat: Ming Image 157 / 29 komentářů, Ming v Comfy 39 / 33, VAE MiniMax H3 167 / 51 a workflow V6 357 / 73. Z komentářů: dekódování 15sekundového videa o 1 MP jednomu uživateli trvá 120 sekund (po vlastní optimalizaci 90 s), jinde devítiminutová generace s krokem zkráceným z 10 na 5 sekund.

## Citace

> „Flux 3 Action je model světa akcí s otevřenými vahami o velikosti 7B. Bere snímky z kamery, stav robota a textovou instrukci a vrací další dávku akcí, odšumovanou společně s dalšími snímky videa.“ (překlad) — Black Forest Labs, modelová karta `flux-3-action-base`

> „Toto je adaptační komponenta, nikoli kompletní robotická politika.“ (překlad) — Black Forest Labs, modelová karta `flux-3-action-base`

> „Nic v modelu neomezuje rychlost, sílu ani pracovní prostor kloubu; limity musí vynutit aplikace a hardwarové zastavení musí být na dosah.“ (překlad) — Black Forest Labs, modelová karta `flux-3-action-base`

> „Pěkné, snad je to znamení, že plný vývojový model není daleko! Zajímavé také je, že vydali základní model tohohle.“ (překlad) — u/retroblade, komentář (42 bodů) pod postem 1wodsr1

> „Dekódování 15sekundového videa o 1 MP mi na sestavě trvá 120 sekund. Už jsem to stáhl na 90 s, ale když se s touhle novinkou dostanu na 60 s, je to celá ušetřená minuta na generaci.“ (překlad) — u/LuluViBritannia012, komentář pod postem 1woj0is

> „Nevím, zkrácení desetisekundového procesu na 5 sekund, když máte devítiminutovou generaci, mi nepřijde tak působivé.“ (překlad) — u/Dirty_Dragons, komentář pod postem 1woj0is

## Co říkají komentáře

Nejvýše hodnocený komentář (42 bodů, u/retroblade) čte vydání jako signál, že se blíží plný vývojový model Flux 3, a v úpravě dodává, že obrazová část ještě vydaná nebyla, takže to vidí zhruba na měsíc. V odpovědi (13 bodů) u/SlothFoc předpovídá, že nejdřív vyjde verze „vše v jednom“ (all-in-one), kterou nikdo nespustí, a pak zvlášť destilovaný obrazový/editovací a zvlášť video model — podle vzorce minulých vydání. u/physalisx (18 bodů) doporučuje oficiální stránku modelu.

Druhý proud jsou vtipy o nasazení v domácnosti: u/__ThrowAway__123___ (37 bodů) píše, že model nainstaloval na robotický vysavač a ten mu utekl, u/nok01101011a se ptá po kvantizované abliterované verzi s tím, že „jeho toustovač se nudí k smrti“ (překlad). Vážněji se řeší, co model je: u/Murder_1337 se ptá, zda jde o model vidění a akcí (vision action model), u/danque odpovídá, že jde o model vizuálního rozpoznávání pro úlohy v reálném světě, a u/fjgcudzwspaper-6312 zvažuje využití pro generování videa. Zazněl i spor o to, zda je 7B málo.

U VAE MiniMax H3 se diskuse točí kolem praktického přínosu. u/rapkannibale (12 bodů) cituje blog Comfy: pro nejrychlejší dekódování použijte int8 VAE jako přímou náhradu standardního. u/StopCreepy se ptá, zda stačí vyměnit fp16 za int8, nebo je třeba měnit workflow. Proti sobě stojí u/Dirty_Dragons (7 bodů), že zkrácení deseti sekund na pět u devítiminutové generace není působivé, a u/Broad_Relative_168 (9 bodů) i u/LuluViBritannia012 (6 bodů), že při častém opakování jde o znatelnou úsporu.

Pod workflow V6 vysvětluje autor u/roychodraws (21 bodů), že maska nezasahuje nežádoucí oblasti: nahradit jednoho člověka v davu zadáním (prompt) je obtížné, kdežto maskou se oblast izoluje a postava se do ní vloží. u/vibribbon (20 bodů) glosuje, že nějaká klaunka posouvá jednu z nejmodernějších oblastí AI práce. u/__generic (9 bodů) namítá, že totéž zvládne běžné workflow Comfy s referencemi, a u/Easy_Werewolf7903 (8 bodů) se ptá na čas generování desetisekundového videa jako měřítko pro vlastní RTX 6kpro.

## Rozpory a neověřené informace

- Načasování plného Flux 3: u/retroblade tvrdí, že plán zavádění ukazuje nevydanou obrazovou část modelu a vydání vidí zhruba za měsíc; jde o jeho čtení plánu, nikoli o potvrzený termín.
- Podoba budoucích vydání: předpověď u/SlothFoc o nespustitelné verzi „vše v jednom“ (all-in-one) a oddělených destilovaných modelech je spekulace z minulých vydání.
- Otázka u/fjgcudzwspaper-6312, zda model funguje jako predikce dalšího snímku a zda se dá použít pro generování videa, zůstala bez jednoznačné odpovědi.
- Domněnka u/Samurai2107, že MiniMax po oznámení obrazového modelu od Black Forest Labs vydá vlastní obrazový model, je spekulativní rivalita bez opory v podkladu.
- Naměřené hodnoty Ming Image (~19,7 GB a ~50 s) pocházejí od jednoho uživatele a šlo o ověření konceptu.
- Údaje o zrychlení VAE jsou z blogu a z grafu; jde o měření na jedné konfiguraci (1344×768, 129 snímků, RTX 5090), nikoli o univerzální hodnoty.
- Komentáře k oběma postům o Ming Image nebyly staženy, takže k nim chybí diskusní odezva.
- Video k postu V6 (v.redd.it) se nestahuje — k dispozici je jen titulek, text a komentáře. Balíček také neobsahuje obsah odkazovaných stránek (blog, dokumentace, PR).

## Další diskuse

| id | subreddit | skóre | komentářů | čas | titulek (překlad) | permalink |
|---|---|---:|---:|---|---|---|
| 1wohtg7 | r/StableDiffusion | 157 | 29 | 22:49 | „Ming Image je opravdu dobrý…“ | https://www.reddit.com/r/StableDiffusion/comments/1wohtg7/ming_image_is_really_good/ |
| 1woagyt | r/StableDiffusion | 39 | 33 | 18:17 | „Nový model Ming pro tvorbu grafiky funguje v Comfy dobře“ | https://www.reddit.com/r/StableDiffusion/comments/1woagyt/graphic_producing_new_model_ming_works_fine_in/ |
| 1woj0is | r/StableDiffusion | 167 | 51 | 23:36 | „Zrychlení video VAE MiniMax H3 na dvojnásobek“ | https://www.reddit.com/r/StableDiffusion/comments/1woj0is/making_the_minimax_h3_video_vae_2x_faster/ |
| 1wo8oqd | r/StableDiffusion | 357 | 73 | 17:11 | „Aktualizace V6 pro začátečníky: úprava cílené oblasti v libovolném videu a vložení postavy do prázdného prostoru“ | https://www.reddit.com/r/StableDiffusion/comments/1wo8oqd/v6_update_newbie_modify_a_targeted_area_of_any/ |

Post 1wohtg7 (u/Nid_All) ukazuje výsledky modelu Ming Image a odkazuje na repozitář `Kijai/Ming-Image-ComfyUI`. Post 1woagyt (u/GreyScope) popisuje praktický test v ComfyUI: autor vytvořil novou instalaci, nasadil požadavek na začlenění (pull request) a převzal workflow z jeho stránky; zadání dal minimum detailů (šlo o ověření konceptu) a model ještě není v hlavní větvi.

Post 1woj0is (u/Lexius2129) přináší zrychlení video VAE pro MiniMax H3 od Kijai, s odkazem na blog Comfy; v diskusi se řeší výměna fp16 VAE za int8 a praktický dopad. Post 1wo8oqd (u/roychodraws) je aktualizace V6 workflow pro MiniMax: přidává uzel pro nahrání masky vytvořené jinde, uzel pro tvorbu masky v ComfyUI a ve verzi 6.2 i rozšíření masky; autor přitom opravoval chybu, kvůli které workflow neběželo.

## Proč to je důležité

Flux 3 Action je pozoruhodný tím, co naznačuje o směru, kterým se generativní modely posouvají: z tvorby obrázků a videa do přímého řízení akcí v reálném světě. Model, který ze snímků kamery, stavu robota a textové instrukce vytváří další dávku pohybů společně s predikovanými snímky, stojí na pomezí „světa akcí“ a video generátoru — a diskuse tuhle hranici hned ohmatává otázkou, zda jde zároveň o generátor videa. Otevřené váhy o velikosti 7B navíc znamenají, že si model může vyzkoušet kdokoli s dostatkem paměti, a karta k tomu dodává finetunovací postup pro nová tělesa i simulátory.

Karta sama připomíná, že jde o adaptační komponentu, ne hotovou politiku, a že limity musí vynutit aplikace. Právě proto je zajímavé, že se pod postem mísí nadšení s vtipy o robotech v domácnosti — čím dostupnější takové modely budou, tím víc bude záležet na nastavení hranic provozu.

Sloučené diskuse doplňují obraz rychlosti, jakou se novinky v oboru šíří. Testy Ming Image ukazují, jak rychle se nový model dostane do komunitního nástroje přes pull request, ještě před začleněním do hlavní větve. Zrychlení video VAE u MiniMax H3 je méně nápadná, ale praktická optimalizace, u které se komunita pře o její přínos u krátkých úspor proti dlouhým generacím. Workflow V6 s maskou nabízí jiný přístup k úpravám videa: přesné vymezení oblasti, do které se má postava vložit. Dohromady jde o typický den v r/StableDiffusion — nový model, zrychlení nástrojů a řemeslné workflow v řádu hodin po sobě.

## Zdroje

- Hlavní post: https://www.reddit.com/r/StableDiffusion/comments/1wodsr1/flux_3_action_7b_action_world_model/
- Kolekce modelů: https://huggingface.co/collections/black-forest-labs/flux-3-action
- Oficiální stránka modelu: https://bfl.ai/models/flux-3-action
- Dokumentace: https://docs.bfl.ai/flux_3/flux3_action_overview
- Ming Image v ComfyUI: https://huggingface.co/Kijai/Ming-Image-ComfyUI
- Modely Ming: https://huggingface.co/Comfy-Org/Ming-Image
- Pull request ComfyUI č. 16482: https://github.com/Comfy-Org/ComfyUI/pull/16482
- Blog Comfy o VAE: https://blog.comfy.org/p/making-the-minimax-h3-video-vae-2x
- int8 VAE MiniMax H3: https://huggingface.co/Comfy-Org/MiniMax-H3/blob/main/vae/minimax_h3_video_vae_int8_convrot.safetensors
- Workflow V6: https://github.com/roycho87/minimax_wf
- Související posty: https://www.reddit.com/r/StableDiffusion/comments/1wohtg7/ming_image_is_really_good/, https://www.reddit.com/r/StableDiffusion/comments/1woagyt/graphic_producing_new_model_ming_works_fine_in/, https://www.reddit.com/r/StableDiffusion/comments/1woj0is/making_the_minimax_h3_video_vae_2x_faster/, https://www.reddit.com/r/StableDiffusion/comments/1wo8oqd/v6_update_newbie_modify_a_targeted_area_of_any/
- Podklady: `2026-09-23/_data/bundles/1wodsr1.md`, `2026-09-23/_data/extracts/1wodsr1.json`
