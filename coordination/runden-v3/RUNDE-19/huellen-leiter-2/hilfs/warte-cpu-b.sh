#!/bin/bash
# Zweite Welle auf Spur cpu: startet erst, wenn die erste Kette auf cpu fertig ist (Eintrag in ketten.log)
D=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-2
until grep -q "^kette cpu $D/hilfs/auf-cpu.txt fertig" "$D/logs/ketten.log" 2>/dev/null; do sleep 10; done
bash "$D/hilfs/kette.sh" cpu "$D/hilfs/auf-cpu-b.txt"
