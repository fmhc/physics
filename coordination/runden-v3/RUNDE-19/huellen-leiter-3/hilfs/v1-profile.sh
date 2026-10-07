#!/bin/bash
# V1: Profile beider Stufen (Zeilen 0 bis 125), parallel auf cpu und cpu2. Aufruf auf der .69 im eigenen Ordner.
R=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 1
bash "$K" cpu r19hl3-prof1 "$R/code/huellen_leiter3.py" profile M2 1 "$R/aus/prof-st1" "$R/hilfs/zeilen-126.json" > "$R/logs/prof-st1.log" 2>&1 &
bash "$K" cpu2 r19hl3-prof2 "$R/code/huellen_leiter3.py" profile M2 2 "$R/aus/prof-st2" "$R/hilfs/zeilen-126.json" > "$R/logs/prof-st2.log" 2>&1 &
wait
echo v1-fertig
