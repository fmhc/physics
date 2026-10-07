#!/bin/bash
# Hauptlauf Spur cpu4 (PLAN 14): V-BZ Teil 1 mit K, U.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
bash $K cpu4 uv-vb1 code/uv.py vbz --teil 1 --out $L/vbz1.json > $L/vbz1.log 2>&1
echo "kette cpu4 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu4.txt
