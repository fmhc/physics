#!/bin/bash
# QBALL-DOPPELSPALT-1, Stufe 0 (eingefrorener Code; PLAN Abschn. 2 und 7): Bilanz und Ruhetest auf p4000a. Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/lauf
cd $D || exit 1
bash $K p4000a qds-bilanz $D/code/qds.py bilanz --out $O/bilanz.json --d2 $D/eingabe/d2.json > $O/bilanz.log 2>&1
echo "bilanz rc=$? $(date --iso-8601=seconds)" >> $O/stufe0.log
bash $K p4000a qds-ruhe $D/code/qds.py ruhe --out $O/ruhe.json --profil $O/profil.json --T 200 --hs 0.25,0.125 --omegas 0.8,0.9 > $O/ruhe.log 2>&1
echo "ruhe rc=$? $(date --iso-8601=seconds)" >> $O/stufe0.log
