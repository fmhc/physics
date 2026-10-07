#!/bin/bash
# PHASE-3D: Start der Kette (einmalig). Prueft die Kopien der PHASE-WAND-Phase. Code-Agent, 03.10.2026.
R=/home/fmh/fmhc-physics-remote/runde26-phase-3d
cd $R
echo "3d4e10833ae6b37f7216bf2fbb5b556a4b8eba25d34b36c191451147e2857cc6  lauf/pw-phase-b05.json" | sha256sum -c - || exit 4
echo "32bedc3d894a946ffd4a3395b0a0c406b20d75d05110d6c7d88394ac307ba096  lauf/pw-phase-b1.json" | sha256sum -c - || exit 4
nohup bash $R/kette.sh > $R/lauf/KETTE.log 2>&1 < /dev/null &
echo "kette gestartet $(date --iso-8601=seconds)"
