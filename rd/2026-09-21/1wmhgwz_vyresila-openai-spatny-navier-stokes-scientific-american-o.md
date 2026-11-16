# 1wmhgwz

**Vyřešila OpenAI „špatný“ Navier–Stokes? Scientific American o povolené vnější síle a o tom, proč je hlavní problém stále otevřený**

| | |
|---|---|
| Subreddit | r/ArtificialInteligence |
| Autor | — |
| Publikováno (Europe/Prague) | 21. 9. 2026, 18:20 |
| Skóre / komentáře | 27 / 103 |
| Odkaz | https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/ |
| Diskuse | https://www.reddit.com/r/ArtificialInteligence/comments/1wmhgwz/did_openai_solve_the_wrong_navierstokes_problem/ |

## Co se stalo

Scientific American 21. 9. 2026 publikoval analýzu toho, co přesně OpenAI vyřešila u Navier–Stokesova problému. Podle článku je důkaz vygenerovaný interním LLM **formálně způsobilý pro milionovou cenu Clay Mathematics Institute, ale jen díky „kontroverznímu loophole“**: řeší variantu, která povoluje vnější sílu (tzv. variantu C).

Podle citovaných matematiků je ale ten zajímavý problém ten **bez** vnější síly, a ten zůstává nevyřešený. Minulý čtvrtek tři matematici zveřejnili důkaz, že metodu OpenAI nelze na plný (bez-silový) případ rozšířit. Už 7. září dva matematici publikovali blow-up pro frikční (bez třecí) tekutinu a OpenAI dokončila práci za méně než den — z čehož vznikl spor o prioritu a o tom, co vlastně OpenAI „vyřešila“.

Článek uvádí, že původní formulace Clayova problému z roku 2000 od Charlese Feffermana variantu C s vnější silou **výslovně připouští**.

## Klíčová fakulta v bodech

- Cena: 1 milion dolarů (Clay Mathematics Institute); článek: „4 min read“.
- Řešení stojí na variantu C (vnější síla způsobí finite-time blowup), což je konstrukce, která podle matematiků neodpovídá ničemu v reálném světě.
- arXiv důkaz o nerozšířitelnosti na bez-silový případ: https://arxiv.org/html/2609.20803v1
- Oficiální zadání problému (Fefferman, 2000): https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

## Citace

> „Důkaz OpenAI zřejmě splňuje podmínky pro cenu 1 milion dolarů – ale pouze díky využití kontroverzní mezery“ (překlad) — Scientific American (Joseph Howlett)

> „Nejdůležitější problém je nevyřešený.“ (překlad) — Luis Silvestre

> „Všechny kapaliny, které známe, jsou pod vlivem nějaké vnější síly.“ (překlad) — Diego Córdoba

> „Většina ostatních skupin, je pravda, uvažovala konkrétně scénář bez síly.“ (překlad) — Luis Martínez-Zoroa

## Co říkají komentáře

- **Varianta C je legitimní zadání, titulek je zavádějící.** Několik komentujících (u/shumpitostick, u/Cronos988, u/StanleyDodds, u/hattusili-the-third) argumentuje, že pokud je vnější síla součástí oficiální formulace, nemůže jít o „špatný problém“.
- **Patologické protipříklady jsou v matematice norma.** u/mushykindofbrick (skóre 30) a reakce: vyvrácení tvrzení bizarním protipříkladem je rutinní matematická praxe a neznamená to méněcenný výsledek.
- **Bez-silová verze je ta důležitá.** Jiní (u/Dear_Locksmith3379) trvají na tom, že právě nevyřešená verze je ta, o kterou jde fyzikálně.
- **Kritika SciAm.** Několik komentujících považuje článek za věcně chybný („Je smutné vidět, jak moc se Scientific American spletl“, překlad).

## Rozpory a neověřené informace

- **Rozpor:** článek rámuje řešení jako „wrong problem“/loophole, komentáře jako legitimní řešení povolené varianty. Současně platí obojí: je to povolená varianta, ale není to varianta, kterou většina matematiků považuje za hlavní.
- **Neověřené:** tvrzení komentujících, že OpenAI „ukradla“ postup matematikům, nebo že jde o zoufalý krok „na záchranu byznysu“ — jde o spekulace bez doložení.

## Proč to je důležité

Tenhle případ je učebnicový test toho, jak se budou posuzovat „AI vědecké objevy“: formální splnění zadání versus vědecká hodnota výsledku. Pro OpenAI je to PR vítězství s právním krytím (varianta C je povolená), pro matematiky je to ukázka, že benchmarkové „vyřešeno“ se musí číst přesně — a že hodnota je v tom, který problém byl vyřešen, ne že byl vyřešen.

---

*Zdroje: [Scientific American](https://www.scientificamerican.com/article/did-openai-solve-the-wrong-navier-stokes-problem/), [Reddit diskuse](https://www.reddit.com/r/ArtificialInteligence/comments/1wmhgwz/did_openai_solve_the_wrong_navierstokes_problem/).*
