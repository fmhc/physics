#!/bin/bash
# ICO-STAB (Runde 29): echte Laeufe nach PLAN.md Abschnitt 2, je Spur nacheinander ueber kleintest.sh; danach
# auswertung.py. Aufruf auf der .69: bash /home/fmh/fmhc-physics-remote/runde29-ico-stab/code/laeufe.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/ico_stab.py
A=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/auswertung.py
D=/home/fmh/fmhc-physics-remote/runde29-ico-stab/lauf
cd "$D" || exit 1

lauf() {  # spur name N lag zentrum start versatz amp l_sp
  bash "$K" "$1" "r29is-$2" "$C" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$D/$2.json" > "$D/$2.log" 2>&1
}

( lauf cpu sym_20 20 G fest null 0 0.001 1; lauf cpu frei_null_20 20 G frei null 0 0.001 1
  lauf cpu frei_ecke_20 20 G frei ecke 0.01 0.001 1; lauf cpu ctrl_12 12 G frei zufall1 0.01 0.001 Rc ) &
( lauf cpu2 frei_kante_20 20 G frei kante 0.01 0.001 1; lauf cpu2 frei_flaeche_20 20 G frei flaeche 0.01 0.001 1
  lauf cpu2 frei_zufall1_20 20 G frei zufall1 0.01 0.001 1; lauf cpu2 ctrl_20 20 G frei zufall1 0.01 0.001 Rc ) &
( lauf cpu3 frei_zufall2_20 20 G frei zufall2 0.01 0.001 1; lauf cpu3 frei_zufall3_20 20 G frei zufall3 0.01 0.001 1
  lauf cpu3 sym_12 12 G fest null 0 0.001 1; lauf cpu3 frei_null_12 12 G frei null 0 0.001 1 ) &
( lauf cpu4 frei_ecke_12 12 G frei ecke 0.01 0.001 1; lauf cpu4 frei_kante_12 12 G frei kante 0.01 0.001 1
  lauf cpu4 frei_flaeche_12 12 G frei flaeche 0.01 0.001 1; lauf cpu4 frei_zufall1_12 12 G frei zufall1 0.01 0.001 1
  lauf cpu4 e_sym_12 12 E fest null 0 0.001 1 ) &
( lauf cpu6 frei_zufall2_12 12 G frei zufall2 0.01 0.001 1; lauf cpu6 frei_zufall3_12 12 G frei zufall3 0.01 0.001 1
  lauf cpu6 e_frei_flaeche_12 12 E frei flaeche 0.01 0.001 1 ) &
wait
echo "laeufe fertig $(date --iso-8601=seconds)"
bash "$K" cpu r29is-auswertung "$A" "$D" "$D/auswertung.json" > "$D/auswertung.log" 2>&1
echo "auswertung fertig $(date --iso-8601=seconds)"
