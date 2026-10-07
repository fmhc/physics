#!/bin/bash
# Startet zwei Zeit-Rauchtests auf der .69 (nur Fortschritt, keine Q/E-Werte)
B=/home/fmh/fmhc-physics-remote/dim-leiter-qball-1
cd $B/rauch
setsid nohup bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu4 dlq1rauch5 $B/code/dim_leiter.py rauch $B/rauch/rauch5.json 12 voll > $B/rauch/rauch5.log 2>&1 < /dev/null &
setsid nohup bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu11 dlq1rauch6 $B/code/dim_leiter.py rauch $B/rauch/rauch6.json 4,7 voll > $B/rauch/rauch6.log 2>&1 < /dev/null &
date -u
