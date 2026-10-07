#!/bin/bash
# Produktionslaeufe S5. Zwei Ketten, je Spur nacheinander (Spur-Lock von kleintest.sh serialisiert zusaetzlich).
D=/home/fmh/fmhc-physics-remote/quant-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
G=datei:$D/code/gwp.npz
T=0.348006576329167
N="$D/code/su2flow.py lauf --gitter netz --L 6 --Nt 12 --tau $T --gew $G --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 15 --rec 2"
H="$D/code/su2flow.py lauf --gitter kubisch --L 12 --Nt 12 --ntherm 150 --mabst 20 --eps 0.02 --epsfrac 0.05 --epsmax 0.1 --tmax 2.0 --rec 1"
kette_a() {
  bash $K p4000a s5-k $H --betas 2.30 2.25 2.35 --ncfg 30 --zeitlimit 520 --seed 20261007 --out $D/lauf-s5/k12 > $D/lauf-s5/k12.out 2>&1
  bash $K p4000a s5-n2 $N --betas 3.29 --ncfg 40 --zeitlimit 480 --seed 20261008 --out $D/lauf-s5/n6t12-s2 > $D/lauf-s5/n6t12-s2.out 2>&1
  bash $K p4000a s5-n34 $N --betas 3.34 --ncfg 40 --zeitlimit 330 --seed 20261009 --out $D/lauf-s5/n6t12-b334 > $D/lauf-s5/n6t12-b334.out 2>&1
}
kette_b() {
  bash $K p4000b s5-n1 $N --betas 3.29 --ncfg 40 --zeitlimit 480 --seed 20261007 --test --volcheck --ttest 2.0 --out $D/lauf-s5/n6t12-s1 > $D/lauf-s5/n6t12-s1.out 2>&1
  bash $K p4000b s5-n24 $N --betas 3.24 --ncfg 40 --zeitlimit 330 --seed 20261010 --out $D/lauf-s5/n6t12-b324 > $D/lauf-s5/n6t12-b324.out 2>&1
}
kette_a &
kette_b &
wait
