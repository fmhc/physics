#!/bin/bash
# STRING-1 Rauchlaeufe Teil 2: Bias (Maximumsnorm) testen, Fehlerniveau auf den echten 3D-Groessen, Probe-Auswertung.
# Nur Spur cpu6, nacheinander. Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde35-string && nohup bash code/rauch2.sh > rauch/rauch2.log 2>&1 < /dev/null &
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde35-string || exit 1
R=rauch
run() { local name=$1; shift; bash "$K" cpu6 "r35s-$name" code/string_mc.py "$@" > "$R/$name.log" 2>&1; }
run pruef2 pruef $R/pruef2
run w3k45b wurm 3 24 4.5 201 60 40 1.9 $R/w_d3_L24_K4.5
run w2k25b wurm 2 64 2.5 202 60 40 0.7 $R/w_d2_L64_K2.5
run w3k15g wurm 3 24 1.5 203 60 40 0 $R/w_d3_L24_K1.5
bash "$K" cpu6 r35s-ausw code/auswertung.py $R $R/auswertung.json 64 32 24 16 32 16 > $R/auswertung.log 2>&1
echo "rauch2 fertig $(date --iso-8601=seconds)" > $R/rauch2_fertig.txt
