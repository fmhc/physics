#!/bin/bash
# TT-GLAS-2 Rauchtest r3b (vor dem Einfrieren): nur Schluessel und Laufzeiten (--rauch), Rauchsaat 901, Spur p4000b.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K p4000b tg2-r3b1 code/dk.py --N 256 --saaten 901 --ridx 0 --rauch --out rauch/r3b1-dk-N256.json > rauch/r3b1.log 2>&1; echo "r3b1 rc=$? $(date -u +%H:%M:%S)"
bash $K p4000b tg2-r3b2 code/dk.py --N 1024 --saaten 901 --ridx 0 --ohne_lin --varianten a --rauch --out rauch/r3b2-dk-N1024.json > rauch/r3b2.log 2>&1; echo "r3b2 rc=$? $(date -u +%H:%M:%S)"
