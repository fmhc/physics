#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-2, einmalige Laufkette (Spur cpu): L1, L4, L7, dann AUS (wartet auf die Marke der Kette cpu7).
# Jeder Lauf ueber kleintest.sh. rc != 0: einmal mit demselben Aufruf wiederholt (Name -wdh).
# Schlusszeit: nach 2026-10-05 11:35:00 UTC (13:35 CEST) startet kein Lauf; AUS spaetestens 11:50:00 UTC.
set -u
D=/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2
cd "$D" || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 11:35:00' +%s)
SCHLUSS_AUS=$(date -u -d '2026-10-05 11:50:00' +%s)
mkdir -p "$D/lauf" "$D/aus"
lauf() {
  local grenze=$1 name=$2; shift 2
  if [ "$(date -u +%s)" -ge "$grenze" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu "$name" "$@" > "$D/lauf/$name.log" 2>&1
  local rc=$?
  echo "$name rc=$rc $(date -u +%H:%M:%S)"
  if [ "$rc" -ne 0 ] && [ "$(date -u +%s)" -lt "$grenze" ]; then
    bash "$K" cpu "$name-wdh" "$@" > "$D/lauf/$name-wdh.log" 2>&1
    echo "$name-wdh rc=$? $(date -u +%H:%M:%S)"
  fi
}
lauf "$SCHLUSS" ksh2-L1 code/ksh2.py lauf --geo kugel --arm Z --N 16000 --budget 520 --r 0.01 --seed 21 --out lauf/L1
lauf "$SCHLUSS" ksh2-L4 code/ksh2.py lauf --geo kugel --arm Z --N 8000 --budget 300 --r 0.03 --seed 24 --out lauf/L4
lauf "$SCHLUSS" ksh2-L7 code/ksh2.py lauf --geo kugel --arm Z --N 2000 --budget 60 --r 0 --seed 11 --out lauf/L7
for i in $(seq 1 240); do
  [ -e "$D/lauf/kette-cpu7.fertig" ] && break
  sleep 5
done
lauf "$SCHLUSS_AUS" ksh2-AUS code/ksh2.py aus2 --ks0 lauf/L6.json --kid lauf/L7.json --ref /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1/lauf/kugel-Z.json --r001 lauf/L5.json lauf/L2.json lauf/L1.json --r0003 lauf/L3.json --r003 lauf/L4.json --out aus/urteile.json --bild aus
echo "kette cpu ende $(date -u +%H:%M:%S)"
