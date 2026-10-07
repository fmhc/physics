#!/bin/bash
# Testlaeufe an den vorhergesagten Sprossen (nach dem Einfrieren), beide Stufen, vier Spuren.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-20/sprossen-vorab
RM=/home/fmh/fmhc-physics-remote/runde20-sprossen-vorab
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
PY=$RM/code/sprossen_vorab.py
lauf() {  # spur kurz stufe teil auswahl
  ssh fmh@192.168.178.69 "cd $RM && bash $KT $1 $2 $PY test $3 $RM/prof-st$3 $RM/hilfs/zeilen-126.json $RM/hilfs/bekannte.json $RM/prof-st1/profile-info.json $RM/aus/test/test/test-st$3-$4.json $5 test" > $D/logs/$2.log 2>&1
}
( lauf cpu r20sv-test-st2-a 2 a 0:44.414,1:44.720,2:44.473; lauf cpu r20sv-test-st1-a 1 a 0:44.414,1:44.720,2:44.473,3:44.059 ) &
( lauf cpu2 r20sv-test-st2-b 2 b 3:44.059,4:39.13,4:41.33; lauf cpu2 r20sv-test-st1-b 1 b 4:39.13,4:41.33,5:40.51,5:42.76 ) &
( lauf cpu3 r20sv-test-st2-c 2 c 5:40.51,5:42.76,6:39.51; lauf cpu3 r20sv-test-st1-c 1 c 6:39.51,6:41.83,7:40.65,7:43.03 ) &
( lauf cpu4 r20sv-test-st2-d 2 d 6:41.83,7:40.65,7:43.03 ) &
wait
echo "test laeufe fertig $(date '+%H:%M:%S')"
