#!/bin/bash
# QBALL-GITTER-1 (Runde 35): Rauch 3 = Auswertepfad mit kurzen Laeufen unter den Namen der Hauptlaeufe (Ergebnisse ohne Bedeutung).
set -u
cd /home/fmh/fmhc-physics-remote/runde35-qgitter
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
mkdir -p rauch/aw
for H in 0.125 0.25 0.5; do
  bash $KT cpu3 r35qa0 code/qgitter.py rauch/aw/g0_h$H $H 0 20 0.02 400 >> rauch/aw/laeufe.log 2>&1
  bash $KT cpu3 r35qa1 code/qgitter.py rauch/aw/f1_h${H}_dt1 $H 0.005 40 0.02 400 >> rauch/aw/laeufe.log 2>&1
  bash $KT cpu3 r35qa2 code/qgitter.py rauch/aw/f2_h${H}_dt1 $H 0.01 40 0.02 400 >> rauch/aw/laeufe.log 2>&1
done
bash $KT cpu3 r35qa3 code/qgitter.py rauch/aw/f1_h0.125_dt2 0.125 0.005 30 0.01 400 >> rauch/aw/laeufe.log 2>&1
bash $KT cpu3 r35qa4 code/qgitter.py rauch/aw/f1_h0.125_lang 0.125 0.005 30 0.02 800 >> rauch/aw/laeufe.log 2>&1
bash $KT cpu3 r35qaw code/auswertung.py rauch/aw rauch/aw/auswertung.json > rauch/aw/auswertung.log 2>&1
date -u '+%Y-%m-%dT%H:%M:%SZ rauch3 fertig' >> rauch/fertig.txt
