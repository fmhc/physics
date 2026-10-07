#!/bin/bash
# REGIME-K-3 Rauchtest (PLAN 7). Aufruf auf der .69: bash code/rauch.sh <kennung> ; aus /home/fmh/fmhc-physics-remote/regime-k-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
R=/home/fmh/fmhc-physics-remote/regime-k-3/rauch
ID=${1:?Kennung}
cd /home/fmh/fmhc-physics-remote/regime-k-3 || exit 2
(bash $K cpu8 rk3-$ID-kw code/rk3.py transfer --arm KW --satz raster --rauch --out $R/$ID-kw-raster.json > $R/$ID-kw-raster.log 2>&1
 bash $K cpu8 rk3-$ID-kwbz code/rk3.py transfer --arm KW --satz bz --rauch --out $R/$ID-kw-bz.json > $R/$ID-kw-bz.log 2>&1) &
(bash $K cpu9 rk3-$ID-b1 code/rk3.py transfer --arm B1-t1 --satz raster --rauch --out $R/$ID-b1-raster.json > $R/$ID-b1-raster.log 2>&1
 bash $K cpu9 rk3-$ID-b1bz code/rk3.py transfer --arm B1-t1 --satz bz --rauch --out $R/$ID-b1-bz.json > $R/$ID-b1-bz.log 2>&1) &
(bash $K cpu10 rk3-$ID-va code/rk3.py transfer --arm V-A --satz raster --rauch --out $R/$ID-va-raster.json > $R/$ID-va-raster.log 2>&1
 bash $K cpu10 rk3-$ID-vabz code/rk3.py transfer --arm V-A --satz bz --rauch --out $R/$ID-va-bz.json > $R/$ID-va-bz.log 2>&1) &
wait
grep -h -E "^(start|ende)|Service runtime|fertig|Error|error" $R/$ID-*.log
