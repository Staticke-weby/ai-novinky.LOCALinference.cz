# Denní AI přehled

Denní souhrny AI novinek z Redditu a Hacker News v češtině. Každý den vznikne
jeden přehled: co se stalo, co k tomu říká odkazovaný zdroj a co se řeší
v diskusi.

**Web:** https://ai-novinky.localinference.cz

## Co tu je

- `rd/<datum>/`, `hn/<datum>/` – zdrojové články pro jednotlivé dny a jejich
  indexy (`00-index.md`).
- `dny/<datum>/` – sloučený denní přehled (Reddit + HN); z něj se staví web.
- `docs/` – vygenerovaný web, ze kterého jedou GitHub Pages (`main` / `/docs`).
- `scripts/` – celá pipeline: sběr, psaní, stavba dne, web, LinkedIn.
- `EXPERIENCE.md` – provozní deník: co se osvědčilo a na co si dát pozor.

Stažené podklady (surové dumpy z Redditu, plné texty odkazovaných článků,
převzaté obrázky, překlady a worklisty v `_data/`) v repu nejsou – jsou
v `.gitignore` a dají se kdykoli stáhnout nebo vyrobit znovu.

## Jak to funguje

`scripts/prehledy.sh` udělá celý den: sběr Redditu (`rd-collect-web.py`, cookies
z přihlášeného prohlížeče) a Hacker News (`hn-collect.py`, veřejné API), nechá
agenty OpenCode napsat české články, sloučí oba zdroje do jednoho přehledu
(`build-denni.py`), vygeneruje web (`build-site.py`), commitne a pushne
(`push-site.sh`). Nakonec vypíše příspěvek na LinkedIn (`build-linkedin.py`).

Web se generuje do `docs/` a commituje do tohohle repa; GitHub Pages ho
servírují z `main` / `/docs` na `ai-novinky.localinference.cz` (doména je
v `docs/CNAME`). Staré dny se publikují zpětně, protože `build-site.py` staví
celý archiv z `dny/`.

Denní přehled vychází jako anotace; plné texty jen na vyžádání
(`FULL_TOP=25 scripts/prehledy.sh`).

## Poznámky

Obsah článků vychází z veřejných diskusí na Redditu a Hacker News; odkazy
u každého tématu míří na původní diskusi. Kód slouží k vlastnímu provozu,
ne jako hotový produkt.
