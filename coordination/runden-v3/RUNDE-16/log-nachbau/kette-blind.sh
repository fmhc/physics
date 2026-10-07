#!/bin/bash
# Einmaliger Starter fuer die blinde Suche je Stufe: Zeilen in zwei Aufrufen, danach Kandidaten.
# Aufruf: bash kette-blind.sh <stufe> <spur> [k2]
set -u
D=/home/fmh/fmhc-physics-remote/runde16-log-nachbau
cd "$D"
ST=$1
SP=$2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
if [ "${3:-}" = "k2" ]; then
  bash $K "$SP" r16k2 stille.py k2 "$D/k2.json" 0.70 0.74 0.78 0.82 0.86 0.90 0.94 0.98
fi
bash $K "$SP" "r16blscanA$ST" stille.py scan log "$ST" "$D/aus-blind-st$ST" 0.700 0.705 0.710 0.715 0.720 0.725 0.730 0.735 0.740 0.745 0.750 0.755 0.760 0.765 0.770 0.775 0.780 0.785 0.790 0.795 0.800 0.805 0.810 0.815 0.820 0.825 0.830 0.835 0.840 0.845
bash $K "$SP" "r16blscanB$ST" stille.py scan log "$ST" "$D/aus-blind-st$ST" 0.850 0.855 0.860 0.865 0.870 0.875 0.880 0.885 0.890 0.895 0.900 0.905 0.910 0.915 0.920 0.925 0.930 0.935 0.940 0.945 0.950 0.955 0.960 0.965 0.970 0.975 0.980
bash $K "$SP" "r16blkand$ST" stille.py kand log "$ST" "$D/blind-kand-st$ST.json" "$D"/aus-blind-st"$ST"/zeile-log-st"$ST"-*.json
