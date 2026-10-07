#!/bin/bash
# TT-GLAS-2, einmalige Laufkette B, Spur p4000b (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (<= 600 s).
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
for s in 7 8 9 10 11 12; do
  lauf tg2-bz256-s$s code/bz.py --N 256 --saat $s --out lauf/bz-N256-s$s.json
done
lauf tg2-dk256-B code/dk.py --N 256 --saaten 7,8,9,10,11,12 --out lauf/dk
lauf tg2-dk512-B code/dk.py --N 512 --saaten 3,4 --out lauf/dk
for s in 2 4; do
  lauf tg2-dk1024-s$s-r0 code/dk.py --N 1024 --saaten $s --ridx 0-6 --varianten a --ohne_lin --out lauf/dk-N1024-s$s-r0.json
  lauf tg2-dk1024-s$s-r1 code/dk.py --N 1024 --saaten $s --ridx 7-12 --varianten a --ohne_lin --out lauf/dk-N1024-s$s-r1.json
done
echo "kette B ende $(date -u +%H:%M:%S)"
