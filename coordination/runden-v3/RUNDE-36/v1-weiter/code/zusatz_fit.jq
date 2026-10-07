# V-1-WEITER, Zusatz (beschreibend, kein Urteil): Anpassung ln P gegen 1/sqrt|eps| und gegen ln|eps|.
# Aufruf: jq -s -f zusatz_fit.jq <json-Dateien mit eps < 0>   (je Datei die Nullstelle naechst rho_WB)
def RWB: 1.7734530718064692;
def linfit(xs; ys):
  (xs | length) as $n | (xs | add / $n) as $mx | (ys | add / $n) as $my
  | ([range(0; $n) as $i | (xs[$i] - $mx) * (ys[$i] - $my)] | add) as $sxy
  | ([range(0; $n) as $i | (xs[$i] - $mx) * (xs[$i] - $mx)] | add) as $sxx
  | ($sxy / $sxx) as $b | ($my - $b * $mx) as $a
  | {steigung: $b, achse: $a,
     rms: (([range(0; $n) as $i | (ys[$i] - $a - $b * xs[$i]) | . * .] | add / $n) | sqrt)};
[.[] | select(.eps < 0) | (.nullstellen | min_by((.rho_z - RWB) | fabs)) as $z
 | {eps, xr: .xr_bg, bg: .hintergrund.art, amp: $z.amp_neu_aus_max, amp10: $z.lose_10rtol.amp_neu_aus_max,
    P: $z.P_neu_aus,
    stabil: ((($z.lose_10rtol.amp_neu_aus_max - $z.amp_neu_aus_max) | fabs) <= 0.2 * $z.amp_neu_aus_max)}]
| sort_by(.eps) as $alle
| [$alle[] | select(.stabil and .P > 0)] as $ok
| {punkte: $alle,
   n_stabil: ($ok | length),
   exp_form: (if ($ok | length) >= 3 then linfit([$ok[] | 1 / (.eps | fabs | sqrt)]; [$ok[] | .P | log]) else null end),
   potenz_form: (if ($ok | length) >= 3 then linfit([$ok[] | .eps | fabs | log]; [$ok[] | .P | log]) else null end)}
