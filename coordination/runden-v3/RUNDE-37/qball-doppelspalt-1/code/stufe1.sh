#!/bin/bash
# QBALL-DOPPELSPALT-1, Stufe 1 Kleintest (Karte: 1 omega, 2 d, 2 v, 21 y = 84 Laeufe; nur AB) auf p4000b. Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/qball-doppelspalt-1
O=$D/lauf-klein
mkdir -p $O
cd $D || exit 1
bash $K p4000b qds-klein1 $D/code/qds.py lauf --out $O/k-1R.json --profil $D/lauf/profil.json --modell qball --omega 0.8 --h 0.25 --nspalt 2 --d_art R --d 1 --konfig AB --ny 21 --vs 0.2,0.45 > $O/k-1R.log 2>&1
echo "k-1R rc=$? $(date --iso-8601=seconds)" >> $O/stufe1.log
bash $K p4000b qds-klein2 $D/code/qds.py lauf --out $O/k-fern.json --profil $D/lauf/profil.json --modell qball --omega 0.8 --h 0.25 --nspalt 2 --d_art fern --konfig AB --ny 21 --vs 0.2,0.45 > $O/k-fern.log 2>&1
echo "k-fern rc=$? $(date --iso-8601=seconds)" >> $O/stufe1.log
