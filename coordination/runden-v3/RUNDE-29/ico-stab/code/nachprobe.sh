#!/bin/bash
# ICO-STAB (Runde 29): Nachprobe nach den echten Laeufen, NICHT im Plan, NICHT gewertet. Anlass: ctrl_12 endete bei
# maxit mit |grad| 2,7e-6 (Liniensuche am Rundungsboden der Energie). Gleicher eingefrorener Code, gleiche Parameter wie
# ctrl_12, nur andere Startrichtungen. Aufruf auf der .69: bash nachprobe.sh
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=/home/fmh/fmhc-physics-remote/runde29-ico-stab/code/ico_stab.py
D=/home/fmh/fmhc-physics-remote/runde29-ico-stab/nachprobe
mkdir -p "$D"
cd "$D" || exit 1

lauf() {  # spur name N lag zentrum start versatz amp l_sp
  bash "$K" "$1" "r29is-$2" "$C" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$D/$2.json" > "$D/$2.log" 2>&1
}

( lauf cpu np_ctrl_12_zufall2 12 G frei zufall2 0.01 0.001 Rc ) &
( lauf cpu2 np_ctrl_12_zufall3 12 G frei zufall3 0.01 0.001 Rc ) &
( lauf cpu3 np_ctrl_12_null 12 G frei null 0 0.001 Rc ) &
wait
echo "nachprobe fertig $(date --iso-8601=seconds)"
