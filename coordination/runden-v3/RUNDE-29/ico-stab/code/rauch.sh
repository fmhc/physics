#!/bin/bash
# ICO-STAB (Runde 29): Rauchlaeufe vor dem Einfrieren, Parameter in keinem echten Lauf (Speichen-Ruhelaenge 0,98 bzw.
# N = 8), interne Zeitgrenze 100 s. Aufruf auf der .69: bash rauch.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/ico_stab.py
D=/home/fmh/fmhc-physics-remote/runde29-ico-stab/rauch
mkdir -p "$D"
cd "$D" || exit 1

lauf() {  # spur name N lag zentrum start versatz amp l_sp
  bash "$K" "$1" "r29is-$2" "$C" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$D/$2.json" 100 > "$D/$2.log" 2>&1
}

( lauf cpu rauch_frei_8 8 G frei flaeche 0.01 0.001 0.98 ) &
( lauf cpu2 rauch_fest_8 8 G fest null 0 0.001 0.98 ) &
( lauf cpu3 rauch_frei_20 20 G frei zufall1 0.01 0.001 0.98 ) &
( lauf cpu4 rauch_ctrl_8 8 G frei zufall1 0.01 0.001 Rc ) &
( lauf cpu6 rauch_e_8 8 E frei flaeche 0.01 0.001 0.98 ) &
wait
echo "rauch fertig $(date --iso-8601=seconds)"
