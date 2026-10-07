#!/bin/bash
# TAKT-DYNAMIK-1 Rauchkette (Rauchsaat 901 und VD2), einmalig per ssh gestartet. Jeder Lauf ueber kleintest.sh.
set -u
cd /home/fmh/fmhc-physics-remote/takt-dynamik-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1
shift
case "$SP" in
  cpu8)
    bash $K cpu8 td-r2b code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-2 --arm b --budget 110 --out rauch/td-s901-A1e-2-b.json > rauch/r2b.log 2>&1; echo "r2b rc=$?"
    bash $K cpu8 td-r2c code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-2 --arm c --ereignisse rauch/td-s901-A1e-2-b.json --budget 110 --out rauch/td-s901-A1e-2-c.json > rauch/r2c.log 2>&1; echo "r2c rc=$?"
    ;;
  cpu9)
    bash $K cpu9 td-r3 code-rauch1/td.py lauf --netz VD2 --A 1e-2 --arm b --budget 110 --rauch --out rauch/r3-vd2.json > rauch/r3.log 2>&1; echo "r3 rc=$?"
    bash $K cpu9 td-r5a code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-2 --arm a --budget 110 --out rauch/td-s901-A1e-2-a.json > rauch/r5a.log 2>&1; echo "r5a rc=$?"
    ;;
  cpu10)
    bash $K cpu10 td-r4p code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-3 --arm b --lesart P --budget 110 --out rauch/td-s901-A1e-3-b-P.json > rauch/r4p.log 2>&1; echo "r4p rc=$?"
    bash $K cpu10 td-r4h code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-3 --arm b --h 0.25 --budget 15 --out rauch/td-s901-A1e-3-b-h025.json > rauch/r4h.log 2>&1; echo "r4h rc=$?"
    bash $K cpu10 td-r4h2 code-rauch1/td.py lauf --netz glas-N128-s901 --A 1e-3 --arm b --h 0.25 --budget 110 --out rauch/td-s901-A1e-3-b-h025.json > rauch/r4h2.log 2>&1; echo "r4h2 rc=$? (Fortsetzung)"
    ;;
esac
echo "kette $SP ende $(date -u +%H:%M:%S)"
