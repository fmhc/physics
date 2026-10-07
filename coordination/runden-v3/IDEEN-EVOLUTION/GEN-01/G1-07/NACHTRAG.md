# G1-07 Nachtrag (nach dem Stempel 07:52:18, vor jedem echten Lauf)

- 2026-09-30 08:03:49 CEST, T-1:
  - Geparkt: 3D-Vergleich der Gegenprobe. RUNDE-07/r5f/r5f.py tod hat feste Laeufe (gamma 1e-3 mit Stopp bei
    Vielfachen von Q_min, dazu ein Dauerabfluss 1e-3). Fuer p in 3D braucht es drei gamma ohne Stopp und dasselbe
    Bruchkriterium mit der 3D-Familie S_c(Q) aus r5a.familie; das ist neuer Code (geschaetzt 30 bis 45 min) und passte
    nicht in die Zeitbox. Der Code hier liefert nur den 1D-Teil; urteil meldet "3D-Gegenprobe offen".
  - Vor jedem Lauf festgelegte Toleranzen, die die Karte offen laesst: Q_tot <= Q_erw mit 1e-4 relativ
    (Diskretisierung); omega > 0 nur wo |psi(0)|^2 > 1e-12 (sonst ist die Phase nicht bestimmt); omega aus der
    Phase im Zentrum ueber +-5 Zeiteinheiten; S_c = |psi(0)|^2.
  - Papiertest kann scheitern (p, Q_d-Band, Verhaeltnis, Stopp); kein "L1 schwach".
