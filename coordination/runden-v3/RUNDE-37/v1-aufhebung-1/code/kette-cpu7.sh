#!/bin/bash
# V1-AUFHEBUNG-1, einmalige Laufkette (Spur cpu7): K1 (Kurve dTT = 0, 18 Punkte + exakter Punkt).
set -u
cd /home/fmh/fmhc-physics-remote/v1-aufhebung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 10:10:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu7 "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf va-K1 code/va.py netz --punkte kurve --kl 0.005,0.01,0.02 --out lauf/kurve.json
echo "kette cpu7 ende $(date -u +%H:%M:%S)"
