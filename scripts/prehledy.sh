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
  [[ "$arg" == "--publish" ]] || ARGS+=("$arg")   # publikuje se jen sloučený den níže
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

echo "=== Reddit ==="
if [[ $DRY -eq 1 ]]; then
  scripts/daily.sh ${ARGS[@]+"${ARGS[@]}"}
else
  scripts/daily.sh --push ${ARGS[@]+"${ARGS[@]}"}
fi

echo "=== Hacker News ==="
if [[ $DRY -eq 1 ]]; then
  scripts/daily.sh --hn ${ARGS[@]+"${ARGS[@]}"}
else
  scripts/daily.sh --hn --push ${ARGS[@]+"${ARGS[@]}"}
fi

echo
echo "=== Jeden denní přehled (Reddit + HN) ==="
# Kolik témat dát v plném znění; zbytek jsou anotace.
# Výchozí 0 = každé téma jen jako anotace (den ~35 kB). Plné texty jen na výslovné
# přání: FULL_TOP=25 scripts/prehledy.sh
FULL_TOP="${FULL_TOP:-0}"
if [[ $DRY -eq 1 ]]; then
  echo "python3 scripts/build-denni.py $DATE --full-top $FULL_TOP"
  echo "python3 scripts/build-site.py $DATE   # -> docs/, push na GitHub Pages"
  echo "python3 scripts/build-linkedin.py --den $DATE"
  exit 0
fi
if [[ -f "rd/$DATE/00-index.md" || -f "hn/$DATE/00-index.md" ]]; then
  python3 scripts/build-denni.py "$DATE" --full-top "$FULL_TOP"
  # Web (GitHub Pages) — trvalé odkazy místo docs-md, které dokumentům
  # dávalo 7 dní. Generuje se celý archiv z dny/, takže staré dny přežijí.
  if python3 scripts/build-site.py "$DATE"; then
    scripts/push-site.sh || echo "push webu selhal (pokračuji)"
  else
    echo "generování webu selhalo (pokračuji)"
  fi
else
  echo "chybí index dne $DATE — sloučený přehled se nestaví"
fi

echo
echo "=== LinkedIn příspěvek ==="
python3 scripts/build-linkedin.py --den "$DATE"
