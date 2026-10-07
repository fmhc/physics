#!/bin/bash
# kette.sh - Runde 20 HUELLEN-QUADRUPOL: alle Laeufe nacheinander auf der .69, Spur cpu6 (PLAN 10).
L=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-20/huellen-quadrupol
RB=/home/fmh/fmhc-physics-remote/runde20-huellen-quadrupol
PY=$RB/code/quadrupol.py
AW=$RB/code/auswertung_quadrupol.py
A=$RB/aus
Z=$A/zeilen.json
K="bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu6"
lauf() {
  n=$1; shift
  ssh fmh@192.168.178.69 "cd $RB && $K $n $*" > $L/aus/logs/$n.log 2>&1
  rc=$?
  echo "$(date +%H:%M:%S) fertig $n rc=$rc" >> $L/aus/logs/kette.txt
  return $rc
}
holen() { rsync -a --exclude '*.npz' fmh@192.168.178.69:$A/ $L/aus/; }
# V0
lauf q20-pruef $RB/code/pruef.py $RB/code/quadrupol.py $RB/code/auswertung_quadrupol.py $RB/code/stille3.py $RB/code/huellen_leiter.py $RB/code/beutel.py $RB/code/auswertung.py || exit 1
lauf q20-liste $PY ell=2 liste $Z || exit 1
# V1
lauf q20-prof-st1 $PY ell=2 profile 1 $A/prof-st1 $Z || exit 1
lauf q20-prof-st2 $PY ell=2 profile 2 $A/prof-st2 $Z || exit 1
lauf q20-k1-l0-st1 $PY ell=0 k1 1 $A/prof-st1 $Z $RB/ref/k1-referenz.json $A/k1-l0 $A/laeufe/k1-l0-st1.json
lauf q20-k1-l1-st1 $PY ell=1 k1 1 $A/prof-st1 $Z $RB/ref/k1-referenz.json $A/k1-l1 $A/laeufe/k1-l1-st1.json
lauf q20-k1-l0-st2 $PY ell=0 k1 2 $A/prof-st2 $Z $RB/ref/k1-referenz.json $A/k1-l0 $A/laeufe/k1-l0-st2.json
lauf q20-k1-l1-st2 $PY ell=1 k1 2 $A/prof-st2 $Z $RB/ref/k1-referenz.json $A/k1-l1 $A/laeufe/k1-l1-st2.json
lauf q20-probe $PY ell=2 probe 1 $A/prof-st1 $Z 40,60,71 $A/laeufe/probe-l2-st1.json
holen
for f in k1-l0-st1 k1-l1-st1 k1-l0-st2 k1-l1-st2; do
  jq -e '.bestanden == true' $L/aus/laeufe/$f.json > /dev/null 2>&1 || { echo "$(date +%H:%M:%S) K1 nicht bestanden ($f): Halt vor der Suche" >> $L/aus/logs/kette.txt; exit 2; }
done
echo "$(date +%H:%M:%S) K1 bestanden (4 von 4 Laeufen): Suche" >> $L/aus/logs/kette.txt
# V2
lauf q20-b1-0-71 $PY ell=2 block 1 $A/prof-st1 $A/laeufe $Z 0 71
lauf q20-b2-0-40 $PY ell=2 block 2 $A/prof-st2 $A/laeufe $Z 0 40
lauf q20-b2-40-71 $PY ell=2 block 2 $A/prof-st2 $A/laeufe $Z 40 71
lauf q20-b1-0-71-w $PY ell=2 block 1 $A/prof-st1 $A/laeufe $Z 0 71
lauf q20-b2-0-40-w $PY ell=2 block 2 $A/prof-st2 $A/laeufe $Z 0 40
lauf q20-b2-40-71-w $PY ell=2 block 2 $A/prof-st2 $A/laeufe $Z 40 71
# V3
lauf q20-stellen $AW stellen $A/laeufe $Z $RB/ref/l0-stellen-r18.json $RB/ref/l1-stellen-r19.json $A/laeufe/auswertung.json
lauf q20-uA1 $PY ell=2 umlauf 1 $A/prof-st1 $Z $A/laeufe/umlauf-punkte-alle-st1.json $A/laeufe/umlauf-alle-st1.json 0 999
lauf q20-uA2 $PY ell=2 umlauf 2 $A/prof-st2 $Z $A/laeufe/umlauf-punkte-alle-st2.json $A/laeufe/umlauf-alle-st2.json 0 999
lauf q20-final $AW final $A/laeufe $A/laeufe/auswertung-final.json
holen
echo "$(date +%H:%M:%S) Kette Ende" >> $L/aus/logs/kette.txt
