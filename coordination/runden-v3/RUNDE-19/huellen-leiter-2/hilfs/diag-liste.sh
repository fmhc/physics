#!/bin/bash
# PLAN-NACHTRAG-1: Diagnose-Punkte D1 (zusaetzliche Stellen) und D2 (bekannte Stellen mit umgekehrtem Zellen-Umlauf)
# Aufruf: diag-liste.sh <stufe> [<stufe>]; Zuordnung eins zu eins (hilfs/diag-vergleich.jq)
B=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-19/huellen-leiter-2
V=/home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-18/huellen-leiter/aus/laeufe
for st in "$@"; do
  for f in $B/aus/laeufe/paar-st$st-0*.json; do jq -c '. as $p | select($p.i <= 109) | .punkte[] | {i: $p.i, k, w2, rho, R, u: .umlauf_zelle, gap, dw2: ($p.w2a - $p.w2b)}' $f; done > $B/hilfs/neu-st$st.jsonl
  for f in $V/paar-st$st-0*.json; do jq -c '. as $p | select($p.i <= 109) | .punkte[] | {i: $p.i, k, w2, rho, R, u: .umlauf_zelle, gap, dw2: ($p.w2a - $p.w2b)}' $f; done > $B/hilfs/alt-st$st.jsonl
  jq -n --slurpfile N $B/hilfs/neu-st$st.jsonl --slurpfile A $B/hilfs/alt-st$st.jsonl -f $B/hilfs/diag-vergleich.jq > $B/hilfs/diag-vergleich-st$st.json
  jq -c '{punkte: ([.zusaetzlich | sort_by(.R)[] | {name: "D1-k\(.k)-R\(.R*100|round/100)", w2, rho, gap, dw2_zeile: .dw2, k, R, umlauf_zelle: .u}]
                    + [.umgekehrt | sort_by(.R)[0:4][] | {name: "D2-k\(.k)-R\(.R*100|round/100)", w2, rho, gap, dw2_zeile: .dw2, k, R, umlauf_zelle: .u}])}' \
     $B/hilfs/diag-vergleich-st$st.json > $B/hilfs/diag-punkte-st$st.json
  echo "St$st: $(jq -c '{n_neu, n_alt, n_zugeordnet, zus: (.zusaetzlich|length), umg: (.umgekehrt|length), fehl: (.fehlend|length)}' $B/hilfs/diag-vergleich-st$st.json) Punkte: $(jq '.punkte|length' $B/hilfs/diag-punkte-st$st.json)"
done
