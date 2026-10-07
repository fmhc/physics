#!/bin/bash
# V1-AUFHEBUNG-1, einmalige Laufkette (Spur cpu): H1 (Hauptpunkte), dann Q1 (Quadratur). Jeder Lauf ueber kleintest.sh.
# Schlusszeit: nach 2026-10-05 10:10:00 UTC (12:10 CEST) startet kein Lauf.
set -u
cd /home/fmh/fmhc-physics-remote/v1-aufhebung-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SCHLUSS=$(date -u -d '2026-10-05 10:10:00' +%s)
lauf() {
  local name=$1; shift
  if [ "$(date -u +%s)" -ge "$SCHLUSS" ]; then echo "$name nicht gestartet (Schlusszeit) $(date -u +%H:%M:%S)"; return; fi
  bash "$K" cpu "$name" "$@" > "lauf/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf va-H1 code/va.py netz --punkte haupt --kl 0.0025,0.005,0.01,0.02 --out lauf/haupt.json
lauf va-Q1 code/va.py netz --punkte haupt --nur J_iso,F1_exakt --kl 0.01 --nt 12 --nphi 24 --out lauf/quad.json
echo "kette cpu ende $(date -u +%H:%M:%S)"
