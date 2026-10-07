#!/bin/bash
SP=cpu4
source /home/fmh/fmhc-physics-remote/runde27-kegel-xd/laufplan/kopf.inc
b3 haupt hf p 0.25 192 24 15 9
b3 haupt hf m 0.25 200 24 15 9
b3 rand rg p 0.35 144 29.25 19 10.25
b3 rand rg m 0.35 150 29.25 19 10.25
b3 flach ff 0 0.25 196 24 15 9
b3 flach fg 0 0.35 147 22 15 7
b3 flach fg 0 0.35 147 24 15 9
echo "spur fertig $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
