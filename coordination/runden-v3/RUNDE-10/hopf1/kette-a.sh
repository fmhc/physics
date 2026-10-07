#!/bin/bash
# HOPF-1 Stufe A: beide Baelle, 3D h = 0,2 und 0,1, 2D h = 0,01, Hopfzahl N = 128; Spur p4000a.
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde10-hopf1 && nohup bash kette-a.sh > KETTE-A.log 2>&1 < /dev/null &
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde10-hopf1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
echo "Kette A Start $(date --iso-8601=seconds)"
bash $K p4000a hopf1a06 hopf1.py --geraet cuda --w2 0.6 --h 0.2,0.1 --h2d 0.01 --hopf-N 128 --out A-w060 > LAUF-hopf1a06.log 2>&1
echo "A 0,6 rc=$? $(date --iso-8601=seconds)"
bash $K p4000a hopf1a08 hopf1.py --geraet cuda --w2 0.8 --h 0.2,0.1 --h2d 0.01 --hopf-N 128 --out A-w080 > LAUF-hopf1a08.log 2>&1
echo "A 0,8 rc=$? $(date --iso-8601=seconds)"
echo "Kette A fertig $(date --iso-8601=seconds)"
