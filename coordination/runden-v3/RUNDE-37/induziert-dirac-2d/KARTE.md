# INDUZIERT-DIRAC-2D: Gibt ein Fermion auf dem Zufallsnetz mit "Zahl = Volumen" die richtige Anomaliezahl, oder verraten Doppler sich als Vielfaches? (Runde 39)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 09:47:38 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - INDUZIERT-DICHTE-2D und -GROB: Ein Skalar auf einem Zufallsnetz mit Punkten nach Flaeche und Neuvernetzung gibt
    Polyakovs konforme Steifigkeit, 1,075 P +- 0,071 P (P = -1/(24 pi), zentrale Ladung c = 1).
  - SPIN-KAUSAL-L und SPIN-ZUFALLSNETZ-1 (laeuft): Spin ist auf Zufallsnetzen nur einsetzbar. Ob Doppler verschwinden,
    ist in der Literatur gespalten.
- **Idee [M/L]:**
  - Die Anomaliezahl zaehlt Freiheitsgrade: Ein Dirac-Fermion hat in 2D c = 1, also die gleiche Polyakov-Steifigkeit
    wie ein Skalar (Vorzeichen nach Konvention von log det beachten).
  - Ein naives Gitterfermion mit 4 Dopplern gaebe c = 4.
  - Die induzierte konforme Steifigkeit ist damit ein Doppler-Zaehler, und zugleich ein Test, ob Fermionen auf dem
    Netz mit "Zahl = Volumen" ebenfalls die richtige Schwerkraft-Antwort geben.
- **Projektbezug:** RUNDE-22 (geometrie-stand) kannte Kaehler-Dirac-Fermionen auf zufaelliger Geometrie. Kaehler-Dirac
  hat in 2D zwei Dirac-Fermionen, also c = 2 [L?].
- Kennzeichen: [M] Mathematik, [L] Literatur, [L?] unsicher, [H] Hypothese.

## Test (Code-Agent)

- **Geometrie und Netz:** wie INDUZIERT-DICHTE-2D. Punkte nach physikalischer Flaeche, Neuvernetzung je Verformung,
  S = 0,5, k-Fenster und k^4-Ausgleich wie in -GROB, zwei Netzabstaende.
- **Fermion:** zwei Bauweisen, im Plan begruendet.
  - (A) naiver Dirac-Operator mit eingesetztem Rahmen: Kanten-Glieder (i/2) w_ij (sigma . n_ij); Gewichte w_ij aus
    Delaunay bzw. Voronoi wie beim Skalar.
  - (B) Kaehler-Dirac (d + delta auf 0-, 1- und 2-Formen des Simplexkomplexes). Erwartet sind dann 2 Dirac-Fermionen,
    also c = 2.
- **Messgroesse:** konforme Steifigkeit aus log abs det D = 1/2 log det(D^dagger D), mit Nullmoden-Behandlung im Plan;
  daraus c_eff = Steifigkeit / P mit Vorzeichen nach Fermion-Konvention.
- **Kontrollen:**
  - Regelmaessiges Quadratnetz mit Bauweise (A): naive Doppler, c_eff ~ 4.
  - Der Skalar-Code aus -GROB auf denselben Netzen gibt c_eff ~ 1.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| ID-F0 | Kontrolle: Regelmaessiges Netz mit (A) gibt c_eff = 4 +- 1 (Doppler); Skalar auf den Zufallsnetzen c_eff = 1 +- 0,2 | 75 % |
| ID-F1 | [H] Zufallsnetz mit (A): c_eff = 1 +- 0,4, also keine Doppler in der Anomalie | 35 % |
| ID-F2 | Zufallsnetz mit (B) Kaehler-Dirac: c_eff = 2 +- 0,5 | 55 % |
| ID-F3 | [H] Vorzeichen der induzierten konformen Steifigkeit wie beim Skalar (Polyakov-Vorzeichen) fuer beide Bauweisen | 60 % |

**Bedeutung (vorab):**
- **ID-F1 trifft ein:** Auf einem Zufallsnetz mit Punkten nach Flaeche verschwinden die Doppler, und das Fermion gibt die
  richtige Schwerkraft-Antwort. Materie mit halbem Spin und Schwerkraft aus Materie passen dann auf dieselbe Buehne
  [H, 2D euklidisch].
- **ID-F1 verfehlt (c_eff ~ 4):** Die Doppler bleiben. Fermionen brauchen dann eine Bauweise wie Kaehler-Dirac (ID-F2)
  oder Zusatzglieder.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu7; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 150 min.
