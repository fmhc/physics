#!/bin/bash
# TAKT-UMKLAPP-1, einmalige Laufkette Spur cpu8 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 07:30:00 UTC (09:30 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/takt-umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 07:30:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu8 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tu-A1 code/tu.py teilA --netze V,S,VD,SD --out lauf/teilA-1-zellen.json
lauf tu-A2a code/tu.py teilA --netze glas-N128-s1,glas-N128-s2,glas-N128-s3,glas-N128-s4,glas-N128-s5,glas-N128-s6 --out lauf/teilA-2a-glas.json
lauf tu-B1 code/tu.py teilB --netze glas-N128-s1,glas-N128-s2 --out lauf/teilB-1.json
lauf tu-B4 code/tu.py teilB --netze glas-N128-s7,glas-N128-s8 --out lauf/teilB-4.json
lauf tu-B7 code/tu.py teilB --netze V2 --out lauf/teilB-7-V2.json
echo "kette cpu8 ende $(date -u +%H:%M:%S)"
