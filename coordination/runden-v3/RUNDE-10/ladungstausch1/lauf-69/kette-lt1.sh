#!/bin/bash
# LADUNGSTAUSCH-1 Kette: Rauchtest auf cpu6 (CPU, T = 60, grob), bei rc = 0 die Laeufe R1 bis R4 auf p4000a.
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde10-ladungstausch1 && nohup bash kette-lt1.sh > KETTE-LT1.log 2>&1 < /dev/null &
export LC_ALL=C
cd /home/fmh/fmhc-physics-remote/runde10-ladungstausch1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=/home/fmh/fmhc-physics-remote/runde10-ladungstausch1
echo "Kette LT1 Start $(date --iso-8601=seconds)"
bash $K cpu6 lt1rauch t5k_ladungstausch.py --geraet cpu --kurz --w2 0.7 --d 4 --d-gleich 4 --out $O/aus-rauch > LAUF-lt1rauch.log 2>&1
RC=$?
echo "Rauchtest rc=$RC $(date --iso-8601=seconds)"
if [ "$RC" != "0" ]; then echo "Kette LT1 abgebrochen"; exit 1; fi
bash $K p4000a lt1r1 t5k_ladungstausch.py --geraet cuda --w2 0.7 --d 3,4,5,6 --d-gleich 4 --d-theta 4 --T 3000 --out $O/aus-r1-w070 > LAUF-lt1r1.log 2>&1
echo "R1 rc=$? $(date --iso-8601=seconds)"
bash $K p4000a lt1r2 t5k_ladungstausch.py --geraet cuda --w2 0.6 --d 3,4,5,6 --d-gleich 4 --T 3000 --out $O/aus-r2-w060 > LAUF-lt1r2.log 2>&1
echo "R2 rc=$? $(date --iso-8601=seconds)"
bash $K p4000a lt1r3 t5k_ladungstausch.py --geraet cuda --w2 0.8 --d 3,4,5,6 --d-gleich 4 --T 3000 --out $O/aus-r3-w080 > LAUF-lt1r3.log 2>&1
echo "R3 rc=$? $(date --iso-8601=seconds)"
bash $K p4000a lt1r4 t5k_ladungstausch.py --geraet cuda --w2 0.7 --d 4 --d-gleich 0 --kein-einzel --stufen fein --T 9000 --out $O/aus-r4-w070-lang > LAUF-lt1r4.log 2>&1
echo "R4 rc=$? $(date --iso-8601=seconds)"
echo "Kette LT1 fertig $(date --iso-8601=seconds)"
