#!/bin/bash
# TT-GLAS-2, einmalige Laufkette C, Spur cpu6 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (<= 600 s).
# Schlusszeit: nach 2026-10-05 06:50:00 UTC (08:50 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 06:50:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu6 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
for s in 1 2 3 4 5 6 7 8 9 10 11 12; do
  lauf tg2-bz128-s$s code/bz.py --N 128 --saat $s --out lauf/bz-N128-s$s.json
done
lauf tg2-dk128-a code/dk.py --N 128 --saaten 1,2,3,4,5,6 --out lauf/dk
lauf tg2-dk128-b code/dk.py --N 128 --saaten 7,8,9,10,11,12 --out lauf/dk
echo "kette C ende $(date -u +%H:%M:%S)"
