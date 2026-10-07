#!/bin/bash
# QBALL-DOPPELSPALT-1, Stufen 2 und 3 (eingefrorener Code; PLAN Abschn. 7), Spur p4000a, omega = 0.8. Laeuft auf der .69.
# Stufe 2: Doppelspalt A, AB, d = R, 1,5R, 2R + 4/kappa, 3R; Stufe 3: Dreifachspalt d = R, 1,5R, Ball, dann linear.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/lauf
P=$O/profil.json
cd $D || exit 1
lauf() { local n=$1; shift; bash $K p4000a qds-$n $D/code/qds.py lauf --out $O/$n.json --profil $P --omega 0.8 --h 0.25 --ny 41 --vs 0.2,0.3,0.45 "$@" > $O/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $O/stufe23a.log; }
lauf q2-0.8-1R --modell qball --nspalt 2 --d_art R --d 1 --konfig A,AB
lauf q2-0.8-1.5R --modell qball --nspalt 2 --d_art R --d 1.5 --konfig A,AB
lauf q2-0.8-fern --modell qball --nspalt 2 --d_art fern --konfig A,AB
lauf q2-0.8-3R --modell qball --nspalt 2 --d_art R --d 3 --konfig A,AB
lauf q3-0.8-1R --modell qball --nspalt 3 --d_art R --d 1 --konfig A,B,AB,AC,ABC
lauf q3-0.8-1.5R --modell qball --nspalt 3 --d_art R --d 1.5 --konfig A,B,AB,AC,ABC
lauf l3-0.8-1R --modell lin --nspalt 3 --d_art R --d 1 --konfig A,B,AB,AC,ABC
lauf l3-0.8-1.5R --modell lin --nspalt 3 --d_art R --d 1.5 --konfig A,B,AB,AC,ABC
