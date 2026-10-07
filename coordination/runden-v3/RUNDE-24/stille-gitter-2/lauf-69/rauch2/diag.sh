#!/bin/bash
# Aufruf: diag.sh <spur> <name> <typ> <stern> <h> <x> <rho0> <liste "lin:lpml:sig0:pexp" ...>
D=/home/fmh/fmhc-physics-remote/runde24-stille-gitter-2; R=$D/lauf/rauch2; K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
SP=$1; NM=$2; TY=$3; ST=$4; H=$5; X=$6; RH=$7; shift 7
cd $R
for P in "$@"; do
  IFS=: read LI LP SG PE <<< "$P"
  TAG=${NM}_${LI}_${LP}_${SG}_${PE}
  bash $K $SP r24sg-d${NM} $D/stille_gitter2.py --modus punkt --typ $TY --stern $ST --h $H --x0 $X --rho0 $RH --lin $LI --lpml $LP --sig0 $SG --pexp $PE --out $R/$TAG.json > $R/$TAG.log 2>&1
done
