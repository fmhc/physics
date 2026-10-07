#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
# Baut die oeffentliche, statische Fassung der Netz-Ansicht auf der .69 (Ziel: netz-web/public/netz/).
# Laeuft auf dem Laptop, braucht nur ssh, rsync und (auf der .69) jq. Den Upload nach physics.fmhc.io macht die Leitung.
# Daten werden als Kopien abgelegt; die Manifeste der Kopien werden bereinigt, die Originale bleiben unveraendert.
set -euo pipefail
V=$(cd "$(dirname "$0")/.." && pwd)
O="$V/oeffentlich"
H=fmh@192.168.178.69
W=/home/fmh/fmhc-physics-remote/netz-web
Z=$W/public/netz
Q=/home/fmh/fmhc-physics-remote/netz-gpu/datensaetze
FILME="schwerewelle-v licht-linse-v qball-fall-v drehrahmen-360-v"
HERKUNFT="netzgpu 0.1, Finns gefuelltes Tetraedernetz V, synthetische Modellrechnung"

ssh -o BatchMode=yes $H "mkdir -p $Z/js $Z/vendor $Z/bilder $Z/data $W/werkzeug"
rsync -a --delete "$V/js/" "$H:$Z/js/"
rsync -a --delete "$V/vendor/" "$H:$Z/vendor/"
rsync -a "$V/stil.css" "$V/schriften.css" "$O/index.html" "$O/ansicht.html" "$O/start.css" "$O/LIZENZEN.txt" "$H:$Z/"
rsync -a --delete "$O/bilder/" "$H:$Z/bilder/"
rsync -a "$O/manifest-bereinigen.jq" "$H:$W/werkzeug/"

for f in $FILME; do
  ssh -o BatchMode=yes $H "set -euo pipefail
    rm -rf '$Z/data/$f.neu'
    cp -a '$Q/$f' '$Z/data/$f.neu'
    jq --arg herkunft '$HERKUNFT' -f '$W/werkzeug/manifest-bereinigen.jq' '$Q/$f/manifest.json' > '$Z/data/$f.neu/manifest.json'
    jq empty '$Z/data/$f.neu/manifest.json'
    rm -rf '$Z/data/$f'
    mv '$Z/data/$f.neu' '$Z/data/$f'"
  echo "kopiert und bereinigt: $f"
done

# Kontrolle: keine internen Pfade oder Kennungen in der oeffentlichen Fassung (Binaerdateien ausgenommen)
ssh -o BatchMode=yes $H "cd '$Z' && if grep -rIl --exclude='*.f32' --exclude='*.u32' -e '/home/' -e 'fmhc-physics' -e 'fmh@' -e '/review' -e 'UEBERLEITUNG' -e '192\.168\.' -e 'netz-gpu/lauf' . ; then echo 'FEHLER: interne Angaben gefunden (Dateien oben)'; exit 1; else echo 'Kontrolle: keine internen Pfade oder Kennungen'; fi
  for f in $FILME; do jq -c '{titel, quelle}' data/\$f/manifest.json; done
  du -sh . data/* | sed 's#^#  #'"
