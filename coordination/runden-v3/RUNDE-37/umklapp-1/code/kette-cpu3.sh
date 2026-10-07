#!/bin/bash
# UMKLAPP-1, einmalige Laufkette Spur cpu3 (kein Dienst, kein Timer). Jeder Lauf ueber kleintest.sh (1 Thread, <= 600 s).
# Schlusszeit: nach 2026-10-05 05:10:00 UTC (07:10 CEST) startet kein neuer Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 05:10:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu3 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf uk-ko128 code/uk.py kontrolle --N 128 --saaten 1-4 --out lauf/kontrolle-N128.json
lauf uk-ko256 code/uk.py kontrolle --N 256 --saaten 1-4 --out lauf/kontrolle-N256.json
lauf uk-mb128 code/uk.py mb --N 128 --saaten 1-48 --zieh 8 --out lauf/mb-N128.json
lauf uk-tt128-f0 code/uk.py tt --N 128 --saaten 1,2,3,4 --f 0 --out lauf/tt-N128-f0-s1-4.json
lauf uk-tt128-f02a code/uk.py tt --N 128 --saaten 1,2 --f 0.2 --out lauf/tt-N128-f0.2-s1-2.json
lauf uk-tt128-f02b code/uk.py tt --N 128 --saaten 3,4 --f 0.2 --out lauf/tt-N128-f0.2-s3-4.json
lauf uk-tt256-s1-f02-A code/uk.py tt --N 256 --saaten 1 --f 0.2 --ridx 0-3 --out lauf/tt-N256-s1-f0.2-A.json
lauf uk-tt256-s1-f02-B code/uk.py tt --N 256 --saaten 1 --f 0.2 --ridx 4-8 --out lauf/tt-N256-s1-f0.2-B.json
lauf uk-tt256-s1-f02-C code/uk.py tt --N 256 --saaten 1 --f 0.2 --ridx 9-12 --out lauf/tt-N256-s1-f0.2-C.json
lauf uk-tt256-s3-f02-A code/uk.py tt --N 256 --saaten 3 --f 0.2 --ridx 0-3 --out lauf/tt-N256-s3-f0.2-A.json
lauf uk-tt256-s3-f02-B code/uk.py tt --N 256 --saaten 3 --f 0.2 --ridx 4-8 --out lauf/tt-N256-s3-f0.2-B.json
echo "kette cpu3 ende $(date -u +%H:%M:%S)"
