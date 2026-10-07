# G1-02 Teilchen oder Welle an der Stufe: ein Spaltfenster erst ab der Bindungsenergie

- **Hypothese:** Ein 1D-Q-Ball springt an einer abstossenden Potentialstufe nur dann scharf von "ganz zurueck" auf "ganz
  durch" (Teilchenverhalten), solange die Stufenhoehe je Ladung klein gegen seine Bindungsenergie je Ladung ist; ab
  Pi = V2 / (2 omega (1 - omega)) ~ 1 wird der Sprung unvollstaendig und ein Spaltfenster oeffnet sich (ein Teil durch,
  ein Teil zurueck), wie bei hellen NLS-Solitonen, die langsam als Teilchen und schnell als Welle streuen.
- **Papier vorab [S]:** Ein Spalt mit dem Anteil f auf der Plateauseite kostet grob f Q (1 - omega) (kleiner Ball: Masse
  je Ladung ~ 1, grosser Ball: dM/dQ = omega). An der Teilchenschwelle v_cl bringt der Ball nur die Stufenenergie
  ~ V2 Q/(2 omega) mit. Also ist ein Spalt bei v <= 1,02 v_cl nur mit f <= Pi/(1 + Pi) moeglich (Naeherung ohne
  Kruemmung von M(Q)). Unter Pi ~ 0,11 ist schon ein 10:90-Spalt energetisch verboten, dort kann nur das Teilchenbild
  herauskommen.
- **Kleiner Test:**
  - Code-Basis: RUNDE-06/weber/weber.py, Unterbefehl feinv1d (Klassen, Fragmente, Box, dx, dt, Daempfung unveraendert).
    Neu (hoechstens 40 min): Schalter fuer omega^2, V2, Stufenbreite B, Startabstand und die v/v_cl-Liste; v_cl exakt
    aus gamma M1(Q) = M2(Q) wie im Unterbefehl papier.
  - Laeufe: omega^2 = 0,9 (omega = 0,94868, 1 - omega = 0,05132); V2 = 0,01 / 0,05 / 0,10 / 0,20, also
    Pi = 0,103 / 0,514 / 1,027 / 2,054 (Grenze Pi/(1 + Pi) = 0,09 / 0,34 / 0,51 / 0,67); B = 1 wie bisher.
    v_cl etwa 0,105 / 0,23 / 0,32 / 0,44 (grob, das Programm rechnet exakt).
  - Je Stufe v/v_cl = 0,90 / 0,95 / 0,98 / 1,00 / 1,02 / 1,05 / 1,10 / 1,20 / 1,35 / 1,50, dazu die Gegenproben unten:
    zusammen 60 Laeufe, T = 45/v + 200 (bei B = 25: Start 80 vor der Stufe, T = 100/v + 200).
  - Rechenort .69, Spur p4000a (Ausweich cpu); geschaetzt 2 bis 4 min grob, dazu derselbe Satz mit --fein.
  - Messgroessen je Lauf: q_durch, q_zurueck, q_frei, Fragmentzahl, Energiedrift. Daraus je Stufe die Sprunghoehe
    dT = q_durch(1,02 v_cl) - q_durch(0,98 v_cl) und das Spaltfenster W = Rasterpunkte mit 0,1 < q_durch < 0,9.
- **Vorhersage vorab:**
  - V1 (Pi = 0,10): dT >= 0,9; kein Rasterpunkt mit 0,1 < q_durch < 0,9; Wechsel zwischen 0,98 und 1,02 v_cl.
  - V2 (Pi = 2,05, B = 1): dT <= 0,8, und mindestens zwei Rasterpunkte mit 0,1 < q_durch < 0,9 ("gespalten": zwei
    Fragmente, eines je Seite, q_frei <= 0,15). In diesem Fenster steigt q_durch mit v (Abweichung hoechstens 0,05).
  - V3: dT faellt mit Pi ueber die vier Stufen monoton (Toleranz 0,05).
  - V4 (Energieschranke [S]): bei v <= 1,02 v_cl ist in keinem gespaltenen Lauf q_durch > Pi/(1 + Pi) + 0,05.
  - **Scheitert, wenn** bei Pi = 2,05 und B = 1 der Sprung voll bleibt (dT >= 0,9 und kein Spaltpunkt), oder bei
    Pi = 0,10 ein Spalt auftritt, oder V3 an zwei oder mehr Stellen verletzt ist. Die Klassen ausserhalb dieser Regeln
    sind "nicht entscheidbar", nicht "getroffen".
- **Gegenprobe (Effekt muss verschwinden):**
  - V2 = 0,20 mit breiter Stufe B = 25 (Rampe viel breiter als der Ball; Durchlaufzeit B/v_cl ~ 57 gegen die innere
    Zeit 1/(1 - omega) ~ 19, also langsam): wieder dT >= 0,9 und kein Spaltpunkt.
  - V2 = 0 bei allen zehn v: alle "durch", q_haupt >= 0,99.
- **Plausibilitaetsschranke:** 0 <= q_durch, q_zurueck, q_frei; Summe 1 +- 0,01; |E-Drift| < 1e-3 bis zur Auswertung;
  alle Fragmentgeschwindigkeiten |v| < 1; V4 (Energie).
- **Latten erwartet:** L1 ja (drei Ausgaenge moeglich: voll, teilweise, auch bei B = 25 gespalten); L2 Gegenproben
  B = 25 und V2 = 0; L3 --fein (halbes dx und dt), gleiche Klassen, |dq| <= 0,05; L4 teilweise (Teilchen-Welle-Uebergang
  heller NLS-Solitonen an Barrieren ist Literatur, fuer Q-Baelle an einer Stufe und die Lage in Pi nicht gefunden);
  L5 nein (Laboranalogon: Kondensat-Solitonen an Barrieren, ohne Zahl, die wir hier nachrechnen).
- **Ergaenzung T-1 vor dem Stempel (nur Messregeln, keine neue Idee):**
  - Gegenprobe V2 = 0: dieselben zehn v wie bei V2 = 0,20.
  - Jeder Lauf wird bei seinem eigenen T ausgewertet (Zustand dort gesichert); Energie-Drift bis zu diesem T.
  - B = 25: Ein Ball bei 0,98 v_cl kehrt erst bei x ~ 40 um und braucht fuer Hin- und Rueckweg ueber 1100 Zeiteinheiten
    (eigene Abschaetzung, Teilchenbild auf der Rampe). Mit T = 100/v + 200 und der Zone |x| <= 8 stuende er bei der
    Auswertung noch auf der Rampe und zaehlte als "durch" oder "haengt". Daher bei B = 25: Zone |x| <= 2B = 50,
    T = 180/v + 1000, Box +-1200 mit Schwamm ab 1160, Start 80 vor der Stufe. B = 1 bleibt wie feinv1d (Zone 8, Box 200).
  - Toleranz der Pruefungen ">= 0" und "Summe 1": 1e-4 bzw. 0,01 wie oben.
- **Einfach gesagt:** Ein Q-Ball, der gegen eine Stufe rollt, verhaelt sich bisher wie eine Murmel: zu langsam, und er
  rollt ganz zurueck; schnell genug, und er kommt ganz hinueber. Die Rechnung auf Papier zeigt aber, dass er bisher gar
  nicht genug Energie hatte, um sich zu teilen. Wir machen die Stufe jetzt hoeher als seine Bindungsenergie. Wenn er dann
  wie eine Welle in einen durchgelassenen und einen zurueckgeworfenen Teil zerfaellt, und bei einer sanften Rampe nicht,
  wissen wir, wo die Grenze zwischen Teilchen und Welle liegt.
- Karte geschrieben: 2026-09-30 07:37:34 CEST
- Vorhersage geschrieben: 2026-09-30 07:52:18 CEST
