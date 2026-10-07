#!/bin/bash
# FLUSS-1 (Runde 34): echte Laeufe nach PLAN.md Abschnitt 4, je Spur nacheinander ueber kleintest.sh (Spuren cpu3, cpu4).
# Aufruf auf der .69 aus /home/fmh/fmhc-physics-remote/runde34-fluss/lauf: bash ../code/laeufe.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde34-fluss/code
D=/home/fmh/fmhc-physics-remote/runde34-fluss/lauf
cd "$D" || exit 1

paar() {  # spur L seed zeitgrenze
  bash "$K" "$1" "r34fl-paar$2s$3" "$C/fluss_mc.py" paar "$2" "$3" 2e9 5e8 4 "$4" "$D/paar_L$2_s$3" > "$D/paar_L$2_s$3.log" 2>&1
}
korr() {  # spur netz L seed einlauf je_messung messungen_je_block zeitgrenze [start]
  bash "$K" "$1" "r34fl-k$2$3s$4" "$C/fluss_mc.py" korr "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$D/korr_$2_L$3_s$4" ${9:-} > "$D/korr_$2_L$3_s$4.log" 2>&1
}

( paar cpu3 12 1 540; paar cpu3 12 2 540; paar cpu3 8 1 420; korr cpu3 B 12 2 2000 2 2000 480 reparatur ) &
( korr cpu4 A 12 1 20000 20 280 540; korr cpu4 A 8 1 20000 20 900 480; korr cpu4 B 12 1 2000 2 2000 480 kette
  korr cpu4 B 8 1 2000 2 3000 300 kette ) &
wait
echo "laeufe fertig $(date --iso-8601=seconds)" > "$D/laeufe_fertig.txt"
bash "$K" cpu3 r34fl-auswertung "$C/auswertung.py" "$D" "$D/auswertung.json" 12 8 > "$D/auswertung.log" 2>&1
echo "auswertung fertig $(date --iso-8601=seconds)" >> "$D/laeufe_fertig.txt"
