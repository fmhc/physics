# B-BALL-2b Auswertung nach KARTE-2B-LETZTES-VIERTEL.md (t = 0,9).
# Aufruf: jq -s -f auswertung2b.jq lauf-69/aus2b/t0.9-h0.02.json lauf-69/aus2b/t0.9-h0.01.json
def imfenster: .x >= 0.8765 and .x <= 0.9256 and .rho >= 1.810 and .rho <= 1.838;
def kand: [.kandidaten[]? | select(.lokal != null and .rechteck.umlauf != null) |
  {x: .lokal.x_stern, rho: .lokal.rho_stern, klammer: .lokal.klammer_breite, u: .rechteck.umlauf,
   u_roh: .rechteck.umlauf_roh, kreuzung: .rechteck.umlauf_kreuzung, aufl: .rechteck.aufgeloest,
   sprung: .rechteck.max_sprung}];
def stufe:
  {h: .h, t: .argumente.t, datei: .argumente.name, laufzeit: .laufzeit, entfallen: (.budget_entfallen | length),
   zeilen_gueltig: ([.mitglieder[] | select(.gueltig)] | length),
   streifen: (.streifen | length), streifen_aufl_u0: ([.streifen[] | select(.umlauf == 0 and .aufgeloest)] | length),
   streifen_u_ne0: [.streifen[] | select(.umlauf != null and .umlauf != 0) | {i, x_lo, x_hi, umlauf, aufgeloest, max_sprung}],
   streifen_fehlend: ([.streifen[] | select(.umlauf == null)] | length),
   max_sprung_streifen: ([.streifen[].max_sprung | select(. != null)] | max),
   wechsel: [.vorzeichenwechsel[] | {x1, x2, rho1, rho2, s1, s2, richtung}],
   wechsel_im_fenster: [.vorzeichenwechsel[] | {x: ((.x1 + .x2) / 2), rho: ((.rho1 + .rho2) / 2)} | select(imfenster)],
   kand: kand,
   gamma: [.mitglieder[] | select(.gueltig) | .x as $x | .wurzeln[] | select(.Gamma != null and .rho > 1.0) |
           {x: $x, rho, Gamma}]};
map(stufe) | sort_by(-.h) as $st |
($st | map(select(.h == 0.02)) | .[0]) as $a |
($st | map(select(.h == 0.01)) | .[0]) as $c |
([ $a.kand[]? as $p | $c.kand[]? as $q |
   select($p.aufl and $q.aufl and ($p.u | fabs) == 1 and ($q.u | fabs) == 1 and ($p | imfenster) and ($q | imfenster)
          and (($p.x - $q.x) | fabs) <= 1e-4 and (($p.rho - $q.rho) | fabs) <= 1e-4) |
   {x_h002: $p.x, rho_h002: $p.rho, x_h001: $q.x, rho_h001: $q.rho, u_h002: $p.u, u_h001: $q.u,
    sprung_h002: $p.sprung, sprung_h001: $q.sprung, dx_stufen: (($p.x - $q.x) | fabs), drho_stufen: (($p.rho - $q.rho) | fabs),
    dx_quadratisch: ($p.x - 0.9022), drho_quadratisch: ($p.rho - 1.8252),
    quadratisch_getroffen: ((($p.x - 0.9022) | fabs) <= 0.012 and (($p.rho - 1.8252) | fabs) <= 0.008)} ]) as $treffer |
($a != null and $c != null) as $beide |
($beide and ([$a, $c] | all(.wechsel_im_fenster == [] and .streifen == 17 and .streifen_aufl_u0 == 17
                             and .streifen_fehlend == 0 and ([.kand[] | select(.u != 0)] | length) == 0))) as $nicht |
(if ($treffer | length) > 0 and $a != null then
   ($treffer[0].rho_h002 as $r | [$a.gamma[] | select(((.rho - $r) | fabs) < 0.05)] | min_by(.Gamma))
 else null end) as $gmin |
{ausgang: (if ($treffer | length) > 0 then "Gefunden (Kontinuitaet im letzten Viertel traegt)"
           elif $nicht then "Nicht gefunden" else "Unentschieden" end),
 treffer: $treffer, breitenminimum_h002: $gmin, stufen: $st}
