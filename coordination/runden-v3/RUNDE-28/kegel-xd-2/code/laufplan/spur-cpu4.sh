#!/bin/bash
set -u
SPUR=cpu4
source /home/fmh/fmhc-physics-remote/runde28-kegel-xd-2/laufplan/kopf.inc
lauf f-m4-a -4 0.1 16 40 "$DA" haupt
lauf f-p2-a 2 0.1 16 40 "$DA" haupt
lauf f-m2-b -2 0.1 16 40 "$DB" haupt
lauf f-m1-b -1 0.1 16 40 "$DB" haupt
lauf g-p1 1 0.16 10 40 "$DALLE" haupt
lauf g-00 0 0.16 10 40 "$DALLE" flach
echo "spur fertig $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
