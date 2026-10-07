#!/bin/bash
# EINFANG-2 Auswertung und Bilder (Runde 34), Spur cpu4. Nur kleintest.sh-Aufrufe.
set -u
B=/home/fmh/fmhc-physics-remote/runde34-einfang2
L=$B/lauf
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$B/einfang2.py
cd $L
bash $K cpu4 r34ef2-auswertung $P auswertung --ordner $L > $L/log-auswertung.txt 2>&1
bash $K cpu4 r34ef2-bild $P bild --ordner $L --namen ik-v0.05,ik-v0.1,ik-v0.05-b,ik-v0.05-lang,ik-v0.05-dt0.05,ik-v0.05-h0.2 > $L/log-bild.txt 2>&1
