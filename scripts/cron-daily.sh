#!/usr/bin/env bash
# Denní běh: celý balík jako „vytvoř souhrny“ – Reddit + HN,
# sloučený den, web na GitHub Pages, push a LinkedIn příspěvek.
#
# Volá ho Orca automation „AI novinky – denní souhrn“ v 6:30 (řídicí agent
# spustí tenhle skript). Zůstává i jako záložní varianta pro cron.
#
# Proč wrapper: cron nespouští přihlašovací shell a nemá session bus.
# Bez `DBUS_SESSION_BUS_ADDRESS` nedosáhne na gnome-keyring, takže by
# `browser_cookies.py` nepřečetl šifrované cookies z Chrome. Tady se
# proměnné doplní a běh se zamkne, aby se nepotkal s ručním spuštěním.
#
# Použití (crontab):
#   30 6 * * * "/home/turany/orca/projects/AI novinky/scripts/cron-daily.sh" >> "/home/turany/orca/projects/AI novinky/logs/cron.log" 2>&1
set -euo pipefail
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

export PATH="$HOME/.local/bin:$PATH"
export TZ=Europe/Prague
export GIT_TERMINAL_PROMPT=0
export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
export DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=$XDG_RUNTIME_DIR/bus}"

mkdir -p logs
exec 8>"logs/.run.lock"
if ! flock -n 8; then
  echo "[$(date -Is)] jiný denní běh už probíhá, přeskakuji"
  exit 3
fi

echo "[$(date -Is)] cron start"
scripts/prehledy.sh "$@" < /dev/null
code=$?
echo "[$(date -Is)] cron konec (exit $code)"
exit "$code"
