#!/bin/bash
# ICO-STAB (Runde 29): Rauchlaeufe Runde 2 (Zentrum fest = Mittel der Ecken), Parameter in keinem echten Lauf
# (Speichen-Ruhelaenge 0,98, N = 8 bzw. 20), interne Zeitgrenze 100 s; danach auswertung.py an Verweisen in rauch/test/.
# Aufruf auf der .69: bash rauch2.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/ico_stab.py
A=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/auswertung.py
D=/home/fmh/fmhc-physics-remote/runde29-ico-stab/rauch
cd "$D" || exit 1

lauf() {  # spur name N lag zentrum start versatz amp l_sp
  bash "$K" "$1" "r29is-$2" "$C" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$D/$2.json" 100 > "$D/$2.log" 2>&1
}

( lauf cpu rauch_fest2_8 8 G fest null 0 0.001 0.98 ) &
( lauf cpu2 rauch_fest2_20 20 G fest null 0 0.001 0.98 ) &
( lauf cpu3 rauch_e_fest_8 8 E fest null 0 0.001 0.98 ) &
( lauf cpu4 rauch_frei_null_8 8 G frei null 0 0.001 0.98 ) &
( lauf cpu6 rauch_frei_ecke_8 8 G frei ecke 0.01 0.001 0.98 ) &
wait
mkdir -p "$D/test"
cd "$D/test" || exit 1
ln -sf ../rauch_ctrl_8.json ctrl_12.json
ln -sf ../rauch_ctrl_8.json ctrl_20.json
ln -sf ../rauch_fest2_8.json sym_12.json
ln -sf ../rauch_fest2_20.json sym_20.json
ln -sf ../rauch_frei_8.json frei_flaeche_12.json
ln -sf ../rauch_frei_null_8.json frei_null_12.json
ln -sf ../rauch_frei_ecke_8.json frei_ecke_12.json
ln -sf ../rauch_frei_20.json frei_zufall1_20.json
ln -sf ../rauch_e_fest_8.json e_sym_12.json
ln -sf ../rauch_e_8.json e_frei_flaeche_12.json
bash "$K" cpu r29is-rauch-auswertung "$A" "$D/test" "$D/test/auswertung_test.json" > "$D/test/auswertung_test.log" 2>&1
echo "rauch2 fertig $(date --iso-8601=seconds)"
