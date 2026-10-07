#!/bin/bash
# TT-GLAS-1 NACHTRAG (nach dem Einfrieren, beschreibend), einmalige Laufkette Spur cpu3. Jeder Lauf ueber kleintest.sh.
# Schlusszeit: nach 2026-10-05 03:55:00 UTC (05:55 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-1 || exit 1
mkdir -p nachtrag/n512
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 03:55:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu3 "$name" "$@" > "nachtrag/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tg-nt-g32 code/nachtrag_gewicht.py --N 32 --saaten 1,2,3,4,5,6,7,8,9,10,11,12 --arten J1,JV,JinvV --out nachtrag/gewicht-N32.json
lauf tg-nt-g64 code/nachtrag_gewicht.py --N 64 --saaten 1,2,3,4,5,6,7,8,9,10,11,12 --arten JV,JinvV --out nachtrag/gewicht-N64.json
lauf tg-nt-512a code/tg.py netz --N 512 --saaten 1 --ridx 0,1 --out nachtrag/n512/netz-N512-s1-a.json
lauf tg-nt-512c code/tg.py netz --N 512 --saaten 1 --ridx 3,5 --out nachtrag/n512/netz-N512-s1-c.json
lauf tg-nt-512e code/tg.py netz --N 512 --saaten 1 --ridx 9,10 --out nachtrag/n512/netz-N512-s1-e.json
echo "nachtrag cpu3 ende $(date -u +%H:%M:%S)"
