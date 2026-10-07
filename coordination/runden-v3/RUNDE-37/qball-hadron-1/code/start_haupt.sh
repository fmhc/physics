#!/bin/bash
# QBALL-HADRON-1 Hauptlaeufe (.69). Zwei Ketten parallel (Spur cpu und Spur cpu7), danach Auswertung.
# Aufruf auf der .69: bash /home/fmh/fmhc-physics-remote/qball-hadron-1/code/start_haupt.sh
set -u
B=/home/fmh/fmhc-physics-remote/qball-hadron-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
W2=0.5200,0.5225,0.5250,0.5275,0.5300,0.5325,0.5350,0.5375,0.5400,0.5425,0.5450,0.5475,0.5500,0.5525,0.5550,0.5575,0.5600,0.5625,0.5650,0.5675,0.5700,0.5725,0.5750,0.5775,0.5800,0.5825,0.5850,0.5875,0.5900,0.5925,0.5950,0.5975,0.6000,0.6025,0.6050,0.6075,0.6100,0.6125,0.6150,0.6175,0.6200,0.6225,0.6250,0.6275,0.6300,0.6325,0.6350,0.6375,0.6400,0.6425,0.6450,0.6475,0.6500,0.6525,0.6550,0.6575,0.6600,0.6625,0.6650,0.6675,0.6700,0.6725,0.6750,0.6775,0.6800,0.6825,0.6850,0.6875,0.6900,0.6925,0.6950,0.6975,0.7000
mkdir -p $B/lauf
kette_cpu() {
  cd $B/rg1-kopie
  bash $K cpu qh1-rg1std $B/rg1-kopie/regge2d.py tabelle --h 0.01 --out $B/lauf/rg1-std-h001 > $B/lauf/rg1-std-h001.log 2>&1
  bash $K cpu qh1-rg1bahn $B/rg1-kopie/regge2d.py bahn --tabelle $B/lauf/rg1-std-h001/ergebnis.json --out $B/lauf/rg1-std-bahn > $B/lauf/rg1-std-bahn.log 2>&1
  bash $K cpu qh1-rg1dichtl3 $B/rg1-kopie/regge2d.py tabelle --h 0.005 --m 0,1,2,3,4 --w2 $W2 --ohne-nls --ohne-gitter --out $B/lauf/rg1-dicht-h0005 > $B/lauf/rg1-dicht-h0005.log 2>&1
  cd $B
  bash $K cpu qh1-d3b $B/code/festq.py --modus axi3 --m 0,1,2,3 --Q 5000,10000,30000 --h 0.15 --L_pro_R 2.2 --L_plus 15 --gtol_rel 1e-10 --out $B/lauf/d3b.json > $B/lauf/d3b.log 2>&1
}
kette_cpu7() {
  cd $B/rg1-kopie
  bash $K cpu7 qh1-rg1dicht $B/rg1-kopie/regge2d.py tabelle --h 0.01 --m 0,1,2,3,4 --w2 $W2 --ohne-nls --ohne-gitter --out $B/lauf/rg1-dicht-h001 > $B/lauf/rg1-dicht-h001.log 2>&1
  cd $B
  bash $K cpu7 qh1-b2d $B/code/festq.py --modus radial --D 2 --m 0,1,2,3,4 --Q 300,400,600,800,1000,1200,1400,2000,3000,5000,8000,12000 --h 0.05 --L_pro_R 1.4 --L_plus 30 --gtol_rel 1e-10 --out $B/lauf/b2d.json > $B/lauf/b2d.log 2>&1
  bash $K cpu7 qh1-d3a $B/code/festq.py --modus axi3 --m 0,1,2,3 --Q 500,1000,2000,3000 --h 0.15 --L_pro_R 2.2 --L_plus 15 --gtol_rel 1e-10 --out $B/lauf/d3a.json > $B/lauf/d3a.log 2>&1
  bash $K cpu7 qh1-d4 $B/code/festq.py --modus dop4 --mm 0:0,1:0,1:1,2:0 --Q 10000,30000,100000,300000 --h 0.2 --L_pro_R 2.2 --L_plus 15 --gtol_rel 1e-10 --out $B/lauf/d4.json > $B/lauf/d4.log 2>&1
}
kette_cpu & P1=$!
kette_cpu7 & P2=$!
wait $P1 $P2
cd $B
bash $K cpu qh1-ausw $B/code/auswertung.py --b2d $B/lauf/b2d.json --a2d $B/lauf/rg1-dicht-h001/ergebnis.json --a2d_l3 $B/lauf/rg1-dicht-h0005/ergebnis.json --rg1bahn $B/lauf/rg1-std-bahn/ergebnis.json --d3 $B/lauf/d3a.json,$B/lauf/d3b.json --d4 $B/lauf/d4.json --dl3 /home/fmh/fmhc-physics-remote/dim-leiter-qball-1/lauf/d3.json --dl4 /home/fmh/fmhc-physics-remote/dim-leiter-qball-1/lauf/d4.json --out $B/lauf/auswertung > $B/lauf/auswertung.log 2>&1
echo "fertig $(date --iso-8601=seconds)" > $B/lauf/FERTIG.txt
