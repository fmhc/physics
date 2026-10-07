#!/bin/bash
# Q-STERN Starter Spur cpu: einmalig per nohup; arbeitet die Liste der Reihe nach ab, jeder Lauf ueber kleintest.sh
# (hoechstens 10 min Wanduhr). Kein Dienst, kein Timer. Reihenfolge = Prioritaet (PLAN Abschnitt 4).
set -u
D=/home/fmh/fmhc-physics-remote/runde13-q-stern
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=cpu
cd "$D" || exit 1
mkdir -p "$D/aus" "$D/logs"
COMMON="--modell kg --n-mid 1 --max-kand 6 --budget 540 --pole nein"
PA="0.700,0.705,0.710,0.715,0.720,0.725,0.730,0.735,0.740,0.745,0.750"
PB="0.75,0.76,0.77,0.78,0.79,0.80,0.81,0.82"
PC="0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.90"
PC1="0.82,0.83,0.84,0.85,0.86"
PC2="0.86,0.87,0.88,0.89,0.90"
QA="0.70,0.71,0.72,0.73,0.74,0.75,0.76"
QB="0.760,0.765,0.770,0.775,0.780,0.785,0.790,0.795,0.800,0.805,0.810,0.815,0.820"
NEB="0.60,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.70"
lauf() {
  local n=$1; shift
  echo "lauf $n start $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
  bash "$KT" "$SP" "$n" qstern.py "$@" --aus "$D/aus" --name "$n" > "$D/logs/$n.log" 2>&1
  local rc=$?
  echo "lauf $n ende $(date --iso-8601=seconds) rc=$rc" >> "$D/logs/starter-$SP.log"
}
k3() {
  local a=$1 t=$2 x=$3
  local f="$D/aus/a$a-h0.02-$t.json"
  local n
  n=$(jq '[.kandidaten[]? | (.rechteck.umlauf? // 0) | select(. != 0)] | length' "$f" 2>/dev/null)
  if [ "${n:-0}" -gt 0 ] 2>/dev/null; then
    lauf "a$a-k3-$t" familie --alpha "$a" --h 0.02 --r-fak 1.5 --x "$x" $COMMON
  else
    echo "K3 a$a $t: kein Kandidat mit Umlauf ungleich 0 (${n:-leer}) $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
  fi
}
echo "start-cpu.sh Start $(date --iso-8601=seconds) PID $$" >> "$D/logs/starter-$SP.log"
lauf k1-h0.02 familie --alpha 0 --h 0.02 --modell kg --budget 540 --pole nein
for a in 0.1 0.03; do
  lauf "a$a-h0.02-pa" familie --alpha "$a" --h 0.02 --x "$PA" $COMMON
  lauf "a$a-h0.02-pb" familie --alpha "$a" --h 0.02 --x "$PB" $COMMON
  lauf "a$a-h0.02-pc" familie --alpha "$a" --h 0.02 --x "$PC" $COMMON
  lauf "a$a-h0.01-pc1" familie --alpha "$a" --h 0.01 --x "$PC1" $COMMON
  lauf "a$a-h0.01-pc2" familie --alpha "$a" --h 0.01 --x "$PC2" $COMMON
  k3 "$a" pa "$PA"
  k3 "$a" pb "$PB"
  k3 "$a" pc "$PC"
done
lauf a0.01-h0.02-pa familie --alpha 0.01 --h 0.02 --x "$QA" $COMMON
lauf a0.01-h0.02-pb familie --alpha 0.01 --h 0.02 --x "$QB" $COMMON
lauf a0.01-h0.02-pc familie --alpha 0.01 --h 0.02 --x "$PC" $COMMON
lauf a0.01-h0.01-pc1 familie --alpha 0.01 --h 0.01 --x "$PC1" $COMMON
lauf a0.01-h0.01-pc2 familie --alpha 0.01 --h 0.01 --x "$PC2" $COMMON
k3 0.01 pa "$QA"
k3 0.01 pb "$QB"
k3 0.01 pc "$PC"
lauf neben-a0.1-h0.02 familie --alpha 0.1 --h 0.02 --x "$NEB" $COMMON --band neben
lauf neben-a0.03-h0.02 familie --alpha 0.03 --h 0.02 --x "$NEB" $COMMON --band neben
echo "start-cpu.sh Ende $(date --iso-8601=seconds)" >> "$D/logs/starter-$SP.log"
