set -u
R=/home/fmh/fmhc-physics-remote/runde27-kegel-xd
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
P=$R/kegel_xd.py
Q=1028.6303777659662
cd $R/lauf
lauf() {
  local name=$1; shift
  bash $K $SP r27kx-$name $P "$@" > $R/lauf/log-$name.txt 2>&1
  echo "$name rc=$? $(date -u +%T)" >> $R/lauf/fertig-$SP.txt
}
# b3 <rolle> <kurz> <vz p|m|0> <h> <nphi> <rmax> <zmax> <d>
b3() {
  local rolle=$1 kurz=$2 vz=$3 h=$4 np=$5 rmax=$6 zmax=$7 d=$8 dl
  case $vz in p) dl=0.1284 ;; m) dl=-0.1284 ;; 0) dl=0.0 ;; esac
  lauf $kurz-$vz-d$d ball3d --rolle $rolle --delta $dl --h $h --rmax $rmax --zmax $zmax --nphi $np --Q $Q --d $d \
    --om2-start 0.64 --aus $R/lauf/b3-$kurz-$vz-d$d.json
}
