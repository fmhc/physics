#!/bin/bash
# HOEHE-ISOTROP-1, Laufkette p4000a (PLAN Abschnitt 10): H1 mitte, H3 strahlen 0, H5 null
R=/home/fmh/fmhc-physics-remote/hoehe-isotrop-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
bash $K p4000a hi-H1 code/hi.py mitte lauf/mitte.json alt/kammer1.json alt/nachtrag-beta.json > $R/lauf/H1.log 2>&1
bash $K p4000a hi-H3 code/hi.py strahlen 0 lauf/f43-0.json > $R/lauf/H3.log 2>&1
bash $K p4000a hi-H5 code/hi.py null lauf/null.json > $R/lauf/H5.log 2>&1
echo "kette p4000a ende $(date --iso-8601=seconds)" > $R/lauf/kette-p4000a.fertig
