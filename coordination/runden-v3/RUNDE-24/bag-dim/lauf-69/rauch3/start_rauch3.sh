#!/bin/bash
# Rauchlauf R3 (BAG-DIM): ganze Kette mit kleinen Graphen und Q-Rastern, die in keinem echten Lauf vorkommen,
# danach Probelauf der Auswertung. Einmalig von Hand gestartet; kein Dienst.
cd /home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch3 || exit 1
C=/home/fmh/fmhc-physics-remote/runde24-bag-dim/code/bagdim.py.rauch3
A=/home/fmh/fmhc-physics-remote/runde24-bag-dim/code/auswertung.py.rauch3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
R=/home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/rauch3
bash $K cpu4 r24bd-r3a $C spektrum g2:41 $R/s_g2.json --klein 9
bash $K cpu4 r24bd-r3b $C spektrum g3:21 $R/s_g3.json --klein 7
bash $K cpu4 r24bd-r3c $C spektrum sg:6 $R/s_sg.json
bash $K cpu4 r24bd-r3d $C spektrum zr:2000:6:7 $R/s_zr.json
bash $K cpu4 r24bd-r3e $C beutel g2:81 $R/b_g2.json --q0 130 --ratio 1.333521432163324 --k0 0 --k1 6 --ra 1.152 --rb 0.3333 --pruef-k 2 --flach-k 1 --dq-k 3 --profil-k 6
bash $K cpu4 r24bd-r3f $C beutel g3:41 $R/b_g3.json --q0 1300 --ratio 1.333521432163324 --k0 0 --k1 5 --ra 1.0 --rb 0.25 --ohne-frisch --pruef-k 3 --dq-k 2
bash $K cpu4 r24bd-r3g $C beutel sg:7 $R/b_sg.json --q0 70 --ratio 1.2686 --k0 0 --k1 20 --ra 1.4 --rb 0.3642 --pruef-k alle --flach-k 4 --dq-k 10
bash $K cpu4 r24bd-r3h $C beutel zr:2000:6:7 $R/b_zr.json --q0 13 --ratio 1.333521432163324 --k0 0 --k1 20 --ra 2 --rb 0 --flach-immer --wahl alle --pruef-k 5 --dq-k 6
bash $K cpu4 r24bd-r3z $A $R $R/auswertung_rauch3.json
