#!/bin/bash
# QBALL-DREIPOL-3, Nachtrag N1 nach Sicht (beschreibend): Feinabtastung mit Entmischungsregel. Laeuft auf der .69.
# Aufruf: laeufe-nachtrag.sh <spur> <dim> <Q-Liste> <name>
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-3/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-3/lauf/nachtrag
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-3 || exit 1
bash $K $1 dp3-N1-$4 $P/nachtrag3.py $O/$4.json $2 $3 110 300 > $O/$4.log 2>&1
echo "$4 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-nachtrag.log
