# LADUNG-MONOPOL-2: Wird ein geladenes Teilchen am Monopol auch auf Finns Pyrochlor-Netz zu Spin 1/2? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 06:49:28 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - LADUNG-MONOPOL-1 (kubisch): Ladung 1 gibt am Gitter-Monopol immer ein Dublett (Spin 1/2), Ladung 2 ein Triplett.
    Kommutatorzeichen (-1)^q; die Ordnung haelt bis zur Schwelle.
  - Teil B des Dossiers (RUNDE-37/ladung-monopol-l/DOSSIER.md, Abschnitt 9): dasselbe auf dem Pyrochlor-Kanten-Netz von
    FLUSS-1, Monopol in einem Tetraeder (Punktgruppe T_d).
  - Projektsuche (grep nach Kaefig, Adamantan, Monopol und Diamant): keine Vorarbeit zu Monopolen auf diesem Netz.
- **Schreibtisch [M]:**
  - Netz wie FLUSS-1 Netz A: Knoten sind die Pyrochlor-Ecken (6 Kanten je Knoten), das Pfeilfeld liegt auf den Kanten.
  - Flaechen sind die Dreiecke der Tetraeder und die Sechsecke der Kagome-Ebenen. Zellen sind die Tetraeder und die
    abgestumpften Tetraeder.
  - Ein Einheitsmonopol in der Mitte eines Tetraeders gibt je Dreieck den Fluss Omega/2 = pi/2.
  - Die Doppelgruppe von T_d hat zwei 2-dim (E_1/2, E_5/2) und eine 4-dim Darstellung (F_3/2).
  - Unten kann also auch ein Quartett liegen; die Vorhersage kann scheitern.
  - Die drei 180-Grad-Drehungen (Wuerfelachsen durch die Tetraedermitte) gehoeren zu T_d. Fuer ungerades q ist das
    Kommutatorzeichen -1 (umschlossener halber Fluss, wie in LADUNG-MONOPOL-1); das ist vorab ableitbar.
- Kennzeichen: [M] Mathematik, [L] Literatur, [H] Hypothese.

## Test (Code-Agent)

- **Gitter:** offene Box aus L^3 kubischen Zellen des Pyrochlor-Gitters (16 Ecken je Zelle), L in {3, 4, 5} oder nach
  Laufzeit. Monopol in einem Tetraeder nahe der Mitte.
- **Fluss:** Phi_p = Omega_p/2 je Flaeche, mit Omega_p dem Raumwinkel vom Monopol aus. Sechsecke sind nicht eben; fuer
  jedes Sechseck dieselbe Faecherflaeche auf beiden Seiten verwenden.
  - Pruefung: Fluss null durch jede geschlossene Zelle, ausser der Monopolzelle (2 pi).
- **Eichfeld und Hamilton:** Peierls-Phasen per lsqr mit Dirac-String; H = -sum (e^{i q A} c^+ c + h.c.) - V0 sum_{4
  Ecken des Monopol-Tetraeders} n_i, q in {0, 1, 2}; V0-Raster und Schwelle wie LADUNG-MONOPOL-1.
- **Messgroessen:** wie LADUNG-MONOPOL-1 (Entartung, Kommutatorzeichen der zwei 180-Grad-Drehungen, Schwellen,
  Groessenvergleich).
  - Dazu die Darstellung der tiefsten Stufe: E_1/2, E_5/2 oder F_3/2, per Charakter der 120-Grad-Drehung.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| LP0 | Kontrolle: q = 0 tiefste gebundene Stufe einfach; Fluss durch jede Zelle <= 1e-12 ausser der Monopolzelle (2 pi); Spektrum unabhaengig von der String-Richtung auf 1e-10 | 90 % |
| LP1 | Kontrolle: q = 1: Kommutatorzeichen -1 auf allen Stufen, jede Stufe gerade entartet; q = 2: +1 | 90 % |
| LP2 | [H] q = 1, groesstes L, jedes V0 ueber der Schwelle: tiefste gebundene Stufe genau 2-fach (Dublett), nicht 4-fach (Quartett F_3/2) | 60 % |
| LP3 | [H] q = 2, gleiche Bedingungen: tiefste gebundene Stufe genau 3-fach (Triplett) | 55 % |
| LP4 | Tief gebundene Eigenwerte bei den zwei groessten L auf 1e-6 gleich | 80 % |

**Bedeutung (vorab):**
- **LP2 trifft ein:** Auch auf Finns Tetraeder-Netz wird ein spinloses geladenes Teilchen am Monopol zum
  Spin-1/2-Dublett. Der Ladung-Monopol-Weg zu Spin 1/2 traegt dann im Fluss-Eis selbst (Einteilchenbild).
- **LP2 verfehlt (Quartett unten):** Die Tetraeder-Geometrie stellt die Ordnung um. Dann ist das tiefste Objekt ein
  Spin-3/2-artiges Quartett; beschreiben, ab welchem V0 oder L das Dublett unten liegt.
- In beiden Faellen bleiben Austauschstatistik und Monopole des Quanten-Eises offen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (geteilt; der Starter wartet auf den Lock); je
  <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 90 min.
