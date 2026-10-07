#!/bin/bash
# SKALAR-MISCH-1, Laufkette Spur cpu5 (T1, dann S2). Einmalig von Hand gestartet, kein Dienst.
cd /home/fmh/fmhc-physics-remote/skalar-misch-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu5 sm-t1 code/smi.py tabelle --out lauf/tabelle.json > lauf/t1.log 2>&1; echo "t1 rc=$?" >> lauf/kette-cpu5.txt
bash $K cpu5 sm-s2 code/smi.py suche --fam F2 --out lauf/suche-F2.json > lauf/s2.log 2>&1; echo "s2 rc=$?" >> lauf/kette-cpu5.txt
