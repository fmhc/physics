#!/bin/bash
# DANZER-TT-1, Nachlauf cpu8 (nach dem Einfrieren; ERGEBNIS Selbstanzeige "Nachlauf"): zweiter Teil des Ersatzes fuer
# L23a (3/2 Saat 3, Richtungen 3-6 bei |k| = 1e-3), nach dem Ende der Kette cpu8. Code unveraendert.
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
until [ -f $R/lauf/kette-cpu8.fertig ]; do sleep 10; done
bash $K cpu8 dtt-N2 code/dtt.py netz --ordnung 3/2 --saaten 3 --ridx 3-6 --eps 1e-3 --out lauf/n32-s3-a2.json > $R/lauf/N2.log 2>&1
echo "N2 rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-nachlauf-cpu8.log
echo "nachlauf cpu8 ende $(date --iso-8601=seconds)" > $R/lauf/kette-nachlauf-cpu8.fertig
