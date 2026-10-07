### Grenzen

- Alles ist modellintern. Die Aussagen gelten nur fuer das diskrete M3-Funktional der Karte auf diesen Graphen
  (Kantengewicht 1, offener Rand).
- "Minimum" heisst lokales Minimum aus L-BFGS-B. Es gab keine Zeitentwicklung und keine Stabilitaetsanalyse.
- Gitter: Die Fortsetzungsaeste sind glatt. Groessenkontrollen und Startformen werden in Abschnitt 3 berichtet.
  - Die chi-Wand ist nur etwa 1,4 Gitterabstaende dick.
  - In der Kette springt die Beutellaenge in ganzen Knoten. p_loc zeigt deshalb ein Saegezahnmuster (0,4995 bis
    0,5038); die Sekante mittelt es weg.
- Sierpinski:
  - Der Fortsetzungsast ist metastabil. Er waechst nur in Spruengen: V_bag 139 -> 179 -> 301 -> 449 -> 521 -> 601
    -> 1007, mit Energieabfall beim Sprung (k = 67: E faellt von 2069 auf 1474 bei steigendem Q).
  - Frische Starts liegen bei k = 46, 58 und 64 um 22 bis 33 % tiefer, bei k = 50 aber 1,4 % hoeher als der Ast. Die
    Energielandschaft hat viele Nebentaeler.
  - Auch Z3 ist kein bewiesenes globales Minimum, sondern eine selbstaehnliche Familie lokaler Minima. Ihr
    Energieverhaeltnis ~3 je Periode folgt aus der Selbstaehnlichkeit (Laenge x 2, Volumen x 3, lambda / 5) [H].
  - Damit misst Z3 genau die Kombination ln3/ln(3 sqrt5) = d_s/(d_s + 1). Unabhaengig davon ist, dass die
    Minimierung die Familie tatsaechlich trifft.
- Die Kette ist bei k = 57 (Q = 8,4e3) durch das Konvergenzkriterium begrenzt, nicht durch die Graphgroesse.
  maxcor 20 reicht dort nur knapp.
- Plateaulaengen (D5) haengen an den gewaehlten Graphgroessen bzw. an der Konvergenz. "In 3D am kuerzesten" gilt nur
  fuer diese Wahl (64^3 gegen 256^2 und 4096).

### Selbstanzeigen

1. Planfehler: Die Randdefinition fuer Gitter (L1-Abstand) war falsch. Ich habe sie in Nachtrag 1 vor jedem Lauf
   berichtigt.
2. Neben py_compile habe ich auf der .69 einmal `python -c "import scipy, numpy, matplotlib"` ausserhalb von
   kleintest.sh aufgerufen (Versionsabfrage, unter 1 s, keine Rechnung).
3. Beim ersten Rauchtest-Aufruf war ein Logpfad falsch (cwd). Fuer die Spur cpu2 lief dadurch nichts; ich habe den
   Aufruf wiederholt.
4. Loeser waehrend der Laeufe umgestellt (Nachtrag 3):
   - maxcor 20 -> 5, weil die Zeit nicht reichte.
   - G3 hat k <= 69 mit maxcor 20 und k >= 70 mit maxcor 5; G4-Ast entsprechend k <= 64 und k >= 65.
   - Funktional und Kriterien blieben gleich.
5. Kette:
   - Der maxcor-5-Versuch erfuellte das Kriterium ab k = 54 nicht. Ich habe ihn per kill (PID) abgebrochen; er wird
     nicht gewertet.
   - Neu gerechnet mit maxcor 20 (ket4096m20-auf). Diesen Lauf habe ich nach k = 59 ebenfalls per PID beendet, weil
     k = 57 schon ungueltig war.
6. Laufreihen umgeplant:
   - Viermal habe ich lokale Laufreihen-Skripte (bash) per kill -9 beendet, ohne laufende Rechnungen zu
     unterbrechen.
   - Einen auf der .69 noch wartenden Aufruf (flock, ohne Rechnung) habe ich per PID beendet.
   - Kein pkill -f.
7. Weggefallen: die G4-Fortsetzungsaeste g = 9 und s2 (ersetzt durch Z4), der G4-Abwaertsast unter k = 40 und Z2
   (Quadrat von oben).
   - Die Startform-Kontrolle von G4 hat deshalb nur bei k = 50 einen Ast zum Vergleich.
   - Frisch A und B bei k = 80 erreichten die Zeitgrenze bzw. die Konvergenz nicht.
8. auswertung.py habe ich nach der Probe-Auswertung erweitert (Z3/Z4, Kette m20). Gewertet wird die Schlussfassung;
   sha256 unten.
9. arXiv-API: Abfrage 1 ok (10:05:53). Abfrage 2 brach mit HTTP 000 ab (Verbindung). Bei der Wiederholung kam
   HTTP 429 (10:12:49), danach habe ich laut Regel abgebrochen.
10. Die Probe-Auswertungen liefen auf Teildaten und nur ueber kleintest.sh. Sie sind nicht gewertet.
