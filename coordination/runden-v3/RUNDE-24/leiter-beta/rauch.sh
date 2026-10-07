#!/bin/bash
# LEITER-BETA (Runde 24): Rauchlaeufe VOR dem Einfrieren des Plans. Ungueltig fuer jede Vorhersage.
# Parameter kommen in keinem echten Lauf vor: 3 Zeilen, Zeilenabstand 3,3e-4 bzw. 7e-4, x0 = 0,78513 bzw. 0,82017,
# n_rho 1000, n_dicht 1001, dicht_halb 0,06, keine Pole. Zweck: Laufzeit je Profil und je W-Punkt bei beta = 1,
# Zahl der Nullstellen von L(y_b) im rho-Fenster, Groesse von s und Kernwachstum.
# Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
cd /home/fmh/fmhc-physics-remote/runde24-leiter-beta || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde24-leiter-beta
P=bic2_3d_praez.py
G="--beta 1.0 --n-zeilen 3 --n-rho 1000 --n-dicht 1001 --dicht-halb 0.06 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 3 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 500 --reserve 150 --pole nein --art leiter --h 0.04"
echo "RAUCH-START $(date -Is)" > $D/rauch/KETTE.log
( bash $K cpu3 r24lb-rauch-a $P praez $G --zeilen-dx 3.3e-4 --x0 0.78513 --rho0 1.8174 --rho-steig 1.25 --x-pol 0.78513 --out rauch/rauch-a > $D/rauch/LAUF-rauch-a.log 2>&1 ) &
( bash $K cpu4 r24lb-rauch-b $P praez $G --zeilen-dx 7e-4 --x0 0.82017 --rho0 1.8612 --rho-steig 1.25 --x-pol 0.82017 --out rauch/rauch-b > $D/rauch/LAUF-rauch-b.log 2>&1 ) &
wait
echo "RAUCH-ENDE $(date -Is)" >> $D/rauch/KETTE.log
