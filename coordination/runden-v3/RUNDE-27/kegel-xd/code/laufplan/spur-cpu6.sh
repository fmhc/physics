#!/bin/bash
SP=cpu6
source /home/fmh/fmhc-physics-remote/runde27-kegel-xd/laufplan/kopf.inc
b3 haupt hf p 0.25 192 25.25 15 10.25
b3 haupt hf m 0.25 200 25.25 15 10.25
b3 haupt hg p 0.35 144 25.25 15 10.25
b3 haupt hg m 0.35 150 25.25 15 10.25
b3 haupt hg p 0.35 144 26.25 15 11.25
b3 haupt hg m 0.35 150 26.25 15 11.25
b3 flach ff 0 0.25 196 25.25 15 10.25
b3 flach ff 0 0.25 196 26.25 15 11.25
b3 flach fg 0 0.35 147 25.25 15 10.25
b3 flach fg 0 0.35 147 26.25 15 11.25
echo "spur fertig $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
