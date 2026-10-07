cd /home/fmh/fmhc-physics-remote/runde11-chem1
K="bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh"
P=/home/fmh/fmhc-physics-remote/runde3-tests1d/ausgabe/profile_r3.pt
for x0 in 0 -2 2; do
  echo "== $(date -Is) trennpunkt $x0"
  $K p4000a chem1-tr$x0 chem1_trenn.py t1 --abstaende 12,14,16,18,20 --trennpunkt $x0 --profil $P --out lauf-69/trenn$x0
  echo "== rc=$? $(date -Is)"
done
echo "KETTE-CHEM1-TRENN-ENDE $(date -Is)"
