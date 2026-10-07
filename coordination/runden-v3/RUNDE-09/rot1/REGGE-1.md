# REGGE-1 (Runde 9, Karte der Leitung nach 10:13:41): Folgen die kreisenden Wirbelpaare einer Regge-Beziehung?

- Bearbeiter: Anthropic-Code-Agent (Opus 5.5), Fortsetzung von ROT-1. Explorativ (v3). Beginn 2026-09-30 10:16:59 CEST
  (date). Diese Vorab-Datei ist vor jedem neuen Lauf geschrieben; Kopie REGGE-1.md.eingefroren-<Zeit>.
- Finn: "und was ist wenn zwei baelle rotieren und damit was machen, damit bosonen oder quarks oder so entstehen?"
  Kein Anspruch auf Quarks, Mesonen oder QCD; Regge ist hier ein Vergleichsmassstab [H].

## 1. Was vorher schon bekannt ist (Offenlegung)

- Aus paardyn (ROT-1 ERGEBNIS 2.4, paardyn_grob_ergebnis.json) kenne ich:
  - Umlauffrequenz Omega und mittleren Abstand d fuer g = 0; 0,2; 0,5 und d_0 = 3, 5, 7, 9
  - bei g = 0,5: Omega < 0 (Uhrzeigersinn, gegen die Windung) und |Omega| d = 0,65 bis 0,77 bei d = 2,6 bis 7,4
- Nicht bekannt: Drehimpuls J und Energie E der Paarzustaende. paardyn hat keine Rohreihen gespeichert; J(t) und E(t)
  gibt es nur im Arbeitsspeicher des damaligen Laufs. Die Frequenzform ist also nicht blind, die J-E-Form schon.

## 2. Groessen

- Fenster um den S^2-Schwerpunkt wie in paardyn (Radius R_halb + 8). Mittel ueber t = 60 bis 250 (nach dem
  Einschwingen des eingepraegten Anfangszustands):
  - Q_w, J_w (um den Fensterschwerpunkt), E_w
  - j = J_w - Q_w: Drehimpulsdefizit gegen einen zentrierten gemischten m = 1-Wirbel gleicher Ladung (dort ist J = Q)
  - eps = E_w - omega_b Q_w (omega_b Ballfrequenz): entfernt den Beitrag kleiner Ladungsverluste in erster Ordnung
    (dE = omega dQ)
- Wirbelpaar wie paardyn: Abstand d(t) und Winkel phi(t) aus der Achter-Umlauf-Suche; Omega aus der Steigung von phi.
- Ball: Q = 700; rho_a = omega S_0 (Ladungsdichte je Komponente):
  - g = 0,5: omega 0,6317, S_0 1,1523, rho_a 0,7279
  - g = 0,2: omega 0,6920, S_0 1,0776, rho_a 0,7457
  - g = 0: omega 0,7271, S_0 1,0275, rho_a 0,7471

## 3. Die zwei Kandidaten mit Zahlen (g = 0,5; Kraft F = 2 sigma_Pol = 1,75, alternativ statische Steigung 0,97)

### 3.1 Magnus (masselose Wirbel im Kondensat, Kraft konstant) [Hand]

- Drehimpuls kinematisch: Ein Wirbel im Abstand b vom Zentrum traegt J_a = Q_a - (Ladung innerhalb b), also
  j = -(pi/4)(rho_1 + rho_2) d^2 = -(pi rho_a/2) d^2 = **-1,143 d^2**.
  - d = 3 / 5 / 7 / 9: j = -10,3 / -28,6 / -56,0 / -92,6
- Energie: eps = eps_0 + F d (Band), F zwischen 0,97 und 1,75.
- Hamilton-Beziehung fuer ein starr drehendes Paar: Omega = d eps/d j = -F/(pi rho_a d). Das Vorzeichen ist fest
  negativ, weil J mit d faellt, waehrend E steigt.
- J gegen E: j - j_0 = -(pi rho_a/(2 F^2)) (eps - eps_0)^2 = **-0,37 (Delta eps)^2** fuer F = 1,75 (-1,21 fuer F = 0,97).
  - Also ebenfalls quadratisch, aber **fallend**.

### 3.2 Regge (relativistischer rotierender String, masselose Enden)

- J = E^2/(2 pi sigma), E = pi sigma d/2, Enden mit Lichtgeschwindigkeit, Omega = +2/d.
  - sigma = 1,75: J = +0,687 d^2
  - d = 3 / 5 / 7 / 9: J = +6,2 / +17,2 / +33,7 / +55,6; Omega = 0,67 / 0,40 / 0,29 / 0,22
- J gegen E: +1/(2 pi sigma) = **+0,091 (Delta E)^2**, **steigend**.

### 3.3 Unterscheidung

- Vorzeichen von dJ/dE (bzw. dj/d(d^2)): Magnus negativ, Regge positiv.
- Betrag: Magnus -1,143 je d^2, Regge +0,687 je d^2.
- Frequenz: Magnus |Omega| d = F/(pi rho_a) = 0,42 bis 0,77, Regge 2. Die Frequenzform kenne ich schon (Abschnitt 1):
  0,65 bis 0,77. Sie ist deshalb kein Test mehr.
- Ableitbarkeit (Memory "vorab ableitbare Kennzahl"): Der kinematische Teil von j folgt schon aus der Lage der Wirbel.
  - Er prueft nur, ob der Zustand nach dem Einschwingen noch der eingepraegte ist.
  - Der dynamische Test ist die Hamilton-Probe Omega = Delta eps/Delta j: drei unabhaengig gemessene Groessen (Omega aus
    der Wirbelverfolgung, eps und j aus Feldintegralen).

## 4. Vorab-Erwartung (10:16:59 bis zur Kopie, vor jedem Lauf)

| Nr. | Erwartung | p |
|---|---|---|
| R1 | g = 0,5: j(d) linear in d^2, Steigung -1,14 +- 0,35 | 0,7 |
| R2 | g = 0,5: eps(d) steigt, Steigung zwischen 0,5 und 2,5 (Rauschen durch die Anfangsabstrahlung moeglich) | 0,5 |
| R3 | g = 0,5: Omega_H = Delta eps/Delta j zwischen Nachbarabstaenden ist negativ wie Omega, \|Omega_H/Omega\| zwischen 0,5 und 2 | 0,4 |
| R4 | Regge (J steigt mit E) wird verworfen | 0,9 |
| R5 | g = 0: j(d) ebenfalls fallend, Steigung -1,17 +- 0,5; eps(d) flach (\|Steigung\| < 0,3) | 0,4 |
| R6 | g = 0,2: wie g = 0,5 mit kleinerer eps-Steigung (0,3 bis 1,5) | 0,4 |

## 5. Scheiterregel (vorab)

- **Regge ist widerlegt**, wenn bei g = 0,5 j(d) mit d faellt: Steigung in d^2 negativ und mehr als drei
  Standardfehler von null. Die Frequenzform (\|Omega\| d = 2) ist schon verletzt (Abschnitt 1).
- **Magnus ist widerlegt**, wenn bei g = 0,5 eine der drei Bedingungen eintritt:
  - (i) die Steigung dj/d(d^2) liegt ausserhalb -1,143 +- 30 %
  - (ii) das Vorzeichen von Delta eps/Delta j ist nicht das von Omega, oder \|Omega_H\| weicht in der Mehrheit der
    Nachbarpaare um mehr als den Faktor 2 von \|Omega\| ab
  - (iii) eps(d) steigt nicht (Steigung <= 0)
- **Etwas anderes**, wenn beide scheitern.
- Nicht auswertbar, wenn die Paare in mehr als 30 % der Analysen fehlen oder die Energieabstaende kleiner sind als die
  Streuung der eps-Werte zwischen Wiederholungen.

## 6. Laeufe (vor der Rechnung festgelegt)

- Wiederholung von paardyn mit gespeicherten Reihen (sonst gleich: Q = 700, dx 0,3, dt 0,05, T = 250, keine Klammer, g
  von Anfang an).
- Abstaende d_0 = 3, 5, 7, 9 wie bisher, dazu **drei neue: 4, 6, 11**.
  - g = 0,5 und g = 0: alle sieben Abstaende
  - g = 0,2: d_0 = 3, 5, 7, 9
  - zusammen 18 Laeufe in einem Aufruf auf einer P4000-Spur
- Die Wiederholung der vier alten Abstaende ist noetig, weil J und E nicht gespeichert waren. Sie ist zugleich eine
  Reproduktionsprobe fuer Omega (Vergleich mit paardyn_grob_ergebnis.json).

## 7. Ergebnis (eingetragen ab 10:22:37 CEST, date; Lauf LAUF10 08:19:12 bis 08:20:59 UTC, rc = 0)

Quelle: lauf-69/ausgabe/regge_grob_ergebnis.json (laeufe[], auswertung["g"]); Bericht regge_grob_bericht.txt. Eine
Gitterstufe (dx 0,3) [num]; Rohreihen regge_grob_roh.pt auf der .69.

### 7.1 Kurz

1. **Regge ist widerlegt.**
   - J faellt mit E, statt zu steigen: bei g = 0,5 j - j_min = -0,268 +- 0,023 (Delta eps)^2, Regge verlangt +0,05 bis
     +0,16.
   - j faellt mit d^2: Steigung -1,60 +- 0,26, also 6 Standardfehler unter null (Scheiterregel Regge erfuellt).
   - Die Enden laufen nicht mit Lichtgeschwindigkeit: \|Omega\| d = 0,64 bis 0,75 statt 2, Endgeschwindigkeit ~0,33.
   - Der Drehsinn ist gegen die Windung festgelegt, nicht frei.
2. **Qualitativ ist das Paar Magnus-artig.**
   - Die Umlauffrequenz geht wie 1/d: \|Omega\| d = 0,647 / 0,656 / 0,638 / 0,704 / 0,716 / 0,751 bei d = 2,45 bis 7,01,
     auf +-10 % konstant, jetzt mit den neuen Abstaenden d_0 = 4 und 6.
   - \|Omega\| d^2 waechst dagegen um den Faktor 3,3.
   - Die Hamilton-Probe hat das richtige Vorzeichen: Omega_H = Delta eps/Delta j ist in allen 5 Nachbarpaaren negativ wie
     Omega. \|Omega_H/Omega\| = 1,67 / 1,75 / 1,31 / 2,32 / 1,41 (4 von 5 innerhalb Faktor 2).
3. **Quantitativ nach der Scheiterregel: Magnus bei g = 0,5 formal widerlegt**, durch Bedingung (i).
   - Die Steigung dj/d(d^2) ist -1,60 +- 0,26 gegen den Soll-Bereich -1,143 +- 30 % = [-1,49; -0,80]; knapp ausserhalb,
     0,4 Standardfehler jenseits der Grenze.
   - Bei g = 0,2 besteht dieselbe Bedingung (-1,044 +- 0,045 gegen -1,171).
   - Da auch Regge scheitert, lautet der Ausgang nach dem Wortlaut der Regel **"etwas anderes"**.
   - Der Befund dahinter [num]: j entspricht dem kinematischen Wert des **eingepraegten** Abstands d_0 (Verhaeltnis 0,78 /
     1,12 / 0,99 / 1,01 / 0,90 / 0,92 fuer d_0 = 3, 4, 5, 6, 7, 9).
   - Die verfolgten Wirbel ruecken aber zusammen (d(t >= 60)/d_0 = 0,82 / 0,96 / 1,01 / 1,01 / 0,88 / 0,78). J bleibt
     erhalten, der Abstand nicht; die feste Kopplung J(d) des reinen Zwei-Wirbel-Magnus-Bildes gilt nach dem
     Einschwingen nicht mehr.
   - [H] Der Drehimpuls-Rest steckt in Ball und Wandlinse.
4. **Die Energie ist durch den ungeglaetteten Start verunreinigt.**
   - eps(d) steigt mit 3,20 +- 0,48 je Laenge (g = 0,5) bzw. 1,50 +- 0,18 (g = 0,2).
   - Das ist steiler als die Bandkraft aus der Umlauffrequenz (1,5 bis 1,7) und aus der statischen Rechnung (0,97).
   - Die Abstrahlung am Anfang waechst mit d (E geschluckt 21 / 25 / 36 / 47 / 59 / 76 bei g = 0,5). Die Restanregung im
     Ball waechst vermutlich ebenso [H].
   - Deshalb ist \|Omega_H\| systematisch 1,3- bis 2,3-mal zu gross. Eine saubere Hamilton-Probe braucht einen
     entspannten Start (Klammer-Relaxation, dann loslassen); nicht gerechnet.
5. **Reproduktion und Kontrollen:**
   - Die vier alten Abstaende reproduzieren paardyn in d(t >= 30) und Omega(t >= 30) auf alle gedruckten Stellen,
     z. B. g = 0,5, d_0 = 5: 5,153 / -0,12525.
   - d_0 = 11 (g = 0,5) und d_0 = 9 (g = 0,2): Paar in 97 % bzw. 69 % der Analysen verloren, Ball stark zerlegt
     (Q_w 196 bzw. 606 von 700). Beide nach Regel nicht gewertet.
   - g = 0 (kein Band): Omega > 0 (+0,027 bis +0,046), eps faellt leicht (-0,22 +- 0,015 je Laenge).
     - j passt zum eingepraegten Abstand auf 0 bis 4 % (z. B. d_0 = 11: -139,4 gegen -142,0).
     - Die verfolgte Nullstelle liegt deutlich innen (d = 7,7). Bei g = 0 raeumt psi_1 Bereiche, die Nullstelle ist
       dort nicht der Ort der Zirkulation.

### 7.2 Vorab gegen Ausgang

| Nr. | Vorab | Ausgang | Bewertung |
|---|---|---|---|
| R1 | g = 0,5: j linear in d^2, Steigung -1,14 +- 0,35 | -1,60 +- 0,26 (Fitrest 12,5) | verfehlt (knapp) |
| R2 | g = 0,5: eps steigt, Steigung 0,5 bis 2,5 | 3,20 +- 0,48 | verfehlt (zu steil) |
| R3 | Omega_H negativ wie Omega, \|Omega_H/Omega\| in [0,5; 2] | 5/5 negativ; 4/5 im Bereich | getroffen (Mehrheit) |
| R4 | Regge verworfen | J faellt mit E (-0,268 +- 0,023) | getroffen |
| R5 | g = 0: j faellt mit -1,17 +- 0,5; eps flach | -2,33 +- 0,26 gegen den verfolgten Abstand; eps -0,22 | teilweise |
| R6 | g = 0,2: wie 0,5, eps-Steigung 0,3 bis 1,5 | j -1,04 +- 0,045; eps 1,499 | getroffen |

### 7.3 Scheiterregel (Abschnitt 5) nach Wortlaut

- Regge: widerlegt (j faellt mit 6 Standardfehlern).
- Magnus bei g = 0,5:
  - (i) eingetreten: Steigung ausserhalb +-30 %
  - (ii) nicht eingetreten: Vorzeichen gleich, Mehrheit innerhalb Faktor 2
  - (iii) nicht eingetreten: eps steigt
  - also widerlegt nach Regel (i)
- Ausgang: **"etwas anderes"**. Inhaltlich: Magnus-artige Bewegung (Kraft konstant, Omega ~ 1/d, Drehsinn fest,
  J faellt mit E). Die Zuordnung J(d) des idealen Zwei-Wirbel-Systems gilt aber nicht, weil Ball und Wandlinse
  Drehimpuls aufnehmen.

### 7.4 Was das fuer Finns Frage heisst [H]

- Die kreisenden Paare liegen nicht auf einer Regge-Linie. Ihre Enden (Wirbelkerne) haben keine Traegheit. Die Bandkraft
  schiebt sie seitwaerts (Magnus), statt sie zu beschleunigen.
- Deshalb dreht ein kuerzeres Paar schneller, und mehr Energie im Band bedeutet weniger Drehimpuls.
- Eine Regge-artige Beziehung J ~ +E^2 braeuchte Enden mit Masse, die das Band auf nahezu Lichtgeschwindigkeit bringt;
  hier sind es 0,3.
- Kein Hinweis auf "Mesonen"; die Analogie reicht bis "Band mit fester Spannung", nicht bis zum Spektrum.

### 7.5 Rechenzeit und Verfahren

- Rechenzeit: 18 Laeufe, Entwicklung 102 s (P4000, Spur p4000a, sofort frei).
- Code: rot1.py Unterbefehl regge (Stand 644277ec auf der .69 = lokal); Rauchtest lokal 10:18:56 bis 10:19:00.
- Keine nachtraegliche Aenderung von Fenster, Fit oder Ausschlussregel. d_0 = 11 und g = 0,2 / d_0 = 9 fallen nach der
  vorab festgelegten Fehlt-Regel (> 30 %) heraus.
