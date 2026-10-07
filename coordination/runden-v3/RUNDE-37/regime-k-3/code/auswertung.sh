#!/bin/bash
# REGIME-K-3 Auswertung (PLAN 9, nach den Hauptlaeufen). Aufruf auf der .69: bash code/auswertung.sh
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=/home/fmh/fmhc-physics-remote/regime-k-3/lauf
R2=/home/fmh/fmhc-physics-remote/regime-k-2/lauf
cd /home/fmh/fmhc-physics-remote/regime-k-3 || exit 2
bash $K cpu8 rk3-auswertung code/rk3.py auswertung --ein \
  kw-r=$L/KW-raster.json kw-b=$L/KW-bz.json b1-r=$L/B1-t1-raster.json b1-b=$L/B1-t1-bz.json \
  va-r0=$L/V-A-raster-0.json va-r1=$L/V-A-raster-1.json va-r2=$L/V-A-raster-2.json va-r3=$L/V-A-raster-3.json \
  va-b0=$L/V-A-bz-0.json va-b1=$L/V-A-bz-1.json va-b2=$L/V-A-bz-2.json va-b3=$L/V-A-bz-3.json \
  ref-va1=$R2/welle-V-A-koord-rw24.json ref-va2=$R2/welle-V-A-koord-rk25.json ref-kw=$R2/welle-KW-koord-rw24.json \
  ref-b1=$R2/welle-B1-t1-koord-rw24.json \
  --out $L/auswertung.json > $L/auswertung.log 2>&1
echo "auswertung rc=$? $(date --iso-8601=seconds)" >> $L/kette-auswertung.txt
