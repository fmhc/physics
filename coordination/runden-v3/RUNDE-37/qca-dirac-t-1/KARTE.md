# QCA-DIRAC-T-1: Bekommt das Spin-1/2-Teilchen der Tetraeder-Quantenregel eine Masse, ohne die Symmetrie zu brechen? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 08:03:06 CEST (date), vor jeder Rechnung.
- **Anlass:** QCA-DIAMANT-4, Teil B.
  - Auf BCC (acht Tetraederrichtungen je Knoten) gibt es mit 4 Zustaenden und voller Tetraedergruppe T zwei exakt
    isotrope Weyl-Kegel (v = 1/3, entgegengesetzte Chiralitaet, 360 Grad = -1), mit Spinordarstellung 2+2'.
  - Eine Dirac-Masse verbietet dort die Symmetrie, weil 2 und 2' inaequivalent sind.
  - Fuer 2+2, wo sie erlaubt waere, fand die Suche keinen Automaten (Defekt 4/45, nicht bewiesen).
- **Frage:** Massive Spin-1/2-Teilchen (Dirac) aus einer voll tetraedersymmetrischen Quantenregel. Geht das mit mehr
  inneren Zustaenden, oder braucht Masse einen Symmetriebruch, wie beim Higgs-Mechanismus?
- Kennzeichen: [M] Mathematik, [L] Literatur, [L?] unsicher, [H] Hypothese.

## Vorgehen (Code-Agent)

- **Schreibtisch zuerst (Pflicht):**
  - Darstellungstheorie von 2T fuer 8 innere Zustaende: welche Zerlegungen erlauben einen T-invarianten Massenterm, der
    die Chiralitaeten koppelt?
  - Gibt es einen Beweis, dass 2+2 bei 4 Zustaenden keinen Automaten hat (oder einen Gegenbeweis)?
  - Bewiesenes als vorab ableitbar kennzeichnen.
- **Teil A (4 Zustaende, 2+2):** Suche mit mehr Starts und allen Muenzen bzw. Sprungformen aus QCA-DIAMANT-4 Teil B.
  Beweis oder Treffer.
- **Teil B (8 Zustaende auf BCC, T-kovariant):**
  - Zerlegungen, die eine Masse erlauben, z. B. 2+2'+2+2' oder 2+2+2'+2', nach Schreibtisch.
  - Ansatz "Muenze mal Tetraederverschiebung" wie in QCA-DIAMANT-4 und eine allgemeinere Nachbarform.
  - Treffer einordnen: masselose Kegel oder Masse (Luecke bei k = 0 mit omega^2 ~ m^2 + v^2 k^2). Dazu 360 Grad und
    Isotropie.
- **Kontrolle:** der Dirac-Automat der Quelle (D'Ariano/Perinotti, unter L_2) mit Masse; Luecke und Kegelform.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QM-D0 | Kontrolle: Der L_2-Dirac-Automat der Quelle hat bei k = 0 eine Luecke 2m (bzw. nach Quelle) und isotrope Kruemmung auf 1e-3 | 85 % |
| QM-D1 | [H] Teil A: Mit 4 Zustaenden und 2+2 gibt es unter T keinen nichttrivialen unitaeren Automaten (Beweis oder >= 200 Starts ohne Treffer) | 60 % |
| QM-D2 | [H] Teil B: Mit 8 Zustaenden auf BCC gibt es einen T-kovarianten unitaeren Automaten mit Luecke bei k = 0 (massiv), dessen tiefste Baender sich wie Spin 1/2 drehen (360 Grad = -1) | 40 % |
| QM-D3 | [H] Falls QM-D2: Die Dispersion um k = 0 ist isotrop (Richtungsstreuung der Kruemmung <= 1e-3) | 50 % |

**Bedeutung (vorab):**
- **QM-D2 und QM-D3 treffen ein:** Mit acht Zustaenden traegt das Tetraeder-Netz massive, isotrope Spin-1/2-Teilchen bei
  voller Symmetrie, also ein Elektron-Gegenstueck.
- **QM-D2 verfehlt:** Masse braucht einen Bruch der Tetraeder-Symmetrie (oder ein zusaetzliches Feld, das sie spontan
  bricht). Das ist eine Parallele zum Higgs-Mechanismus [H]: Masselose chirale Teilchen sind die natuerliche Grundform des
  Netzes.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu5 und p4000b; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
