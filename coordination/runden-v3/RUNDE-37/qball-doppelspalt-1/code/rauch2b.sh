#!/bin/bash
# QBALL-DOPPELSPALT-1, Rauchtest 2b (vor dem Einfrieren, Fremdwerte bzw. verkuerzte Laufwege). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/rauch
cd $D || exit 1
bash $K p4000b qds-r2b1 $D/code/qds.py lauf --out $O/r2b1.json --profil $O/profil.json --modell qball --omega 0.8 --h 0.125 --nspalt 2 --d_art R --d 1 --konfig A,AB --ny 41 --vs 0.45 --weg 2 > $O/r2b1.log 2>&1
echo "r2b1 rc=$? $(date --iso-8601=seconds)" >> $O/rauch2b.log
bash $K p4000b qds-r2b2 $D/code/qds.py ruhe --out $O/r2b2.json --profil $O/profil.json --T 10 --hs 0.25,0.125 --omegas 0.9 > $O/r2b2.log 2>&1
echo "r2b2 rc=$? $(date --iso-8601=seconds)" >> $O/rauch2b.log
