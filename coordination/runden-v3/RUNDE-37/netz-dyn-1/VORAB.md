# NETZ-DYN-1: Vorab-Datei des Bau- und Rechenagenten (vor jeder Rechnung)

- Geschrieben ab 2026-10-06 20:31:10 CEST (date), vor dem ersten Lauf auf der .69. Claude-Subagent (Opus 5.5) fuer die
  Leitung claude-primary. Die Karte (D1 bis D7) bleibt unveraendert; hier steht nur meine eigene Erwartung.

## Plan (wie gebaut wird)

- Ein dimensionsfreier Kern fuer d = 2 und d = 4: Simplizes als Eckenmengen, Zeitschicht je Ecke.
  - Zeitartige Zuege = Pachner-Zuege 2-4, 3-3, 4-2 (in d = 2 der 2-2-Zug), angenommen nur, wenn alle neuen Simplizes
    genau zwei benachbarte Schichten beruehren und keine raumartige Teilflaeche entsteht oder verschwindet.
  - Raumartige Zuege = Pachner-Zuege in der Schicht (3D: 1-4, 2-3, 3-2, 4-1; 1D: Kante teilen bzw. Ecke entfernen),
    hochgehoben auf die Kegel darueber und darunter. In 4D sind das die Zuege (2,8), (4,6), (6,4), (8,2), in 2D (2,4)
    und (4,2).
  - Zugliste nach Ambjoern, Jurkiewicz, Loll [L, aus dem Gedaechtnis]: (2,8), (4,6), (2,4), (3,3) und Umkehrungen.
    Ergodizitaet ist eine Annahme; Pruefung im Kleinen: Startunabhaengigkeit der Mittelwerte, jede Zugart angenommen,
    Mannigfaltigkeitspruefung (jedes Tetraeder in genau zwei Simplizes, Euler-Zahlen der Schichten).
  - Wirkung 4D: S = -(k0 + 6 Delta) N0 + k4 (N41 + N32) + Delta (2 N41 + N32) + eps (N4 - Nziel)^2 (AJL-Zaehlform),
    2D: S = lambda N2 + eps (N2 - Nziel)^2. Metropolis mit Auswahlfaktor N4/N4'.
- Felder auf dem jeweiligen Komplex mit Rueckwirkung: U(1) auf Kanten (Wilson ueber Dreiecke, Gewichte w = 1),
  SU(2) auf Kanten, SU(2)-Rahmen an den Ecken (O(4)-artige Nachbarkopplung). Neue Kanten bzw. Ecken bekommen ihren Wert
  aus dem bedingten Waermebad; dessen Dichte geht in die Annahme ein (Rosenbluth-Gewicht), damit die Feldwirkung exakt
  in die Geometriezuege zurueckwirkt.
- Start 3+1D: Finns Netz V (ew.geometrie('V'), unveraendert kopiert), periodischer Kasten 2x2x2 Zellen, Zeitschichten
  per Treppenzerlegung des Prismas Tetraeder x Intervall (je Tetraeder ein (4,1), (3,2), (2,3), (1,4)).

## Eigene Erwartungen (vorab, mit Wahrscheinlichkeit)

| Nr | Erwartung | Wahrsch. |
|---|---|---|
| V1 | Der Kern laeuft in 1+1D fehlerfrei (Mannigfaltigkeitspruefung nach jedem Abschnitt bestanden) und gibt d_H im Fenster 1,8 bis 2,2 (D1) | 70 % |
| V2 | Der 4D-Kern laeuft fehlerfrei und alle sieben Zugarten werden angenommen | 60 % |
| V3 | In den etwa 150 min erreiche ich in 3+1D nur N4 von einigen Tausend bis etwa 2e4 und zu wenige Sweeps; D2 bleibt dann "nicht entschieden" (kein sauberes d_s-Plateau). Wahrscheinlichkeit, dass ich D2 in der Zeit entscheide (Treffer oder Fehlschlag mit Plateau) | 25 % |
| V4 | Bei k0 klein (etwa 1) und Delta = 0 entsteht eine zerknuellte Phase mit Ecken sehr hoher Ordnung (Superpunkte), bei k0 = 2,2 und Delta = 0,6 nicht | 60 % |
| V5 | Wo Superpunkte auftreten, ist die U(1)-Ladung durch ihre raeumliche Hülle im Mittel 0 (D7) | 75 % |
| V6 | Die Felder bei beta = 2 (U(1)) aendern die Phasenlage bei den kleinen Volumina nur wenig (D4); messbar ist das in der Zeit nur grob | 50 % |

## Was als Ergebnis gilt

- Erreichte Stufe (S0, S1, S2) mit bestandenen Kontrollen; Zahlen nur mit Volumen, Sweeps und Fehlerbalken.
- Wenn die 4D-Zuege nicht sauber laufen oder die Volumina zu klein sind: das ist das Ergebnis, mit Beschreibung der
  Fortsetzung. Keine Abkuerzung, die D2 vortaeuscht.

## Nachtrag vor den Ergebnissen der zweiten Welle (2026-10-06 21:23:40 CEST, date)

- Geschrieben, bevor ich Ergebnisse dieser Laeufe gesehen habe (Laeufe teils schon gestartet). Bekannt war: S0 erste
  Abschnitte, S1 bei (2.2, 0.6), (2.2, 0.0), (5.0, 0.6) erster Abschnitt, DT-Abtastung, F1 (U(1) + Rahmen), Startkontrollen.

| Lauf | eigene Erwartung | Wahrsch. |
|---|---|---|
| s0a2/s0b2 (1+1D, volle Schalen) | Groessenskalierung des mittleren Abstands gibt d_H 1,8 bis 2,2; lokale Steigung bleibt um 2,3 | 70 % |
| L = 3 (N4 ~ 25000) bei (2.2, 0.6) | d_s-Maximum wandert zu groesserem sigma, Hoehe 3,8 bis 4,4, weiter kein Plateau | 60 % |
| F2 (nur Rahmen J = 1) gegen S1-A | d_s-Kurve aendert sich um weniger als 0,3 (D5-Richtung) | 65 % |
| F3 (nur SU(2) beta = 2,5) | wie F1: Eckenzahl sinkt bei gleichem k0, Feldgewicht (2,8) stark negativ | 70 % |
| F1b (U(1) + Rahmen bei k0 = 10,2) | N0/N4 bleibt naeher an 0,04 als bei k0 = 2,2 mit Feldern (Verschiebung grob richtig) | 55 % |
| F4 ((2.2, 0.0) mit U(1) + Rahmen, ohne k0-Nachfuehrung) | keine Superpunkte; Ladung 0 an gewoehnlichen Ecken | 70 % |
| s1x-unten (Endzustand F1 ohne Felder bei (2.2, 0.6)) | N0/N4 steigt in einem Abschnitt Richtung 0,035 bis 0,04 (Startunabhaengigkeit) | 60 % |
