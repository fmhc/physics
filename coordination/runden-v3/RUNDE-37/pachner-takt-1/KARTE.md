# PACHNER-TAKT-1 mit TAKT-KOMMUTATOR-1: Finns Flip-Flop als Umbau-Takt auf dem Tetraeder-Netz, und kommutieren zwei lokale Takte? (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 16:15:31 CEST (date), vor jeder
  Rechnung.
- **Herkunft:**
  - Kartenvorschlag K1 aus TETRAEDER-L (RUNDE-37/tetraeder-l/DOSSIER.md, "PACHNER-TAKT-1")
  - Kartenvorschlag aus TAKT-UMBENENNUNG-L (RUNDE-37/takt-umbenennung-l/DOSSIER.md, Z. 331 ff., "TAKT-KOMMUTATOR-1")
  - Zusammengelegt, weil beide dasselbe Netz und denselben Code brauchen.
  - Ersetzt FLIPFLOP-ZWEIWELTEN-1.
- **Finns Bild (04.10.):**
  - Flip-Flop zwischen Auf- und Ab-Tetraedern je Takt ("negativ-positiv-Flopping")
  - "ein dark tick der pro einzelteil einzeln laeuft"
  - Lesart der Flip-Flop-Rueckfrage im Chat (16:00): Standard ist C, solange Finn nichts anderes sagt; bis jetzt keine
    andere Antwort.
- **Lesarten des Flip-Flops (TETRAEDER-L):**
  - (A) raeumliche Inversion bzw. Kopientausch: Umbenennung ohne Zug, vorab ableitbar, keine Dynamik
  - (B) 1-4 bzw. 4-1 je Tetraeder: traegt keine Kruemmung (Hoehn 2014, S. 6 [S]), also 0 Gravitonen, vorab ableitbar
  - (C) Diagonalwechsel in den Oktaedern im Takt (4-4-Wechsel = 2-3 gefolgt von 3-2 [L]). Offen ist, ob ein periodischer
    Takt auf festem Netz konsistent ist und wie viele Gravitonen je Takt propagieren.
- **Kopplung der zwei Welten (vorab, [M] aus TETRAEDER-L, R4):** Ein Takt koppelt die beiden Kopien nur, wenn seine Zuege
  Kanten zwischen Ecken beider Teilgitter erzeugen. Das wird im Schreibtisch des PLAN fuer C entschieden; es ist keine
  Messung.
- **TAKT-KOMMUTATOR-1 (Weg-Unabhaengigkeit nach HKT auf dem Gitter):**
  - Zwei Zeltzuege (Eckverschiebung, "Zeltstange", an benachbarten Regge-Ecken A und B, in B1 an den Tetraedermitten)
    in der Reihenfolge AB gegen BA, mit lokalem und mit globalem Takt.
  - Vorab ableitbar und damit nur Kontrollen: kein Unterschied ohne Kruemmung, Wachstum mit dem Quadrat der Amplitude
    eps, die Global-Variante.
  - Nicht ableitbar: Vorfaktor und Abhaengigkeit von L/a auf dieser Geometrie, Auf- gegen Ab-Kopie, Drift ueber viele
    Takte. Vermutung des Agenten: eps^2 (a/L)^4.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [S] an der Quelle gelesen, [P] Projektdatei, [L] Literatur aus dem
  Gedaechtnis, [H] Hypothese.

## Auftrag (Code-Agent)

1. **Lesen:**
   - RUNDE-37/tetraeder-l/DOSSIER.md (Frage 3, K1, Gegensweep) und quellen/ (Hoehn 2014, Dittrich/Hoehn)
   - RUNDE-37/takt-umbenennung-l/DOSSIER.md (Abschnitte 4 und 5, Kartenvorschlag)
   - RUNDE-37/tensor-eis-pyro-1/ (B1, Code tp.py nur kopieren)
   - RUNDE-36/REGEL.md
2. **Schreibtisch im PLAN:**
   - Netz: kleine periodische fcc-Zelle, eine B1-Kopie, Oktaeder mit Diagonale.
   - Linearisiertes kanonisches Regge nach Hoehn, Zugfolge C.
   - Entscheidung zu R4 fuer C: koppelt C die Kopien, ja oder nein, mit Begruendung.
   - Kommutator: Definition von "Zustand nach AB" gegen "nach BA", Hintergrund mit Kruemmung (Fehlwinkel eps), L/a in
     mindestens drei Stufen.
   - Kontrollen: B gibt 0 Gravitonen; kein Kommutator ohne Kruemmung.
3. **Plan, Rauchlauf, Einfrieren wie ueblich.**

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PT0 | Kontrollen: Lesart B gibt 0 Gravitonen; ohne Kruemmung ist der Kommutator null (auf 1e-10); mit Kruemmung waechst er wie eps^2 (Steigung 1,8 bis 2,2) | 85 % |
| PT1 | [H] Lesart C ist auf dem festen periodischen Netz als Takt konsistent: Nach einem vollen Takt sind die Zwangsbedingungen wieder loesbar, und ihr Rang ist gleich | 50 % |
| PT2 | [H] Ein C-Takt traegt je Zelle mindestens ein propagierendes Graviton (nicht nur Eichung) | 40 % |
| PT3 | [H] Lokaler Takt: Der Kommutator faellt mit der Gitterweite wie (a/L)^p mit p zwischen 3 und 5 | 40 % |

**Bedeutung (vorab):**
- **PT1 und PT2 treffen ein:** Finns Flip-Flop ist als lokaler Umbau-Takt rechenbar und traegt Schwerkraft.
- **PT1 verfehlt:** Ein periodischer Flip-Flop auf festem Netz ist inkonsistent. Dann bleibt nur ein unregelmaessiger
  bzw. von der Geometrie gesteuerter Takt.
- **PT3 trifft ein:** Lokale Takte kommutieren auf feinen Netzen schnell besser. Die freie Zeitumbenennung, also die 1/2,
  kommt im Feinen zurueck, wie Bahr/Dittrich es fuer Regge erwarten lassen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, auf den Spuren, die die Leitung beim Start eintraegt; je Lauf
  <= 10 min, 1 Thread. Zeitbox 150 min.

## Lesepunkt (Leitung, 2026-10-04 16:16:49 CEST)

- arXiv-Scout 04.10.: Yan/Ding/Ma/Zhang, "Dynamics of Regge calculus with torsion", arXiv:2610.00593 (gr-qc). Optional ein
  Abruf (Abstract): Regge-Dynamik mit Torsion; Torsion koppelt an Spin, Bezug zu Fermionen auf K-AM.

## Start (Leitung, 2026-10-04 17:01:04 CEST)

- Spuren: cpu8 und cpu9 (neu seit 04.10., Finn: "mach weiter mehr plaetze").
- Ordner auf der .69: /home/fmh/fmhc-physics-remote/runde42-pachner-takt/ (code/, rauch/, lauf/).
