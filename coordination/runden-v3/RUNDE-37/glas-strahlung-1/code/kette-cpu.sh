#!/bin/bash
# GLAS-STRAHLUNG-1, einmalige Laufkette C (Spur cpu): GS0 auf V, N = 128 Saaten 1-4, Quadratur-Kontrolle; danach AUS
# erst von Hand. Jeder Lauf ueber kleintest.sh (<= 600 s). Schlusszeit: nach 2026-10-05 09:05:00 UTC startet kein Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 09:05:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf gs-GV code/gs.py netz --N 0 --nt 10 --nphi 20 --out lauf/v.json
lauf gs-GV6 code/gs.py netz --N 0 --nt 6 --nphi 12 --out lauf/kontrolle/v-6x12.json
lauf gs-C128a code/gs.py netz --N 128 --saaten 1,2,3,4 --out lauf/gs
lauf gs-Q128 code/gs.py netz --N 128 --saaten 1 --nt 8 --nphi 16 --out lauf/kontrolle/q8x16
echo "kette cpu ende $(date -u +%H:%M:%S)"
