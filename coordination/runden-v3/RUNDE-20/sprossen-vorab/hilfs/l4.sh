#!/bin/bash
# L4-Durchgang: bekannte Stellen, beide Stufen, vier Spuren. Aufruf: bash hilfs/l4.sh <durchgang>
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-20/sprossen-vorab
RM=/home/fmh/fmhc-physics-remote/runde20-sprossen-vorab
G=$1
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
PY=$RM/code/sprossen_vorab.py
lauf() {  # spur kurz stufe teil auswahl
  ssh fmh@192.168.178.69 "cd $RM && bash $KT $1 $2 $PY test $3 $RM/prof-st$3 $RM/hilfs/zeilen-126.json $RM/hilfs/bekannte.json $RM/prof-st1/profile-info.json $RM/aus/l4-d$G/l4/l4-st$3-$4.json $5 l4" > $D/logs/$2.log 2>&1
}
( lauf cpu r20sv-l4d$G-st1-a 1 a 0:39.594,3:39.765,2:40.229,1:40.506,4:36.92,6:37.19; lauf cpu r20sv-l4d$G-st2-c 2 c 2:42.351,1:42.613 ) &
( lauf cpu2 r20sv-l4d$G-st1-b 1 b 3:41.912,0:42.004,2:42.351,1:42.613,5:38.26,7:38.27; lauf cpu2 r20sv-l4d$G-st2-d 2 d 5:38.26,7:38.27 ) &
lauf cpu3 r20sv-l4d$G-st2-a 2 a 0:39.594,3:39.765,2:40.229,4:36.92 &
( lauf cpu4 r20sv-l4d$G-st2-b 2 b 1:40.506,3:41.912,0:42.004,6:37.19 ) &
wait
echo "l4 d$G laeufe fertig $(date '+%H:%M:%S')"
