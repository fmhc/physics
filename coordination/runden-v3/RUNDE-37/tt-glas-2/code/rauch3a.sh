#!/bin/bash
# TT-GLAS-2 Rauchtest r3a (vor dem Einfrieren): nur Schluessel und Laufzeiten (--rauch), Rauchsaat 901, Spur p4000a.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K p4000a tg2-r3a1 code/bz.py --N 256 --saat 901 --kmax 4 --frist 90 --rauch --out rauch/r3a1-bz-N256.json > rauch/r3a1.log 2>&1; echo "r3a1 rc=$? $(date -u +%H:%M:%S)"
bash $K p4000a tg2-r3a2 code/dk.py --N 512 --saaten 901 --ridx 0 --ohne_lin --rauch --out rauch/r3a2-dk-N512.json > rauch/r3a2.log 2>&1; echo "r3a2 rc=$? $(date -u +%H:%M:%S)"
