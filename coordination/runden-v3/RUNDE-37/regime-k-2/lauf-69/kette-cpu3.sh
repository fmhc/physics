#!/bin/bash
# REGIME-K-2 Hauptlaeufe, Spur cpu3 (PLAN 8). Aufruf aus /home/fmh/fmhc-physics-remote/regime-k-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=/home/fmh/fmhc-physics-remote/regime-k-2/lauf
lauf() { n=$1; shift; bash $K cpu3 "rk2-$n" code/rk2.py "$@" --out $L/$n.json > $L/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $L/kette-cpu3.txt; }
echo "start $(date --iso-8601=seconds)" > $L/kette-cpu3.txt
lauf welle-V-A-koord-rw24 welle --arm V-A --betraege 0.05 --lesart koord --richtungen rw24
lauf welle-V-A-kl-rw24 welle --arm V-A --betraege 0.05 --lesart kl --richtungen rw24
lauf welle-V-A-k02-rw24 welle --arm V-A --betraege 0.2 --lesart koord --richtungen rw24
echo "ende $(date --iso-8601=seconds)" >> $L/kette-cpu3.txt
