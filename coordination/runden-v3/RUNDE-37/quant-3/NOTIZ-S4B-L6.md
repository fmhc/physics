# S4 auf L = 6: Laeufe der Leitung (06.10.2026, nach Erschoepfung des agy-Kontingents)

- beta_c(L = 6, Nt = 4) aus m5-n6t4: |L| bei 3,25 0,019 bzw. 0,029, bei 3,30 0,083 bzw. 0,048 (heiss/kalt), bei 3,325
  0,104 bzw. 0,090. Der Anstieg liegt zwischen 3,25 und 3,30. Die Leitung hat beta = 3,30 gewaehlt (Schaetzung aus dem
  Anstieg; die Suszeptibilitaet ist noch nicht ausgewertet).
- Gestartet ueber kleintest.sh: s4b-n6t8 (p4000a), s4b-n6t10 (p4000b), s4b-n6t12 (p4000a, wartet auf den Lock).
  Netz L = 6, beta 3,30, su2b.py mit --korr --mh, 800 Messungen, Zeitlimit 540 s.
- Auswertung offen: streng nach VORAB-S4B.md (nur 111-Achse, Fenster ab d = 1, Jackknife). Den Unterschied zwischen
  3,30 und dem genauen beta_c aus der Suszeptibilitaet als Fehlerquelle nennen.
