#!/bin/bash
# STRING-1 Rauchlaeufe Teil 3: Wurm mit Paarbildung (S6) pruefen, Probe d = 3, L = 24; Pruefung mit dem neuen Kern.
# Nur Spur cpu6, nacheinander. Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde35-string && setsid nohup bash code/rauch3.sh > rauch/rauch3.log 2>&1 < /dev/null &
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde35-string || exit 1
R=rauch
run() { local name=$1; shift; bash "$K" cpu6 "r35s-$name" code/string_mc.py "$@" > "$R/$name.log" 2>&1; }
run pruef3 pruef $R/pruef3
run pruefp pruef_paare $R/pruef_paare
run wp3 wurm_paare 3 24 4.5 5.673 301 60 40 1.9 6 $R/wp_d3_L24_K4.5
bash "$K" cpu6 r35s-ausw3 code/auswertung.py $R $R/auswertung3.json 64 32 24 16 32 16 > $R/auswertung3.log 2>&1
echo "rauch3 fertig $(date --iso-8601=seconds)" > $R/rauch3_fertig.txt
