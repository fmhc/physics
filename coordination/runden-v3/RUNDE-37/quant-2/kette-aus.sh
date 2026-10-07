#!/bin/bash
# QUANT-2 Gesamtauswertung (Spur cpu7, nach kette-s7 und kette-p0): kubisch (rmin 0.9), Netz (rmin 0 und 0.3).
set -u
D=/home/fmh/fmhc-physics-remote/quant-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
cd $D
until [ -f $L/kette-s7.txt ] && [ -f $L/kette-p0.txt ]; do sleep 5; done
df -h /home | tail -1
bash $K cpu7 q2-ausk code/qu2.py auswertung --ein $L/k6-heiss $L/k6-kalt $L/k8-heiss $L/k8-kalt --rmin 0.9 --out $L/aus-kub.json > $L/aus-kub.log 2>&1
bash $K cpu7 q2-ausn code/qu2.py auswertung --ein $L/n1-dec-heiss $L/w1-heiss $L/w2-kalt $L/f3-heiss $L/f3-kalt $L/p130 $L/p142 $L/p160 $L/p200 $L/s142-nt6 $L/s142-nt4 --rmin 0.0 --out $L/aus-netz.json > $L/aus-netz.log 2>&1
bash $K cpu7 q2-ausn3 code/qu2.py auswertung --ein $L/p130 $L/p142 $L/s142-nt6 $L/s142-nt4 --rmin 0.3 --out $L/aus-netz-r03.json > $L/aus-netz-r03.log 2>&1
cd $L && sha256sum *.json *.npz *.log > PRUEFSUMMEN-lauf.txt
echo "kette-aus fertig $(date -u +%H:%M:%S)" > $L/kette-aus.txt
