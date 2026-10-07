# Gemeinsamer Kopf der Spurskripte KEGEL-XD-2 (Runde 28). Wird von spur-*.sh per source gelesen.
B=/home/fmh/fmhc-physics-remote/runde28-kegel-xd-2
KT=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
DA="0,1.2,2.4,3.6"
DB="4.8,6.0,7.2,8.4"
DC="9.6,10.8,12.0,13.2,14.4,15.6,16.8,18.0,19.2"
DALLE="0,1.2,2.4,3.6,4.8,6.0,7.2,8.4,9.6,10.8,12.0,13.2,14.4,15.6,16.8,18.0,19.2"
DRAND="7.2,19.2"
# lauf <name> <k> <dr> <m> <rmax> <d-Liste> <rolle>
lauf() {
  bash "$KT" "$SPUR" "r28k2-$1" ../kegel_xd2.py ball2d --rolle "$7" --k "$2" --dr "$3" --m "$4" --rmax "$5" --Q 200 \
    --d "$6" --aus "$B/lauf/b2-$1.json" > "$B/lauf/log-$1.txt" 2>&1
  echo "$1 rc=$? $(date -u +%H:%M:%S)" >> "$B/lauf/fertig-$SPUR.txt"
}
cd "$B/lauf" || exit 1
