#!/bin/bash
# GLAS-STRAHLUNG-1, einmalige Laufkette (Spur p4000b): N = 256 Saaten 5,6,7,8, dann N = 512 Saaten 2 4 6 (je ein Lauf).
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 09:05:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" p4000b "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf gs-B256 code/gs.py netz --N 256 --saaten 5,6,7,8 --out lauf/gs
for s in 2 4 6; do
  lauf gs-B512-$s code/gs.py netz --N 512 --saaten $s --out lauf/gs
done
echo "kette p4000b ende $(date -u +%H:%M:%S)"
