# WINKELFELD-1: Ergebnis (Leitung, Runde 22, explorativ)

- Gerechnet von der Leitung auf der .69 (kleintest.sh, cpu3), Laeufe 20:41 bis 20:54 CEST, alle rc = 0.
- Karte: KARTE.md (20:30). Nachtrag und Plan eingefroren 20:40:58 (PLAN.md.eingefroren-20261002-204058).
- Code: code/winkelfeld.py (sha256 beginnt mit c4c7c4d1171aa9ae). Rohdaten in aus/.

## Ergebnis zuerst

1. **Eine Winkelladung ist eine echte Feldladung mit Fernwirkung, aber nur als Netto-Ladung.**
   - Kegelquelle (+60 Grad) in der flachen Scheibe: E ~ R^1,99 (R = 9 bis 24).
   - Neutrales Paar (+15/-15): E waechst logarithmisch (fester Zuwachs 0,0126 je ln R), Potenzfit-Exponent 0,46.
   - Neutrale Sechseck-Quelle: E konstant (0,0434 bis 0,0438).
   - Das ist genau die bekannte Defekt-Elastizitaet (Disklination R^2, Versetzung log R, neutraler Klumpen endlich;
     GEOMETRIE-STAND, Literatur). L4: schon bekannt; hier als Eichung unserer Werkzeuge.
2. **Verformen allein erzeugt keine Netto-Winkelladung (diskreter Gauss-Bonnet, Rauchlauf-Befund).**
   - Aendert man nur innere Ruhelaengen, bleibt die Summe der Fehlwinkel im Inneren null.
   - Eine Netto-Ladung braucht eine Topologie- oder Randaenderung, also einen fehlenden Baustein (Fuenfer-Ecke) oder
     einen Kegel.
3. **Gleichnamige Ladungen stossen sich weitreichend ab.** Zwei +15-Kegel (R = 24): E_int = 0,853 bei d = 2 bis 0,441
   bei d = 12, also bei halbem Scheibenradius noch 52 %. E_int > 0 und fallend: Abstossung.
4. **Der Stoff weicht durch Kruemmung aus.** Darf das Blatt beulen (kappa = 0,01), faellt die Energie der +60-Quelle
   gegenueber flach um 96 bis 99 % (R = 12: 1,76 -> 0,029; R = 24: 7,10 -> 0,065). Die Werte springen allerdings
   zwischen Nebenminima (0,026 bis 0,065, nicht monoton).
5. **3D: Eine einzelne Kantenquelle (Regge-Scharnier, netto neutral) wirkt wie ein Punktdefekt.**
   - Die Eigenenergie ist endlich (E(14)/E(12) - 1 = 0,06 %).
   - Die Kopplung zweier Quellen ist anziehend und faellt mit d^-2,41 (L = 16, d = 3 bis 6).
   - Nachtraeglich in der groesseren Box (L = 24, nicht gewertet): d^-2,73. Der Exponent haengt also an der Boxgroesse;
     zu erwarten waere asymptotisch ~3 (Eshelby).

## Vorab gegen Ausgang

| Nr | Vorhersage | Ausgang |
|---|---|---|
| W0 | F1: Exponent 1,7 bis 2,3 (80 %) | **eingetroffen**: 1,99 (Kleinste Quadrate, R = 9 bis 24). R = 6 und 9 waren aus dem Rauchlauf bekannt (Nachtrag) |
| W1 | F2: Exponent < 0,5 (75 %) | **eingetroffen**: 0,459; der Verlauf ist logarithmisch |
| W2 | F3: \|E_int(12)\| >= 0,5 \|E_int(2)\| (65 %) | **eingetroffen, knapp**: 0,517 |
| W3 | B1: Exponent < 1 fuer R >= 12 (70 %) | **eingetroffen formal**: 0,86. Die Werte springen zwischen Nebenminima, der Exponent ist schwach bestimmt; die Absenkung gegen flach (96 bis 99 %) ist eindeutig |
| W4 | D3: Eigenenergie < 5 % Aenderung (L 12 -> 14) **und** Kopplungsexponent >= 2,5 (60 %) | **nicht eingetroffen, knapp**: Eigenenergie 0,06 % (ja), Exponent 2,41 (nein) |

**Bedeutung (vorab festgelegt):**
- Der erste Fall (W0, W1 und W4) ist nicht vollstaendig ausgeloest, weil W4 fehlt.
- Der Fall "W4 trifft nicht ein" lautet: "Fernwirkung in 3D: Auch einzelne Kantenquellen tragen ein weitreichendes
  Winkelfeld". Er ist formal ausgeloest, aber **von den Zahlen nicht gedeckt**.
  - Die Eigenenergie ist endlich, die Kopplung faellt mit 2,4 (L = 16) bzw. 2,7 (L = 24).
  - Der Fehler liegt in der Karte: Zwischen "Exponent >= 2,5" und "weitreichend" fehlte eine Stufe.
  - Ich uebernehme die Deutung "Fernwirkung" nicht und ersetze auch keine Regel. Der Ausgang bleibt "W4 nicht
    eingetroffen"; die Deutung bleibt offen.
- W3 eingetroffen: Der Stoff loest Winkelspannung durch Kruemmung [H, im Modell; Literatur: Seung/Nelson, L?].

## Kontrollen

- K: Ohne Quelle gilt E < 1e-28 (flach), 1e-14 (beulend), 0 (Kuhn-Netz); eine Quelle der Staerke 0 ergibt 0.
- Gradienten am Ende <= 5e-9 (2D). lsqr in 3D mit istop = 2 ueberall.
- Zaehler ueberlappender Kanten (D3b): 0 fuer alle d.

## Latten (v3)

- L1: ja
- L2: teilweise (Kontrollen ohne Quelle; neutrale gegen geladene Quelle)
- L3: nein (kein zweites Gitter bzw. keine zweite Aufloesung, nur Boxgroessen)
- L4: ja, schon bekannt (Defekt-Elastizitaet)
- L5: nein

## Selbstanzeigen

- Die Sechseck-Quelle der Karte war falsch gebaut (netto neutral); im Rauchlauf gefunden und vor den echten Laeufen
  ersetzt.
- F2 und F3 wurden mit s = 15 statt 60 gerechnet (Ueberlagerung im linearen Bereich); im Nachtrag vor den Laeufen
  begruendet.
- B1 hat mehrere Nebenminima (zufaellige Startauslenkung); nur eine Saat je R.
- Der Arm zur groesseren Box (L = 24) ist nachtraeglich.

## Einfach gesagt

Wenn in einem Netz aus Dreiecken ein Dreieck fehlt, entsteht eine Spannung, die bis zum Rand reicht und mit der Groesse
des Netzes stark waechst. Zwei solche Stellen stossen sich ueber grosse Entfernungen ab. Darf sich das Netz aber woelben,
verschwindet fast die ganze Spannung: Es wird zu einem Kegel. Drueckt man die Dreiecke nur zusammen, ohne dass eins
fehlt, gleicht sich die Spannung von selbst aus und wirkt nur in der Naehe. Das alles kennt man aus der Physik der
Kristallfehler, unsere Werkzeuge messen es richtig.
