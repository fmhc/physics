#!/bin/bash
# FLUSS-1 Rauchlaeufe (Gittergroesse 6 und Pruefgroessen 1 bis 4, keine echte Groesse), je Spur nacheinander
# ueber kleintest.sh. Spuren cpu3 und cpu4 (hoechstens zwei zugleich).
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde34-fluss/code
D=/home/fmh/fmhc-physics-remote/runde34-fluss/rauch
cd "$D" || exit 1
( bash "$K" cpu3 r34fl-rauch-pruef "$C/fluss_mc.py" pruef "$D/pruef" > "$D/pruef.log" 2>&1
  bash "$K" cpu3 r34fl-rauch-paar6 "$C/fluss_mc.py" paar 6 99 2e8 1e8 4 120 "$D/paar_L6_s99" > "$D/paar_L6_s99.log" 2>&1 ) &
( bash "$K" cpu4 r34fl-rauch-ka6 "$C/fluss_mc.py" korr A 6 99 2000 20 100 120 "$D/korr_A_L6_s99" > "$D/korr_A_L6_s99.log" 2>&1
  bash "$K" cpu4 r34fl-rauch-kb6 "$C/fluss_mc.py" korr B 6 99 200 2 200 90 "$D/korr_B_L6_s99" kette > "$D/korr_B_L6_s99.log" 2>&1
  bash "$K" cpu4 r34fl-rauch-kb6r "$C/fluss_mc.py" korr B 6 98 200 2 200 90 "$D/korr_B_L6_s98" reparatur > "$D/korr_B_L6_s98.log" 2>&1 ) &
wait
echo "rauch fertig $(date --iso-8601=seconds)" > "$D/rauch_fertig.txt"
