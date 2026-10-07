#!/bin/bash
# B-BALL-2 (Runde 13, Karte 2): einmaliger Starter auf der .69, per nohup gestartet. Kein Dienst, kein Timer, kein Hook.
# Spuren nur cpu3 und cpu4 (Zusatz der Leitung). Jeder Aufruf ueber kleintest.sh (RuntimeMaxSec 600, Budget im Code 520 s).
# Reihenfolge: Kontrollen K1 (t = 0) und K2 (t = 1), dann t = 0,5, dann 0,25, dann 0,75 (Zusatz der Leitung).
set -u
R=/home/fmh/fmhc-physics-remote/runde13-bball-leiter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 2
mkdir -p "$R/aus2"
X0=0.7577,0.7627,0.7677,0.7727,0.7777,0.7827,0.7877,0.7927,0.7977,0.8027,0.8077,0.8127,0.8177,0.8227,0.8277,0.8327,0.8377
X25=0.7897,0.7947,0.7997,0.8047,0.8097,0.8147,0.8197,0.8247,0.8297,0.8347,0.8397,0.8447,0.8497,0.8547,0.8597,0.8647,0.8697
X50=0.8217,0.8267,0.8317,0.8367,0.8417,0.8467,0.8517,0.8567,0.8617,0.8667,0.8717,0.8767,0.8817,0.8867,0.8917,0.8967,0.9017
X75=0.8536,0.8586,0.8636,0.8686,0.8736,0.8786,0.8836,0.8886,0.8936,0.8986,0.9036,0.9086,0.9136,0.9186,0.9236,0.9286,0.9336
X100=0.8856,0.8906,0.8956,0.9006,0.9056,0.9106,0.9156,0.9206,0.9256,0.9306,0.9356,0.9406,0.9456,0.9506,0.9556,0.9606,0.9656
lauf() {
  local spur=$1 name=$2
  shift 2
  bash "$KT" "$spur" "$name" bball2.py familie --modell mix "$@" --aus "$R/aus2" --name "$name" > "$R/logs/$name.log" 2>&1
  echo "$name rc=$? $(date --iso-8601=seconds)"
}
echo "start2.sh Beginn $(date --iso-8601=seconds)"
(
  lauf cpu3 k1-t0-h0.02 --t 0.0 --band K1 --x "$X0" --h 0.02 --pole ja
  lauf cpu3 k2-t1-h0.01 --t 1.0 --band K2 --x "$X100" --h 0.01
  lauf cpu3 t0.5-h0.02 --t 0.5 --band t0.5 --x "$X50" --h 0.02 --pole ja
  lauf cpu3 t0.25-h0.01 --t 0.25 --band t0.25 --x "$X25" --h 0.01
  lauf cpu3 t0.75-h0.02 --t 0.75 --band t0.75 --x "$X75" --h 0.02 --pole ja
) &
(
  lauf cpu4 k1-t0-h0.01 --t 0.0 --band K1 --x "$X0" --h 0.01
  lauf cpu4 k2-t1-h0.02 --t 1.0 --band K2 --x "$X100" --h 0.02 --pole ja
  lauf cpu4 t0.5-h0.01 --t 0.5 --band t0.5 --x "$X50" --h 0.01
  lauf cpu4 t0.25-h0.02 --t 0.25 --band t0.25 --x "$X25" --h 0.02 --pole ja
  lauf cpu4 t0.75-h0.01 --t 0.75 --band t0.75 --x "$X75" --h 0.01
) &
wait
echo "start2.sh Ende $(date --iso-8601=seconds)"
