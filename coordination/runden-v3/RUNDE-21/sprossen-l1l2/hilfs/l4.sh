#!/bin/bash
# L4-Durchgang: letzte zwei bekannte Stellen jeder Kurve, l = 1 und 2, beide Stufen, fuenf Spuren.
# Aufruf: bash hilfs/l4.sh <durchgang>
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-21/sprossen-l1l2
RM=/home/fmh/fmhc-physics-remote/runde21-sprossen-l1l2
G=$1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
PY=$RM/code/sprossen_l1l2.py
lauf() {  # spur kurz ell stufe teil auswahl
  ssh fmh@192.168.178.69 "cd $RM && bash $KT $1 $2 $PY ell=$3 test $4 $RM/prof-st$4 $RM/aus/zeilen.json $RM/hilfs/bekannte-l$3.json $RM/prof-st1/profile-info.json $RM/aus/l4-d$G/l4-l$3-st$4-$5.json $6 l4" > $D/logs/$2.log 2>&1
}
L1A=0:16.593,0:19.02,1:15.839,1:18.024
L1B=2:17.094,2:19.378,3:15.584,3:18.1
L2A=0:15.172,0:17.63,1:16.565
L2B=1:18.787,2:15.268,2:17.68
lauf cpu r21sl-l4d$G-l1-st1-a 1 1 a $L1A,$L1B &
( lauf cpu2 r21sl-l4d$G-l2-st1-a 2 1 a $L2A,$L2B; lauf cpu2 r21sl-l4d$G-l2-st2-b 2 2 b $L2B ) &
lauf cpu3 r21sl-l4d$G-l1-st2-a 1 2 a $L1A &
lauf cpu4 r21sl-l4d$G-l1-st2-b 1 2 b $L1B &
lauf cpu6 r21sl-l4d$G-l2-st2-a 2 2 a $L2A &
wait
echo "l4 d$G laeufe fertig $(date '+%H:%M:%S')"
