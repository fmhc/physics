#!/bin/bash
# Z2-SCHUTZ-1, NACHTRAG (nach Sicht, beschreibend): Hesse G2 lief im Hauptlauf in die Laufzeitgrenze (600 s), weil die
# beschreibenden ZS0-Endpunkte mitgerechnet wurden. Hier nur S, T und Kletterbild SB, eingefrorener Code, eigener Ordner.
# Danach Auswertung (eingefrorener Code) auf einer Kopie der Hauptlauf-JSONs plus dieser Hesse-Datei.
set -u
B=/home/fmh/fmhc-physics-remote/z2-schutz-1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
C=$B/code/z2.py
A=$B/lauf
N=$B/nachtrag
E=$B/eingaben-gfn1
mkdir -p $N
cd $B/code || exit 1
run() { local name=$1; shift; bash $K cpu7 "$name" "$@" >> $N/$name.log 2>&1; echo "rc=$? $name $(date -u +%H:%M:%S)" >> $N/kette-cpu7.out; }
echo "kette start $(date -u +%H:%M:%S)" >> $N/kette-cpu7.out
run z2NH2 $C hesse --r0 12 --R 24 --start $A/start-r12-R24.npz --zusatz SB=$A/weg-haupt-r12-R24-neb.npz:X --aus $N
while [ ! -e $A/alles.fertig ]; do sleep 5; done
for f in $A/*.json; do b=$(basename $f); [ "$b" = "hesse-r12-R24.json" ] || cp $f $N/; done
run z2NAusw $B/code/auswertung_z2.py --lauf $N --eingaben $E --aus $N
echo "kette ende $(date -u +%H:%M:%S)" >> $N/kette-cpu7.out
touch $N/alles.fertig
