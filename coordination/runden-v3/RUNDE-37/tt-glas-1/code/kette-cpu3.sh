#!/bin/bash
# TT-GLAS-1, einmalige Laufkette Spur cpu3 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 03:45:00 UTC (05:45 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 03:45:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu3 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tg-ko code/tg.py kontrolle --out lauf/kontrolle.json
lauf tg-n32 code/tg.py netz --N 32 --saaten 1,2,3,4,5,6,7,8,9,10,11,12 --out lauf/netz
lauf tg-n64 code/tg.py netz --N 64 --saaten 1,2,3,4,5,6,7,8,9,10,11,12 --out lauf/netz
lauf tg-n128a code/tg.py netz --N 128 --saaten 1,2,3,4,5,6 --out lauf/netz
for s in 1 3 5 7 9 11; do
  lauf tg-n256-s$s code/tg.py netz --N 256 --saaten $s --out lauf/netz-N256-s$s.json
done
echo "kette cpu3 ende $(date -u +%H:%M:%S)"
