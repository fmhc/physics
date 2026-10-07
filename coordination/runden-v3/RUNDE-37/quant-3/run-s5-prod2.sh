#!/bin/bash
# Nachlaeufe S5: beta 3,34 mit groesserem tmax; Endvolumen-Kontrollen (Netz L = 4, Hyperkubus L = 8).
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=datei:$D/code/gwp.npz
T=0.348006576329167
N="$D/code/su2flow.py lauf --gitter netz --tau $T --gew $G --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --rec 2"
H="$D/code/su2flow.py lauf --gitter kubisch --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 2.0 --rec 1"
kette_a() {
  bash $K p4000a s5-n34b $N --L 6 --Nt 12 --betas 3.34 --tmax 22 --ncfg 40 --zeitlimit 420 --seed 20261011 --out $D/lauf-s5/n6t12-b334b > $D/lauf-s5/n6t12-b334b.out 2>&1
}
kette_b() {
  bash $K p4000b s5-n4 $N --L 4 --Nt 12 --betas 3.29 --tmax 15 --ncfg 40 --zeitlimit 300 --seed 20261012 --out $D/lauf-s5/n4t12 > $D/lauf-s5/n4t12.out 2>&1
  bash $K p4000b s5-k8 $H --L 8 --Nt 8 --betas 2.30 --ncfg 40 --zeitlimit 200 --seed 20261013 --out $D/lauf-s5/k8t8 > $D/lauf-s5/k8t8.out 2>&1
}
kette_a &
kette_b &
wait
