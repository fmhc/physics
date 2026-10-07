# AFM-BREITE: Median von ln Gamma je Mitglied (Pole mit 1,0 <= Re rho <= 1,95), Vergleich mit dem Gesetz der Karte
def gesetz(u): 2.549 - 2.860 * u;
def median: sort | length as $n | if $n == 0 then null elif ($n % 2) == 1 then .[($n - 1) / 2] else ((.[$n / 2 - 1] + .[$n / 2]) / 2) end;
.kappa as $k | .mitglieder[] |
  (1 / ((1 - .x) | sqrt)) as $u |
  ([.wurzeln[] | select(.rho >= 1.0 and .rho <= 1.95 and .Gamma != null and .Gamma > 0) | (.Gamma | log)] | median) as $m |
  {kappa: $k, x: .x, u: $u, n_pole: ([.wurzeln[] | select(.rho >= 1.0 and .rho <= 1.95 and .Gamma != null)] | length),
   ln_med: $m, gamma_med: (if $m == null then null else ($m | exp) end), ln_gesetz: gesetz($u),
   dlog10: (if $m == null then null else (($m - gesetz($u)) / (10 | log)) end)}
