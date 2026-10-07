#!/bin/bash
set -u
SPUR=cpu
source /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/laufplan/kopf.inc
lauf f-p4-a 4 0.1 16 40 "$DA" haupt
lauf f-m4-c -4 0.1 16 40 "$DC" haupt
lauf f-m2-c -2 0.1 16 40 "$DC" haupt
lauf f-m1-a -1 0.1 16 40 "$DA" haupt
lauf g-p2 2 0.16 10 40 "$DALLE" haupt
lauf f-00-b 0 0.1 16 40 "$DB" flach
echo "spur fertig $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
