#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-1, einmalige Laufkette (Spur cpu): L1, L3, L5, dann AUS (wartet auf das Ende der Kette cpu7).
# Jeder Lauf ueber kleintest.sh. Schlusszeit: nach 2026-10-05 10:55:00 UTC (12:55 CEST) startet kein Lauf.
set -u
D=/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1
cd "$D" || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 10:55:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu "$name" "$@" > "$D/lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf ksh-L1 code/ksh.py lauf --geo kugel --arm Z --N 500,2000,8000 --budget 50,90,300 --seed 11 --out lauf/kugel-Z
lauf ksh-L3 code/ksh.py lauf --geo scheibe --arm Z --N 500,2000,8000 --budget 50,90,300 --seed 13 --out lauf/scheibe-Z
lauf ksh-L5 code/ksh.py lauf --geo scheibe --arm Z --N 2000 --budget 150 --r 0.01,0.1 --seed 15 --out lauf/rate
for i in $(seq 1 240); do
  [ -e "$D/lauf/kette-cpu7.fertig" ] && break
  sleep 5
done
lauf ksh-AUS code/ksh.py aus --ein lauf/kugel-Z.json lauf/kugel-D.json lauf/scheibe-Z.json lauf/scheibe-D.json lauf/btw.json lauf/rate.json --out aus/urteile.json --bild aus
echo "kette cpu ende $(date -u +%H:%M:%S)"
