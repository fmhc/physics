#!/bin/bash
# GLAS-STRAHLUNG-1, einmalige Laufkette (Spur p4000a): N = 256 Saaten 1,2,3,4, dann N = 512 Saaten 1 3 5 (je ein Lauf).
set -u
cd /home/fmh/fmhc-physics-remote/glas-strahlung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 09:05:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" p4000a "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf gs-A256 code/gs.py netz --N 256 --saaten 1,2,3,4 --out lauf/gs
for s in 1 3 5; do
  lauf gs-A512-$s code/gs.py netz --N 512 --saaten $s --out lauf/gs
done
echo "kette p4000a ende $(date -u +%H:%M:%S)"
