#!/bin/bash
# Bildschirmfoto der Netz-Ansicht mit headless Chrome auf der echten GPU (ANGLE ueber Vulkan).
# Aufruf: bash bilder/aufnehmen.sh <name> '<query>' [virtuelle ms] [basis-url]
#   z. B.  bash bilder/aufnehmen.sh probe '?probe=1&bild=6' 12000
# Jedes Foto bekommt ein frisches Chrome-Profil: Mit warmem Cache lief die virtuelle Zeit davon,
# bevor die Ansicht aufgebaut war. Profil und Temp-Dateien liegen unter netz-viewer/.chrome-*, nicht in /tmp.
set -u
NAME=${1:?Name}
QUERY=${2:?Query}
BUDGET=${3:-12000}
BASIS=${4:-http://192.168.178.69:8777/viewer/}
V=$(cd "$(dirname "$0")/.." && pwd)
rm -rf "$V/.chrome-profil"
mkdir -p "$V/.chrome-tmp" "$V/.chrome-profil"
TMPDIR="$V/.chrome-tmp" timeout 180 google-chrome-stable --headless=new --disable-dev-shm-usage --hide-scrollbars \
  --use-angle=vulkan --enable-features=Vulkan --enable-gpu --ignore-gpu-blocklist \
  --user-data-dir="$V/.chrome-profil" --window-size=1500,900 \
  --screenshot="$V/bilder/$NAME.png" --virtual-time-budget="$BUDGET" "$BASIS$QUERY" > "$V/.chrome-tmp/chrome-$NAME.log" 2>&1
echo "$NAME rc=$?"
