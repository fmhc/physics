#!/bin/bash
# QBALL-DOPPELSPALT-1, Rauchtest 2a (vor dem Einfrieren, Fremdwerte bzw. verkuerzte Laufwege). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/rauch
cd $D || exit 1
bash $K p4000a qds-r2a1 $D/code/qds.py lauf --out $O/r2a1.json --profil $O/profil.json --modell qball --omega 0.8 --h 0.25 --nspalt 3 --d_art R --d 1 --konfig A,B,AB,AC,ABC --ny 41 --vs 0.45 --weg 4 > $O/r2a1.log 2>&1
echo "r2a1 rc=$? $(date --iso-8601=seconds)" >> $O/rauch2.log
bash $K p4000a qds-r2a2 $D/code/qds.py lauf --out $O/r2a2.json --profil $O/profil.json --modell lin --omega 0.8 --h 0.25 --nspalt 3 --d_art R --d 1 --konfig A,B,AB,AC,ABC --ny 41 --vs 0.45 --weg 4 > $O/r2a2.log 2>&1
echo "r2a2 rc=$? $(date --iso-8601=seconds)" >> $O/rauch2.log
bash $K p4000a qds-r2a3 $D/code/qds.py lauf --out $O/r2a3.json --profil $O/profil.json --modell qball --omega 0.8 --h 0.25 --nspalt 2 --d_art R --d 2 --konfig A,AB --ny 5 --vs 0.4 > $O/r2a3.log 2>&1
echo "r2a3 rc=$? $(date --iso-8601=seconds)" >> $O/rauch2.log
