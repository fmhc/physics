#!/bin/bash
# BAG-DIM (Runde 24): echte Laeufe nach PLAN.md Abschnitt 4. Einmalig von Hand gestartet; kein Dienst, kein Timer.
# Je Spur eine Kette nacheinander (kleintest.sh sperrt je Spur ohnehin).
cd /home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/haupt || exit 1
C=/home/fmh/fmhc-physics-remote/runde24-bag-dim/code/bagdim.py
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
H=/home/fmh/fmhc-physics-remote/runde24-bag-dim/lauf/haupt
R8=1.333521432163324
G2="g2:241 --q0 100 --ratio $R8 --ra 1.152 --rb 0.3333333333333333 --pruef-k 0,8,16,24,26 --flach-k 4,12 --dq-k 8,16,24 --profil-k 14,26"
G3="g3:81 --q0 1000 --ratio $R8 --ra 1.0 --rb 0.25 --ohne-frisch --dq-k 8,16 --profil-k 22"
SG="sg:9 --q0 60 --ratio 1.268603140 --ra 1.4 --rb 0.3642 --pruef-k alle --flach-k 8,16 --dq-k 12,24,32"

lauf() {  # lauf <spur> <name> <argumente...>
  local spur=$1 name=$2
  shift 2
  bash $K $spur r24bd-$name $C "$@" > $H/$name.log 2>&1
}

kette_cpu() {
  lauf cpu S-g2 spektrum g2:241 $H/s_g2.json --klein 12
  lauf cpu S-g3 spektrum g3:81 $H/s_g3.json --klein 8
  lauf cpu D3a beutel ${G3%% *} $H/b_g3_a.json ${G3#* } --k0 0 --k1 6
  lauf cpu D3b beutel ${G3%% *} $H/b_g3_b.json ${G3#* } --k0 7 --k1 11
  lauf cpu D3p1 beutel ${G3%% *} $H/b_g3_p1.json ${G3#* } --k0 10 --k1 10 --pruef-k 10
  lauf cpu SGf beutel ${SG%% *} $H/b_sg_f.json ${SG#* } --k0 33 --k1 34
}
kette_cpu2() {
  lauf cpu2 S-sg spektrum sg:8 $H/s_sg.json
  lauf cpu2 D3c beutel ${G3%% *} $H/b_g3_c.json ${G3#* } --k0 12 --k1 15
  lauf cpu2 SGa beutel ${SG%% *} $H/b_sg_a.json ${SG#* } --k0 0 --k1 13
  lauf cpu2 SGe beutel ${SG%% *} $H/b_sg_e.json ${SG#* } --k0 30 --k1 32
}
kette_cpu3() {
  lauf cpu3 S-zr spektrum zr:10000:6:1 $H/s_zr.json
  lauf cpu3 D3d beutel ${G3%% *} $H/b_g3_d.json ${G3#* } --k0 16 --k1 19
  lauf cpu3 SGb beutel ${SG%% *} $H/b_sg_b.json ${SG#* } --k0 14 --k1 20
}
kette_cpu4() {
  lauf cpu4 Z beutel zr:10000:6:1 $H/b_zr.json --q0 10 --ratio $R8 --ra 2 --rb 0 --k0 0 --k1 24 --wahl alle --flach-immer --pruef-k 8,16 --dq-k 8,16
  lauf cpu4 D2a beutel ${G2%% *} $H/b_g2_a.json ${G2#* } --k0 0 --k1 15
  lauf cpu4 D2b beutel ${G2%% *} $H/b_g2_b.json ${G2#* } --k0 16 --k1 26
  lauf cpu4 D3p2 beutel ${G3%% *} $H/b_g3_p2.json ${G3#* } --k0 21 --k1 21 --pruef-k 21
}
kette_cpu6() {
  lauf cpu6 D3e beutel ${G3%% *} $H/b_g3_e.json ${G3#* } --k0 20 --k1 22
  lauf cpu6 SGc beutel ${SG%% *} $H/b_sg_c.json ${SG#* } --k0 21 --k1 25
  lauf cpu6 SGd beutel ${SG%% *} $H/b_sg_d.json ${SG#* } --k0 26 --k1 29
}

kette_cpu > $H/kette-cpu.log 2>&1 &
kette_cpu2 > $H/kette-cpu2.log 2>&1 &
kette_cpu3 > $H/kette-cpu3.log 2>&1 &
kette_cpu4 > $H/kette-cpu4.log 2>&1 &
kette_cpu6 > $H/kette-cpu6.log 2>&1 &
wait
echo "alle Ketten fertig $(date --iso-8601=seconds)" > $H/ketten-fertig.txt
