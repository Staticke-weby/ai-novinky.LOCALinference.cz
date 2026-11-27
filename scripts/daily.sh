#!/usr/bin/env bash
# Denní AI souhrn z Redditu -> <projekt>/rd/<YYYY-MM-DD>/  (--hn -> hn/<YYYY-MM-DD>/)
#
# Použití:
#   scripts/daily.sh                    # Reddit z webu, 1 den zpět (Europe/Prague), přeskočí hotové
#   scripts/daily.sh --hn               # místo Redditu souhrn z Hacker News -> hn/<datum>/
#   scripts/daily.sh --days 2           # posun o N dní zpět (výchozí: 1)
#   scripts/daily.sh --force            # přepočítá i existující den
#   scripts/daily.sh --date 2026-10-01
#   scripts/daily.sh --dry-run          # jen vypíše, co by spustil
#   scripts/daily.sh --push             # po úspěchu commitne daný den a pushne
#   scripts/daily.sh --publish          # po vygenerování publikuje den na docs-md.com
#   scripts/daily.sh --cron             # neinteraktivní režim pro cron (implikuje --push)
#   scripts/daily.sh --remote gitlab    # jiný git remote (výchozí origin)
#
# Reddit data bere `scripts/rd-collect-web.py` přímo z webu (cookies z prohlížeče
# OpenChamber -> reddit .json endpointy); HN bere `scripts/hn-collect.py` z HN API.
# `scripts/rd-collect.py` (archiv Arctic Shift) zůstává jako záložní varianta.
#
# Běží na OpenCode CLI (`opencode run`). Sběr Redditu potřebuje prohlížeč
# OpenChamber s přihlášenou reddit session (cookies), takže pro plný běh musí
# být dostupná sdílená služba OpenCode / OpenChamber.
#
# Cron (denně 6:30) řeší `scripts/cron-daily.sh` (celý balík včetně webu a LinkedIn):
#   30 6 * * * "/home/turany/orca/projects/AI novinky/scripts/cron-daily.sh" >> "…/logs/cron.log" 2>&1
#
# Návratové kódy: 0 ok / přeskočeno, 1 chyba běhu či push, 2 špatné argumenty,
#                 3 jiný běh už probíhá, 4 výsledek neprošel kontrolou před commitem
set -euo pipefail

export TZ=Europe/Prague
export PATH="$HOME/.local/bin:$PATH"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# `opencode` nemusí být v PATH – desktopová appka veze CLI ve verzované složce.
if [[ -z "${OPENCODE_BIN:-}" ]]; then
  if command -v opencode >/dev/null 2>&1; then
    OPENCODE_BIN="opencode"
  else
    OPENCODE_BIN="$(ls -1 "$HOME"/.config/ai.opencode.desktop/cli/*/opencode-cli 2>/dev/null | sort -V | tail -1 || true)"
  fi
fi
OPENCODE_BIN="${OPENCODE_BIN:-opencode}"
MODEL="${OPENCODE_MODEL:-opencode-go/deepseek-v4.1-flash}"
PUSH_REMOTE="${PUSH_REMOTE:-origin}"

DATE=""
DAYS=""
FORCE=0
DRY=0
PUSH="${PUSH:-0}"
PUBLISH="${PUBLISH:-0}"
CRON=0
SOURCE="reddit"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1 ;;
    --dry-run) DRY=1 ;;
    --push) PUSH=1 ;;
    --publish) PUBLISH=1 ;;
    --cron) CRON=1; PUSH=1 ;;
    --hn) SOURCE="hn" ;;
    --days) DAYS="$2"; shift ;;
    --remote) PUSH_REMOTE="$2"; shift ;;
    --date) DATE="$2"; shift ;;
    -h|--help) sed -n '2,24p' "$0"; exit 0 ;;
    *) echo "neznámý argument: $1" >&2; exit 2 ;;
  esac
  shift
done

# Výchozí posun zpět: oba zdroje teď sbírají čerstvě (Reddit z webu, HN z API),
# takže stačí 1 den zpět; web sběr umí i `--days 0` (dnešek).
if [[ -z "$DAYS" ]]; then
  DAYS=1
fi
[[ "$DAYS" =~ ^[0-9]+$ ]] || { echo "špatný počet dní: $DAYS" >&2; exit 2; }
[[ -n "$DATE" ]] || DATE="$(date -d "$DAYS days ago" +%F)"

[[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "špatné datum: $DATE" >&2; exit 2; }
EPOCH_START="$(date -d "$DATE 00:00:00" +%s)"
EPOCH_END="$(( EPOCH_START + 86400 ))"

if [[ "$SOURCE" == "hn" ]]; then
  REL_DIR="hn/$DATE"
  PROMPT_SRC="$PROJECT_DIR/scripts/prompt-hn.md"
  PROMPT_FILE="$PROJECT_DIR/logs/prompt-hn-$DATE.md"
  LOG="$PROJECT_DIR/logs/hn-$DATE.log"
  TITLE="souhrn HN $DATE"
  COMMIT_PREFIX="souhrn HN"
  COLLECT_SCRIPT="hn-collect.py"
  COLLECT_NAME="HN"
  SRC_KEY="hn"
else
  REL_DIR="rd/$DATE"
  PROMPT_SRC="$PROJECT_DIR/scripts/prompt-souhrn.md"
  PROMPT_FILE="$PROJECT_DIR/logs/prompt-$DATE.md"
  LOG="$PROJECT_DIR/logs/$DATE.log"
  TITLE="souhrn $DATE"
  COMMIT_PREFIX="souhrn"
  COLLECT_SCRIPT="rd-collect-web.py"
  COLLECT_NAME="Reddit (web)"
  SRC_KEY="rd"
fi
OUT_DIR="$PROJECT_DIR/$REL_DIR"
RECENT_FILE="$PROJECT_DIR/logs/recent-$DATE-$SRC_KEY.md"
mkdir -p "$PROJECT_DIR/logs"

# Commitne složku daného dne (REL_DIR) a pushne ji. 0 = ok, 1 = chyba, 4 = neprošlo kontrolou.
push_day() {
  local rel="$1" out="$2" n branch word
  if [[ ! -f "$out/00-index.md" ]]; then
    echo "[$rel] chybí 00-index.md — nepushuji" | tee -a "$LOG"; return 4
  fi
  n="$(find "$out" -maxdepth 1 -name '*.md' ! -name '00-index.md' ! -name 'prehled.md' | wc -l)"
  if [[ "$n" -lt 1 ]]; then
    echo "[$rel] žádné články — nepushuji" | tee -a "$LOG"; return 4
  fi
  case "$n" in
    1) word="článek" ;;
    2|3|4) word="články" ;;
    *) word="článků" ;;
  esac
  cd "$PROJECT_DIR"
  if [[ -z "$(git status --porcelain -- "$rel")" ]]; then
    echo "[$rel] v gitu není co commitnout" | tee -a "$LOG"
  else
    git add -- "$rel"
    git commit -q -m "$COMMIT_PREFIX $DATE: $n $word" | tee -a "$LOG"
    echo "[$rel] commitnuto ($n $word)" | tee -a "$LOG"
  fi
  branch="$(git rev-parse --abbrev-ref HEAD)"
  if git push "$PUSH_REMOTE" "HEAD:$branch" 2>&1 | tee -a "$LOG"; then
    echo "[$rel] pushnuto na $PUSH_REMOTE/$branch" | tee -a "$LOG"; return 0
  fi
  echo "[$rel] push na $PUSH_REMOTE selhal" | tee -a "$LOG"; return 1
}

if [[ $CRON -eq 1 ]]; then
  export GIT_TERMINAL_PROMPT=0
  exec </dev/null
fi

if [[ -f "$OUT_DIR/00-index.md" && $FORCE -eq 0 ]]; then
  echo "[$REL_DIR] už hotovo ($OUT_DIR/00-index.md), použíj --force pro přepočet"
  if [[ $PUSH -eq 1 ]]; then push_day "$REL_DIR" "$OUT_DIR" || exit $?; fi
  exit 0
fi

# --force přepočítá i existující den: starou složku smaž, ať v _data nezůstanou
# obrázky, balíčky a články z předchozího běhu.
if [[ $FORCE -eq 1 && "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ && -d "$OUT_DIR" ]]; then
  rm -rf "${OUT_DIR:?}"
  echo "[$REL_DIR] --force: smazána stará složka $OUT_DIR" | tee -a "$LOG"
fi

# Seznam toho, co už vyšlo v posledních 3 dnech (Reddit i HN). U HN navíc
# dnešní Reddit, aby se stejné téma sloučilo, ne aby se psalo dvakrát.
if ! python3 "$PROJECT_DIR/scripts/recent-topics.py" "$DATE" --source "$SRC_KEY" > "$RECENT_FILE" 2>>"$LOG"; then
  echo "()" > "$RECENT_FILE"
  echo "[$REL_DIR] seznam už vyšlých témat se nepodařilo sestavit (pokračuji)" | tee -a "$LOG"
fi

sed -e "s/__DATE__/$DATE/g" -e "s/__EPOCH_START__/$EPOCH_START/g" -e "s/__EPOCH_END__/$EPOCH_END/g" \
  -e "s|__RECENT__|$RECENT_FILE|g" \
  "$PROMPT_SRC" > "$PROMPT_FILE"

if [[ $DRY -eq 1 ]]; then
  echo "datum: $DATE  zdroj: $SOURCE  okno: $EPOCH_START..$EPOCH_END  složka: $OUT_DIR"
  echo "model: $MODEL  prompt: $PROMPT_FILE  push: $PUSH (remote $PUSH_REMOTE)"
  echo "seznam už vyšlých témat: $RECENT_FILE"
  echo "nejdřív bych spustil: python3 scripts/$COLLECT_SCRIPT $DATE"
  [[ $PUBLISH -eq 1 ]] && echo "po generování bych publikoval: python3 scripts/publish-docs.py $REL_DIR"
  echo "spustil bych (v $PROJECT_DIR): $OPENCODE_BIN run --auto --model '$MODEL' --title '$TITLE' \"\$(cat '$PROMPT_FILE')\""
  exit 0
fi

mkdir -p "$OUT_DIR/_data/bundles" "$OUT_DIR/_data/extracts" "$OUT_DIR/_data/img"
exec 9>"$PROJECT_DIR/logs/.lock"
if ! flock -n 9; then echo "jiný běh už probíhá (logs/.lock), končím"; exit 3; fi
echo "[$(date -Is)] start $REL_DIR -> $OUT_DIR" | tee -a "$LOG"

# Sběr dat před agentem: Reddit přes web (cookies z profilu OpenChamber, netřeba
# otevřený prohlížeč), HN přes veřejné API.
# Když sběr selže nebo vrátí málo postů (výpadek archivu / vypršená session),
# den se přeskočí — agent se vůbec nespustí, ať nevznikne prázdný/rozbitý souhrn.
set +e
python3 "$PROJECT_DIR/scripts/$COLLECT_SCRIPT" "$DATE" 2>&1 | tee -a "$LOG"
COLLECT_CODE=${PIPESTATUS[0]}
set -e
if [[ "$COLLECT_CODE" -ne 0 ]]; then
  if [[ "$COLLECT_CODE" -eq 5 ]]; then
    echo "[$REL_DIR] reddit session vypršela — otevři reddit v prohlížeči OpenChamber a spusť znovu" | tee -a "$LOG"
  fi
  echo "[$REL_DIR] sběr $COLLECT_NAME nepřinesl data — den přeskočen, končím" | tee -a "$LOG"
  exit "$COLLECT_CODE"
fi

( cd "$PROJECT_DIR" && "$OPENCODE_BIN" run --auto --model "$MODEL" --title "$TITLE" "$(cat "$PROMPT_FILE")" ) 2>&1 | tee -a "$LOG"
echo "[$(date -Is)] hotovo $REL_DIR" | tee -a "$LOG"

# Kontrola, že se do dne nevrátila témata z posledních 3 dnů. Jen varování:
# jeden falešný zásah nesmí zahodit celý den.
set +e
python3 "$PROJECT_DIR/scripts/recent-topics.py" "$DATE" --source "$SRC_KEY" --check 2>&1 | tee -a "$LOG"
RECENT_CODE=${PIPESTATUS[0]}
set -e
if [[ "$RECENT_CODE" -ne 0 ]]; then
  echo "[$REL_DIR] VAROVÁNÍ: v přehledu zůstala témata z posledních dnů (viz výše)" | tee -a "$LOG"
fi

# Publikace dne na docs-md.com (jeden post z článků). Selhání jen zapíšeme.
if [[ $PUBLISH -eq 1 ]]; then
  echo "[$(date -Is)] publikuji $REL_DIR na docs-md.com" | tee -a "$LOG"
  if ( cd "$PROJECT_DIR" && python3 scripts/publish-docs.py "$REL_DIR" ) 2>&1 | tee -a "$LOG"; then
    echo "[$(date -Is)] publikováno $REL_DIR" | tee -a "$LOG"
  else
    echo "[$(date -Is)] publikace selhala (pokračuji)" | tee -a "$LOG"
  fi
fi

if [[ $PUSH -eq 1 ]]; then
  push_day "$REL_DIR" "$OUT_DIR" || exit $?
fi
