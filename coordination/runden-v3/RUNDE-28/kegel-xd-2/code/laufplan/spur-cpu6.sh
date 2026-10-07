#!/bin/bash
set -u
SPUR=cpu6
source /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/laufplan/kopf.inc
lauf f-m4-b -4 0.1 16 40 "$DB" haupt
lauf f-m2-a -2 0.1 16 40 "$DA" haupt
lauf f-p1-a 1 0.1 16 40 "$DA" haupt
lauf f-m1-c -1 0.1 16 40 "$DC" haupt
lauf g-m2 -2 0.16 10 40 "$DALLE" haupt
lauf f-00-c 0 0.1 16 40 "$DC" flach
echo "spur fertig $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
