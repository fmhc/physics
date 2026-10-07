#!/bin/bash
# Kette 8192 Groessenkontrolle maxcor 20, nur k 40..57 (10:23), Spur cpu.
D=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-16/dim-beutel
ssh fmh@192.168.178.69 'cd /home/fmh/fmhc-physics-remote/runde16-dim-beutel && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu db-ket8192m20-auf code/dimbeutel2.py ast --graph kette --size 8192 --tag ket8192m20-auf --out aus/kontrolle --kstart 40 --kende 57 --richtung 1 --maxcor 20' > $D/aus/logs/ket8192m20-auf.log 2>&1
