#!/bin/bash
# REGIME-K-2 Hauptlaeufe, Spur cpu2 (PLAN 8). Aufruf aus /home/fmh/fmhc-physics-remote/regime-k-2
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
L=/home/fmh/fmhc-physics-remote/regime-k-2/lauf
lauf() { n=$1; shift; bash $K cpu2 "rk2-$n" code/rk2.py "$@" --out $L/$n.json > $L/$n.log 2>&1; echo "$n rc=$? $(date --iso-8601=seconds)" >> $L/kette-cpu2.txt; }
echo "start $(date --iso-8601=seconds)" > $L/kette-cpu2.txt
lauf gitter-KW gitter --arm KW
lauf gitter-B1-t1 gitter --arm B1-t1 --pt
lauf gitter-V-A gitter --arm V-A
lauf gitter-V-B gitter --arm V-B
lauf gitter-S-A gitter --arm S-A
lauf vorz-KW vorzeichen --arm KW
lauf vorz-V-A vorzeichen --arm V-A
lauf vorz-B1-t1 vorzeichen --arm B1-t1
lauf vorz-V-B vorzeichen --arm V-B
lauf vorz-S-A vorzeichen --arm S-A
lauf welle-KW-koord-rw24 welle --arm KW --betraege 0.05 --lesart koord --richtungen rw24
lauf welle-B1-t1-koord-rw24 welle --arm B1-t1 --betraege 0.05 --lesart koord --richtungen rw24
echo "ende $(date --iso-8601=seconds)" >> $L/kette-cpu2.txt
