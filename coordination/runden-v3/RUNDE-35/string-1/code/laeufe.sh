#!/bin/bash
# STRING-1 (Runde 35): echte Laeufe nach PLAN.md (eingefroren), nacheinander ueber kleintest.sh, nur Spur cpu6.
# Aufruf auf der .69: cd /home/fmh/fmhc-physics-remote/runde35-string && setsid nohup bash code/laeufe.sh > lauf/laeufe.log 2>&1 < /dev/null &
# S6: Wurm mit Paarbildung, mu/T = 5,673 (= 3/xi aus dem Rauchlauf, PLAN.md Abschnitt 5).
set -u
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd /home/fmh/fmhc-physics-remote/runde35-string || exit 1
D=lauf
MUT6=5.673
Z=240   # Sekunden je Lauf (Probezeit; Einlauf 10 % davon), 50 Bloecke
run() { local name=$1; shift; bash "$K" cpu6 "r35s-$name" code/string_mc.py "$@" > "$D/$name.log" 2>&1; echo "$name rc=$? $(date --iso-8601=seconds)" >> $D/laeufe_status.txt; }
echo "start $(date --iso-8601=seconds)" > $D/laeufe_status.txt
run kette kette $D/kette
run gauss gauss $D/gauss
run w2k25g wurm 2 128 2.5 1001 $Z 50 0.7 $D/w_d2_L128_K2.5
run w2k25k wurm 2 64 2.5 1002 $Z 50 0.7 $D/w_d2_L64_K2.5
run w2k05g wurm 2 128 0.5 1003 $Z 50 0 $D/w_d2_L128_K0.5
run w2k05k wurm 2 64 0.5 1004 $Z 50 0 $D/w_d2_L64_K0.5
run w3k45g wurm 3 32 4.5 1005 $Z 50 1.9 $D/w_d3_L32_K4.5
run w3k45k wurm 3 24 4.5 1006 $Z 50 1.9 $D/w_d3_L24_K4.5
run w3k15g wurm 3 32 1.5 1007 $Z 50 0 $D/w_d3_L32_K1.5
run w3k15k wurm 3 24 1.5 1008 $Z 50 0 $D/w_d3_L24_K1.5
run v2k25 villain 2 64 2.5 1009 $Z 50 2.5 - 1000 $D/v_d2_L64_K2.5
run v3k15 villain 3 24 1.5 1010 $Z 50 1.5 - 2000 $D/v_d3_L24_K1.5
bash "$K" cpu6 r35s-ausw1 code/auswertung.py $D $D/auswertung_zwischen.json 128 64 32 24 64 24 > $D/auswertung_zwischen.log 2>&1
echo "auswertung1 rc=$? $(date --iso-8601=seconds)" >> $D/laeufe_status.txt
if [ -n "$MUT6" ]; then
  run wp3k45 wurm_paare 3 24 4.5 "$MUT6" 1011 $Z 50 1.9 6 $D/wp_d3_L24_K4.5
fi
run v2k05 villain 2 64 0.5 1012 $Z 50 1.0 - 3000 $D/v_d2_L64_K0.5
run v3k45 villain 3 24 4.5 1013 $Z 50 3.14159 - 1000 $D/v_d3_L24_K4.5
bash "$K" cpu6 r35s-ausw2 code/auswertung.py $D $D/auswertung.json 128 64 32 24 64 24 > $D/auswertung.log 2>&1
echo "auswertung rc=$? $(date --iso-8601=seconds)" >> $D/laeufe_status.txt
echo "fertig $(date --iso-8601=seconds)" >> $D/laeufe_status.txt
