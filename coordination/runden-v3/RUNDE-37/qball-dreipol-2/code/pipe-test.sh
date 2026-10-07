#!/bin/bash
# QBALL-DREIPOL-2, Leitungstest (vor dem Einfrieren): alle Modi mit fremden Werten (Q1 = 25 bzw. 300, wenige
# Schritte, T = 2) und die Auswertung. Prueft nur, dass der Weg durchlaeuft; die Zahlen sind keine Hauptwerte.
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=/home/fmh/fmhc-physics-remote/qball-dreipol-2/code
O=/home/fmh/fmhc-physics-remote/qball-dreipol-2/rauch/pipe
mkdir -p $O
cd /home/fmh/fmhc-physics-remote/qball-dreipol-2 || exit 1
bash $K p4000a dp2-pA $P/dreipol2.py A --out $O/A.json --Q1 25 --nmax_nachbau 30 --nmax_ref 30 --nmax_st 20 \
  --wand_st 10 > $O/A.log 2>&1
echo "A rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
for t in m01:-0.1 p01:0.1; do
  bash $K p4000a dp2-pB-${t%%:*} $P/dreipol2.py B --out $O/B_${t%%:*}.json --N 32 --L 48 --Q1 300 --g4=${t##*:} \
    --nfluss 20 --nmax_ball 30 --wand_fluss 20 > $O/B_${t%%:*}.log 2>&1
  echo "B_${t%%:*} rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
done
bash $K p4000a dp2-pS $P/dreipol2.py S --out $O/S.json --Q1 25 --g4liste 0.1,-0.1 > $O/S.log 2>&1
echo "S rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
for t in m01:-0.1 p01:0.1; do
  bash $K p4000a dp2-pC-${t%%:*} $P/dreipol2.py C --out $O/C_${t%%:*}.json --Q1 25 --g4=${t##*:} --T 2 \
    --saaten 1,2,3,4 --schnapp 0,1,2 > $O/C_${t%%:*}.log 2>&1
  echo "C_${t%%:*} rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
done
bash $K p4000a dp2-paw $P/auswertung2.py $O > $O/aw.log 2>&1
echo "aw rc=$? $(date --iso-8601=seconds)" >> $O/pipe.log
