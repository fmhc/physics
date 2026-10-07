# QCA-WINDUNG-1: Tabellen aus den Ergebnisdateien (nur Lesen, jq). Aufruf: jq -r -f tabellen.jq lauf/DATEI.json
# Ort eines Weyl-Punkts aus t (Zellkoordinaten): Gamma (0,0,0), P (1/4,...), H (1/2,...), P' (3/4,...), sonst "allg."
def ort: .t as $t
  | ($t | map(. - ($t[0])) | map(if . > 0.5 then . - 1 elif . < -0.5 then . + 1 else . end) | map(fabs) | max) as $d
  | if $d > 1e-6 then "allg."
    else ($t[0] | if fabs < 1e-6 or fabs > 1 - 1e-6 then "Gamma" elif fabs - 0.25 | fabs < 1e-6 then "P"
          elif fabs - 0.5 | fabs < 1e-6 then "H" elif fabs - 0.75 | fabs < 1e-6 then "P'" else "allg." end) end;
.automaten[]
| . as $a
| {name, s, inv: .inversion.inversion, trivial, W3: (.w3.gitter // {} | to_entries | map("\(.key):\(.value.W3 * 1e6 | round / 1e6)") | join(" ")),
   konv: .w3.konvergiert, anz: .weyl.anzahl, voll: .weyl.vollstaendig, global: .weyl.global,
   netto: .weyl.luecken.netto_je_luecke, summe: .weyl.summe_chi, takt: .weyl.takt_tabelle,
   orte: ((.weyl.punkte // []) | map({o: ort, takt, chi}) | group_by(.o) | map({(.[0].o): {n: length, netto: (map(.chi) | add)}}) | add)}
| tojson
