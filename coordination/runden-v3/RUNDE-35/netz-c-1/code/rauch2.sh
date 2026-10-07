#!/bin/bash
# NETZ-C-1 (Runde 35): Rauchlaeufe Teil 2 (nach dem Plan, vor dem Einfrieren): Teil A klein, Fortsetzung, Auswertepfad.
set -u
cd /home/fmh/fmhc-physics-remote/runde35-netz
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
mkdir -p rauch/aw
bash $KT cpu3 r35ra code/netz_a.py rauch/aw/netz_a.json fcc,pyro,diamant,srs Z,W1,W2 20,40 > rauch/netz_a.log 2>&1
for i in $(seq 1 15); do
  bash $KT cpu3 r35rk3 code/kette.py rauch/ck2_h0.5 0.5 0.02 0 0 5 10 930 50 0.001 >> rauch/ck2.log 2>&1
  grep -q '"status": "unterbrochen"' rauch/ck2_h0.5.json || break
done
bash $KT cpu3 r35rk4 code/kette.py rauch/ok2_h0.5 0.5 0.02 0 0 5 10 930 50 > rauch/ok2.log 2>&1
bash $KT cpu3 r35rvgl code/vergleich.py rauch/ck2_h0.5.npz rauch/ok2_h0.5.npz > rauch/vergleich2.log 2>&1
bash $KT cpu3 r35rk5 code/kette.py rauch/aw/k0_h1_t10 1 0 0 0.9 30 10 400 50 > rauch/aw_k0.log 2>&1
bash $KT cpu3 r35rk6 code/kette.py rauch/aw/f_h0.5_t10 0.5 0.02 0 0 30 10 930 50 > rauch/aw_f.log 2>&1
bash $KT cpu3 r35rk7 code/kette.py rauch/aw/r_h1_q10.0_t10 1 0.12732395447351628 0.01 0 30 10 1150 50 > rauch/aw_r.log 2>&1
bash $KT cpu3 r35raw code/auswertung.py rauch/aw rauch/aw/auswertung.json > rauch/aw_auswertung.log 2>&1
date -u '+%Y-%m-%dT%H:%M:%SZ rauch2 fertig' >> rauch/fertig.txt
