#!/bin/bash
# Lokale Laufreihe Nachtrag 3 (Z3), Spur cpu.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-frisch-sie10-z3 code/dimbeutel2.py frisch --graph sierpinski --size 10 --start s1 --tag sie10s1-z3 --out aus/frisch --klist 46,52,58,64,70,76,82 --formen A --maxcor 5' > $D/aus/logs/frisch-sie10s1-z3.log 2>&1
date --iso-8601=seconds > $D/aus/logs/nachtrag3.fertig
