# Numerische Korrektur nach QA-Abbruch

Die Kriterien in PLAN.md bleiben unverändert. Erster Lauf: 28 Spektren vollständig gespeichert (Basis l0/1/2, feines Gitter l0). Abbruch beim Rekonstruieren der nahezu nullfrequenten Translationsmode in full/grid/l1: Originalgleichungsresiduum 5,8143e-7 > 1e-7. Rohresultate, ursprünglicher Code und Journal unter initial-failure/ erhalten.

Die Formel t=(P−2ωq)/ν subtrahiert nahe einer Translationsnullrichtung nahezu gleiche Vektoren und teilt durch kleines ν. Stattdessen aus D t=νP direkt t_range=ν V diag(d^-1/2) w auf range(D) rekonstruieren. Im radialen Phasenkern zusätzlich t_kernel=−(2ω/ν) Πkernel q. Das ist dasselbe exakte lineare System; kein gelockerter Grenzwert, keine entfernte zusätzliche Mode. Numerische Phasennullrichtung und analytischer Hintergrund stimmen nur bis zu den dokumentierten Residuen überein.

Fortsetzung übernimmt nur vollständige, bestandene Gruppen mit sieben Spektren und sechs Vergleichen. Die 28 vorhandenen Spektren behalten ihre ursprüngliche Provenienz; 35 verbleibende Spektren werden mit der korrigierten Rückrechnung erzeugt. Kein Neulauf der bestandenen Gruppen. Der erste Lauf wird nicht als vollständig bestanden dargestellt.
