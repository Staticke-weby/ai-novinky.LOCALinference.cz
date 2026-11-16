# 1wmg1pb

**Supra2-IMG: 100M text-to-image model trénovaný 10 hodin na jedné H100 — „SOTA“ jen v rámci své velikosti**

| | |
|---|---|
| Subreddit | r/StableDiffusion |
| Autor | u/LH-Tech_AI |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 437 / 276 |
| Diskuse | https://www.reddit.com/r/StableDiffusion/comments/1wmg1pb/massive_release_supra2img_a_tiny_100m/ |

## Co se stalo

SupraLabs zveřejnili **Supra2-IMG** — **100M parametrů velký DiT text-to-image model**, trénovaný **od nuly za méně než 10 hodin na jedné H100** (Runpod). Generuje obrázky **256×256 px**; autoři tvrdí, že vzorky **nejsou cherry-picked** (seed 0, steps 50, cfg 3.0 pro každý obrázek). Lokální inference přes `inference.py` na Hugging Face: **~20 s na obrázek na CPU, ~2 s na GPU**.

Vlákno se okamžitě rozdělilo na dva tábory: nadšení z kvality na velikost vs kritika titulku „[MASSIVE RELEASE]“ a nepodloženého slova „SOTA“.

## Čísla

- 100M parametrů, <10 hodin tréninku, 1× H100.
- 256×256 px, seed 0 / steps 50 / cfg 3.0.
- ~20 s/obrázek (CPU), ~2 s/obrázek (GPU).
- Diskuse: 437 skóre, 276 komentářů (143 v balíčku).
- Komentující uvádějí srovnatelné malé modely: **IRIS** (10,3M/40M/53,4M, Apache-2.0), **MicroForge Tiny** (28M), **transformer_latent_diffusion** (~100M, MIT).

## Citace

> „Je to 100M parametrový DiT text-to-image model trénovaný zcela od nuly za méně než 10 hodin na jediné H100 na Runpod.“ (překlad) — OP

> „Tyto vzorky NEJSOU třešničkově vybírané! Sampling: seed 0, steps 50, cfg 3.0; stejné nastavení pro každý obrázek.“ (překlad) — OP

> „"SOTA" je myšleno pro velikost 100M parametrů, lidi!“ (překlad) — OP (reakce na kritiku)

> „Je to pěkný úspěch? Ano. Je to [MASSIVE RELEASE]? Ne. Je to kvalita nejvyšší úrovně? Ani zdaleka.“ (překlad) — u/mcmonkey4eva

> „nechápu, proč jsou tu lidi tak natvrdlí a nechápou pointu – SOTA pro tu velikost. Máte podobný model téhle velikosti s touhle kvalitou? Ne? Tak tohle je sota. Tečka.“ (překlad) — u/LimTimLmao

## Hlavní linky diskuse

- **„Pro 100M je to úžasné.“** Většina vysokých skóre oceňuje, že model poběží i na telefonu a má smysl pro specializované úlohy (avatary, přání, textury do her, experimenty s pre-trainingem).
- **Nadpis a „SOTA“ přestřelily.** Kritici (u/mcmonkey4eva, u/nowrebooting) namítají, že absolutní kvalita je daleko od SOTA a že u 100M velikosti není relevantní konkurence.
- **Existují alternativy.** Jeden komentující vypočítává tři obdobně velké modely; jiný tvrdí, že kvalita odpovídá SD 1.4–1.5 při ~1/7 velikosti.
- **Limit 256 px** je zmiňován jako hlavní omezení pro praktické použití.

## Rozpory a neověřené informace

- **Rozpor:** je „SOTA“ férové tvrzení (relativně k velikosti) vs nepodložený hype.
- **Rozpor:** existují konkurenční ~100M text-to-image modely, nebo ne?
- **Neověřené:** tvrzení, že vzorky nejsou vybírané; srovnání se SD 1.4/1.5; seznam alternativ od komentujícího.

## Proč to je důležité

Supra2-IMG je datový bod k **„small-model“ trendu**: trénink od nuly za jednu GPU desítky hodin už dává použitelné 256px obrázky. To je relevantní pro on-device generování a pro výzkum (rychlá iterace nad architekturami). Zároveň je to učebnicový případ toho, jak si projekt podkope důvěryhodnost přehnaným titulkem — kvalitní inženýrský výsledek se ztratil v hádce o slovo „SOTA“.

---

*Zdroj: [Reddit diskuse](https://www.reddit.com/r/StableDiffusion/comments/1wmg1pb/massive_release_supra2img_a_tiny_100m/).*
