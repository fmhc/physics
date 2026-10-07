#!/bin/bash
# Q-STERN-2b Starter: einmalig per nohup; Liste der Reihe nach, jeder Lauf ueber kleintest.sh (<= 10 min).
set -u
D=/home/fmh/fmhc-physics-remote/runde15-q-stern2b
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$D" || exit 1
A1=0.00041
A2=0.00122
O="0.660,0.665,0.670,0.675,0.680,0.685,0.690"
K3A1="0.675,0.680,0.685,0.690"
K3A2="0.665,0.670,0.675,0.680"
F="--fenster 0.60,0.70,1.60,1.75"
COMMON="--modell kg --n-mid 1 --max-kand 3 --budget 420 --pole nein --n-rampe 2 $F"
K3C="--modell kg --n-mid 0 --max-kand 3 --budget 420 --pole nein --n-rampe 2 --r-fak 1.5 $F"
lauf() {
  local n=$1; shift
  echo "lauf $n start $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
  bash "$KT" "$SP" "$n" qstern2b.py "$@" --aus "$D/aus" --name "$n" > "$D/logs/$n.log" 2>&1
  local rc=$?
  echo "lauf $n ende $(date --iso-8601=seconds) rc=$rc" >> "$D/logs/starter-$SP.log"
}
SP=cpu
echo "start-cpu.sh Start $(date --iso-8601=seconds) PID $$" >> "$D/logs/starter-$SP.log"
lauf k1-h0.02 familie --alpha 0 --psi voll --h 0.02 --x 0.680,0.685,0.690 --modell kg --n-mid 1 --max-kand 2 --budget 420 --pole nein $F
lauf a1-voll-o-h0.02 familie --alpha $A1 --psi voll --h 0.02 --x "$O" $COMMON
lauf a1-voll-k3 familie --alpha $A1 --psi voll --h 0.02 --x "$K3A1" $K3C
lauf a2-voll-o-h0.02 familie --alpha $A2 --psi voll --h 0.02 --x "$O" $COMMON
lauf a2-voll-k3 familie --alpha $A2 --psi voll --h 0.02 --x "$K3A2" $K3C
echo "start-cpu.sh Ende $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
