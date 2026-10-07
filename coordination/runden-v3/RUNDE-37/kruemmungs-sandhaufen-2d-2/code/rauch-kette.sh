#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-2, Rauchtests (vor dem Einfrieren; je <= 120 s). Gelesen werden nur rc, Laufzeiten,
# Schluessel und fuer N_max die Schrittzahlen und Zeiten von Einschwingen und Messung (PLAN 11).
# Aufruf: bash rauch-kette.sh cpu|cpu7
set -u
D=/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-2
cd "$D" || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=code-r1/ksh2.py
mkdir -p "$D/rauch"
lauf() {
  local spur=$1 name=$2; shift 2
  bash "$K" "$spur" "$name" "$@" > "$D/rauch/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
case "$1" in
  cpu)
    lauf cpu ksh2-R1 $C lauf --geo kugel --arm Z --N 16000 --budget 100 --r 0.01 --seed 91 --out rauch/R1 --rauch
    lauf cpu ksh2-R3 $C lauf --geo kugel --arm Z --N 32000 --budget 100 --r 0.01 --seed 93 --out rauch/R3 --rauch
    for i in $(seq 1 120); do
      [ -e "$D/rauch/kette-cpu7.fertig" ] && break
      sleep 5
    done
    lauf cpu ksh2-R10 $C aus2 --ks0 rauch/R4.json --kid rauch/R5.json --ref /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1/lauf/kugel-Z.json --r001 rauch/R6.json rauch/R7.json rauch/R1.json --r0003 rauch/R8.json --r003 rauch/R9.json --out rauch/aus/urteile.json --bild rauch/aus --rauch
    ;;
  cpu7)
    lauf cpu7 ksh2-R2 $C lauf --geo kugel --arm Z --N 24000 --budget 100 --r 0.01 --seed 92 --out rauch/R2 --rauch
    lauf cpu7 ksh2-R4 $C lauf --geo kugel --arm Z --N 2000 --budget 10 --r 0 --seed 94 --out rauch/R4 --rauch
    lauf cpu7 ksh2-R5 $C lauf --geo kugel --arm Z --N 2000 --budget 20 --r 0 --seed 11 --out rauch/R5 --rauch
    lauf cpu7 ksh2-R6 $C lauf --geo kugel --arm Z --N 2000 --budget 10 --r 0.01 --seed 96 --out rauch/R6 --rauch
    lauf cpu7 ksh2-R7 $C lauf --geo kugel --arm Z --N 8000 --budget 15 --r 0.01 --seed 97 --out rauch/R7 --rauch
    lauf cpu7 ksh2-R8 $C lauf --geo kugel --arm Z --N 8000 --budget 15 --r 0.003 --seed 98 --out rauch/R8 --rauch
    lauf cpu7 ksh2-R9 $C lauf --geo kugel --arm Z --N 8000 --budget 15 --r 0.03 --seed 99 --out rauch/R9 --rauch
    date -u +%H:%M:%S > "$D/rauch/kette-cpu7.fertig"
    ;;
esac
echo "kette $1 ende $(date -u +%H:%M:%S)"
