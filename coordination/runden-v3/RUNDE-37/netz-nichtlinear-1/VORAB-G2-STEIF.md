# VORAB-G2-STEIF: Integrator mit CFL, vor jeder Rechnung

- Geschrieben 2026-10-06T20:34:37+02:00 (date), Sitzung Cursor Grok, vor jedem Lauf.
- Karte NETZ-NICHTLINEAR-1 unveraendert (N1 bis N4). Dies ist der fehlende Integrator fuer N4 / G2, nicht eine neue Karte.
- Synthetisch, keine Messdaten. 3D-Glas N = 128; keine 1D/2D-Variante in diesem Lauf (Traegheit ist die reduzierte 3D-Flaeche der 4D-Wirkung).

## Was anders ist als der gescheiterte G2-Versuch

Der vorige G2-Lauf (stueckweise M_eff alle 200 Schritte, festes dt, Leapfrog dazwischen) brach mit "Metrik nicht positiv" ab. Lesart hier [H]: zuerst explodiert der Integrator (omega_max * dt > 2), danach ist der Zustand kein zulässiges Netz mehr. Ein steifer bzw. CFL-angepasster Schritt muss das trennen.

Wahl, begruendet:

1. Implizite Mitte in jedem Schritt (A-stabil fuer den linearen Teil, symplektisch, Energie bis auf den Integrationsfehler).
2. Nach jedem Operatorwechsel dt so setzen, dass omega_max * dt <= 0,25.
3. M_eff nicht alle 200 Leapfrog-Schritte nachfuehren. Zwei Stufen: (F) Operatoren eingefroren am Hintergrund; (P) einmal je Periode am aktuellen x neu bauen, bei "Metrik nicht positiv" den alten Operator behalten und den Fehlschlag zaehlen.

Nicht gewaehlt: dM/dl per finiter Differenz (128 Richtungen, ~10 min, sprengt das 10-min-Limit). Das bleibt eine Luecke gegenueber der vollen Hamiltonfunktion mit Ableitungstermen.

## Eigene Erwartungen (scheiterfaehig)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| S0 | Stufe F, glas-N128-s4, 10 Perioden, A = 1e-3: max \|H-H0\|/H0 < 1e-8 (das ist N4 fuer eingefrorene Operatoren) | Drift >= 1e-8 oder Abbruch | 85 % |
| S1 | Stufe P, dasselbe Netz: max \|H-H0\|/H0 < 1e-6; kein Metrik-Abbruch; M_n_neg bleibt 128 | Drift >= 1e-6, Metrik-Fehler, oder extra negative Richtungen | 55 % |
| S2 | G1 mit CFL auf s4 Arm b-R, 10 Perioden: kein Leapfrog-Weglaufen; Enddrift < 1e-4 relativ; nach Zuegen 128 negative Richtungen | Drift >= 1e-4 oder extra negative Richtungen | 50 % |
| S3 | G1 mit CFL auf s2 Arm b-R: nach dem echten Ausnahmezug bleiben extra negative Richtungen (nicht 128) | Die extra Richtungen verschwinden | 70 % |

S0 ist Integratorkontrolle. S1 ist G2 ohne Zuege mit periodischer Nachfuehrung. S3 ist die Physikfrage; ein Treffer waere kein Beweis, dass Ausnahmezuege "echt" sind, nur dass CFL sie nicht wegraeumt.
