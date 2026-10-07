#!/bin/bash
# SKALAR-MISCH-1, Laufkette Spur cpu6 (S1, dann K1). Einmalig von Hand gestartet, kein Dienst.
cd /home/fmh/fmhc-physics-remote/skalar-misch-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu6 sm-s1 code/smi.py suche --fam F1 --out lauf/suche-F1.json > lauf/s1.log 2>&1; echo "s1 rc=$?" >> lauf/kette-cpu6.txt
bash $K cpu6 sm-k1 code/smi.py karte --out lauf/karte.json > lauf/k1.log 2>&1; echo "k1 rc=$?" >> lauf/kette-cpu6.txt
