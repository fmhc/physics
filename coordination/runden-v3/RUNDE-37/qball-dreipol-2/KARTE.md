# QBALL-DREIPOL-2: Ist das einfarbige Q-Ball-Dreieck stabil, gibt es es auch in 3D, und bleibt ein schiefer Dreier gebunden? (Runde 42, Fast Lane)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 18:02:54 CEST (date), vor jeder
  Rechnung.
- **Herkunft:** QBALL-DREIPOL-1 (RUNDE-37/qball-dreipol-1/ERGEBNIS.md, 2D-Gitter L = 64, N = 256, Papier-I-Potential
  mit drei Komponenten und g4 sum |phi_a|^4).
  - Neu und ohne Urteil: Bei g4 = -0,1 endet der Fluss bei festen Ladungen in einem festen Dreieck aus drei einfarbigen
    Klumpen. Paarabstand 1,245 R; das Dreieck liegt 0,146 unter dem Mischball.
  - Gerechnet ist das nur im symmetrischen Unterraum; Minimum oder Sattel ist offen.
  - In echter Zeit pulsiert der symmetrische Dreier ("atmender Klumpen"). Das ist durch Energieerhaltung weitgehend
    erzwungen (Startenergie unter drei getrennten Baellen).
- **Finns Bild:** Q-Baelle als 3 Pole "auf 3d/4d" (17:11 bis 17:13). Dazu atmende Punkte (ATEM-NETZ-1, laeuft).
- **Regel Dimensionsvergleich (AGENTS.md, Finn 04.10.):** Eine Bindungsaussage aus 2D gilt nicht ungeprueft in 3D.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [P] Projektdatei, [L] Literatur, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung; nach dem Rueckfall bei QBALL-DREIPOL-1 ausfuehrlich)

**Vorab ableitbar:**
- Verschmelzen ist bei konkavem E(Q) immer guenstig, also ist ein Dreier "gebunden" gegen drei getrennte trivial
  (QD2-Lehre). Deshalb keine Vorhersage dazu.
- Die Energieerhaltung verbietet das Auseinanderfliegen aller drei, solange E_start < 3 E_1 (QD3-Lehre).
- Der Vergleich Mischball gegen Einpolball folgt in 3D aus radialen Loesungen; nur Kontrolle.

**Nicht ableitbar:**
- (a) Ist das 2D-Dreieck bei g4 = -0,1 ausserhalb des symmetrischen Unterraums ein Minimum? Untersucht werden
  Verschiebungen, Ladungsverschiebung zwischen den Klumpen und Phasenversatz.
- (b) Gibt es in 3D ein festes Dreieck aus drei einfarbigen Klumpen (oder eine andere Mehrklumpen-Form), und liegt es
  unter dem 3D-Mischball?
- (c) Bleibt ein schiefer Dreier in echter Zeit beisammen, oder wird ein Pol ausgestossen, waehrend zwei verschmelzen?
  Die Energie erlaubt das.

**Projekt-grep (18:00 bis 18:03):**
- QBALL-DREIPOL-1, QBALL-PYRO-1, QB-BS-2D (drehender Knoten plus Q-Ball nicht gebunden).
- RUNDE-02: Q-Baelle verschmelzen gleichphasig.
- Kein Mehrkomponenten-Dreieck in 3D und keine Stabilitaetsprobe des Dreiecks.

## Auftrag (Code-Agent)

1. Code aus qball-dreipol-1/code/ kopieren (dreipol.py, Laeufe, Auswertung), nicht dort aendern.
2. **Teil A (2D):**
   - Dreieck bei g4 = -0,1 nachbauen (Kontrolle).
   - Dann je 6 Stoerungen ausserhalb des Unterraums:
     - 2 Verschiebungen (asymmetrisch)
     - 2 Ladungsverschiebungen +-5 % zwischen zwei Klumpen
     - 2 Phasenversaetze
   - Fluss bei festen Ladungen: Kehrt er zurueck? Abstand zum Dreieck ueber den Fluss; Energie am Ende gegen das Dreieck.
3. **Teil B (3D):**
   - Dieselbe Rechnung mit drei Komponenten auf einem 3D-Gitter. Gitter und Kasten im Plan begruenden, mit Gitterprobe;
     Rechenweg auf der .69-GPU, wenn noetig.
   - Messen:
     - 3D-Einpolball und 3D-Mischball (radial und auf dem Gitter)
     - Fluss vom beruehrenden Dreieck bei g4 = -0,1 und +0,1
     - Endform (Dreieck, Mischball, anderes), Energien
4. **Teil C (2D, echte Zeit):**
   - Schiefer Start: ein Pol 10 % weiter weg, eine Ladung 5 % kleiner. 4 Saaten mit kleinem Rauschen, bis t = 300.
   - Messen: Anteil jeder Polladung im Haufen, Ausstoss (ein Pol ueber 4 R von der Mitte) und Pulsationsdauer.
5. Plan, Rauchlauf und Einfrieren wie ueblich; Auswerte-Code vor jeder Sicht auf Hauptergebnisse einfrieren.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DP0 | Kontrolle: 2D-Dreieck bei g4 = -0,1 nachgebaut (Paarabstand 1,245 R auf 2 %, Abstand zum Mischball 0,146 auf 10 %); 3D-Gitter gegen 3D-radial auf 1e-4 | 85 % |
| DP1 | [H] Das 2D-Dreieck ist ein lokales Minimum: alle 6 Stoerungen kehren zurueck (Endabstand < 2 % R, Energie gleich auf 1e-3) | 45 % |
| DP2 | [H] In 3D endet der Fluss bei g4 = -0,1 in einem festen Dreieck aus drei einfarbigen Klumpen, und es liegt unter dem 3D-Mischball | 30 % |
| DP3 | [H] Der schiefe 2D-Dreier bleibt beisammen: in >= 3 von 4 Saaten bis t = 300 kein Ausstoss und je Pol >= 90 % der Ladung im Haufen | 55 % |

**Bedeutung (vorab):**
- **DP1 und DP2 treffen ein:** Im Q-Ball-Modell gibt es einen echten Dreier aus drei "Farben", der weder verschmilzt
  noch zerfaellt. Er waere ein Kandidat fuer Finns Drei-Pol-Teilchen; Farbeinschluss ist er trotzdem nicht (U(1)^3,
  einzelne Pole stabil).
- **DP1 verfehlt:** Das Dreieck ist ein Sattel, also eine Durchgangsform.
- **DP2 verfehlt:** Das Dreieck ist eine 2D-Besonderheit (Dimensionsregel).
- **DP3 verfehlt:** Der atmende Dreier ist nur im symmetrischen Fall beisammen; schief stoesst er einen Pol aus.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren p4000a und p4000b (frei seit QBALL-DREIPOL-1). Je Lauf <= 10 min,
  1 Thread bzw. eine GPU. Zeitbox 150 min.
- Teil B darf auf eine kleinere Ladung bzw. ein groberes Gitter ausweichen, wenn die Gitterprobe das traegt; sonst Teil B
  als "nicht machbar in 10 min" melden.
