#!/bin/bash
# TT-GLAS-2 NACHTRAG (nach dem Einfrieren, beschreibend, geht in kein Urteil ein), Spur p4000a: weitere Saaten N = 1024,
# eingefrorener Code (dk.py), nur Variante a, ohne Linearitaet, je Netz zwei Laeufe. Ausgabe in nachtrag/.
# Schlusszeit: nach 2026-10-05 06:50:00 UTC (08:50 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
mkdir -p nachtrag
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 06:50:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" p4000a "$name" "$@" > "nachtrag/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
for s in 5 7; do
  lauf tg2-nt1024-s$s-r0 code/dk.py --N 1024 --saaten $s --ridx 0-6 --varianten a --ohne_lin --out nachtrag/dk-N1024-s$s-r0.json
  lauf tg2-nt1024-s$s-r1 code/dk.py --N 1024 --saaten $s --ridx 7-12 --varianten a --ohne_lin --out nachtrag/dk-N1024-s$s-r1.json
done
echo "nachtrag A ende $(date -u +%H:%M:%S)"
