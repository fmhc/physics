#!/bin/bash
# PHASE-3D-BLIND (Runde 31): Rauchlaeufe VOR dem Einfrieren des Plans, an den bekannten Sprossen (PB0-Kontrolle),
# ausserhalb der echten Fenster: beta = 1/2 u = 1/eps in [34,203222; 36,048630] (n = 15 bei 35,1259 +- 0,4 b),
# beta = 1 u in [31,345598; 33,422734] (k = 1 bei 32,3842 +- 0,4 b). Zweck: Laufzeit je Profil und je Illinois-Schritt,
# Nullstellenzahl von L(y_b), Groesse von s, Kernwachstum. Erst h = 0,04 (Fenster), dann h = 0,02 (Startklammer aus
# h = 0,04). Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer. Spuren cpu und cpu2.
cd /home/fmh/fmhc-physics-remote/runde31-phase-3d-blind || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde31-phase-3d-blind
P=bic2_3d_suche.py
G="--n-scan 5 --n-rho 1000 --n-dicht 801 --dicht-halb 0.04 --iter-wurzel 80 --tol-wurzel 1e-13 --tol-x 1e-9 --iter-x 14 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --budget 560 --reserve 60"
B05="--beta 0.5 --fenster-u 34.203222,36.048630 --x0 0.528469 --rho0 1.557309 --rho-steig 1.07"
B1="--beta 1.0 --fenster-u 31.345598,33.422734 --x0 0.780879 --rho0 1.802761 --rho-steig 0.86"
echo "RAUCH-START $(date -Is)" > $D/rauch/KETTE.log
( bash $K cpu r31pb-rauch-b05-h004 $P suche $G $B05 --h 0.04 --out rauch/b05-h004 > $D/rauch/LAUF-b05-h004.log 2>&1 ;
  bash $K cpu r31pb-rauch-b05-h002 $P suche $G --beta 0.5 --klammer-aus rauch/b05-h004/suche.json --h 0.02 --out rauch/b05-h002 > $D/rauch/LAUF-b05-h002.log 2>&1 ) &
( bash $K cpu2 r31pb-rauch-b1-h004 $P suche $G $B1 --h 0.04 --out rauch/b1-h004 > $D/rauch/LAUF-b1-h004.log 2>&1 ;
  bash $K cpu2 r31pb-rauch-b1-h002 $P suche $G --beta 1.0 --klammer-aus rauch/b1-h004/suche.json --h 0.02 --out rauch/b1-h002 > $D/rauch/LAUF-b1-h002.log 2>&1 ) &
wait
echo "RAUCH-ENDE $(date -Is)" >> $D/rauch/KETTE.log
