#!/bin/bash
# BILDUNG-LEITER (Runde 22): eine Laufkette je Spur nach PLAN.md.eingefroren-20261002-204146, Abschnitt 3.
# Code-Agent, 02.10.2026. Kein Dienst: je Spur einmal von Hand mit nohup gestartet.
# Aufruf auf der .69: bash kette.sh <spur> <punkt> [scanpunkt ...]
set -u
D=/home/fmh/fmhc-physics-remote/runde22-bildung-leiter
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1
P=$2
shift 2
cd "$D" || exit 1
lauf() {   # <kurzname ohne Punkte> <logname> <argumente fuer zeit2d_v2.py ...>
  local KN=$1 LOG=$2
  shift 2
  bash "$K" "$SP" "$KN" zeit2d_v2.py "$@" > "$D/aus/$LOG.log" 2>&1
  echo "$(date --iso-8601=seconds) $LOG rc=$?" >> "$D/aus/kette-$SP.txt"
}
L=${P//./}
for ARM in lin nl; do
  lauf "r22-$ARM-02a-$L" "$ARM-02-$P-a" "$ARM" "$P" 0.02 2000 80 140 "$D/aus/$ARM-02-$P.json" bis=1000
  lauf "r22-$ARM-02b-$L" "$ARM-02-$P-b" "$ARM" "$P" 0.02 2000 80 140 "$D/aus/$ARM-02-$P.json" weiter
done
for ARM in lin nl; do
  lauf "r22-$ARM-04-$L" "$ARM-04-$P" "$ARM" "$P" 0.04 2000 80 140 "$D/aus/$ARM-04-$P.json"
done
for S in "$@"; do
  LS=${S//./}
  lauf "r22-scan-$LS" "scan-04-$S" lin "$S" 0.04 2000 80 140 "$D/aus/scan-04-$S.json"
done
echo "$(date --iso-8601=seconds) kette fertig" >> "$D/aus/kette-$SP.txt"
