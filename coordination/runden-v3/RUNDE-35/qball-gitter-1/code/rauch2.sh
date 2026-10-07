#!/bin/bash
# QBALL-GITTER-1 (Runde 35): Rauchlaeufe 2 (nach Messkorrektur): Erhaltung, Vorzeichen/Formel, dt, Fortsetzung, Zeit.
set -u
cd /home/fmh/fmhc-physics-remote/runde35-qgitter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
mkdir -p rauch/r2
spur3() {
  bash $KT cpu3 r35qs1 code/qgitter.py rauch/r2/g0_h0.5 0.5 0 50 0.02 400 > rauch/r2/g0_h0.5.log 2>&1
  bash $KT cpu3 r35qs4 code/qgitter.py rauch/r2/g0_h0.125 0.125 0 50 0.02 400 > rauch/r2/g0_h0.125.log 2>&1
  for i in $(seq 1 40); do
    bash $KT cpu3 r35qs3 code/qgitter.py rauch/r2/c_h0.5 0.5 0.01 60 0.02 400 0.3 >> rauch/r2/c_h0.5.log 2>&1
    grep -q '"status": "unterbrochen"' rauch/r2/c_h0.5.json || break
  done
  bash $KT cpu3 r35qs3o code/qgitter.py rauch/r2/o_h0.5 0.5 0.01 60 0.02 400 > rauch/r2/o_h0.5.log 2>&1
  bash $KT cpu3 r35qsv code/vergleich.py rauch/r2/c_h0.5.npz rauch/r2/o_h0.5.npz > rauch/r2/vergleich.log 2>&1
  date -u '+%Y-%m-%dT%H:%M:%SZ spur3 fertig' >> rauch/fertig.txt
}
spur4() {
  bash $KT cpu4 r35qs2 code/qgitter.py rauch/r2/f_h0.125_dt0.02 0.125 0.005 100 0.02 400 > rauch/r2/f_dt0.02.log 2>&1
  bash $KT cpu4 r35qs2b code/qgitter.py rauch/r2/f_h0.125_dt0.01 0.125 0.005 100 0.01 400 > rauch/r2/f_dt0.01.log 2>&1
  date -u '+%Y-%m-%dT%H:%M:%SZ spur4 fertig' >> rauch/fertig.txt
}
date -u '+%Y-%m-%dT%H:%M:%SZ rauch2 start' >> rauch/fertig.txt
spur3 &
spur4 &
wait
bash $KT cpu3 r35qsc code/rauchcheck.py rauch/r2 g0_h0.5 g0_h0.125 f_h0.125_dt0.02 f_h0.125_dt0.01 c_h0.5 o_h0.5 > rauch/r2/rauchcheck.log 2>&1
date -u '+%Y-%m-%dT%H:%M:%SZ rauch2 fertig' >> rauch/fertig.txt
