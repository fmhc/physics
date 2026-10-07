#!/bin/bash
# QBALL-DOPPELSPALT-1, Rauchtest 1 (vor dem Einfrieren): Energiebilanz und Profil. Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/rauch
cd $D || exit 1
bash $K p4000a qds-r1b $D/code/qds.py bilanz --out $O/bilanz.json --d2 $D/eingabe/d2.json > $O/bilanz.log 2>&1
echo "bilanz rc=$? $(date --iso-8601=seconds)" >> $O/rauch1.log
bash $K p4000a qds-r1p $D/code/qds.py profil --out $O/profil.json --wand 50 > $O/profil.log 2>&1
echo "profil rc=$? $(date --iso-8601=seconds)" >> $O/rauch1.log
