#!/bin/bash
# Rauchlaeufe R1 (BAG-DIM), einmalig von Hand gestartet; kein Dienst.
cd /home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch || exit 1
C=/home/fmh/fmhc-physics-remote/runde24-bag-dim/code/bagdim.py.rauch1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
R=/home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch
nohup bash $K cpu2 r24bd-rb2 $C beutel g2:81 $R/b_g2_81.json --q0 130 --ratio 1.5 --k0 0 --k1 6 --ra 1.152 --rb 0.3333 --pruef-k 3 --dq-k 4 --profil-k 6 > $R/b_g2_81.log 2>&1 &
nohup bash $K cpu3 r24bd-rsg $C beutel sg:7 $R/b_sg7.json --q0 60 --ratio 1.7 --k0 0 --k1 8 --ra 1.4 --rb 0.3642 --pruef-k 4 --dq-k 5 > $R/b_sg7.log 2>&1 &
nohup bash $K cpu4 r24bd-rg3 $C beutel g3:31 $R/b_g3_31.json --q0 1200 --ratio 1.6 --k0 0 --k1 3 --ra 1.0 --rb 0.25 --dq-k 2 --profil-k 3 > $R/b_g3_31.log 2>&1 &
nohup bash -c "bash $K cpu6 r24bd-rzr $C beutel zr:2000:6:7 $R/b_zr2000.json --q0 15 --ratio 2 --k0 0 --k1 8 --ra 2 --rb 0 --flach-immer --pruef-k 4 --dq-k 3; bash $K cpu6 r24bd-rzs $C spektrum zr:4000:6:7 $R/s_zr4000.json" > $R/zr.log 2>&1 &
