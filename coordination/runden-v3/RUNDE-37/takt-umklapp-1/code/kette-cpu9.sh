#!/bin/bash
# TAKT-UMKLAPP-1, einmalige Laufkette Spur cpu9 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 07:30:00 UTC (09:30 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/takt-umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 07:30:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu9 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tu-A3 code/tu.py teilA --netze uk-N128-s1-f0.05,uk-N128-s2-f0.05,uk-N128-s3-f0.05,uk-N128-s4-f0.05,uk-N128-s1-f0.2,uk-N128-s2-f0.2,uk-N128-s3-f0.2,uk-N128-s4-f0.2 --out lauf/teilA-3-uk128.json
lauf tu-A2b code/tu.py teilA --netze glas-N128-s7,glas-N128-s8,glas-N128-s9,glas-N128-s10,glas-N128-s11,glas-N128-s12 --out lauf/teilA-2b-glas.json
lauf tu-B2 code/tu.py teilB --netze glas-N128-s3,glas-N128-s4 --out lauf/teilB-2.json
lauf tu-B5 code/tu.py teilB --netze glas-N128-s9,glas-N128-s10 --out lauf/teilB-5.json
echo "kette cpu9 ende $(date -u +%H:%M:%S)"
