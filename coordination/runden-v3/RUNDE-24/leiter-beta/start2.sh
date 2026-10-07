#!/bin/bash
# LEITER-BETA (Runde 24), Phase 2 (Kandidaten, Stufen h = 0,04 und 0,02); erzeugt von gen2.sh aus kandidaten.json.
# Einmal von Hand per nohup auf der .69 gestartet; kein Dienst, kein Timer.
cd /home/fmh/fmhc-physics-remote/runde24-leiter-beta || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
D=/home/fmh/fmhc-physics-remote/runde24-leiter-beta
P=bic2_3d_praez.py
G2="--beta 1.0 --n-zeilen 7 --zeilen-dx 3e-4 --n-rho 5000 --n-dicht 2001 --dicht-halb 0.002 --u-n 60 --u-runden 30 --pr-drho 0.01 --pr-drho-max 0.03 --pr-u-halb 3 --iter-wurzel 80 --tol-wurzel 1e-13 --budget 480 --reserve 150 --pole ja --art leiter"
lauf() {   # spur name argumente...
  local s=$1 n=$2
  shift 2
  bash $K $s r24lb-$n $P praez $G2 "$@" --out lauf/$n > $D/LAUF-$n.log 2>&1
}
echo "PHASE2-START $(date -Is)" > $D/KETTE2.log
( lauf cpu c1-h002 --h 0.02 --x0 0.780863 --rho0 1.8027468 --rho-steig 0.8595 --x-pol 0.780863 ; lauf cpu c3-h004 --h 0.04 --x0 0.786755 --rho0 1.8077218 --rho-steig 0.8294 --x-pol 0.786755 ; lauf cpu c6-h002 --h 0.02 --x0 0.80138 --rho0 1.81935 --rho-steig 0.763 --x-pol 0.80138 ; lauf cpu c8-h004 --h 0.04 --x0 0.819616 --rho0 1.8325129 --rho-steig 0.688 --x-pol 0.819616 ) &
( lauf cpu2 c1-h004 --h 0.04 --x0 0.780863 --rho0 1.8027468 --rho-steig 0.8595 --x-pol 0.780863 ; lauf cpu2 c4-h002 --h 0.02 --x0 0.790621 --rho0 1.8108931 --rho-steig 0.8112 --x-pol 0.790621 ; lauf cpu2 c6-h004 --h 0.04 --x0 0.80138 --rho0 1.81935 --rho-steig 0.763 --x-pol 0.80138 ) &
( lauf cpu3 c2-h002 --h 0.02 --x0 0.783559 --rho0 1.805045 --rho-steig 0.8455 --x-pol 0.783559 ; lauf cpu3 c4-h004 --h 0.04 --x0 0.790621 --rho0 1.8108931 --rho-steig 0.8112 --x-pol 0.790621 ; lauf cpu3 c7-h002 --h 0.02 --x0 0.809149 --rho0 1.8251324 --rho-steig 0.7272 --x-pol 0.809149 ) &
( lauf cpu4 c2-h004 --h 0.04 --x0 0.783559 --rho0 1.805045 --rho-steig 0.8455 --x-pol 0.783559 ; lauf cpu4 c5-h002 --h 0.02 --x0 0.79538 --rho0 1.8146993 --rho-steig 0.788 --x-pol 0.79538 ; lauf cpu4 c7-h004 --h 0.04 --x0 0.809149 --rho0 1.8251324 --rho-steig 0.7272 --x-pol 0.809149 ) &
( lauf cpu6 c3-h002 --h 0.02 --x0 0.786755 --rho0 1.8077218 --rho-steig 0.8294 --x-pol 0.786755 ; lauf cpu6 c5-h004 --h 0.04 --x0 0.79538 --rho0 1.8146993 --rho-steig 0.788 --x-pol 0.79538 ; lauf cpu6 c8-h002 --h 0.02 --x0 0.819616 --rho0 1.8325129 --rho-steig 0.688 --x-pol 0.819616 ) &
wait
echo "PHASE2-ENDE $(date -Is)" >> $D/KETTE2.log
