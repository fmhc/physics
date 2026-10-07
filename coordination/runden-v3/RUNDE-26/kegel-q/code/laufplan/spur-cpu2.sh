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
for h in 0.4 0.3 0.2; do lauf cpu2 bind-n5-h$h ball --rolle bindung --n 5 --h $h --R 40 --Q $QS --d 0,19.2 --aus "$L/bind-n5-h$h-Q{Q}.json"; done
lauf cpu2 kraft-n5-h0.4 ball --rolle kraft --n 5 --h 0.4 --R 40 --Q 200 --d $D_ALLE --aus "$L/kraft-n5-h0.4-Q200.json"
lauf cpu2 kraft-n5-h0.3 ball --rolle kraft --n 5 --h 0.3 --R 40 --Q 200 --d $D_ALLE --aus "$L/kraft-n5-h0.3-Q200.json"
lauf cpu2 kq0-h0.3 ball --rolle kq0 --n 6 --h 0.3 --R 40 --Q $QS --xy "0,0;0.15,0;0.15,0.08660254;0.37,0.23;3,-2;-5.5,4.1" --aus "$L/kq0-h0.3-Q{Q}.json"
echo "spur cpu2 fertig $(date --iso-8601=seconds)" > $L/fertig-cpu2.txt
