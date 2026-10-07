#!/bin/bash
# RUECKFLUSS-INFO-1: Kette Spur p4000b (L4a, L4b), je Lauf ein kleintest.sh-Aufruf
R=/home/fmh/fmhc-physics-remote/runde45-rueckfluss-info
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
O=$R/lauf
cd $R/code || exit 1
bash $K p4000b ri-l4a rueckfluss_info.py --modus leiter --N 160 --sigma 4 --W '2*pi' --saaten 2 --saatbasis 49000 --schritte 200 --out $O/haupt_L4a.json > $O/haupt_L4a.log 2>&1
bash $K p4000b ri-l4b rueckfluss_info.py --modus leiter --N 160 --sigma 4 --W '2*pi' --saaten 2 --saatbasis 49010 --schritte 200 --out $O/haupt_L4b.json > $O/haupt_L4b.log 2>&1
