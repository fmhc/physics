#!/bin/bash
# FLUSS-1 Rauchlaeufe Teil 2 (Gittergroesse 10, keine echte), nach Einfuehrung der Ringform.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde34-fluss/code
D=/home/fmh/fmhc-physics-remote/runde34-fluss/rauch
cd "$D" || exit 1
( bash "$K" cpu3 r34fl-rauch-ka10 "$C/fluss_mc.py" korr A 10 97 4000 20 150 150 "$D/korr_A_L10_s97" > "$D/korr_A_L10_s97.log" 2>&1 ) &
( bash "$K" cpu4 r34fl-rauch-kb10 "$C/fluss_mc.py" korr B 10 97 500 2 650 100 "$D/korr_B_L10_s97" kette > "$D/korr_B_L10_s97.log" 2>&1 ) &
wait
bash "$K" cpu3 r34fl-rauch-ausw2 "$C/auswertung.py" "$D" "$D/auswertung2.json" 10 6 > "$D/auswertung2.log" 2>&1
echo "rauch2 fertig $(date --iso-8601=seconds)" > "$D/rauch2_fertig.txt"
