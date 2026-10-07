#!/bin/bash
# Testlaeufe an den vorhergesagten Sprossen (Start bei P_lin, nach dem Einfrieren), l = 1 und 2, beide Stufen.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-21/sprossen-l1l2
RM=/home/fmh/fmhc-physics-remote/runde21-sprossen-l1l2
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
PY=$RM/code/sprossen_l1l2.py
lauf() {  # spur kurz ell stufe teil auswahl
  ssh fmh@192.168.178.69 "cd $RM && bash $KT $1 $2 $PY ell=$3 test $4 $RM/prof-st$4 $RM/aus/zeilen.json $RM/hilfs/bekannte-l$3.json $RM/prof-st1/profile-info.json $RM/aus/test/test-l$3-st$4-$5.json $6 test" > $D/logs/$2.log 2>&1
}
T1A=0:21.447,0:23.874,1:20.209,1:22.394
T1B=2:21.662,2:23.946,3:20.616,3:23.132
T2A=0:20.088,0:22.546,1:21.009
T2B=1:23.231,2:20.092,2:22.504
lauf cpu r21sl-test-l1-st1-a 1 1 a $T1A,$T1B &
( lauf cpu2 r21sl-test-l2-st1-a 2 1 a $T2A,$T2B; lauf cpu2 r21sl-test-l2-st2-b 2 2 b $T2B ) &
lauf cpu3 r21sl-test-l1-st2-a 1 2 a $T1A &
lauf cpu4 r21sl-test-l1-st2-b 1 2 b $T1B &
lauf cpu6 r21sl-test-l2-st2-a 2 2 a $T2A &
wait
echo "test laeufe fertig $(date '+%H:%M:%S')"
