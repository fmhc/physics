#!/bin/bash
# B-BALL-LEITER (Runde 13): einmaliger Starter auf der .69, per nohup gestartet. Kein Dienst, kein Timer, kein Hook.
# Spuren nur cpu3 und cpu4 (Zusatz der Leitung). Jeder Aufruf ueber kleintest.sh (RuntimeMaxSec 600, Budget im Code 520 s).
# Ablauf: K1 (Sextik, beide Stufen) -> Auswertung K1 -> nur bei bestandenem K1 die drei Log-Baender je Stufe -> Auswertung.
set -u
R=/home/fmh/fmhc-physics-remote/runde13-bball-leiter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 2
B1=0.30,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40
B2=0.50,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.60
B3=0.70,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.80
lauf() {
  local spur=$1 name=$2
  shift 2
  bash "$KT" "$spur" "$name" bball.py "$@" --aus "$R/aus" --name "$name" > "$R/logs/$name.log" 2>&1
  echo "$name rc=$? $(date --iso-8601=seconds)"
}
echo "start.sh Beginn $(date --iso-8601=seconds)"
lauf cpu3 kg-h0.02 familie --modell kg --h 0.02 --pole ja &
lauf cpu4 kg-h0.01 familie --modell kg --h 0.01 &
wait
lauf cpu3 auswertung-k1 auswertung
if ! grep -q "K1 h = 0.02: bestanden" "$R/aus/auswertung-k1.txt" || ! grep -q "K1 h = 0.01: bestanden" "$R/aus/auswertung-k1.txt"; then
  echo "K1 verfehlt: Abbruch $(date --iso-8601=seconds)"
  exit 1
fi
(
  lauf cpu3 log-b1-h0.02 familie --modell log --band b1 --x "$B1" --h 0.02 --pole ja
  lauf cpu3 log-b2-h0.02 familie --modell log --band b2 --x "$B2" --h 0.02 --pole ja
  lauf cpu3 log-b3-h0.02 familie --modell log --band b3 --x "$B3" --h 0.02 --pole ja
) &
(
  lauf cpu4 log-b1-h0.01 familie --modell log --band b1 --x "$B1" --h 0.01
  lauf cpu4 log-b2-h0.01 familie --modell log --band b2 --x "$B2" --h 0.01
  lauf cpu4 log-b3-h0.01 familie --modell log --band b3 --x "$B3" --h 0.01
) &
wait
lauf cpu3 auswertung auswertung
echo "start.sh Ende $(date --iso-8601=seconds)"
