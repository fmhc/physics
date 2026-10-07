#!/bin/bash
# UMKLAPP-1, einmalige Laufkette Spur cpu4 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 05:10:00 UTC (07:10 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 05:10:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu4 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf uk-mb256a code/uk.py mb --N 256 --saaten 1-24 --zieh 8 --out lauf/mb-N256-a.json
lauf uk-mb256b code/uk.py mb --N 256 --saaten 25-48 --zieh 8 --out lauf/mb-N256-b.json
lauf uk-tt256-s2-f02-A code/uk.py tt --N 256 --saaten 2 --f 0.2 --ridx 0-3 --out lauf/tt-N256-s2-f0.2-A.json
lauf uk-tt256-s2-f02-B code/uk.py tt --N 256 --saaten 2 --f 0.2 --ridx 4-8 --out lauf/tt-N256-s2-f0.2-B.json
lauf uk-tt256-s2-f02-C code/uk.py tt --N 256 --saaten 2 --f 0.2 --ridx 9-12 --out lauf/tt-N256-s2-f0.2-C.json
lauf uk-tt128-f005 code/uk.py tt --N 128 --saaten 1,2,3,4 --f 0.05 --out lauf/tt-N128-f0.05-s1-4.json
lauf uk-tt256-f0p code/uk.py tt --N 256 --saaten 1,2,3 --f 0 --ridx 0 --out lauf/tt-N256-f0-s1-3-r0.json
lauf uk-tt256-s1-f005-A code/uk.py tt --N 256 --saaten 1 --f 0.05 --ridx 0-5 --out lauf/tt-N256-s1-f0.05-A.json
lauf uk-tt256-s1-f005-B code/uk.py tt --N 256 --saaten 1 --f 0.05 --ridx 6-12 --out lauf/tt-N256-s1-f0.05-B.json
lauf uk-tt256-s3-f02-C code/uk.py tt --N 256 --saaten 3 --f 0.2 --ridx 9-12 --out lauf/tt-N256-s3-f0.2-C.json
echo "kette cpu4 ende $(date -u +%H:%M:%S)"
