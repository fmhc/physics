#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-1, einmalige Laufkette (Spur cpu7): L2, L4, L6; danach Marke lauf/kette-cpu7.fertig.
# Jeder Lauf ueber kleintest.sh. Schlusszeit: nach 2026-10-05 10:55:00 UTC (12:55 CEST) startet kein Lauf.
set -u
D=/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1
cd "$D" || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 10:55:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu7 "$name" "$@" > "$D/lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf ksh-L2 code/ksh.py lauf --geo kugel --arm D --N 500,2000,8000 --budget 50,90,300 --seed 12 --out lauf/kugel-D
lauf ksh-L4 code/ksh.py lauf --geo scheibe --arm D --N 500,2000,8000 --budget 50,90,300 --seed 14 --out lauf/scheibe-D
lauf ksh-L6 code/ksh.py btw --N 500,2000,8000 --budget 40,80,300 --seed 16 --out lauf/btw
date -u +%H:%M:%S > "$D/lauf/kette-cpu7.fertig"
echo "kette cpu7 ende $(date -u +%H:%M:%S)"
