#!/bin/bash
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
# Prueft die oeffentliche Fassung auf der .69, waehrend dort der Vorschau-Server laeuft (kleintest.sh, Wurzel public/).
# 1. Vorschaubilder (Kinomodus) aufnehmen und hochladen
# 2. Testkopien mit derselben Richtlinie als <meta> (ohne frame-ancestors) anlegen
# 3. Startseite und vier Filme unter der Richtlinie fotografieren, Konsole und DOM auf CSP-Verstoesse pruefen
# 4. Testkopien wieder entfernen (sie gehoeren nicht in die oeffentliche Fassung)
set -uo pipefail
V=$(cd "$(dirname "$0")/.." && pwd)
O="$V/oeffentlich"
H=fmh@192.168.178.69
Z=/home/fmh/fmhc-physics-remote/netz-web/public/netz
URL=http://192.168.178.69:8777/netz
B="$V/bilder/oeffentlich"
L="$V/.chrome-tmp"
mkdir -p "$B" "$L" "$O/bilder"

declare -A ANSICHT=(
  [schwerewelle-v]='ebenen=netz,energie&schnitt=scheibe,z,6,1&blick=oben&skala=bild&bild=12'
  [licht-linse-v]='ebenen=netz,energie,takt&schnitt=scheibe,z,6,1.2&blick=oben&skala=bild&bild=21'
  [qball-fall-v]='ebenen=netz,skalar_betrag2,takt&schnitt=scheibe,y,6,1.2&blick=vorn&bild=12'
  [drehrahmen-360-v]='ebenen=rahmen,energie&schnitt=scheibe,z,6,1&blick=oben&rahmenanteil=1&skala=bild&bild=6'
)
FILME="schwerewelle-v licht-linse-v qball-fall-v drehrahmen-360-v"

chrome() {  # chrome <groesse> <budget-ms> <weitere Argumente ...>
  local groesse=$1 budget=$2
  shift 2
  rm -rf "$V/.chrome-profil"
  mkdir -p "$V/.chrome-profil"
  TMPDIR="$L" timeout 120 google-chrome-stable --headless=new --disable-dev-shm-usage --hide-scrollbars \
    --use-angle=vulkan --enable-features=Vulkan --enable-gpu --ignore-gpu-blocklist \
    --enable-logging=stderr --v=0 --user-data-dir="$V/.chrome-profil" --window-size="$groesse" \
    --virtual-time-budget="$budget" "$@"
}

echo "== 1. Vorschaubilder"
for f in $FILME; do
  chrome 1200,750 30000 --screenshot="$O/bilder/$f.webp" "$URL/ansicht.html?d=data/$f/manifest.json&${ANSICHT[$f]}&ui=0&foto=1" > "$L/plakat-$f.log" 2>&1
  echo "  $f: rc=$? $(stat -c %s "$O/bilder/$f.webp") Byte"
done
rsync -a "$O/bilder/" "$H:$Z/bilder/"

echo "== 2. Testkopien mit Meta-Richtlinie"
sed '/^<head>$/r '"$O/pruefung/csp-kopf.html" "$O/index.html" > "$L/csp-test-index.html"
sed '/^<head>$/r '"$O/pruefung/csp-kopf.html" "$O/ansicht.html" > "$L/csp-test-ansicht.html"
grep -c "Content-Security-Policy" "$L/csp-test-index.html" "$L/csp-test-ansicht.html"
scp -q "$L/csp-test-index.html" "$L/csp-test-ansicht.html" "$O/pruefung/csp-zaehler.js" "$H:$Z/"

echo "== 3. Fotos und Konsole unter der Richtlinie"
pruefe() {  # pruefe <name> <groesse> <budget> <adresse>
  local name=$1 groesse=$2 budget=$3 adresse=$4
  chrome "$groesse" "$budget" --screenshot="$B/$name.png" "$adresse" > "$L/$name-foto.log" 2>&1
  chrome "$groesse" "$budget" --dump-dom "$adresse" > "$L/$name-dom.html" 2> "$L/$name-dom.log"
  local zahl_dom verstoss_log zaehler
  zahl_dom=$(grep -o 'data-csp-verstoesse="[0-9]*"' "$L/$name-dom.html" | head -1)
  verstoss_log=$(cat "$L/$name-foto.log" "$L/$name-dom.log" | grep -c -i -e 'CSP-VERSTOSS' -e 'Content Security Policy' -e 'Refused to')
  zaehler=$(cat "$L/$name-foto.log" "$L/$name-dom.log" | grep -c 'CSP-ZAEHLER aktiv')
  echo "  $name: DOM ${zahl_dom:-kein Zaehlerstand}, Konsolenzeilen mit Verstoss: $verstoss_log, Zaehler gestartet: $zaehler"
}
pruefe csp-startseite 1500,2400 8000 "$URL/csp-test-index.html"
for f in $FILME; do
  pruefe "csp-$f" 1500,900 30000 "$URL/csp-test-ansicht.html?d=data/$f/manifest.json&${ANSICHT[$f]}&foto=1"
done

echo "== 4. Testkopien entfernen"
ssh -o BatchMode=yes $H "rm -f '$Z/csp-test-index.html' '$Z/csp-test-ansicht.html' '$Z/csp-zaehler.js'; ls '$Z'"
