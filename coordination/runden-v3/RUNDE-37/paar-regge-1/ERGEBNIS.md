# PAAR-REGGE-1: Ergebnis (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:23:05 CEST; Text dieser Datei ab 18:40:54 CEST
  (beides date). Zeitbox 60 min.
- Grundlage: KARTE.md, gluon-paar-l/DOSSIER.md Abschn. 6 (bindend), PLAN.md (eingefroren in zwei Stufen,
  EINGEFROREN-SHA256.txt).
- Kennzeichen: [E] gerechnet auf der .69, [M] von Hand (nicht gegengelesen), [S] an der Quelle gelesen, [P]
  Projektdatei, [L] Gedaechtnis, [H] Hypothese, [F] Festlegung des Plans, [D] Diagnose ohne Urteil.
- Alle Massen in Einheiten sqrt(sigma); sigma_A = 9/4 sigma, wenn nicht anders gesagt.

## 1. Ergebnis zuerst

1. **Das Modell traegt die Gitter-Trajektorie in keinem Datensatz [E].** Gemeint ist der rotierende String mit zwei
   gleichen Endmassen und festem Intercept (a = 0 oder 1/12).
   - (A): chi^2 = 371 bzw. 202, p <= 1e-45.
   - (B), Hauptlesart: chi^2 = 70 bzw. 67, p ~ 1e-16.
   - PR1 und PR2 sind nicht eingetroffen, nach Plan und nach Kartenwortlaut.
2. **Es scheitert am festen Intercept, nicht an der Endgeschwindigkeit [E, M].**
   - Endmassen machen den Zustand bei festem J schwerer; in allen Fits waechst E(2) mit m [E].
   - Das Gitter-2++ (4,894(22)) liegt schon unter dem masselosen Wert: 5,317 bei a = 0, 5,205 bei a = 1/12. Fuer (A) ist
     die beste Endmasse deshalb 0.
   - (B) verlangt Intercept 0,93(24) bei Steigung 0,281(22). Die besten Modellsekanten liegen bei Intercept -0,58 bis
     -0,07 und Steigung 0,41 bis 0,44.
3. **Endgeschwindigkeit:** Im Hauptfall (9/4) liegt v_end(2) nirgends im Band [0,70; 0,82], wo zugleich p >= 0,05 gilt.
   - Hauptlesart: v_end(2) = 0,89 bis 0,93 (B), 1 (A, masselos).
   - Lesart R2: 0,75 bis 0,76, aber p ~ 3e-7.
   - Nur die lose Lesart R1 (Bandbreite je Punkt, Korrelation weggelassen) laesst (B) zu: p = 0,09 bis 0,10,
     v_end(2) = 0,85 bis 0,88, m = 0 innerhalb 1 sigma ("masselos").
   - Mit der Casimir-Variante 2,14 erreicht R1 das (a)-Band knapp: v_end(2) = 0,815, p = 0,079.
4. **PR0 nicht eingetroffen: Die Dossier-Handrechnung hat ein falsches Kraftgleichgewicht [E, M].**
   - Masselos 5,3174 ist bestaetigt. "Konstantes v = 3/4: 6,80" nicht: Die bindende Endmassenformel [P] gibt 6,331.
   - Das Dossier rechnet mit sigma_A = gamma m v^2/R. Die [P]-Formel hat sigma_A sqrt(1 - v^2) = gamma m v^2/R.
   - Der erste Hauptsatz dE/dJ = omega haelt fuer [P] auf 3,5e-9. Die Dossier-Form verletzt ihn um bis zu 26 %.
   - Der Sonderfall "konstantes v" liegt deshalb bei 0,71 (B) und 0,83 (A), nicht bei 0,77 und 0,93.
   - Auch mit der Dossier-Form traegt (B) nicht (Diagnose: p ~ 1e-8).
5. **2+1D, nur beschreibend:** Die 2+1D-Gerade passt gut (p = 0,72 und 0,83).
   - Die Enden sind dort schwer (m ~ 1,6), v_end(2) ~ 0,66, v_end(4) ~ 0,73.
   - Das J = 0 dieser Geraden kann das klassische Modell nicht abbilden.
   - Dass v_end(4) nahe 3/4 liegt, ist eine Beobachtung nach der Rechnung, ohne Band und ohne Urteil.

## 2. Urteilstabelle

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut |
|---|---|---|---|---|
| PR0 | Kontrollen masselos 5,32 und konstantes v = 3/4 6,80 auf 1e-3 reproduziert | 90 % | **nicht eingetroffen.** Masselos 5,31736 (relativ 5,0e-4: ja). Konstantes v = 3/4: 6,3307 (relativ 6,9e-2: nein) | **nicht eingetroffen.** Relativ wie nach Plan; absolut verfehlt auch 5,32 (2,6e-3, Rundung der Karte) |
| PR1 | [H] Datensatz (B): Band "(a) traegt" | 30 % | **nicht eingetroffen.** R3: "traegt nicht" (p = 5,7e-17 und 2,7e-16) | **nicht eingetroffen** unter allen drei Lesarten: R1 "masselos" (v_end(2) 0,88/0,85), R2 "traegt nicht", R3 "traegt nicht" |
| PR2 | [H] Datensatz (A): Band "(a) traegt" | 10 % | **nicht eingetroffen.** "traegt nicht" (p = 1,3e-82 und 7,2e-46; bestes m = 0) | **nicht eingetroffen** (nur eine Lesart) |

Bedeutung nach der Vorab-Regel der Karte ("Beide verfehlt"): In diesem Modell traegt die "3/4" als Endgeschwindigkeit
die Gitterdaten nicht. Entscheidend ist dabei der feste Intercept, nicht die Groesse von v (Abschn. 8).

## 3. Fit-Tabelle [E]

Hauptfall: sigma_A = 9/4 sigma, Endmassenformel [P], ein freier Parameter m, 1 Freiheitsgrad je a. Das
1-sigma-Intervall gilt fuer Delta chi^2 <= 1. Band je Datensatz und Lesart (Regel PLAN Abschn. 5).

| Datensatz, Lesart | a | m/sqrt(sigma) (1 sigma) | chi^2 | p | v_end(2) | v_end(4) | E(2); E(4) | Band |
|---|---|---|---|---|---|---|---|---|
| (A) A&T 2020 | 0 | 0,000 [0; 0,007] | 370,77 | 1,3e-82 | 1,000 | 1,000 | 5,317; 7,520 | traegt nicht |
| (A) A&T 2020 | 1/12 | 0,000 [0; 0,008] | 202,11 | 7,2e-46 | 1,000 | 1,000 | 5,205; 7,441 | (dto.) |
| (B) MT, R3 (Plan) | 0 | 0,258 [0; 0,607] | 70,08 | 5,7e-17 | 0,928 | 0,948 | 5,448; 7,631 | traegt nicht |
| (B) MT, R3 (Plan) | 1/12 | 0,413 [0; 0,716] | 67,03 | 2,7e-16 | 0,886 | 0,918 | 5,469; 7,665 | (dto.) |
| (B) MT, R1 | 0 | 0,444 [0; 0,807] | 2,797 | 0,094 | 0,880 | 0,913 | 5,608; 7,767 | masselos |
| (B) MT, R1 | 1/12 | 0,544 [0; 0,885] | 2,717 | 0,099 | 0,854 | 0,894 | 5,598; 7,775 | (dto.) |
| (B) MT, R2 | 0 | 1,005 [0,497; 1,413] | 26,83 | 2,2e-7 | 0,761 | 0,820 | 6,249; 8,327 | traegt nicht |
| (B) MT, R2 | 1/12 | 1,067 [0,583; 1,467] | 26,07 | 3,3e-7 | 0,746 | 0,809 | 6,227; 8,324 | (dto.) |

- Daten: (A) 4,894(22), 7,60(12). (B) Punkte der MT-Geraden 4,8913 und 8,2853. Bandbreite je Punkt (R1): 0,581 und
  0,458; Korrelation der beiden Punkte 0,90 (R2). R3 rechnet direkt mit s = 0,281(22) und a0 = 0,93(24).
- Sekanten der besten Fits (s, a0): R3 (0,440; -0,080) und (0,436; -0,075). R1 (0,435; -0,177) und (0,432; -0,152).
  R2 (0,415; -0,578) und (0,412; -0,541).
- Delta chi^2 bei m = 0: (A) ~ 0; (B) R3 0,13 und 0,61; R1 0,53 und 0,97; R2 2,36 und 2,84.
- In jedem Fit hat das m-Gitter hoechstens ein lokales Minimum.

**Casimir-Varianten (beschreibend) [E]:**

| Datensatz, Lesart | sigma_A/sigma | a = 0: m, chi^2, p, v_end(2) | a = 1/12: m, chi^2, p, v_end(2) | Band |
|---|---|---|---|---|
| (A) | 2,14 | 0; 180,8; 3,3e-41; 1 | 0; 77,0; 1,7e-18; 1 | traegt nicht |
| (A) | 2,36 | 0; 629,8; 5,5e-139; 1 | 0; 394,8; 7,4e-88; 1 | traegt nicht |
| (B) R3 | 2,14 | 0,492; 85,5; 2,3e-20; 0,866 | 0,603; 81,9; 1,4e-19; 0,837 | traegt nicht |
| (B) R3 | 2,36 | 0; 57,1; 4,1e-14; 1 | 0,137; 54,5; 1,5e-13; 0,961 | traegt nicht |
| (B) R1 | 2,14 | 0,616; 3,16; 0,075; 0,837 | 0,700; 3,08; 0,079; 0,815 | **(a) traegt** |
| (B) R1 | 2,36 | 0,235; 2,45; 0,117; 0,935 | 0,365; 2,38; 0,123; 0,900 | masselos |
| (B) R2 | 2,14 | 1,193; 30,1; 4,1e-8; 0,723 | 1,248; 29,3; 6,2e-8; 0,710 | traegt nicht |
| (B) R2 | 2,36 | 0,801; 23,7; 1,1e-6; 0,805 | 0,874; 23,0; 1,6e-6; 0,787 | traegt nicht |

- Hauptauswertung (A; B mit R3): bei allen drei Spannungen "traegt nicht", also robust gegen Casimir +-5 %.
- In der Lesart R1 haengt das Band an der Spannung: 9/4 "masselos", 2,14 "(a) traegt" (knapp: v_end(2) = 0,815,
  p = 0,079), 2,36 "masselos". Das R1-Urteil ist also nicht robust.

## 4. Kontrollen [E] (Lauf vor dem Code-Freeze, Code unveraendert)

| Kontrolle | Karte/Dossier | [P]-Formel | Dossier-Kraftgleichgewicht [D] |
|---|---|---|---|
| K1 masselos, J = 2, a = 0 | 5,32 | 5,317362; Grenzwert m = 1e-8: gleich auf 1e-12; Laenge 1,505 | (gleich, m = 0) |
| K2 konstantes v = 3/4, J = 2, a = 0 | 6,80; Laenge 1,04; Endmasse 1,37 | **6,3307**; Laenge 1,220; Endmasse 1,067 | 6,8007; 1,039; 1,375 |
| K2 Steigung bei festem v = 3/4 | 0,272 | 0,3135 | 0,2717 |
| K3 dE/dJ = omega (m = 1, eta 0,1 bis 3) | - | max. Abweichung 3,5e-9 | max. Abweichung 0,26 |
| K4 Sonderfall konstantes v, (B) Steigung 0,281 | v ~ 0,77 | 0,706 | 0,765 |
| K4 Sonderfall konstantes v, (A) Sekante 0,3717 | v ~ 0,93 | 0,834 | 0,941 |

- Herleitung [M] (PLAN Abschn. 1): Aus dL/dR = 0 fuer L = -2 sigma_A Int sqrt(1 - omega^2 r^2) dr - 2 m sqrt(1 -
  omega^2 R^2) folgt sigma_A sqrt(1 - v^2) = gamma m v omega. Das ist die [P]-Form; Sonnenschein/Weissman 2014 [L].
- Die Dossier-Form hat keinen masselosen Grenzfall. Bei v -> 1 bleibt die Endenergie 2 m gamma endlich, und die
  Steigung geht gegen 0,377 statt 4/9 (K4-Tabelle in lauf-69/kontrollen.json).

## 5. Nachtrag 2+1D (beschreibend, ohne Urteil) [E]

MT-Gerade Gl. (5): s = 0,384(16), a0 = -1,144(71); Lesart R3; sigma_A = 9/4 sigma; a = 0 und a = (D - 2)/24 = 1/24 [F].

| a | m/sqrt(sigma) (1 sigma) | chi^2 | p | v_end(2) | v_end(4) | E(2); E(4) | Delta chi^2 (m = 0) |
|---|---|---|---|---|---|---|---|
| 0 | 1,627 [1,557; 1,697] | 0,132 | 0,72 | 0,662 | 0,735 | 7,125; 9,111 | 274 |
| 1/24 | 1,673 [1,602; 1,742] | 0,046 | 0,83 | 0,654 | 0,729 | 7,144; 9,137 | 293 |

- Die Punkte der 2+1D-Geraden bei J = 2 und 4 sind 7,172 und 9,174 [E].
- Die fuehrende 2+1D-Trajektorie enthaelt das 0++ (MT Z. 248-249 [S]). Klassisch hat J = 0 die Energie 2 m ~ 3,3; das
  Gitter-0++ liegt bei 4,368 (Dossier-Ankertabelle [S]). Das Modell beschreibt also nur den Teil ab J = 2.
- Der Unterschied zu 3+1D liegt im Intercept. In allen Fits liegt der Sekanten-Intercept unter a und sinkt mit m [E].
  So ist -1,144 mit Masse erreichbar, +0,93 in keinem Fit.

## 6. Diagnose: Fits mit dem Kraftgleichgewicht des Dossiers [D]

| Datensatz | a | m | chi^2 | p | Sekante (s; a0) |
|---|---|---|---|---|---|
| (A) | 0 / 1/12 | 0 | 370,8 / 202,1 | 1,3e-82 / 7,2e-46 | wie [P] (masselos) |
| (B) R3 | 0 | 4e-11 (Grenzwert m -> 0+) | 34,13 | 5,1e-9 | 0,377; 0,000 |
| (B) R3 | 1/12 | 7e-11 (Grenzwert m -> 0+) | 31,56 | 1,9e-8 | 0,377; 0,083 |

- Mit der Dossier-Form traegt (B) ebenfalls nicht. Der Befund haengt also nicht an der Formelwahl.
- Das beste "m" der Dossier-Form liegt bei m -> 0+. Das ist nicht der masselose String (Delta chi^2 bei m = 0 betraegt
  36). Hier zeigt sich wieder, dass dieser Form der masselose Grenzfall fehlt.

## 7. Bild

![J gegen M^2](BILD-J-gegen-M2.png)

- Datei: BILD-J-gegen-M2.png (= lauf-69/paar-regge-1-v2.png). Links (A), rechts (B).
- Gezeigt: Daten, masselose Gerade (a = 0), Gerade mit festem v = 3/4 ([P], Steigung 0,314), beste Fits a = 0 und
  1/12 (B: R3 durchgezogen, R1 strichpunktiert).
- Gezeichnet mit code/bild2.py, nach dem Freeze geschrieben (Selbstanzeige 1). Das Bild des eingefrorenen Codes
  (lauf-69/paar-regge-1.png) zeigt die (A)-Fits nicht.

## 8. Bedeutung und Grenzen

- **Was traegt [E]:** In allen Fits mit festem Intercept 0 oder 1/12 liegt E(2) mindestens beim masselosen Wert (5,317
  bzw. 5,205). Das Gitter-2++ liegt darunter. Die fuehrende 3+1D-Trajektorie braucht einen hohen Intercept: MT
  0,93(24); fuer (A) mit masselosen Enden etwa 0,31 [M, Dossier]. Endmassen senken den Sekanten-Intercept weiter.
- **Fuer Lesart (a) "Enden mit 3/4 c":** In diesem Modell nicht gestuetzt. Die Werte von v_end ergeben sich aus dem
  Versuch, die Intercept-Luecke zu schliessen; sie messen keine Gluon-Geschwindigkeit.
- **Nicht geprueft:** freier Intercept (dann 2 Parameter, 0 Freiheitsgrade bei zwei Punkten); Quantisierung mit
  Endmassen; Spin und Helizitaet; J = 6.
- **Grenzen:**
  - klassisch bei J = 2 bis 4;
  - die 4++-Zuordnung ist unsicher (A&T: Stern, "likely");
  - die (B)-Fehler haengen an der nicht angegebenen Korrelation von s und a0;
  - Casimir-Skalierung ist nur bis ~1 fm belegt;
  - die Gitterdaten sind synthetisch (reine Eichtheorie), keine Messung der Natur;
  - Look-elsewhere fuer jede 3/4 (Dossier Abschn. 5.5).

## 9. Selbstanzeigen

1. **Bildfehler im eingefrorenen Code:**
   - Was: Der Bildmodus von paar_regge.py zeichnet die Kurven ueber ein festes eta-Fenster. Bei m ~ 1e-8 (beste
     (A)-Fits) liegt die ganze Kurve am Ursprung; die (A)-Fits fehlen im ersten Bild.
   - Behebung: code/bild2.py, geschrieben nach dem Freeze und nach der Sicht auf die Fits. Es dient nur der Darstellung
     und rechnet die Kurven mit den eingefrorenen Modellfunktionen aus fits.json nach.
   - Folge: Auswertung und Baender sind unberuehrt. Das erste Bild liegt unveraendert in lauf-69/.
2. **Sicht vor dem Freeze:**
   - Von Hand [M] habe ich vor dem Kontrolllauf K2 (6,331) und K4 (0,71/0,83) gerechnet. Dazu kam der masselose
     chi^2-Wert fuer (B) unter R1 (~3,1) und R3 (~70).
   - Die Wahl von R3 als Hauptlesart fiel nach dieser Sicht. Offengelegt in PLAN Abschn. 11; R1 und R2 sind voll
     mitgerechnet und gehen in das Wortlaut-Urteil ein.
   - Kleiner Rechenfehler [M]: Die Handschaetzung ~3,1 weicht vom gerechneten Wert ab. Gerechnet ist chi^2(m = 0) unter
     R1 3,33 (2,797 + 0,529).
3. **Projekt-grep moeglicherweise ueber verbotene Pfade:**
   - Die Suche nach "regge-anschluss" lief per grep -r ueber coordination/ und model-lab/.
   - Ausgeschlossen waren vertraege-20260925, ks-1-dk-lauf, ks-1-dk-laeufe, Dateien *VERSIEGELT* und T8-SOLL-*.
   - Nicht ausgeschlossen waren weitere KS-1-Ergebnispfade und Ordner mit VERSIEGELT im Namen. grep kann deren Inhalt
     maschinell gelesen haben; angezeigt wurde daraus nichts, KS-1-Treffer habe ich aus der Liste gefiltert.
4. **Werkzeuge ausserhalb der Liste:**
   - Lokal: ls, cat, find, wc, mkdir, cp, mv, date, dazu die Lese- und Schreibwerkzeuge des Agenten. Kein python,
     awk oder perl, keine Rechnung auf dem Laptop.
   - .69 ausserhalb des Starters: mkdir, mv, ls, cat, sha256sum, uptime. Fuer numpy/scipy/matplotlib habe ich
     site-packages gelistet und eine .pth-Datei gelesen; python habe ich dafuer nicht gestartet.
   - Den Farbpruefer des dataviz-Skills (node) habe ich nicht laufen lassen. Benutzt ist dessen dokumentierte
     Standardpalette.
5. **Plan nach Stufe 1 ergaenzt:** PLAN.md bekam nach dem Kontrolllauf den Nachtrag 12. Das war im Plan vorgesehen; die
   Kopie von Stufe 1 liegt unveraendert daneben.
6. **Ungeprueft an einer Quelle:** a = (D - 2)/24 [L]; die Sonnenschein/Weissman-Randbedingung [L]. Fuer [P] spricht
   K3 [E].
7. **Festlegungen ueber die Karte hinaus [F]:**
   - Lesarten R1, R2, R3 und R3 als Hauptlesart;
   - "mindestens ein a" fuer die Baender;
   - viertes Etikett "uebrig";
   - relative Lesart von "1e-3" bei PR0;
   - a = 1/24 in 2+1D.

## 10. Laeufe (alle .69, kleintest.sh, Spur cpu11, 1 Thread, rc = 0; Zeiten UTC aus den Logs)

| Lauf | Inhalt | Start bis Ende | Rechenzeit |
|---|---|---|---|
| pr1kontr | Kontrollen K1 bis K4, Budget | 16:35:07 bis 16:35:28 | 0,2 s |
| pr1fits | 30 Fits (eingefrorener Code) | 16:35:55 bis 16:36:13 | 15,8 s |
| pr1bild | Bild aus dem eingefrorenen Code | 16:36:20 bis 16:36:23 | 1,2 s |
| pr1bild2 | Bild aus code/bild2.py (nach dem Freeze) | 16:38:07 bis 16:39:06 | 4,4 s CPU (58 s Laufzeit der Unit) |

## 11. Dateien

- PLAN.md; PLAN.md.eingefroren-stufe1-20261004-183459; PLAN.md.eingefroren-stufe2-20261004-183551;
  EINGEFROREN-SHA256.txt.
- code/paar_regge.py (+ .eingefroren-stufe2-20261004-183551); code/bild2.py (nach dem Freeze, nur Bild).
- lauf-69/: kontrollen.json/.log, fits.json/.log, bild.log, bild2.log, paar-regge-1.png (erstes Bild),
  paar-regge-1-v2.png, PRUEFSUMMEN.txt (lokal und .69 gleich).
- BILD-J-gegen-M2.png.
- .69: /home/fmh/fmhc-physics-remote/paar-regge-1/ (code/, lauf/).

## 12. Einfach gesagt

Finns Idee: Zwei Teilchen haengen an einem Gummiband, drehen sich umeinander, und ihre Enden laufen mit drei Vierteln
der Lichtgeschwindigkeit. Wir haben nachgerechnet, ob so ein drehendes Paar die Massen der Glueballs auf der
wichtigsten Linie (Drehimpuls 2 und 4) aus grossen Computerrechnungen trifft. Das klappt nicht, und es liegt nicht an
der 3/4: Schon ohne jede Endmasse ist das Paar mit Drehimpuls 2 im Modell zu schwer, und jede Endmasse macht es noch
schwerer. Ausserdem steckte im Vorschlag ein Formelfehler: Am schnellen Ende zieht das Band schwaecher, als dort
angenommen. Deshalb kommt bei 3/4 die Zahl 6,33 heraus, nicht 6,80.

## Zeitbox

- Start 2026-10-04 18:23:05 CEST; Abgabe 2026-10-04 18:43:38 CEST (date, beim Schreiben dieser Zeile gemessen), also innerhalb der 60 min.
