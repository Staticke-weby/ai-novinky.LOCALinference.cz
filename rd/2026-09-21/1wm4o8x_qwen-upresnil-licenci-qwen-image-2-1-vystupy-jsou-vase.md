# 1wm4o8x

**Qwen upřesnil licenci Qwen-Image-2.1: výstupy jsou vaše, model ale nesmíte prodávat ani hostovat**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/Bestlife73 |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 741 / 134 |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wm4o8x/clarification_on_the_qwenimage21_license/ |

## Co se stalo

Po 24 hodinách masivního zájmu o **Qwen-Image-2.1** se Qwen Developers na X pokusili ukončit zmatky kolem licence:

> „Výstupy nejsou součástí licencovaných Materiálů. Uživatelé si ponechávají práva k obrázkům a dalšímu obsahu, který pomocí modelu vygenerují.“ (překlad)

Praktický výklad, na kterém se diskuse shoduje: **vygenerované obrázky můžete používat komerčně** (včetně prodeje), ale **model samotný nesmíte prodávat, bundleovat ani placeně hostovat** bez samostatné licence.

## Klíčová fakta

- Výstupy nejsou součástí „licensed Materials“ → práva k obrázkům zůstávají uživateli.
- Zákaz komerčního poskytování modelu trvá; pro písemné potvrzení Qwen uvádí kontakt **model-business@notice.qwencloud.com**.
- **Problém: soubor LICENSE na Hugging Face nebyl aktualizován**, změnil se jen README. Podle u/Micha0827 sekce 2(b) stále zakazuje komerční „use“ materiálů, nejen servírování modelu.
- Lokální běh: Qwen-Image-2.1 v int8 přes ComfyUI na **16GB RTX 5060 Ti**, špička ~**15,2 GB** VRAM.
- Post má 741 skóre a 134 komentářů.

## Citace

> „Dostali jsme za posledních 24 hodin tolik lásky za Qwen-Image-2.1, děkujeme!! … Takže tady je odpověď:“ (překlad) — Qwen Developers

> „Nemůžete prodávat samotný model, např.: „Kupte si lepší generování obrázků s Qwen Image v mém softwaru!“ Ale můžete použít Qwen Image např. ke generování obrázků pro svůj komerční web“ (překlad) — u/YogurtclosetLimp7351

> „soubor LICENSE na HF nebyl aktualizován, pouze README. Oddíl 2(b) stále zakazuje "užití" Materiálů pro komerční účely, nejen obsluhu modelu.“ (překlad) — u/Micha0827

> „Model můžete **sami** použít k tvorbě obrázků; s těmi obrázky si můžete dělat, co chcete, včetně komerčního využití, prodeje atd.“ (překlad) — u/therealpygon

## Hlavní linky diskuse

- **„Tweet jako právní autorizace?“** Část lidí tvrdí, že vyjádření na X stačí; jiní (a to je bezpečnější čtení) upozorňují, že pro klientskou práci a SaaS je potřeba text v LICENSE a písemné potvrzení.
- **Zmatení z licencí.** Opakovaný dotaz: co smím s Apache-2.0/MIT modelem a co už ne s tímto.
- **Vymahatelnost.** „Téměř dvě třetiny světa tyhle licence vůbec neřeší“ (překlad) vs argument, že pro firmy a SaaS je to zásadní.
- **Kvalita modelu.** Srovnání s Flux, Krea 2 a Klein 9b; část uživatelů hlásí problémy s konzistencí v edit módu, jiní ho označují za nejlepší dostupný image model.

## Rozpory a neověřené informace

- **Rozpor:** šlo o „rug pull“ (u/kabachuha), nebo o dodatečné vysvětlení bez změny licence (u/OneMoreName1)?
- **Rozpor:** stačí tweet jako autorizace, nebo ne?
- Neověřené: tvrzení, že Qwen Image 3.0 bude closed source; subjektivní srovnání kvality s Flux/Krea/Klein; právní výklady komentujících.

## Proč to je důležité

Je to učebnicový případ **licenční nejistoty u open-weight modelů**: schopnosti jsou skvělé, ale komerční použití stojí na výkladu tweetu versus textu licence. Pro firmy, které chtějí Qwen-Image-2.1 použít v produktu, je dnešní stav rizikový — dokud se LICENSE neaktualizuje, právní jistota neexistuje. Zároveň se potvrzuje trend: open image modely se dostaly do kvality, kde je licence hlavní překážka adopce.

---

*Zdroje: [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wm4o8x/clarification_on_the_qwenimage21_license/), screenshot příspěvků @QwenDevs.*
