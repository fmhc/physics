#!/bin/bash
# MINKOWSKI-DIM-1: echte Laeufe nach PLAN.md Abschnitt 4. Einmalig von Hand gestartet; kein Dienst, kein Timer, kein Hook.
# Je Spur eine Kette nacheinander (kleintest.sh sperrt je Spur). Danach die Auswertung (cpu2).
B=/home/fmh/fmhc-physics-remote/minkowski-dim-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code
H=$B/lauf
cd $H || exit 1
ST="st:7 --q0 40 --periode 9.797958971132712 --ra 1.2 --rb 0.3037 --pruef-k alle --flach-k 8,16 --dq-k 12,24 --budget 560"

lauf() {  # lauf <spur> <name> <skript> <argumente...>
  local spur=$1 name=$2
  shift 2
  bash $K $spur md-$name "$@" > $H/$name.log 2>&1
}

kette_cpu2() {
  lauf cpu2 M1 $C/md.py kubisch --out $H/kubisch.json
  lauf cpu2 M0 $C/md.py kasten --out $H/kasten.json
  lauf cpu2 S4 $C/bagdim_st.py spektrum st:4 $H/s_st4.json
  lauf cpu2 S5 $C/bagdim_st.py spektrum st:5 $H/s_st5.json
  lauf cpu2 S6 $C/bagdim_st.py spektrum st:6 $H/s_st6.json
  lauf cpu2 BD $C/bagdim_st.py beutel ${ST%% *} $H/b_st_d.json ${ST#* } --k0 22 --k1 25
  lauf cpu2 BB $C/bagdim_st.py beutel ${ST%% *} $H/b_st_b.json ${ST#* } --k0 12 --k1 17
}
kette_cpu3() {
  lauf cpu3 T1 $C/md.py takt --netze V,S,C15,A15 --out $H/takt-kristall.json
  lauf cpu3 T2 $C/md.py takt --netze glas-N512-s1,glas-N512-s2,glas-N512-s3,glas-N512-s4 --out $H/takt-glas.json
  lauf cpu3 BE $C/bagdim_st.py beutel ${ST%% *} $H/b_st_e.json ${ST#* } --k0 26 --k1 28
  lauf cpu3 BA $C/bagdim_st.py beutel ${ST%% *} $H/b_st_a.json ${ST#* } --k0 0 --k1 11
}
kette_cpu4() {
  lauf cpu4 BF $C/bagdim_st.py beutel ${ST%% *} $H/b_st_f.json ${ST#* } --k0 29 --k1 32
  lauf cpu4 BC $C/bagdim_st.py beutel ${ST%% *} $H/b_st_c.json ${ST#* } --k0 18 --k1 21
}

kette_cpu2 > $H/kette-cpu2.log 2>&1 &
kette_cpu3 > $H/kette-cpu3.log 2>&1 &
kette_cpu4 > $H/kette-cpu4.log 2>&1 &
wait
echo "alle Ketten fertig $(date --iso-8601=seconds)" > $H/ketten-fertig.txt
lauf cpu2 AW $C/md.py auswertung --ordner $H --out $H/auswertung.json
echo "auswertung fertig $(date --iso-8601=seconds)" >> $H/ketten-fertig.txt
