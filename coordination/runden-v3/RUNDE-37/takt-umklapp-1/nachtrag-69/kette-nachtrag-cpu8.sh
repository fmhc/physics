#!/bin/bash
# TAKT-UMKLAPP-1, Nachtraege nach dem Einfrieren (beschreibend), Spur cpu8, startet erst nach dem Ende der Laufkette cpu8.
set -u
cd /home/fmh/fmhc-physics-remote/takt-umklapp-1 || exit 1
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
until grep -q "kette cpu8 ende" kette-cpu8.out; do sleep 5; done
lauf() {
  local name=$1; shift
  bash "$K" cpu8 "$name" "$@" > "nachtrag/$name.log" 2>&1
  echo "$name rc=$? $(date -u +%H:%M:%S)"
}
lauf tu-nt-p1 code/nachtrag_p1.py --out nachtrag/nachtrag-p1.json
lauf tu-nt-ht3-s2 code/nachtrag_ht3.py --netz uk-N256-s2-f0.2 --out nachtrag/nachtrag-ht3-s2.json
lauf tu-nt-ht3-s3 code/nachtrag_ht3.py --netz uk-N256-s3-f0.2 --out nachtrag/nachtrag-ht3-s3.json
echo "kette nachtrag ende $(date -u +%H:%M:%S)"
