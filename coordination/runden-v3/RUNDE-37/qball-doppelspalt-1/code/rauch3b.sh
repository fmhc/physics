#!/bin/bash
# QBALL-DOPPELSPALT-1, Rauchtest 3b (vor dem Einfrieren, Fremdwerte d = 2R, v = 0,6): linearer Arm, Dreifachspalt.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/rauch/test3/lauf
mkdir -p $O
cd $D || exit 1
bash $K p4000b qds-r3b1 $D/code/qds.py lauf --out $O/l3.json --profil $D/rauch/profil.json --modell lin --omega 0.9 --h 0.25 --nspalt 3 --d_art R --d 2 --konfig A,B,AB,AC,ABC --ny 41 --vs 0.6 > $O/l3.log 2>&1
echo "r3b1 rc=$? $(date --iso-8601=seconds)" >> $D/rauch/rauch3.log
