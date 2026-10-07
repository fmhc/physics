#!/bin/bash
# TT-GLAS-2 Rauchtest r2 (vor dem Einfrieren): nur Schluessel und Laufzeiten (--rauch), Rauchsaat 901, Spur cpu6.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu6 tg2-r2a code/bz.py --N 128 --saat 901 --kmax 3 --frist 60 --rauch --out rauch/r2a-bz-N128.json > rauch/r2a.log 2>&1; echo "r2a rc=$? $(date -u +%H:%M:%S)"
bash $K cpu6 tg2-r2b code/bz.py --N 256 --saat 901 --kmax 2 --frist 60 --ohne_kontrolle --rauch --out rauch/r2b-bz-N256.json > rauch/r2b.log 2>&1; echo "r2b rc=$? $(date -u +%H:%M:%S)"
bash $K cpu6 tg2-r2c code/dk.py --N 128 --saaten 901 --ridx 0 --rauch --out rauch/r2c-dk-N128.json > rauch/r2c.log 2>&1; echo "r2c rc=$? $(date -u +%H:%M:%S)"
bash $K cpu6 tg2-r2d code/dk.py --N 256 --saaten 901 --ridx 0 --ohne_lin --rauch --out rauch/r2d-dk-N256.json > rauch/r2d.log 2>&1; echo "r2d rc=$? $(date -u +%H:%M:%S)"
