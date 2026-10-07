#!/bin/bash
# TT-GLAS-1 NACHTRAG (nach dem Einfrieren, beschreibend), einmalige Laufkette Spur cpu4. Jeder Lauf ueber kleintest.sh.
# Schlusszeit: nach 2026-10-05 03:55:00 UTC (05:55 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-1 || exit 1
mkdir -p nachtrag/n512
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 03:55:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu4 "$name" "$@" > "nachtrag/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tg-nt-g128 code/nachtrag_gewicht.py --N 128 --saaten 1,2,3,4,5,6 --arten JV,JinvV --out nachtrag/gewicht-N128.json
lauf tg-nt-512b code/tg.py netz --N 512 --saaten 1 --ridx 2,4 --out nachtrag/n512/netz-N512-s1-b.json
lauf tg-nt-512d code/tg.py netz --N 512 --saaten 1 --ridx 6,7,8 --out nachtrag/n512/netz-N512-s1-d.json
lauf tg-nt-512f code/tg.py netz --N 512 --saaten 1 --ridx 11,12 --out nachtrag/n512/netz-N512-s1-f.json
echo "nachtrag cpu4 ende $(date -u +%H:%M:%S)"
