#!/bin/bash
# Diagnose D1 Stufe 2 (Nachtrag 1), nur Variante F, nach dem Ende aller Testlaeufe der Stufe 2 (Spur cpu3).
R=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 1
until [ "$(cat logs/test-st2-a.log logs/test-st2-b.log logs/test-st2-c.log logs/test-st2-d.log 2>/dev/null | grep -c '^ende ')" -ge 4 ]; do sleep 5; done
bash "$K" cpu3 r19hl3-diag-st2 "$R/code/diag_knoten.py" 2 "$R/aus/prof-st2" "$R/hilfs/zeilen-126.json" "$R/aus/test/test-st2-*.json" "$R/aus/diag/knoten-st2.json" F > "$R/logs/diag-st2.log" 2>&1
