# INDUZIERT-DICHTE-2D: Bringt "Zahl = Volumen" die richtige Schwerkraft aus der Materie zurueck? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 07:06:53 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - INDUZIERT-1: Festes Kristallnetz gibt riesige, richtungsabhaengige Gitterterme statt Einsteins bzw. Polyakovs
    Struktur.
  - INDUZIERT-ZUFALL-2D: Ein festes Zufallsnetz ist richtungsfrei, aber c_P = +0,159 statt -1/(24 pi) = -0,0133.
    Knotenverschiebungen sind hunderte- bis tausendmal zu steif.
- **Schreibtisch der Leitung [H]:**
  - Auf festem Netz aendert eine konforme Aenderung der Kantenlaengen die Zahl der Moden je physikalischer Flaeche. Die
    Abschneidelaenge wandert mit, und das erzeugt den grossen lokalen Term.
  - Kausalmengen-Prinzip "Zahl = Volumen": Punkte mit fester Dichte in der *physikalischen* Flaeche streuen und neu
    vernetzen. Dann ist die Abschneidelaenge ueberall gleich.
  - Uebrig bleiben sollte nur die universelle Antwort, Polyakovs Anomalie, plus ein Flaechenglied (kosmologische
    Konstante), das man abzieht.
  - Das waere die 2D-Fassung von Ueberleitung 3 fuer Schwerkraft aus Materie.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Geometrie:** 2D-Torus mit konformer Metrik g = e^(2 sigma) delta, sigma = s cos(k.x), mehrere k und
  Richtungen.
- **Streuung:** Poisson-Punkte mit Dichte rho in der physikalischen Flaeche, also Intensitaet rho e^(2 sigma(x)) in
  Koordinaten. N = 16 000 und 64 000.
- **Netz:** Delaunay in Koordinaten (fuer langsam veraenderliches sigma winkeltreu genug; Abweichung offenlegen).
  - Kantenlaengen physikalisch: l_ij = Integral von e^sigma laengs der Kante, oder in guter Naeherung e^((sigma_i +
    sigma_j)/2) abs(x_i - x_j).
  - Materie: P1-Skalar (Kotangens-Laplace aus den physikalischen Laengen), Konvention fuer log det' wie in
    INDUZIERT-ZUFALL-2D.
- **Rauschen:** gemeinsame Zufallszahlen fuer s = +-s0 und 0.
  - Z. B. dieselben Grundpunkte z_i mit einer flaechentreuen Abbildung psi (Moser-Konstruktion o. ae.) in die
    gewichtete Dichte bringen.
  - Lege offen, wie viele Delaunay-Kanten dabei kippen.
  - Viele Saaten. Wenn das Rauschen zu gross ist, als "nicht auswertbar" mit Abschaetzung des noetigen Aufwands melden.
- **Messgroesse:** Steifigkeit der konformen Mode pro physikalischer Flaeche und k^2, nach Abzug des Flaechenglieds.
  Bezug Polyakov -1/(24 pi).
- **Kontrolle:** Feste Grundpunkte ohne Neuvernetzung (nur die Kantenlaengen aendern sich) muessen INDUZIERT-ZUFALL-2D
  wiedergeben (+0,159).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ID0 | Kontrolle: Variante "feste Punkte" gibt c_P = +0,159 auf 2 % wieder | 85 % |
| ID1 | [H] Mit Streuung nach physikalischer Flaeche liegt die konforme Steifigkeit (Saatmittel, kleinstes k, N = 64 000) innerhalb 30 % von -1/(24 pi) | 35 % |
| ID2 | Das Ergebnis mit Streuung nach Flaeche unterscheidet sich von +0,159 um mehr als 3 Standardfehler | 70 % |
| ID3 | [H] Das Vorzeichen der konformen Steifigkeit ist negativ (wie Polyakov) | 50 % |

**Bedeutung (vorab):**
- **ID1 und ID3 treffen ein:** "Zahl = Volumen" stellt die geometrische Antwort her. Der grosse Gitterterm war ein
  Artefakt des festen Netzes.
  - Schwerkraft aus Materie wird dann auf einem Netz moeglich, dessen Punkte nach Volumen gestreut sind.
  - Das stuetzt die Kausalmengen-Seite von Finns Weiche, als 2D-euklidisches Modell.
- **ID2 trifft ein, ID1 verfehlt:** Neu vernetzen aendert etwas, reicht aber nicht.
- **ID2 verfehlt:** Auch "Zahl = Volumen" laesst den Gitterterm stehen. Dann braucht Ueberleitung 1 echte Summen ueber
  Netze (Dynamik) oder Feinabstimmung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3 und cpu4; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
