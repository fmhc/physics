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
lauf cpu radial radial --Q $QS --dr 0.01 --aus $L/radial.json
for h in 0.4 0.3 0.2; do lauf cpu netz-h$h netz --h $h --R 40 --aus $L/netz-h$h.json; done
for h in 0.4 0.3 0.2; do lauf cpu bind-n6-h$h ball --rolle bindung --n 6 --h $h --R 40 --Q $QS --d 0 --aus "$L/bind-n6-h$h-Q{Q}.json"; done
lauf cpu kq0-h0.4 ball --rolle kq0 --n 6 --h 0.4 --R 40 --Q $QS --xy "0,0;0.2,0;0.2,0.11547005;0.37,0.23;3,-2;-5.5,4.1" --aus "$L/kq0-h0.4-Q{Q}.json"
lauf cpu dq-n6-h0.3 ball --rolle dEdQ --n 6 --h 0.3 --R 40 --Q 199.8,200.2 --d 0 --aus "$L/dq-n6-h0.3-Q{Q}.json"
lauf cpu dq-n5-h0.3 ball --rolle dEdQ --n 5 --h 0.3 --R 40 --Q 199.8,200.2 --d 0 --aus "$L/dq-n5-h0.3-Q{Q}.json"
lauf cpu rand-n6 ball --rolle rand --n 6 --h 0.4 --R 48 --Q 400 --d 0 --aus "$L/rand-n6-h0.4-Q400.json"
lauf cpu rand-n5 ball --rolle rand --n 5 --h 0.4 --R 48 --Q 400 --d 0,19.2 --aus "$L/rand-n5-h0.4-Q400.json"
lauf cpu rand-n7 ball --rolle rand --n 7 --h 0.4 --R 48 --Q 400 --d 0,19.2 --aus "$L/rand-n7-h0.4-Q400.json"
echo "spur cpu fertig $(date --iso-8601=seconds)" > $L/fertig-cpu.txt
