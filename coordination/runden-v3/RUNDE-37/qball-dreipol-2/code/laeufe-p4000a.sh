#!/bin/bash
# QBALL-DREIPOL-2, Hauptlaeufe Spur p4000a (eingefrorener Code; PLAN.md Abschnitt 7). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-2/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-2/lauf
cd /home/fmh/fmhc-physics-remote/qball-dreipol-2 || exit 1
bash $K p4000a dp2-A $P/dreipol2.py A --out $O/A.json --g4=-0.1 --Q1 60 --nmax_st 30000 --wand_st 45 > $O/A.log 2>&1
echo "A rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000a.log
bash $K p4000a dp2-B-m01 $P/dreipol2.py B --out $O/B_m01.json --g4=-0.1 --Q1 2500 --N 80 --L 48 --nfluss 60000 \
  --wand_fluss 420 > $O/B_m01.log 2>&1
echo "B_m01 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000a.log
bash $K p4000a dp2-C-p01 $P/dreipol2.py C --out $O/C_p01.json --g4=0.1 --Q1 60 --saaten 1,2,3,4 > $O/C_p01.log 2>&1
echo "C_p01 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000a.log
