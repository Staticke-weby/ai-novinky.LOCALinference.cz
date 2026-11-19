#!/usr/bin/env bash
# "vytvoř přehledy" / "vytvoř články" / "vytvoř souhrny" = Reddit + HN
# (sběr -> články -> jeden sloučený denní přehled -> web na GitHub Pages -> push) + LinkedIn.
#
# Denní přehled je jeden md pro oba zdroje: stejná témata z Redditu a HN
# sloučí `scripts/build-denni.py` do jedné sekce. LinkedIn pak odkazuje
# jedním odkazem na celý den.
#
# Argumenty se předají oběma běhům `daily.sh` (např. --force, --days,
# --remote, --date). `--publish` se zahazuje – publikuje se jen sloučený den.
#
# Commituje se **jednou na konci** (`push-day.sh`): články z obou zdrojů,
# `dny/` i `docs/`. Dřív se pushovalo po každém zdroji a pak ještě web, takže
# na main šly tři pushe během pár minut a souběžné deploye Pages na sebe
# narážely. `--push` se proto oběma `daily.sh` zahazuje.
#
# Použití:
#   scripts/prehledy.sh                 # Reddit i HN, 1 den zpět, vše jako anotace
#   scripts/prehledy.sh --force         # přepočítat i hotové dny
#   scripts/prehledy.sh --date 2026-10-09
#   FULL_TOP=25 scripts/prehledy.sh     # prvních 25 témat v plném znění (výjimka)
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"
export TZ=Europe/Prague

DATE=""
DAYS=""
DRY=0
ARGS=()
for arg in "$@"; do
  case "$arg" in
    --publish) ;;                       # publikuje se jen sloučený den níže
    --push) ;;                          # pushuje se jednou na konci (push-day.sh)
    *) ARGS+=("$arg") ;;
  esac
done

args=("$@")
i=0
while [[ $i -lt ${#args[@]} ]]; do
  case "${args[$i]}" in
    --date) DATE="${args[$((i + 1))]:-}"; i=$((i + 1)) ;;
    --days) DAYS="${args[$((i + 1))]:-}"; i=$((i + 1)) ;;
    --dry-run) DRY=1 ;;
  esac
  i=$((i + 1))
done
[[ -n "$DATE" ]] || DATE="$(date -d "${DAYS:-1} days ago" +%F)"

FAILED=0

echo "=== Reddit ==="
if [[ $DRY -eq 1 ]]; then
  echo "scripts/daily.sh ${ARGS[*]}"
else
  if ! scripts/daily.sh ${ARGS[@]+"${ARGS[@]}"}; then
    echo "Reddit selhal — pokračuji s tím, co je" >&2
    FAILED=1
  fi
fi

echo "=== Hacker News ==="
if [[ $DRY -eq 1 ]]; then
  echo "scripts/daily.sh --hn ${ARGS[*]}"
else
  if ! scripts/daily.sh --hn ${ARGS[@]+"${ARGS[@]}"}; then
    echo "HN selhalo — pokračuji s tím, co je" >&2
    FAILED=1
  fi
fi

echo
echo "=== Jeden denní přehled (Reddit + HN) ==="
# Kolik témat dát v plném znění; zbytek jsou anotace.
# Výchozí 0 = každé téma jen jako anotace (den ~35 kB). Plné texty jen na výslovné
# přání: FULL_TOP=25 scripts/prehledy.sh
FULL_TOP="${FULL_TOP:-0}"
if [[ $DRY -eq 1 ]]; then
  echo "python3 scripts/build-denni.py $DATE --full-top $FULL_TOP"
  echo "python3 scripts/build-site.py $DATE   # -> docs/"
  echo "scripts/push-day.sh $DATE   # jeden commit + push (články, dny/, docs/)"
  echo "python3 scripts/build-linkedin.py --den $DATE"
  exit 0
fi

DAY_OK=1
if [[ -f "rd/$DATE/00-index.md" || -f "hn/$DATE/00-index.md" ]]; then
  if python3 scripts/build-denni.py "$DATE" --full-top "$FULL_TOP"; then
    # Web (GitHub Pages) — trvalé odkazy místo docs-md, které dokumentům
    # dávalo 7 dní. Generuje se celý archiv z dny/, takže staré dny přežijí.
    if ! python3 scripts/build-site.py "$DATE"; then
      echo "generování webu selhalo (pokračuji)"
      FAILED=1
    fi
  else
    echo "sloučení dne selhalo (pokračuji)"
    DAY_OK=0
    FAILED=1
  fi
else
  echo "chybí index dne $DATE — sloučený přehled se nestaví"
  DAY_OK=0
  FAILED=1
fi

# Jeden commit a push za celý den (i když web selhal, ať se články neztratí).
if [[ $DAY_OK -eq 1 || -f "rd/$DATE/00-index.md" || -f "hn/$DATE/00-index.md" ]]; then
  scripts/push-day.sh "$DATE" || { echo "commit/push dne selhal" >&2; FAILED=1; }
fi

if [[ $DAY_OK -eq 1 ]]; then
  echo
  echo "=== LinkedIn příspěvek ==="
  python3 scripts/build-linkedin.py --den "$DATE" || FAILED=1
fi

exit "$FAILED"
