#!/bin/bash
# MINKOWSKI-DIM-1: Rauchtests r1 bis r4 (nur Schluessel, Laufzeiten, Bauproben; keine Ergebniswerte zu MD0 bis MD4).
# Einmalig von Hand gestartet; kein Dienst, kein Timer. Graphen/Netze/Raster der Rauchtests kommen in keinem echten Lauf vor.
B=/home/fmh/fmhc-physics-remote/minkowski-dim-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code
R=$B/rauch
cd $B || exit 1
kette_cpu2() {
  bash $K cpu2 md-r1 $C/md.py takt --netze V,S,C15,A15,glas-N128-s901 --rauch --out $R/r1.json > $R/r1.log 2>&1
  bash $K cpu2 md-r4 $C/bagdim_st.py beutel st:7 $R/r4.json --q0 100000 --k0 0 --k1 0 --ra 1.2 --rb 0.3037 --budget 110 > $R/r4.log 2>&1
}
kette_cpu3() {
  bash $K cpu3 md-r2 $C/md.py kasten --rauch --out $R/r2.json > $R/r2.log 2>&1
  bash $K cpu3 md-r5 $C/md.py kubisch --rauch --out $R/r5.json > $R/r5.log 2>&1
}
kette_cpu4() {
  bash $K cpu4 md-r3s $C/bagdim_st.py spektrum st:3 $R/r3s.json > $R/r3s.log 2>&1
  bash $K cpu4 md-r3b $C/bagdim_st.py beutel st:4 $R/r3b.json --q0 40 --periode 9.797958971132712 --k0 0 --k1 2 --ra 1.2 --rb 0.3037 --pruef-k alle --flach-k 1 --dq-k 2 --budget 100 > $R/r3b.log 2>&1
}
kette_cpu2 > $R/kette-cpu2.log 2>&1 &
kette_cpu3 > $R/kette-cpu3.log 2>&1 &
kette_cpu4 > $R/kette-cpu4.log 2>&1 &
wait
echo "rauch fertig $(date --iso-8601=seconds)" > $R/rauch-fertig.txt
