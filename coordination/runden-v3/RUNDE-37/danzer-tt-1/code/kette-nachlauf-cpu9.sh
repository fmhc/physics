#!/bin/bash
# DANZER-TT-1, Nachlauf cpu9 (nach dem Einfrieren; ERGEBNIS Selbstanzeige "Nachlauf").
# Grund: L23a (3/2 Saat 3, Richtungen 0-6) laeuft wegen hoeherer Last ueber 600 s; Saat 4 (L24a-d) haette dasselbe Risiko
# und spaeter geendet. Die Kette cpu9 wurde vor L21c beendet; hier laufen L21c und L21d mit denselben Argumenten, dann der
# erste Teil des Ersatzes fuer L23a. Code unveraendert (dtt.py eingefroren).
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
lauf() {
  local n=$1; shift
  bash $K cpu9 dtt-$n code/dtt.py "$@" > $R/lauf/$n.log 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-nachlauf-cpu9.log
}
lauf L21c netz --ordnung 3/2 --saaten 1 --ridx 0-6 --eps 2e-3 --out lauf/n32-s1-c.json
lauf L21d netz --ordnung 3/2 --saaten 1 --ridx 7-12 --eps 2e-3 --out lauf/n32-s1-d.json
lauf N1 netz --ordnung 3/2 --saaten 3 --ridx 0-2 --eps 1e-3 --dn2 --affin --out lauf/n32-s3-a1.json
echo "nachlauf cpu9 ende $(date --iso-8601=seconds)" > $R/lauf/kette-nachlauf-cpu9.fertig
