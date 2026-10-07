#!/bin/bash
# Q-STERN-2 Starter: einmalig per nohup; Liste der Reihe nach, jeder Lauf ueber kleintest.sh (<= 10 min).
set -u
D=/home/fmh/fmhc-physics-remote/runde14-q-stern2
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$D" || exit 1
A1=0.00087
A2=0.0027
O="0.770,0.775,0.780,0.785,0.790,0.795,0.800"
U="0.740,0.745,0.750,0.755,0.760,0.765,0.770"
K3A1="0.785,0.790,0.795,0.800"
K3A2="0.775,0.780,0.785,0.790"
COMMON="--modell kg --n-mid 1 --max-kand 3 --budget 420 --pole nein --n-rampe 2"
K3C="--modell kg --n-mid 0 --max-kand 3 --budget 420 --pole nein --n-rampe 2 --r-fak 1.5"
lauf() {
  local n=$1; shift
  echo "lauf $n start $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
  bash "$KT" "$SP" "$n" qstern2.py "$@" --aus "$D/aus" --name "$n" > "$D/logs/$n.log" 2>&1
  local rc=$?
  echo "lauf $n ende $(date --iso-8601=seconds) rc=$rc" >> "$D/logs/starter-$SP.log"
}
SP=cpu3
echo "start-cpu3.sh Start $(date --iso-8601=seconds) PID $$" >> "$D/logs/starter-$SP.log"
lauf k2-a1 k2 --alpha $A1 --x 0.775,0.785,0.793,0.7977 --h 0.02 --modell kg --n-rampe 2
lauf k2-a2 k2 --alpha $A2 --x 0.775,0.785,0.793,0.7977 --h 0.02 --modell kg --n-rampe 2
lauf k4-h0.02 familie --alpha 0.01 --psi null --h 0.02 --x 0.75,0.76 --modell kg --n-mid 1 --max-kand 0 --budget 420 --pole nein
lauf a1-null-o-h0.02 familie --alpha $A1 --psi null --h 0.02 --x "$O" $COMMON
lauf a1-null-k3 familie --alpha $A1 --psi null --h 0.02 --x "$K3A1" $K3C
lauf a2-null-o-h0.02 familie --alpha $A2 --psi null --h 0.02 --x "$O" $COMMON
lauf a2-null-k3 familie --alpha $A2 --psi null --h 0.02 --x "$K3A2" $K3C
lauf a1-null-u-h0.02 familie --alpha $A1 --psi null --h 0.02 --x "$U" $COMMON
lauf a2-null-u-h0.02 familie --alpha $A2 --psi null --h 0.02 --x "$U" $COMMON
echo "start-cpu3.sh Ende $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
