# PHASE-3D-BLIND (Runde 31): mechanische Auswertung nach PLAN.md Abschnitt 6 und Ausgabe sprossen.json (Abschnitt 7).
# Aufruf (lokal, nur jq): jq -n -f auswertung.jq lauf-69/lauf/*/suche.json lauf-69/rauch2/*/suche.json
def betrag: if . == null then null elif . < 0 then -. else . end;
def w0: if . == null then null else (.wurzeln // [])[0] end;
# [N] Rauschmass mit der Steigung der weiten h004-Startklammer (die Endklammer liegt bei beta = 1/2 im Rauschen)
def steig_start($w4): if $w4 == null or $w4.s_start == null then null
  else ($w4.s_start[1] - $w4.s_start[0]) / ($w4.klammer_start[1] - $w4.klammer_start[0]) end;
def rausch($w; $w4): steig_start($w4) as $st
  | if $w == null or $w.terme_a_max == null or $st == null or $st == 0 then null
    else 1e-15 * $w.terme_a_max / ($st | betrag) end;
[inputs | {f: input_filename, d: .}] as $alle
| def datei($n): ([$alle[] | select(.f | endswith("/" + $n + "/suche.json")) | .d.ergebnisse.suche] | .[0]);
  def lauf($n): ([$alle[] | select(.f | endswith("/" + $n + "/suche.json")) | .d] | .[0]);
  [ {name: "b05-n16", beta: 0.5, index: 16, fenster: 1}, {name: "b05-n17", beta: 0.5, index: 17, fenster: 2},
    {name: "b05-n18", beta: 0.5, index: 18, fenster: 3}, {name: "b1-k0", beta: 1.0, index: 0, fenster: 1},
    {name: "b1-km1", beta: 1.0, index: -1, fenster: 2}, {name: "b1-km2", beta: 1.0, index: -2, fenster: 3} ] as $liste
| [ $liste[] as $sp
    | datei($sp.name + "-h004") as $h4 | datei($sp.name + "-h002") as $h2 | datei($sp.name + "-u004") as $u4
    | datei($sp.name + "-rand") as $rd
    | ($h4 | w0) as $w4 | ($h2 | w0) as $w2 | ($u4 | w0) as $wu | ($rd | w0) as $wr
    | (if $sp.beta == 0.5 then 0.5 else 0.75 end) as $om
    | ($w2.x_stern // null) as $x2 | ($w4.x_stern // null) as $x4
    | (if $x2 != null and $x4 != null then (($x2 - $x4) | betrag) + ([$w2.breite_end, $w4.breite_end] | max) else null end) as $uns
    | ($wu.rechteck // {}) as $re
    | {beta: $sp.beta, index: $sp.index, name: $sp.name, fenster: $sp.fenster,
       fenster_u: $h4.fenster_u,
       omega2: $x2, eps: (if $x2 then $x2 - $om else null end), inv_eps: (if $x2 then 1 / ($x2 - $om) else null end),
       umlauf: $re.umlauf_kreuzung, umlauf_phase: $re.umlauf, rechteck_aufgeloest: $re.aufgeloest,
       rechteck_max_sprung: $re.max_sprung, rechteck_runden: $re.runden_benutzt, rechteck_punkte: $re.punkte,
       rechteck_zeilen: [$re.x_lo, $re.x_hi], rechteck_rho: [$re.rho_lo, $re.rho_hi],
       R_halb: $w2.R_wand_stern, R_halb_konvention: "S(R) = S_c/2, S_c = 1/(2 beta) (RUNDE-26)",
       R_halb_S0: $w2.R_halb_S0_stern, rho: $w2.rho_stern,
       unsicherheit_omega2: $uns,
       unsicherheit_inv_eps: (if $uns != null and $x2 != null then $uns / (($x2 - $om) * ($x2 - $om)) else null end),
       gitter_vergleich: {omega2_h004: $x4, omega2_h002: $x2,
                          differenz_h002_minus_h004: (if $x2 != null and $x4 != null then $x2 - $x4 else null end),
                          endklammer_h004: $w4.breite_end, endklammer_h002: $w2.breite_end,
                          schritte_h004: $w4.schritte, schritte_h002: $w2.schritte,
                          rho_h004: $w4.rho_stern, rho_h002: $w2.rho_stern,
                          R_halb_h004: $w4.R_wand_stern,
                          randprobe_omega2: $wr.x_stern, randprobe_R_aus: $rd.R_aus, h004_R_aus: $h4.R_aus,
                          h002_R_aus: $h2.R_aus,
                          randprobe_minus_h004: (if $wr.x_stern != null and $x4 != null then $wr.x_stern - $x4 else null end)},
       rauschmass_omega2_h004: rausch($w4; $w4), rauschmass_omega2_h002: rausch($w2; $w4),
       steigung_s_start_h004: steig_start($w4),
       steigung_s_h002: $w2.steigung_s_x, terme_a_h002: $w2.terme_a_max,
       kernwachstum_kandidat_h002: $w2.wachstum_kandidat, kernwachstum_kandidat_h004: $w4.wachstum_kandidat,
       pb1: {a: (($h4.n_wechsel_start // 0) == 1 and ($h4.wechsel_start[0].ast_konsistent // false)),
             b: ($w4.breite_end != null and $w4.breite_end <= 1e-9 and $w2.breite_end != null and $w2.breite_end <= 1e-9
                 and $x2 != null and $x4 != null and (($x2 - $x4) | betrag) <= 1e-6),
             c: (($u4.n_wechsel_start // 0) == 1 and $re.umlauf_kreuzung != null
                 and ((($re.umlauf_kreuzung | betrag) - 1) | betrag) < 0.1)},
       nullstellen_je_startzeile_h004: [$h4.zeilen_start[]?.n_nullstellen],
       s_startzeilen_h004: [$h4.zeilen_start[]? | {x, u, s, s_roh: .ziel.s_roh, rho}]} ] as $sprossen
| [ {name: "b05-pb0", beta: 0.5, x_ref: 0.528469}, {name: "b1-pb0", beta: 1.0, x_ref: 0.780879} ] as $pb0liste
| [ $pb0liste[] as $p
    | datei($p.name + "-h002") as $h2 | datei($p.name + "-h004") as $h4
    | datei("pb0-" + (if $p.beta == 0.5 then "b05" else "b1" end) + "-u004") as $u4
    | ($h2 | w0) as $w2 | ($h4 | w0) as $w4 | ($u4 | w0) as $wu
    | {name: $p.name, beta: $p.beta, x_ref: $p.x_ref, omega2_h002: $w2.x_stern, omega2_h004: $w4.x_stern,
       endklammer_h002: $w2.breite_end, endklammer_h004: $w4.breite_end,
       delta_h002: (if $w2.x_stern != null then $w2.x_stern - $p.x_ref else null end),
       delta_h004: (if $w4.x_stern != null then $w4.x_stern - $p.x_ref else null end),
       R_halb_h002: $w2.R_wand_stern, rho_h002: $w2.rho_stern, rauschmass_omega2_h002: rausch($w2; $w4),
       rauschmass_omega2_h004: rausch($w4; $w4),
       umlauf: $wu.rechteck.umlauf_kreuzung, umlauf_phase: $wu.rechteck.umlauf,
       rechteck_aufgeloest: $wu.rechteck.aufgeloest, rechteck_max_sprung: $wu.rechteck.max_sprung,
       u004_wechsel: $u4.n_wechsel_start,
       bestanden: ($w2.x_stern != null and $w2.breite_end != null and $w2.breite_end <= 1e-9
                   and (($w2.x_stern - $p.x_ref) | betrag) < 1e-6)} ] as $pb0
| (reduce (0.5, 1.0) as $b ({};
    . + {(if $b == 0.5 then "beta_0.5" else "beta_1" end):
         (([($pb0[] | select(.beta == $b) | .umlauf)] + [($sprossen[] | select(.beta == $b) | .umlauf)]) as $u
          | {umlaeufe: $u,
             wechselnd: (($u | length) == 4 and ($u | all(. != null))
                         and ([range(0; 3) as $i | ($u[$i] * $u[$i + 1]) < 0] | all))})})) as $wechsel
| {sprossen: $sprossen,
   pb0: {je_sprosse: $pb0, eingetroffen: ($pb0 | all(.bestanden))},
   pb1: {je_fenster: [$sprossen[] | {name, a: .pb1.a, b: .pb1.b, c: .pb1.c}], wechsel: $wechsel,
         eingetroffen: (($sprossen | all(.pb1.a and .pb1.b and .pb1.c)) and ($wechsel | to_entries | all(.value.wechselnd)))},
   laeufe: [$alle[] | {datei: .f, start: .d.start, ende: .d.ende, sek: .d.sek, entfallen: .d.entfallen,
                       fehler: (.d.fehler // .d.ergebnisse.suche.fehler // null)}]}
