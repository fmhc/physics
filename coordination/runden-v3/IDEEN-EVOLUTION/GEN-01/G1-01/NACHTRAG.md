# G1-01 Nachtrag (Test-Agent T-2)

- 2026-09-30 08:08:05 CEST (date): Code und Formprobe, KARTE.md unveraendert seit 07:58:24.
- Code neu geschrieben (pinning1d.py), keine Kopie: Keine Rundenvorlage rechnet stationaere Gitterloesungen per Newton
  in Q. tests1d.py und r5a.py schiessen im Kontinuum.
- Umsetzung der Plausibilitaetspruefung dE/dQ = omega:
  - Der zentrale Differenzenquotient (E_{k+1} - E_{k-1}) / (2 dQ) wird mit dem Simpson-Mittel
    (omega_{k-1} + 4 omega_k + omega_{k+1}) / 6 verglichen.
  - Mit dem blossen Mittelpunktwert omega_k haette der Abbruchfehler dQ^2 omega''/6 bei h = 1 etwa 4e-4 relativ
    betragen und die Schranke 1e-4 ohne echten Fehler gerissen.
  - Festgelegt vor jedem Lauf, als Papierabschaetzung, nicht nach einem Ergebnis.
- Formprobe 08:02 (lokal, 1 Thread, nice 19): laeuft, rc 0. Die dabei gedruckten Zahlen gelten nicht (verkuerzter
  Q-Bereich) und werden nicht geerntet.
- Rauschschwellen im Code (nicht in KARTE.md beziffert):
  - Extrema von omega^2(Q) zaehlen erst ab 1e-14 Umkehr.
  - "2 Loesungen je Q" gilt ab einem Energieabstand von 1e-12, gleich der Schranke von V4.
  - Der Fit fuer c nimmt nur A_E > 1e-13.

## Nachtrag 2 (2026-09-30 08:17:14 CEST, date), vor jedem echten Lauf

- Newton stagnationsfest gemacht:
  - Konvergiert heisst: Schritt unter 1e-13, oder ab Iteration 3 Schritt unter 1e-9 und nicht mehr quadratisch fallend
    (Rundungsboden).
  - Danach folgt ein Nachschritt. Dessen |d omega| (in omega^2 umgerechnet) ist das Rauschmass je Punkt.
  - Grund: Auf feinen Gittern (Eintraege ~ 4/h^2) kann der Rundungsboden die starre Schranke 1e-13 knapp verfehlen. Dann
    haette die Plausibilitaet "Newton nicht konvergiert" ohne echten Fehler gemeldet.
- Die Schwelle fuer Extrema von omega^2(Q) ist jetzt max(1e-14, 10 x groesstes Rauschmass des Zweigs). Damit ist "ueber
  dem Rauschen" der Karte konkret gemessen.
  - Formprobe: Rauschmass bei h = 0,1 etwa 1e-15, Schwelle also etwa 1e-14.
  - Die letzte Newton-Korrektur allein haette das Rauschen ueberschaetzt (4,6e-13 bei h = 0,5), weil sie bei
    quadratischer Konvergenz noch eine echte Korrektur ist.
- Formprobe erneut 08:17:07, rc 0. Neue Laufzeitschaetzung in LAUF.txt. Formprobe-Zahlen werden nicht geerntet.
