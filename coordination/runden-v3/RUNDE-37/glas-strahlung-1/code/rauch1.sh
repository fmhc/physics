#!/bin/bash
# GLAS-STRAHLUNG-1 Rauchtest 1 (vor dem Einfrieren): Absturzproben mit Rauchsaaten 901, 902 und grobem Richtungsgitter
# (nt 2, nphi 4). Gelesen werden nur Rueckgabewerte, Laufzeiten, Speicher und Schluessel, keine Werte.
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=code-r1/gs.py
( bash $K cpu gs-r1 $C netz --N 0 --nt 2 --nphi 4 --out rauch/r1-v.json > rauch/r1.log 2>&1; echo "r1 rc=$? $(date -u +%H:%M:%S)"
  bash $K cpu gs-r2 $C netz --N 128 --saaten 901,902 --nt 2 --nphi 4 --out rauch/r2 > rauch/r2.log 2>&1; echo "r2 rc=$? $(date -u +%H:%M:%S)" ) &
( bash $K p4000a gs-r3 $C netz --N 512 --saaten 901 --nt 2 --nphi 4 --out rauch/r3 > rauch/r3.log 2>&1; echo "r3 rc=$? $(date -u +%H:%M:%S)" ) &
( bash $K p4000b gs-r4 $C netz --N 256 --saaten 901 --nt 2 --nphi 4 --out rauch/r4 > rauch/r4.log 2>&1; echo "r4 rc=$? $(date -u +%H:%M:%S)" ) &
wait
bash $K cpu gs-r5 $C aus --v rauch/r1-v.json --ein rauch/r2-N128-s901.json rauch/r2-N128-s902.json rauch/r3-N512-s901.json rauch/r4-N256-s901.json --out rauch/r5.json --bild rauch/r5.png > rauch/r5.log 2>&1; echo "r5 rc=$? $(date -u +%H:%M:%S)"
