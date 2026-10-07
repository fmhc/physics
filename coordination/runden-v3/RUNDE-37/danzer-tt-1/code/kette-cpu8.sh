#!/bin/bash
# DANZER-TT-1, Laufkette cpu8 (PLAN Abschnitt 5). Kein neuer Lauf nach SCHLUSS (10:15:00 UTC = 12:15 CEST).
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -d '2026-10-05 10:15:00 UTC' +%s)
cd $R
lauf() {  # lauf <name> <argumente ...>
  local n=$1; shift
  if [ "$(date +%s)" -ge "$SCHLUSS" ]; then echo "$n nicht gestartet (SCHLUSS) $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu8.log; return; fi
  bash $K cpu8 dtt-$n code/dtt.py "$@" > $R/lauf/$n.log 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu8.log
}
A="--ridx 0-12 --eps 1e-3,2e-3"
lauf L01 kontrolle --out lauf/kontrolle.json
lauf L02 netz --ordnung 1/1 --saaten 0,1,2,3,4,5,6,7 $A --dicht --wuerfel --affin --bz 8 --dn2 --out lauf/n11.json
lauf L03 netz --ordnung 1/1 --saaten 0 --zitter 1 $A --dicht --wuerfel --bz 8 --dn2 --out lauf/n11-z1.json
lauf L04 netz --ordnung 2/1 --saaten 0 $A --dicht --wuerfel --affin --bz 4 --dn2 --out lauf/n21-s0.json
lauf L05 netz --ordnung 2/1 --saaten 1,2 $A --wuerfel --affin --bz 4 --dn2 --out lauf/n21-s12.json
lauf L06 netz --ordnung 2/1 --saaten 3,4 $A --wuerfel --affin --bz 4 --dn2 --out lauf/n21-s34.json
lauf L07 netz --ordnung 2/1 --saaten 5,6 $A --wuerfel --affin --bz 4 --dn2 --out lauf/n21-s56.json
lauf L08 netz --ordnung 2/1 --saaten 7 $A --wuerfel --affin --bz 4 --dn2 --out lauf/n21-s7.json
lauf L09 netz --ordnung 2/1 --saaten 0 --zitter 1 $A --wuerfel --dn2 --out lauf/n21-z1.json
lauf L23a netz --ordnung 3/2 --saaten 3 --ridx 0-6 --eps 1e-3 --dn2 --affin --out lauf/n32-s3-a.json
lauf L23b netz --ordnung 3/2 --saaten 3 --ridx 7-12 --eps 1e-3 --out lauf/n32-s3-b.json
lauf L23c netz --ordnung 3/2 --saaten 3 --ridx 0-6 --eps 2e-3 --out lauf/n32-s3-c.json
lauf L23d netz --ordnung 3/2 --saaten 3 --ridx 7-12 --eps 2e-3 --out lauf/n32-s3-d.json
echo "kette cpu8 ende $(date --iso-8601=seconds)" > $R/lauf/kette-cpu8.fertig
