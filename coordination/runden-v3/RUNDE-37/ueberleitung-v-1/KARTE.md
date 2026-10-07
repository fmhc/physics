# UEBERLEITUNG-V-1: Welche Traegheit liefert die 4D-Zeit auf Finns gefuelltem Netz V im Grenzfall stetiger Zeit, und sind Schwerewellen damit isotrop und stabil? (Runde 49, Fast Lane nach UEBERLEITUNG-KH-1 und REGIME-K-2)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 14:07:36 CEST (date), vor jeder Rechnung.
- **Herkunft [P]:**
  - Finn, 05.10.2026: "entwickle das weiter wo finden wir eine überleitung".
  - UEBERLEITUNG-KH-1 (Kuhn-Gitter):
    - Die Bloecke fuer Traegheit, Potential, Lapse- und Shift-Kopplung der 4D-Zeltstangen-Wirkung haengen nicht von der Zeltstangenhoehe ab.
    - Das Potential ist das 3D-Regge-B; der Lapse ist reiner Multiplikator mit der Eckenregel unseres Codes; die Lapse-Bedingung ist erster Klasse; R1 ist zulaessige Eichfixierung, RH entartet.
    - Die Traegheit M_eff ist nicht Lund-Regge (r = 0,75 bis 0,77): Die Raumdiagonale hat keine Traegheit, M_eff ist singulaer.
    - Nachtrag nach Sicht: Mit der Raumdiagonale als statischer Groesse laufen zwei Moden isotrop (2,6e-9) und wachsen an 420 k nicht; der BZ-Rand (k_i = pi) ist offen.
  - REGIME-K-2 (gefuelltes V mal Zeit): euklidisch langwellig TT-isotrop ohne Abstimmung (8,0e-9), 40 Nullmoden je k; 26 Gittermoden negativer Steifigkeit; in echter Zeit leicht komplexe TT-Frequenzen (|Im omega|/|k| bis 1,9e-4) und Doppelbrechung bis 2,5e-4.
  - Regime H auf V (TT-ISO-1, HODGE-MASSE-1, LUND-REGGE-MASSE-1): mit A1, A2, Lund-Regge und R1/RH 5,9 bis 10,6 % anisotrop oder wachsend.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung)

- **Vorab ableitbar bzw. nach UEBERLEITUNG-KH-1 erwartet [P, M]:** Auch auf V haengen die Bloecke der Zeltstangen-Wirkung linear nicht von h ab; M_eff ist dann eine feste Matrix auf den raeumlichen Kanten von V, das Potential das 3D-Regge-B von V.
- **Nicht ableitbar:**
  - Struktur von M_eff auf V: welche Kanten bzw. Kombinationen ohne Traegheit sind (statisch)
  - ob Regime H mit M_eff und R1 auf V isotrop ist (wie Regime K euklidisch) oder ob die stetige Grenze etwas verliert
  - ob es dann wachsende Moden gibt, insbesondere am BZ-Rand und in den 26 Gittermoden negativer Steifigkeit aus REGIME-K-2
- **Vorab festgelegt [Zusatz Leitung]:** Statische Richtungen (Kern von M_eff) werden als Zwangsbedingungen behandelt: Ihre Gleichung ist die zugehoerige Zeile des Potentials (Gleichgewicht), die sie aus den uebrigen Groessen festlegt (Schur-Komplement). Keine Pseudo-Inverse ohne diese Ausweisung. Das ist die Regel, die auf Kuhn nach Sicht trug; hier steht sie vorab.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UV0 | Kontrolle [P]: Der Code gibt auf Kuhn die Kennzahlen aus UEBERLEITUNG-KH-1 wieder (M_eff gegen Lund-Regge r = 0,75 bis 0,77; mit statischer Raumdiagonale zwei Moden, TT-Spanne < 1e-8) | 85 % |
| UV1 | [H] Auf V haengen die Bloecke von M_eff, Potential und Lapse-/Shift-Kopplung fuer h = 1 bis 1/64 auf 1e-10 nicht von h ab | 75 % |
| UV2 | [H] Auf V ist M_eff singulaer (mindestens eine statische Richtung je Grundzelle) | 60 % |
| UV3 | [H] Regime H auf V mit M_eff, R1 und der vorab festgelegten Behandlung statischer Richtungen: langwellige TT-Spanne (extrapoliert) unter 1e-6 | 55 % |
| UV4 | [H] Dasselbe: an allen gerechneten k einschliesslich BZ-Rand keine wachsende Mode | 35 % |

**Bedeutung (vorab):**
- **UV3 und UV4 treffen ein:** Finns stetiger Takt funktioniert auf seinem gefuellten Netz, wenn die Traegheit aus der 4D-Zeit kommt (M_eff) und die Eckenregel R1 gilt. Die Grundgleichung bekaeme Traegheit, Lapse und Shift aus einem einzigen 4D-Ansatz; die Richtungsabhaengigkeit des alten Regimes H war eine Folge der gesetzten Traegheit.
- **UV3 trifft ein, UV4 nicht:** Isotrop, aber instabil; die Instabilitaet ist dann eine Eigenschaft der stetigen Grenze bzw. der Gittermoden, nicht der Traegheitswahl. REGIME-K-3 (echte Zeitschritte) entscheidet, ob die diskrete Zeit sie heilt.
- **UV3 verfehlt:** Die stetige Grenze verliert auf V, was die 4D-Wirkung leistet.

## Rahmen

- Code-Agent. Code aus RUNDE-37/ueberleitung-kh-1/code und RUNDE-37/regime-k-2/code kopieren (gefuelltes V mal Zeit), dort nichts aendern. Regime-H-Spektren mit der R1-Reduktion aus RUNDE-37/hodge-masse-1/code bzw. lund-regge-masse-1/code.
- k-Raster wie HODGE-MASSE-1 plus BZ-Rand (Komponenten pi) ausdruecklich.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu2, cpu3 und cpu4. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256); Ausweichpfade (z. B. Pseudo-Inverse) im Plan nur mit Meldung, nie still.
- Synthetisch, keine Messdatenbestaetigung.

## Nachtrag der Leitung (17:06:58, date): Folgeversuch ohne Karte

- Licht und Schwerewellen mit derselben Uhr (DEC und Maxwell auf dem 4D-Zeltnetz, stetige Grenze), gerechnet 16:12:03 bis 16:24:37 ohne Karte (Finn, 05.10. 15:38). Ergebnis in LICHT-GLEICHE-UHR.md; Zusammenfassung RUNDE-50.md (16:25:16). Frage: GR-Pruefliste Nr. 4. Keine Vorhersagen, keine Urteile; Gleichheit bei kl -> 0 folgt aus dem Aufbau. Karte nachgearbeitet auf Finns Wunsch.
