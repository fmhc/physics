#!/bin/bash
# DANZER-TT-1, Laufkette cpu10 (PLAN Abschnitt 5): 3/2 Saat 2, dichte Gegenprobe, Gitter Lk = 2, Zitter-Kontrolle 3/2.
# Kein neuer Lauf nach SCHLUSS (10:15:00 UTC).
R=/home/fmh/fmhc-physics-remote/danzer-tt-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -d '2026-10-05 10:15:00 UTC' +%s)
cd $R
lauf() {
  local n=$1; shift
  if [ "$(date +%s)" -ge "$SCHLUSS" ]; then echo "$n nicht gestartet (SCHLUSS) $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu10.log; return; fi
  bash $K cpu10 dtt-$n code/dtt.py "$@" > $R/lauf/$n.log 2>&1
  echo "$n rc=$? $(date --iso-8601=seconds)" >> $R/lauf/kette-cpu10.log
}
lauf L22a netz --ordnung 3/2 --saaten 2 --ridx 0-6 --eps 1e-3 --dn2 --affin --out lauf/n32-s2-a.json
lauf L22b netz --ordnung 3/2 --saaten 2 --ridx 7-12 --eps 1e-3 --out lauf/n32-s2-b.json
lauf L22c netz --ordnung 3/2 --saaten 2 --ridx 0-6 --eps 2e-3 --out lauf/n32-s2-c.json
lauf L22d netz --ordnung 3/2 --saaten 2 --ridx 7-12 --eps 2e-3 --out lauf/n32-s2-d.json
lauf L30 netz --ordnung 3/2 --saaten 0 --weg dicht --ridx 0 --eps 1e-3 --out lauf/n32-s0-dicht.json
lauf L31a netz --ordnung 3/2 --saaten 0 --bz 2 --bz-teil 0/3 --out lauf/n32-s0-bz-a.json
lauf L31b netz --ordnung 3/2 --saaten 0 --bz 2 --bz-teil 1/3 --out lauf/n32-s0-bz-b.json
lauf L31c netz --ordnung 3/2 --saaten 0 --bz 2 --bz-teil 2/3 --out lauf/n32-s0-bz-c.json
lauf L32a netz --ordnung 3/2 --saaten 0 --zitter 1 --ridx 0-6 --eps 1e-3 --dn2 --out lauf/n32-z1-a.json
lauf L32b netz --ordnung 3/2 --saaten 0 --zitter 1 --ridx 7-12 --eps 1e-3 --out lauf/n32-z1-b.json
echo "kette cpu10 ende $(date --iso-8601=seconds)" > $R/lauf/kette-cpu10.fertig
