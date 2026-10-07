#!/bin/bash
# QBALL-GITTER-1 (Runde 35): Rauchlaeufe vor dem Einfrieren (Newton, Erhaltung, Vorzeichen/Formel, Fortsetzung, Zeit).
set -u
cd /home/fmh/fmhc-physics-remote/runde35-qgitter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
spur3() {
  bash $KT cpu3 r35qr1 code/qgitter.py rauch/r1_g0_h0.5 0.5 0 50 0.0125 400 > rauch/r1.log 2>&1
  bash $KT cpu3 r35qr4 code/qgitter.py rauch/r4_g0_h0.125 0.125 0 50 0.0125 400 > rauch/r4.log 2>&1
  for i in $(seq 1 30); do
    bash $KT cpu3 r35qr3 code/qgitter.py rauch/r3c_h0.5 0.5 0.01 60 0.0125 400 0.3 >> rauch/r3c.log 2>&1
    grep -q '"status": "unterbrochen"' rauch/r3c_h0.5.json || break
  done
  bash $KT cpu3 r35qr3o code/qgitter.py rauch/r3o_h0.5 0.5 0.01 60 0.0125 400 > rauch/r3o.log 2>&1
  bash $KT cpu3 r35qrv code/vergleich.py rauch/r3c_h0.5.npz rauch/r3o_h0.5.npz > rauch/r3_vergleich.log 2>&1
  date -u '+%Y-%m-%dT%H:%M:%SZ spur3 fertig' >> rauch/fertig.txt
}
spur4() {
  bash $KT cpu4 r35qr2 code/qgitter.py rauch/r2_f_h0.125 0.125 0.005 100 0.0125 400 > rauch/r2.log 2>&1
  date -u '+%Y-%m-%dT%H:%M:%SZ spur4 fertig' >> rauch/fertig.txt
}
date -u '+%Y-%m-%dT%H:%M:%SZ rauch1 start' >> rauch/fertig.txt
spur3 &
spur4 &
wait
