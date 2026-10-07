#!/bin/bash
# Runde 17 ZWEIFELD-NACHBAU, PLAN-NACHTRAG-4. Aufruf: kette-n4.sh <spur> <stufe> <kurzname> <index ...>
cd /home/fmh/fmhc-physics-remote/runde17-zweifeld-nachbau || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1; ST=$2; KN=$3; shift 3
bash $K $SP z17-n4-$KN code/zweifeld_n4.py kurve M2 $ST aus/prof-M2.npz aus/n4-kurve-M2-$KN.json aus/n3w2-kand-M2-st1.json "$@" > logs/N4-$KN.log 2>&1
