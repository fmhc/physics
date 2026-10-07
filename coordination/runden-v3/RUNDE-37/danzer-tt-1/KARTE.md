# DANZER-TT-1: Werden Schwerewellen auf den Ikosaeder-Naeherungsnetzen von Stufe zu Stufe richtungsgleicher, so wie die Symmetrie es verlangt? (Runde 48, Vorschlag aus CODEX-REVIEW-R48)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 10:24:30 CEST (date), vor jeder Rechnung.
- **Herkunft:**
  - Der unabhaengige Pruefer CODEX-REVIEW-R48 (RUNDE-37/codex-review-r48/REVIEW.md, "Was fehlt", Punkt 2): Ikosaedersymmetrie liefert einen Grund fuer die Isotropie aller langwelligen Formen, nicht nur eine Abstimmung. Sein Test: die TT-Spanne auf den Danzer-Naeherungen.
  - Projektbefunde [P]:
    - DANZER-NAEHERUNG-1 und -2: Skalar und Maxwell auf den Ammann-Kramer-Naeherungen 1/1, 2/1, 3/2 (5/3); der kubische a2-Anteil faellt von Stufe zu Stufe.
    - TT auf diesen Netzen ist nicht gerechnet.
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Ableitbarkeitsprobe (Leitung, verkettet)

- **Vorab ableitbar [M]:**
  - Die Ikosaedergruppe hat keine Invariante bei l = 4 (erst bei l = 0, 6, 10 usw.). Ein langwelliger Rang-4-Tensor mit voller Ikosaedersymmetrie ist deshalb isotrop.
  - Im Quasikristall-Grenzfall ist die TT-Ausbreitung langwellig also isotrop, unabhaengig von der Masse, sofern sie die Symmetrie behaelt.
  - Naeherungen haben nur Wuerfelsymmetrie; ihr kubischer l = 4-Anteil muss mit der Ordnung gegen null gehen.
- **Nicht ableitbar:**
  - wie schnell der kubische TT-Anteil faellt (beim Skalar mit Einheitsgewichten folgte er nicht der Phason-Regel, mit Takt-Gewichten linear in eps)
  - ob die Netze mit der Projektmasse (A1, R1) stabil sind
  - ob es einen Boden gibt
- **Kennzahlen-Abgleich:** Die Naeherungsnetze gibt es nur aus DANZER-NAEHERUNG-1 und -2; TT darauf ist neu.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DT0 | Kontrolle: Der TT-Code gibt auf V die TT-ISO-1-Spanne 6,34 % (A1, R1) auf 1e-3 wieder | 90 % |
| DT1 | [H] Mit A1 und R1 faellt die TT-Spanne von 1/1 zu 3/2 auf hoechstens ein Drittel | 50 % |
| DT2 | [H] Die Naeherungen 1/1 bis 3/2 sind mit A1 und R1 an allen gerechneten k stabil | 60 % |
| DT3 | [H] Bei 3/2 liegt die TT-Spanne ohne Abstimmung unter der von A15 (0,934 %) | 45 % |

**Bedeutung (vorab):**
- **DT1 und DT2 treffen ein:** Ikosaedrische Ordnung ist ein Grund fuer die Richtungsgleichheit der Schwerewellen, ohne Abstimmung, und damit emergent. Der Quasikristall-Zweig waere fuer GW170817 der natuerliche Kandidat.
- **DT1 verfehlt:** Die Symmetrie setzt sich erst bei hohen Stufen durch, oder es gibt einen Boden.

## Rahmen

- Code-Agent. Netzbau aus danzer-naeherung-1/code und danzer-naeherung-2/code, TT aus tt-iso-1/code bzw. tt-glas-1/code kopieren, dort nichts aendern.
- Masse A1 und R1 (Projektstandard). Die Lund-Regge-Masse laeuft separat (LUND-REGGE-MASSE-1); nicht doppeln.
- Delaunay-Gleichstaende so aufloesen wie in DANZER-NAEHERUNG-2 und melden.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu8, cpu9 und cpu10. Je Lauf hoechstens 10 min. Zeitbox 150 min.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
- Synthetisch, keine Messdatenbestaetigung.
