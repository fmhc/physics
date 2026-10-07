# Tabelle fuer ERGEBNIS.md aus lauf-69/ausgabe/bio28c_auswertung.json
# Aufruf: jq -r -f tabelle.jq bio28c_auswertung.json | sed -E 's/([0-9])\.([0-9])/\1,\2/g'
def r3: (. * 1000 | round) / 1000;
def r4: (. * 10000 | round) / 10000;
.laeufe | to_entries[] | .key as $n | .value.tabelle | to_entries[]
| "| \($n) | \(.key) | \(.value.n_gebiete) | \(.value.L | r4) | \(.value.a | r3) | \(.value.b | r3) | \(.value.c | r3) | \(.value.s | r4) | \(.value.a_Z | r3) / \(.value.b_Z | r3) / \(.value.c_Z | r3) |"
