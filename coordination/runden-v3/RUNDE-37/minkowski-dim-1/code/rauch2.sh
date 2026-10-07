#!/bin/bash
# MINKOWSKI-DIM-1: Rauchtest R2 = Probelauf der ganzen Kette mit kleinen Einstellungen (k-Gitter 6^3/4^3, Glas Saat 901,
# Kaestchen nur drei Groessen, Sierpinski-Tetraeder Stufe 6 statt 10, Beutel auf st:6 statt st:7), danach die Auswertung.
# Gelesen werden nur rc, Laufzeiten und Schluessel, keine Werte zu MD0 bis MD4. Einmalig von Hand gestartet.
B=/home/fmh/fmhc-physics-remote/minkowski-dim-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code
R=$B/rauch2
mkdir -p $R
cd $B || exit 1
kette_cpu2() {
  bash $K cpu2 md-r6 $C/md.py takt --netze V,C15,A15,glas-N512-s901 --klein --out $R/takt-klein.json > $R/r6.log 2>&1
}
kette_cpu3() {
  bash $K cpu3 md-r7 $C/md.py kasten --klein --out $R/kasten.json > $R/r7.log 2>&1
  bash $K cpu3 md-r8 $C/md.py kubisch --out $R/kubisch.json > $R/r8.log 2>&1
}
kette_cpu4() {
  bash $K cpu4 md-r9 $C/bagdim_st.py spektrum st:3 $R/s_st3.json > $R/r9.log 2>&1
  bash $K cpu4 md-r10 $C/bagdim_st.py spektrum st:4 $R/s_st4.json > $R/r10.log 2>&1
  bash $K cpu4 md-r11 $C/bagdim_st.py beutel st:6 $R/b_st_x.json --q0 20 --periode 9.797958971132712 --k0 0 --k1 20 --ra 1.2 --rb 0.3037 --dq-k 12 --budget 100 > $R/r11.log 2>&1
}
kette_cpu2 > $R/kette-cpu2.log 2>&1 &
kette_cpu3 > $R/kette-cpu3.log 2>&1 &
kette_cpu4 > $R/kette-cpu4.log 2>&1 &
wait
bash $K cpu2 md-r12 $C/md.py auswertung --ordner $R --out $R/auswertung.json > $R/r12.log 2>&1
echo "rauch2 fertig $(date --iso-8601=seconds)" > $R/rauch2-fertig.txt
