# Tetraeder: Bestandteile, Analogien, was folgt (Analyse der Leitung, Runde 34)

- Leitung claude-primary, geschrieben ab 2026-10-03 18:00:25 CEST (date).
- Anlass: Finn ~17:58: "mach weiter und ueberleg noch mal zu unseren ideen von den tetraeder-bestandteilen und analogien
  dazu, bzw analyse der tetraeder".
- Kennzeichen:
  - [E] eigene Rechnung des Projekts, mit Fundort
  - [M] exakte Mathematik
  - [L] Lehrbuch oder bekannte Literatur, nicht neu gelesen
  - [L?] aus dem Gedaechtnis, vor Verwendung an der Quelle pruefen
  - [H] Hypothese oder Deutung der Leitung

## 1. Was wir an Tetraedern gerechnet haben

| Wann | Was | Ergebnis | Fundort |
|---|---|---|---|
| 01.10. | Federtetraeder (Codex, Papier) | vier Massen, sechs Federn: innere Moden omega^2 = (k/m){4; 1,1; 2,2,2}, also Atmung, Verdrillung (doppelt), Biegung (dreifach); lokal stabil; kleine Atmung macht die Form parametrisch instabil (Rate 3\|eps\| sqrt(k/m)/4); ein flaches K4-Federnetz steigt von selbst in die dritte Dimension | resonance-20260930/concept-review-tus/TETRAEDER-20261001.txt |
| 02.10. | Tetraederketten "11+1"/"19+1" aus Finns Buendel | Schnittzaehlregel P = T3 + 2 T4 + 2 C stimmt; 12 und 20 Ecken sind in Steifigkeit, Feldklumpen, LJ-Bindung und Schnittstatistik nicht besonders; 11 Schritte ergeben fast 4 Umlaeufe | RUNDE-16 (TETRAKETTE-1, tetra-chain/EINORDNUNG.md) |
| 02.10. | STABIL-6-8-12 | stabil sind 6 in der Ebene und 12 (+1) im Raum; 8 ist nirgends besonders; 19 ist magisch (Doppel-Ikosaeder), 11 anti-magisch | RUNDE-16/stabil-6-8-12 |
| 02.10. | Frustrationsliteratur | 30er-Ring der Tetrahelix in der 600-Zelle [S]; isotrope Ikosaeder-Klumpen koppeln in erster Ordnung nicht (Eshelby) | RUNDE-17/quellen-frustration |
| 02.10. | Winkelfeld | 2D: Kegelquelle E ~ R^2 (weitreichend); 3D-Scharnierquelle faellt mit Potenz p ~ 2,4 bis 2,7 | RUNDE-22/winkelfeld-1 |
| 03.10. | TETRA-STAB | vorgebogene Staebe: reine Eckmomente, kraftfrei; Kippen bei ~35 Grad | RUNDE-24 |
| 03.10. | TETRA-KETTE | Defektspannung faellt in Dreierstufen, Faktor ~10 je drei Tetraeder | RUNDE-26 |
| 03.10. | GEOMETRIE-XD, FRUST-3D | nur in 2D fuellen gleiche Simplexe spannungsfrei; fuenf Tetraeder um eine Kante schliessen 7,36 Grad durch Biegen, mit Symmetriebruch | RUNDE-27 |
| 03.10. | ICO-STAB | Franks Ikosaeder aus Knicklichtern wird schief (Zentrum 0,06 L, 2 % Energiegewinn), wie vorhergesagt | RUNDE-29 |
| 03.10. | KEGEL-XD | Q-Baelle haften an Fuenfer-Defekten jeder Dimension, nur kurzreichweitig (von Laue: int T_ij = 0) | RUNDE-27 bis 29 |
| 03.10. | Meiri/Efrati 2025 | triangulierte Ketten schirmen ab; Fernwirkung braucht eine weiche Schermode | RUNDE-27 [S] |

## 2. Analyse: Woraus ein Tetraeder besteht

- **Bestandteile:** 4 Ecken, 6 Kanten, 4 Flaechen, 1 Zelle; V - E + F = 2 [M].
  - Das Tetraeder ist selbstdual: Ecken <-> Flaechen.
  - Die 6 Kanten bilden 3 Paare gegenueberliegender, windschiefer Kanten. Ihre Mittelpunkte legen drei zueinander
    senkrechte Achsen fest: Das Tetraeder sitzt so im Wuerfel, dass seine Kanten Flaechendiagonalen sind [M].
- **Symmetrie** [M]:
  - volle Gruppe T_d (24 Elemente) = alle Vertauschungen der 4 Ecken (S4)
  - Drehgruppe T (12) = A4
  - Ihre Doppelueberlagerung in SU(2) ist die binaere Tetraedergruppe 2T (24 Einheitsquaternionen). Sie hat
    Spinor-Darstellungen und bildet die Ecken der 24-Zelle in 4D [L].
  - McKay-Zuordnung: 2T <-> E6, binaere Ikosaedergruppe 2I <-> E8 [L].
- **Steifigkeit** [M]:
  - Als Gelenkwerk ist ein Tetraeder genau bestimmt: 3V - 6 = 6 = E. Es hat keine Eigenspannung, also keine
    Laengen-Frustration in einem einzelnen Tetraeder.
  - Spannung entsteht nur ueber Winkel (Vorbiegung, Einspannung, TETRA-STAB) oder ueber das Zusammenfuegen mehrerer
    Tetraeder (FRUST-3D, ICO-STAB).
- **Packung** [M, S]:
  - Diederwinkel 70,53 Grad; fuenf um eine Kante lassen 7,36 Grad.
  - Geschlossen wird das nur im gekruemmten Raum (600-Zelle, 2I) oder mit Defektlinien (Frank-Kasper-Netze).
- **Kette** [M, E]: Boerdijk-Coxeter-Helix, Drehung je Tetraeder arccos(-2/3) = 131,8 Grad. Diese Drehung ist kein
  rationaler Teil von 360 Grad, die Kette hat also keine Periode. Fast-Rueckkehr nach 4/11 und 11/30 Umlaeufen; der
  30er-Ring schliesst exakt erst in der 600-Zelle.
- **Schwingungen** [E, Codex]: Die sechs inneren Moden zerfallen nach der Symmetrie in A1 (Atmung), E (2) und T2 (3).
  Das ist dasselbe Muster wie beim Methanmolekuel [L].

## 3. Analogien, nach Tragweite fuer unsere Fragen

1. **Spin-Eis: Teilchen und Fernkraft aus einer Regel je Tetraeder** [L]:
   - Auf dem Pyrochlor-Gitter (eckenverknuepfte Tetraeder) gilt je Tetraeder die Eisregel "zwei Spins rein, zwei raus".
   - Das ist ein divergenzfreies Feld, also eine emergente Magnetostatik (Coulomb-Phase).
   - Verletzungen der Regel (drei rein, einer raus) verhalten sich wie magnetische Monopole und ziehen sich mit 1/r an
     (Castelnovo, Moessner, Sondhi, Nature 2008).
   - Im Quanten-Spin-Eis entsteht zusaetzlich ein masseloses "Photon" (Hermele, Fisher, Balents, PRB 2004).
   - **Lehre fuer uns [H]:** Fernwirkung aus Tetraedern entsteht durch eine Erhaltungsregel je Tetraeder, nicht durch
     Steifigkeit. Unsere Stab-Tetraeder sind steif und schirmen deshalb ab (TETRA-KETTE, Meiri/Efrati); Q-Baelle haften
     nur kurzreichweitig (KEGEL-XD).
2. **Fraktonen: Spin-2-aehnliche Moden aus Tensor-Regeln** [L]:
   - Gitterregeln, die ein symmetrisches Tensorfeld erhalten, ergeben gravitonaehnliche Moden und eine Art
     Mach-Prinzip (Pretko, PRD 2017).
   - Sie sind nicht Lorentz-invariant und umgehen so das Weinberg-Witten-Verbot emergenter masseloser Spin-2-Teilchen
     [L].
   - **Bezug [H]:** genau die schwaechsten Glieder unserer Spin-2-Kette, 10 (Eindeutigkeit) und 7 (Spin >= 3). Ein
     emergentes Spin-2 aus Tetraederregeln waere ein Gegenbeispiel-Kandidat zur Eindeutigkeit, aber nur ohne
     Lorentz-Invarianz.
3. **A4 und drei Familien** [L]:
   - Die Drehgruppe des Tetraeders A4 ist die bekannteste diskrete Flavor-Symmetrie. Drei Leptonfamilien als A4-Triplett
     erklaerten die tribimaximale Neutrinomischung (Ma/Rajasekaran 2001, Altarelli/Feruglio 2005).
   - Seit theta_13 != 0 (2012) braucht das Korrekturen [L].
   - **Analogie [H]:** drei Familien <-> drei Kantenpaar-Achsen des Tetraeders. Nur eine Zuordnung, keine Ableitung.
4. **Spin 1/2 nur ueber Topologie** [L, H]:
   - Ein starrer Koerper aus bosonischen Bausteinen bleibt bosonisch, auch mit Tetraedersymmetrie.
   - Halbzahliger Spin entsteht bei Solitonen ueber die Topologie des Feldraums (Finkelstein-Rubinstein). Das Skyrmion mit
     Baryonenzahl 3 hat Tetraedersymmetrie und ist als Fermion quantisierbar [L?: Braaten/Townsend/Carson 1990].
   - Das passt zu unserer Notiz "Spin 1/2 mit der unveraenderten Formel unmoeglich" (Q-Baelle sind nicht topologisch).
     Der Weg fuehrt ueber einen topologischen Feldraum (S^3 oder Codex' C x S^2), nicht ueber Stab-Tetraeder.
5. **Chemie und Materialien** [L]:
   - sp3-Bindung (Methan, Diamant), Eis (Tetraeder-Netz der Wasserstoffbruecken), Silikate (SiO4)
   - Frank-Kasper-Phasen, Quasikristalle, metallische Glaeser mit ikosaedrischer Nahordnung
   - Tetraeder sind in der Natur der haeufigste Baustein lokaler Ordnung im Raum, gerade weil sie den Raum nicht
     spannungsfrei fuellen (Frank 1952).
6. **Spektren mit Tetraedersymmetrie** [L]: Die Rotationsniveaus von Methan zerfallen nach den Symmetriesorten A, E, F
   mit verschiedenen Kernspin-Gewichten. Eine Symmetrie des Bausteins erzeugt so diskrete "Sorten" im Spektrum.

## 4. Was daraus fuer unsere Ideen folgt [H]

1. **Als mechanische Bausteine** (Staebe, Federn, Knicklichter) liefern Tetraeder lokale Physik: abgeschirmte Spannung,
   Symmetriebruch verspannter Cluster, Haftung von Q-Baellen an Fuenfer-Stellen. Eine Fernkraft entsteht so nicht, durch
   unsere Rechnungen gut gestuetzt.
2. **Fernkraft** braucht eine Erhaltungsregel je Tetraeder (Spin-Eis-Weg). Eine skalare Regel ergibt Coulomb-Kraft und
   Photonen, eine Tensor-Regel spin-2-aehnliche Moden (Fraktonen). Das ist der aussichtsreichste Weg von "Tetraeder-Ursuppe"
   zu "Kraeften", und er ist in der Festkoerperphysik erprobt.
3. **Spin 1/2** braucht Topologie, nicht Geometrie allein. Die Tetraedersymmetrie hilft dann bei der Form (B = 3), nicht
   beim Spin.
4. **Die Zahlen 6, 12 (+1), 19, 30** sind Geometrie: Packung, magische Cluster, der Ring in der 600-Zelle. Neue
   Teilchenzahlen folgen daraus nicht (STABIL-6-8-12, TETRAKETTE-1).
5. **Drei Familien <-> A4** ist eine bekannte, aber geschwaechte Analogie. Sie lohnt nur mit einer konkreten Vorhersage.

## 5. Vorschlaege fuer kleine Tests (Karten erst nach Finns Wahl)

- **EIS-1 (Kopplung vor Bauteil):**
  - Klassisches Spin-Eis auf einem kleinen Pyrochlor-Gitter (Monte Carlo, <= 10 min) mit zwei festgehaltenen Defekten.
  - Die freie Energie gegen den Abstand sollte ~ 1/r folgen (Literaturwert als Kontrolle).
  - Dann unsere Variante: eine Winkel- oder Volumenregel je Tetraeder in einem Stabnetz statt Spins. Erzeugt sie
    Fernwirkung zwischen zwei Defekten, oder schirmt das Netz weiter ab?
  - Neu ist nur die zweite Haelfte.
- **TETRA-ATMUNG:** Codex' vorhergesagte parametrische Forminstabilitaet des Federtetraeders (Rate 3\|eps\| sqrt(k/m)/4)
  numerisch pruefen, dazu ob Winkelsteifigkeit sie verstimmt. Nahe an Codex' Rechnung; klein.
- **TETRA-SKYRMION (Schreibtisch):** Traegt die Gesamtformel, erweitert um einen topologischen Feldraum (Codex' C x S^2),
  einen Soliton mit Tetraedersymmetrie und Fermion-Quantisierung? Zuerst Literatur zu B = 3 an der Quelle lesen.
