#!/usr/bin/env bash
# Commitne vygenerovaný web a pushne ho.
#
# Web se servíruje přímo z tohohle repa: GitHub Pages z větve `main`, složky
# `/docs`, na doméně z `docs/CNAME` (ai-novinky.localinference.cz). Do repa jde
# i `dny/` (zdroj, ze kterého se web staví) a články; stažené podklady
# (`_data/`) jsou v .gitignore, takže je `git add` ignoruje.
#
# Použití:
#   scripts/push-site.sh
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

[[ -f docs/index.html ]] || { echo "chybí docs/index.html — spusť build-site.py" >&2; exit 1; }

git add -A -- docs dny
if git diff --cached --quiet; then
  echo "[web] beze změny"
  exit 0
fi
git commit -q -m "web: $(date +%F)"
branch="$(git rev-parse --abbrev-ref HEAD)"
git push -q origin "HEAD:$branch"
echo "[web] pushnuto na origin/$branch"
