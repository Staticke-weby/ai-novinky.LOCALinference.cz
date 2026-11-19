#!/usr/bin/env bash
# Commitne celý den jedním commitem a pushne: články z Redditu i HN,
# sloučený přehled (`dny/`) a vygenerovaný web (`docs/`).
#
# Proč jeden commit: `prehledy.sh` dřív pouštěl `daily.sh --push` po každém
# zdroji a pak ještě `push-site.sh`, takže na main šly tři pushe během pár
# minut. Každý spustil workflow Pages a souběžné deploye na sebe narážely
# (`Deployment request failed … due to in progress deployment`).
#
# Použití:
#   scripts/push-day.sh 2026-11-18
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

DATE="${1:-}"
[[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "použití: $0 <YYYY-MM-DD>" >&2; exit 2; }

[[ -f docs/index.html ]] || { echo "chybí docs/index.html — spusť build-site.py" >&2; exit 1; }

# Do commitu jde jen tenhle den (a web, který se staví z celého archivu).
# `_data/` je v .gitignore, takže podklady zůstanou mimo repo.
git add -A -- "rd/$DATE" "hn/$DATE" "dny/$DATE" docs
if git diff --cached --quiet; then
  echo "[den] beze změny"
  exit 0
fi

count() { # počet článků ve složce zdroje (bez indexu a přehledu)
  local dir="$1"
  [[ -f "$dir/00-index.md" ]] || { echo 0; return; }
  find "$dir" -maxdepth 1 -name '*.md' ! -name '00-index.md' ! -name 'prehled.md' | wc -l
}
RD="$(count "rd/$DATE")"
HN="$(count "hn/$DATE")"
if [[ "$RD" -gt 0 && "$HN" -gt 0 ]]; then
  MSG="souhrn $DATE: $RD + $HN článků, web"
elif [[ "$RD" -gt 0 ]]; then
  MSG="souhrn $DATE: $RD článků, web"
elif [[ "$HN" -gt 0 ]]; then
  MSG="souhrn HN $DATE: $HN článků, web"
else
  MSG="web: $DATE"
fi

git commit -q -m "$MSG"
branch="$(git rev-parse --abbrev-ref HEAD)"
if ! git push origin "HEAD:$branch"; then
  echo "[den] push na origin/$branch selhal" >&2
  exit 1
fi
echo "[den] commitnuto a pushnuto na origin/$branch: $MSG"
