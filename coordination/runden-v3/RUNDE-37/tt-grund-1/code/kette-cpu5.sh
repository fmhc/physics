#!/bin/bash
# TT-GRUND-1, einmalige Laufliste Spur cpu5 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh.
# Kein neuer Lauf ab SCHLUSS = 2026-10-04 23:45:00 CEST (21:45:00 UTC).
set -u
SCHLUSS=$(date -d '2026-10-04 21:45:00 UTC' +%s)
D=/home/fmh/fmhc-physics-remote/tt-grund-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$D/code" || exit 1
lauf() {
  local n=$1; shift
  if [ "$(date +%s)" -ge "$SCHLUSS" ]; then echo "SCHLUSS vor $n $(date -u +%FT%TZ)" >> "$D/lauf/kette-cpu5.log"; return 1; fi
  echo "start $n $(date -u +%FT%TZ)" >> "$D/lauf/kette-cpu5.log"
  bash "$K" cpu5 "tg$n" "$D/code/tg.py" "$@" > "$D/lauf/tg$n.log" 2>&1
  echo "ende $n rc=$? $(date -u +%FT%TZ)" >> "$D/lauf/kette-cpu5.log"
}
lauf K kontrolle --out "$D/lauf/kontrolle.json"
lauf R regeln --out "$D/lauf/regeln.json"
lauf KV karte --netz V --npkt 161 --gitter_alt "$D/ref/gitter-V-A1R1.json" --out "$D/lauf/karte-V.json"
lauf KS karte --netz S --npkt 81 --out "$D/lauf/karte-S.json"
echo "kette fertig $(date -u +%FT%TZ)" >> "$D/lauf/kette-cpu5.log"
