#!/bin/bash
# TAKT-UMKLAPP-1, einmalige Laufkette Spur cpu10 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 07:30:00 UTC (09:30 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/takt-umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 07:30:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu10 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tu-A4 code/tu.py teilA --netze uk-N256-s1-f0.2,uk-N256-s2-f0.2 --out lauf/teilA-4-uk256.json
lauf tu-A5 code/tu.py teilA --netze uk-N256-s3-f0.2,uk-N256-s1-f0.05 --out lauf/teilA-5-uk256.json
lauf tu-B3 code/tu.py teilB --netze glas-N128-s5,glas-N128-s6 --out lauf/teilB-3.json
lauf tu-B6 code/tu.py teilB --netze glas-N128-s11,glas-N128-s12 --out lauf/teilB-6.json
echo "kette cpu10 ende $(date -u +%H:%M:%S)"
