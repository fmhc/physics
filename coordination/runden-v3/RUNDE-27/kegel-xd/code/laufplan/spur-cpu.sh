#!/bin/bash
SP=cpu
source /home/fmh/fmhc-physics-remote/runde27-kegel-xd/laufplan/kopf.inc
lauf teil-a teil_a --kq-ordner $R/eingabe-kegel-q --aus $R/lauf/teil-a.json
b3 null nf p 0.25 1 15 15 0
b3 null nf m 0.25 1 15 15 0
b3 null nf 0 0.25 1 15 15 0
b3 null ng p 0.35 1 15 15 0
b3 null ng m 0.35 1 15 15 0
b3 null ng 0 0.35 1 15 15 0
b3 haupt hf p 0.25 192 18 15 3
b3 haupt hf m 0.25 200 18 15 3
b3 haupt hf p 0.25 192 26.25 15 11.25
b3 haupt hf m 0.25 200 26.25 15 11.25
b3 haupt hg p 0.35 144 18 15 3
b3 haupt hg m 0.35 150 18 15 3
b3 flach ff 0 0.25 196 18 15 3
echo "spur fertig $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
