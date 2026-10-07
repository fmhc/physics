#!/bin/bash
# GLAS-STRAHLUNG-1, einmalige Laufkette D (Spur cpu7): N = 128 Saaten 5-8, kabs-Kontrolle.
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 09:05:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu7 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf gs-C128b code/gs.py netz --N 128 --saaten 5,6,7,8 --out lauf/gs
lauf gs-K128 code/gs.py netz --N 128 --saaten 1 --kabs 0.02 --out lauf/kontrolle/k002
echo "kette cpu7 ende $(date -u +%H:%M:%S)"
