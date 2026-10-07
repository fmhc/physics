#!/bin/bash
SP=cpu3
source /home/fmh/fmhc-physics-remote/runde27-kegel-xd/laufplan/kopf.inc
b3 haupt hf p 0.25 192 22 15 7
b3 haupt hf m 0.25 200 22 15 7
b3 haupt hg p 0.35 144 22 15 7
b3 haupt hg m 0.35 150 22 15 7
b3 haupt hg p 0.35 144 24 15 9
b3 haupt hg m 0.35 150 24 15 9
b3 flach ff 0 0.25 196 22 15 7
b3 flach fg 0 0.35 147 20 15 5
echo "spur fertig $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
