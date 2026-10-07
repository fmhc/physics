# REGGE-SCHAUM-1, mechanische Urteile nach KARTE.md. Geschrieben vor dem Ende der Hauptlaeufe.
# Aufruf: jq -n --slurpfile K K-R20-s1.json --slurpfile J J-R20-s1.json --slurpfile P1 P-R20-s1.json \
#            --slurpfile P2 P-R20-s2.json -f auswertung.jq
# Festlegungen (nach der Karte, vor den Ergebnissen):
#   - RS3: "Schale um r = 12" ist [12, 13), "bei r = 5" ist [5, 6) (Eintraege r = 12.5 bzw. 5.5).
#   - RS4: eingetroffen, wenn die SA-Rechnung konvergiert und ihr kleinster Wert > 0 ist. Konvergiert sie nicht, ist RS4
#     nicht auswertbar, auch wenn die Werte nahe null alle positiv sind.
#   - RS2: "RS1-Mittel" ist der Mittelwert der drei gewichteten Quadrattest-Werte desselben Netzes.
def schale($n; $r): ($n.newton.schalen[] | select(.r == $r));
def relstd($n; $r): (schale($n; $r) | .f_std / .f_mittel);
def gew($n): ([$n.quadrattest.x.gewichtet, $n.quadrattest.y.gewichtet, $n.quadrattest.z.gewichtet]);
def abs: if . < 0 then -. else . end;
($K[0]) as $k | ($J[0]) as $j | ($P1[0]) as $p1 | ($P2[0]) as $p2 |
[$k, $j, $p1, $p2] as $alle |
{
  RS0: {
    werte: {
      schlaefli_max: ([$alle[].kontrollen.schlaefli_rel] | max),
      symmetrie_max: ([$alle[].kontrollen.symmetrie_rel] | max),
      eins_max: ([$alle[].kontrollen.L_eins_rel] | max),
      linear_max: ([$alle[].kontrollen.L_linear_rel[]] | max),
      kuhn_schablone: $k.kontrollen.kuhn_schablone_max_abw,
      kuhn_a: $k.newton.a
    }
  },
  RS1: {werte: {P1_gew: gew($p1), P2_gew: gew($p2),
                P1_std: [$p1.quadrattest.x.std, $p1.quadrattest.y.std, $p1.quadrattest.z.std],
                P2_std: [$p2.quadrattest.x.std, $p2.quadrattest.y.std, $p2.quadrattest.z.std]}},
  RS2: {werte: {P1_a: $p1.newton.a, P2_a: $p2.newton.a,
                P1_1_durch_gew: (1 / (gew($p1) | add / 3)), P2_1_durch_gew: (1 / (gew($p2) | add / 3))}},
  RS3: {werte: {P1_12: relstd($p1; 12.5), P1_5: relstd($p1; 5.5), P2_12: relstd($p2; 12.5), P2_5: relstd($p2; 5.5)}},
  RS4: {werte: {P1_SA: $p1.eigen_kleinste_algebraisch, P2_SA: $p2.eigen_kleinste_algebraisch,
                P1_null: $p1.eigen_nahe_null, P2_null: $p2.eigen_nahe_null}}
}
| .RS0.urteil = (if (.RS0.werte.schlaefli_max <= 1e-10 and .RS0.werte.symmetrie_max <= 1e-10
                     and .RS0.werte.eins_max <= 1e-9 and .RS0.werte.linear_max <= 1e-9
                     and .RS0.werte.kuhn_schablone <= 1e-9 and ((.RS0.werte.kuhn_a - 1) | abs) <= 0.01)
                 then "eingetroffen" else "nicht eingetroffen" end)
| .RS1.urteil = (if ([.RS1.werte.P1_gew[], .RS1.werte.P2_gew[]] | all(((. - 1) | abs) <= 0.03))
                     and ([.RS1.werte.P1_std[], .RS1.werte.P2_std[]] | all(. > 0.10))
                 then "eingetroffen" else "nicht eingetroffen" end)
| .RS2.urteil = (if (((.RS2.werte.P1_a - 1) | abs) <= 0.05 and ((.RS2.werte.P2_a - 1) | abs) <= 0.05
                     and ((.RS2.werte.P1_a - .RS2.werte.P1_1_durch_gew) | abs) <= 0.03
                     and ((.RS2.werte.P2_a - .RS2.werte.P2_1_durch_gew) | abs) <= 0.03)
                 then "eingetroffen" else "nicht eingetroffen" end)
| .RS3.urteil = (if (.RS3.werte.P1_12 < 0.03 and .RS3.werte.P2_12 < 0.03
                     and .RS3.werte.P1_12 < .RS3.werte.P1_5 and .RS3.werte.P2_12 < .RS3.werte.P2_5)
                 then "eingetroffen" else "nicht eingetroffen" end)
| .RS4.urteil = (if ((.RS4.werte.P1_SA | type) != "array") or ((.RS4.werte.P2_SA | type) != "array")
                 then "nicht auswertbar"
                 elif ((.RS4.werte.P1_SA | min) > 0 and (.RS4.werte.P2_SA | min) > 0)
                 then "eingetroffen" else "nicht eingetroffen" end)
