#!/bin/bash
# Q-STERN Starter Spur cpu2: einmalig per nohup; Liste der Reihe nach, jeder Lauf ueber kleintest.sh (<= 10 min).
set -u
D=/home/fmh/fmhc-physics-remote/runde13-q-stern
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=cpu2
cd "$D" || exit 1
mkdir -p "$D/aus" "$D/logs"
COMMON="--modell kg --n-mid 1 --max-kand 6 --budget 540 --pole nein"
PA1="0.700,0.705,0.710,0.715,0.720,0.725"
PA2="0.725,0.730,0.735,0.740,0.745,0.750"
PB1="0.75,0.76,0.77,0.78,0.79"
PB2="0.79,0.80,0.81,0.82"
QA="0.70,0.71,0.72,0.73,0.74,0.75,0.76"
QB1="0.760,0.765,0.770,0.775,0.780,0.785,0.790"
QB2="0.790,0.795,0.800,0.805,0.810,0.815,0.820"
lauf() {
  local n=$1; shift
  echo "lauf $n start $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
  bash "$KT" "$SP" "$n" qstern.py "$@" --aus "$D/aus" --name "$n" > "$D/logs/$n.log" 2>&1
  local rc=$?
  echo "lauf $n ende $(date --iso-8601=seconds) rc=$rc" >> "$D/logs/starter-$SP.log"
}
echo "start-cpu2.sh Start $(date --iso-8601=seconds) PID $$" >> "$D/logs/starter-$SP.log"
lauf k1-h0.01 familie --alpha 0 --h 0.01 --modell kg --budget 540 --pole nein
for a in 0.1 0.03; do
  lauf "k2-a$a" k2 --alpha "$a" --x 0.75,0.80,0.85 --h 0.02 --modell kg
  lauf "a$a-h0.01-pa1" familie --alpha "$a" --h 0.01 --x "$PA1" $COMMON
  lauf "a$a-h0.01-pa2" familie --alpha "$a" --h 0.01 --x "$PA2" $COMMON
  lauf "a$a-h0.01-pb1" familie --alpha "$a" --h 0.01 --x "$PB1" $COMMON
  lauf "a$a-h0.01-pb2" familie --alpha "$a" --h 0.01 --x "$PB2" $COMMON
done
lauf k2-a0.01 k2 --alpha 0.01 --x 0.75,0.80,0.85 --h 0.02 --modell kg
lauf a0.01-h0.01-pa familie --alpha 0.01 --h 0.01 --x "$QA" $COMMON
lauf a0.01-h0.01-pb1 familie --alpha 0.01 --h 0.01 --x "$QB1" $COMMON
lauf a0.01-h0.01-pb2 familie --alpha 0.01 --h 0.01 --x "$QB2" $COMMON
echo "start-cpu2.sh Ende $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
