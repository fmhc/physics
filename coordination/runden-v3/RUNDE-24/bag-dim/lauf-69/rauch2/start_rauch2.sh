#!/bin/bash
# Rauchlaeufe R2 (BAG-DIM, Zeitmessung), einmalig von Hand gestartet; kein Dienst. Q-Werte liegen auf keinem echten Raster.
cd /home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch2 || exit 1
C=/home/fmh/fmhc-physics-remote/runde24-bag-dim/code/bagdim.py.rauch2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
R=/home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch2
nohup bash $K cpu r24bd-r2g3 $C beutel g3:81 $R/b_g3_81.json --q0 2e5 --ratio 1.3 --k0 0 --k1 1 --ra 1.0 --rb 0.25 --ohne-frisch --dq-k 1 > $R/b_g3_81.log 2>&1 &
nohup bash $K cpu2 r24bd-r2zs $C spektrum zr:10000:6:7 $R/s_zr10000_s7.json > $R/s_zr.log 2>&1 &
nohup bash $K cpu3 r24bd-r2sg $C beutel sg:9 $R/b_sg9.json --q0 5e4 --ratio 1.4 --k0 0 --k1 1 --ra 1.4 --rb 0.3642 --pruef-k alle > $R/b_sg9.log 2>&1 &
nohup bash $K cpu6 r24bd-r2g2 $C beutel g2:181 $R/b_g2_181.json --q0 1.5e5 --ratio 1.15 --k0 0 --k1 1 --ra 1.152 --rb 0.3333 --pruef-k alle --profil-k 1 > $R/b_g2_181.log 2>&1 &
