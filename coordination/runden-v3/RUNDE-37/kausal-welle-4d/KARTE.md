# KAUSAL-WELLE-4D: Laeuft eine Welle auch auf einem Raumzeit-Netz in 3+1 Dimensionen wie im glatten Raum? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 07:09:37 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - KAUSAL-WELLE-1 und SCHACHBRETT-KAUSAL-1: In 1+1 laufen Wellen und Fermionen auf der Kausalmenge im Mittel wie im
    Kontinuum. Sie sind stabil, das Rauschen faellt wie rho^(-1/2).
  - Das ist eine Spielzeugwelt. Fuer Finns Weiche zaehlt 3+1.
  - In 3+1 gibt es keine 2D-Ordnung (kein Fenwick-Trick); Kausalrelationen kosten O(N^2), Links O(N^3) bzw. eine
    Matrixmultiplikation.
- **Literatur [L?]:** Johnston (arXiv 0806.3083) gibt fuer 4D einen retardierten Propagator aus Links: masselos K_0 =
  a L mit a = sqrt(rho)/(2 pi sqrt 6), massiv per Spruengen und Halten mit b = -m^2/rho. Faktoren an der Quelle
  pruefen (in KAUSAL-WELLE-1 fuer 2D schon gelesen).
- Kennzeichen: [M] Mathematik, [L] Literatur, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Netz:** Poisson-Streuung in einem 4D-Kausaldiamanten (oder einem Zylinder mit festem Zeitfenster), N bis ca. 10^4
  bis 2 x 10^4 Punkte, je nach Laufzeit. Mehrere Dichten und Saaten.
- **Kausalmatrix C** blockweise; Links L = C und nicht (C C > 0), per Gleitkomma-Matrixprodukt in Bloecken. Laufzeit
  vorab messen.
- **Propagator:** Johnstons 4D-Form, Faktoren an der Quelle geprueft.
  - Wellenpaket aus glatter Quelle J (Gauss-Huelle mal ebene Welle), m = 1.
  - phi = K J / rho; Saatmittel gegen Kontinuumsloesung (Faltung mit dem retardierten massiven 4D-Propagator, glatt
    gemacht durch die Quelle) an Pruefpunkten im Inneren.
- **Messgroessen:** Saatmittel gegen Kontinuum, relative Streuung gegen rho, Norm gegen t; beschreibend die Linkzahl je
  Element gegen N.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KV0 | Kontrolle: Die mittlere Linkzahl je Element trifft den exakten Erwartungswert (numerisches Integral fuer das Gebiet) innerhalb 3 Standardfehlern | 80 % |
| KV1 | Das Saatmittel des Pakets trifft die Kontinuumsloesung an mindestens 80 % der Pruefpunkte innerhalb 3 Standardfehlern (groesste Dichte) | 50 % |
| KV2 | [H] Die relative Streuung an den Pruefpunkten ist bei der groessten Dichte kleiner als 50 % und faellt mit rho | 40 % |
| KV3 | Stabil: Die Norm waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 55 % |

**Bedeutung (vorab):**
- **KV1 bis KV3 treffen ein:** Auch in 3+1 laeuft eine Welle auf dem Raumzeit-Netz ohne Ruhesystem im Mittel richtig
  und stabil. Ueberleitung 3 bliebe tragfaehig, mit Rauschen als Preis der Nichtlokalitaet.
- **KV2 verfehlt:** In 3+1 ist das Rauschen bei machbaren Dichten zu gross. Dann braucht es Glaettung (Sorkins
  Nichtlokalitaetslaenge) oder viel groessere Netze.
- **KV3 verfehlt:** Instabilitaet in 3+1; das waere ein ernster Einwand gegen Ueberleitung 3.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
