#!/bin/bash
# SCHWERE-MASSE-V: Ortsprobe (Zentrum P0 = 0, H0 = 6 statt C1 = 4), sm_z.py, Spur als Argument.
SPUR=$1
LOG=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-37/schwere-masse-v/lauf-69
R='cd /home/fmh/fmhc-physics-remote/schwere-masse-v && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh'
for zhl in "0 1.0 20" "6 1.0 20" "0 1.25 16" "6 1.25 16" "0 0.64 32" "6 0.64 32" "0 2.0 10" "6 2.0 10"; do
  set -- $zhl
  N=qbz$1-o0.8-h$2
  ssh -o BatchMode=yes fmh@192.168.178.69 "$R $SPUR sm-z$1-h$2 code/sm_z.py qball --zentrum $1 --om 0.8 --h $2 --L $3 --maxiter 20000 --tmax 480 --out lauf/$N.json" > $LOG/$N.log 2>&1
done
T=$(date '+%Y-%m-%d %H:%M:%S %Z')
printf 'zentrum %s fertig %s\n' "$SPUR" "$T" >> $LOG/ketten-fertig.txt
