#!/bin/bash
# TT-GLAS-1, einmalige Laufkette Spur cpu4 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 03:45:00 UTC (05:45 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 03:45:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu4 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tg-af code/tg.py affin --N 256 --saaten 1,2 --out lauf/affin
lauf tg-af2000 code/tg.py affin --N 2000 --saaten 1,2 --out lauf/affin
lauf tg-af8000 code/tg.py affin --N 8000 --saaten 1,2 --out lauf/affin
lauf tg-n128b code/tg.py netz --N 128 --saaten 7,8,9,10,11,12 --out lauf/netz
for s in 2 4 6 8 10 12; do
  lauf tg-n256-s$s code/tg.py netz --N 256 --saaten $s --out lauf/netz-N256-s$s.json
done
echo "kette cpu4 ende $(date -u +%H:%M:%S)"
