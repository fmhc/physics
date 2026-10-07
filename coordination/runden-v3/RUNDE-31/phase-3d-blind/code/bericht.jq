# PHASE-3D-BLIND (Runde 31): Markdown-Tabellen aus auswertung.json (nur Darstellung, keine Wertung).
# Aufruf: jq -r -f bericht.jq lauf-69/auswertung.json
def r($n): if . == null then "-" else ((. * pow(10; $n) | round) / pow(10; $n) | tostring | sub("\\."; ",")) end;
def e($n): if . == null then "-" else (. as $x | ($x | if . < 0 then -. else . end) as $a
  | if $a == 0 then "0" else (($a | log10 | floor) as $k | (($x / pow(10; $k)) * pow(10; $n) | round / pow(10; $n)
  | tostring | sub("\\."; ",")) + "e" + ($k | tostring)) end) end;
def vz: if . == null then "-" elif . > 0 then "+" + r(0) else r(0) end;
def ja: if . == true then "ja" elif . == false then "nein" else "-" end;
"| Sprosse | omega^2 (h = 0,02) | eps | 1/eps | Umlauf Kreuzung / Phase (Sprung, Runden, aufgeloest) | R_halb | rho | Unsicherheit omega^2 / 1/eps (Plan) | Rauschmass omega^2 / 1/eps | h002 - h004 | Randprobe - h004 | Kernwachstum |",
"|---|---|---|---|---|---|---|---|---|---|---|---|",
(.sprossen[] | (if .eps then (.eps * .eps) else null end) as $e2
 | "| \(.name) | \(.omega2 | r(10)) | \(.eps | r(9)) | \(.inv_eps | r(5)) | \(.umlauf | vz) / \(.umlauf_phase | r(3)) (\(.rechteck_max_sprung | r(3)) rad, \(.rechteck_runden // "-"), \(.rechteck_aufgeloest | ja)) | \(.R_halb | r(5)) | \(.rho | r(8)) | \(.unsicherheit_omega2 | e(1)) / \(.unsicherheit_inv_eps | e(1)) | \(([.rauschmass_omega2_h002, .rauschmass_omega2_h004] | max) | e(1)) / \((if $e2 then ([.rauschmass_omega2_h002, .rauschmass_omega2_h004] | max) / $e2 else null end) | e(1)) | \(.gitter_vergleich.differenz_h002_minus_h004 | e(1)) | \(.gitter_vergleich.randprobe_minus_h004 | e(1)) | \(.kernwachstum_kandidat_h002 | e(1)) |"),
"",
"| Sprosse | omega^2 h = 0,04 | 1/eps h = 0,04 | Endklammer h = 0,04 / 0,02 (Schritte) | R aussen h = 0,04 / 0,02 / Randprobe | R_halb_S0 |",
"|---|---|---|---|---|---|",
(.sprossen[] | "| \(.name) | \(.gitter_vergleich.omega2_h004 | r(10)) | \((if .gitter_vergleich.omega2_h004 then 1 / (.gitter_vergleich.omega2_h004 - (if .beta == 0.5 then 0.5 else 0.75 end)) else null end) | r(5)) | \(.gitter_vergleich.endklammer_h004 | e(1)) / \(.gitter_vergleich.endklammer_h002 | e(1)) (\(.gitter_vergleich.schritte_h004 // "-") / \(.gitter_vergleich.schritte_h002 // "-")) | \(.gitter_vergleich.h004_R_aus | r(2)) / \(.gitter_vergleich.h002_R_aus | r(2)) / \(.gitter_vergleich.randprobe_R_aus | r(2)) | \(.R_halb_S0 | r(5)) |"),
"",
"| PB0 | x_ref | omega^2 h = 0,02 | Delta h = 0,02 | omega^2 h = 0,04 | Delta h = 0,04 | Endklammer h = 0,02 | Rauschmass | Umlauf Kreuzung / Phase | R_halb | rho | bestanden |",
"|---|---|---|---|---|---|---|---|---|---|---|---|",
(.pb0.je_sprosse[] | "| \(.name) | \(.x_ref | r(6)) | \(.omega2_h002 | r(10)) | \(.delta_h002 | e(2)) | \(.omega2_h004 | r(10)) | \(.delta_h004 | e(2)) | \(.endklammer_h002 | e(1)) | \(([.rauschmass_omega2_h002, .rauschmass_omega2_h004] | max) | e(1)) | \(.umlauf | vz) / \(.umlauf_phase | r(3)) | \(.R_halb_h002 | r(5)) | \(.rho_h002 | r(8)) | \(.bestanden | ja) |"),
"",
"| Fenster | (a) ein Wechsel, Ast konsistent | (b) Wurzel beide Stufen (Endklammer <= 1e-9), Lagen auf 1e-6 | (c) u004 Wechsel und Umlauf +-1 |",
"|---|---|---|---|",
(.pb1.je_fenster[] | "| \(.name) | \(.a | ja) | \(.b | ja) | \(.c | ja) |"),
"",
"Umlaeufe (bekannte Sprosse, Fenster 1, 2, 3): beta = 1/2 \(.pb1.wechsel["beta_0.5"].umlaeufe | map(vz) | join(", ")) -> wechselnd \(.pb1.wechsel["beta_0.5"].wechselnd | ja); beta = 1 \(.pb1.wechsel["beta_1"].umlaeufe | map(vz) | join(", ")) -> wechselnd \(.pb1.wechsel["beta_1"].wechselnd | ja)",
"PB0 eingetroffen: \(.pb0.eingetroffen | ja); PB1 eingetroffen: \(.pb1.eingetroffen | ja)"
