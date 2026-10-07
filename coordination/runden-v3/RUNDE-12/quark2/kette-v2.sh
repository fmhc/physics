cd /home/fmh/fmhc-physics-remote/runde12-quark2
K="bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh"
echo "== $(date -Is) w2 0.80 mit K1/K2"
$K cpu6 q2v2-080 quark2_v2.py --out lauf-69-v2/w080 --w2 0.80
echo "== rc=$? $(date -Is)"
for w in 0.55 0.60 0.65 0.70; do
  n=$(echo $w | tr -d .)
  echo "== $(date -Is) w2 $w"
  $K cpu6 q2v2-$n quark2_v2.py --out lauf-69-v2/w$n --w2 $w --ohne-k
  echo "== rc=$? $(date -Is)"
done
echo "KETTE-Q2V2-ENDE $(date -Is)"
