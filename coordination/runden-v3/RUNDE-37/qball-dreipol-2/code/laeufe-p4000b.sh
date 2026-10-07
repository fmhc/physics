#!/bin/bash
# QBALL-DREIPOL-2, Hauptlaeufe Spur p4000b (eingefrorener Code; PLAN.md Abschnitt 7). Laeuft auf der .69.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-2/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-2/lauf
cd /home/fmh/fmhc-physics-remote/qball-dreipol-2 || exit 1
bash $K p4000b dp2-B-p01 $P/dreipol2.py B --out $O/B_p01.json --g4=0.1 --Q1 2500 --N 80 --L 48 --nfluss 60000 \
  --wand_fluss 420 > $O/B_p01.log 2>&1
echo "B_p01 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
bash $K p4000b dp2-C-m01 $P/dreipol2.py C --out $O/C_m01.json --g4=-0.1 --Q1 60 --saaten 1,2,3,4 > $O/C_m01.log 2>&1
echo "C_m01 rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
bash $K p4000b dp2-S $P/dreipol2.py S --out $O/S.json --Q1 60 --g4liste 0.1,-0.1 > $O/S.log 2>&1
echo "S rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
bash $K p4000b dp2-B-m01-fein $P/dreipol2.py B --out $O/B_m01_fein.json --g4=-0.1 --Q1 2500 --N 96 --L 48 \
  --nfluss 60000 --wand_fluss 400 > $O/B_m01_fein.log 2>&1
echo "B_m01_fein rc=$? $(date --iso-8601=seconds)" >> $O/laeufe-p4000b.log
