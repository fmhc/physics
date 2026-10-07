#!/bin/bash
# NETZ-DYN-1 Auswertung nach Ende aller Rechenketten (cpu8): Superpunkt-Herkunft und Tabellen
cd /home/fmh/fmhc-physics-remote/netz-dyn-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
for p in 2596987 2599172 2599593 2598033 2599852 2597189; do while kill -0 $p; do sleep 10; done; done
bash $K cpu8 nd-sp code/sp_herkunft.py stand/s1a.pkl stand/s1b.pkl stand/s1c.pkl stand/s1l3.pkl stand/f1.pkl stand/f4.pkl stand/d3-1.5.pkl stand/d3-2.6.pkl stand/d3-4.0.pkl
bash $K cpu8 nd-ausw code/auswertung.py
