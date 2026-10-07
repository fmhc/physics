# Geometrie aus x-dimensionalen Bausteinen: Pruefuebersicht (Runde 27, Leitung)

- Leitung claude-primary, geschrieben ab 2026-10-03 05:14:01 CEST (date).
- Anlass: Finn ~05:12: "Check die Geometrie Sachen aus x dimensionalen Sachen" (Fortsetzung seiner Fragen "Punkte ->
  Striche -> Dreiecke -> Tetraeder" und "1+2+3+4+xD Teilchen in einer Ursuppe").
- Kennzeichen:
  - [M] exakte Mathematik, hier mit jq nachgerechnet
  - [S] an der Quelle gelesen (aus RUNDE-17/quellen-frustration/DOSSIER.md)
  - [E] eigene Rechnung des Projekts
  - [H] Hypothese

## 1. Grundzahl: Wie gut fuellen gleiche Simplexe den flachen Raum? [M; fuer 3D S, RUNDE-17]

Der Diederwinkel des regulaeren d-Simplex ist arccos(1/d). Um eine (d-2)-Flaeche passen n = 2 pi/arccos(1/d) Stueck.

| d | Diederwinkel | n flach | 5 bzw. floor | ceil |
|---|---|---|---|---|
| 2 (Dreiecke) | 60,000 Grad | **6 genau** | passt | passt |
| 3 (Tetraeder) | 70,529 Grad | 5,104 | 5 lassen **7,36 Grad** Luecke | 6 ueberlappen 63,2 Grad |
| 4 | 75,522 Grad | 4,767 | 4 lassen 57,9 Grad | 5 ueberlappen 17,6 Grad |
| 5 | 78,463 Grad | 4,588 | 46,1 Grad Luecke | 32,3 Grad Ueberlapp |
| 8 | 82,819 Grad | 4,347 | 28,7 Grad | 54,1 Grad |

- **Nur in 2D fuellen gleiche Simplexe den flachen Raum ohne Spannung.** In 3D fehlt bei 5 Tetraedern um eine Kante
  wenig (7,36 Grad, 2 %).
  - Diese Luecke schliesst sich exakt im positiv gekruemmten 3D-Raum S^3: Die 600-Zelle hat 5 Tetraeder je Kante, und
    jede Ecke hat 12 Nachbarn in Ikosaeder-Anordnung [S, RUNDE-17; L? Coxeter].
  - Ab 4D passt keine ganze Zahl gut.
- Ikosaeder (12 Kugeln um eine): Umkreis/Kante = sin(2 pi/5) = 0,9511, also passen die 12 aeusseren um 5,1 % nicht
  (Frank 1952) [M; S fuer Frank, RUNDE-17].

## 2. Was das Projekt dazu gerechnet hat (Stand heute)

| Ebene | Befund | Datei |
|---|---|---|
| 0D -> Graph | Eine Suppe mit lokalen Regeln ergibt keine Dimension (Klumpen K7, Flicken) | RUNDE-22/ursuppe-1 |
| Graph -> Dimension | Ein Beutel-Teilchen misst die spektrale Dimension (2/3, 3/4, 0,577 auf dem Sierpinski-Dreieck); auf dem Zufallsgraph entsteht kein Teilchen | RUNDE-24/bag-dim |
| 2D-Dreiecke | Kegelquelle E ~ R^2, Dipol log R, neutral endlich; Beulen baut 96 bis 99 % ab | RUNDE-22/winkelfeld-1 |
| 2D-Kugel | genau 12 Fuenfer-Ecken; gamma steuert rund gegen Ikosaeder | RUNDE-23/kugelschale-1 |
| 2D-Defekt mit Feldteilchen | Q-Ball haftet an Fuenfer-Ecken, Siebener stossen ab; exakte Formel auf 0,05 % | RUNDE-26/kegel-q |
| 3D-Tetraeder (Kontinuum) | Scharnierquelle mit Potenzabfall p ~ 2,4 bis 2,7 | RUNDE-22/winkelfeld-1 |
| 3D-Tetraeder (Staebe) | vorgebogenes Tetraeder: reine Eckmomente, kraftfrei, Kippen bei ~35 Grad | RUNDE-24/tetra-stab |
| 3D-Kette | Tetrahelix (Boerdijk-Coxeter): Defektspannung klingt in Dreierstufen ab, Faktor ~10 je drei Tetraeder | RUNDE-26/tetra-kette |
| 3D-Literatur | 30er-Ring der BC-Helix in der 600-Zelle; Eshelby: isotrope Ikosaeder-Klumpen koppeln in erster Ordnung nicht | RUNDE-17/quellen-frustration [S] |
| Gitter-Isotropie | Stille misst die Anisotropie (h^4 / h^8); die 12 Ikosaeder-Richtungen sind bis Ordnung 5 isotrop [L] | RUNDE-23/24 |
| 4D | Laufende Spin-2-Wellen gibt es erst in 4D (Regge/ART) [L]; CDT braucht 4D-Simplexe und Zeitschichten [L] | RUNDE-22/geometrie-stand |

## 3. Was daraus folgt [H]

1. **Die Bausteindimension entscheidet ueber die Spannung.**
   - 2D-Dreiecke bauen flachen Raum spannungsfrei; Kruemmung entsteht nur durch Defekte (5er/7er), die gequantelt und
     erhalten sind (Euler).
   - 3D-Tetraeder koennen den flachen Raum nicht spannungsfrei fuellen. Entweder ist der Raum positiv gekruemmt (S^3,
     600-Zelle) oder er enthaelt Defektlinien (Kanten mit 4 bzw. 6 Tetraedern, Frank-Kasper-Netze [L?]).
   - Ein 3D-Raum aus gleichen Tetraedern ist also von sich aus "gekruemmt oder verspannt".
2. **Defektlinien sind 3D-Strings.**
   - Eine Kante mit 5 Tetraedern traegt ein Defizit von 0,128 rad (7,36 Grad), wie eine Kegellinie.
   - Nach der KEGEL-Q-Abbildung (exakt fuer den zentrierten Ball) bindet ein Q-Ball schwach daran: Die Oberflaechenenergie
     sinkt um 1 - s^(-1/3) = 0,69 % mit s = 2 pi/(2 pi - 0,128) [M, Abbildung wie in 2D].
   - Q-Baelle in einem tetraedrischen 3D-Raum saessen also bevorzugt an den Fuenfer-Kanten.
3. **Kopplung:**
   - In 2D wirkt eine Netto-Winkelladung weit (E ~ R^2).
   - In 3D-Stabketten ist die Spannung abgeschirmt (TETRA-KETTE), und isotrope Ikosaeder-Klumpen koppeln in erster
     Ordnung gar nicht (Eshelby).
   - Weitreichende "Winkelspannung als Feld" gibt es also nur als Netto-Ladung (2D) oder als Kruemmung (Regge, 4D-Spin-2).
4. **Dimension:**
   - Aus der Suppe allein entsteht keine Dimension.
   - Wer sie misst, kann ein Teilchen sein (Beutel-Exponent = spektrale Dimension).
   - Wer sie festlegt, ist die Bauregel: CDT setzt 4D-Simplexe und Zeitschichten ein; flach spannungsfrei geht es nur in
     2D.

## 4. Naechste Tests (Vorschlag)

1. **FRUST-3D** (klein, mit dem Stabcode der TETRA-KETTE):
   - fuenf Tetraeder um eine Kante aus gleichen Staeben, also eine pentagonale Bipyramide mit 16 Staeben und 7 Ecken
   - als Stabwerk mit Gelenken (ein ueberzaehliger Stab, also eine Eigenspannung) und mit Einspannung
   - Wie viel Spannung kostet die 7,36-Grad-Luecke, und wie verteilt sie sich?
   - Erwartung [M]: Bei gleichen Ruhelaengen muesste die Achse 2 sqrt(1 - 1/(4 sin^2 36 Grad)) = 1,0515 lang sein, ist
     aber 1. Daraus folgt ein Fehlpass von 5 % mit Zug in der Achse und Druck im Ring bzw. umgekehrt.
2. **KEGEL-Q-3D:** Q-Ball an einer Fuenfer-Kante (Defizit 0,128 rad). Die Bindung von 0,69 % der Oberflaechenenergie
   numerisch pruefen; klein und billig mit der radialen Familie.
3. **600-ZELLE als Stabwerk in R^4:** spannungsfrei (alle Kanten gleich); in R^3 gezwungen ergibt sich ein Mass der
   3D-Frustration. Spaeter.

## Einfach gesagt

Dreiecke passen auf einer flachen Ebene perfekt zusammen, sechs um jede Ecke. Tetraeder koennen das im flachen Raum nicht:
Fuenf um eine Kante lassen eine kleine Luecke von gut 7 Grad, sechs ueberlappen. Ein Raum aus lauter gleichen Tetraedern ist
deshalb entweder gekruemmt, wie eine Kugeloberflaeche in einer Dimension mehr, oder er hat Fehlerlinien. Unsere Rechnungen
zeigen: In 2D wirken solche Fehler weit, in Tetraeder-Ketten nur in der Naehe, und Q-Baelle setzen sich gern an die
Fehlerstellen mit Luecke.
