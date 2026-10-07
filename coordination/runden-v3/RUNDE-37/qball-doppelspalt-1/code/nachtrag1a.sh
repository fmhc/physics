#!/bin/bash
# QBALL-DOPPELSPALT-1, Nachtrag N1 (festgelegt 06:09 CEST vor jedem W-Ergebnis; beschreibend, kein Urteil):
# Konvergenz-Stichprobe fuer den Zusatzarm W, Doppelspalt d = R: 40 Zwischen-y (alle v) und h = 0,125 (nur v = 0,45).
# Spur p4000a, omega = 0.8, eingefrorener Code. Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/lauf
P=$O/profil.json
cd $D || exit 1
bash $K p4000a qds-w3q2-0.8-1R-n81 $D/code/qds.py lauf --out $O/w3q2-0.8-1R-n81.json --profil $P --omega 0.8 --h 0.25 --ny 81 --nur_ungerade 1 --vs 0.2,0.3,0.45 --wf 3 --modell qball --nspalt 2 --d_art R --d 1 --konfig A,AB > $O/w3q2-0.8-1R-n81.log 2>&1
echo "w3q2-0.8-1R-n81 rc=$? $(date --iso-8601=seconds)" >> $O/nachtrag1a.log
bash $K p4000a qds-w3q2-0.8-1R-h0125 $D/code/qds.py lauf --out $O/w3q2-0.8-1R-h0125.json --profil $P --omega 0.8 --h 0.125 --ny 41 --vs 0.45 --wf 3 --modell qball --nspalt 2 --d_art R --d 1 --konfig A,AB --chunk 1 > $O/w3q2-0.8-1R-h0125.log 2>&1
echo "w3q2-0.8-1R-h0125 rc=$? $(date --iso-8601=seconds)" >> $O/nachtrag1a.log
