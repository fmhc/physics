#!/bin/bash
SP=cpu2
source /home/fmh/fmhc-physics-remote/runde27-kegel-xd/laufplan/kopf.inc
b3 haupt hf p 0.25 192 20 15 5
b3 haupt hf m 0.25 200 20 15 5
b3 haupt hg p 0.35 144 20 15 5
b3 haupt hg m 0.35 150 20 15 5
b3 rand rg p 0.35 144 24 19 5
b3 rand rg m 0.35 150 24 19 5
b3 flach ff 0 0.25 196 20 15 5
b3 flach fg 0 0.35 147 18 15 3
echo "spur fertig $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
