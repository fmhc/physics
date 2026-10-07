#!/bin/bash
# LEITER-BETA (Runde 24): K0 (beta = 1/2, n = 10, woertlich wie RUNDE-13) und Phase 1 (Grobsuche bei beta = 1, h = 0,04)
# nach PLAN.md (eingefrorene Fassung PLAN.md.eingefroren-*). Einmal von Hand per nohup auf der .69 gestartet; kein Dienst,
# kein Timer. Spuren cpu, cpu2, cpu3, cpu4, cpu6 (nicht cpu5, keine GPU).
cd /home/fmh/fmhc-physics-remote/runde24-leiter-beta || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde24-leiter-beta
P=bic2_3d_praez.py
# K0: G und N10 woertlich aus RUNDE-13/leiter3d-praez/start.sh
G0="--beta 0.5 --n-zeilen 9 --zeilen-dx 2.5e-4 --n-rho 400 --n-dicht 401 --dicht-halb 0.02 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 3 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 500 --reserve 150"
N10="--x0 0.5424 --rho0 1.57178 --rho-steig 5.3 --x-pol 0.5424"
# Phase 1: fuenf Fenster in omega^2, Nachbarfenster teilen eine Zeile; dichtes rho-Band um 1,77345 + 1,25 eps
G1="--beta 1.0 --h 0.04 --n-rho 5000 --n-dicht 2001 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 0 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 500 --reserve 150 --pole nein --art leiter --rho-steig 1.25"
F1="--n-zeilen 10 --zeilen-dx 5.5e-4 --x0 0.782475 --rho0 1.814044 --dicht-halb 0.027 --x-pol 0.782475"
F2="--n-zeilen 10 --zeilen-dx 7.5e-4 --x0 0.788325 --rho0 1.821356 --dicht-halb 0.032 --x-pol 0.788325"
F3="--n-zeilen 10 --zeilen-dx 1.1e-3 --x0 0.79665 --rho0 1.831763 --dicht-halb 0.039 --x-pol 0.79665"
F4="--n-zeilen 10 --zeilen-dx 1.7e-3 --x0 0.80925 --rho0 1.847513 --dicht-halb 0.051 --x-pol 0.80925"
F5="--n-zeilen 7 --zeilen-dx 2.9e-3 --x0 0.8256 --rho0 1.86795 --dicht-halb 0.064 --x-pol 0.8256"
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r24lb-$n $P praez "$@" --out lauf/$n > $D/LAUF-$n.log 2>&1
}
echo "PHASE1-START $(date -Is)" > $D/KETTE1.log
( lauf cpu  k0-h004 $G0 $N10 --h 0.04 ; lauf cpu  g1 $G1 $F1 ) &
( lauf cpu6 k0-h002 $G0 $N10 --h 0.02 ; lauf cpu6 g5 $G1 $F5 ) &
( lauf cpu2 g2 $G1 $F2 ) &
( lauf cpu3 g3 $G1 $F3 ) &
( lauf cpu4 g4 $G1 $F4 ) &
wait
echo "PHASE1-ENDE $(date -Is)" >> $D/KETTE1.log
