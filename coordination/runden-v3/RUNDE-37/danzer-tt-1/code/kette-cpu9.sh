#!/bin/bash
# DANZER-TT-1, Laufkette cpu9 (PLAN Abschnitt 5): 3/2 Saaten 0, 1, dann 4. Kein neuer Lauf nach SCHLUSS (10:15:00 UTC).
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -d '2026-10-05 10:15:00 UTC' +%s)
cd $R
lauf() {
  local n=$1; shift
  if [ "$(date +%s)" -ge "$SCHLUSS" ]; then echo "$n nicht gestartet (SCHLUSS) $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu9.log; return; fi
  bash $K cpu9 dtt-$n code/dtt.py "$@" > $R/lauf/$n.log 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu9.log
}
for s in 0 1 4; do
  lauf L2${s}a netz --ordnung 3/2 --saaten $s --ridx 0-6 --eps 1e-3 --dn2 --affin --out lauf/n32-s$s-a.json
  lauf L2${s}b netz --ordnung 3/2 --saaten $s --ridx 7-12 --eps 1e-3 --out lauf/n32-s$s-b.json
  lauf L2${s}c netz --ordnung 3/2 --saaten $s --ridx 0-6 --eps 2e-3 --out lauf/n32-s$s-c.json
  lauf L2${s}d netz --ordnung 3/2 --saaten $s --ridx 7-12 --eps 2e-3 --out lauf/n32-s$s-d.json
done
echo "kette cpu9 ende $(date --iso-8601=seconds)" > $R/lauf/kette-cpu9.fertig
