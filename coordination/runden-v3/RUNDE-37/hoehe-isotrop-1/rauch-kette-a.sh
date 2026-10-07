#!/bin/bash
# HOEHE-ISOTROP-1, Rauch-Pfadtests Spur p4000a (PLAN Abschnitt 11): R2 mitte, R3 null --rauch, R4 gitter --rauch
R=/home/fmh/fmhc-physics-remote/hoehe-isotrop-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000a hi-R2 code/hi.py mitte rauch/r2-mitte.json alt/kammer1.json alt/nachtrag-beta.json > $R/rauch/R2.log 2>&1
bash $K p4000a hi-R3 code/hi.py null rauch/r3-null.json --rauch > $R/rauch/R3.log 2>&1
bash $K p4000a hi-R4 code/hi.py gitter rauch/r4-gitter.json --rauch > $R/rauch/R4.log 2>&1
echo "kette a ende $(date --iso-8601=seconds)" > $R/rauch/kette-a.fertig
