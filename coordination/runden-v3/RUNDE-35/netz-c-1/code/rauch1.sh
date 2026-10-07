#!/bin/bash
# NETZ-C-1 (Runde 35): Rauchlaeufe Teil 1 (vor dem Plan; ohne Ergebnisgroessen): Netzbau, Zeitmessung, Fortsetzung.
set -u
cd /home/fmh/fmhc-physics-remote/runde35-netz
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
mkdir -p rauch/aw
bash $KT cpu3 r35rbau code/netz_a.py rauch/bau.json fcc,pyro,diamant,srs Z,W1,W2 bau > rauch/bau.log 2>&1
bash $KT cpu3 r35rk1 code/kette.py rauch/z_h0.1 0.1 0.012732395447351628 0.01 0 20 10 1150 50 > rauch/z_h0.1.log 2>&1
bash $KT cpu3 r35rk2 code/kette.py rauch/z_h0.125 0.125 0.02 0 0 20 10 3420 50 > rauch/z_h0.125.log 2>&1
for i in 1 2 3 4 5 6 7 8 9 10; do
  bash $KT cpu3 r35rk3 code/kette.py rauch/ck_h0.5 0.5 0.02 0 0 40 10 930 50 0.5 >> rauch/ck.log 2>&1
  grep -q '"status": "unterbrochen"' rauch/ck_h0.5.json || break
done
bash $KT cpu3 r35rk4 code/kette.py rauch/ok_h0.5 0.5 0.02 0 0 40 10 930 50 > rauch/ok.log 2>&1
date -u '+%Y-%m-%dT%H:%M:%SZ rauch1 fertig' >> rauch/fertig.txt
