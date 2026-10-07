#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-2, einmalige Laufkette (Spur cpu7): L2, L3, L5, L6; danach Marke lauf/kette-cpu7.fertig.
# Jeder Lauf ueber kleintest.sh. rc != 0: einmal mit demselben Aufruf wiederholt (Name -wdh).
# Schlusszeit: nach 2026-10-05 11:35:00 UTC (13:35 CEST) startet kein Lauf.
set -u
D=/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2
cd "$D" || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 11:35:00' +%s)
mkdir -p "$D/lauf"
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu7 "$name" "$@" > "$D/lauf/$name.log" 2>&1
  local rc=$?
  echo "$name rc=$rc $(date -u +%H:%M:%S)"
  if [ "$rc" -ne 0 ] && [ "$(date -u +%s)" -lt "$SCHLUSS" ]; then
    bash "$K" cpu7 "$name-wdh" "$@" > "$D/lauf/$name-wdh.log" 2>&1
    echo "$name-wdh rc=$? $(date -u +%H:%M:%S)"
  fi
}
lauf ksh2-L2 code/ksh2.py lauf --geo kugel --arm Z --N 8000 --budget 300 --r 0.01 --seed 22 --out lauf/L2
lauf ksh2-L3 code/ksh2.py lauf --geo kugel --arm Z --N 8000 --budget 300 --r 0.003 --seed 23 --out lauf/L3
lauf ksh2-L5 code/ksh2.py lauf --geo kugel --arm Z --N 2000 --budget 90 --r 0.01 --seed 25 --out lauf/L5
lauf ksh2-L6 code/ksh2.py lauf --geo kugel --arm Z --N 2000 --budget 90 --r 0 --seed 26 --out lauf/L6
date -u +%H:%M:%S > "$D/lauf/kette-cpu7.fertig"
echo "kette cpu7 ende $(date -u +%H:%M:%S)"
