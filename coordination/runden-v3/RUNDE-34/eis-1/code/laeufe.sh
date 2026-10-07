#!/bin/bash
# EIS-1 (Runde 34): echte Laeufe nach PLAN.md Abschnitte 2 und 6, je Spur nacheinander ueber kleintest.sh.
# Aufruf auf der .69 aus /home/fmh/fmhc-physics-remote/runde34-eis/lauf: bash ../code/laeufe.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde34-eis/code
D=/home/fmh/fmhc-physics-remote/runde34-eis/lauf
cd "$D" || exit 1

eis() {  # spur L seed
  bash "$K" "$1" "r34eis-eis$2s$3" "$C/eis_mc.py" "$2" "$3" 2e9 5e8 4 540 "$D/eis_L$2_s$3" > "$D/eis_L$2_s$3.log" 2>&1
}
stab() {  # spur netz L
  bash "$K" "$1" "r34eis-$2$3" "$C/stabnetz.py" antwort "$2" "$3" "$D/stab_$2_L$3.json" > "$D/stab_$2_L$3.log" 2>&1
}
zaehl() {  # spur netz Ls methode
  bash "$K" "$1" "r34eis-z$2$4" "$C/stabnetz.py" zaehlen "$2" "$3" "$4" "$D/zaehl_$2_$4.json" > "$D/zaehl_$2_$4.log" 2>&1
}

( eis cpu 12 1; eis cpu 12 2; eis cpu 12 3 ) &
( stab cpu2 pyro 12; stab cpu2 pyro 8; stab cpu2 fcc 12; stab cpu2 fcc 8
  zaehl cpu2 pyro 3,4,5 dicht; zaehl cpu2 pyro 3,4,5,8,12 bloch; zaehl cpu2 fcc 3,4,5 dicht; zaehl cpu2 fcc 3,4,5,8,12 bloch
  eis cpu2 12 4; eis cpu2 8 1; eis cpu2 8 2 ) &
wait
echo "laeufe fertig $(date --iso-8601=seconds)" > "$D/laeufe_fertig.txt"
bash "$K" cpu r34eis-auswertung "$C/auswertung.py" "$D" "$D/auswertung.json" 12 8 12 8 3,4,5 > "$D/auswertung.log" 2>&1
echo "auswertung fertig $(date --iso-8601=seconds)" >> "$D/laeufe_fertig.txt"
