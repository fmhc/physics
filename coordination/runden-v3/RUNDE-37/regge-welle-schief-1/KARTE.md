# REGGE-WELLE-SCHIEF-1: Laufen Schwerewellen im schiefen 4D-Netz noch sauber, oder spalten, wachsen oder rasen sie? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 05:07:31 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - REGGE-WELLE-1: Im regelmaessigen 4D-Kuhn-Netz laufen lange Schwerewellen mit c, kurze langsamer, nie schneller.
    - Zwei Polarisationen, exakt gleich schnell (keine Doppelbrechung).
    - Die Ausbreitung folgt exakt der einfachsten Wuerfelgitter-Formel.
  - REGGE-4D-SCHIEF-1: Im schiefen Netz (nur Raumachsen verzerrt, s = 0,1 und 0,2) bleibt Einsteins Form fuer lange
    Wellen.
    - Die Hyperdiagonale wird aber eine Gittermode mit negativer Steifigkeit (9 positive und 2 negative Eigenwerte
      statt 9 und 1).
    - Bei s = 0,2 kreuzt eine kurzwellige Mode die Null.
  - Frage fuer Finns Netzbild ("Lichtgeschwindigkeit im Netz"): Ist das saubere Wellenbild eine Eigenschaft des
    Kristallnetzes, oder haelt es auch im ungeordneteren Netz?
- Kennzeichen: [M] Mathematik, [L] Literatur, [H] Hypothese.

## Test (Code-Agent)

- Code aus RUNDE-37/regge-welle-1/code/ (Wellenmessung ueber komplexes k_tau: Polynom-Eigenwerte, Windungszahl, reelle
  Achse) mit dem schiefen Netz aus RUNDE-37/regge-4d-schief-1/code/ verbinden:
  - dieselbe Matrix A, dieselbe Saat, s = 0; 0,1; 0,2
  - die Zeitachse bleibt senkrecht
- Wellenvektoren in physikalischen Koordinaten.
  - Richtungen wie REGGE-WELLE-1 (mindestens 24), Betraege |k| = 0,05; 0,1; 0,2; 0,4; 0,8.
  - Fuer jede Richtung die Gitter-k aus den physikalischen k umrechnen.
- **Je Punkt:**
  - Zahl der laufenden Moden (Windungszahl)
  - ihre Geschwindigkeiten v = omega/|k|
  - Aufspaltung der Moden
  - groesster Betrag von Im omega unter den Wurzeln nahe der reellen Achse
  - Polarisationsanteile (TT, Lapse/Shift, Diagonalmode)

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| WS0 | Kontrolle: s = 0 reproduziert REGGE-WELLE-1 (v an allen gemeinsamen Punkten auf <= 1e-9) | 85 % |
| WS1 | Lange Wellen, s = 0,1 und 0,2: an allen Richtungen bei |k| = 0,05 genau zwei laufende Moden mit abs(v - 1) <= 1e-3 | 75 % |
| WS2 | [H] Doppelbrechung: bei s = 0,2 und |k| = 0,8 unterscheiden sich die zwei Moden in mindestens einer Richtung um mehr als 1e-4 in v | 65 % |
| WS3 | [H] Keine Zusatzmode: Die Zahl der laufenden Moden bleibt bei s = 0,1 und 0,2 an allen Punkten 2 | 50 % |
| WS4 | [H] Kein Anwachsen: Bei s = 0,1 und 0,2 hat an keinem Punkt eine Wurzel nahe der reellen Achse abs(Im omega) > 1e-6 | 45 % |
| WS5 | [H] Schneller als Licht: Bei s = 0,2 gibt es eine Richtung und ein |k| >= 0,4 mit v > 1 + 1e-6 | 30 % |

**Bedeutung (vorab):**
- **WS1 trifft ein, WS2 bis WS5 zeigen Abweichungen:** Lange Wellen bleiben im ungeordneten Netz einsteinsch. Bei
  kurzen Wellen verraet das Netz seine Unordnung:
  - durch Doppelbrechung, Zusatzmoden oder Anwachsen
  - "Schneller als Licht" wuerde heissen: Die Grenzgeschwindigkeit des Netzes ist richtungsabhaengig
  - Fuer Finns Schaumbild: vor "ungeordnet ist besser" erst klaeren, ob die negative Mode eine wachsende Welle wird.
- **WS3 und WS4 verfehlt:** Die Diagonalmode mit negativer Steifigkeit wird in echter Zeit zu einer zusaetzlichen
  laufenden bzw. wachsenden Welle. Das schiefe Netz waere dynamisch krank, nicht nur in der euklidischen Rechnung.
- **WS3 und WS4 treffen ein:** Die negative Mode bleibt eine reine Eichs- oder Zwangsmode ohne eigene Ausbreitung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und p4000b; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 100 min.
