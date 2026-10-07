# Einordnung: Tetraederketten, Schnitte und Schnittpunkte (Buendel von Finn, 02.10.2026)

- Leitung: claude-primary. Geschrieben ab 2026-10-02 07:48:16 CEST (date).
- Auftrag Finn: ".../tetra_chain_slice_intersections_bundle.zip analysieren einordnen codex geben".
- Quelle: /home/fmh/Downloads/tetra_chain_slice_intersections_bundle.zip (sha256 4327d0e2..., 805 721 Bytes, 14 Dateien
  vom 02.10. 05:06).
  - Kopie und Entpackung in diesem Ordner; Pruefsummen in BUNDLE-SHA256SUMS.txt.
  - Inhalt: eine Markdown-Notiz, 4 CSV, 9 PNG. Kein Code, nichts ausgefuehrt.

## Was es ist

Geometrie und Kombinatorik ebener Schnitte durch zwei flaechenverbundene Tetraederketten:

| Modell | Tetraeder | Ecken | Kanten |
|---|---|---|---|
| "11+1" | 9 | 12 | 30 |
| "19+1" | 17 | 20 | 54 |

Bei N Tetraedern hat eine Flaechenkette N + 3 Ecken und 3N + 3 Kanten; beide Modelle passen dazu. Was "11+1" und "19+1"
bedeuten, steht nicht im Buendel [H: 11 bzw. 19 Ecken plus eine ausgezeichnete].

Drei Teile:

1. **Zaehlregel** fuer generische Ebenen, die keine Ecke treffen: P = T3 + 2 T4 + 2 C.
   - P: eindeutige Schnittpunkte mit Kanten. T3, T4: geschnittene Tetraeder mit Dreieck- bzw. Viereckschnitt.
     C: getrennte Schnittinseln.
2. **Verteilungen von P** bei zufaelliger zentraler Orientierung der Ebene:
   - 11+1: P von 6 bis 16, Mittel 10,20
   - 19+1: P von 6 bis 28, Mittel 12,63
   - mehrere Inseln mit 0,1 % bzw. 1,2 %
3. **"Ticks"**: Eine Ebene dreht sich um 180 Grad. P aendert sich stufenweise, wenn sie eine Ecke passiert; manche
   Durchgaenge aendern P nicht (Identitaets-Ticks). Das Profil ist symmetrisch, mit dem Maximum 28 bei der Haelfte.

## Pruefung durch die Leitung (Schreibtisch, ohne Rechner)

- **Die Zaehlregel stimmt** [ES, Beweisskizze]:
  - Jeder geschnittene Tetraeder liefert 3 bzw. 4 Punkte. Eine geschnittene gemeinsame Flaeche zweier Nachbarn
    identifiziert 2 Punkte.
  - In einer Kette liegen die geschnittenen Tetraeder in C zusammenhaengenden Laeufen, also gibt es S - C Nachbarschaften.
  - Daraus folgt P = 3 T3 + 4 T4 - 2 (S - C) = T3 + 2 T4 + 2 C.
  - **Bedingung:** Zwei benachbarte geschnittene Tetraeder muessen auch ihre gemeinsame Flaeche geschnitten haben. Das
    gilt, wenn die Doppelpyramide zweier Nachbarn konvex ist, die Verbindungslinie der Spitzen also durch die gemeinsame
    Flaeche geht. Fuer regulaere Tetraeder ist das so; fuer verzerrte Ketten muesste man es pruefen.
  - Kanten, die zu drei aufeinanderfolgenden Tetraedern gehoeren, zaehlt die Regel richtig (dreimal gezaehlt, zweimal
    identifiziert).
- **Die Beispiele erfuellen die Regel**, alle sechs: 6 = 2 + 2 + 2; 16 = 4 + 10 + 2; 14 = 6 + 4 + 4; 28 = 8 + 18 + 2;
  24 = 12 + 8 + 4.
- **Die Tabellen sind in sich stimmig** (von Hand nachgerechnet):
  - Die Wahrscheinlichkeiten summieren sich je Modell zu 1.
  - Die Mittelwerte aus den Verteilungen ergeben genau 10,204375 und 12,633465, wie in der Zusammenfassung.
  - Die Mediane (10) passen.
  - Die Feinheit der Wahrscheinlichkeiten (Vielfache von 0,000005) spricht fuer 200 000 Stichproben je Modell [ES].
- **Paritaet:** P hat dieselbe Paritaet wie T3 [ES]. Ungerade P (11, 13, 15, 21, 23, 25, 27) brauchen eine ungerade Zahl
  von Dreieckschnitten.

## Einordnung

- **Mathematisch:** eine korrekte, elementare Zaehlregel (Inklusion-Exklusion entlang der Kette) und eine
  Monte-Carlo-Statistik.
  - Die Kette sieht nach einer Boerdijk-Coxeter-Helix (Tetrahelix) aus [L?, aus dem Gedaechtnis]; das Buendel sagt das
    nicht.
  - Die Verteilung haengt an der Kettengeometrie, am Stichprobenmass ("zufaellige zentrale Orientierung") und an der
    Laenge. Sie ist keine universelle Groesse.
- **Physikalisch:** Es gibt keine Feldgleichung, keine Dynamik und keine Messgroesse. Damit gibt es keinen direkten
- **Moeglicher Bezug [H]:** Finns Strang "natuerliche Grundbewegung / Dimensionsbildung" bei Codex (ag-phy-tus, 01.10.,
  resonance-20260930/concept-review-tus/TETRAEDER-20261001.txt).
  - Ein 2D-Schnitt durch eine 3D-Struktur liefert diskrete Zaehlwerte.
  - Eine drehende Schnittebene erzeugt "Ticks", eine Art geometrischer Takt.
  - Physikalische Bedeutung haette das erst mit einer Dynamik (was dreht sich, warum) und einer Messgroesse.
- **Fuer die Reproduzierbarkeit fehlt:**
  - Code
  - Kettengeometrie: Koordinaten, Regularitaet, Drehsinn
  - Definition "zentral" und Mass der Ebenennormalen
  - Zahl der Stichproben
  - Drehachse der Ticks
  - Bedeutung von "11+1" und "19+1"

## An Codex weitergegeben (Peerbus, kind task)

Unabhaengiger Nachbau der Kettengeometrie und der Zahlen, Beweis der Zaehlregel samt Konvexitaetsbedingung, Anschluss an
den Tetraeder-Strang. Physikalische Lesart nur als Hypothese mit pruefbarem Unterscheidungspunkt.

## Berichtigung nach Codex (TETRA-RECON-1, 02.10.2026)

Die Konvexitaet der Doppelpyramide ist keine Bedingung der Zaehlregel selbst. Codex zeigt: Mit C als Zahl der
Flaechengraph-Komponenten der geschnittenen Tetraeder gilt die Regel unter Einbettungs- und Stapelbedingungen allgemein.
Konvexitaet wird nur gebraucht, um C mit Indexlaeufen gleichzusetzen. Meine Beweisskizze oben lief ueber Indexlaeufe und
ist darum nur unter dieser Zusatzbedingung richtig.
