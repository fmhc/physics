#!/bin/bash
# DIM-LEITER-QBALL-1: Auswertung und Bilder mit dem eingefrorenen Code (Spur cpu11).
B=/home/fmh/fmhc-physics-remote/dim-leiter-qball-1
cd $B/lauf
E="$B/lauf/d1.json $B/lauf/d2.json $B/lauf/d3.json $B/lauf/d4.json $B/lauf/d5.json $B/lauf/d6.json $B/lauf/d7.json $B/lauf/d8.json $B/lauf/d9.json $B/lauf/d10.json $B/lauf/d11.json $B/lauf/d12.json"
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu11 dlq1ausw $B/code/dim_leiter.py auswertung $B/lauf/auswertung.json $E > $B/lauf/auswertung.log 2>&1 < /dev/null
bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu11 dlq1bild $B/code/dim_leiter.py bild $B/lauf/auswertung.json $E -- $B/lauf/dim-leiter-qball-1 > $B/lauf/bild.log 2>&1 < /dev/null
date -u
