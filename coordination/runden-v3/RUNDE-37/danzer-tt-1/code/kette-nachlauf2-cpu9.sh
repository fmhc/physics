#!/bin/bash
# DANZER-TT-1, Nachlauf 2 cpu9 (nach dem Einfrieren; ERGEBNIS Selbstanzeige "Nachlauf").
# L23a hat die 600 s doch eingehalten; der Ersatz (N1, N2) entfaellt. Saat 4 wird wie in kette-cpu9.sh gerechnet
# (L24a bis L24d, gleiche Argumente), aber auf cpu8, cpu9 und cpu10 verteilt. L21c laeuft aus kette-nachlauf-cpu9.sh.
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd $R
lauf() {
  local n=$1; shift
  bash $K cpu9 dtt-$n code/dtt.py "$@" > $R/lauf/$n.log 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-nachlauf2-cpu9.log
}
lauf L21d netz --ordnung 3/2 --saaten 1 --ridx 7-12 --eps 2e-3 --out lauf/n32-s1-d.json
lauf L24a netz --ordnung 3/2 --saaten 4 --ridx 0-6 --eps 1e-3 --dn2 --affin --out lauf/n32-s4-a.json
lauf L24d netz --ordnung 3/2 --saaten 4 --ridx 7-12 --eps 2e-3 --out lauf/n32-s4-d.json
echo "nachlauf2 cpu9 ende $(date --iso-8601=seconds)" > $R/lauf/kette-nachlauf2-cpu9.fertig
