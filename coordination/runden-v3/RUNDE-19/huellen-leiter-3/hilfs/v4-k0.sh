#!/bin/bash
# V4a: formale K0'-Auswertung, sobald die drei K0'-Laeufe beendet sind (Spur cpu4, nach dem dortigen Testlauf).
R=/home/fmh/fmhc-physics-remote/runde19-huellen-leiter-3
K=/home/fmh/fmhc-physics-remote/kleintests/kleintest.sh
cd "$R" || exit 1
until [ "$(cat logs/k0-st1-a.log logs/k0-st2-a.log logs/k0-st2-b.log 2>/dev/null | grep -c '^ende ')" -ge 3 ]; do sleep 5; done
bash "$K" cpu4 r19hl3-ausw-k0 "$R/code/huellen_leiter3.py" ausw-k0 "$R/aus" "$R/ref/stellen-r18.json" "$R/aus/k0-auswertung.json" > "$R/logs/ausw-k0.log" 2>&1
