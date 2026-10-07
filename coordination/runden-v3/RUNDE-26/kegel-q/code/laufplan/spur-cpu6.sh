#!/bin/bash
# KEGEL-Q Laufplan (Runde 26). Nur eine Folge von kleintest.sh-Aufrufen; kein Dienst.
set -u
B=/home/fmh/fmhc-physics-remote/runde26-kegel-q
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/kegel_q.py
cd $L
lauf() { local spur=$1 name=$2; shift 2; bash $K $spur r26kq-$name $P "$@" > $L/log-$name.txt 2>&1; }
D_ALLE=0,1.2,2.4,3.6,4.8,6,7.2,8.4,9.6,10.8,12,13.2,14.4,15.6,16.8,18,19.2
D_A=0,1.2,2.4,3.6,4.8,6,7.2,8.4,9.6
D_B=10.8,12,13.2,14.4,15.6,16.8,18,19.2
QS=50,100,200,400
lauf cpu6 kraft-n5-h0.2-b ball --rolle kraft --n 5 --h 0.2 --R 40 --Q 200 --d $D_B --aus "$L/kraft-n5-h0.2-Q200-b.json"
lauf cpu6 kraft-n7-h0.2-b ball --rolle kraft --n 7 --h 0.2 --R 40 --Q 200 --d $D_B --aus "$L/kraft-n7-h0.2-Q200-b.json"
lauf cpu6 kraft-n7-h0.3-Q100-400 ball --rolle kraft --n 7 --h 0.3 --R 40 --Q 100,400 --d $D_ALLE --aus "$L/kraft-n7-h0.3-Q{Q}.json"
echo "spur cpu6 fertig $(date --iso-8601=seconds)" > $L/fertig-cpu6.txt
