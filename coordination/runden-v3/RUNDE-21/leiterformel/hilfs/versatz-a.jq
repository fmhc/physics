# Nachtraeglich [H], keine Wertung: Radiusversatz a, mit dem Delta(k_innen (R + a)) = pi waere
# (ohne McMahon-Term): a = pi Rest / (-(k_n+1 - k_n)). Nur l = 0.
[.paare[] | select(.l == 0) | {k, R_n, rest, a: (3.141592653589793 * .rest / (.k_n - .k_n1))}]
| group_by(.k) | map({k: .[0].k, n: length, a_erstes: (.[0].a), a_letztes: (.[-1].a), R_letztes: (.[-1].R_n),
  a_je_paar: [.[] | (.a * 100 | round / 100)]})
