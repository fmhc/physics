#!/bin/bash
# TT-GLAS-2 NACHTRAG (nach dem Einfrieren, beschreibend, geht in kein Urteil ein), Spur p4000a: weitere Saaten N = 512
# (5 bis 10), eingefrorener Code (dk.py), alle Varianten mit Linearitaet. Ausgabe in nachtrag/.
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
lauf tg2-nt512-a code/dk.py --N 512 --saaten 5,6,7 --out nachtrag/dk
lauf tg2-nt512-b code/dk.py --N 512 --saaten 8,9,10 --out nachtrag/dk
echo "nachtrag A2 ende $(date -u +%H:%M:%S)"
