#!/bin/bash
set -u
SPUR=cpu2
source /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/laufplan/kopf.inc
lauf f-p4-b 4 0.1 16 40 "$DB" haupt
lauf f-p2-c 2 0.1 16 40 "$DC" haupt
lauf f-p1-b 1 0.1 16 40 "$DB" haupt
lauf g-m4 -4 0.16 10 40 "$DALLE" haupt
lauf f-00-a 0 0.1 16 40 "$DA" flach
lauf r-m4 -4 0.16 10 48 "$DRAND" rand
lauf r-m1 -1 0.16 10 48 "$DRAND" rand
echo "spur fertig $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
