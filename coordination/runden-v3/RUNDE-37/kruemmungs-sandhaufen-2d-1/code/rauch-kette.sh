#!/bin/bash
# KRUEMMUNGS-SANDHAUFEN-2D-1, Rauchtests (vor dem Einfrieren). Gelesen werden nur rc, Laufzeiten und Schluessel.
# Aufruf: bash rauch-kette.sh cpu|cpu7|aus
set -u
cd /home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=code-r1/ksh.py
lauf() {
  local spur=$1 name=$2; shift 2
  bash "$K" "$spur" "$name" "$@" > "/home/fmh/fmhc-physics-remote/kruemmungs-sandhaufen-2d-1/rauch/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
case "$1" in
  cpu)
    lauf cpu ksh-r1 $C lauf --geo kugel --arm Z --N 500,2000,8000 --budget 2,2,4 --seed 91 --out rauch/kugel-Z --rauch
    lauf cpu ksh-r2 $C lauf --geo scheibe --arm Z --N 500,2000,8000 --budget 2,2,4 --seed 93 --out rauch/scheibe-Z --rauch
    lauf cpu ksh-r3 $C lauf --geo scheibe --arm Z --N 2000 --budget 2 --r 0.01,0.1 --seed 95 --out rauch/rate --rauch
    ;;
  cpu7)
    lauf cpu7 ksh-r4 $C lauf --geo kugel --arm D --N 500,2000,8000 --budget 2,2,4 --seed 92 --out rauch/kugel-D --rauch
    lauf cpu7 ksh-r5 $C lauf --geo scheibe --arm D --N 500,2000,8000 --budget 2,2,4 --seed 94 --out rauch/scheibe-D --rauch
    lauf cpu7 ksh-r6 $C btw --N 500,2000,8000 --budget 2,2,4 --seed 96 --out rauch/btw --rauch
    ;;
  aus)
    lauf cpu ksh-r7 $C aus --ein rauch/kugel-Z.json rauch/kugel-D.json rauch/scheibe-Z.json rauch/scheibe-D.json rauch/btw.json rauch/rate.json --out rauch/aus/urteile.json --bild rauch/aus --rauch
    ;;
esac
echo "kette $1 ende $(date -u +%H:%M:%S)"
