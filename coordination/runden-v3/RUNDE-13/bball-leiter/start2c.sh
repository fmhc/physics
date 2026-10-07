#!/bin/bash
# B-BALL-2c (Runde 13, Karte 2c): einmaliger Starter auf der .69, per nohup gestartet. Kein Dienst, kein Timer, kein Hook.
# Spuren nur cpu3 und cpu4 (Zusatz der Leitung). Jeder Aufruf ueber kleintest.sh (RuntimeMaxSec 600, Budget im Code 520 s).
# Je (t, h) zwei Haelften: A = 0,82 .. 0,895 (16 Zeilen), B = 0,895 .. 0,97 (16 Zeilen), Zeile 0,895 in beiden.
# Reihenfolge nach Zusatz der Leitung: t = 0,95, dann 0,975, dann 0,925.
set -u
R=/home/fmh/fmhc-physics-remote/runde13-bball-leiter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 2
mkdir -p "$R/aus2c"
XA=0.82,0.825,0.83,0.835,0.84,0.845,0.85,0.855,0.86,0.865,0.87,0.875,0.88,0.885,0.89,0.895
XB=0.895,0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97
lauf() {
  local spur=$1 t=$2 h=$3 teil=$4 x=$5 pole=$6
  local name="t$t-h$h-$teil"
  bash "$KT" "$spur" "$name" bball2.py familie --modell mix --t "$t" --band "t$t" --x "$x" --h "$h" --pole "$pole" \
    --aus "$R/aus2c" --name "$name" > "$R/logs/2c-$name.log" 2>&1
  echo "$name rc=$? $(date --iso-8601=seconds)"
}
echo "start2c.sh Beginn $(date --iso-8601=seconds)"
(
  lauf cpu3 0.95 0.02 A "$XA" ja
  lauf cpu3 0.95 0.02 B "$XB" ja
  lauf cpu3 0.975 0.01 A "$XA" nein
  lauf cpu3 0.975 0.01 B "$XB" nein
  lauf cpu3 0.925 0.02 A "$XA" ja
  lauf cpu3 0.925 0.02 B "$XB" ja
) &
(
  lauf cpu4 0.95 0.01 A "$XA" nein
  lauf cpu4 0.95 0.01 B "$XB" nein
  lauf cpu4 0.975 0.02 A "$XA" ja
  lauf cpu4 0.975 0.02 B "$XB" ja
  lauf cpu4 0.925 0.01 A "$XA" nein
  lauf cpu4 0.925 0.01 B "$XB" nein
) &
wait
echo "start2c.sh Ende $(date --iso-8601=seconds)"
