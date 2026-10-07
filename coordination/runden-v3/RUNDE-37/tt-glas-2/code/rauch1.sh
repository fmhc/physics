#!/bin/bash
# TT-GLAS-2 Rauchtest r1 (vor dem Einfrieren): nur Schluessel und Laufzeiten (--rauch), Rauchsaat 901, Spur cpu6.
set -u
cd /home/fmh/fmhc-physics-remote/tt-glas-2 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
bash $K cpu6 tg2-r1a code/bz.py --N 128 --saat 901 --kmax 2 --frist 60 --rauch --out rauch/r1a-bz-N128.json > rauch/r1a.log 2>&1; echo "r1a rc=$? $(date -u +%H:%M:%S)"
bash $K cpu6 tg2-r1b code/sz.py --N 256 --saaten 901 --ridx 0 --lin --rauch --out rauch/r1b-sz-N256.json > rauch/r1b.log 2>&1; echo "r1b rc=$? $(date -u +%H:%M:%S)"
bash $K cpu6 tg2-r1c code/sz.py --N 512 --saaten 901 --ridx 0 --varianten a --rauch --out rauch/r1c-sz-N512.json > rauch/r1c.log 2>&1; echo "r1c rc=$? $(date -u +%H:%M:%S)"
