#!/bin/bash
# STRING-1 Rauchlaeufe (kleine Gitter, kurze Zeiten), nacheinander ueber kleintest.sh, nur Spur cpu6.
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde35-string && nohup bash code/rauch.sh > rauch/rauch.log 2>&1 &
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde35-string || exit 1
R=rauch
run() { local name=$1; shift; bash "$K" cpu6 "r35s-$name" code/string_mc.py "$@" > "$R/$name.log" 2>&1; }
run pruef pruef $R/pruef
run gauss gauss $R/gauss
run w2k25 wurm 2 32 2.5 101 30 40 0 $R/w_d2_L32_K2.5
run w3k45 wurm 3 16 4.5 102 30 40 0 $R/w_d3_L16_K4.5
run w2k05 wurm 2 32 0.5 103 30 40 0 $R/w_d2_L32_K0.5
run w3k15 wurm 3 16 1.5 104 30 40 0 $R/w_d3_L16_K1.5
run v2k25 villain 2 32 2.5 105 30 40 2.5 - 500 $R/v_d2_L32_K2.5
run v3k15 villain 3 16 1.5 106 30 40 1.5 - 1000 $R/v_d3_L16_K1.5
echo "rauch fertig $(date --iso-8601=seconds)" > $R/rauch_fertig.txt
