#!/bin/bash
# Hauptlauf Spur cpu3 (PLAN 14): V-BZ Teil 0.
set -u
D=/home/fmh/fmhc-physics-remote/ueberleitung-v-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=$D/lauf
bash $K cpu3 uv-vb0 code/uv.py vbz --teil 0 --out $L/vbz0.json > $L/vbz0.log 2>&1
echo "kette cpu3 fertig $(date -u +%H:%M:%S)" > $L/kette-cpu3.txt
