#!/bin/bash
# QBALL-DOPPELSPALT-1, Rauchtest 3a (vor dem Einfrieren, Fremdwerte d = 2R, v = 0,6): Doppel- und Dreifachspalt, Teilstapel.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/rauch/test3/lauf
mkdir -p $O
cd $D || exit 1
bash $K p4000a qds-r3a1 $D/code/qds.py lauf --out $O/q2.json --profil $D/rauch/profil.json --modell qball --omega 0.9 --h 0.25 --nspalt 2 --d_art R --d 2 --konfig A,AB --ny 41 --vs 0.6 > $O/q2.log 2>&1
echo "r3a1 rc=$? $(date --iso-8601=seconds)" >> $D/rauch/rauch3.log
bash $K p4000a qds-r3a2 $D/code/qds.py lauf --out $O/q3.json --profil $D/rauch/profil.json --modell qball --omega 0.9 --h 0.25 --nspalt 3 --d_art R --d 2 --konfig A,B,AB,AC,ABC --chunk 2 --ny 41 --vs 0.6 > $O/q3.log 2>&1
echo "r3a2 rc=$? $(date --iso-8601=seconds)" >> $D/rauch/rauch3.log
