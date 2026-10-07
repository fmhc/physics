# PLAN (LOG-NACHBAU, Runde 16)

- Verfasst: 2026-10-02 ab 08:07:26 CEST (date). Code-Agent, frischer Kontext. Zeitbox 90 min ab 07:46:33 CEST.
- Code: stille.py (eigener Code). Herleitung: HERLEITUNG.md.

## 1 Herleitung

- Siehe HERLEITUNG.md.
- W = G_a + i G_b, G_x = Wronski[Y_x, Z_d] = -2 kappa gamma_x.
- Geschlossene Bedingung G_b = 0, s = G_a an deren Nullstellen.
- Stille Stelle <=> W = 0 (Lagrange-Argument).

## 2 Numerik

- Profil:
  - Mehrfachbisektion (24 Kandidaten, 8 Runden, Schritt 0,02) fuer den Startwert f0.
  - Danach zweiseitiges Schiessen mit Newton in (f0, A) auf dem Stufengitter. Anschluss bei r_p = 2,5/mu.
  - Innen-Start bei R = r_p + 16/mu mit Yukawa-Schwanz, Abbruch bei relativem Newtonschritt < 1e-14.
- Kanaele: RK4 mit festem Schritt h fuer u, v (Form u = r a), von r = 0 bis R. Profilwerte auf dem Gitter h/2 (Profilgitter).
- Gitterstufen: Stufe 1 mit hp = 0,01 (h = 0,02), Stufe 2 mit hp = 0,005 (h = 0,01).
- Aussenrand R = r_p + 16/mu je Block (Maximum ueber den Block). Im Fenster: w^2 = 0,98 gibt R ~ 131, w^2 = 0,70 gibt R ~ 34.
- Auswertung G_x = -e^{-kappa R} (kappa v_x(R) + v_x'(R)).
- Mitlaufende Pruefungen:
  - Isotropie W[Y_a, Y_b] relativ (soll ~0)
  - Anschlusssprung des Profils
  - Knotenzahl 0

## 3 Kontrollen

- K1 (Kontrollmodell U = S - S^2 + S^3/2):
  - Zeilen w^2 = 0,780 bis 0,815, Abstand 0,005 (8 Zeilen).
  - Je Zeile 401 rho-Punkte von 1 - w + 0,002 bis 1 + w - 0,002.
  - Danach dasselbe Verfahren wie bei der blinden Suche (Abschnitt 4), auf beiden Stufen getrennt.
- K2 (Log): Profile auf beiden Stufen fuer w^2 = 0,70; 0,74; 0,78; 0,82; 0,86; 0,90; 0,94; 0,98. Vergleich der relativen
  Abweichung von Q und E. Dazu informativ alle 57 Zeilen der blinden Suche.

## 4 Blinde Suche (Log, U = ln(1 + S))

- Zeilen w^2 = 0,700 + 0,005 j, j = 0..56 (57 Zeilen, Abstand 0,005), beide Stufen getrennt.
- Je Zeile:
  - G_a und G_b auf 401 rho-Punkten von 1 - w + 0,002 bis 1 + w - 0,002.
  - Jede Vorzeichenwechsel-Klammer von G_b wird mit Illinois-Regula-falsi verfeinert (hoechstens 14 Schritte,
    Klammer < 1e-10).
  - s = G_a an jeder Nullstelle.
- Detektor 1:
  - Nullstellen benachbarter Zeilen werden gepaart (wechselseitig naechste, Abstand <= 0,03).
  - Wechselt s das Vorzeichen, entsteht ein Kandidat (lineare Interpolation zwischen den Zeilen).
- Detektor 2 (Zusatz gegen Faltungen):
  - Umlauf der Phase von W um jede Gitterzelle aus den vier Eckwerten.
  - Zellen mit Umlauf ungleich 0 werden Kandidaten.
- Lokalisierung:
  - Kandidaten im Abstand < 2e-3 werden zusammengelegt.
  - 2D-Newton auf (G_a, G_b) = 0 mit Differenzenquotienten (1e-6), Schritt hoechstens 0,01, Abbruch bei Schritt
    < 1e-10, hoechstens 10 Iterationen.
- Rechteck:
  - Halbbreiten 1e-3 in w^2 und rho um den lokalisierten Punkt, 16 Punkte je Kante.
  - Abschnitte mit Phasensprung >= 0,4 rad werden halbiert, hoechstens 6 Runden.
  - Umlauf = Summe der gewickelten Zuwaechse / 2 pi.

## 5 Laufliste (Spur, gemessene Dauer kommt in ERGEBNIS.md)

- L0 Rauchtest lokal (System-python3, timeout 120, nice 19, 1 Thread):
  - grobes Gitter hp = 0,04, Kontrollmodell, Profil und G an drei Punkten
  - 08:07:08 bis 08:07:09, rc 0
  - Funktionsprobe, keine Kontrolle.
- K1-Vorversuch: keiner geplant.
- Nach dem Einfrieren:
  - L1/L2: K1-Zeilen Stufe 1 (cpu3) und Stufe 2 (cpu4).
  - L3/L4: K1-Kandidaten Stufe 1 (cpu3) und Stufe 2 (cpu4).
  - L5: K2 (cpu3).
  - L6 ff.: blinde Zeilen, beide Stufen. Die Bloecke werden nach der in L1/L2 gemessenen Laufzeit so geschnitten, dass
    jeder Aufruf unter 8 min bleibt. Die Schnitte aendern nichts am Ergebnis.
  - Danach je Stufe ein Kandidatenlauf.
- Jede Zeile wird nach ihrem Block sofort als JSON gespeichert (Block = hoechstens 10 Zeilen).

## 6 Auswertung (wortgleich zur Karte)

- K1: "Mit dem Kontrollmodell findet der eigene Code die bewiesene Stelle bei omega^2 = 0,797677, rho = 1,744618 auf 1e-4,
  Umlauf +-1 auf zwei Gitterstufen."
- K2: "Profile des Log-Balls auf zwei Gittern, Ladung Q und Energie E auf 1e-6 relativ gleich."
- "Verfehlt K1 oder K2: nicht auswertbar."
- Blinde Suche:
  - "Testmodell, omega^2 von 0,70 bis 0,98, Zeilenabstand hoechstens 0,005. Je Zeile alle Nullstellen der geschlossenen
    Bedingung im Fenster und s, zwei Gitterstufen."
  - "Jeder Vorzeichenwechsel von s zwischen benachbarten Zeilen wird mit einem kleinen Rechteck lokalisiert."
  - "Gefunden: jede Stelle mit aufgeloestem Umlauf +-1 auf beiden Stufen; Lagen der Stufen auf 1e-4 gleich."
  - "Aufgeloest heisst: groesster Phasensprung zwischen benachbarten Randpunkten < 0,4 rad."
- Zusatz des Agenten (kein Kriterium):
  - Kandidaten aus Detektor 2 ohne s-Wechsel werden mit derselben Regel geprueft und getrennt berichtet.
  - "Auf 1e-4" heisst: Abstand in w^2 und in rho je <= 1e-4.

## 7 Folgelaeufe

- Nur mit eingefrorenem Nachtrag (PLAN-NACHTRAG-*.md), als nachtraeglich gekennzeichnet.
