#!/bin/bash
set -u
SPUR=cpu3
source /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/laufplan/kopf.inc
lauf f-p4-c 4 0.1 16 40 "$DC" haupt
lauf f-p2-b 2 0.1 16 40 "$DB" haupt
lauf f-p1-c 1 0.1 16 40 "$DC" haupt
lauf g-p4 4 0.16 10 40 "$DALLE" haupt
lauf g-m1 -1 0.16 10 40 "$DALLE" haupt
lauf r-p4 4 0.16 10 48 "$DRAND" rand
lauf r-p1 1 0.16 10 48 "$DRAND" rand
echo "spur fertig $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
