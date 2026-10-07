#!/bin/bash
# TT-GLAS-2, Nachholung geplanter Laeufe (PLAN Abschn. 4: N = 1024, Saaten 1 und 3), Spur p4000b statt p4000a:
# auf p4000a brach tg2-dk1024-s1-r0 mit CUDA-Speichermangel ab (05:50:13 UTC, rc = 1). Eingefrorener Code, gleiche Aufrufe.
# Schlusszeit: nach 2026-10-05 06:50:00 UTC (08:50 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 06:50:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" p4000b "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
for s in 1 3; do
  lauf tg2-dk1024-s$s-r0-p4000b code/dk.py --N 1024 --saaten $s --ridx 0-6 --varianten a --ohne_lin --out lauf/dk-N1024-s$s-r0.json
  lauf tg2-dk1024-s$s-r1-p4000b code/dk.py --N 1024 --saaten $s --ridx 7-12 --varianten a --ohne_lin --out lauf/dk-N1024-s$s-r1.json
done
echo "nachhol B ende $(date -u +%H:%M:%S)"
