#!/bin/bash
# LEITER-BETA: mechanische Auswertung (PLAN.md Abschnitt 7). Lokal, nur bash und jq, im Ordner leiter-beta:
#   bash auswertung.sh [lauf-69]  ->  <ordner>/auswertung/{k0.json, gesamt.json, auswertung.json}
# Erwartet <ordner>/k0-h004, k0-h002, kandidaten.json und die Phase-2-Ordner c<k>-h004, c<k>-h002 (je praez.json).
set -eu
B=${1:-lauf-69}
H=$(cd "$(dirname "$0")" && pwd)
A=$B/auswertung
mkdir -p "$A"
jq -n --slurpfile a "$B/k0-h004/praez.json" --slurpfile b "$B/k0-h002/praez.json" -f "$H/k0.jq" > "$A/k0.json"
{
  printf '{"kand":'
  cat "$B/kandidaten.json"
  printf ',"laeufe":{'
  erst=1
  for f in "$B"/c*-h00?/praez.json; do
    [ -e "$f" ] || continue
    n=$(basename "$(dirname "$f")")
    [ $erst = 1 ] || printf ','
    erst=0
    printf '"%s":' "$n"
    jq -c '{x_pol: .argumente.x_pol, h: .ergebnisse.praez.h,
            p: (.ergebnisse.praez | {profile_vollstaendig, x, ziel_wechsel, rechtecke})}' "$f"
  done
  printf '}}'
} > "$A/gesamt.json"
jq -f "$H/auswertung.jq" "$A/gesamt.json" > "$A/auswertung.json"
jq -r '"K0 bestanden: \(.bestanden) (h004 \(.h004.ok), h002 \(.h002.ok))"' "$A/k0.json"
jq -r '.kandidaten[] | "k=\(.k) \(.ast) x_grob=\(.x_grob) -> \(.status) x=\(.x) eps=\(.eps) rho=\(.rho) c=\(.c_wert) U=\(.umlauf) dx=\(.d_x_stufen) drho=\(.d_rho_stufen) [h004: \(.h004.grund // "")] [h002: \(.h002.grund // "")]"' "$A/auswertung.json"
jq -r '"Folgen \(.folgen); gewertete Folge \([.folge[] | .k]); Schritte \([.schritte[] | .schritt])",
       "LB1 \(.LB1)", "LB2 \(.LB2)", "LB3 eingetroffen \(.LB3.eingetroffen) (auswertbar \(.LB3.auswertbar))"' "$A/auswertung.json"
